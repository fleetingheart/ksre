label de_H21:

scene bg school_scienceroom onlayer master
with locationchange

play music music_normal fadein 3.0

"Ich wache auf, nehme meine Pillen, dusche, schlüpfe schnell in meine Uniform, esse ein leckeres Frühstück, schnappe mir meine Tasche und gehe los, so wie ich es jeden Tag mache."


"Erst als ich im Klassenzimmer ankomme, wird mein Tag aus der Bahn geworfen."


"Nachdem ich mich gesetzt habe, sehe ich zu, wie meine Klassenkameraden während der nächsten Stunde langsam eintreffen, bis schließlich jeder Platz besetzt ist – bis auf Hanakos."


stop music fadeout 10.0

$ ksgallery_unlock("evul hanako_emptyclassroom")
scene evbg hanako_emptyclassroom onlayer master:
    truecenter
    subpixel True zoom 0.9
    easein 20.0 zoom 1.0
show evfg hanako_emptyclassroom onlayer master:
    truecenter
    subpixel True zoom 0.8
    easein 20.0 zoom 1.0
with whiteout

"Ich werde mich nie daran gewöhnen, dass sie hin und wieder einfach nicht zum Unterricht auftaucht. Jetzt ist es sogar noch besorgniserregender, weil Lilly nicht da ist."


"Während Mutou weiter schwafelt, werfe ich immer wieder einen Blick auf ihren Platz, als ob sie jeden Moment dort auftauchen könnte. Niemand sonst scheint sich an ihrer Abwesenheit zu stören, aber sie haben auch kaum einen Grund dazu."


"Dass Hanako nicht im Unterricht ist, ist immerhin völlig normal. Oder zumindest war es das. So viel ich gesehen habe, hat sie, seit ich hier bin, nicht so oft gefehlt, aber vorher war sie offenbar viel seltener anwesend."


"Ihre Abwesenheit fällt auch auf einen ungewöhnlichen Zeitpunkt. Es ist der Tag vor ihrem Geburtstag, und nachdem sie im Unterricht zusammengebrochen ist, weil wir diesen angesprochen haben, wirkt das für mich verdächtig."


"Ein großer Teil meiner Gedanken dreht sich darum, wie ich ihr helfen könnte, aber letzten Endes habe ich das Gefühl, dass ich nichts tun kann."


scene bg school_scienceroom onlayer master
with silentwhiteout
play sound sfx_normalbell

"Die Mittagsglocke ertönt und reißt mich aus meinen Gedanken. Ein kollektives Seufzen ist von der erleichterten Klasse zu hören, auch wenn Mutou ziemlich verärgert wirkt."


"Schließlich mag er es nicht, während seiner aufregenden Vorlesungen unterbrochen zu werden."


"Gerade als ich überlege, was ich in der Mittagspause machen soll, jetzt wo Hanako und Lilly nicht da sind, präsentiert sich die Lösung von selbst."


show shizu invis onlayer master:
    tworight
    xpos 0.8
show misha invis onlayer master:
    twoleft
    xpos 0.2
with None

show shizu behind_blank onlayer master at tworight
show misha hips_grin onlayer master at twoleft
with dissolvecharamove

play music music_shizune fadein 5.0

mi "Tag, Hicchan~!"


show shizu adjust_happy onlayer master
with charachange

shi "…"


hi "Tag Misha, Shizune. Ihr beide seht so strahlend aus wie immer."


show shizu basic_normal2 onlayer master
with charachange

shi "…"


show misha sign_smile onlayer master
with charachange

mi "Shicchan wollte wissen, ob du heute mit uns Mittagessen willst~."


hi "Klar. Ein wenig Gesellschaft kann nie schaden."


scene bg school_cafeteria onlayer master
show crowd onlayer master
with locationskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 1.0

"Die Cafeteria brummt vor Aktivität, ähnlich wie die meiner alten Schule. Die Yamaku ist allerdings anders in der Hinsicht, wie… zivilisiert der Ansturm zur Mittagspause abläuft."


"Wo man erwarten würde, dass ein wilder Mob mit den Hufen scharrt, um zur Essensausgabe zu kommen, steht stattdessen eine saubere und ordentliche Schlange."


"Es gibt ein bisschen Gedrängel, und die Leute in der Schlange strecken oft ihren Kopf, um zu sehen, was vorne vor sich geht, aber es läuft recht dezent ab."


"Das liegt ohne Zweifel an den sehr strengen Regeln dieser Schule, was diese Angelegenheiten betrifft. Die gleiche Disziplin ist zu beobachten, wenn sich Schüler durch die Flure und das restliche Schulgelände bewegen."


"Obwohl die Gründe dafür vielleicht etwas beunruhigend sind, habe ich die Ordnung, die in dieser Schule durchgesetzt wird, zu schätzen gelernt."


show shizu behind_smile onlayer master:
    tworight
    ypos 1.1
show misha perky_smile onlayer master:
    twoleft
    ypos 1.1
with charaenter

hide crowd onlayer master
with charaexit

$ renpy.music.set_volume(0.4, 7.0, channel="ambient")

"Allerdings hat es mir nicht wirklich gefallen, dass Shizune und Misha mich geschickt haben, um ihr Essen zu holen. Ich fühle mich etwas ausgenutzt, als ich mich an ihren Tisch setze und ihr Essen vor ihnen auf den Tisch fallen lasse."


"Yakisoba-Brot und Erdbeermilch für Misha, eine Schüssel Ramen und Saft für Shizune. Erleichtert seufze ich, als ich es absetze, nachdem ich solche Schwierigkeiten hatte, es noch zusätzlich zu meiner eigenen Portion zu tragen."


show misha hips_grin onlayer master
with charachange

mi "Danke~!"


show shizu behind_smile onlayer master
with charachange

"Misha klatscht in die Hände, bevor sie die Verpackung aufplatzen lässt und sich mit Heißhunger auf das Brot stürzt. Shizune nickt einfach nur dankbar, bevor sie ihre dampfenden Nudeln einmal umrührt und zum Kühlen darauf pustet."


"Ich mache meine eigene Mahlzeit auf – auch eine Portion Yakisoba-Brot – nehme einen Bissen und spüle es mit etwas Saft hinunter. Das Brot ist sehr süß – so sehr, dass ich mich zwingen muss, es hinunterzuschlucken, um es hinter mich zu bringen."


"Nach der Hälfte unterbreche ich diese schwierige Aufgabe und frage, was mir auf dem Herzen liegt."


hi "Also… ich schätze, ihr zwei hattet einen Grund, mich hierher zu schleppen? Immerhin scheint ihr Zwei immer einen Hintergedanken zu haben."


show misha sign_confused onlayer master
with charachange

mi "Waf fagft du da, Hiffan~! Bir hawen kein Hinfergemanken~."


show shizu basic_angry onlayer master
with charachange

"Ihr Mund ist voller Yakisoba-Brot, als sie spricht. Ein ziemlich unerfreulicher Anblick. Shizune schaut ein bisschen angeekelt und wendet sich dann wieder ihren Nudeln zu."


show shizu basic_normal onlayer master
show misha perky_smile onlayer master
with charachange

"Bevor ich wieder etwas sage, warte ich, bis Misha den Inhalt ihres Mundes heruntergeschluckt hat."


hi "Ihr wollt mir nicht Honig ums Maul schmieren, damit ich euch nach Schulende bei der Arbeit helfe?"


show misha hips_smile onlayer master
with charachange

mi "Nope!"


hi "Ihr wollt keine Informationen aus mir herausholen, die ich vielleicht nicht preisgeben will?"


show misha cross_smile onlayer master
with charachange

mi "Nööö!"


hi "… Also gut. Ihr habt gewonnen. Ihr wolltet dann wohl einfach nur mit jemandem essen, der so intelligent und gutaussehend ist wie ich."


show misha cross_grin onlayer master
with charachange

mi "Das ist es, Hicchan~! Jetzt hast du's~!"


"Nachdem Misha mit dem Übersetzen fertig ist, macht Shizune ein unbeeindrucktes Gesicht und saugt den letzten Rest einer langen Nudel ein, während sie uns mit ihren Händen ihre Gedanken mitteilt."


show shizu behind_blank onlayer master
with charachange

shi "…"


show misha sign_smile onlayer master
with charachange

mi "Shicchan sagt, du sollst uns gegenüber nicht so misstrauisch sein~. Immerhin tut sie nur ihre Pflicht als Klassensprecherin~."


hi "Wie tut sie… ääh… wie tust du das?"


"So sehr ich es hasse, das zuzugeben, aber ich habe offenbar immer noch Probleme, mich mit Shizune zu verständigen."


"Eigentlich müsste ich nur Augenkontakt mit ihr halten und sie ansprechen anstatt Misha, aber wenn jemand anderes für sie redet, ist das eine überraschend schwierige Aufgabe."


show shizu basic_normal2 onlayer master
with charachange

shi "…"


show misha hips_smile onlayer master
with charachange

mi "Es ist die Aufgabe des Klassensprechers, dafür zu sorgen, dass im Unterricht alle gut abschneiden, oder~?"


hi "Nicht… wirklich…"


hi "Warte. Inwiefern sollte, euch das Essen zu holen, dazu führen, dass ich im Unterricht besser mitkomme?"


show shizu adjust_frown onlayer master
with charachange

"Shizune schnaubt und richtet missbilligend ihre Brille."


show shizu behind_frown onlayer master
with charachange

shi "…"


show misha cross_frown onlayer master
with charachange

mi "Das ist also der Dank dafür, dass wir dir beim Mittagessen Gesellschaft leisten?"


$ renpy.music.set_volume(0.0, 3.0, channel="music")

"Das ist überhaupt keine Antwort auf meine Frage. Warte mal…"


hi "Woher wusstet ihr, dass ich…?"


show shizu basic_normal onlayer master
with charachange

shi "…"


show misha sign_smile onlayer master
with charachange

mi "Lilly ist weg, und Hanako ist abwesend, und da die Zwei die einzigen sind, mit denen du Zeit verbringst…"


show shizu adjust_smug onlayer master
with charachange

shi "…"


show misha cross_smile onlayer master
with charachange

mi "Es war dir auch regelrecht anzusehen…"


$ renpy.music.set_volume(1.0, 3.0, channel="music")

"Autsch. Das könnte schon sein, aber sie muss es mir ja nicht unter die Nase reiben. Vielleicht ist das die Rache für vorhin."


hi "Verstehe. Na ja, danke. Ich weiß es zu schätzen, und das ist nicht sarkastisch gemeint."


show shizu basic_normal onlayer master
show misha perky_smile onlayer master
with charachange

"Die Zwei nicken, und wir machen uns wieder an unser Essen. Es ist etwas beschämend, mit ihnen zusammen zu sein, nur weil sie bemerkt haben, dass ich einsam bin, aber es ist ja nicht so, als würden wir uns nicht kennen."


"Es dauert nicht lange, bis ich den letzten Rest meines Brotes aufgegessen habe und ansetze, meinen Saft leerzutrinken. Als ich das tue, erinnere ich mich an den Gedanken, den ich hatte, bevor die beiden mich unterbrochen haben."


"Ich habe das Gefühl, der Einzige in der Klasse zu sein, der in irgendeiner Weise Kenntnis nimmt, dass Hanako nicht da ist. Dieses Gefühl hatte ich die anderen Male auch, als sie den Unterricht geschwänzt hat, aber jetzt irritiert es mich noch mehr."


"Kümmert es keinen, ob sie glücklich ist oder nicht? Haben sie einfach jede Möglichkeit abgeschrieben, ihr zu helfen?"
"Selbst Mutou versucht nicht, sie vom Schwänzen abzuhalten, und ich bin von seiner Begründung immer noch nicht ganz überzeugt."


show misha perky_smile onlayer master
with charachange

mi "Hey Hicchan, ist dein Saft abgelaufen?"


hi "Was?"


show misha hips_grin onlayer master
with charachange

mi "Du hast so ein komisches Gesicht gemacht, so ungefähr~."


show misha perky_confused onlayer master
show shizu adjust_happy onlayer master
with charachange

"Als ob es nötig wäre, macht Misha meinen Gesichtsausdruck nach. Bei ihrer übertriebenen Darstellung verziehe ich das Gesicht. Allerdings hat Shizune wenigstens ein wenig Spaß daran."


hi "Ich habe nur über Hanako nachgedacht."


show misha hips_smile onlayer master
with charachange

mi "Oh?"


show shizu basic_happy onlayer master
with charachange

"Mishas Interesse ist geweckt, und Shizunes auch, sobald für sie übersetzt wurde."


hi "Ich mache mir nur Gedanken darüber, dass sie so oft abwesend ist. Und zwar besonders jetzt, wo sie bald Geburtstag hat."


show misha perky_sad onlayer master
show shizu behind_sad onlayer master
with charachange

"Die Erinnerung daran, was im Unterricht passiert ist, ist noch ganz frisch in ihren Köpfen. Allein ihre Gesichter sprechen Bände."


hi "Wisst ihr irgendwas über Hanako? Irgendwas, das vielleicht hilft?"


show misha perky_confused onlayer master
show shizu behind_blank onlayer master
with charachange

"Misha zuckt mit den Schultern und schaut zu Shizune, die eine Weile darüber nachdenkt."


show shizu basic_normal2 onlayer master
with charachange

shi "…"


show misha perky_smile onlayer master
with charachange

mi "Die Einzigen, mit denen sie je mehr als ein oder zwei Sätze gewechselt hat, sind du und Lilly."


"Shizune kann Lillys Namen zwar nicht auf spöttische Weise sagen, aber ich habe das Gefühl, als ob es in ihren Gebärden mitschwingt. Die Wirkung ist nach Mishas Übersetzung allerdings verloren."


show shizu behind_blank onlayer master
with charachange

shi "…"


show misha sign_smile onlayer master
with charachange

mi "Dank der Unterlagen, die in unserer Funktion als Schülerrat durch unsere Hände gehen, gibt es ein paar Dinge, die wir über Hanako wissen, aber darüber dürfen wir nichts sagen."


hi "Verständlich."


"Klingt ziemlich nach der „ärztlichen Schweigepflicht” von Doc. Jedes Mal, wenn ich jemanden finde, der etwas über Hanakos Vergangenheit weiß, stellt es sich als Sackgasse heraus."


"Der einzige Weg, es jemals herauszufinden, ist, sie zu fragen. Ich weiß nicht, ob sie mir solche Sachen anvertrauen würde, aber um ihretwillen muss ich es wenigstens versuchen."



show shizu adjust_happy onlayer master
with charachange

shi "…"


show misha hips_smile onlayer master
with charachange

mi "Mach dir keine Gedanken darüber, Hicchan~. Schließlich passiert das jedes Jahr~."


"Das beruhigt mich auch nicht wirklich. Ich fühle mich wegen dem, was im Unterricht passiert ist, immer noch ein bisschen schuldig, aber ich habe das Gefühl, dass mehr dahinter steckt, auch wenn sie das nicht aussprechen."


show misha perky_confused onlayer master
show shizu behind_blank onlayer master
with charachange

"Misha bemerkt mein sorgenvolles Gesicht, und ihr eigenes, für gewöhnlich fröhliches und beruhigendes Gesicht wirkt auf einmal traurig."


mi "Jeder hat Probleme, mit denen er sich rumschlagen muss, oder nicht, Hicchan?"


hi "Ja. Ich wünschte nur, ich könnte Hanako bei ihren mehr helfen."


"Damit findet unser Gespräch ein bedrückendes Ende."


stop music fadeout 4.0

show misha hips_grin onlayer master
with charachange

"Schließlich gelingt es Misha mit ihrer fröhlichen und quirligen Art, die Stimmung wieder zu heben, doch meine Gedanken sind weiterhin bei Hanako."


"Später werde ich nach ihr sehen."


stop ambient fadeout 1.0

scene bg school_dormhallway onlayer master
with shorttimeskip

"Nachdem ich meine Schultasche abgelegt habe, vergewissere ich mich, dass meine Tür abgeschlossen ist."


"Im Wohnheim ist es still. Mutou hat mich länger in Anspruch genommen als erwartet."
"Nach dem Unterricht hat er mit mir über meine Studienpläne gesprochen und mir ein paar Arbeitsblätter für Hanako in die Hand gedrückt, fast als wäre es ihm gerade noch eingefallen."


"Völlig in Gedanken bemerke ich den Schatten, der vor mir auftaucht, erst sehr spät. Ein Blick nach oben offenbart mir seinen Besitzer."


show kenji happy onlayer master at center
with charaenter

play music music_kenji fadein 0.5

ke "Hey, Mann. Hab dich eine ganze Weile nicht gesehen."


hi "Oh. Hi."


show kenji tsun onlayer master
with charachange

ke "Was ist denn das für eine Antwort?"


"Meine geistesabwesende Begrüßung verärgert ihn offensichtlich. Wahrscheinlich würde ich genauso reagieren."


hi "Entschuldige, ich muss nur gerade über vieles nachdenken."


ke "„Nachdenken” ist eine schlechte Ausrede dafür, den gerechten Krieg nicht zu unterstützen."


hi "Und wie läuft der Krieg?"


show kenji neutral onlayer master
with charachange

ke "Meine Vorbereitungen laufen. Im Moment brauche ich finanzielle Unterstützung für diese Vorbereitungen."


hi "Wenn du willst, dass ich dir Geld leihe, sag's einfach."


show kenji happy onlayer master
with charachange

ke "Nein Mann, schon okay."


hi "Schon… okay? Du willst mein Geld nicht?"


show kenji tsun onlayer master
with charachange

ke "Hey Mann, schau nicht so überrascht. Das kränkt mich."


show kenji neutral onlayer master
with charachange

ke "Ich bin ziemlich groß in der Bowling-Szene, aber gestern hab ich ein paar Leute gefunden, die das nicht wussten."


hi "Ich bin mir ziemlich sicher, dass Wetten gegen die Schulregeln verstößt…"


show kenji tsun onlayer master
with charachange

ke "Schulregeln sind unwichtig; wir befinden uns im Krieg. Die Leute von heute haben kein Verständnis dafür, was Krieg bedeutet."


hi "Wozu brauchst du denn das Geld, wenn ich fragen darf?"


show kenji neutral onlayer master
with charachange

ke "Haltbare Lebensmittelkonserven. Baumaterialien; hauptsächlich Wellblech und Holzplatten. Erste-Hilfe-Ausrüstung. Campingkocher. Tragbares Radio. Schlafsack. Taschenlampe. Mechanische Uhr."


"Zuerst kommt es mir vor wie eine willkürliche Auswahl an Gegenständen und Materialien, aber nach ein paar Sekunden macht es klick."


hi "Ist das nicht eine Materialliste für einen Atomschutzbunker?"


show kenji happy onlayer master
with charachange

ke "Ah, also hast du eine „Protect and Survive”-Broschüre gelesen. Gut jemanden anzutreffen, der weiß, wie er sich schützen kann."



hi "Du glaubst nicht ernsthaft…"


show kenji neutral onlayer master
with charachange

ke "Die Wahrscheinlichkeit für einen Atomangriff ist größer als null."


hi "Nein, ich bin ziemlich sicher, dass die Wahrscheinlichkeit dafür bei null liegt."


show kenji happy onlayer master
with charachange

"Langsam und dramatisch zieht er eine Augenbraue hoch. Na ja, so dramatisch wie man eine Augenbraue eben hochziehen kann."


hi "Die Chance liegt bei, keine Ahnung, knapp über Null – vielleicht eins zu einer Trilliarde. Sie ist unendlich klein. Außerdem, wo kannst du denn überhaupt einen Atombunker bauen? Sicher nicht auf dem Schulgelände."


show kenji neutral onlayer master
with charachange

ke "Das ist mein Projekt in den Sommerferien, wenn ich zu Hause bin. Mein Vater hat's mir erlaubt."


hi "Wirklich?"


ke "Ja. Er meinte, es wird meine handwerklichen Fähigkeiten und Fingerfertigkeit verbessern. Oder so."


"So wie ich Kenji kenne, hat sein Vater wohl nur gedacht, dass er ihn dadurch eine Weile vom Hals hat."


"Das macht mich neugierig darauf, wie seine Eltern wohl sind. Vielleicht sind sie völlig normal, und Kenji ist nur eine Ausnahme. Andererseits liegt diese Art Paranoia und ängstliche Vorbereitung auf die Apokalypse vielleicht in der Familie."


show kenji happy onlayer master
with charachange

ke "Hey, willst du mir helfen, ihn zu bauen? Du siehst aus, als könntest du mit Werkzeug umgehen. Wenn du mithilfst, könnten wir einen richtig krassen Bunker bauen und nicht nur einen Schutzraum."


"Das bezweifle ich. Durch meine Zeit beim Fußball habe ich eine gute Beinarbeit bekommen, aber ich habe mich noch nie wirklich richtig handwerklich betätigt."


hi "Kann ich nicht, ehrlich. Ich fürchte, ich hab in den Ferien sowieso zu tun."


show kenji tsun onlayer master
with charachange

ke "Schade. Wenn die Feministen jemals die Startcodes in die Finger kriegen, habe ich die Befürchtung, dass nur sehr wenige vorbereitet sein werden."


hi "Und dein Atombunker wird dir vor einer Nuklearexplosion Schutz bieten, wenn jemals der Fall eintreten sollte?"


ke "Ein Atomschutzbunker ist nicht dazu da, um vor der Explosion zu schützen. Dafür gibt es Explosionsschutzbunker."


ke "Ich dachte, das wüsstest du."


hi "Mein Fehler…"


show kenji neutral onlayer master
with charachange

ke "Ich wohne ziemlich weit von größeren Militärstandorten entfernt, daher wird der Fallout nach einem nuklearen Schlagabtausch eine größere Sorge sein als die Explosion selbst."


show kenji happy onlayer master
with charachange

ke "Der Bunker ist dafür zuständig, Staub und andere Partikel von mir, meinen Lebensmitteln und meinem Schlafbereich fernzuhalten. Ich werde dort mindestens vierzehn Tage lang aushalten können."


hi "Vierzehn Tage ist eine ziemlich lange Zeit."


show kenji neutral onlayer master
with charachange

ke "Stimmt. Ich brauche einen Liter Wasser am Tag zum Trinken, am besten zwei, damit ich mich auch waschen kann. Für die Toilettensituation reichen ein Müllbeutel und ein Eimer draußen vor dem Unterschlupf. Lebensmittel heißt natürlich Konserven."


hi "Natürlich. Und das Radio ist für die Kommunikation nach draußen?"


ke "Ganz genau. Damit ich Regierungsmitteilungen darüber abfangen kann, was draußen vor sich geht. Ich brauche eine mechanische Uhr anstatt einer elektrischen, falls die auch vom elektromagnetischen Impuls einer Luftdetonation gegrillt wird."


ke "Es gibt noch so viele andere Sachen, die ich brauche, wie zusätzliche Klamotten, Streichhölzer und Kerzen. Ich glaube aber, dass ich noch genug Zeit habe, das zu besorgen. Vielleicht."


"So ungern ich es zugebe, ich bin beeindruckt. Er hat wirklich recherchiert und alles durchdacht. Andererseits weiß ich nicht, ob ich in einer post-apokalyptischen Welt leben will, in der nur Menschen wie Kenji überlebt haben."


hi "Klingt, als wüsstest du wirklich, was du tust."


show kenji happy onlayer master
with charachange

ke "Verdammt, und wie ich das tue."


"Es muss schwer sein, ständig mit so einer Angst leben zu müssen. Er ist auch kaum unter Leuten, darum ist es an sich schon eine Überraschung, dass er mit anderen beim Bowling war."


"Diese Wesensart erinnert mich ein bisschen an eine gewisse Person. Zum Glück zeigt sich ihre Angst vor Mitmenschen nicht auf so eine ausgeprägt exzentrische Weise."


"Was ich ihm aber definitiv nicht erklären kann, ist, warum genau ich mich in letzter Zeit nicht bei ihm hab blicken lassen."


hi "Es ist spät. Ich hab noch was zu tun. Aber ich denk darüber nach, einen Schutzraum oder so zu bauen."


show kenji neutral onlayer master
with charachange

ke "Ja, okay, cool. Ein Mann muss schließlich tun, was ein Mann tun muss."


ke "Du solltest übrigens mal mit mir abhängen. Du bist ein cooler Typ. Coole Typen sollten miteinander abhängen, stimmt's?"


"Aus irgendeinem Grund fühlt sich das Kompliment ziemlich gut an. Aber da die Situation mit Hanako ist wie sie ist, kann ich seinen Wunsch wohl nicht erfüllen. Zumindest vorläufig."


hi "Das wäre klasse. Ich werde später mit dir darüber reden, wenn ich kann."


show kenji happy onlayer master
with charachange

ke "Cool. Bis später, Alter."


stop music fadeout 3.0

hide kenji onlayer master
with charaexit

"Er geht in sein Zimmer zurück."


"Ich sollte besser nach Hanako sehen."


stop ambient fadeout 1.0

scene bg school_dormhanako_ni onlayer master
show hanagown worry_close onlayer master:
    center
    xpos 0.39
show expression Solid("#00000022") onlayer master
show hanako_door_base onlayer master at right
show hanako_door_door onlayer master at left
with locationskip

"In der Hoffnung, dass Hanako nicht zu aufgewühlt ist, stehe ich vor ihrer Zimmertür und umklammere die Arbeitsblätter, die Mutou mir für sie gegeben hat."


"Es ist ein weiterer Grund, sie zu besuchen, und dadurch habe ich ein Gesprächsthema. Ich sollte ihm wohl für die Aufgabe dankbar sein."


play sound sfx_doorknock2

"Ich atme tief ein, um mich zu beruhigen, und klopfe an die Tür."


"… Stille. Ich lausche, ob irgendetwas von innen zu hören ist, aber da ist rein gar nichts."


$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_hammer

"Ich klopfe erneut, dieses Mal etwas lauter."


"Immer noch keine Antwort. Wie seltsam."


"Ich kratze mich am Hinterkopf und starte einen letzten Versuch, doch noch eine Antwort von Hanako zu bekommen. Ich klopfe ein letztes Mal an die Tür."


hi "Hanako, ich bin's nur. Ich soll für Mutou ein paar Zettel abliefern."


"Für eine Weile scheint der Versuch genauso erfolglos wie die vorigen. Gerade als ich die Zettel unter ihrer Tür durchschieben will, höre ich wie die Türklinke sich bewegt."


$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_dooropen

show hanako_door_door onlayer master:
    xpos -0.1
with charamove

play music music_moonlight fadein 4.0

"Als die Tür sich einen Spalt öffnet, versuche ich so schnell wie möglich zu erkennen, wie es Hanako geht – eine Aufgabe, die durch ihr übergroßes Nachthemd, das den Großteil ihres Körpers verhüllt, nicht gerade erleichtert wird."


"Auf den ersten Blick sieht sie nicht wirklich krank aus. Aber um ehrlich zu sein, wäre mir das im Vergleich zu ihrem jetzigen Gesichtsausdruck um einiges lieber."
"Sie sieht schrecklich müde aus und scheint meine Anwesenheit kaum zur Kenntnis zu nehmen."


hi "Hi, Hanako. Mutou wollte, dass ich dir die hier gebe, weil du heute nicht im Unterricht warst."


"Ich halte ihr die losen Zettel entgegen, die sie zögernd in ihre Hände nimmt. Ihre Bewegungen sind völlig apathisch. Ihre zusammengesackte Körperhaltung ist ungewöhnlich für jemanden, der so oft angespannt und überdreht ist."


show hanagown distant_close onlayer master
with charachange

"Sogar ihre Augen weichen meinen aus und tun ihr Bestes, Blickkontakt zu vermeiden. Ich versuche, einen besseren Blickwinkel zu bekommen, aber sie dreht sich einfach weg."


hi "Bist du… okay? Wenn du dich krank fühlst oder so, kann ich einen Pfleger holen."


"Es ist schon fast erbärmlich, wie ich in einen typischen „Gute Besserung” Dialog herunterrassele, aber mir fällt nichts anderes ein, was ich für sie tun kann."


show hanagown normal_close onlayer master
with charachange

"Bei dem Gedanken scheint sie sich etwas zusammenzunehmen… aber nur ein bisschen. Ihr Kopf ist weiterhin von mir abgewandt, aber ihre Augen richten sich jetzt auf mich."


ha "Es geht mir gut."


"Es folgt eine unangenehme Stille. Während wir uns anschweigen, fallen mir leicht feuchte Flecken an ihren Ärmeln auf. Ihre Wangen sind auch etwas rot. Hat sie geweint?"


hi "Alles klar."


"Ein bisschen zögere ich, bevor ich mit dem herausrücke, weshalb ich eigentlich gekommen bin."


hi "Soll ich hierbleiben? Im Moment hab ich nichts Dringendes zu tun, es wäre also kein Problem."


show hanagown distant_close onlayer master
with charachange

"Sie wendet ihre Augen von mir ab, und ich verliere jede Hoffnung darauf, ihre Laune zu verbessern. Ich warte auf eine Antwort, aber sie sagt weder etwas noch macht sie irgendeine Geste. Sie steht nur da und schaut weg."


hi "Hanako…?"


"Langsam schüttelt sie den Kopf."


hi "Okay. Ähm… dann… gute Nacht."


stop music fadeout 3.0

show hanako_door_door onlayer master:
    xpos 0.0
with charamove

play sound sfx_doorclose

"Und damit macht Hanako einen Schritt zurück und schließt ohne ein weiteres Wort die Tür."


"Mehr als nur ein bisschen besorgt ziehe ich mich in mein Zimmer zurück."



scene bg school_dormhallway onlayer master
with locationskip

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_footsteps_hard

"Während ich den Flur entlanggehe, grüble ich darüber nach, was passiert ist."
"Ich hatte das Gefühl, dass Hanako nur halb da war. So als ob ich mit einem Roboter interagiert hätte, der nur getan hat, worauf er programmiert wurde, ohne wirklich nachzudenken."


"Sie war wie eine leere Hülle."


"Das ist frustrierend. Ich hatte die Hoffnung, dass ein Treffen mit Hanako die Situation verbessern würde, aber ich habe das Gefühl, dass es nur noch schwieriger wurde, sie zu verstehen."
"Wie soll ich ihr denn helfen, wenn sie mich buchstäblich so aussperrt?"


stop ambient fadeout 0.3

scene bg school_dormhisao_ni onlayer master
with locationchange

"Ich mache mir gar nicht die Mühe, das Licht anzuschalten, und entscheide mich stattdessen dafür, einfach meinen Schlafanzug anzuziehen. Dann schlucke ich schnell meine Abendpillen hinunter und lasse mich auf mein Bett fallen."


scene black onlayer master
with shuteye



label de_H22:

scene bg school_scienceroom onlayer master
with locationchange

play music music_pearly

"Wieder einmal erscheint Hanako nicht zum Unterricht. So sehr ich auch versuche, mich auf andere Dinge zu konzentrieren, das lenkt mich den ganzen Schultag lang ab – sogar während ich durch die Schulgärten zu den Wohnheimen gehe."


"Dass heute ihr Geburtstag ist, ist wohl auch kein Zufall. Ich weiß allerdings weder, was die beiden Ereignisse verbindet, noch habe ich irgendeine Vorstellung davon, wie sie sich fühlt."


"Wären es körperliche Schmerzen könnte ich wenigstens ein bisschen Trost spenden. Bei dem hier habe ich aber keine Ahnung, wo ich anfangen soll."


"Im Kopf gehe ich alle Leute durch und überlege, ob sie vielleicht helfen könnten. Shizune und Misha wissen nicht viel über Hanako, und das Bisschen, was sie wissen, dürfen sie mir nicht sagen. Dasselbe gilt für Doc."


"Letzten Endes gibt es nur eine Person, die Hanako gut kennt und die bereit wäre, mir etwas zu erzählen."


scene bg school_dormhisao onlayer master
with shorttimeskip

"Als ich mein Zimmer betrete, stelle ich etwas Überraschendes fest: Es fühlt sich langsam vertraut an."


"Bei dem, was um mich herum passiert, bin ich dankbar, dass dieses Zimmer langsam zu einem Ort wird, an dem ich mich ein wenig entspannen kann."
"Als ich an diese Schule kam, fühlte sie sich sofort in jeder Hinsicht fremd an, von der unberührten Reinlichkeit bis zu der Art, wie sie roch."


"Ich konzentriere mich wieder auf mein Vorhaben, werfe meine Tasche auf das Bett und öffne die Schublade meines Schreibtisches."


"Bevor sie gegangen ist, hat Lilly mir die Nummer gegeben, unter der ich sie in Schottland erreichen kann, und ich habe sie aufgeschrieben. Im Nachhinein frage ich mich, ob sie wusste, dass so etwas passieren könnte."


"Jetzt, wo sie nicht da ist, fällt mir auf, wie sehr Hanako und ich uns auf sie verlassen haben."


"Eine Schublade nach der anderen durchsuche ich nach dem verdammten Fetzen Papier. Zum Glück finde ich es schließlich – unter einem Buch aus der Bibliothek."


scene bg school_dormhisao_blurred onlayer master
show phone mobile onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)

"Wenn ich es mir recht überlege, hätte ich die Nummer direkt in mein Handy einspeichern sollen. Ohne weitere Umschweife tippe ich die Zahlen ein und drücke unruhig auf den Anrufen-Knopf."


"Irgendwann nimmt jemand ab, und eine unbekannte weibliche Stimme meldet sich am anderen Ende. Vermutlich ist es Lillys Mutter."


stop music fadeout 1.0


mystery "{image=vfx/garbage.png} {image=vfx/garbage.png} Satou {image=vfx/garbage.png}?"

"Englisch? Plötzlich komme ich mir völlig unvorbereitet vor. Ich verstehe kein Wort von dem, was sie sagt. Entweder wegen meines begrenzten Wortschatzes oder wegen ihres starken Akzents."
"Eigentlich hätte ich das voraussehen sollen. Laut Lilly ist ihre Mutter nämlich eine gebürtige Schottin."


"In der Hoffnung, dass sie ein bisschen Japanisch spricht – schließlich ist es die Muttersprache ihrer Tochter – fange ich einfach an zu reden."


hi "Äh, hier ist Hisao Nakai… am Apparat…"


"Sie klingt begeistert, als sie die Sprache erkennt. Mir fällt ein riesiger Stein vom Herzen."


"Frau Satou" "Ah, du musst einer von Lillys Schulfreunden sein, richtig?"


"Aber dennoch muss ich mich wegen ihres Akzents konzentrieren, um zu verstehen, was sie sagt."


hi "Ja, richtig. Freut mich, Sie kennenzulernen, Frau Satou."


"Frau Satou" "Es ist so schön, dass sie jemand so höfliches gefunden hat! Lilly, Liebes, es ist für dich!"


"Ihre Mutter wirkt nett, wenn auch etwas überenthusiastisch in Anbetracht der banalen Umstände."


"Es folgt eine kurze Stille, als Lilly an den Apparat kommt. Im Hintergrund kann ich gerade so hören, wie ihre Mutter sie scherzhaft dafür tadelt, dass sie gerade erst aufgestanden ist."


li "Hallo, hier ist Lilly."


hi "Du klingst furchtbar."


"Sie macht ein Geräusch irgendwo zwischen einem sterbenden Tier und einem Gähnen."


"Eine Sache, die ich noch vor dem Anruf überprüft habe, war die Zeitzone. Dort drüben ist es inzwischen ziemlich später Morgen, daher hat sie nicht wirklich eine Entschuldigung."


hi "Geht's dir nicht gut?"


li "Nur müde. Wie spät ist es bei euch?"


hi "Später Nachmittag. Der Unterricht für heute ist gerade vorbei."


li "Hanako geht es nicht gut, nicht wahr?"


play music music_drama 

"Das ging schnell. Meine Annahme, dass sie wusste, dass so etwas passieren würde, war offenbar absolut richtig."


hi "Woher weißt du das?"


li "Weil heute ihr Geburtstag ist. Ich hatte gehofft, dass es ihr zumindest ein bisschen besser gehen könnte, nachdem sie dich kennengelernt hat, aber…"


li "Wie geht es ihr gerade?"


hi "Sie war heute und gestern nicht in der Schule. Ich muss heute noch nach ihr sehen. Ehrlich gesagt, nachdem ich gesehen habe, wie es ihr ging, als ich gestern mit ihr gesprochen habe… bin ich ziemlich besorgt."


hi "Ich weiß wirklich nicht, was ich davon halten soll. Ist das früher schon einmal passiert? Hat es irgendwas mit ihren Narben zu tun?"


li "Bedauerlicherweise ja. In etwa dasselbe passierte letztes Jahr, als ihr Geburtstag bevorstand."


li "Soweit ich sagen kann, ist es, weil ihre Eltern bei dem Unfall gestorben sind, durch den sie ihre Narben hat, und Hanako gibt sich die Schuld an ihrem Tod."


"Ihre Erklärung klingt einleuchtend. Wenn sie diese Schuldgefühle immer an ihrem Geburtstag bekommt, dann bereut sie vielleicht, überhaupt geboren worden zu sein."


"Hanako hat mir gegenüber ihre Zeit im Waisenhaus erwähnt. Vielleicht sollte es mir Mut machen, dass sie mir genug Vertrauen entgegenbringt, um mir so etwas zu erzählen."


"Aber dass Lilly diesbezüglich fast genauso im Dunklen tappt wie ich, ist eine Überraschung."


hi "Also wohnt sie deshalb im Wohnheim der Schule. Hat sie dir noch mehr über den Unfall erzählt?"


li "So nahe wir uns auch gekommen sind… Sie hat mir nur sehr wenig über die Geschehnisse erzählt. Was ich darüber weiß, sind größtenteils Vermutungen."


"Sie klingt deprimiert, fast niedergeschlagen. Angesichts des Traumas, das Hanako durchgemacht haben muss, kann ich es Lilly nicht wirklich übel nehmen, dass sie es nicht weiß. Nichtsdestotrotz scheint sie es als persönliches Versagen zu sehen."


hi "Mach dir keine Vorwürfe, Lilly. Bei allem, was sie erlebt hat…"


"Am anderen Ende der Leitung herrscht ein langes Schweigen. Ich frage mich schon, ob die Verbindung abgebrochen ist, bis ich vom anderen Ende wieder eine Stimme höre."


li "Da gibt es aber noch jemanden, um den ich mir in letzter Zeit Sorgen mache."


hi "Oh?"


"Im Kopf gehe ich die Leute durch, von denen sie sprechen könnte. Die einzigen Personen, die sie zu ihrem engeren Freundeskreis zu zählen scheint, sind Hanako und ich. Obwohl da auch noch Akira ist…"


li "Dieser jemand bist du, Hisao."


"Wieder herrscht Schweigen in der Leitung, aber dieses Mal von meiner Seite."


"Seit ich auf der Yamaku bin, habe ich mir große Mühe gegeben zu verhindern, dass andere sich um mich Sorgen machen."
"Wahrscheinlich hat meine Freundschaft mit Hanako sogar geholfen, größere Gesundheitsprobleme zu vermeiden, da wir ein entspanntes und ruhiges Leben führen."


hi "Äh… hm. Über was muss man sich bei mir Sorgen machen?"


li "Ich bitte um Entschuldigung; das war nicht böse gemeint."


hi "Tut mir leid, ich war nur etwas überrascht. Aber ist Hanako nicht immer noch das größere Problem?"


li "Ich habe schon seit einiger Zeit den Gedanken, dass ihr beide eure eher besorgniserregenden Angewohnheiten gegenseitig verstärkt. Vor meiner Abreise habe ich versucht, das zu korrigieren, aber es hat scheinbar wenig gebracht."


hi "„Besorgniserregende Angewohnheiten”?"


li "Als ich dich gefragt habe, wie deine Pläne für die Zukunft aussehen, war deine Antwort der von Hanako ziemlich ähnlich, als ihr früher diese Frage gestellt wurde."


li "Es ist schön und gut, sie beschützen zu wollen, aber ich befürchte, Hanako so zu behandeln wie eine Tochter oder jemanden, der eine Sonderbehandlung braucht, würde nur das Gegenteil erreichen."





label de_choiceH22:
menu:
    with menueffect
    "Die Situation wurde quasi auf den Kopf gestellt. Nach allem, was passiert ist, ist es das erste Mal, dass ich an Lillys Urteil zweifle."
    "Lilly zustimmen.":




        return m1
    "Dem eigenen Urteil vertrauen.":


        return m2

label de_H22a:

"Ich will es nicht zugeben, aber sie könnte Recht haben. Mich stört allerdings etwas anderes."


hi "Und du hast versucht, das zu… „korrigieren”?"


hi "Warte… unser Ausflug in die Stadt?"


li "Sehr scharfsinnig. Ich dachte, es hilft vielleicht, wenn ich euch zwei aus der Yamaku und in die Welt da draußen schleife. Ich bin froh, dass ihr euch dabei etwas nähergekommen seid."


"Das hat sie also bemerkt. Ich vermute, dass sie uns wohl aufmerksam zugehört hat, und ihr Gehör ist unglaublich gut; höchstwahrscheinlich gut genug, um gehört zu haben, worüber wir gesprochen haben."


hi "Das hört sich mehr und mehr so an, als hättest du uns manipuliert."


"Schweigen. Das ist hart ausgedrückt, aber ich habe nicht vor, diese Worte zurückzunehmen."


li "Tut mir leid. Ich war nur… besorgt um euch."


hi "Es ist okay. Ich schätze, es gibt sowieso Wichtigeres."


"Dass sie so etwas macht, ist keine völlige Überraschung. Ihre mütterliche Fürsorge kann manchmal etwas überheblich werden, aber sie hat die besten Absichten."


hi "Du denkst also, ich sollte mehr an mich denken, anstatt mich um Hanako zu kümmern?"


li "Das ist im Großen und Ganzen, was ich sagen will. Entschuldige bitte noch mal, dass ich dir das nicht eindeutiger gesagt habe, anstatt hinter deinem Rücken zu agieren."


li "Ich weiß, dass ich bei Hanako mindestens genauso überfürsorglich war wie du, aber ich befürchte, dass du dich bei deiner Aufgabe, Hanako glücklich zu machen, selbst vernachlässigst."


hi "Glaubst du wirklich, Hanako kommt klar?"


li "Sie ist nicht so zerbrechlich wie du denkst. Ich weiß nicht genau, welche Erlebnisse sie hinter sich hat oder was für Gefühle sie in sich trägt, aber bis jetzt hat sie es geschafft, sich durchzuschlagen."


li "Außerdem hoffe ich, dass ihr ein wenig Freiraum dabei hilft, sich zu entscheiden, was sie wirklich will und ihr die Stärke gibt, danach zu greifen."


li "Bitte glaub an Hanako. Das ist alles, worum ich dich bitte."


hi "Ich… Ich glaube, ich werde eine Weile darüber nachdenken."


li "Das ist gut. Überstürztes Handeln wird dich nicht weiterbringen."


li "Ich weiß, dass du manchmal an deiner Beziehung mit Hanako zweifelst, aber sie…"


"Lilly unterbricht sich selbst und überdenkt ihre Worte noch einmal."


li "Bitte denk daran, dass ich mich nicht mit dir angefreundet hätte, wenn ich dich nicht für einen von Grund auf guten Menschen gehalten hätte. Du bist ein guter Freund – sowohl für mich als auch für Hanako."


hi "Danke. Das hilft."


"Wir machen ein bisschen Smalltalk, um die Stimmung zu heben, aber es wirkt ziemlich aufgesetzt. Über Lillys Aufenthalt in Schottland weiß ich nur wenig, aber nach so einem heftigen Thema will ich ein bisschen allein sein, um nachzudenken."


stop music fadeout 8.0

show phone mobile onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

scene bg school_dormhisao onlayer master
show phone mobile onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with locationchange
with Pause (0.5)

hide phone onlayer master
with None

"Nach ein paar Minuten verabschieden wir uns, und ich lege mein Handy auf den Tisch."


"Im Vergleich zu Hanakos Lage wirkt meine absolut banal. Ich habe immer noch beide Eltern, ich hatte eine relativ normale Kindheit, und anders als bei vielen an der Yamaku, kann man in der Öffentlichkeit mein Leiden nicht sofort erkennen."


"Aber andererseits… Ist das nicht einfach nur ein Versuch, mein Verhalten ihr gegenüber zu rechtfertigen?"


"So mag unsere Vergangenheit gewesen sein, aber wenn es um die Zukunft geht, habe ich immer noch keine Ahnung, was ich tun will."
"In der Schule habe ich mich einfach auf jeden einzelnen Tag konzentriert und mehr und mehr Dinge zurückgestellt, um mich um Hanako zu kümmern."


"Ich rufe mir in Erinnerung, was Mutou mir nach Hanakos Zusammenbruch gesagt hat; über den Sinn der Yamaku und meine Ausbildung. Im Nachhinein wollte er wohl auf exakt dasselbe hinaus."


"Was habe ich nur seit meiner Herzattacke gemacht? Wenn ich es jemals geschafft hätte, Hanako aus ihrem Zimmer zu bekommen und sie sich geöffnet hätte, was dann?"


"Während die Sonne langsam untergeht, schaue ich aus meinem Zimmerfenster. Es ist ein schöner Anblick, aber der wahre Genuss ist eigentlich die Stille, während die Schüler zu ihren Zimmern zurückkehren."


"Alles, was ich jetzt will, ist nachdenken. Ich bin mir nicht sicher, wie viel Zeit ich habe, aber ich will herausfinden, wie ich weitermache."


scene black onlayer master
with dissolve




label de_H22b:

stop music fadeout 5.0

"Ich höre sorgfältig zu, was Lilly zu sagen hat, aber ich kann mich nicht dazu überwinden, ihr zuzustimmen."


"Hanako ist bestenfalls ein empfindlicher Mensch, und nach dem, was passiert ist, als ihr Geburtstag erwähnt wurde, ist die momentane Situation die letzte, in der wir sie alleinlassen sollten, wenn sie sich bewusst absondert."


"Ich habe aber das Gefühl, dass Lilly ein ganz bestimmtes Bild im Kopf hat, wie man am besten mit Hanako umgeht. Nicht nur jetzt, sondern während all der Zeit, in der ich die beiden kenne."


"Ich grübele darüber nach, was der beste Schritt ist, und versuche schließlich so sachte und doppeldeutig wie möglich, zustimmende Worte zu finden."


"Danach machen wir noch ein bisschen Smalltalk, aber keiner von uns hat in Anbetracht der jüngsten Geschehnisse wirklich Lust dazu. Wir verabschieden uns, und ich lege auf."


show phone mobile onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

scene bg school_dormhisao onlayer master
show phone mobile onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with locationchange
with Pause (0.5)

hide phone onlayer master
with None

"Ich will selbst mit Hanako sprechen, um ihr zu helfen, so gut ich kann. Im Moment wäre es das Beste für sie, jemanden bei sich zu haben und nicht alleingelassen zu werden."







label de_H22c:

stop music fadeout 5.0

"Ich höre sorgfältig zu, was Lilly zu sagen hat, aber ich kann mich nicht dazu überwinden, ihr zuzustimmen."


"Ich will mehr mit Hanako zusammen sein. Ich will ein besserer Freund für sie sein, um sie zu unterstützen, wenn sie Unterstützung braucht, und um da zu sein, wenn sie am dringendsten jemanden braucht. Ich glaube, jetzt ist einer dieser Momente."


"Die Erinnerung an den Ladenbesitzer, den wir zusammen in der Stadt getroffen haben, bringt mich immer noch durcheinander."
"Jeder, der Hanako auch nur kurz ansieht, verfällt schließlich in ein Starren, und ihnen einen Vorwurf dafür zu machen wäre angesichts meiner eigenen Reaktion völlig scheinheilig."


"Meine eigenen Narben mag ich auch nicht, aber ich kann sie wenigstens mit so etwas Einfachem wie einem Hemd verdecken. Ich kann mir ein Leben gar nicht vorstellen, in dem ich jeden Tag versuche, mich so gut es geht zu verstecken."


"Und darüber hinaus hat Hanako nicht einmal jemanden, der sie unterstützen würde, egal wie sie aussieht. Ich wohne nicht bei meinen Eltern, aber ich kann mich immer noch an sie wenden und sie besuchen, wenn ich will."


"Ich grübele darüber nach, was der beste Schritt ist, und versuche schließlich so sachte und doppeldeutig wie möglich, zustimmende Worte zu finden."


"Danach machen wir noch ein bisschen Smalltalk, aber keiner von uns hat in Anbetracht der jüngsten Geschehnisse wirklich Lust dazu. Wir verabschieden uns, und ich lege auf."


show phone mobile onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

scene bg school_dormhisao onlayer master
show phone mobile onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with locationchange
with Pause (0.5)

hide phone onlayer master
with None

"Es gibt wenigstens eine Sache, die ich für Hanako tun kann. Wenn ich diese kleine Geste für sie mache, kann ich nur hoffen, dass sie mir erlaubt, ihr ein kleines Stück näherzukommen."






label de_H23:



scene bg school_dormhanako_ni onlayer master
show hanako_door_base onlayer master at right
show hanako_door_door onlayer master at left
with shorttimeskip

play sound sfx_hammer


play music music_tragic fadein 0.5

"Dreimal klopfe ich an Hanakos Tür. Wie erwartet kommt keine Antwort. Kurz überlege ich, ob ich noch einmal klopfe, aber ich weiß ganz genau, dass es nur auf dasselbe hinauslaufen würde."


"Mit der Hand auf Hanakos Türklinke versuche ich, mir zu überlegen, was ich zu ihr sagen will."
"So sehr ich es versuche, mir fällt irgendwie nichts ein, das es wert wäre, gesagt zu werden. Ich will sie trösten, ja, aber ich habe keine Ahnung, wie ich das machen soll."


"Das allein reicht schon fast, um mich abzuhalten. Allerdings habe ich Lilly gesagt, dass ich es tun werde, also habe ich das Gefühl, es durchziehen zu müssen – ob ich davon überzeugt bin oder nicht."


"Nach langem Zögern drücke ich die Türklinke nach unten. Die Tür bleibt aber geschlossen, weil sie abgeschlossen ist."


hi "Hanako…"


"Also hat sie mich wirklich ausgesperrt. Nach allem, was zwischen uns passiert ist und der Zeit, die wir miteinander verbracht haben… hat sie mich völlig ausgesperrt."


hi "Ähm… Ich weiß nicht, ob du mich hören kannst, aber…"


hi "Ich will nur ein bisschen mit dir reden. Wenn du mich hören kannst, könntest du die Tür aufmachen?"


with Pause(4.0)

play sound sfx_lock

"Schweigend warte ich. Minuten vergehen, aber irgendwann höre ich, wie sich Schritte der Tür nähern und sie aufgeschlossen wird."


"Wenigstens will sie mir zuhören. Das ist schon mal gut."


hi "Ich… Ich weiß nicht wirklich, was ich sagen soll, aber… Ich wollte dich nur sehen. Ich wollte sichergehen, dass es dir gut geht."


"Ich hole tief Luft, bevor ich die Klinke herunterdrücke und die Tür öffne. Wenn sie sie ohne Widerspruch aufgeschlossen hat, sollte es in Ordnung sein, wenn ich hineingehe."


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
show hanagown distant onlayer master:
    center
    ypos 1.15
with silentwhiteout

"Hanako sitzt an der Seite ihres Bettes; mit einem mürrischen Gesicht, als wäre sie tief in Gedanken. Ihr Zimmer ist so schlicht wie immer, und im Moment scheint sie perfekt zu der davon ausgehenden Stimmung zu passen."


show hanagown normal onlayer master
with charachange

show hanagown worry onlayer master at center
with Dissolvemove(0.2)

"Schließlich wandern ihre Augen langsam zur Tür. Sobald sie meine Anwesenheit bemerkt, schießt sie vom Bett auf, springt auf ihre Beine und sieht mich direkt an."


"Ihr übergroßer Bademantel lässt diese Bewegung umso ausladender wirken, weil er locker um ihren zierlichen Körper fällt."


ha "W-Was machst…?"


"Als ich sie ansehe, bereue ich schnell, dass ich hereingekommen bin. Sie wirkt deprimiert, aber mit einem Fünkchen Wut dahinter. Sie kann also auch so ein Gesicht machen."


hi "Ich… ich wollte nur nachsehen, ob bei dir alles in Ordnung ist. Ich dachte, das wäre okay, weil du die Tür aufgesperrt hast."


show hanagown distant_blush onlayer master
with charachange

"Hanako setzt an, etwas zu sagen, schließt aber schnell wieder ihren Mund und sieht weg."


show hanagown distant_blush onlayer master:
    center
    ypos 1.15
with charamove

"Eine Weile lang stehen wir schweigend da, dann macht sie einen Schritt zurück und setzt sich wieder auf die Bettkante."
"Ich bin mir nicht sicher, ob sie meinetwegen frustriert ist und sich einfach nur mit meiner Anwesenheit im Zimmer abgefunden hat, oder ob es für sie wirklich in Ordnung ist."


"Wieder einmal kann ich nicht ganz verstehen, wie sie sich fühlt. Das nervt."


"Schließlich gehe ich zu ihrem Schreibtischstuhl und setze mich hin. Das tue ich langsam, um ihr Zeit zu geben, jegliches Problem anzusprechen, das sie damit haben könnte."
"Sie sagt jedoch nichts. Sie tut nichts, außer auf den Boden zu starren und sich nicht zu rühren."


"Nachdem ich mich mit der Stuhllehne nach vorne hingesetzt habe, schaue ich mir Hanako genauer an. Sie wirkt blass, aber ihre Wangen sind rot. Bei dem Anblick ihrer dünnen Figur bin mir auch nicht sicher, ob sie gut gegessen hat."


"Lilly mag zwar gesagt haben, dass es besser wäre, mehr Abstand von ihr zu halten, aber es fällt mir schwer, das als den richtigen Weg zu sehen, wenn sie so aussieht."


"Noch immer sieht sie ohne ein Wort zu Boden, als ob sie darauf warten würde, dass ich etwas sage. Das ist absolut verständlich, da ich derjenige war, der in ihr Zimmer gekommen ist."


hi "Willst du irgendwo hingehen? Ein Ausflug den Hügel hinunter ins Dorf ist vielleicht ein bisschen zu viel, aber wir könnten wenigstens draußen spazieren gehen."


show hanagown worry_blush onlayer master
with charachange

ha "Warum… willst du das tun?"


hi "Ich habe mir nur gedacht, es könnte dir vielleicht ein bisschen helfen. Du bist so viel hier drinnen, dass deine Haut bald genauso blass ist wie die von Lilly."


show hanagown distant_blush onlayer master
with charachange

"Ich lache über meinen Witz und erwarte, dass Hanako mitlacht, aber sie reagiert nicht; sie starrt nur weiter auf den Boden."


ha "Wenn du nicht gehen willst… will ich auch nicht."


hi "Schon in Ordnung. Ich habe viel mit Freunden Fußball gespielt, bevor ich an die Yamaku gekommen bin. Ich bin gerne draußen."


"Hanako zeigt keine sichtbare Reaktion. Es ist schwer, mit ihr zu reden, wenn die Diskussion so einseitig ist."


hi "Wir könnten auch in die Bibliothek gehen… äh, wenn sie nicht jetzt gerade schließen würde. Der Garten ist aber auch okay."


"Sie fängt an, mit ihren Haaren zu spielen. Es lenkt mich ab und ist auch irgendwie ungewöhnlich für sie."


"Allerdings… Seit diesem Vorfall im Unterricht, bin ich in ihrer Gegenwart auf Eierschalen gegangen, um sie nicht wieder zu verletzen. Sie aktiv aus ihrem Zimmer zu holen, könnte genau das Richtige für sie sein."


"Ich lehne mich auf meinem Stuhl nach vorne und lächle sie leicht gezwungen an, um die Stimmung ein wenig zu verbessern."


hi "Um diese Zeit ist dort keiner, also bräuchtest du dir keine Sorgen zu machen, dass uns jemand begegnet. Du könntest es als kleines Date sehen oder so was."


show hanagown normal onlayer master
with charachange

"Ich fange an zu lachen, aber ich höre auf, als Hanako aufhört, mit ihren Haaren zu spielen und sich an der Bettkante festkrallt. Ihr Mund bewegt sich, aber so sehr ich mir auch Mühe gebe, ich verstehe ihr Gemurmel nicht."


hi "Hanako?"


ha "Du… verstehst nicht…"


"Sogar jetzt verstehe ich kaum, was sie sagt. Es kommt mir vor, als ob sie sich so klein wie möglich machen will – dass sie das in der Klasse oder vor anderen macht, ist zwar ganz normal für sie, aber wenn sie es bei mir macht, tut es weh."


hi "Ich habe dir doch gesagt, es ist okay. Es ist nur ein kleiner Spaziergang; keiner wird uns sehen."


"Ich erhebe mich von dem Stuhl und gehe zur Tür. Dort drehe ich mich um, um Hanako zum Mitkommen aufzufordern. Wieder reagiert sie überhaupt nicht auf meine Worte."


show hanagown distant onlayer master
with charachange

ha "Ich…"


hi "Rausgehen wird dir helfen, den Kopf freizubekommen."


ha "Warum willst du… das tun…"


hi "Weil ich dir helfen will."


ha "Ich… will… keine Hilfe. Bist du nur hergekommen… um zu versuchen, mich nach draußen…?"


hi "Es macht mir nichts aus. Ich denke, jeder braucht manchmal Hilfe. Als ich neu an der Yamaku war, haben du und Lilly mir sehr viel geholfen."


hi "Außerdem habe ich nichts anderes vor."


ha "Ich w-will nicht gehen. Es… geht mir gut."


hi "Ich glaube nicht, dass es gesund ist, so lange drinnen zu bleiben. Die Sonne ist noch draußen, also ist es noch nicht zu spät für einen kleinen Spaziergang."


hi "Ein bisschen Bewegung könnte ich sicher auch gebrauchen, um wach zu werden. Ich muss nachher noch ein paar Hausaufgaben fertig machen, und dabei will ich ja schließlich nicht einschlafen."


show hanagown normal onlayer master
with charachange

ha "Dann… geh."


hi "Allein?"


"Sie nickt."


hi "Na ja, ich habe nicht wirklich etwas dagegen, aber… bist du sicher? Ich bin vorbeigekommen, um dich zu fragen, ob du mitkommst."


show hanagown distant onlayer master
with charachange

ha "Es geht mir gut. Du kannst gehen."


hi "Komm schon, nur ein kurzer Spaziergang."


ha "Bitte geh einfach. E-Es geht mir gut."


hi "… Hanako?"


"Ich versuche, einen Blick auf ihr Gesicht zu erhaschen, um ihre Gefühle einschätzen zu können, aber ihr Ausdruck ist wie versteinert. Als wäre er so sorgfältig aufgesetzt, dass jede Bewegung ihn zerstören könnte."


hi "Na ja, wenn du hierbleiben willst… vielleicht könnten wir ein Spiel spielen?"


ha "Geh einfach. Bitte. Ich will… jetzt gerade nichts machen."


hi "Aber sicher gibt es irgendetwas, was du machen willst. Hier ganz allein in deinem Zimmer zu sitzen muss doch langweilig sein."


ha "Ich will, dass du gehst."


hi "Komm schon, sei nicht so. Ich will doch nur ein wenig Zeit mit dir verbringen. Weißt du, Lilly und ich machen uns Sorgen, also…"


show hanagown worry_blush onlayer master
with charachange

ha "Du hast mit ihr gesprochen?"


hi "Äh… ja. Wir haben… telefoniert, gerade eben. Wir machen uns beide große Sorgen um dich."


show hanagown irritated onlayer master
with charachange

"Hanako murmelt wieder vor sich hin. Es wird immer beunruhigender."


hi "Hanako…?"


ha "Ich sage dir… bitte, geh. Du verstehst nichts…"


hi "Wenn du einfach mit mir reden würdest, könntest du mir sagen, was ich nicht verstehe. Ich will dich doch nur beschützen, ich verstehe nicht…"


ha "Geh… weg, bitte…"


hi "Dich einfach nur wieder in deinem Zimmer einzuschließen wird dir auch nicht helfen, Hanako. Bitte…"


stop music fadeout 2.0

"Stille."


hi "Hanako, ich will dir doch nur hel—{w=0.3}{nw}"


scene ev hanako_rage onlayer master:
    truecenter
    subpixel True zoom 3.0
    0.25
    linear 0.2 zoom 1.05
    easein 8.0 zoom 1.0
with flash

play music music_rain

"Plötzlich springt sie von ihrem Bett auf und starrt mich mit einem Ausdruck an, der mich völlig unvorbereitet trifft."


ha "Raus aus meinem Zimmer, raus aus meinem Zimmer, raus aus meinem Zimmer!" with vpunch


"Hanako schreit mich so laut an, dass ich zum ersten Mal seit langer Zeit wirklich Angst habe – und das ausgerechnet bei Hanako. Ich… Ich habe keine Ahnung, wie ich darauf reagieren soll."


ha "Verschwinde! Ich sagte, du sollst gehen!" with vpunch


hi "A-Aber… Ich wollte dir… doch nur helfen…"


ha "Ich weiß, dass ich Hilfe brauche! Ich weiß, dass ich kaputt bin! Das musst du mir nicht extra sagen!" with vpunch


hi "Ich hab nie gesagt, dass du kaputt bist oder irgendwas in der Richtung!"


ha "Es steht dir ins Gesicht geschrieben; es steht Lilly ins Gesicht geschrieben; es steht allen ins Gesicht geschrieben!" with vpunch


ha "Ich muss jede Woche zu einem Therapeuten, Lilly behandelt mich, als wäre ich ihr Kind, und jetzt… sogar du!" with vpunch


ha "Nichts hat sich geändert, rein gar nichts! Ich hasse Lilly, und ich… ich hasse dich mehr als alle anderen…!" with vpunch


"In ihrem Gesicht arbeitet es auf seltsame, fast groteske Weise. Ich habe noch nie jemanden gesehen, der vollständig die Kontrolle über sich verliert, aber es sieht so aus, als würde das sonst so stille und scheue Mädchen vor mir kurz davor stehen."


"Ich weiß nicht, was ich tun soll. Ich habe keine Ahnung, was ich sagen oder tun könnte."


ha "Geh! Lass mich allein! Verschwinde!" with vpunch


"Ich gehe einen Schritt zurück, dann noch einen und dann noch einen. Mein Rückzug wird erst gebremst, als ich die Tür in meinem Rücken spüre."


"Diese Situation kann ich nicht retten. Nichts, was ich jetzt sage, würde irgendetwas ändern. Ich fühle mich, als wäre ich in einer seltsamen und bizarren fremden Welt. Ich will nicht mehr hier sein."


"Der Türgriff widersetzt sich meinen ungeschickten Versuchen, die Tür zu öffnen, ohne Hanako den Rücken zuzuwenden. Schließlich senkt sich die Klinke, und ich öffne so schnell ich kann die Tür und springe beinahe rückwärts nach draußen."


"Dabei lasse ich das Mädchen vor mir nicht aus den Augen."


"Sie ist nicht kaputt. Hanako ist nicht kaputt. Wenn sie kaputt wäre, dann wäre ich nach allem, was mir passiert ist, genauso kaputt wie sie. Lilly wollte immer nur ihr Bestes, und ich habe immer nur versucht, sie so gut wie möglich zu beschützen."


scene ev hanako_rage_sad onlayer master:
    zoom 1.0
with charachange

"Hanako schaut nach unten, ihre Energie verbraucht. Jetzt, wo ich nicht mehr in ihrem Zimmer bin, ist ihr schlimmster Zorn verraucht."


"Aber auch jetzt noch kann ich mich nicht überwinden, ihr zu widersprechen. Es ist nicht nur der Schock dessen, was sie gesagt hat… Es fühlt sich an, als ob mich etwas anderes zurückhält – etwas, wodurch mir beinahe übel wird."


show bg school_dormhanako_ni onlayer master:
    center
    xpos 0.55
    linear 5.0 center
show hanako_door_door onlayer master:
    left
    xpos -0.2
    linear 5.0 left
show hanako_door_base onlayer master:
    right
    xpos 1.1
    linear 5.0 right
with flash

stop music fadeout 4.0

"Ohne ein Wort schließe ich langsam die Tür. Das Quietschen der alten Türangeln ist beinahe ohrenbetäubend."


play sound sfx_doorclose

show bg school_dormhanako_ni onlayer master at center
show hanako_door_door onlayer master at left
show hanako_door_base onlayer master at right
with ease

"Mit einem endgültigen Klicken schließt sich die Holztür. Die Hanako, von der ich dachte, dass ich sie kenne, verschwindet dahinter, und nur schwache, orangene Lichtstrahlen scheinen darunter durch."


scene bg school_girlsdormhall onlayer master
with locationchange

"Ich fühle mich wie betäubt. Ich weiß nicht, was ich tun soll, also mache ich mich auf den Weg zurück in mein Zimmer. Mechanisch setze ich einen Fuß vor den anderen, wobei ich kaum etwas von meiner Umgebung wahrnehme."


"Nur mein Verstand arbeitet; er stellt alles infrage, was ich dachte, über Hanako zu wissen."


"Aber eines stelle ich nicht infrage: Dass diese sich schließende Tür mehr beendet hat als nur diesen einen Besuch."




label de_H24:



scene bg school_girlsdormhall onlayer master
with locationchange

play music music_night fadein 4.0

"Nachdem ich nach Unterrichtsende mit Lilly telefoniert hatte, habe ich mich an meinen Schreibtisch gesetzt und aus dem Fenster heraus die anderen Schüler beobachtet, wie sie das Schulgebäude verlassen."
"Normalerweise waren sie in Gruppen unterwegs, aber auch wenn sie allein gegangen sind, haben sie sich immer erst von Freunden verabschiedet."


"Das ist völlig normal. Etwas, was mir an jedem anderen Tag gar nicht aufgefallen wäre, weil es so banal ist."


"Aber es ist auch etwas, was Hanako noch nie hatte, seit ich sie kenne. Als ich zum zweiten Mal in ebenso vielen Tagen vor Hanakos Tür stehe, geht mir das nicht aus dem Kopf."


"Ich habe zwei Teller in der Hand. Darauf ist… nicht gerade das gesündeste Essen, aber ich will zumindest sichergehen, dass Hanako isst. Es könnte auch ein Versuch sein, sie dazu zu bringen, mich hereinzulassen."


"Lilly und ich haben unser Bestes versucht, um für sie da zu sein."
"Seit ihrem Zusammenbruch im Unterricht will ich Hanako unbedingt beschützen. Ich will gar nicht daran denken, dass so etwas – oder sogar etwas Schlimmeres – ihr noch einmal passieren könnte."


scene bg school_dormhanako_ni onlayer master
show hanagown distant_close onlayer master:
    center
    xpos 0.39
show hanako_door_base onlayer master at right
show hanako_door_door onlayer master at left
with locationchange

play sound sfx_doorknock2

"Mein Klopfen ist laut und kräftig zu hören, während ich vorsichtig einen Teller auf meinem anderen Arm balanciere. Ich bezweifle, dass Hanako sie für mich öffnen wird; ich kann nur hoffen, dass ich wenigstens ihre Aufmerksamkeit habe."


hi "N'Abend, Hanako. Ich bin's nur."


"Ich warte einen Moment ab, ob sie vielleicht antwortet, aber es überrascht mich nicht wirklich, dass sie es nicht tut."


hi "Ich… Ich habe was zum Essen für uns beide. Kann ich reinkommen?"


"Für eine gefühlt sehr lange Zeit sind die einzigen Geräusche, die ich hören kann, gedämpfte Stimmen aus dem Stockwerk unter uns."


play sound sfx_lock

"Dann höre ich, wie sich nackte Füße der Tür nähern, und ich unterdrücke ein erleichtertes Seufzen, als die Tür aufgeschlossen wird."


play sound sfx_dooropen

show hanako_door_door onlayer master:
    xpos -0.1
with charamove

"Als Hanako die Tür öffnet, schaue ich sie durchdringend an."


show hanagown normal_close onlayer master
with charachange

"Sie schaut kurz auf den Teller in meiner linken Hand. Es ist ein einfaches Currygericht, das ich schnell aus einer Fertigpackung gemacht habe."


show hanagown distant_close onlayer master
with charachange

"Ihre Augen wandern zu dem Teller in meiner rechten Hand, der das gleiche enthält; dann schaut sie wieder nach unten."


hide hanagown onlayer master
with charaexit

"Als sie wieder in ihr Zimmer schlurft, merke ich, dass ich noch kein Wort zu ihr gesagt habe. Ich folge ihr bedrückt nach drinnen; etwas verlegen, dass ich so darin vertieft war, sie zu betrachten."


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
with silentwhiteout

"Mehr denn je fühlt sich die triste und kahle Atmosphäre in Hanakos Zimmer wie ein Spiegel ihrer Persönlichkeit an. Als ich die Tür schließe, sind die Stimmen von draußen nicht mehr zu hören, und die Stille hier drinnen ist bedrückend."


"Ich gehe durch das Zimmer und stelle die zwei Teller auf ihren Schreibtisch. Ich bin froh, dass sie mich hereingelassen hat, aber als ich mich zu ihr umdrehe, frage ich mich, ob mein Besuch so eine gute Idee war."


show hanagown distant onlayer master:
    center
    ypos 1.15
with charaenter

"Ich glaube aber trotzdem nicht, dass Lilly Recht hatte. Wenn ich Hanako so sehe, bin ich mir sicher, dass sie in Ruhe zu lassen, das letzte ist, was wir tun sollten. Ich will gar nicht daran denken, aber sie könnte vielleicht etwas sehr Dummes tun."


hi "Ähm… Es ist nur ein Fertiggericht, aber es sollte sattmachen."


"Ich nehme einen Teller und halte ihn ihr hin. Sie nimmt ihn wortlos entgegen und setzt sich auf die Bettkante."
"Ich setze mich auf ihren Stuhl, und die gewohnten Essensgeräusche erklingen im Raum, als wir mit den Gabeln, die ich in den Reis gesteckt hatte, anfangen zu essen."


"Das Curry selbst schmeckt… okay. Viel kann man von einer Marke, die ich nicht kannte, auch nicht erwarten, also ist es schon mal gut, dass man es essen kann."


"Beim Essen ist es nicht so schlimm, dass sie nicht redet. Keiner von uns spricht gerne beim Essen, und das hier erinnert mich an all die Mittagspausen, die wir zusammen verbracht haben."


hi "Es ist irgendwie schön, so zusammen zu essen."


show hanagown worry onlayer master
with charachange

"Hanako schaut mich fragend an. Das ist zumindest etwas besser als der Gesichtsausdruck, den sie bisher hatte."


hi "Der Grund, warum wir Freunde geworden sind, waren doch unsere gemeinsamen Mittagspausen. Es ist schön, sich an diese Zeiten zu erinnern."


"Sie zögert ein paar Sekunden, und ich verziehe das Gesicht. Habe ich etwas Falsches gesagt?"


show hanagown smile onlayer master
with charachange

"Schließlich lächelt sie und nickt. Normalerweise würde mich das ermutigen, aber ihr Lächeln sieht seltsam aus. Ich kann nicht genau sagen warum."


ha "Alles ist… genau wie vorher, oder?"


hi "J-Ja. Natürlich ist es das."


hi "Du hast immer noch Lilly und mich, um dir zu helfen und dich zu beschützen, und wenn sie zurück ist, wird alles so sein, als wäre sie nie weg gewesen."


show hanagown distant onlayer master
with charachange

"Hanako nickt erneut; ihr Gesichtsausdruck immer noch genau wie vorher. Sie scheint etwas anders zu sein als vorhin, als ich das Zimmer betreten habe, und es ist irgendwie verstörend."


"Nach dem kurzen Gespräch machen wir uns beide wieder daran, unsere Teller leer zu essen. Obwohl Hanako fröhlicher aussieht als vorhin, blicke ich immer wieder kurz zu ihr hinüber, um sicherzugehen."


"Bald darauf ist Hanakos Curry leer. Ich esse die letzten Reste von meinem, als sie den Teller auf den Schreibtisch stellt. Danach stelle ich meinen leeren Teller samt Gabel auf ihren."


"Ich frage mich, was ich sagen soll. Ich will vermeiden, dass wir uns wieder anschweigen, und ich will das Zimmer auch nicht so schnell wieder verlassen – aber Hanako ist diejenige, die zuerst spricht."


show hanagown worry_blush onlayer master
with charachange

ha "Ich… Ich habe mich gefragt… wo du schon hier bist…"


"Sie öffnet schnell eine ihrer Schubladen und zieht nach kurzem Wühlen ihr Schachbrett heraus."


show hanagown smile onlayer master
with charachange

ha "W-Würdest du… gerne spielen…?"


"Dieses Mal kann ich einen erleichterten Seufzer nicht unterdrücken."


hide hanagown onlayer master
with charaexit

show bg school_dormhanako onlayer master at left
with charamove_slow

"Ich stimme hastig zu, und Hanako beginnt, die Figuren auszupacken, während ich vom Stuhl aufstehe und mich auf ihr Bett setze."


"Hanako ist wieder bereit, mich in ihre Welt zu lassen – mit einer so simplen Geste wie einem gemeinsamen Schachspiel. Ich habe mir wohl einfach grundlos Sorgen gemacht."


show hanagown smile_close onlayer master:
    center
    xpos 0.55
    easein 1.0 center
with Dissolve(1.0)

"Das Spielbrett liegt zwischen uns auf dem Bett, und wir stellen beide unsere jeweiligen Figuren auf."


"Seit wir befreundet sind, haben wir nie viel geredet. In diesem Moment wird mir klar, dass das nie wirklich nötig war. Nur ein einfaches Buch oder ein Brettspiel oder eine Mahlzeit reichen aus, um die Distanz zwischen uns zu überbrücken."


"Ich mache den ersten Zug, wie ich es immer getan habe. So ist unsere Freundschaft eben, und so wird sie wohl auch immer bleiben."


"Irgendetwas fühlt sich aber bei ihr definitiv anders an, und ich weiß nicht, was es ist. Ich schaue Hanako eindringlich an, aber ich kann ihren Gesichtsausdruck nicht lesen."


"Wir mögen zwar körperlich im selben Zimmer sein, aber ich habe das Gefühl, als wären wir weiter voneinander entfernt als je zuvor. Aber Hanako ist eine zerbrechliche Person, und ich will sie nicht verletzen."


"Das ist auch etwas, was schon immer so war und wohl für immer so bleiben wird."


stop music fadeout 2.0






label de_H25:



scene bg school_scienceroom onlayer master at bgright
with locationchange

"Nach meinem Gespräch mit Lilly gestern, habe ich mir vorgenommen, mich von der Lustlosigkeit zu befreien, die ich seit meiner Ankunft an der Yamaku mit mir herumtrage."


"Doch auch wenn ich versuche, mich auf das Buch vor mir zu konzentrieren, geht mir Hanakos leerer Platz am hinteren Ende der Klasse einfach nicht aus den Kopf."
"Jedes Mal, das ich versuche, mich zu konzentrieren, wandern meine Augen wieder hinüber zu ihrem Tisch und meine Gedanken schweifen ab."


show miki smile onlayer master at center
with charaenter

"Wieder einmal wandern meine Augen hinüber, doch diesmal wird meine Sicht von einer gewissen anderen Klassenkameradin blockiert."


hi "Oh, hey Miki."


show miki grinclosed onlayer master
with charachange

mk "Vielleicht solltest du etwas zu Mittag essen. Deinen knurrenden Magen kann ich bis zum meinem Tisch hören."


play music music_happiness

"Ich lasse enttäuscht meinen Kopf hängen. Meine Reaktion scheint sie etwas zu amüsieren, dann hopst sie auf meinen Tisch. Ihr Grinsen, als sie auf ihm sitzt, erinnert an die Grinsekatze aus Alice im Wunderland."


show miki grin_close onlayer master
with characlose

mk "Also, woran arbeitest du?"


hi "Bisschen Mathe. Ich hab es ganz gut im Griff, aber ich wollte es einfach noch mal durchgehen."


show miki whistle_close onlayer master
with charachange

mk "Ach, echt? Lass mal sehen."


"Bevor ich protestieren kann, schnappt sie sich mein Mathematik-Buch. Sie hält es mit einer Hand offen und überfliegt die Seite, auf der ich gerade war, während ihr linker Arm nutzlos auf ihrer Hüfte ruht."


"Während meiner Zeit hier auf der Yamaku habe ich bemerkt, dass die anderen Schüler ein breites Spektrum an praktischen Ausgleichen für ihre Behinderungen haben. Miki ist eine von denen, die anscheinend ein paar Probleme damit haben."


"Der Stummel ihres rechtens Arms tendiert dazu, an ihrer Seite herabzuhängen, in eine Tasche gesteckt oder anderweitig aus dem Weg bewegt zu werden. Manchmal hat sie Schwierigkeiten bei alltäglichen Tätigkeiten, was sie sichtlich frustriert."


"Ich fühle mich etwas mies, dass ich so denke, aber ich bin dankbar dafür, dass Hanako und ich keine Behinderungen haben, die unsere Bewegungsfreiheit so sehr einschränken."


"Andererseits… Miki läuft wenigstens nicht Gefahr zu sterben, wenn sich ihr Problem verschlimmert."


show miki smile_close onlayer master
with charachange

"Ich richte meine Aufmerksamkeit wieder auf sie, als sie ein paar Seiten durchblättert und ihren Inhalt überfliegt. Mit solch einem beiläufigem Interesse für das Thema ist es mittlerweile klar, dass sie keine große Hilfe sein wird."


hi "Ich schätze, du interessierst dich nicht für so ein Zeug?"


show miki angry_close onlayer master
with charachange

mk "Scheiß auf Mathe. Es ist langweilig wie Sau."


"Sie legt das Buch gleichgültig wieder auf meinen Tisch. Ihre Augen bewegen sich zu dem daneben liegenden Notizheft, in dem ich Gleichungen Lösen geübt hatte."


show miki confused_close onlayer master
with charachange

mk "Warte, du verstehst das ganze Zeug wirklich?"


hi "Jepp."


show miki wink_close onlayer master
with charachange

mk "Wow. Ich hab noch nie mit einem Computer mit Beinen gesprochen."


hi "Danke… schätze ich. Zumindest schlage ich mich darin besser als in Geschichte."


show miki grin_close onlayer master
with charachange

mk "Kannst du da nicht die Bibliothekarin um Hilfe bitten? Hab gehört, sie will an die Uni."


hi "Ah, Yuuko? Vielleicht. Allerdings weiß ich nicht, was sie studieren will."


hi "Und was ist mir dir? Schon 'ne Idee, was du nach dem Abschluss machen willst?"


show miki grinclosed_close onlayer master
with charachange

mk "Ich? Nee, nicht wirklich. Ich genieße einfach die Zeit, solange ich noch hier bin."


"Sie schaut etwas verlegen drein, als sie nach ihrer Zukunft gefragt wird, und reibt gedankenverloren ihren linken Unterarm. Ich will sie irgendwie danach fragen, aber ich glaube nicht, dass ich sie dafür gut genug kenne."


show miki serious_close onlayer master
with charachange

"Als die Unterhaltung versiegt, lehne ich mich in meinem Stuhl zurück und gebe die Hoffnung auf, noch zum Lernen zu kommen. Miki bemerkt meinen müden Gesichtsausdruck und schaut auf einmal seltsam ernst drein."


mk "Denkst du an Hanako?"


hi "Ist das so offensichtlich?"


show miki wink_close onlayer master
with charachange

mk "Du hast die ganze Zeit zu ihrem Platz gesehen, und du bist ziemlich still gewesen. Ist nicht schwierig, eins und eins zusammenzuzählen."


hi "Ich mache mir nur Sorgen um sie."


show miki serious_close onlayer master
with charachange

mk "Ja, das kann ich mir denken. Sie kann manchmal… seltsam sein."


"Sie klingt etwas genervt, aber ich kann es ihr nicht verübeln. Mit Hanako zu interagieren war schwierig, bevor sie sich für mich erwärmt hat – und das sogar mit Lillys Hilfe."
"Ich kenne sie auch noch nicht so lange, darum sind mir vielleicht auch einige ihrer Gewohnheiten noch unbekannt."


"Meine Miene trübt sich. Wenn ich keine Gefühle für sie entwickelt hätte, wäre es zumindest ein bisschen einfacher, damit umzugehen."


show miki whistle_close onlayer master
with charachange

mk "Ah, das war nicht böse gemeint. Sie ist kein schlechter Mensch, so viel weiß ich."



label de_H25a:

hi "Das weiß ich doch. Es ist nur schwieriger, damit umzugehen, wenn man, na ja, du weißt schon… Wenn man Gefühle für jemanden hat."


show miki serious_close onlayer master
with charachange

mk "Ja, das kann ich mir denken. Es ist auch schwierig, so was zu vergessen wie das, was ihr da im Unterricht passiert ist."


"Ich wünschte, sie hätte mich nicht daran erinnert. Sie hat gerade bestätigt, dass auch die anderen im Raum es bemerkt haben."



label de_H25c:

show miki smile_close onlayer master
with charachange

mk "Komm schon, lass den Kopf nicht hängen. Sie hat das früher auch schon getan, du musst einfach nur abwarten."


"Seit sie an die Yamaku gekommen ist – vielleicht auch schon vorher – sperrt sie sich manchmal für eine ziemlich lange Zeit in ihrem Zimmer ein und verhält sich wie die leere Hülle eines Menschen, und ich soll mir darüber keine Sorgen machen?"


"Na ja, das mag ich zwar denken, aber es gibt nichts, was ich tun kann. Ich kann sie nicht zum Herauskommen zwingen, und sie besucht einen Therapeuten. Also ist es nicht so, als würde sie keine Hilfe für ihre Probleme bekommen."


"Vielleicht ist es normal, so zu denken, wenn man machtlos ist, jemandem zu helfen. „So ist sie einfach, du musst einfach damit zurechtkommen.”"


show bg school_scienceroom onlayer master at center
show miki smile_close onlayer master at twoleft
with charamove

stop music fadeout 3.0

"Während ich über diese Dinge grüble, bemerke ich aus dem Augenwinkel eine Bewegung. Ich sehe hinüber, um zu erkennen, wer es ist – und muss ein zweites Mal hinsehen."


show hanako invis onlayer master:
    right
    xpos 1.1
with None

show hanako basic_normal onlayer master at right
with dissolvecharamove

"Es ist tatsächlich Hanako. Sie läuft durch die Tür, als wäre es ein ganz normaler Schultag, und begibt sich auf ihre übliche ruhige und bescheidene Art zu ihrem Platz."


show hanako emb_downtimid onlayer master
with charachange

"Sie sieht mich einen Augenblick an, bevor sie errötet und verlegen wegsieht, was mich begreifen lässt, dass ich sie gerade angestarrt habe. Das tut mir leid, aber es nicht zu tun ist schwierig nach allem, was passiert ist."


hide hanako onlayer master
with charaexit

play music music_another fadein 4.0

show bg school_scienceroom onlayer master at bgright
show miki grinclosed_close onlayer master at center
with dissolvecharamove

"Das Mädchen, das auf meinem Tisch sitzt, sieht mich grinsend an."


show miki grin_close onlayer master
with charachange

mk "Siehste? Und schon ist dein Schatz wieder zurück. Was hab ich dir gesagt?"


hi "Du sei leise."


"Es war vielleicht nur als Witz gemeint, aber sie liegt nah genug dran, dass mir ziemlich unbehaglich zumute wird."


show miki smile onlayer master
with charadistant

"Während wir reden, ruft jemand von der Tür aus Mikis Namen. Sie springt von ihrem Sitzplatz auf meinem Tisch herunter und wendet sich mir noch einmal zu."


show miki grin onlayer master
with charachange

mk "Ich muss dann, Hisao. Iss mal ab und zu was, verstanden?"


hi "Okay, werde ich. Bis dann."


hide miki onlayer master
with charaexit

"Sie grüßt lässig, bevor sie zur Tür joggt, wo ein männlicher Schüler in Sportuniform auf sie wartet. Wahrscheinlich jemand aus dem Leichtathletikklub."


show bg school_scienceroom onlayer master at right
with charamove_slow

"Ich ergreife die Gelegenheit, stehe auf und begebe mich zu Hanakos Tisch."


show hanako emb_timid onlayer master:
    center
    ypos 1.15
with charaenter

ha "H-Hallo…"


hi "Hi, Hanako. Was gibt's?"


show hanako emb_downtimid onlayer master
with charachange

ha "N-Nichts…"


"Vielleicht war es doch keine so gute Idee, mit ihr zu reden, direkt nachdem sie zurück zum Unterricht gekommen ist."


hi "Willst du mit mir kommen und etwas aus der Cafeteria holen? Ich bin ziemlich hungrig."


show hanako cover_worry onlayer master
with charachange

ha "Aber… ich dachte, du würdest lernen."


"Lernen kann warten. Nach all dieser Zeit zum Unterricht zu erscheinen, muss Hanako einiges an Courage abverlangt haben, also ist bei ihr zu bleiben das Mindeste, was ich tun kann."


"„So ist sie einfach, du musst einfach damit zurechtkommen.” So sehen Miki – und wahrscheinlich auch die ganze Klasse – Hanako. Aber ich kann mehr für sie tun. Ich will mehr für sie tun."


hi "Nachdem ich von Miki abgelenkt wurde, glaube ich nicht, dass ich noch irgendwas zustande bringe. Komm schon, lass uns gehen."


show hanako basic_bashful onlayer master at center
with dissolvecharamove

"Sie zögert, doch schließlich steht sie auf, und wir laufen los. Es mögen kleine Schritte für sie sein, aber die Tatsache, dass sie endlich freiwillig aus ihrem Zimmer gekommen ist, hebt ein großes Gewicht von meinen Schultern."


stop music fadeout 2.0

scene black onlayer master
with dissolve



label de_H26:

scene bg suburb_shanghaiint onlayer master at bgright
with locationchange

play music music_dreamy fadein 2.0

"Mein Stift kritzelt geschäftig auf einer sich langsam füllenden Seite meines Notizheftes."
"Meine andere Hand ruht auf der Seite eines Nachschlagebuchs, das ich mir aus der Bibliothek ausgeliehen habe, um meine gegenwärtige Stelle zu markieren, während meine Augen hin und her huschen."


"Während ich arbeite, mache ich gelegentlich rote Kreise oder unterstreiche etwas auf den kopierten Papierseiten, die auf dem Tisch vor mir liegen."


"Weil ich etwas Abwechslung von der Bibliothek brauchte und die Ablenkungen im Klassenzimmer vermeiden wollte, habe ich beschlossen, das Shanghai aufzusuchen, um in Ruhe zu lernen."


"Wie erwartet war es schön ruhig, und beim Lernen einen Kaffee bekommen zu können ist ein netter Bonus."


"Seit sie aus ihrem Zimmer gekommen ist, mag Hanako zu ihrem normalen Ich zurückkehrt sein, aber bei mir ist so ziemlich Gegenteil der Fall. Die tägliche Routine mag zurück sein, aber ich fühle mich, als wäre ich ein anderer Mensch."


"Vielleicht bin ich es auch nicht. Immerhin ist es erst ein paar Tage her, dass ich beschlossen habe, aus dem Tief zu entkommen, in dem ich nach meinem Unfall versunken bin. Aber ich will mich ändern, und nun arbeite ich aktiv auf dieses Ziel hin."


"Oder zumindest würde ich gerne glauben, dass ich das tue."


hi "Ugh, das ist unmöglich. Es mit roher Gewalt zu erzwingen, wird nicht funktionieren."


"Und außerdem muss ich nach diesem noch ein weiteres Blatt bearbeiten. Ich fürchte, dass das kaum einfacher sein wird."


yu "Ähm…"


"Leicht überrascht sehe ich zum Ursprung der zaghaften Stimme auf."


show yuukoshang worried_up onlayer master at center
with charaenter

"Yuuko steht mit einem feuchten Handtuch in der Hand vor dem Tisch. Eindeutig hat sie die Gelegenheit genutzt, dass keine anderen Gäste da sind, um die Tische zu reinigen. Neugierig springen ihre Augen von meiner Arbeit zu mir und zurück."


hi "Was ist denn?"


show yuukoshang worried_down onlayer master
with charachange

yu "Ich habe mich nur gefragt… Mit welcher Aufgabe hast du denn so viele Schwierigkeiten?"


hi "Oh. Ist nur Geschichte. Mir Naturwissenschaften und Mathe komme ich zurecht, darum versuche ich, meine anderen Fächer zu verbessern."


show yuukoshang happy_up onlayer master
with charachange

"Yuuko scheint meine Antwort sehr zu freuen. Es kommt mir vor, als hätte ich gerade die richtige Antwort in einer großen Quizshow ausgewählt."


show yuukoshang closedhappy_down onlayer master
with charachange

yu "Oh! Ich glaube, damit kann ich dir helfen!"


show yuukoshang worried_down onlayer master
with charachange

yu "Ähm, falls du nichts dagegen hast… natürlich…"


"Kurz wäge ich ab, ob ich das Angebot lieber ablehnen soll, damit ich ihr nicht zu viele Umstände bereite, aber sie sieht so begeistert aus. Es wäre gemein, sie nach so einer Reaktion noch zu enttäuschen."


hi "Wenn du helfen möchtest, würde ich mich echt darüber freuen."


show yuukoshang closedhappy_up onlayer master
with charachange

hide yuukoshang onlayer master
with charaexit

"Sie klatscht ihre Hände zusammen und legt rasch ihr Handtuch auf dem Tresen ab, bevor sie zurückkommt und sich mir gegenüber setzt."


show yuukoshang invis onlayer master at center
with None

show yuukoshang smile_down onlayer master at Position(ypos=1.15)
with dissolvecharamove

"Ich nehme mein Notizheft von meinem Schulbuch herunter und reiche es ihr, damit sie es überprüfen kann."


show yuukoshang neutral_up onlayer master
with charachange

yu "Also befasst ihr euch gerade mit der Edo-Periode?"


hi "Genau. Aber ich bin nicht allzu gut darin."


show yuukoshang worried_up onlayer master
with charachange

"Sie nimmt das Schulbuch und liest in ein paar Seiten aus zufälligen Stellen nahe der Buchmitte, doch die enthusiastische Aura, die sie gerade noch ausgestrahlt hatte, ebbt zügig ab."


hi "Ich schätze mal, das ist nicht die Art von Geschichte, die du erwartet hast?"


show yuukoshang worried_down onlayer master
with charachange

yu "Leider nein. Mein Fachgebiet ist europäische Geschichte, besonders die klassische Ära. Tut mir leid."


"Sie sieht etwas geknickt aus, aber als sie das Buch vorsichtig schließt und es zurück auf den Tisch legt, erhellt sich ihr Gesicht wieder."


show yuukoshang smile_down onlayer master
with charachange

yu "Hättest du gerne eine weitere Tasse Kaffee?"


hi "Hmm? Oh, ja, klar."


show yuukoshang invis onlayer master at center
with dissolvecharamove

"Ich greife nach meinem Buch, während Yuuko aufsteht, meine Tasse nimmt und langsam zum Tresen läuft, um eine weitere aufzubrühen."


"Wie gewohnt ist sie vollkommen still, als sie das tut; jedes bisschen ihrer Konzentration ist darauf gerichtet, nicht zu stolpern oder die schlichte, weiße Tasse fallen zu lassen."


"Ich ergreife die Gelegenheit, um mich zurückzulehnen und etwas zu entspannen. Das Summen der Kaffeemaschine erfüllt die ansonsten ruhige Atmosphäre."


"Es sind Kleinigkeiten wie diese, die mich erkennen lassen, wie sehr ich die kleinen Dinge im Leben zu schätzen gelernt habe."


"Die Ruhe und Gelassenheit des Dorfes hier, die Disziplin und Ordnung an der Yamaku, das Grün der Bäume, das in meiner Heimatstadt so selten war, das entspannte Tempo, mit dem die alternden Bewohner ihre Leben leben…"


"Alles fühlt sich so… beständig an. Es ist beruhigend."


"Ich kann spüren, wie ich langsam einnicke, als das Geräusch der Tasse, die auf dem Tisch abgesetzt wird, meine Aufmerksamkeit auf sich zieht. Scheint, als wäre sie nicht eine Sekunde zu früh angekommen."


show yuukoshang neutral_down onlayer master at Position(ypos=1.15)
with dissolvecharamove

"Yuuko setzt sich erneut auf ihren vorigen Platz, während ich mich aufrichte und eine Hand an die Tasse lege, um die Temperatur zu prüfen. Er ist noch ein bisschen zu heiß, um ihn sofort zu trinken, darum puste ich etwas."


show yuukoshang worried_down onlayer master
with charachange

yu "Es ist schade, dass du Geschichte nicht so sehr magst. Irgendwie habe ich mir gedacht, dass du eher der wissenschaftliche Typ bist."


hi "Wie das?"


show yuukoshang smile_up onlayer master
with charachange

yu "Du hast schon fast die ganze Science Fiction Abteilung der Bibliothek gelesen. Das zu bemerken, war nicht schwierig."


hi "Damit hast du wohl Recht. Na ja, was soll ich sagen? Du hast den Nagel auf den Kopf getroffen."


show yuukoshang neutral_down onlayer master
with charachange

hi "Allerdings klingst du, als würde dich Geschichte echt interessieren, besonders wenn man bedenkt, wie konkret du gerade warst. Studierst du in in diesem Gebiet, oder so? Ausgrabungen in anderen Ländern?"


show yuukoshang closedhappy_up onlayer master
with charachange

"Bei dem Gedanken kichert sie nervös."


show yuukoshang neurotic_down onlayer master
with charachange

yu "Ich würde irgendwann gerne mal das Mittelmeer besuchen und die alte Architektur mit meinen eigenen Augen sehen, aber ich glaube nicht, dass ich in die Nähe solch empfindlicher Dinge gehen sollte."


show yuukoshang neutral_down onlayer master
with charachange

yu "Ich spare, um das an der Universität studieren, aber ich lese auch viel darüber, wann immer ich außerhalb der Arbeit etwas Freizeit habe."


"Also hatte Miki Recht wegen ihrer Universitätsbestrebungen. Wenn man bedenkt, wie sie sich als Kellnerin schlägt, würde ein mehr theoretischer Weg eher zu Yuuko passen. Es ist schön zu hören, dass sie nach etwas strebt, so hart wie sie arbeitet."


"Ich nicke und nehme vorsichtig einen Schluck von meinem Kaffee. Mittlerweile hat er sich auf die richtige Temperatur abgekühlt, darum fange ich an zu trinken, während ich ein Auge auf das Buch vor mir werfe und versuche, es zu lesen."


"Ein paar Minuten vergehen ohne Worte, als Yuuko aus dem Fenster sieht und der Welt zuschaut, während ich meinen Kaffee trinke und lerne."


show yuukoshang closedhappy_up onlayer master
with charachange

"Eine Bewegung fällt mir ins Auge, und ich hebe den Kopf, um zu sehen, wie Yuuko lächelt und jemandem draußen zuwinkt. Als ich ihrem Blick Folge, stellt sich dieser Jemand überraschenderweise als Hanako heraus."


"Sie sieht von der anderen Seite der Straße zu uns hinüber. Ihre normalerweise nur allzu gut erkennbare Schüchternheit fehlt größtenteils, wahrscheinlich weil gerade so wenig Leute in der Nähe sind."


"Offenbar entschließt sie sich, sich zu uns zu gesellen, da sie nach einem kurzen Winken die Straße auf und ab schaut und sie dann überquert."


$ renpy.music.set_volume(0.3, 0.0, channel="sound")
play sound sfx_storebell

show hanako invis onlayer master:
    right
    xpos 1.0
with None

show yuukoshang happy_up onlayer master:
    twoleft
    ypos 1.15
show bg suburb_shanghaiint onlayer master at center
show hanako basic_normal onlayer master at tworight
with dissolvecharamove

"Die vertraute Türglocke des Shanghai ertönt, als Hanako eintritt und sich zu dem Tisch begibt, an dem wir sitzen."


show hanako cover_distant onlayer master at Position(ypos=1.15)
with dissolvecharamove

ha "H-Hallo…"


show yuukoshang smile_down onlayer master
with charachange

yu "Guten Tag."


hi "Hi, Hanako. Was gibt's?"


with charachange

ha "N-Nichts… ich war nur… e-etwas spazieren… weil das Wetter so schön ist."


hi "Ja, ich weiß, was du meinst. Ich bin froh, dass ich mich entschieden habe, hier zu lernen anstatt in der Bibliothek."


"Hier ist es richtig gemütlich – besser als in der manchmal recht stickigen Bibliothek. Ich sehe zu Yuuko, die als Antwort nickt."


show yuukoshang neutral_down onlayer master
with charachange

yu "Das ist es. Es ist nur schade, dass der Sommer nicht für immer anhalten kann."


show yuukoshang neurotic_up onlayer master
with charachange

yu "Oh warte, entschuldige, ähm, würdest du gerne etwas trinken?"


show hanako basic_smile onlayer master
with charachange

show yuukoshang neutral_down onlayer master
with charachange

"Hanako schüttelt ihren Kopf. Zum Glück ist das genug, um Yuuko wieder zu beruhigen."


show hanako basic_bashful onlayer master
with charachange

ha "W-Wie kommst du mit dem Lernen voran?"


hi "Es geht… so."


hi "Ah ja, hast du mit Lilly gesprochen?"


show yuukoshang smile_up onlayer master
with charachange

yu "Das interessiert mich auch; wie geht es ihr?"


show hanako cover_worry onlayer master
with charachange

ha "I-Ihr gefällt es… glaube ich."


"Ich… glaube, das ist alles, was wir aus ihr herausbekommen werden. In Yuukos Nähe zu sein, macht sie nervös."


show yuukoshang closedhappy_down onlayer master
with charachange

yu "Ah, es wäre so schön, nach Schottland zu reisen."


show yuukoshang happy_down onlayer master
with charachange

yu "Grüne Wiesen, Burgen, entzückende kleine Städte, Männer in Kilts, interessante Geschichte…"


"Von mir kann ich nicht behaupten, dass mich Männer in Kilts reizen. Aber es scheint ein malerischer Ort zu sein."


play sound sfx_storebell

show hanako defarms_shock onlayer master
show yuukoshang panic_up onlayer master
with vpunch

"Während wir reden, ertönt die Türglocke erneut. Hanako schreckt auf, als sie Yuukos panischen Gesichtsausdruck bemerkt. Panik, weil die Kunden vielleicht ein paar Sekunden warten müssen, weil sie mit uns geplaudert hat."


show yuukoshang worried_down onlayer master at twoleft
with Dissolvemove(0.3)

with Pause(0.2)

hide yuukoshang onlayer master
with charaexit

"Yuuko verbeugt sich kurz und huscht dann hastig zum Eingang und begrüßt die neuen Gäste – ein älterer Mann und seine Frau. Ich sehe ihr ein wenig dabei zu und recke meinen Hals, um einen guten Blick zu bekommen."


show hanako def_worry onlayer master
with charachange

"Hanako starrt mich mit ihrem einen sichtbaren Auge an."


show hanako def_worry onlayer master:
    center
    ypos 1.15
show bg suburb_shanghaiint onlayer master at bgleft
with charamove

show hanako emb_downtimid onlayer master
with charachange

"Verlegen wendet sie ihren Kopf ab, als ich Augenkontakt mit ihr herstelle."


hi "Ich dachte mir nur, dass es schön ist, Ambitionen für die Zukunft zu haben. Yuuko hat mir vorhin etwas über ihre Universitätspläne erzählt."


show hanako emb_timid onlayer master
with charachange

ha "Oh."


hi "Es ist schade. Wenn sie nicht so neurotisch und überarbeitet wäre, glaube ich, dass sie wirklich glücklich sein könnte."


"So sehr ich Hanako auch bewirten und sie etwas unterhalten will, muss ich mich doch auch aufs Lernen konzentrieren. Um ehrlich zu sein, glaube ich auch nicht, dass mir die Ablenkung von Yuuko geholfen hat."


hi "Entschuldige, wenn ich etwas abgelenkt bin. Ich muss das hier fertigkriegen, andernfalls rassle ich knallhart durch die Geschichtsprüfung."


"Ich fahre mir frustriert mit der Hand durch mein Haar. Um den Brief muss ich mich auch noch kümmern, sobald ich wieder zurück in meinem Wohnheimzimmer bin."


hi "Ich hoffe, ich habe damit mehr Glück als hiermit. Verdammt."


show hanako emb_downtimid onlayer master
with charachange

ha "W-Womit?"


hi "Oh, äh… Ich wollte… Iwanako schreiben. Im Moment ist aber das hier wichtiger."


"Jetzt habe ich mich nur selbst nervös gemacht. Ich kann mich nicht auf die Arbeit vor mir konzentrieren, wenn mein Magen sich bei dem Gedanken umdreht, ihr nach all dieser Zeit wirklich zurückzuschreiben."


"Ich zwinge mich dazu, mich auf das Buch zu konzentrieren, und nehme nach einem kurzen Schluck Kaffee meinen Stift in die Hand."


show hanako basic_distant onlayer master
with charachange

"Nach ein paar Sekunden hört Hanako auf, mich still zu beobachten, und lehnt sich in ihrem Sitz zurück. Sie entspannt sich so gut sie kann und sieht aus dem Fenster, um sich die Zeit zu vertreiben."


$ renpy.music.set_volume(1.0, 0.0, channel="sound")
stop music fadeout 3.0

"So verweilen wir eine lange Zeit, bis wir uns zusammen auf den Rückweg zu den Wohnheimen machen. Ich bin überrascht, dass sie die Geduld hatte, auf mich zu warten."


scene ev hisao_letter_open onlayer master
with shorttimeskip

play music music_night fadein 1.0

"Iwanakos Brief liegt auf meinem Tisch neben einem leeren, linierten Blatt Papier und einem unbenutzten Briefumschlag."


"Wie ich befürchtet habe, stellt sich meine zweite Aufgabe des Tages als genauso schwierig wie die erste heraus – wenn nicht sogar schwieriger."


"Es ist so viele Monate her, dass wir uns das letzte Mal gesehen haben. Trotzdem kann ich mich immer noch daran erinnern, wie sie aussah, wie sie klang und wie sie sich verhielt. Doch mittlerweile beginnen die kleinen Details zu verblassen."


"Als ich ihren Brief zum ersten Mal sah, erkannte ich kaum ihre Handschrift. Sogar den pinken Stift, den sie immer benutzte, hatte ich vergessen, bis der Brief mich an ihn erinnert hat."


"Ich frage mich, warum sie ihn nicht für den Brief benutzt hat; sie hat sonst alles damit geschrieben. Vielleicht denkt sie nun, er wäre zu kindisch."


"Ich sollte über mich selbst nachdenken und über das, was ich ihr mitteilen will. Aber meine Gedanken wandern immer wieder zu ihr und zu der Zeit, die wir gemeinsam verbracht haben, bevor alles so abrupt endete."


"Die grellen und etwas aufdringlichen Verzierungen passen zu ihrer Vorstellung von Ästhetik. Als ich den Brief aufhebe, um ihn mir genauer anzusehen, gebe ich ein langes Seufzen von mir."


"Das ist die letzte Verbindung zu meiner Vergangenheit. Iwanako hat nicht plötzlich aufgehört zu existieren, als sie zum letzten Mal mein Krankenhauszimmer verließ, aber ich habe diesen Brief gebraucht, um mich daran zu erinnern."


"Ich hatte all diese Gefühle säuberlich zu den Akten gelegt. Ich dachte, ich bräuchte sie nicht – dass ich das Leben einfach komplett von vorne beginnen könnte. Auf diese Weise war es einfacher."


"Am Ende war das vermutlich ein eher naiver Gedanke. Früher oder später würde mich meine Vergangenheit so oder so einholen."


"Aber was soll ich ihr sagen? „Danke, dass du mir geholfen hast, mit dem Thema abzuschließen.”? Wenn überhaupt, dann hat der Brief alte Wunden wieder aufgerissen."


"So sehr ich es auch versuche, ich kriege kein einziges Wort zu Papier. Ich weiß nicht einmal, was genau ich sagen will."


stop music fadeout 4.0

scene bg school_dormhisao_ss onlayer master
with locationchange

"Ich lege den Brief auf das leere Blatt, sammle all mein Schreibzeug zusammen und lege es in meine Schublade."


"Das dumpfe Geräusch, das beim Schließen der Schublade entsteht, erfüllt mich Augenblicklich mit Frust. Dann stehe ich auf, um mir ein Getränk aus dem Verkaufsautomaten im ersten Stock zu holen."


scene bg school_dormhallway onlayer master
with locationchange

"Ich habe es versucht, konnte es aber nicht. Nach all der Zeit, die vergangen ist, weiß ich immer noch nicht, wie ich mit Iwanako umgehen soll."


scene black onlayer master
with dissolve



label de_H27:

scene bg school_library onlayer master
with locationchange

play music music_happiness

"Die Bibliothek ist merklich voller als sonst, obwohl sie nicht gerade vor Betriebsamkeit brodelt."
"Die Prüfungen sind nicht mehr weit, und das spiegelt sich in der Zahl von Schülern wider, die an den Tischen um uns herum ihre Nasen in Lehrbücher stecken."


"In den letzten paar Tagen war ich ziemlich oft am Lernen, genau wie sie in der Hoffnung, bei den Prüfungen gut abzuschneiden."
"Das bedeutet auch, dass Hanako und ich weniger Spiele gespielt haben. Darum hat sie – nur um die Zeit auszufüllen – ebenfalls angefangen zu lernen."


"Nichtsdestotrotz hat sie mich an diesem speziellen Tag alleingelassen."


"Das Schulbuch vor mir ist schon seit einiger Zeit auf der gleichen Seite aufgeschlagen. Nachdem ich nur für die Prüfungen so viel über Themen gelesen habe, die mich nicht weniger interessieren könnten, beginnt mein Verstand abzuschweifen."


"Ich bemerke, wie meine Augen dorthin huschen, wo Hanako normalerweise wäre – genau wie an den Tagen, an denen sie nicht im Unterricht war. Ihr gewohnter Sitzsack in der Ecke des Raumes ist auffällig leer."


"Es war hier, dass wir uns das erste Mal trafen. Ich versuchte, eine Unterhaltung mit ihr zu beginnen, sie wurde scheu und stürmte schließlich aus dem Raum."


"Wahrscheinlich sollte ich darüber nicht lächeln, aber rückblickend war es irgendwie amüsant."
"Heutzutage wird es immer schwieriger, sich vorzustellen, dass sie so etwas tut. Jetzt, wo sie aus ihrem Zimmer gekommen ist, schlägt sie sich auch ganz wacker, obwohl Lilly nicht da ist."


"Ich will mit ihr reden, oder wenigstens wieder einmal mit ihr Schach spielen. Ich bin das Lernen leid, und es ist ein paar Tage her, dass wir richtig etwas zusammen unternommen haben."


"Die Frage, wo man Hanako finden kann, ist nicht besonders schwierig. Wenn sie nicht in der Bibliothek ist, ist sie entweder für etwas Ruhe und Frieden im Teezimmer oder in ihrem Zimmer im Wohnheim."


"Ich beschließe, diese Orte in dieser Reihenfolge abzuklappern, packe meine Bücher zusammen und verlasse die Bibliothek."


stop music fadeout 5.0

scene bg school_girlsdormhall onlayer master
with shorttimeskip

"Während ich den Flur entlanglaufe, strecke ich mich und gebe ein lautes Stöhnen von mir. Lernen mag manchmal frustrierend sein, aber ich glaube, ich habe gute Fortschritte gemacht, und das macht mich auch etwas stolz. Ein gutes Gefühl."


scene bg school_dormhanako_ni onlayer master
show hanako_door_base onlayer master at right
show hanako_door_door onlayer master at left
with locationchange

"Es ist kein Geräusch von drinnen zu hören, als ich vor der Tür zu Hanakos Zimmer stehe. Ich schätze, das sagt mir nicht wirklich, ob sie da ist oder nicht, so ruhig wie sie normalerweise ist."


"Aber sie war nicht im Teezimmer. Ich versuche, leicht zu klopfen, um meine Gegenwart kundzutun, bin aber überrascht, als sich die Tür als unverschlossen herausstellt und bei meiner Berührung nachgibt."


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
show hanako basic_distant onlayer master:
    center
    ypos 1.15
with silentwhiteout

"Mit einem leisen Knarren öffnet sich die Tür. Es sieht aus, als wäre mein Verdacht korrekt; Hanako ist tatsächlich hier."


"Sie sitzt am Tisch mit einem offenem Buch vor sich, aber sie schenkt ihm keine Beachtung und sieht aus dem Fenster. Sie sieht aus, als würde sie meine Anwesenheit gar nicht bemerken."


"Während ihr Kopf nachdenklich auf ihrer Hand ruht, sieht sie ruhig und gefasst aus. Es ist schade, dass sie nicht öfter so aussehen kann."


show hanako basic_distant_close onlayer master:
    center
    ypos 1.1
with characlose

"Mit einem kleinen Lächeln laufe ich zum Tisch und spreche sie leise an."


hi "Guten Abend, Hanako."


show hanako basic_normal_close onlayer master
with charachange

"Hanakos Kopf dreht sich ein wenig, um mich anzusehen, aber sie ist nur halb da. Ich lege eine Hand auf den Tisch und senke meinen Kopf, um ihr besser ins Gesicht sehen zu können. Ich bin etwas neugierig, in welcher Stimmung sie ist."


hi "Wie geht's?"


show hanako basic_worry_close onlayer master
with Dissolve(0.2)

"Sie schnappt kurz nach Luft und nimmt endlich meine Anwesenheit wahr."


"Hanako läuft knallrot an. Ihr Mund ist ein bisschen geöffnet, als wollte sie etwas sagen. Am Auffallendsten ist jedoch das, was sie tut."


scene ev hanako_eye onlayer master:
    truecenter
    subpixel True zoom 0.9
    acdc_warp 20.0 zoom 1.0
with locationchange

"Sie schaut mich direkt an. Ihre Augen sind an meine eigenen geheftet, aus so kurzer Distanz, dass ich beinahe meine eigene Reflektion in ihnen erkennen kann."
"Weder wenden sie sich ab noch regen sie sich in irgendeiner Weise. Sie stehen absolut still und blicken nur in die meinen."


"Sie sind dunkel und verleihen ihr einen fast analytischen Blick. Selbst wenn sie über Themen liest, für die sie kein Interesse hat, wirkt sie für einen oberflächlichen Beobachter, als wäre sie in ihre Arbeit vertieft."
"Sie absorbiert Informationen sehr gut, und sogar jetzt kann ich das spüren."


"Es kommt mir vor, als würde ich etwas hinter diesen Augen sehen, das ich noch nie zuvor gesehen habe, aber ich weiß nicht, was es ist."


hi "Hanako…?"


"Ihre Lippen bewegen sich kaum merklich und formen lautlos Worte. Sie sieht aus, als wäre sie kurz davor, etwas zu sagen, tut es aber nicht."


"Aber so ist Hanako immer. Sie ist kurz davor, etwas zu sagen, aber sie tut es nie wirklich. Als ich aufmerksam in ihre Augen sehe, bemerke ich etwas."


"Jeder hat seine eigenen Gedanken. Dinge, die er sagen will, seine eigene Weltsicht. Aber ich kann nicht ergründen, was Hanako sagen will – genauso wenig was sie gerade denkt. Dazu war ich noch nie in der Lage."


"Es ist frustrierend. Ich komme mir vor, als würde ich sie gar nicht kennen, trotz all der Zeit, die wir zusammen verbracht haben."


ha "Hi… sao…"

scene bg school_dormhanako onlayer master
show hanako basic_worry_close onlayer master
with charachange

"Und jetzt werde ich rot. Ich habe aus so kurzer Distanz direkt in Hanakos Augen gesehen, ohne sie dabei auch nur beachtet zu haben, und sie hat in meine gesehen ohne auszuweichen."


show hanako emb_downtimid_close onlayer master
with charachange

"Schnell sehe ich weg und verberge dabei mein Gesicht mit meiner Hand. Hanako tut genau das Gleiche."


"Es herrscht eine weitere peinliche Stille. Ich hasse so etwas. Anfangs habe ich sie einfach als Teil des Umgangs mit Hanako akzeptiert, aber nun fühlen sie sich alle an, als wären sie ein Bestätigung für unsere Unfähigkeit zu kommunizieren."


"Etwas Zorn bahnt sich seinen Weg in die komplexe Mischung aus Gefühlen, die mich gerade durchströmt. Ich will diese Kluft zwischen uns überbrücken. Freunde sollten nicht so zögerlich miteinander umgehen."


"Ich spreche lieber, bevor ich mich aus dem herausrede, was ich gleich tun werde. Meine Narbe ist nicht so schlimm wie Hanakos, und ich kann mein Leben unmöglich mit ihrem vergleichen, aber ich will ihr zeigen, dass sie nicht allein ist."


"Dies auf schonungslose Art zu tun, könnte der einzige Weg sein, um meinen Standpunkt deutlich zu machen."


hi "Hanako… Ich will dir etwas zeigen."


show hanako emb_timid_close onlayer master
with charachange

"Ich nehme einen tiefen Atemzug, um mich vorzubereiten. Das könnte krass nach hinten losgehen, aber ich glaube, wir sollten uns dafür nah genug gekommen sein."


hi "Ich werde mich nicht nackt ausziehen oder irgendwas Komisches tun, ich werde nur mein Hemd ausziehen."


show hanako def_shock_close onlayer master at center
with dissolvecharamove

"Hanakos Augen weiten sich auf die Größe von Untertassen. Auf ihrem Gesicht zeichnet sich eine lustige Mischung aus Neugier und Nervosität ab. Es hilft, mir die schlimmste meiner Aufregung zu nehmen, dies vor einer anderen Person zu tun."


play sound sfx_rustling

"Langsam, mit einem völlig angespannten Körper, löse ich den Knoten meiner Krawatte und beginne, die ersten Knöpfe zu öffnen."
"Dabei versuche ich, Hanako aus meinen Gedanken zu verdrängen, um es einfacher zu machen, aber es funktioniert nicht wirklich."


"Während ich mich weiter hinabarbeite, rechne ich damit, dass sie protestiert, aber sie bleibt still, wodurch mir das Ganze nur noch komischer vorkommt."


"Nachdem ich den letzten Knopf meines Hemdes aufgeknöpft habe, hole ich tief Luft und sehe sie an."


scene ev hisao_scar_large onlayer master:
    xanchor 0 yanchor 0 xpos -600 ypos -140 
with whiteout

play music music_heart fadein 0.5

"Hanakos Blick haftet wie erwartet auf meiner Narbe, und sobald ich ihr zunicke, um zu sagen, dass es okay ist, macht sie einen Schritt nach vorne und legt ihre Hand auf die Linie, die vertikal meine Brust hinabführt."


show ev hisao_scar_large onlayer master:
    ease 1.0 xpos 0 ypos -290

"Die Narben auf ihrer Hand – ein Muster aus beschädigter Haut – kontrastiert mit der einzelnen, gleichförmigen Linie auf meiner Brust. Anders als ich es mir vorgestellt hatte, zittert ihre Hand überhaupt nicht."


ha "Das ist…"


hi "Die Narbe von meiner Operation nach meiner Herzattacke. Die Chirurgen mussten meinen Brustkorb aufschneiden, um an meinem Herzen zu operieren."


show ev hisao_scar_large onlayer master:
    ease 1.0 xpos -600 ypos -140 

ha "Ich wusste nie…"


"Hanakos Worte sind ruhiger und sanfter als sonst. Das weiche Gefühl ihrer Finger, die sich von meiner Narbe zu meiner Brust bewegen, lässt mich etwas zögern, bevor ich fortfahre."


hi "Du bist der erste Mensch, der das sieht, seit ich das Krankenhaus verlassen habe."


scene ev hisao_scar onlayer master:
    truecenter
    zoom 1.05 subpixel True
    easein 8.0 zoom 1.0
with flash

ha "Aber… wieso zeigst du mir das?"


hi "Ich wollte mir selbst beweisen, dass ich das tun kann; dass ich meine Vergangenheit akzeptieren und voranschreiten kann. Und ich wollte es dir zeigen."


"Sie nickt. Ihrer Reaktion nach scheint sie zu wissen, wie schwierig das für mich ist. Mehr als alles andere stellt diese Narbe eine sichtbare Erinnerung an meine Krankheit dar. Eine Erinnerung daran, dass ich nicht mehr „normal” bin."


"Das ist etwas, was ich bis jetzt mit aller Kraft zu ignorieren versucht hatte."


"Während die Minuten vergehen, verweilt Hanakos Blick auf mir. Ihr Augen fokussieren sich nicht mehr so sehr auf meine Narbe wie eben noch. Die Situation fühlt sich etwas anders an als zuvor, und das gibt mir ein etwas unbehagliches Gefühl."


scene bg school_dormhanako onlayer master
show hanako basic_normal_close onlayer master at center
with silentwhiteout

"Ihre Hand zieht sich zurück, woraufhin ich mein Hemd richte und anfange, es wieder zuzuknöpfen. Als sie wegsieht, nimmt ihr gerötetes Gesicht plötzlich wieder seinen gewohnten schüchternen und angespannten Ausdruck an."


"Der Raum ist vollkommen still, während ich mein Hemd und meine Krawatte richte. Nach einem so unerwartet intimen Moment weiß ich nicht so genau, wie es weitergehen soll."


hi "Also… bist du wohl nicht die einzige mit Narben."


show hanako basic_smile_close onlayer master
with charachange

"Hanako lächelt ein bisschen über diesen Witz, was zum Glück die Stimmung etwas aufhellt."


ha "Danke… H-Hisao. Ich glaube… ich verstehe."


"Ich gebe einen langes, erleichtertes Seufzen von mir. Ich wusste wirklich nicht, wie sie es aufnehmen würde, aber ich bin froh, dass scheinbar alles so geklappt hat, wie ich es gehofft hatte. Hanakos Lächeln bestätigt das."


"Ich finde nun meinen Pfad, dem ich folgen will, und was Hanako tun muss, ist, ihren eigenen zu finden. Es ist etwas, womit ich ihr nicht helfen kann, und es ist etwas, wofür sie ihre Vergangenheit überwinden muss."


show hanako basic_distant_close onlayer master
with charachange

"Hanako sieht auf ihre Uhr. Es wird mittlerweile spät."


show hanako basic_worry_close onlayer master
with charachange

ha "Hisao… ähm…"


hi "Ja, ich sollte besser los. Ich wäre dankbar für etwas Schlaf. Immerhin war es ein langer Tag."


hi "Gute Nacht, Hanako."


show hanako basic_bashful_close onlayer master
with charachange

ha "G-Gute Nacht."


stop music fadeout 3.0

scene bg school_girlsdormhall onlayer master
with locationchange

"Schweigend verlasse ich ihr Zimmer. Ich denke, wir beide haben heute einige Emotionen durchlebt."


scene black onlayer master
with dissolve



label de_H28:

scene bg city_street1 onlayer master
with locationchange

play music music_daily fadein 2.0
$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_traffic fadein 2.0

"Die Hitze der Sommersonne knallt auf meine schwitzende Stirn. Sie mit dem Taschentuch abzutupfen, macht es nicht wirklich angenehmer."


"Nachdem ich die Idee aufgegeben habe, heute noch etwas zustande zu bringen, bleibe ich stehen und lehne mich gegen den Zaun des Hochweges. Meine Tasche lege ich auf den Boden."


"Die Läden in dem Dorf unter Yamaku sind gut ausgestattet und ihre Auswahl ist für mich vielfältig genug, um über die Runden zu kommen, aber zumindest ein gelegentlicher Einkaufstrip in die Stadt lässt sich nicht wirklich vermeiden."


"Hier bin ich nun schon einige Male gewesen. Der Grundriss der Stadt wird mir vertrauter, und die Nostalgie ihrer Atmosphäre beginnt nachzulassen."


"Ich bemerke, dass ich angefangen habe zu keuchen. Ich klinge wie ein alter Mann, der sich überanstrengt hat, und diese Tatsache zu akzeptieren, ist ein bisschen verstörend."


"Ich lege eine Hand auf meine Brust und konzentriere mich eine Weile, um sicherzustellen, dass ich nicht so weit gegangen bin, dass noch weitere Probleme auftreten."


"Glücklicherweise verhält sich mein Herz normal. Es gibt keinen dumpfen Schmerz, und der Rhythmus ist gleichmäßig, wenn auch recht schnell, während ich mich davon erhole, mich in dieser Hitze so angestrengt zu haben."


"Ich hasse meinen Körper. Zurückgehalten zu werden ist frustrierend, und sogar noch mehr, weil es aus Angst ist, mein Leben könnte in Gefahr sein, wenn ich etwas so Simples tue, wie eine Weile lang in der Stadt herumzulaufen."


$ renpy.music.set_volume(0.2, 0.0, channel="sound")
play sound sfx_phone

"Während ich über meine Gesundheit nachdenke, spüre ich meine Hosentasche vibrieren. Bis mein Handy anfängt zu klingeln, habe ich es bereits herausgefischt."


"Ein Blick auf das Display zeigt eine Nummer, die ich nicht wiedererkenne. Seltsam."


$ renpy.music.set_volume(0.1, 2.0, channel="ambient")
$ renpy.music.set_volume(0.5, 2.0, channel="music")

scene bg city_street1_blurred onlayer master
show phone mobile onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)

"Schulterzuckend drücke ich den Annahmeknopf und lege das Telefon an mein Ohr."


hi "Hallo, hier ist Hisao Nakai."


mystery "…"

"Ich kann ein paar kurze Atemzüge hören, aber niemand sagt etwas."


hi "Hallo?"


ha "H-Hisao?"

"Es ist Hanako. Ihre Stimme ist wirklich einfach einzuordnen, auch wenn ich sie nie zuvor durch ein Telefon gehört habe."


hi "Hanako? Sorry, ich hatte nicht damit gerechnet, dass du anrufst. Was gibt's?"


ha "Ä-Ähm… Ich… ähm…"


ha "Wenn… wenn du nichts zu tun hast… w-wollte ich fragen, o-ob du… d-dich vielleicht mit mir tre…"


hi "… treffen willst?"


ha "Ja! Ä-Ähm… ich meine…"


"Sie klingt deswegen wirklich nervös. Ich kann gedämpfte Stimmen im Hintergrund hören, und es ist langsam Zeit für den Nachmittags-Tee. Also vermute ich, dass sie mich im Shanghai oder so treffen will."


hi "Das klingt gut. Bist du im Shanghai?"


ha "I-Ich bin… in der Stadt…"


"Hanako ist hier? Allein? Das ist eine Überraschung. Es ist kein Wunder, dass sie so nervös ist, so ganz allein und umringt von Menschen."


hi "Das passt gut; ich spaziere gerade hier herum. Wo bist du?"


"Hanako schafft es, die Adresse und ein paar einfache Richtungsanweisungen zu stammeln. Zum Glück ist es nicht allzu weit weg, darum machen wir direkt einen Treffpunkt aus."


$ renpy.music.set_volume(1.0, 0.0, channel="sound")
$ renpy.music.set_volume(1.0, 1.0, channel="music")
stop ambient fadeout 2.0

show phone mobile onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 0.5 ypos 0.6
with None

scene bg misc_sky onlayer master
with locationchange

stop music fadeout 5.0

"Ich sehe zum Himmel hinauf. Die Sommerhitze knallt herab."


"Das ist das erste Mal, dass Hanako gefragt hat, ob wir über ein schlichtes Brettspiel hinaus etwas unternehmen wollen, und das erste Mal – zumindest seit ich sie kennengelernt habe – dass sie allein in die Stadt gegangen ist."
"Vielleicht bedeutet das, dass Lilly Recht hatte."


scene bg city_karaokeint onlayer master
with shorttimeskip

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_soothing fadein 2.0
$ renpy.music.set_volume(0.4, 0.0, channel="ambient")
play ambient sfx_crowd_outdoors fadein 2.0

"Bis ich zu dem Café getorkelt bin, wo Hanako auf mich wartet, habe ich schon wieder angefangen zu keuchen. Ich schwitze so sehr, dass ich mich wie ein schmelzendes Eis am Stiel fühle, und die Tasche und in meiner Hand kann ich kaum noch halten."


"Ich muss mich hinsetzen. Dringend."


"Die Tische draußen sind alle von sich eifrig unterhaltenden Pärchen und schnatternden Mädchen besetzt."
"Der Kontrast zwischen den verschiedenen Altersgruppen und Kleidungen der Menschen hier und in dem Dorf nahe Yamaku ist bemerkenswert."


"Ich überfliege die an den Tischen sitzenden Leute, kann Hanako aber nicht entdecken. Sie sagte, sie würde draußen sitzen, also muss ich sie einfach übersehen. Keine große Sache, wenn man bedenkt, wie klein sie ihre Präsenz normalerweise machen will."


"Ich sehe mich noch einmal um, diesmal langsamer, und achte besonders auf Hanakos Kappe. Sie ist ziemlich auffällig, und ich wäre sehr überrascht, wenn sie sie nicht tragen würde."


"Da ist sie. Tatsächlich ist ihr Kopf eingezogen und der Tisch, an dem sie sitzt, ist direkt neben dem Gebäude in einer unauffälligen Ecke."


$ renpy.music.set_volume(0.2, 4.0, channel="ambient")

"Ich laufe zu ihr und stelle sicher, dass ich ihre Aufmerksamkeit habe, bevor ich mich hinsetze, damit ich sie nicht erschrecke. Sie bemerkt mich und winkt kurz, als ich bei ihrem Tisch ankomme."


show hanako basic_worry_cas_close onlayer master:
    center
    ypos 1.1
with charaenter

ha "G-Geht's dir gut?"


"Ich gebe meine Bestes, um es mit einem Lachen abzutun, aber das bringt mich nur noch mehr außer Atem."


hi "Bin zur Zeit nur nicht mehr ganz so fit. Mach dir keinen Kopf."


show hanako basic_distant_cas_close onlayer master
with charachange

"Hanako nickt, sieht aber trotzdem etwas besorgt aus."


"Jetzt, wo ich einen guten Blick auf ihr Gesicht habe, wirkt etwas an ihr ein wenig anders. Ich bin mir nicht sicher, ob meine Augen mir einen Streich spielen, aber sie sieht ziemlich gut aus."


show hanako basic_normal_cas_close onlayer master
with charachange

show hanako basic_distant_cas_close onlayer master
with charachange

"Ihr Augen sehen zu mir auf, bevor sie sich wieder nach unten richten. Ich fange an zu glauben, dass dies ein eher stilles Treffen wird, aber glücklicherweise kommt eine Kellnerin an unseren Tisch und stellt eine Tasse Tee vor Hanako hin."


show hanako emb_downtimid_cas_close onlayer master
with charachange

"Fast automatisch dreht sich Hanako leicht weg und senkt ihren Kopf. Eine beeindruckend geübte Bewegung, und sie erfüllt ihren Zweck recht gut: Ihre Narben vor jemanden zu verstecken, der in die Nähe ihres Gesichtes kommt."


"Allerdings liegt ihr rechter Arm immer noch auf dem Tisch, wo die Narben auf ihrem Handrücken gut zu sehen sind. Sie fallen der Kellnerin ins Auge, und ich versuche schnell, sie davon abzulenken."


hi "Entschuldigen Sie, dürfte ich etwas bestellen?"


"Die Kellnerin nickt und gibt mir ein paar Sekunden, um in die Karte zu schauen."


hi "Könnte ich bitte einen Mango-Smoothie haben?"


"Sie nickt mir zu, bevor sie fast begeistert nach innen schwebt. In der Stadt ist alles so anders, auf mehr als nur eine Art."


show hanako emb_timid_cas_close onlayer master
with charachange

"Hanako sieht wieder zu mir auf und richtet etwas ihre Kappe. Wenn sie bemerkt hat, dass die Kellnerin ihre Narben angestarrt hat, zeigt sie es zumindest nicht."


ha "K-Kein Kaffee…?"


hi "Ich glaube, ich würde in dieser Hitze sterben, wenn ich jetzt so was wie einen Kaffee trinken würde."


show hanako emb_downtimid_cas_close onlayer master
with charachange

"Während ich meinen Kopf auf meiner Hand ruhen lasse, sehe ich meine stille Gefährtin an. Sie ist anscheinend etwas verblüfft; eine sehr unerwartete Reaktion auf meinen lahmen Witz."
"Ein unwillkommenes Gefühl wallt in mir auf, als mir ihr Grund dafür klar wird."


"Anders als die Meisten an der Yamaku – oder besser anders als bei jedem, den ich kenne – geht meine Krankheit über das bloße Einschränken meiner Handlungsmöglichkeiten hinaus."
"Oder genauer gesagt, würde es viel schlimmere Konsequenzen haben, über diese Einschränkungen hinauszugehen."


"Gott sei Dank ist das etwas, das sehr selten passiert ist, seit ich an die Yamaku gekommen bin. Ich dachte, es wäre so selten, dass Hanako und Lilly überhaupt nicht daran denken. Nun stellt sich heraus, dass ich falsch lag."


"Während ich auf meinen Smoothie warte, nippt Hanako schweigend an ihrem Tee, um sicherzustellen, dass er die richtige Temperatur hat, dann trinkt sie einen Schluck."


"Ich fühle mich schuldig, die Ursache für diese unangenehme Stille zu sein, denn in der Vergangenheit war ich genau wegen so etwas recht hart zu ihr."


"Schließlich kommt die gleiche Kellnerin wie zuvor angeflogen und überreicht mir mein Getränk."
"Ich suche Kleingeld aus meiner Tasche und lasse es in ihre wartende Hand fallen, bevor sie die anderen Gäste bedienen geht. Als sie davongeht, bleiben meine Augen auf ihr haften."


show hanako emb_sad_cas_close onlayer master
with charachange

ha "Findest du sie… hübsch…?"


"Hanako folgt meinem Blick und betrachtet die Kellnerin. Ich kann spüren, wie mir das Blut langsam im die Wangen wandert, als ich meinen Smoothie zurück auf den Tisch stelle."


hi "Nee, kann nicht wirklich behaupten, dass ich auf diesen Typ stehe. Sie sah nur sehr wie eine alte Freundin aus, die ich vor meiner Herzattacke kannte."


show hanako basic_worry_cas_close onlayer master
with charachange

ha "Hattest du… viele Freunde?"


hi "Ich hatte ein paar an meiner alten Schule, aber ich würde nicht sagen, dass es viele waren. Wir hingen nur zu viert nach der der Schule ab."


show hanako basic_normal_cas_close onlayer master
with charachange

ha "Hast du noch Kontakt zu ihnen?"


"Ich schüttle meinen Kopf."


hi "Nein. Wir haben nach und nach den Kontakt verloren, als ich im Krankenhaus feststeckte."


show hanako cover_worry_cas_close onlayer master
with charachange

ha "Bist du… deswegen nicht traurig? Oder wütend?"


"Hanako sieht wirklich überrascht aus. Ich schätze, das ist eine verständliche Reaktion."


hi "Na ja, das Leben ging für sie weiter, während ich auf der Station festsaß. Damals hat es mich ziemlich verletzt, aber jetzt ist es nur ein Haufen schöner Erinnerungen."


hi "Außerdem habe ich auch neue Freunde gefunden, als ich an die Yamaku kam."


"Das ist eine ziemliche Beschönigung meiner damaligen Gefühle."
"Während meines Aufenthalts im Krankenhaus bin ich durch ein paar dunkle Zeiten gegangen, und ich bin echt froh, dass Hanako und Lilly für mich da waren, nachdem ich es verlassen hatte."


show hanako basic_bashful_cas_close onlayer master
with charachange

"Hanako errötet, als wir beide unsere Getränke genießen. Sie hat sich anscheinend seit meiner Ankunft beruhigt, und da ich mich etwas ausruhen konnte, fühle ich mich ebenfalls etwas besser – es wird also langsam ein richtig schöner Ausflug."


"Aber auch wenn sie gelassener ist als vorhin, zappelt sie immer noch etwas herum. Ihre Hand fährt ihren Pony entlang, während ich darüber nachdenke, was ich sagen soll."


hi "Stimmt ja. Ich wollte dich was fragen…"


show hanako emb_timid_cas_close onlayer master
with charachange

"Hanako neigt fragend ihren Kopf."


hi "Ich wusste nicht, dass du ein Handy hast. Wie bist du an meine Nummer gekommen?"


show hanako emb_smile_cas_close onlayer master
with charachange

ha "L-Lilly… hat sie… mir gegeben."


"Hätte ich mir denken können."


hi "Weißt du, du hättest auch einfach fragen können; ich hätte sie dir gegeben."


hi "Wollen wir unsere E-Mail-Adressen austauschen?"


show hanako basic_bashful_cas_close onlayer master
with charachange

"Hanako nickt, stellt ihr Getränkt ab und kramt ihr Handy aus ihrer Hosentasche, während ich dasselbe tue."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

show hanaphone onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Es ist – zu meiner Überraschung – das gleiche Modell wie meins. Aber in pink."


hi "Hübsches Handy."


show hanako basic_smile_cas_close onlayer master
with None

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show hanaphone onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide hanaphone onlayer master
with None

"Sie sieht mich mit einem neugierigen Gesichtsausdruck an, bevor sie mein Handy bemerkt und kichert. Es ist einer dieser sehr selten Momente, in denen ich Hanako entspannt genug sehe, dass sie zu so etwas in der Lage ist."


show hanako cover_bashful_cas_close onlayer master
with charachange

ha "Ich habe es aber nicht selbst ausgesucht."


hi "Nicht?"


show hanako basic_bashful_cas_close onlayer master
with charachange

ha "Es war ein Geschenk. Von Lilly."


show hanako emb_emb_cas_close onlayer master
with charachange

ha "Ich habe nie wirklich ein Telefon gebraucht, und ich konnte mir auch keins leisten. Aber sie hat mir eins zu Weihnachten gekauft und gesagt, dass wir damit in Kontakt bleiben können."


"Sie sehen sich im Grunde genommen sowieso jeden Tag, inner- und außerhalb der Schule…"


"Andererseits hat Lilly ihre Klassensprecherpflichten und andere Freunde, mit denen sie redet. Zusätzlich würde es wahrscheinlich in so einer Situation wie jetzt helfen – wenn sie für eine Weile weg ist."


hi "Lilly bedeutet dir eine Menge, nicht wahr?"


show hanako emb_downsmile_cas_close onlayer master
with charachange

ha "Tut sie. Ich… liebe sie… wirklich sehr."


"Hanako sieht nach unten und lächelt, als sie an sie denkt. Keine meiner Freundschaften war so tief wie ihre, und ich muss mir selbst eingestehen, dass ich etwas neidisch darauf bin."


"Wir tauschen unsere E-Mail-Adressen aus und tippen sie in unsere Handys. Außerdem suche ich Hanakos Nummer von vorhin und speichere sie in meiner Kontaktliste."


show hanako basic_smile_cas_close onlayer master
with charachange

ha "… Fertig. Das macht nun drei."


hi "Drei?"


show hanako basic_bashful_cas_close onlayer master
with charachange

ha "Lilly, Akira und du."


hi "Ah, Akira. Sie ist ein interessanter Mensch, nicht wahr?"


show hanako emb_smile_cas_close onlayer master
with charachange

ha "Das ist sie. Aber sie ist auch wirklich nett. Ihr Anzug lässt sie ein bisschen… cool aussehen."


hi "Ich bin etwas überrascht, dass ihr einander so gut kennt, obwohl ihr Job so viel ihrer Zeit verschlingt."


show hanako emb_downsmile_cas_close onlayer master
with charachange

"Hanako senkt etwas ihren Blick und nimmt einen weiteren Schluck von ihrem Getränk."
"Würde ich nicht aufmerksam ihr Gesicht betrachten, würde mir das kleine Lächeln darauf entgehen. Wenn sie so wenig Leute kennt, müssen die, die sie kennt, ihr eine Menge bedeuten."


ha "Wie viele… hast du denn?"


hi "Ich? Um die neun oder zehn."


"Ich zögere, weiter darauf einzugehen – aus Angst, dass ich ihr die Tatsache unter die Nase reibe, dass sie keine Eltern oder sonstigen nahen Verwandten hat."
"Zudem sind zwei von ihnen Shizune und Misha, was noch eine weitere komplizierte Geschichte ist."


hi "Ich könnte mir vorstellen, dass Lilly wahrscheinlich mehr hat als wir beide zusammen."


show hanako basic_smile_cas_close onlayer master
with charachange

"Hanako gibt ein kindliches Kichern von sich, was mich unweigerlich zum Lächeln bringt. Es fühlt sich gut an, dass sie sich in meiner Gegenwart mittlerweile so wohlfühlt. In solchen Momenten habe ich das Gefühl, dass ich ihrem wahren Ich nahekomme."


hi "Dürfte ich dich etwas fragen, was mich schon ein Zeit lang interessiert?"


show hanako basic_normal_cas_close onlayer master
with charachange

"Hanako nickt, als sie ihren letzten Schluck Tee trinkt."


hi "Du bist anscheinend nicht sehr neidisch darauf, dass Lilly so viele Freunde hat. Willst du nicht selbst mehr Freunde finden? Oder welche von ihren kennenlernen?"


show hanako cover_worry_cas_close onlayer master
with charachange

ha "Ich bin nicht neidisch. Ich… mag keine Menschen, darum stört es mich nicht, nicht viele Freunde zu haben."


"Das ist… nicht wirklich die Antwort, die ich erwartet hatte. Als sie das sagt, sieht sie nicht ängstlich oder traurig aus, sondern sogar ziemlich ernst."


show hanako cover_distant_cas_close onlayer master
with charachange

ha "Ich…"


"Hanako reibt sich verlegen ihren Arm und interpretiert mein Schweigen als Aufforderung fortzufahren. Ich bin mir nicht wirklich sicher, was ich erwidern soll, daher schenke ich ihr lediglich schweigend meine Aufmerksamkeit."


ha "In der Mittelstufe… wurde ich gehänselt… sehr oft. Ich wurde beschimpft, und von Arbeitsgruppen oder Sportteams ausgeschlossen. Es gab auch… schlimmere Dinge."


hi "Und deswegen magst du keine anderen Menschen mehr?"


"Sie nickt."


show hanako emb_timid_cas_close onlayer master
with charachange

ha "In der… Grundschule war es noch schlimmer."


"Jetzt fühle ich mich mies, weil ich das angesprochen habe. Erwachsene haben schon genug Probleme, mit Hanakos Narben umzugehen; Kinder sind wohl viel schlimmer."


"Ich hatte angenommen, dass sie nur versucht hat, sich unsichtbar zu machen, weil sie den Blicken der Menschen ausweichen wollte, oder weil sie vor ihnen Angst hatte. Aber ganz sicher nicht, weil sie erst gar nicht mit ihnen interagieren wollte."


"Ich bemerke, wie das Kondenswasser meines vernachlässigten Smoothies eine kleine Pfütze um den Becherboden formt, also nutze ich die Gelegenheit, um ihn auszutrinken."


stop music fadeout 5.0

show hanako emb_downtimid_cas_close onlayer master
with charachange

"Während ich trinke, beginnt sie, an ihrem Handy herumzufummeln. Es sieht aus, als ob sie sich wieder an die Menschen um uns herum erinnert hat und deshalb nervös geworden ist."


"Es ist nicht gerade ein billiges Handy – ich musste eine ganze Weile sparen, bis ich mir meins leisten konnte. Wenn Lilly allerdings auf eine Privatschule gegangen ist, hat sie wahrscheinlich keine großen Probleme damit, eins zu verschenken."


"Sie daran herumfummeln zu sehen bringt mich auf eine Idee…"


hi "Hey Hanako, warte kurz hier. Ich bin sofort zurück."


$ renpy.music.set_volume(0.4, 4.0, channel="ambient")

"Ich stelle den nun leeren Becher ab, stecke mein Handy in meine Hosentasche und mache mich davon, wobei ich mich vorsichtig um die Tasche herumbewege, die ich neben meinen Füße abgestellt habe."
"Glücklicherweise geht es mir inzwischen viel besser als vorhin – das Sitzen und das Reden mit Hanako hat mir richtig gut getan."


show hanako defarms_worry_cas_close onlayer master
with charachange

ha "Warte, w-was? W-Wo gehst du hin?"


hi "Bleib einfach hier, ich bin sofort wieder da!"


$ renpy.music.set_volume(0.0, 1.0, channel="ambient")

show bg city_karaokeint onlayer master
show hanako invis_close onlayer master
with shorttimeskip

$ renpy.music.set_volume(0.2, 0.3, channel="ambient")

"So gerne ich auch zurückgejoggt wäre, weiß ich sehr gut, dass ich das nicht könnte. Schließlich laufe ich zurück zum Café, mit einer kleinen blauen Tasche in meiner rechten Hand."


show hanako defarms_worry_cas_close onlayer master
with charachange

play music music_another fadein 3.0

"Hanako bemerkt mich sofort und sieht ungefähr genauso verwirrt aus, wie ich sie zurückgelassen habe. Ich platziere die kleine Tasche vor ihr und setze mich wieder hin."


show hanako basic_worry_cas_close onlayer master
with charachange

ha "Ist das…?"


hi "Ist für dich. Du kannst es aufmachen."


show hanako cover_worry_cas_close onlayer master
with charachange

ha "A-Aber…"


hi "Nur zu."


"Sie sieht sehr unsicher aus, gibt aber schließlich nach, öffnet die Tasche langsam und holt ihren Inhalt heraus."


show phonestrap onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

$ renpy.music.set_volume(0.5, 1.0, channel="music")

"Eine silberne Kette – ein Handyanhänger – baumelt von ihren Fingern und endet in einer zierlichen Blume. Sie ist nicht wirklich ein Meisterwerk der Juwelierkunst, aber mehr konnte ich mir nicht leisten."


show hanako cover_bashful_cas_close onlayer master
with None

"Hanakos Augen leuchten auf, als sie sie sich ansieht. Es ist die Art von Reaktion, auf die ich gehofft hatte."


"Das Licht der Sommersonne schimmert auf dem Silber, als sich die Kette hin und her dreht. Sie ist nicht allzu prunkvoll, sieht aber immer noch sehr anmutig aus. Ich denke, sie passt gut zu ihr."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

show phonestrap onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide phonestrap onlayer master
with None

"Hanako legt den Handyanhänger auf den Tisch und sieht mich wieder an."


show hanako cover_worry_cas_close onlayer master
with charachange

ha "Aber… es ist nicht… Weihnachten… oder mein Geburtstag…"


hi "Schon okay, mach dir deswegen keinen Kopf. Ich dachte mir bloß, dass es vielleicht schön wäre, etwas zu haben, womit du dein Handy verzieren kannst."


show hanako basic_worry_cas_close onlayer master
with charachange

ha "A-Aber ich habe nichts, was ich dir geben könnte…"


hi "Wie gesagt, schon okay. Freunde können sich doch ab und zu etwas schenken, oder?"


show hanako emb_downsmile_cas_close onlayer master
with charachange

ha "Freunde…"


"Hanako senkt ihr Gesicht so sehr, dass ich ihren Ausdruck nicht sehen kann. Schließlich nickt sie, bevor sie ihr Handy nimmt und mit dem Anhänger hantiert, um ihn richtig zu befestigen."


show hanako emb_smile_cas_close onlayer master
with charachange

$ renpy.music.set_volume(0.5, 1.0, channel="music")

show hanaphonestrap onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Sie sieht mich an und lächelt, als sie ihr nun mit einer kleinen Blume verziertes Handy hochhält."


ha "Danke… Hisao."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

show hanaphonestrap onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide hanaphonestrap onlayer master
with None

"Ihr Lächeln erweist sich als ansteckend."


"Aus meinem Augenwinkel heraus bemerke ich, wie ein Pärchen aufsteht und geht. Das erinnert mich daran, dass der Bus zurück zur Schule bald kommen wird."


hi "Ich denke, ich sollte lieber los, falls ich noch den nächsten Bus zurück erwischen will. Kommst du auch mit?"


show hanako def_worry_cas_close onlayer master
with charachange

ha "Ah, j-ja."


show hanako invis_close onlayer master at center
with dissolvecharamove

"Hastig nickt sie, bevor sie ihr Handy wieder vorsichtig in ihre Hosentasche steckt und von ihrem Stuhl aufsteht. Ich stehe auch auf und nehme die Tasche mit, die ich vorhin zurückgelassen habe."


stop ambient fadeout 1.0
stop music fadeout 3.0

scene bg city_street2 onlayer master
show hanako emb_downsmile_cas_close onlayer master at center
with locationskip

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_traffic fadein 1.0

"Wir laufen Seite an Seite zur Busstation, ohne etwas zu sagen. Hanakos Blick ist starr nach vorne gerichtet, aber sie sieht sehr zufrieden mit sich aus."


"Ich bin mir nicht sicher, was ich zu ihr sagen könnte, aber bin mir auch nicht sicher, ob ich überhaupt etwas sagen muss."
"Die Tatsache, dass Hanako glücklich ist – und zwar glücklich meinetwegen – reicht aus, dass die Last an meinem Arm sich leicht wie eine Feder anfühlt."


stop ambient fadeout 2.0

scene black onlayer master
with dissolve




label de_H29:

scene bg school_scienceroom onlayer master
with locationchange

play music music_normal fadein 2.0

"Ich erreiche nach meinem gewohnten Fußweg von dem Wohnheimen endlich das Klassenzimmer und trete ein. Meine Augen wandern sofort zum dritten Platz von links in der hinteren Reihe. Hanakos Platz."


"Er ist leer, und es sieht aus, als sei sie noch nicht hier. Die zwei Mädchen vom Schülerzeitungsklub sitzen auf den zwei Plätzen zu Hanakos linken. Shizune und Misha sind ebenfalls da, aber das war es auch schon."


"Wir tauschen unsere morgendlichen Begrüßungen aus, bevor ich mich auf meinen Platz setzte. Ich muss zugeben, dass das eine kleine Erleichterung ist. Das gibt mir zumindest ein paar Minuten mehr, um nachzudenken."


"Nicht, dass ich das vorher nicht getan hätte; seit unserem Ausflug in die Stadt schwirrt mir Hanako die ganze Zeit durch den Kopf."


"Ich weiß immer noch nicht, was ich vom meinem Verhältnis zu Hanako halten soll. Ich mag sie, so viel kann ich mir eingestehen. Ich will sie beschützen und sie vor ihrem Schmerz bewahren."
"Dass meine Gefühle nur freundschaftlich sind, glaube ich mittlerweile nicht mehr."


"Aber andererseits… kommt es mir so vor, als würde ich sie gar nicht richtig kennen."


"Wie würde sie reagieren, wenn ich den ersten Schritt machen würde? Ist sie in einem emotionalen Zustand, der ihr erlaubt, eine vernünftige Entscheidung über eine Beziehung zu treffen? Wie würde sie alles bewältigen, was danach passieren könnte?"


$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_footsteps_hard fadein 4.0

"Es gibt auch die Möglichkeit, dass ich Hanako einfach vollkommen falsch verstehe. Bei jemanden, dessen soziale Fähigkeiten anscheinend so unterentwickelt sind, passiert das ganz leicht."


"Das Geräusch von Schritten nähert sich der Tür und lässt mich aufhorchen."


stop ambient fadeout 0.3

show miki invis onlayer master:
    right
    xpos 1.1
with None

show miki whistle onlayer master at right
with dissolvecharamove

"Es ist nur Miki."


show miki smile onlayer master
with charachange

show miki invis onlayer master at Position (xpos=0.9)
with dissolvecharamove

"Sie nimmt kaum meine Anwesenheit wahr, als ich aus Versehen Augenkontakt mit ihr herstelle. Ich will gerade wegsehen, aber kurz nachdem sie Platz genommen hat, kommt eine weitere Person herein."


show hanako invis onlayer master:
    right
    xpos 1.1
with None

show hanako emb_downtimid onlayer master at right
with dissolvecharamove

stop music fadeout 2.0

"Ich spüre, wie ich erstarre, als ich Hanako eintreten sehe. Das ist keine rationale Reaktion, aber ich habe keine Ahnung, wie ich ich mich verhalten oder was ich zu ihr sagen soll."


show hanako emb_timid onlayer master
with charachange

"Für einen Augenblick treffen sich unsere Blicke."


show hanako emb_downtimid onlayer master
with charachange

show hanako invis onlayer master at Position (xpos=0.9)
with dissolvecharamove

"Und dann sieht sie genauso schnell wieder weg und und begibt sich zu ihrem Platz, ohne ein einziges Wort zu sagen."


scene bg school_library_ss onlayer master
with shorttimeskip

play music music_tranquil fadein 3.0

"Wie üblich in der Zeit nach dem Unterricht, ist mein Gesicht tief in einem Buch vergraben, das ich völlig uninteressant finde."


"Lernen ist nichts, was mir zufliegt. Bevor ich an die Yamaku kam, habe ich nicht viel gelernt, und bis jetzt habe ich mich größtenteils mit Talent durchgeschlagen. Es ist frustrierend, dass ich das nicht mehr kann."


"Den Gesichtern der anderen Schüler in der Bibliothek nach zu urteilen, glaube ich nicht, dass ich mit dieser Abneigung allein dastehe. Elend sucht Elend, schätze ich."


"Ich habe beschlossen, die Mittagspause mit Hanako zu verbringen, da wir nun schon eine Weile nicht mehr zusammen zu Mittag gegessen haben."
"Ich hätte die Zeit aber auch genauso gut mit Lernen verbringen können – abgesehen von erbärmlich kleinen Smalltalk-Schnipseln haben wir kaum ein Wort gewechselt."


"Warum tut sie mir das immer an? Ich will sie nur beschützen, für sie da sein, aber jedes Mal, wenn ich das Gefühl bekomme, dass wir uns näherkommen, entfernen wir uns nur noch weiter voneinander."


ha "B-Bist du gerade beschäftigt…?"


$ renpy.music.set_volume(0.0, 0.3, channel="music")

show hanako defarms_shock_ss onlayer master at center
with vpunch

hi "Hanako?"


"Überrascht drehe ich meine Kopf ruckartig um, wodurch sie verängstigt zurückspringt."


show hanako emb_downsad_ss onlayer master
with charachange

"Das war ein schlechtes Timing. Hätte ich nicht genau in diesem Moment an sie gedacht, wäre ich wahrscheinlich nicht annähernd so aufgeschreckt."


$ renpy.music.set_volume(1.0, 5.0, channel="music")

hi "Entschuldige, du hast mich nur erschreckt."


"Ich bemerke, dass ich sie länger anstarre als ich sollte, also wende ich mich wieder dem Text zu, der auf dem Tisch vor mir liegt. Es kommt mir immer mehr so vor, als würde ich bloß Wörter anstarren, als wirklich zu lesen."


"Ich bekomme das Gefühl, dass Hanako das ebenfalls bemerkt, daher seufze ich und schließe das Buch."


hi "Was gibt's?"


show hanako emb_sad_ss onlayer master
with charachange

ha "Ich habe mich nur g-gefragt… was du gerade l-liest…"


"Nach meiner Reaktion auf ihren Anblick sieht sie etwas niedergeschlagen aus. Ich gebe das Vorhaben auf, noch etwas fertigzukriegen, stehe auf und stelle das Buch zurück an seinen Platz auf einem nahegelegenen Bücherregal."


hi "Es ist nur ein Englischbuch."


show hanako basic_normal_ss onlayer master
with charachange

ha "H-Hat es etwas gebracht?"


hi "Es hat mir geholfen zu begreifen, dass ich Englisch nicht mag, ja."


show hanako basic_smile_ss onlayer master
with charachange

"Hanako kichert leise."
"Ich mag mir über den seltsamen Zustand unserer Freundschaft den Kopf zerbrechen, aber ich weiß, dass ich solche kleinen Gesten nicht sehen würde, wenn wir uns seit unserer ersten Begegnung nicht wenigstens etwas nähergekommen wären."


"Ich sehe sie einen Moment lang an und frage mich, was ich über sie weiß und was nicht. Ein etwas deprimierendes Thema."


show hanako basic_worry_ss onlayer master
with charachange

ha "S-Stimmt etwas… nicht?"


stop music fadeout 5.0

"Wenn ich mehr über sie wissen will, sollte ich vielleicht aufhören, das Thema zu vermeiden."


"Ganz normal mit Lilly zu sprechen, anstatt andauernd Angst zu haben, dass sie wegen irgendetwas beleidigt wird, hat ganz gut geklappt, also sollte ich es bei Hanako auch einfach geradeheraus versuchen."


hi "Hey, Hanako, hättest du was dagegen, wenn ich dir eine Frage stelle?"


show hanako cover_worry_ss onlayer master
with charachange

ha "H-Habe ich nicht."


hi "Ich… will wissen, wie dein Leben war. Dein Leben vor der Yamaku."


show hanako emb_blushing_ss onlayer master
with charachange

"Sie zögert. Kurz ziehe ich in Erwägung, zurückzurudern, aber sie nimmt die Frage anscheinend ziemlich ernst."


"Ich setze mich und beobachte sie, während ich ihr schweigend die Zeit gebe, die sie braucht. Sie sieht mir nicht in die Augen und sieht fast so aus, als würde sie mit sich selbst kämpfen, ob sie sich mir weiter öffnet."


"Ihr Antwort folgt endlich in Form eines steifen, fast widerwilligen Nickens. Sie sieht angespannter aus als vor meiner Frage."


show hanako basic_worry_ss onlayer master
with charachange

ha "Okay. A-Aber dafür… musst du mir dann auch ü-über dein Leben erzählen…"


hide hanako onlayer master
with charaexit

"Ich nicke, und folge ihr, als sie zum Ausgang der Bibliothek läuft, damit wir draußen reden können."


scene bg school_hallway3 onlayer master
show hanako basic_normal onlayer master at center
with locationchange

play music music_serene fadein 0.5

"Mittlerweile haben die meisten Schüler das Hauptgebäude bereits verlassen, daher sind abgesehen von ein paar Leuten in den Klubräumen die Flure größtenteils leer."


hi "Ich schätze… wir fangen bei der Ankunft an der Yamaku an."


hi "Mal sehen… Ich war im Krankenhaus, als meine Eltern mir zum ersten Mal von der Yamaku-Akademie erzählten."


hi "Die Ärzte sagten mir, ich solle nicht mehr an meine alte Schule gehen. Meine Eltern willigten ein und überredeten mich dazu, mich an der Yamaku zu bewerben, auch wenn das bedeuten würde, dass ich zum ersten Mal weit weg von ihnen lebe."


show hanako cover_worry onlayer master
with charachange

ha "Das muss… hart für dich gewesen sein."


hi "Nun, ja, das war es wohl. Meine Eltern arbeiten beide ganztags und in Vollzeit, daher war mehr oder weniger unabhängig zu leben kein Neuland für mich."
hi "Es war die Tatsache, dass ich an eine Schule für körperbehinderte Schüler gehen würde, die mich am härtesten traf, glaube ich."


hi "Und du?"


scene bg school_staircase2 onlayer master
show hanako emb_downtimid_close onlayer master at right
with locationchange

"Eine kleine Gruppe sich unterhaltender Mädchen läuft an uns vorbei, als wir uns der Treppe nähern, und Hanako presst sich fest an meine Seite, bis wir das Erdgeschoss erreichen."
"Normalerweise kommt sie mir nicht so nahe, wenn wir einfach in der Schule umherlaufen, darum bin ich etwas verdutzt."


show hanako emb_downsad_close onlayer master
with charachange

ha "Das Personal im W-Waisenheus bot mir ein paar Optionen an. Die Mittelschule… war nicht gut, also dachte ich, dass Yamaku besser sein könnte."


ha "Ich war ausgegrenzt, und ich dachte, es wäre einfacher, hier zurechtzukommen, da die meisten anderen Behinderungen haben."


scene bg school_lobby_ss onlayer master
with locationchange

"Es ist ziemlich ironisch, dass der Grund, aus dem Hanako sich auf die Yamaku gefreut hat, genau der ist, weswegen ich den Gedanken gehasst habe."
"Mir kam es vor, als würde ich irgendwohin abgeschoben werden – fern von der Gesellschaft und von allen, die ich kannte. Für Hanako war das wahrscheinlich eine einladende Aussicht."


hi "Wie war das Leben im Waisenhaus?"


show hanako emb_timid_ss onlayer master at center
with charaenter

ha "Es war… okay. Das Personal dort war nett, und sie haben sich um uns gekümmert. Die Kinder haben nicht viel mit mir geredet, aber ich wollte auch nicht wirklich mit ihnen reden. Darum hat es mich nicht gestört."


show hanako emb_downsmile_ss onlayer master
with charachange

ha "Das Waisenhaus hatte eine kleine Bibliothek, also fing ich an zu lesen und dort die Zeit zu verbringen. Das Personal hatte nichts dagegen, weil sie dadurch leichter mit mir zurechtkamen als mit den vielen anderen Kindern."


hi "Hast du dort keine Freunde gefunden?"


show hanako basic_worry_ss onlayer master
with charachange

ha "Nein. Ich glaube… zu jener Zeit… stand mein Leben still. Ich wusste das, aber es war mir egal."


"Zu glauben, dass ihr Leben für all diese Zeit stillstand… Je nachdem, wann das mit dem Feuer passiert ist, war das ein riesiger Teil ihres Lebens. Keine Eltern, keine Freunde, anscheinend keine Verwandten…"


scene bg school_courtyard_ss onlayer master
with locationchange

"Wir laufen durch die Tür auf den Hof. Ich rechne damit, meine Augen von der Sonne abwenden zu müssen, aber sie ist schon fast untergegangen."


show hanako emb_timid_ss onlayer master at center
with charaenter

"Hanakos Augen huschen immer wieder zu mir, darum sehe ich eine Weile weg."


ha "Wie war es im Krankenhaus?"


"Schnell kläre ich meinen Kopf und versuche, mich zu konzentrieren."


"Ich zögere ein bisschen, aber ich weiß, dass ich es ihr erzählen muss. Für sie stehen wir uns nahe genug, dass sie mir das alles ohne Sorgen erzählen kann, daher ist es nur fair, dass ich das erwidere."


hi "Manchmal war es okay, aber manchmal war es auch ziemlich schlimm. Zu Anfang haben mir alle ihr Mitleid ausgedrückt und kamen oft zu Besuch. Es war ungefähr so wie bei einem gebrochenem Arm."


hi "Alle meine Freunde zu treffen, gehörte zu den guten Zeiten. Iwanako kam auch oft vorbei; öfter als jeder andere."


hi "Aber wie gesagt gab es auch schlimmere Zeiten. Als meine Freunde langsam aufhörten, mich zu besuchen, fing ich an zu begreifen, wie ernst meine Situation war."
hi "Es erinnerte mich daran, dass dies nicht nur ein gebrochener Knochen war, sondern dass ich nun ein anderer Mensch war als zuvor."


hi "Sogar die Zeiten, in denen Iwanako bei mir war, wurden zu einer Folter. Am Anfang hat sie noch andauernd geredet, aber am Ende haben wir uns nur noch angeschwiegen."


"Aber so war Iwanako immer schon. Sie mag ein zerbrechlicher Mensch gewesen sein, aber sie hat versucht, diese Tatsache zu verstecken, indem sie andauernd redete – nicht über irgendwas Bestimmtes; sie hat einfach nur geredet."


hi "Ich denke, die drei Tiefpunkte waren der Moment, als meine Eltern mir sagten, dass ich nicht mehr an meine alte Schule gehen würde, als ich meinen Geburtstag im Krankenhaus verbrachte, und… als Iwanako mich zum letzten Mal verließ."


scene bg school_gardens_ss onlayer master
with locationchange

"Wir lassen das Schulgebäude hinter uns und folgen dem Hauptpfad durch die Gärten. Im Schulgebäude mag es den einen oder anderen Schaulustigen gegeben haben, aber draußen sind wir praktisch allein."


show hanako basic_worry_ss onlayer master at center
with charaenter

ha "Wie war deine Mittelschule?"


hi "Ich mochte sie. Ich wuchs in einer echten Großstadt auf, und die Mittelschule war in der Nähe, daher war sie ziemlich überfüllt. Es störte mich nicht, wahrscheinlich weil ich es gewohnt bin, unter Menschen zu sein."


hi "Ich bekam gute Noten, und ich spielte Fußball mit meinen Freunden. Nach der Schule hab ich auch eine Menge Zeit mit ihnen verbracht. Allerdings haben sie mich wegen meiner Haare aufgezogen."


show hanako def_worry_ss onlayer master
with charachange

ha "Deine Haare?"


"Ich verziehe etwas mein Gesicht, und lege eine Hand darauf, um sie zu bedecken."


hi "Ich bekam immer wieder Büschel und Strähnen, die einfach nicht dort bleiben wollten, wo ich sie haben wollte, und meine Mutter hat nicht zugelassen, dass ich es mir kurz schneiden lasse."
hi "Es hatte die Angewohnheit, immer aus der Reihe zu tanzen, egal wie sehr ich versuchte, es zu bändigen."


show hanako basic_smile_ss onlayer master
with charachange

ha "Das tut es immer noch, ein bisschen."


hi "Genau diese Antwort wollte ich nicht hören."


show hanako cover_worry_ss onlayer master
with charachange

ha "T-Tut mir leid, ich wollte nicht…!"


"Ich gebe ein gedämpftes Lachen von mir und winke ab."


hi "Schon okay, das weiß ich doch."


"Es kommt mir komisch vor, dass sich jemand so für meine Vergangenheit interessiert. Wenn es jemand anderes wäre, würde ich denken, dass es nur Höflichkeit ist, aber ich glaube wirklich nicht, dass Hanako so etwas tun würde."
"Und wenn sie sie täte, würde sie es so schlecht machen, dass es offensichtlich wäre."


scene bg school_dormhallground onlayer master
show hanako emb_downtimid_close onlayer master at right
with locationskip

"Es sind einige Mädchen im Aufenthaltsraum im Erdgeschoss, und Hanako presst sich ein weiteres Mal an meine Seite, als wir an ihnen vorbeilaufen."
"Ich rechne damit, dass sie sich wieder löst, doch stattdessen klammert sie sich weiter an mich, während wir zur Treppe laufen."


stop music fadeout 5.0

"Etwas an der Art, wie sie sich an mir festhält, fühlt sich… anders an als sonst."


scene bg school_girlsdormhall onlayer master
with locationchange

"Ich versinke tief in Gedanken, als wir die Treppen hinaufsteigen und den Flur entlanglaufen. Erst als wir anhalten und ich aufsehe, bemerke ich, dass ich ihr gefolgt bin, ohne darüber nachzudenken."


hi "Warum sind wir zu deinem Zimmer gegangen?"


show hanako basic_distant_close onlayer master at center
with charaenter

"Sie schaut direkt auf die Tür, ohne auch nur einen Blick in meine Richtung zu werfen."


hi "Hanako?"


show hanako basic_normal_close onlayer master
with charachange

"Sie will gerade antworten, verkneift es sich dann aber."


hide hanako onlayer master
with charaexit

play sound sfx_dooropen

"Stattdessen löst sie sich still von meiner Seite, öffnet ihre Tür und tritt ein."


"Ich sehe den Flur etwas verloren auf und ab und weiß nicht genau, was ich tun sollte. Schulterzuckend beschließe ich, ihr zu folgen, da ich keinen Grund habe, es nicht zu tun."


scene bg school_dormhanako_ss onlayer master
show hanako basic_normal_ss onlayer master at center
with locationchange

"Hanako steht in der Mitte ihres Zimmers und sieht mich direkt an. Es ist nervenaufreibend, weil es so unüblich für sie ist. Ich öffne meinen Mund, um etwas zu sagen, doch sie kommt mir zuvor."


ha "Könntest du… die Tür zumachen und abschließen?"


"Hanakos Hand wandert zu ihrer Brust und greift die Bluse an ihrem Herz."


hide hanako onlayer master
with charaexit

play sound sfx_doorclose
with Pause (0.8)

play sound sfx_lock

"Ich drehe mich um und schließe die Tür ab. Dann erstarre ich."


"Die Atmosphäre beginnt sich ziemlich seltsam anzufühlen. Dieses Gefühl wird nur intensiver, als ich höre, wie die Vorhänge hinter mir zugezogen werden."


"Es wird bald Nacht sein. Wir sind ein Junge und ein Mädchen, in einem Schlafzimmer. Sie schließt die Vorhänge, und ich schließe die Tür ab. Sie kann… sie kann doch nicht wirklich {b}das{/b} im Sinn haben… oder?"


"Ich schlucke und drehe mich sehr, sehr langsam um. Hanako steht in der Mitte des Zimmers, hat sich mir aber nicht wieder zugewandt."


show hanako emb_downtimid_ss onlayer master at center
with charaenter

ha "Du hast mir von deiner Vergangenheit erzählt, also muss ich dir von meiner erzählen."


"Sie nimmt einen tiefen, zitternden Atemzug und hält für einige Sekunden inne. Ihre Hände bewegen sich zu ihrer Schleife und beginnen an ihr zu zupfen, wodurch meine Gedanken bestätigt werden."


hi "H-Hanako…"


show hanako emb_timid_ss onlayer master
with charachange

ha "B-Bitte… sag nichts."


"Gehorsam schweige ich, als sie ihre Schleife löst, als nächstes ihre Bluse aufknöpft und sich danach an den Verschluss ihres BHs macht. Der Vorgang ist langsam. Vielleicht fühlt es sich auch einfach nur langsam an. Ich weiß es nicht."


"An Ort und Stelle festgefroren kann ich nichts tun, außer zuzusehen, wie Hanako mit zitternden Händen ihren Rock öffnet und ihn auf den Boden fallen lässt."


play music music_hanako fadein 1.0

scene ev hanako_scars onlayer master:
with whiteout

"Endlich nimmt sie ihre Bluse in ihre Hände und zieht sie aus, wobei ihr BH von ihren Schultern fällt. Und so steht Hanako fast vollkommen nackt in der Mitte des Raum, abgesehen von ihrer Strumpfhose und Unterwäsche."


ha "Das bin ich. Das ist… alles von mir."


show ev hanako_scars_large onlayer master:
    xalign 0.0 yalign 1.0 subpixel True
    acdc_warp 30.0 xalign 1.0 yalign 0.0
with locationchange

"Meine Augen richten sich augenblicklich auf die Narben auf ihrem Rücken."
"Die Haut auf ihrer rechten Seite hat die gleiche Textur wie die Haut im ihrem Gesicht, aber sie ist auch gespannt und bedeckt einen viel größeren Bereich. Die Narben auf der Schulter, Pobacke und Hüfte sind bei Weitem am schlimmsten."


"Genau wie mein Herzanfall mein Leben verändert hat… ist dies das Ereignis, das Hanakos verändert hat."


"Hätte ich das bei unserer ersten Begegnung gesehen, wäre ich schockiert gewesen. Nicht nur wegen des Anblicks, sondern auch von dem Gedanken, dass man etwas wie das überleben kann."


"Aber nachdem ich Zeit hatte, mich an diese Vorstellung zu gewöhnen, und nachdem ich die Narben auf ihrem Gesicht, ihren Händen und ihrem Hals sah, ist meine Reaktion gemäßigter."
"Im Moment reagiere ich weniger auf ihre Narben, sondern auf ihren Körper."


ha "Das Feuer geschah, als ich acht Jahre alt war. Es war Nacht, und wir schliefen, als es anfing."


"Hanakos Stimme zittert. Das Beben ihrer Bluse verrät, dass ihre Hände es auch tun."


ha "Ich… rollte mich zusammen… als das Feuer über mich hinwegfegte. Meine Mutter… versuchte, mich abzuschirmen. Das ist der… einzige Grund, warum… ich überlebte…"


"Hanakos Augen fangen an, feucht zu werden, und ihre Stimme wird brüchig. Die Kombination aus dem Druck, sich mir so zu zeigen, und diese schmerzhaften Erinnerungen von vor so langer Zeit noch einmal zu durchleben, muss heftig sein."


"Ich will etwas sagen, irgendetwas, damit sie sich besser fühlt, aber ich kann es nicht."
"Ich komme mir in dieser Situation vollkommen nutzlos vor. Sie zwingt sich dazu, mir näherzukommen, und dennoch fühle ich in solchen Momenten unsere Distanz noch stärker."


ha "Es tut mir leid… dass du das sehen musstest."


"Es bringt nichts, das Offensichtliche zu leugnen. Ich denke, was ich jetzt sagen sollte und was Hanako jetzt von mir hören will, ist die Wahrheit. Was ich aufrichtig und ehrlich fühle."


hi "Das spielt keine Rolle. Du bist ein wundervoller Mensch, Hanako. Dein Körper ändert nichts daran."


"Sie sieht mich für eine lange Zeit an. Ihre Atmung ist ungleichmäßig, als sie versucht, trotz der Emotionen, die wird beide empfinden, standhaft zu bleiben."
"Es kommt mir weniger so vor, als würde sie mich ansehen, sondern eher, als würde sie durch mich hindurchsehen."


"Langsam gehe ich auf sie zu und lege meine Hände sanft auf ihre Schultern, während sie ihre Bluse fallen lässt. Sie schnappt kurz nach Luft; nicht aus Angst, sondern einfach überrascht."


"Ihr so nahe zu sein, macht aus meinem Verstand ein Karussell aus Gefühlen."
"Die Narben auf ihrer Schulter, klar zu sehen und bei Berührung lederartig, stehen im seltsamen Kontrast zu ihrer ansonsten weichen Haut und ihrem geschmeidigen, dunklen Haar."


"Hanako ist ein Mädchen, mit allem, was dazugehört. Sie ist größer als die meisten Frauen, hat aber trotzdem Kurven an genau den richtigen Stellen. Ihr Nacken, gerade noch sichtbar durch ihr über die Schulter hängendes Haar, ist verführerisch."


ha "Ich weiß… dass ich nicht so hübsch… wie Lilly bin. Ich wollte nur… dass du mich siehst. Mein wahres Ich."


hi "Aber ich habe dein wahres Ich doch schon gesehen. Dafür musstest du dich nicht ausziehen."


scene bg school_dormhanako_ss onlayer master
show hanagown stockworry_blush_close_ss onlayer master at center
with locationchange

"Ihre Lippen sind geöffnet – nur ein bisschen. Sie atmet kurz und stoßartig aus, als ich mich – ohne nachzudenken – mit angehaltenem Atem nach vorne lehne und meine Lippen auf ihre presse."


"Der Kuss dauert nur einen flüchtigen Moment, bevor sich unsere Gesichter trennen und wir dabei schnell und nervös atmen. Das Gefühl von Hanakos Mund verbleibt, und ihre Augen haften auf meinen."


show hanagown stockdistant_blush_ss onlayer master at center
with charachange

"Während ich selbst etwas zittere, löse ich meine Krawatte und beginne, die Knöpfe an meinem Hemd zu öffnen. Hanako steht regungslos da und sieht auf den Boden vor sich, anstatt mir beim Ausziehen zuzusehen."


"Auf der einen Seite bin ich dankbar dafür. Ich bin was meinen Körper betrifft schon immer irgendwie gehemmt gewesen, aber meine Narbe hat das noch ziemlich verschlimmert. Andererseits fühlt sich diese Atmosphäre sehr seltsam an."


show hanagown stocknormal_blush_ss onlayer master at center
with charachange

"Mein Hemd fällt genauso unordentlich und zerknittert auf den Boden wie Hanakos Bluse und Rock. Bei dem Geräusch meines sich öffnenden Reißverschlusses zuckt Hanakos gesamter Körper zusammen."


"Meine Hosen gesellen sich zum meinem Hemd auf dem Boden neben dem Bett, kurzer darauf auch meine Socken. Ich zögere, bevor ich meine Boxershorts ausziehe, und lasse sie letztendlich an."


"Sie repräsentieren die letzte Hürde, von der ich glaube, dass ich sie noch nicht wirklich überwinden kann. Schiere Verlegenheit stoppt mich, zusätzlich zu dem Wunsch, Hanako nicht noch weiter aufzuwühlen."
"Mein Unwohlsein über diese Situation hat auch dafür gesorgt, dass ich nun selbst Anregung brauche."


show hanagown stockdistant_blush_ss onlayer master at center
with charachange

hi "Hanako…"


hide hanagown onlayer master
with charaexit

"Sie nickt, ohne mich anzusehen, und begibt sich mit mir zum Bett. Sie läuft, als wären ihre Beine steif. Ich würde es witzig finden, wenn es mir nicht genauso gehen würde."


"Ich ergreife die Initiative, drehe mich um und setze mich auf die Bettkante."
"Ich sehe ihr ins Gesicht, um sie einzuladen, sich entweder neben oder vor mich zu setzen, schaue aber letztendlich unbeholfen nach unten, um mich davon abzuhalten, ihren Körper anzustarren."


label de_H29h:

scene evh hanako_bed_boobs_glance onlayer master
with whiteout

"Nichtsdestotrotz deutet sie es richtig und setzt sich zögernd zwischen meine Beine. Als sie das tut, überkommt mich ein Ansturm aus Empfindungen."


"Das Gefühl ihres Hinterns an meinem Schritt ist das offensichtlichste, aber ihr Duft ist genauso stark. Durch ihre Nervosität hat sich bereits etwas Schweiß gebildet, und der Geruch und das Gefühl ihres Haars weht mir ins Gesicht."


"Ich versuche, ein Lächeln aufzusetzen, um ihr die Situation etwas angenehmer zu machen, aber es fühlt sich wirklich gekünstelt an. Ich beschließe, die Dinge etwas ins Rollen zu bringen, und lege eine Hand auf ihre Brust und die andere auf ihr Bein."


show evh hanako_bed_boobs_blush onlayer master
with charachange

"Ihre Lippen pressen sich zusammen, als sie – ohne Erfolg – versucht, ein überraschtes Quieken zu unterdrücken."


hi "Entschuldige, ich wollte dich nicht erschrecken."


"Hanako atmet tief durch und schüttelt als einzige Antwort ihren Kopf."


"Ich schlucke heftig, bevor ich damit beginne, meine Hand umherzubewegen und ihre Brust und ihren Nippel zu spüren und zu massieren. Es fühlt sich wirklich gut an, wie fest sie unter meiner Handfläche sind und doch nachgeben."


"Für eine Weile glaube ich nicht, dass es ihr überhaupt hilft, in Stimmung zu kommen, doch allmählich senken sich ihre Augenlider. Ihre Atmung verlangsamt sich und wird gleichmäßiger, und ihr Körper lässt sich langsam in meinen sinken."


"Es ist eine neue Art der Zufriedenheit, Hanako so ein Gefühl geben zu können; auf jeden Fall besser als das Gefühl ihres Körpers allein. Ich kann auch einen kleinen harten Hügel gegen meine Finger streifen spüren, der vorher noch nicht da war."


show evh hanako_bed_crotch_blush onlayer master
with charachange

"Langsam fahre ich mit meiner Hand abwärts und versuche dabei, sie nicht allzu sehr zu überraschen. Sie protestiert nicht, und bald beginnen meine Finger, sich entlang der weichen Spalte zwischen ihren Beinen auf- und abzubewegen."


"Mittlerweile presst sich ihr Körper gegen meinen, mit einer dünnen Schicht aus Schweiß zwischen uns beiden. Sie fühlt sich warm an, und all das hat mehr als ausgereicht, um mich – und auch sie – zu erregen."


"Hanako keucht leise, als sich meine Finger fast instinktiv etwas fester und etwas schneller bewegen. Das Mädchen vor mir, das Mädchen, dass sich gegen mich presst… Ich will sie. Ich will sie ganz."


show evh hanako_bed_crotch_glance onlayer master
with charachange

"Ich höre auf, meine Finger zu bewegen, und Hanako atmet tief aus, als die Gefühle nachlassen, die in ihr aufquellen. Sie wendet ihr Gesicht etwas zu mir und sieht mich an. Schweigend, aber erwartungsvoll."


"Alles, was ich tue, ist zu nicken. Ich weiß nicht, wer von uns gerade ängstlicher ist."


scene bg school_dormhanako_ss onlayer master
with locationchange

"Ich zwinge mich rückwärts aufs Bett und befreie mich sehr widerwillig von Hanako. Was sie betrifft, rutscht sie nach hinten und legt sich mit ihrem Kopf auf das Kissen, während sie dabei die ganze Zeit heftig atmet."


scene evh hanako_missionary_underwear onlayer master
with whiteout

"Hanako liegt vor mir, ihr Höschen dunkel gefärbt. Ihre Brust hebt und senkt sich, ihr Gesicht ist errötet, ihre Augen sehen in meine… ihre Narben lassen sie nur noch einzigartiger aussehen. Ich bin sprachlos, dass sie mir erlaubt, sie so zu sehen."


"Ich nähere mich ihr und lege meine Hände um ihre Taille. Ich warte darauf, dass sie nickt, bevor ich vorsichtig ihre Strumpfhose greife und sie so sanft wie ich kann etwas herunterziehe."


"Ich glaube nicht, dass ich sie ganz ausziehen kann, ohne sie zu zerreißen, also lasse ich sie einfach an ihren Beinen und bewege ihr Höschen beiseite."


"Hanako liegt praktisch nackt auf dem Bett; ihre empfindlichsten Stellen und die Narben ihres Körpers sind nun deutlich zu sehen."


"Ich lege meine Finger auf ihren Schritt und streichle sie noch etwas mehr, wodurch ihr Atem ins Stocken kommt. Es sollte okay für sie sein, wenn sie so erregt ist, also öffne ich meine Boxershorts und bewege mich im Bett etwas nach oben."


"Hanakos ganzer Körper spannt sich an, als ich mich ihr nähere, und ihre Augen weiten sich. Sie hat… Angst?"


"Ich atme tief ein, bevor mir etwas einfällt, woran ich vorher hätte denken sollen. Ich schließe meine Augen und konzentriere mich fest."


"Mein Herz klopft vor sich hin, als ich meinen Geist auf seinen Rhythmus konzentriere. Es ist schneller als sonst – natürlich – aber gleichmäßig. Ich… glaube… ich kann es unter Kontrolle halten, wenn ich es langsam angehe."


ha "Bist du… okay…?"


"Ich öffne meine Augen und sehe sie an. Das muss für jemanden, der mir dabei zugesehen hat, wohl ziemlich besorgniserregend ausgesehen haben."


hi "Ich bin okay. Ich wollte nur sichergehen, dass ich es bin."


"Sie zögert etwas, bevor sie nickt. Sie sieht etwas weniger ängstlich aus als zuvor. Ihr zu zeigen, dass ich selbst besorgt war, hat sie also etwas beruhigt."


"Ich lehne mich zu ihr und presse meine Lippen auf ihre, wobei sich unsere Zungen zaghaft berühren. Ich kann spüren, wie ihr Körper unter meinem immer weniger angespannt ist. Es bringt uns beide also wieder in die richtige Stimmung."


"Dann erinnere ich mich an etwas und löse mich."


"Ich lehne mich aus dem Bett heraus zu meiner Hose, und greife in die Gesäßtasche. Ein paar Sekunden krame ich darin herum, bis meine Finger eine kleine, quadratische Plastikfolie finden."


"Rasch hole ich sie heraus, richte mich etwas entfernt von Hanako auf dem Bett auf und fummle mit dem Päckchen herum."
"Es dauert eine Weile, bis alles richtig sitzt, aber schließlich bedeckt der Gummischlauch alles, was er bedecken soll, und passt genau."


"Meine leichte Verwirrung bei meinem ersten Versuch, mit einem Kondom umzugehen, scheint sie etwas belustigt zu haben, und als ich mich über ihr positioniere, teilen wir ein kleines nervöses Lachen. Jetzt allerdings muss ich mich konzentrieren."


"Ich sehe nach unten und versuche, meine Knie und Taille dorthin zu bringen, wo sie glaube, dass sie hingehören, und nehme meinen Penis in meine leicht zitternde Hand."
"Hanako Gesicht sieht in meins, doch ihre Augen sind dorthin gerichtet, wo sich unsere Geschlechtsteile begegnen."


"Mit einem kurzen Atemzug positioniere ich die Eichel und schiebe meine Hüften nach vorne."


scene evh hanako_missionary_closed onlayer master
with charachange

ha "Aahn…!"

"Mit einem Stoß schiebe ich mich selbst ganz in sie hinein. Der Ansturm aus Empfindungen und Emotionen erfüllt meinen Kopf, und Hanako jault vor Schmerz auf."


"Bei einem Blick in ihr Gesicht wird mir unwohl. Aus Unwissen habe ich zu hart und zu schnell gestoßen, und ihr mehr Schmerz als nötig bereitet. Keiner von uns weiß wirklich, was wir gerade tun, und das letzte, was ich wollte, war, ihr wehzutun."


scene evh hanako_missionary_open onlayer master
with charachange

"Hanako öffnet ihre Augen wieder und sieht mich an. Sie muss gesehen haben, wie beunruhigt ich aussehe, da sie ihr Bestes versucht, eine glückliche Miene aufzusetzen. Wirklich überzeugend ist sie nicht."


"Ich sehe hinab und gebe ihr ein paar Augenblicke, um sich zu erholen, dann fange ich an, meine Hüften langsam zu bewegen."


"Die Bewegung fühlt sich wirklich unnatürlich an, und ich kann spüren, wie sich in meinem ganzen Unterkörper Muskeln bewegen, bei denen ich noch nie so eine Bewegung gespürt habe."


"Genauso weiß ich, dass ich mein Herz einer Belastung aussetze, die ich wahrscheinlich vermeiden sollte, und mit jeder Bewegung achte ich auf meinen Herzschlag."


"Das Gefühl im Inneren von Hanako ist weich und warm, und wenn das Kondom die Empfindung nicht etwas abstumpfen würde, bezweifle ich, dass ich lange durchhalten würde."
"Ihr leises Keuchen und ihre konstanten Bewegungen machen es auch nicht besser."


scene evh hanako_missionary_clench onlayer master
with charachange

"Was Hanako betrifft verfliegt der schmerzerfüllte Blick anscheinend nicht wirklich, wie ich es erhofft hatte."
"Ihr Narbengewebe bewirkt, dass sich eine Seite ihres Körpers etwas anders bewegt als die andere, und Strähnen ihres Haares kleben mittlerweile an ihrem Gesicht."


"Ich lege meine Arme um ihren Körper und hebe ihn etwas an. Nach etwas Hin- und Herrutschen versuchen wir, eine etwas andere Position zu finden, um ihre Schmerzen zu minimieren."


"Während meine Hände ihre Beine festhalten, bewegen wir beide uns inzwischen immer ungezügelter. Hanakos Geruch erfüllt meine Sinne, und in dieser Position strapaziere ich meinen Körper nicht ganz so sehr."


"Meine Zeitgefühl scheint verzerrt zu sein, und ich fühle mich allmählich, als würde ich vom Hyperventilieren ohnmächtig werden. Aber ich will, dass sich Hanako gut fühlt, und ich kann an diesem Punkt auch nicht mehr aufhören."


"Eine neue Welle aus Lust beginnt, mich plötzlich zu überschwemmen. Meine Gefühle werden stärker, und ich glaube nicht, dass ich sie noch länger kontrollieren kann. Ich werde schneller und konzentriere mich immer weniger auf meinen Rhythmus."


"Jedes Mal, wenn es sich so anfühlt, als hätten wir einen Rhythmus gefunden, verlieren wir ihn in unseren Bewegungen."
"Von ihren Geräuschen her glaube nicht, dass diese Position Hanako geholfen hat, sich viel besser zu fühlen, und ich glaube auch nicht, dass ich sie noch viel länger festhalten kann."


"Ich lege sie wieder zurück aufs Bett. Wir beide sind weit über den Punkt hinaus, an dem wir noch etwas anderes tun können, als das Ende zu erreichen."


"Einen Stoß nach dem anderen beginne ich zu spüren, wie sich dieser Zeitpunkt nähert. Krampfhaft spanne ich mich an, um zu versuchen, ihn so lange ich kann hinauszuzögern."


hi "Hanako…!"

scene evh hanako_missionary_closed onlayer master
with charachange

"Hanako gibt einen leisen Schrei von sich, während mein Verstand verblasst. Meine Taille trifft ihre mit einer ziemlichen Kraft, als ich meinen Höhepunkt erreiche, und ich kann spüren, wie ich in ihrem Inneren zucke."
"Ihr Körper dreht und windet sich unter meinem, wodurch das Gefühl der Euphorie nur noch größer wird."


window hide

label de_H29x:

scene bg school_dormhanako_ni onlayer master
show white onlayer master
with Dissolve(3.0)

window show

"Und dann, nach ein paar Sekunden… ist es vorbei."


"Das Geräusch von Hanakos Atmung und meiner eigenen klingt fast schmerzhaft laut in meinen Ohren. Hanako hält einen Arm über ihr Gesicht, und ihr Mund ist offen und schnappt nach Luft."


stop music fadeout 10.0

show white onlayer master:
    linear 10.0 alpha 0.0

"Als ich mich über sie stütze, gibt mein Arm fast nach, als hätte ihn jemand gepackt und zur Seite gezogen, und meine Sicht verzerrt sich."
"Ich lasse mich seitlich neben die keuchende Hanako auf das Bett fallen, damit ich nicht aus Versehen auf ihr lande."


"Wir beide liegen nebeneinander, nackt und aneinandergepresst, um in das Bett zu passen, das nur für eine Person gemacht ist."
"Meine Augen versuchen ohne viel Erfolg, sich auf die Zimmerdecke zu konzentrieren. Eine Bettdecke über uns zu ziehen, um die Kälte abzuhalten, ist alles, was ich tun kann."


"Das einzige Geräusch im Zimmer ist das unserer Atmung. Der Schweiß, der sich auf meinen Körper gesammelt hat, fühlt sich unangenehm an. Wir sind beide körperlich und emotional ausgelaugt, und vollends zerzaust."


window hide

play sound sfx_heartslow
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.8)

window show

"Meine Sicht normalisiert sich langsam wieder, während ich weiter an die Decke starre, aber meine Gliedmaßen fühlen sich immer noch wie Pudding an."
"Ich versuche, mich auf meine Brust zu konzentrieren, und bemerke, dass mein Herzschlag unregelmäßig und ein bisschen schmerzhaft ist."


window hide

play sound sfx_heartslow
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.8)

window show

"Dies ist ein gefährlicher Moment. Ich muss das durchdenken und nicht in Panik geraten, damit ich meine Lage nicht noch schlimmer mache."


window hide

play sound sfx_heartslow
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.8)

window show

"Mit extremer Mühe erlange ich die Kontrolle über meine unregelmäßige Atmung zurück und zwinge mich, lange, tiefe Atemzüge zu machen."
"Es sind ein halbes Dutzend, bis ich wieder anfange, mich körperlich ruhig zu fühlen, und presse meine Hand an meine Brust, um mich dessen zu versichern."


"Mein Herzschlag ist wieder normal. Ich bin okay."


scene ev hanako_after_worry onlayer master
with locationchange

play music music_twinkle fadein 1.0

"Ich wende mein Gesicht zu Hanako, die mich bereits ansieht. Sie sieht ziemlich benommen aus, ist aber offensichtlich auch besorgt um mich. Sie hat bemerkt, was passiert ist."


hi "Mir geht's… gut. Alles… ist wieder normal."


"Ich merke, wie ich zwischen den Atemzügen kaum die Worte hervorbringe kann."
"Ich denke nicht, dass Sex einen normalen Körper so auslaugen würde, also habe ich keine Zweifel, dass meine Krankheit zumindest teilweise daran Schuld ist. Warum musste mein Körper das ausgerechnet jetzt tun?"


scene ev hanako_after_smile onlayer master
with charachange

"Jedoch lösen sich meine Gedanken über mein Herz in Luft auf, als ich das breite Lächeln sehe, das sich auf Hanakos Gesicht formt."


"Wie immer lächle ich ohne einen weiteren Gedanken zurück. Hanakos Lächeln ist in seiner fast kindlichen Niedlichkeit und Ehrlichkeit schon immer ansteckend gewesen. Es ist etwas, das sie von allen anderen abhebt."


"In diesem Moment… brauchen wir keine Worte. Alles, was wir einander sagen wollen, können wir uns genauso gut ohne sie mitteilen."


stop music fadeout 2.0

scene black onlayer master
with shuteye



label de_H30:

scene black onlayer master
with dissolve


hi "Mmh…"

play music music_pearly

scene bg school_dormhanako onlayer master at left
with openeye

"Meine Augen fühlen sich schwer an, als ich sie langsam öffne. Das Licht von draußen lässt mich etwas blinzeln, damit sie sich daran gewöhnen. Mein Körper fühlt sich wie aus Blei an, und mein Kopf ebenfalls."


"Unter einer unbekannten Zimmerdecke aufzuwachen, ist ein unangenehmes Gefühl. Es erinnert mich an das erste Mal, als ich unter der weiß gesprenkelten Fliesendecke des Krankenhauses aufwachte."


"Erst nachdem ich sie ein paar Sekunden lang angestarrt habe, begreife ich, wo ich bin. Dies ist Hanakos Zimmer."


"Es fühlt sich an, als hätte mein Herz wieder aufgehört zu schlagen, als mir die Ereignisse der letzten Nacht durch den Kopf gehen. Blut schießt in meine Wangen, und ich schließe meine Augen aufs Neue."


"Allerdings bringt es kaum etwas, mich so früh am Morgen aufzuregen, also versuche ich, solche Dinge fürs Erste aus meinem Kopf zu verdrängen."


"Ich rolle meinen Kopf zur Seite, um zu sehen, ob Hanako noch da ist, wo sie war, als ich weggedämmert bin. Alles, was jetzt noch da ist, ist eine leere Stelle auf dem Bett, und der Raum dahinter."


"Träge setze ich mich auf und reibe mir die Augen, bevor ich mir an die Nasenwurzel fasse und mich im Zimmer umsehe."


show bg school_dormhanako onlayer master at right
with charamove_slow

"Ich bin der Einzige hier. Ich bin immer noch ohne meine Kleidung, und nach einer kurzen Suche auf dem Boden bemerke ich, dass sie ordentlich gefaltet in einer Ecke des Zimmers liegt. So sehr ich es auch versuche, ich kann Hanako nirgends entdecken."


"Die Verpackung des Kondoms wurde auch entfernt und wahrscheinlich in den Mülleimer geworfen."


"Nach einem beträchtlichen Gähnen steige ich aus dem Bett und suche zügig nach Unterwäsche."
"Mein Gesicht verzieht sich etwas bei dem Gedanken, die Boxershorts wieder anzuziehen, nachdem die gestrigen Aktivitäten ihre Spuren auf ihr hinterlassen haben, aber ich habe nicht wirklich eine Wahl."


"Ich nutze den Vorteil, dass ich etwas Zeit ohne jemanden in der Nähe habe, um mich in kurzer Zeit für den kommenden Schultag anzuziehen."


"Und dann… bin ich allein."


"Ohne etwas, womit ich mich noch beschäftigen könnte, fixiert sich mein Kopf auf die Tatsache, dass ich im Schlafzimmer einer anderen stehe, nachdem wir die Nacht zusammen verbracht haben, es in der Nähe aber kein Anzeichen von ihr gibt."


play sound sfx_rumble

"Mein Bauch erweist sich bei der Lösung dieses Rätsels als hilfreicher als mein Gehirn. Mit einem lauten Knurren erinnert er mich daran, dass sie vielleicht einfach Frühstück holen gegangen ist."


"Ich wäre lieber neben ihr aufgewacht, aber… vielleicht ist es eine gute Sache, dass ich ein paar Momente für mich allein habe."


"Hanakos Zimmer ist – wie immer – ziemlich trostlos. Es gibt herzlich wenig Dekoration, und praktisch keine persönlichen Dinge, die nicht in Schränken oder Schubladen versteckt sind."


"Sie lebt hier seit drei Jahren, aber das Zimmer sieht aus, als wäre es kaum einen Tag belegt gewesen."


"Ich sollte nicht zu viel darüber nachdenken. Vielleicht lebt sie einfach gerne so. Mit so wenig Besitztümern zufrieden sein zu können, hat seine Vorteile, aber in Anbetracht ihrer Vergangenheit fühlt es sich etwas befremdlich an."


"Sie sagte, dass ihr Leben im Waisenhaus stillstand. Sie lebt zwar noch immer so, als ob es so wäre, aber… nach dem, was letzte Nacht passiert ist, ist es ziemlich schwierig, sich vorzustellen, dass sie immer noch so denkt."


play sound sfx_dooropen

"Das Geräusch der Türklinke reißt mich aus meinen Gedanken, und ich sehe zur Tür."


show hanako basic_normal onlayer master at center
with charaenter

"Tatsächlich kommt Hanako hindurch und schließt die Tür hinter sich. In ihren Händen hält sie etwas, das wie zwei in der Mikrowelle zubereitete Fertiggerichte aussieht, was die ganze Sache ein bisschen erschwert."


hi "Guten Morgen, Hanako."


show hanako basic_bashful onlayer master
with charachange

ha "M-Morgen."


"Sie verbeugt sich kurz, bevor sie sich zu ihrem Schreibtisch begibt und die beiden Teller abstellt. Nun kann ich die beiden dampfenden Teller mit Satay-Spießen sehen, bei denen je eine Gabel im Reis steckt."


show hanako basic_distant onlayer master at Position(ypos=1.15)
with dissolvecharamove

"Ich bedanke mich bei ihr, dass sie sie mitgebracht hat. Dann nehmen wir jeweils einen Teller und fangen an zu essen. Sie sitzt auf ihrem Schreibtischstuhl, während ich auf der Bettkante sitze."


"Ich rede nicht gerne, während ich esse, darum ist das Schweigen zwischen uns an sich nicht störend – aber dieses Schweigen besteht nur, weil wir beide nicht ganz wissen, was wir zueinander sagen sollen."


show hanako basic_normal onlayer master
with charachange

show hanako basic_distant onlayer master
with charachange

"Hanako wirft mir beim Essen hin und wieder einen Blick zu. Ich bemerke es nur, weil ich genau dasselbe tue."


"Wir essen gemeinsam, als wären wir ein Paar. Wir hatten sogar letzte Nacht Sex – für uns beide das erste Mal. Jedoch fühlt sich etwas… falsch an."


"Vielleicht können wir deswegen nicht ein Wort zueinander sagen, als wir unsere Teller leeressen und sie auf dem Tisch lassen."


scene bg school_girlsdormhall onlayer master
with locationchange

"Vielleicht halten wir deswegen keine Hände oder machen Smalltalk, als wir Hanakos Raum verlassen."


"Vielleicht kommt es mir deswegen so vor, als wären wir uns entfernter als wir es je gewesen sind."


scene bg school_scienceroom onlayer master at left
with locationskip

"Wir betreten zusammen das Klassenzimmer, wobei keiner von uns den anderen auch nur ansieht. Direkt nachdem wir das tun, fällt mir ein, dass das ein Fehler gewesen sein könnte. Shizune hebt bei dem Anblick argwöhnisch ihre Augenbraue."


show hanako cover_distant onlayer master at center
with charaenter

"Wir erreichen den Gang zwischen den Tischen des Klassenzimmers und sehen einander an. Ich bin mir nicht wirklich sicher, was ich sagen soll."
"Will sie, dass ich sie als meine Freundin anrede? Ich dachte nicht, dass unsere Beziehung… Oh. Darum fühlt sich das so komisch an."


hi "B-Bis dann."


show hanako cover_bashful onlayer master
with charachange

ha "Okay."


hide hanako onlayer master
with charaexit

"Unbeholfen halte ich eine Hand hoch, als wir uns trennen und unsere jeweiligen Plätze einnehmen."


"Aus Verlegenheit kann ich nicht einmal zu ihr zurückschauen. Es kommt mir vor, als wäre die Kluft zwischen mir und Hanako nur meinetwegen da."


show shizu invis onlayer master:
    center
    xpos -0.1
show muto invis onlayer master:
    center
    xpos 0.75
with None

show shizu basic_normal onlayer master:
    xpos 0.0
with dissolvecharamove

show muto normal onlayer master:
    tworight
with dissolvecharamove

"Shizune will gerade zu mir kommen, doch da betritt Mutou den Raum."


show shizu invis onlayer master at Position(xpos=-0.1)
with dissolvecharamove

"Ich bin dankbar dafür, dass er gerade rechtzeitig ankommt und Shizunes Befragung fürs Erste verhindert."


"Ich hätte ihr sowieso nicht antworten können."


"Ich mag Hanako, aber ich habe ihr nie gesagt, wie ich für sie empfinde. Hanako hat nie auch nie gesagt, dass sie in mir mehr als nur einen Freund sieht. Und trotzdem haben wir miteinander geschlafen."


stop music fadeout 2.0

scene bg school_scienceroom onlayer master at left
with shorttimeskip

play sound sfx_normalbell

"Die Glocke zum Beginn der Mittagspause ertönt. Mutou ist etwas überrascht – und anscheinend auch enttäuscht – dass seine Chemie-Lektion mitten im Satz unterbrochen wird."


"Für die gesamte Klasse gingen seine Abschweifungen in das eine Ohr hinein und zum anderen wieder heraus, während ich über Hanako grüble. Ich kriege sie nicht aus meinem Kopf, und mittlerweile habe ich es geschafft, mich in etwas hineinzusteigern."


"Mir wird klar, dass sie nie ja zu dem gesagt hat, was wir getan haben."
"Sie hat auch nicht nein gesagt, aber… wäre sie dazu in der Lage gewesen? Zu ihren besten Zeiten kann sie sehr unterwürfig sein, und ohne Zweifel hat es ihr gewaltige Mühen abverlangt, mir ihre Narben zu zeigen."


"Ich beschließe, es zu versuchen und zumindest eine Unterhaltung mit ihr anzufangen. Bisher haben wir heute – außer einsilbiger Kommunikation – nichts zustande gebracht."


show bg school_scienceroom onlayer master at bgleft
with charamove_slow

show hanako emb_downtimid onlayer master:
    center
    ypos 1.15
with charaenter

"Ich laufe zu ihrem Tisch und habe vor, mich mit ihr zu unterhalten, doch schon bevor ich bei ihr ankomme, läuft sie verlegen rot an und sieht nach unten."


play music music_rain fadein 4.0

"Ich hole tief Luft, um zu sprechen, finde dann aber keine Worte. Was in aller Welt soll ich ihr nur sagen?"


"Als ich sich nähernde Schritte höre, drehe ich mich um, um zu sehen, wie Shizune und Misha sich bereits auf dem Weg zu uns befinden. Ohne Zweifel wollen sie lästige Dinge fragen."


"Ein paar andere Klassenkameraden tratschen unter sich, während sie uns verstohlene Blicke zuwerfen. Sie müssen auch bemerkt haben, wie ich und Hanako vorhin zusammen hereingekommen sind."


"Ich öffne meinen Mund, um Hanako zu beschwichtigen, doch sie kommt mir zuvor."


show hanako def_strain onlayer master
with charachange

ha "Ich… Ich…"


show hanako defarms_strain onlayer master:
    center
with Dissolvemove(0.3)

ha "Ichhabnochwaszuerledigen!"


show hanako defarms_strain onlayer master:
    easeout 0.5 alpha 0.0 xpos 0.0 xanchor 1.0
with Pause(0.5)

hide hanako onlayer master
with None

"Sie springt von ihrem Stuhl auf und rast durch die Tür. Eine paar der Bücher und Stifte, die auf ihrem Tisch lagen, werden durch ihre Eile auf den Boden geworfen."


"Anscheinend sind nicht viele Leute an diesem Ereignis interessiert. Ein paar sehen sich um, um zu sehen, worum es bei all dieser Aufregung geht, wenden sich dann aber wieder ihrer vorigen Tätigkeit zu."


"Verzweifelt stehe ich da und sehe zur Tür, durch die Hanako gerade verschwunden ist. Der Gedanke, ihr nachzurennen, schießt mir durch den Kopf, aber ich bin mir ziemlich sicher, dass Hanako schneller rennen kann als ich."


"Und außerdem… Was soll ich ihr sagen, sobald ich sie eingeholt habe?"


"Schließlich hocke ich mich einfach hin und hebe die Gegenstände auf, die von ihrem Tisch auf den Boden gefallen sind. Ich fühle mich in jeglicher Weise schlecht, als Schüler auf ihrem Weg aus dem Raum heraus an mir vorbeilaufen."


show shizu invis_close onlayer master:
    tworight
    xpos 0.8
show misha invis_close onlayer master:
    twoleft
    xpos 0.2
with None

show shizu behind_blank_close onlayer master at tworight
show misha perky_smile_close onlayer master at twoleft
with dissolvecharamove

"Ich spüre ein Tippen auf meiner Schulter. Ich sehe auf, um Shizunes und Mishas Blick zu erwidern."
"Den beiden steht die Neugier ins Gesicht geschrieben – teilweise auch gemischt mit einem entschuldigenden Blick, da sie zum Teil für das gerade Geschehene verantwortlich sind."


show shizu basic_normal2_close onlayer master
with charachange

shi "…"

show misha sign_confused_close onlayer master
with charachange

mi "Hicchan, wenn wir dir irgendwie helfen können…"


"Ich schüttle lediglich meinen Kopf. Das geht sie nichts an, und Shizunes Gesichtsausdruck und Mishas Stimmlage nach zu Urteilen wissen sie das genauso gut."


show shizu behind_blank_close onlayer master
with charachange

with Pause(0.3)

hide misha onlayer master
hide shizu onlayer master
with charaexit

"Shizune nimmt meine Antwort zur Kenntnis und verbeugt sich feierlich, bevor sie den Raum verlässt. Misha folgt ihr hinaus und spielt gehorsam ihre Rolle als Shizunes Schatten."


"Ich erhebe mich – mit den Büchern und Stiften in meiner Hand – und lege sie unter Hanakos Tisch. Da das Klassenzimmer nun leer ist, lehne ich mich schließlich nur gegen ihren Schreibtisch und denke still nach."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\nEs fühlt sich an, als gäbe es eine komplette emotionale Trennung zwischen mir und Hanako. Wir kennen uns noch nicht so lange, und obwohl ich mit ihr zusammenkommen wollte, weiß ich nicht wirklich, wie Hanako die Dinge sieht."


n "Ich habe so viel für die Prüfungen gelernt, wie ich konnte, aber es kommt mir noch immer so vor, als hätte ich keinen wirklichen Plan für die Zukunft. Ich habe versucht, ein Freund für Hanako zu sein, auch wenn ich ihr meine Gefühle nicht gestehen konnte, und alles, was wir getan haben, hat die Kluft zwischen uns nur noch vergrößert."


n "\nIch konnte nicht mal einen Brief an das einzige Mädchen schreiben, das mich je geliebt hat: Iwanako."


n "\nWas soll ich tun…? Was kann ich tun…? Ich weiß die Antwort einfach nicht – auf keine dieser Fragen. Und ich weiß, dass niemand mir damit helfen kann."


n "Einfach wieder zum Status Quo zurückzukehren, würde mich schon glücklich machen, aber ich weiß, dass das niemals passieren kann. Etwas hat sich letzte Nacht zwischen uns verändert. Vielleicht auch schon vorher, und es hat sich dann erst zugespitzt."


nvl clear

n "\n\nIch weiß, dass da eine Mauer ist, die Hanako zwischen mir und sich selbst errichtet hat. Jedes Mal, wenn ich irgendwie mit ihr interagieren wollte, bin ich gegen diese Mauer geprallt."


n "Doch nun fange ich an zu glauben, dass ich genauso wie sie meine eigene Mauer errichtet habe. Sie musste mir meine Vergangenheit praktisch aus die Nase ziehen, und meine war viel weniger traumatisch als ihre."


n "Ich würde gerne sagen, dass es daran lag, dass ich nach meiner Herzattacke kaum Zeit hatte, mich anzupassen, aber ich weiß ganz genau, dass das nur eine Ausrede wäre."


n "Das einzige Mal, dass es mir wirklich so vorkam, als würde sie sich mir aus eigenem Antrieb öffnen, war, als wir in der Stadt Billard spielten. Damals war ich derjenige, der sie davon abhielt."


n "\n\nIch will Hanako besser kennen. Ich will unsere Freundschaft retten, wenn möglich sogar eine echte Beziehung mit ihr beginnen."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show

"Während ich in dem leeren Klassenraum, in dem wir so viel Zeit miteinander verbracht haben an ihrem Tisch lehne, beginne ich, einen Plan zu schmieden."


stop music fadeout 2.0

"Ich muss mit Hanako reden."




label de_H31:

scene bg suburb_park onlayer master
with shorttimeskip

play music music_moonlight fadein 0.5

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 2.0

"Ich streife im Park umher, und ein Gefühl der Beklommenheit überkommt mich. Hin und wieder greife ich in meine Hosentasche, um mein Handy herauszuholen, doch jedes einzelne Mal zögere ich und schiebe es letztendlich wieder hinein."


"Wenn das eine normale Situation wäre, würde ich nicht den Unterricht schwänzen. Unglücklicherweise ist es keine, also finde ich mich um zwei Uhr nachmittags im Dorf unter der Schule wider."


"Seit ich Hanako getroffen habe, bin ich immer derjenige gewesen, der die Initiative zwischen uns ergreifen musste. Derjenige, der die Unterhaltungen angefangen hat, dorthin ging, wo auch immer sie war, und vorschlug, was wir tun sollten."
"Heute, dieses eine Mal, will ich das nicht sein."


"Meine Hand taucht ein weiteres Mal in meine Hosentasche. Dieses Mal navigiere ich zügig zum SMS-Menü, bevor ich die Chance habe, mich wieder umzuentscheiden."


"„Hanako, falls du reden willst, werde ich eine Weile im Park unten im Dorf sein.”"


"Ich unterdrücke meine letzten Zweifel, tippe die Nachricht für Hanako ein und drücke den Knopf, um sie abzuschicken."


"Und jetzt… warte ich. Meinen Teil habe ich erfüllt; nun muss Hanako die Entscheidung treffen. Es hätte keine Bedeutung, wenn ich sie hierherschleifen würde. Sie muss für sich selbst entscheiden, ob sie mich treffen will."


stop ambient fadeout 4.0

with shorttimeskip

"Der Apfelsaft aus dem Verkaufsautomaten schmeckt furchtbar bitter, als ich ihn hinunterstürze. Mein Griff um die Dose hat in ihrer Mitte eine kleine Delle hervorgerufen."


"Ich sollte nicht so angespannt sein, aber das ist wahrscheinlich unvermeidbar."


"Hanako ist mir wichtig."


"Was die letzten paar Tage passiert ist, hat uns beide sehr unter Druck gesetzt. Der Gedanke, all unseren Annäherungsfortschritt und unsere Freundschaft als Ganzes zu verlieren, ist äußerst beunruhigend."


"Doch selbst dann… weiß ich immer noch nicht, wie nahe wir uns eigentlich stehen. Wie mögen Sex gehabt haben, aber davor sind wir meines Erachtens nur Freunde gewesen. Vielleicht sind wir mehr als das, aber wenn es so ist, habe ich es nie bemerkt."


"Vielleicht fühle ich mich deswegen gerade so unwohl. Trotz all der Zeit, die wir miteinander verbracht haben, verstehe ich Hanako nicht. Die Minuten vergehen, und ich habe immer noch keine Ahnung, ob sie auftauchen wird."


ha "H-Hisao…?"

"Ich halte einen Moment lang inne und zweifle einen Moment daran, dass ich diese Stimme wirklich höre. Ich lasse die Dose fallen und stehe mit einem Ruck auf."


show hanako basic_worry_cas onlayer master at center
with charaenter


hi "Hanako…"

show hanako emb_downtimid_cas onlayer master
with charachange

"Wir sehen einander für ein paar Sekunden an, bevor Hanako zu verlegen wird, um den Augenkontakt zu halten. Nervös fängt sie an, an den Haaren herumzufummeln, die die Seite ihres Gesichts bedecken."


"Als ich nach ihrem Zusammenbruch zu Hanakos Zimmer gegangen bin, um nach ihr zu sehen, hatte ich keine Ahnung, was ich sagen sollte. Damals war das in Ordnung. Alles, was wir beide wollten, war die Gegenwart des anderen."


"Aber jetzt… bin ich der Meinung, dass ich direkt mit ihr reden muss. Ich will diese Mauer zwischen uns einreißen, bevor sie uns endgültig auseinanderzwingt."


stop music fadeout 4.0

hi "Hanako… Ich…"


hi "Was wir letzte Nacht getan haben… Wie soll ich das interpretieren?"


show hanako cover_worry_cas onlayer master
with charachange

"Hanako hört auf, an ihren Haaren herumzufummeln, und sieht mich an, wobei sie ihren Kopf leicht hängen lässt. Sie sieht beschämt aus, was wahrscheinlich ein guter Spiegel meiner selbst wäre, wenn ich nicht gerade so besorgt wäre."


show hanako basic_worry_cas onlayer master
with charachange

play music music_innocence fadein 4.0

ha "Ich dachte… du würdest irgendwann weggehen, wenn ich nur jemand wäre, den du beschützen musst."


show hanako emb_sad_cas onlayer master
with charachange

ha "Ich dachte, wenn ich dich das tun lasse… würdest du in mir mehr sehen als so jemanden."


"Meine erste Reaktion ist Fassungslosigkeit, aber… schließlich habe ich es mit ihr getan."
"Ich hatte reichlich Gelegenheiten, in denen ich es hätte aufhalten können – zurückweichen und mich fragen, was wir da eigentlich tun. Aber letzten Endes… habe ich es nicht."


"Ein schreckliches Gefühl entsteigt meiner Magengrube. Sie hat sich mir angeboten, weil sie dachte, dass ich es will, und jetzt kommt es mir vor, als hätte ich sie ausgenutzt. Sie mag es gewollt haben, aber unter den falschen Prämissen."


"Ich bin nie gut darin gewesen, meine Emotionen zu verbergen, und jetzt ist es nicht anders. Hanako sieht wieder einmal nach unten. Eine seltsame Mischung aus Bedrückung, Bedauern und Schwäche steht ihr ins Gesicht geschrieben."


"Eine schwere Stille hängt in der Luft, abgesehen von der Brise, die durch die Bäume um uns herum weht."


show hanako emb_downsad_cas onlayer master
with charachange

ha "Ich wusste… dass du mich nicht auf diese Weise sehen konntest."


"Hanakos Worte sind kaum mehr als ein Flüstern und anscheinend genauso sehr an sich wie an mich gerichtet."


hi "Auf welche Weise? Wovon redest du?"


ha "Alles, was ich je für dich war… war eine nutzlose Person. Nur jemanden… den du beschützen musstest. Wie ein… Kind."


show hanako cover_distant_cas onlayer master
with charachange

ha "I-Ich wollte für dich mehr sein als das, aber nach so langer Zeit habe… ich… mich daran gewöhnt."


"Ihre Stimme klingt anders, als ich sie je zuvor gehört habe. Sie klingt angewidert. Nicht meinetwegen, sondern wegen sich selbst."


show hanako cover_worry_cas onlayer master
with charachange

ha "Nachdem ich aus meinem Zimmer kam… erkannte ich, dass du dabei warst, dich langsam von mir zu entfernen."


show hanako basic_worry_cas onlayer master
with charachange

ha "Es fühlte sich an, als würde ich dich verlieren, weil… du jemanden wolltest… mit dem du diese Art von Beziehung haben könntest."


show hanako emb_downtimid_cas onlayer master
with charachange

ha "Du hast nicht mehr so viel mit mir in der Schule gesprochen, und du hast dich so gut mit Yuuko verstanden… Ich dachte… ich würde dich verlieren."


"Sie dachte, sie wäre mir langweilig geworden, weil ich eine romantische Beziehung wollte?"


hi "Aber… wir sind doch Freunde, oder? Ich würde dich nicht einfach so verlassen, selbst wenn das, was du sagst, wahr wäre."


show hanako emb_timid_cas onlayer master
with charachange

ha "Freundschaft… war etwas, von dem ich dachte, dass ich es aufgegeben hätte. Ich hörte auf, anderen zu vertrauen… wegen der Dinge, die nach dem Unfall passiert sind."


show hanako emb_downsad_cas onlayer master
with charachange

ha "Vor dem Unfall kam ich mit Menschen und anderen Kindern gut zurecht. Ich hatte nicht viele Freunde… aber es störte mich nicht, weil ich die zu schätzen wusste, die ich hatte."


show hanako emb_sad_cas onlayer master
with charachange

ha "Aber danach…"


show hanako emb_downsad_cas onlayer master
with charachange

ha "Ich wurde von anderen beschimpft, und sehr oft gehänselt. Es… verletzte mich zutiefst. Die Lehrer versuchten zu helfen, aber sie konnten nicht viel tun, und viele schreckten sogar bei meinem bloßen Anblick zurück."


ha "Unter denen, die mich beschimpften und hänselten… waren diejenigen, von denen ich dachte, dass sie meine engsten Freunde wären."


show hanako cover_worry_cas onlayer master
with charachange

ha "Ab da an glaubte ich, dass es egal wäre, wenn mich niemand beachten würde. Immerhin war meine Existenz für andere Leute immer nur störend. Es war… einfacher… einfach nicht zu existieren."


show hanako cover_bashful_cas onlayer master
with charachange

ha "Aber als ich Lilly traf, und dann dich…"


show hanako basic_normal_cas onlayer master
with charachange

ha "Ich hab es versucht, aber ich… konnte nicht wieder so denken wie vorher."


"All die Zeit… hat sie mir nicht vertraut. Sie dachte, wie es jeder andere in ihrem Leben tat, dass sie wertlos sei. Jemand, den ich wegwerfen würde, sobald mir ihre Nähe langweilig geworden wäre."


"Das tut weh. Das ist die einzige Art von Mensch, als die ich niemals gesehen werden wollte, weil ich besser als die meisten weiß, wie furchtbar es sich anfühlt, von denen weggeworfen zu werden, von denen man dachte, dass sie einen mögen."


"Sie bricht wegen ihrer Erinnerungen in Tränen aus. Ich komme mir nutzlos vor; vollkommen unfähig, sie zu trösten. Aber auf eine seltsame Weise bin ich fast dankbar, dass sie mir erlaubt, das zu erfahren."


"Die Mauer zwischen uns verschwindet, auch wenn das Einreißen so sehr schmerzt."


hi "Hanako, wenn du mir das nur gesagt hättest…"


show hanako cover_worry_cas onlayer master
with charachange

ha "Lag ich… falsch?"


hi "Natürlich lagst du…"


"Lag sie nicht. Hanako lag nicht falsch. Es ist schwierig, mich dazu zu zwingen, mir das einzugestehen, aber ich weiß, dass es sinnlos wäre, es zu leugnen. Für mich – und für Lilly – war sie jemand, den wir zu beschützen versuchten."


"Sie war für mich das geworden, was ich für meine Freunde nach meiner Herzattacke geworden war – ein gebrochener Mensch. Ich mochte sie, vielleicht liebte ich sie sogar, aber ich habe nie so gehandelt, weil ich dachte, dass sie zu zerbrechlich sei."


hi "Ich meine… jetzt sehe ich dich nicht mehr auf diese Weise."


hi "Nach dem, was im Unterricht mit dir passiert war, hatte ich mir Sorgen um dich gemacht, und ich dachte, ich sollte versuchen, dich zu beschützen."


hi "Aber als du dich in deinem Zimmer eingesperrt hast, bekam ich Angst. Ich dachte, du würdest mich zurückweisen, und es zwang mich dazu, über eine Menge… verschiedener Dinge nachzudenken."


show hanako defarms_strain_cas onlayer master
with charachange

ha "Ich habe dich nicht zurückgewiesen!"


"Sie platzt damit in einem fast ängstlichen Tonfall heraus, was mich völlig unvorbereitet trifft. Sofort ist ihr der Gefühlsausbruch peinlich, aber dann ballt sie ihre Fäuste und legt sich die Worte zurecht, die ihr auf der Zunge liegen."


show hanako emb_timid_cas onlayer master
with charachange

ha "Das würde ich niemals tun. Nicht bei dir."


show hanako emb_downtimid_cas onlayer master
with charachange

ha "Auch wenn ich Angst hatte… auch wenn ich versucht habe, dich abzuweisen… du hast trotzdem versucht, mir näherzukommen."


ha "Ich habe mich eingesperrt, weil… ich nur eine Bürde für dich war. Für Lilly. Für alle."


show hanako emb_sad_cas onlayer master
with charachange

ha "J-Jeder Geburtstag war das Gleiche. Jeder tat sein Bestes, um so zu tun, als wäre ich wichtig. Jeder tat so, als wäre alles in Ordnung… für diesen einen Tag im Jahr."


show hanako emb_downsad_cas onlayer master
with charachange

ha "Ich wollte nicht existieren, aber sie ließen mich nicht. Sogar nachdem ich Lilly traf… war alles das Gleiche. Ich war so nutzlos wie ich es schon immer gewesen bin – unfähig, irgendetwas für sie oder für mich selbst zu tun."


ha "Für dich… wollte ich nicht dasselbe sein."


"Lilly und ich lagen komplett falsch. Ihren Worten zufolge war alles, was wir für sie getan haben… Es hätte ihr nur ein noch mieseres Gefühl gegeben."
"Sogar das Bisschen über sie, von dem ich dachte, ich würde damit richtig liegen, war ein komplettes Fehlurteil."


hi "Nachdem du dich in deinem Zimmer eingeschlossen hattest, beschloss ich ebenfalls, meine eigene Vergangenheit auf die Reihe zu kriegen."
hi "Ich wusste nicht, wie ich mit den Dingen umgehen sollte, die ich durch meinen Wechsel an die Yamaku verloren hatte. Also versuchte ich, allein damit zurechtzukommen."


hi "Ich dachte… wenn ich das täte, würde es uns helfen… bessere Freunde zu werden…"


hide hanako onlayer master
with charaexit

"Stille hängt wieder in der Luft. Ich versuche, sie weiter anzusehen, kann es aber nicht. Ich fühle mich richtig niedergeschlagen, und auch wenn ich mich entschuldigen will… weiß ich nicht, wie ich das tun soll."


"Ich höre, wie sie einen tiefen Atemzug macht, und sehe erst wieder zu ihr, als ich höre, wie sie zu Boden sackt."


scene ev hanako_park_alone onlayer master
with whiteout

"Sie weinen zu hören, bricht mein Herz. Ich weiß, dass ich dafür verantwortlich bin, und ich weiß, dass ich nichts tun kann, um ihr zu helfen. Wenn Hanako sich schämt, dann tue ich es umso mehr."


show ev hanako_park_away onlayer master
with charachange

"Ich eile zu ihr, während ihre Tränen weiter unvermindert ihre Wangen herunterlaufen, und wickle meine Arme um sie. Mir ist mittlerweile egal, wie ich aussehen muss. Ich will ihr jetzt einfach nur nahe sein."


ha "Es tut mir leid, Hisao… I-Ich habe alles kaputtgemacht…"


hi "Schon okay. Alles ist okay. Ich bin der, dem es leidtun sollte. Ich hab mich hinter deinem Rücken eingemischt und dir nie etwas davon erzählt."


"Ich kann spüren, wie mein Griff um Hanako fester wird, während gleichzeitig meine Sicht verschwimmt. Ich darf mich jetzt nicht zurückhalten lassen. Als sich ein Kloß in meinem Hals bildet, muss ich meine Worte herauszwingen."


hi "Um dir die Wahrheit zu sagen, Hanako… hatte ich Angst. Zum ersten Mal seit meiner Herzattacke hatte ich wirklich Angst."


show ev hanako_park_look onlayer master
with charachange

ha "Hisao…?"

hi "Ich verlor so viel, als ich nach Yamaku kam. Ich war… von dir abhängig – mehr als ich es je gedacht hätte."


hi "Sogar jetzt habe ich noch dieses Loch in mir. Nachdem ich mein gesamtes Leben und jeden, den ich kannte, verloren hatte, war der Gedanke, dich auch noch zu verlieren…"


show ev hanako_park_away onlayer master
with charachange

ha "Aber ich bin nur ein nutzloses…"


hi "Du bist meine Freundin, Hanako! Du bist…"


hi "Nein, du bist mehr als das. Ich liebe dich, Hanako. Ich liebe dich so sehr, dass der Gedanke, dich zu verlieren, mir so viel Angst bereitet hat…"


"Ah, das ist nicht gut… Ich lasse wirklich alles heraus. Ich kann mich gerade nicht einmal dazu überwinden, ihr ins Gesicht zu sehen."


show ev hanako_park_look onlayer master
with charachange

ha "Es tut mir leid, Hisao…"


ha "Ich kann nicht anders… als mich ein wenig zu freuen. Das wollte ich… seit so langer Zeit… schon hören…"


show ev hanako_park_closed onlayer master
with charachange

"Die letzten Dämme brechen, und ihr Weinen durchdringt die Luft, als ihr Körper in meinen Armen zittert. Wir halten einander fest; verbundener als je zuvor in unserem geteilten Leid und in unserem geteilten Glück."


"Ich weiß nicht, wie die Dinge hiernach aussehen werden. Aber im Augenblick… ist mir das egal. Es gibt keinen anderen Menschen auf der Welt, mit dem wir beide diese Erinnerungen und Emotionen teilen könnten. Keinen."


stop music fadeout 2.0

scene bg suburb_park onlayer master
with shorttimeskipsilent

play ambient sfx_parkambience fadein 2.0
play sound sfx_can_clatter

"Ich lasse die schmutzige Dose in den Mülleimer neben der Bank fallen, und nehme neben Hanako platz. Sie steckt das Taschentuch weg, das ich ihr gegeben habe, damit sie sich saubermachen kann. Viel geholfen hat es allerdings nicht."


"Andererseits bezweifle ich, dass ich viel vorzeigbarer aussehe. Sogar jetzt fühle ich mich noch leer und bin etwas verlegen, dass ich meine Emotionen so in der Öffentlichkeit zur Schau gestellt habe."
"Doch es ist kein schlechtes Gefühl. Ich denke, Hanako empfindet das Gleiche."


hi "Hast du dich etwas beruhigt?"


play music music_comfort fadein 4.0

show hanako cover_bashful_cas_close onlayer master:
    tworight
    ypos 1.1
with charaenter

ha "J-Ja. Danke."


"Für eine Weile sitzen wir lediglich da und lassen uns Zeit, bevor wir weiter miteinander reden. Wir brauchen beide ein wenig Zeit, um uns wieder zu sammeln."


show hanako basic_smile_cas_close onlayer master
with charachange

ha "Das Wetter ist um diese Jahreszeit wirklich schön."


hi "Ja, das ist es."


show black onlayer master
with shuteye 

"Ich schließe meine Augen für einen Moment und genieße das Gefühl der warmen Sonne und der kalten Brise auf meinem Gesicht. Das Wetter ist heute wirklich schon. Wirklich, wirklich schön."


hi "Weißt du… Ich hab nicht wirklich Lust, jetzt noch zurück zum Unterricht zu gehen. Du etwa?"


hide black onlayer master
show hanako basic_bashful_cas_close onlayer master
with openeye

"Sie schüttelt den Kopf, nachdem sie sich ihre Augen mit ihrem Ärmel abgewischt hat. Das kleine Lächeln, das sie mir schenkt, erinnert mich daran, wie aufrichtig es sein kann."


"Für andere Menschen zu lächeln mag etwas vollkommen Normales und Alltägliches sein. Aber für Hanako… Sie lächelt so selten und so ehrlich, dass mich jedes Mal ein Gefühl der Erleichterung und des Glücks überkommt."


show hanako cover_worry_cas_close onlayer master
with charachange

ha "Es tut mir leid. Alles…"


hi "Es ist okay. Ich glaube, wir haben beide etwas, das uns leid tut."


show hanako emb_timid_cas_close onlayer master
with charachange

ha "Das weiß ich… ich bin zu schüchtern. Ich weiß, dass du das an mir nicht magst, aber ich glaube nicht, dass ich…"


hi "Du kannst dich ändern, Hanako. Ich weiß das, weil du es in der kurzen Zeit, in der ich dich kenne, bereits getan hast."
hi "Um ehrlich zu sein: Dass ich hier sitzen und so mit dir reden kann, bedeutet, dass du dich seit unserem ersten Treffen sehr stark verändert hast."


show hanako emb_downtimid_cas_close onlayer master
with charachange

ha "Aber… so kann ich… für keinen anderen sein. Für die Zeit nach der Schule habe ich auch keine Pläne…"


"Hanakos Selbstbewusstsein beginnt wieder zu bröckeln, aber ich glaube, dass ich mit ihr nun endlich wie mit einer Gleichgestellten reden kann. Das kann ich, weil ich weiß, dass wir auf so vielen Ebenen genau gleich sind."


hi "Gib dir einfach Zeit, und ich denke, du wirst das erreichen, was du erreichen willst. Nein, ich bin mir sicher, dass du wirst. Ich kann sehen, dass du es versucht hast, und ich glaube an dich."


hi "Und du weißt, dass du dich auf mich verlassen kannst, wenn du jemanden brauchst, der dich unterstützt."


show hanako defarms_strain_cas_close onlayer master
with charachange

ha "A-Aber das kann ich nicht von dir verlangen…"


hi "Du kannst, weil es genau das ist, worum ich dich bitte. Ich mache das gleiche durch, weißt du."


hi "Es nennt sich Liebe."


show hanako basic_bashful_cas_close onlayer master at tworight
with dissolvecharamove

"Hanako lächelt, bevor ich aufstehe und mir den Staub abklopfe. Sie tut kurzum dasselbe."


hi "Ich bin ziemlich hungrig. Wollen wir uns was zu Essen besorgen?"


"Sie nickt energisch. So wie sie lächelt, wie sie sich verhält, sogar nur ihre allgemeine Ausstrahlung… Es kommt mir vor, als wäre dies das erste Mal, dass ich sie wirklich glücklich sehe."


$ renpy.music.set_volume(0.6, 1.0, channel="ambient")

scene bg suburb_roadcenter onlayer master
with locationchange

"Wir machen uns auf den Weg zur Straße – Seite an Seite."


show hanako emb_emb_cas_close onlayer master at center
with charaenter

ha "Hisao?"


hi "Ja?"


show hanako emb_downtimid_cas_close onlayer master
with charachange

ha "Ich… Ich glaube… ich verstehe dich nicht wirklich."


hi "Ich glaube auch nicht, dass ich dich verstehe. Aber ich glaube, das ist okay."


"Es gibt nicht ein einziges Anzeichen von Verzweiflung in unseren Stimmen. Den jeweils anderen nicht zu verstehen, ist nur natürlich; die Mauer, die wir zwischen uns errichtet haben, kann unmöglich an einem Tag eingerissen werden."


"Aber das ist okay. Solange wir es Tag für Tag angehen und versuchen, einander zu verstehen… denke ich, dass alles gut werden wird."


show hanako emb_timid_cas_close onlayer master
with charachange

show hanako emb_downtimid_cas_close onlayer master
with charachange

"Doch als wir die Straße entlanglaufen, huschen Hanakos Augen wiederholt zu meinem Gesicht und wieder auf die Straße."


hi "Liegt dir was auf dem Herzen? Du siehst unruhig aus."


show hanako basic_normal_cas_close onlayer master
with charachange

"Sie wird langsamer und hält dann gänzlich an. Als ich mich zu ihr drehe, nimmt sie einen langen, tiefen Atemzug und sieht mir aufmerksam ins Gesicht."
"Dieser Gesichtsausdruck… ich habe ihn schon einmal bei ihr gesehen. Nur einmal, als ich sie aus Versehen in ihrem Zimmer überrascht habe."


ha "Ich… ich glaube… ich glaube, ich habe etwas… was ich dir geben muss."


hi "Was denn? Du kannst es ruhig sagen."


show hanako cover_distant_cas_close onlayer master
with charachange

ha "Ich wollte dir das schon eine lange, lange Zeit geben, aber… jetzt, wo ich es tun muss… ist es zu peinlich…"


hi "Keine Sorge. Ich werde es annehmen, was auch immer es ist."


show hanako basic_bashful_cas_close onlayer master
with charachange

"Sie schenkt mir ein süßes, verlegenes Lächeln, bevor sie ihre Hand auf meine Schulter legt."


ha "Dann nimm bitte mein erstes Geschenk für dich an, Hisao…"


hi "Hanako…?"


stop ambient fadeout 1.0

window hide
scene unlock_ev hanako_goodend_close onlayer master
show unlock_ev hanako_goodend_muffin onlayer master
show unlock_ev hanako_goodend onlayer master

show ev hanako_goodend_close onlayer master:
    xalign 0.0 yalign 0.0
    zoom 1.0 subpixel True
    linear 6.5 zoom 0.8
with whiteout

$ renpy.pause(4.0, hard=True)

play sound sfx_whiteout

scene ev hanako_goodend onlayer master:
    xalign 0.0 yalign 0.0
    zoom 1.0 subpixel True
    parallel:
        easein 12.0 zoom 0.8
    parallel:
        6.0
        "ev hanako_goodend_muffin" with Dissolve(2.0)
with locationchange

$ renpy.pause(12.0, hard=True)

$ renpy.music.set_volume(1.0, 2.0, channel="ambient")
stop music fadeout 4.0

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
