label de_R30:

window hide None

scene bg school_scienceroom onlayer master
with locationchange

window show

play music music_normal fadein 3.0

"Ich schaffe es zwar pünktlich zum Unterricht, aber leider nicht zum Frühstück."


"Der Klassenraum ist in das sanfte Licht der Sonne getaucht."


"Das bedeutet, dass es am Nachmittag unerträglich heiß sein wird. Für den Augenblick ist es jedoch sehr angenehmen."


"Ich sehe, wie Misha und Shizune energisch über etwas diskutieren, wie Hanako aus dem Klassenfenster starrt und wie Mutou vier Minuten zu spät in den Klassenraum stolpert, ohne einen blassen Schimmer zu haben, was er heute unterrichten soll."


"Ich könnte mir nie vorstellen, einfach so die Schule zu schmeißen – auch wenn es nur für ein paar Wochen ist."


"Andererseits scheint Rin kein Problem mit dieser Vorstellung zu haben – oder sie zieht es einfach durch."


"Allerdings wurde ich irgendwie in ihrer irrsinnigen Isolation mitgefangen, auch wenn wir uns letztendlich gegenseitig verletzt haben."


"Haben wir das überhaupt? Vielleicht wurde ja auch nur ich verletzt."


scene bg school_scienceroom_ss onlayer master
with shorttimeskip

"Ich brauche bis zum Nachmittag, bis mir bewusst wird, dass heute Montag ist. Der Kunstklub trifft sich heute."


"Nicht nur das. Wegen der Prüfungen wird es das letzte Treffen vor den Sommerferien sein."




label de_R30x:

"Ich habe keinen wirklichen Grund hinzugehen…"


"Aber ich will mit Herrn Nomiya reden."


scene bg school_hallway3 onlayer master
with locationchange

"Darum lungere ich letztendlich unbeholfen vor dem Kunstraum herum und warte darauf, dass das Treffen zu Ende geht."


no "Das war's für dieses Trimester, meine Lieben!"


"Sein Stimme ist laut genug, um sie durch die Tür hören zu können, und viel zu enthusiastisch, als dass man sie ernst nehmen könnte."


no "Das nächste Treffen ist nach den Sommerferien – am Montag der ersten Woche des nächsten Trimesters."


no "Ich hoffe, euch alle dort wiederzusehen!"


no "Habt schöne Ferien!"


play ambient sfx_crowd_indoors fadein 1.0
stop music fadeout 4.0

show crowd onlayer master
with charaenter

"Es folgt ein verwirrtes Murren als Antwort, dann öffnet sich die Tür zum Klassenraum, und die Schüler strömen heraus."


"Ich warte, bis alle anderen gegangen sind, damit ich mit Nomiya allein reden kann. Es ist fast Zeit fürs Abendessen, daher muss ich nicht allzu lange warten."


stop ambient fadeout 2.0

scene bg school_classroomart_ss onlayer master
with locationchange




label de_R30y:

"Ohne Rin kommt es mir ziemlich sinnlos vor, dorthin zu gehen, aber ich will mit Herrn Nomiya reden."


scene bg school_classroomart_ss onlayer master
with locationskip

"Das Treffen selbst ist nicht erwähnenswert, genau wie meine Fähigkeiten mit Wasserfarben."


"Nomiya versucht, mich zu ermutigen und zu beraten, ohne dabei zu herablassend zu klingen, aber es gelingt ihm nicht wirklich."


"Nicht zuletzt hat mir der Betritt zum Kunstklub beigebracht, dass ich Kunst mag. Aber es wäre nett, wenn ich im Kunstklub wirklich mal etwas Kunst zustande bringen würde."


"Nachdem die Früchte der Arbeit aller in einem ordentlichen Stapel auf dem Lehrertisch gestapelt wurden, räuspert er sich, um eine kleine Rede zu halten."


show nomiya talk onlayer master at center
with charaenter

no "Das war's für dieses Trimester, meine Lieben!"


"Seine Stimme ist viel zu enthusiastisch, als dass man sie ernst nehmen könnte."


show nomiya smile onlayer master
with charachange

no "Das nächste Treffen ist nach den Sommerferien – am Montag der ersten Woche des nächsten Trimesters."


no "Ich hoffe, euch alle dort wiederzusehen!"


show nomiya veryhappy onlayer master
with charachange

no "Habt schöne Ferien!"


hide nomiya onlayer master
with charaexit

stop music fadeout 4.0

"Alle wünschen ihm ebenfalls schöne Ferien, während sie im Gänsemarsch durch die Tür marschieren."


"Ich bleibe zurück und warte, bis wir beide allein sind. Es ist fast Zeit fürs Abendessen, daher muss ich nicht allzu lange warten."



label de_R30z:

"Nomiya sieht die Gemälde durch, von denen einige wirklich ziemlich gut sind."


"Rin mag jeden anderen im Kunstklub übertreffen, aber sie ist nicht die einzige mit Talent."


hi "Entschuldigen Sie, Herr Lehrer…"


play music music_happiness fadein 2.0

show nomiya smile onlayer master at center
with charaenter

no "Hmm? Was ist denn, Nakai?"


"Er hebt fragend seine Augenbrauen und lächelt breit."


hi "Es geht um Rin…"


show nomiya frown onlayer master
with charachange

no "Oh? Stimmt etwas nicht mit Tezuka?"


hi "Nein, aber…"


"Ich bin für den Bruchteil einer Sekunde unsicher, wie ich das formulieren soll. Das gibt Nomiya genug Zeit, um vor sich hinzufaseln."


show nomiya smile onlayer master
with charachange

no "Ich habe sie vor ein paar Tagen gesehen, als ich an Saes Galerie vorbeikam."


no "Sie sagte, sie würde ein oder zwei weitere Gemälde für die Ausstellung fertigkriegen."


show nomiya talk onlayer master
with charachange

no "Ich war wirklich erfreut, sie arbeitet überraschend hart. Ich dachte immer, sie wäre etwas faul und würde immer tun, was sie will, statt sich an die Anweisungen zu halten."


"Er scheint meine Besorgnis wahrzunehmen und bemerkt, dass er abschweift, weswegen er verstummt, bevor er den Gedanken ganz ausgesprochen hat."


show nomiya smile onlayer master
with charachange

no "Ah, aber du wolltest ja über etwas reden. Was gibt's?"


hi "Ich weiß nicht… Sie kommt mir von allem so losgelöst vor, als ob sie an nichts außer der Ausstellung denken kann."


show nomiya frown onlayer master
with charachange

no "Nun, ist das nicht etwas Gutes? Sie konzentriert sich auf ihre Malerei – so wie es sein sollte."


hi "Ja, aber das ist anders. Es ist, als sei sie besessen. Ich war sie besuchen und…"


show nomiya serious onlayer master
with charachange

no "Hast du sie gestört?"


"Er fällt mir ins Wort, bevor ich überhaupt zu Ende reden kann und sieht mich ziemlich verärgert an."


hi "Nein… ich… glaube nicht."


hi "Ich habe nur Bedenken, weil sie komplett aufgehört hat, zur Schule zu kommen. Und sie kommt mir seltsam vor."


hi "Seltsamer als sonst zumindest."


show nomiya stern onlayer master
with charachange

no "Humbug! Das ist für sie viel wichtiger als irgendein lausiger Mathe-, Physik- oder was auch immer für ein Unterricht."


no "Genau deswegen ist diese Schule so flexibel – um jedem Schüler die Chance zu geben, sich selbst zu verwirklichen."


show nomiya serious onlayer master
with charachange

no "Tezuka ist eine Malerin, also sollte sie malen, oder nicht? Und eine Ausstellung haben. Das tun Künstler nun mal. Sie sollte sich darauf konzentrieren dürfen und nicht auf diesen albernen Unterricht. Sie sollte gefördert werden."


no "Wenn man darüber nachdenkt, ist das doch ziemlich offensichtlich."


"Seine Gegenargumente sind nicht sehr überzeugend, aber es fällt mir auch schwer, darauf irgendetwas zu entgegnen."


"Mein widerwilliges Schweigen wird als Zustimmung interpretiert. Nomiya wendet sich wieder dem Stapel der eingereichten Aufgaben auf seinem Tisch zu und durchblättert sie wie ein Kartendeck."


show nomiya smile onlayer master
with charachange

no "Wo wir gerade über Tezukas Ausstellung reden… Ich muss sagen…"


no "… dass ich wirklich gespannt bin, wie sie ankommen wird."


show nomiya dreamy onlayer master
with charachange

no "Sie ist noch so jung und schon solch ein wunderbares Talent! Und der Stil erst!"


"Er spricht ins Leere, um die Stimmung aufzulockern, die etwas angespannt geworden ist."


show nomiya talk onlayer master
with charachange

no "Ich nehme an, dass du auch da sein wirst?"


hi "Ja, ich denke schon."


show nomiya smile onlayer master
with charachange

no "Nun, dann werden wir uns dort wiedersehen."


stop music fadeout 3.0

scene bg school_hallway3 onlayer master
with locationchange

"Ich nehme das als mein Stichwort, dass ich gehen soll. Und das tue ich auch – allerdings bin ich nicht sehr glücklich darüber."


"Meine Botschaft ist – gelinde gesagt – nicht angekommen."


$ suppress_window_after_timeskip = True

scene black onlayer master
with dissolve


label de_R31:

window hide None
nvl clear

scene bg school_scienceroom_bw onlayer master
with locationchange

nvl show dissolve

play music music_night fadein 1.0

n "\n\n\n\n\n\n\n\n\nAm Tag danach muss ich an all die verpassten Gelegenheiten und die Dinge denken, die ich hätte sagen sollen. Mir bleibt nichts übrig außer zu grübeln."


nvl clear
nvl hide dissolve

with shorttimeskip

nvl show dissolve

n "\n\n\n\n\n\n\n\n\nZweiter Tag. Ich beginne, mich unruhig zu fühlen. Ich fange an, meine Zweifel anzuzweifeln, und das fühlt sich bescheuert an, besonders weil ich immer noch an nichts anderes außer Rin denken kann."


nvl clear
nvl hide dissolve

with shorttimeskip

nvl show dissolve

n "\n\n\n\n\n\n\n\n\nDritter Tag. Japanisch- {b}und{/b} Geschichtsprüfung. Klasse. Das, was ich am meisten an ihr hasse, ist, dass sie mich so mies fühlen lassen kann, obwohl ich mich gerade auf ganz andere Dinge konzentrieren sollte."



nvl clear
nvl hide dissolve

with shorttimeskip

nvl show dissolve

n "\n\n\n\n\n\n\n\n\nVierter Tag. Matheprüfung. Wir haben eine Matheprüfung. Sie läuft, wie sie läuft. Mir egal."


nvl clear
nvl hide dissolve

with shorttimeskip

nvl show dissolve

n "\n\n\n\n\n\n\n\n\nFünfter Tag. Nomiya fragt mich erneut, ob ich zur Ausstellungseröffnung kommen werde. Ich kann ihm nicht nein sagen, auch wenn ich das ernsthaft will. Ich will einfach nichts Rin-Bezogenes mit ihm diskutieren, darum ist es besser, den Weg des geringsten Widerstandes zu gehen."


nvl clear
nvl hide dissolve

stop music fadeout 2.0

scene bg school_dormhallway onlayer master
show rin basic_absent onlayer master at center
with shorttimeskip

window show

"Am sechsten Tag – dem Tag vor der Ausstellungseröffnung – sehe ich Rin, wie sie im Flur vor meinem Zimmer steht, als ich nach dem Abendessen ins Wohnheim zurückgehe."


play music music_rain fadein 6.0 

hi "Was tust du hier?"


"Mein Ton ist wütender als ich es beabsichtigt hatte. Ich bin etwas enttäuscht, dass ich mich nicht beherrschen konnte, aber ich kann nichts dafür."


"Rin steht lediglich da, als würde sie einfach zufällig hier herumstehen, ohne wirklich etwas zu tun zu haben. Die Art, wie sie auf alles so cool reagiert, nervt mich."


"Das ist nicht gut. Es waren sechs Tage, und allein sie zu sehen, bringt mich zum Kochen. Sie hat noch nicht einmal etwas gesagt."


show rin basic_deadpan onlayer master
with charachange

rin "Fertig mit Malen."


hi "Solltest du nicht bei der Galerie sein? Vorbereiten?"


show rin basic_awayabsent onlayer master
with charachange

rin "Sie meinten nein."


"Anscheinend kümmert sich die Galeristin um diesen Teil. Die Bilder einrahmen, sie an die Wand hängen und so was."


hi "Und… Warum bist du hier?"


show rin basic_deadpannormal onlayer master
with charachange

rin "Mir war danach."


"Wieder dieses alte, dumme Muster: Ich stelle ihr Fragen, auf die sie mir nichtssagende Antworten gibt, weil es die einzige Art ist, auf die wir uns miteinander unterhalten können."


"Abgesehen von den Momenten, in denen ich ihrem Gebrabbel zuhöre – was man aber nicht wirklich eine Unterhaltung nennen kann."


"Ist das ein Theaterstück? Gibt es ein paar geheime Rollen in die wir uns unwissentlich hineinversetzt haben? Rollen, die die Regeln jeder neuen Begegnung diktieren und unausweichlich dazu führen, dass wir uns gegenseitig verletzen?"


"Ihre lässigen Antworten gepaart mit ihrem noch lässigeren Schulterzucken machen auch mich nicht wirklich schlauer. Ich schätze, ich sollte glücklich darüber sein, dass die Ausstellungsvorbereitungen abgeschlossen sind."


play sound sfx_dooropen

scene bg school_dormhisao onlayer master
with locationchange

"Als ich in mein Zimmer gehe, höre ich, wie ihre Schritte mir folgen."


"Ich habe sie nicht hereingebeten. Ich werde sie nicht bitten zu gehen."


show rin basic_awayabsent onlayer master:
    center
    alpha 0.0
    ease 0.5 ypos 1.15 alpha 1.0
    parallel:
        ease 0.3 center
    parallel:
        "rin basic_absent" with Dissolve(0.3, alpha=True)
with Pause(0.5)

stop music fadeout 6.0

"Sie beansprucht das Bett, ohne um Erlaubnis zu fragen. Ich wünschte, ich hätte mir die Zeit genommen, es zu machen, bevor ich heute Morgen losgegangen bin. Dann steht sie wieder auf, als hätte sie auf heißen Kohlen gesessen."


"Ich lehne mich halb gegen die einzige Ecke meines Schreibtisches, die nicht mit Zeug vollgestellt ist, um meine Beine etwas zu entlasten."


show rin basic_awayabsent onlayer master:
    center
    alpha 1.0
with charachange

"Rin verbringt einige Momente damit, sich neugierig in meinem Zimmer umzuschauen. Dabei wird mir klar, dass sie es noch nie gesehen hat."


"Für einen Moment sieht es so aus, als würde sie sich tatsächlich konzentrieren und versuchen, alles aufzunehmen. Das muss der Blick für Details sein, der sie zu einer Künstlerin macht."


show rin basic_absent onlayer master
with charachange

"Da der Raum klein ist, gehen ihr schnell die Dinge aus, die sie sich ansehen kann, aber dann geschieht nichts mehr, was es der unangenehmen Stille ermöglicht, die Atmosphäre zu vergiften."


"Die Stimmung ist gelinde gesagt kühl. Wir sind beide vorsichtig und warten darauf, dass der andere den ersten Schritt macht."


"Natürlich könnte Rin dieses Spiel ewig spielen. Darum bleibt es an mir hängen."


hi "Also…"


"Ich gebe auf, da sie anscheinend etwas sagen will, es aber wohl nie schaffen würde, eine Unterhaltung anzufangen. Außerdem will ich es hinter mich bringen."


"Warum würde sie sonst herkommen, wenn nicht zum Reden?"


"Ich weiß selbst nicht, was ich sagen soll. Ich will wütend sein, aber ich bringe es nicht übers Herz, sie anzuschreien."


"Meine Stimme erregt ihre Aufmerksamkeit. Sie scheint genauso nach Worten zu suchen, aber anscheinend ist sie sich auch nicht ganz sicher, warum sie eigentlich hier ist."


show rin basic_absent_close onlayer master:
    center
    ypos 1.05
    easein 0.5 ypos 1.0
with characlose

"Und so macht Rin lediglich ein paar Schritte, um die Entfernung zwischen uns zu schließen, stellt sich auf ihre Zehenspitzen, um den Höhenunterschied auszugleichen und…"


window hide

show rin basic_lucid_superclose onlayer master at center
with charachange

centered "„Es war eine schlechte Idee.”"


centered "„Vielleicht sollten wir das vergessen.”"


window show

"Reflexartig schießen mir die Worte „nein,” „ja” und „vielleicht” gleichzeitig durch den Kopf."


"Meine Hand ist zwischen ihren und meinen Lippen, eine Wand, die ich als Schutz gegen… etwas errichtet habe."


"Ihr warmer Atem streift meine Finger. Der Duft ihrer Haut liegt in der Luft und dieses mysteriöse, unbeschreibliche Gefühl, das mich einfängt und mich tief in ihre Augen zieht."


show rin basic_surprised_close onlayer master
with charachange

play music music_moonlight fadein 0.5

"Der Blick in ihren Augen ist überrascht und fragend, warum denn diese unverschämte Hand ihren Vorstoß verhindert hat."


"In ihren großen Augen funkelt Feuchtigkeit. Mit einem sanften und doch starren Blick, dem ich kaum standhalten kann, schauen sie in meine."


"Rins halb offener Mund lässt sie noch verwirrter aussehen, auch wenn ihre sich wölbenden Lippen etwas vollkommen anderes vermitteln."


show rin basic_upset_close onlayer master
with charachange

rin "Bitte."


show rin negative_angry_close onlayer master
with charachange

rin "Ich brauche dich."


"Die Worte entspringen ihrem Hals als ein raues Flüstern, das nur für mich bestimmt ist, und an ihrer Zunge und ihren Zähnen vorbeigeht, ohne ihnen eine Möglichkeit zu geben, es daran zu hindern."


show rin negative_angry onlayer master
with Dissolve(0.15)
with vpunch

"Sie ernüchtern mich augenblicklich. Ich zucke ungeschickt zurück, um wieder etwas Distanz zwischen uns beide zu bringen und stoße mich dabei schmerzhaft an meinem Schreibtisch."


"Vielleicht ist es ihre Wortwahl, vielleicht ist es ihre Ausdrucksweise, aber etwas daran schreckt mich ab."


"Etwas stimmt nicht, irgendetwas stimmt mal wieder ganz und gar nicht."


hi "Wozu brauchst du mich?"


"All die unangenehmen Gefühle kommen wieder zum Vorschein, und ich spüre, wie mein Herzschlag plötzlich aufs Zehnfache ansteigt."


show rin basic_absent onlayer master
with charachange

"Rins Augen verlieren kurz ihren Fokus und erlangen ihn dann wieder, als ihr angespannter Körper sich entspannt und sie sich wieder aufrichtet."


show rin basic_deadpanupset onlayer master
with charachange

rin "Ich glaube nicht, dass ich über irgendetwas nachgedacht habe. Warum zeichnest du Muster in den Staub auf deinem Nachttisch?"


show rin basic_awayabsent onlayer master
with charachange

rin "Dafür gibt es ein Wort, aber es fällt mir nicht ein…"


"Ihre Bemerkung wirft mich fast aus der Bahn. Ich blicke über ihre Schulter auf den kleinen Tisch neben meinem Bett, aber aus dieser Entfernung kann ich nichts erkennen."


"Also braucht sie mich für nichts Bestimmtes?"


"Mal eben vorbeigekommen, weil sie dachte, ich würde mich freuen, sie zu sehen? Nachdem sie mich eine Woche lang ausgesperrt hat, ohne irgendeiner Beschwerde Gehör zu schenken?"


"Vollkommen altruistische Motive?"


"Ihr war danach?"


hi "Schwachsinn. Ich kann es selbst beantworten."


hi "Um Gedankenspielchen zu spielen, wann immer du willst; um mich zu küssen, wann immer du willst; um mich zu ignorieren, wann immer du willst; um deine Launen auszuleben, wann immer du willst?"



hi "Ist es das? Brauchst du mich dafür?"


"Sogar in meinen Ohren klingt meine Stimme sehr wütend."


extend " Gut."


show rin basic_absent onlayer master
with charachange

"Rin erfasst auch endlich die Stimmung, und ihr neugieriger Gesichtsausdruck verzieht sich zu einem eher untypischen."


show rin negative_sad onlayer master
with charachange

rin "Nein…"


"Dabei belässt sie es. Ihre Augen wandern rastlos umher und durchsuchen den Raum, als würden die Worte, die sie zu finden versucht, auf meinen Wänden geschrieben stehen."


hi "Was dann?"


show rin negative_confused onlayer master
with charachange

stop music fadeout 2.0

rin "Ich musste malen, darum…"


"Malen."


"Natürlich. Das tun Künstler nun mal."


"Die Worte hallen in meinem Geist wider und bringen mein Blut zum Kochen."


play music music_tragic fadein 2.0

hi "Komm mir nicht damit, Rin! Ich bin keine deiner verdammten Musen, die man für die Malerei durch den Dreck ziehen kann!"


hi "Ich bin nicht irgendein Mittel, mit dem du erreichen kannst, was auch immer die anstrebst! Ich bin ich!"


hi "Was also, wenn ich überhaupt nichts über meine eigene Zukunft weiß?"


hi "Es gibt Dinge, die ich will, und Dinge, die mir wichtig sind! Sogar ich kann von etwas anderem träumen als Alpträumen!"


"Ich brülle, doch ich habe mich bereits viel zu sehr hineingesteigert, als dass ich mir über solche Dinge noch Gedanken machen würde."


show rin negative_sad onlayer master
with charachange

"Rin schaut auf ihre Zehen und wackelt etwas melancholisch mit ihnen, während sie meinen Ausbruch auf sich wirken lässt, ohne etwas zu ihrer Verteidigung zu sagen."


"Erst nachdem ich fertig bin, versucht sie irgendwie zu antworten."


show rin basic_sad onlayer master
with charachange

rin "Ich kann nichts anderes tun. Oder besser, ich kann alles Mögliche tun, aber ich… kann nicht… tun."


show rin basic_upset onlayer master
with charachange

rin "Es ist das einzige, was ich mehr oder weniger richtig kann. Meistens."


"Ich verstehe vollkommen. Kunst steht an erster Stelle. Alles andere kommt an zweiter – oder an tausendster Stelle."


hi "Was ist mit mir? Bin ich nichts? Hat es mich für eine kurze Weile ein bisschen interessant gemacht, als ich mich für Kunst interessiert habe?"


hi "Sag's mir. Ich will's wirklich wissen. Hast du je über meine Perspektive nachgedacht, oder geht es immer nur um dich?"


"Wie Galle steigen die Worte meinen Hals empor."


show rin basic_surprised onlayer master
with charachange

"Rin sieht beunruhigt aus. Und komplett verwirrt, als ob sie einfach nicht verstehen kann, weswegen ich mich so aufrege."


"Ich kann nicht fassen, dass sie so dumm sein kann."


show rin negative_sad onlayer master
with charachange

rin "Ich wollte nicht…"


"Diesmal unterbricht Rin sich selbst."


show rin basic_upset onlayer master
with charachange

rin "Verstehst du nicht? Ich kann nicht."


hi "Was kannst du nicht?"


hi "Du erklärst nie etwas! Wie soll ich irgendwas verstehen, wenn du nie etwas sagst?"


hi "Warum redest du nie?"


hi "Sag was!"


"Doch sie tut es nicht."


"Meinen Zorn an ihr auszulassen befriedigt mich. Es fühlt sich schrecklich an, davon befriedigt zu werden, aber ich kann mich nicht zügeln."


show rin negative_annoyed onlayer master
with charachange

"Da sie meinem Zorn nicht frontal entgegenstehen will, dreht Rin sich um, um unerschütterlich aus meinem Fenster zu sehen, obwohl es dort nichts zu sehen gibt."


"Mein schlimmster Zorn ist verraucht. Ich halte den Mund, da ich keine Lust habe, ihren Hinterkopf anzubrüllen. Somit kehrt endlich wieder Stille ein."


"Ich versuche durch meine andrenalinverzerrte Sicht ein paar Hinweise auf ihre Reaktion auszumachen."


"Meine Reaktion war sicher nicht die Beste, aber ich hoffe, dass Rin nun begriffen hat, dass sie nicht einfach alles andere ignorieren kann, wann immer ihr danach ist."


"Es würde mich krank machen, wenn sie es nicht begriffen hätte. Sie hört niemals zu; sie ist so unbeeinflusst von der Welt um sich herum."


"Nicht dieses Mal, wie es scheint."


"Ihr Körper zittert, als würde sie Tränen zurückhalten, aber ich weiß bereits, dass Rin nicht weint."


"Ihre Gleichgültigkeit hat mich so zornig gemacht. Jetzt, da sie vorüber ist, weiß ich nicht mehr weiter. Ich frage mich…"


"Bin ich zu weit gegangen?"


hi "Schau, ich-"


show rin negative_angry onlayer master
with charachange

rin "Geh weg."


rin "Geh weg, Hisao."


"Ihre Stimme ist kaum hörbar und müde, als sie das sagt, aber die Worte waren für mich unmissverständlich."


"…"


"Was gibt es noch zu sagen?"


hi "Das ist mein Zimmer."


"Die schroffe, leere Bemerkung ist ein passendes Ende für diese unangenehme Diskussion, die zu einer noch Unangenehmeren wurde – ein einseitiger Brüllwettbewerb."


show rin basic_lucid onlayer master
with charachange

"Nachdem sie sich einen Moment gesammelt hat, gibt Rin einfach auf. Ich erkenne es daran, wie sie ihre Schultern hängen lässt und hinausgeht."


hide rin onlayer master
with charaexit

"Obwohl sie absichtlich in die andere Richtung schaut, kann ich sehen, wie sie sich so fest auf die Lippe beißt, dass es anfangen könnte zu bluten, wenn sie nicht aufhört."


"Als sie das Zimmer verlässt, bemerke ich, dass sie die Tür offen gelassen hat, als sie hereinkam. Mein Gebrüll muss durch das ganze Wohnheim geschallt haben."


"Ich seufze. Jetzt, wo sie weg ist, bin ich allein mit meiner Schuld."


"Während das Pochen in meiner Brust langsam nachlässt, nimmt Beklemmung seinen Platz ein."


"Irgendwie kommt es mir vor, als wäre nichts von dem passiert, wenn ich nicht gewesen wäre."


"Ganz gleich wie aufreibend, unausstehlich und unverschämt Rin ist – sie ist nicht die Rin, die ich zu kennen glaubte."


"Die Rin, die ich erwartet hatte."


"…"


"War ich es, der all das angerichtet hat, indem er Rin überredet hat, ihre Chancen mit der Ausstellung wahrzunehmen?"


"Bin ich direkt dafür Verantwortlich, dass Rin sich in den letzten Wochen so verändert hat?"


"Mir fällt keine andere Erklärung für ihr seltsames Verhalten ein als die Ausstellung und all die Dinge, die damit einhergehen."


"Vielleicht war es der einzige Weg, der uns hätte näher zusammenbringen können. Aber am Ende hat es uns nur weiter auseinander gebracht, und jetzt sind wir außerhalb der Reichweite des jeweils anderen."


play sound sfx_impact2
with vpunch

"Ich schlage meinen Kopf hart gegen die Wand."


play sound sfx_impact2
with vpunch

stop music fadeout 4.0

"Zweimal, damit es auch garantiert wehtut."


scene black onlayer master
with dissolve



label de_R32:

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 0.5

scene bg gallery_ext onlayer master
with locationchange

"Ein Kopfschmerz pocht erbarmungslos in meinem Hinterkopf, als ich die Tür zum 22nd corner öffne."


"Abgesehen davon bin ich vollkommen gelassen."


$ renpy.music.set_volume(0.1, 1.0, channel="ambient")

window hide
nvl clear
nvl show dissolve

n "\n\nNachdem ich an Rin all meinen Ärger ausgelassen habe, den ich in meinem Inneren angestaut hatte, fühlte ich mich, als hätte man eine ungeheure Last von meinem Herzen genommen."


n "Die Anspannung, die in den letzten paar Wochen meinen Verstand eingenommen hatte, ließ nach, ohne auch nur eine Spur zurückzulassen."


n "In diesem fast schon zengleichen Zustand der Erleuchtung begriff ich, dass es vielleicht eine schlechte Idee war, sie so anzubrüllen."


n "\nIch meinte es wirklich so, aber was bringt es, so zu explodieren? Gar nichts."


n "So bin ich nicht. Ich brülle keine Menschen an. Ich weiß nicht, warum ich es gestern getan habe."


n "Daher fühle ich mich weiterhin schuldig dafür und will meine Worte zurücknehmen."


n "\n\nRin ist wahrscheinlich ebenfalls aufgebracht. Mehr noch als mein Verhalten hat mich ihre Reaktion schockiert."


nvl clear

n "\nIch hielt sie immer für beständig, losgelöst von ihrem Umfeld. Deswegen kam es mir so… unpassend vor, dass mein Gebrüll sie so durcheinanderbringt."


n "\nOb sie versteht, wie ich mich fühle?"


n "In Rins Welt scheint alles so absolut und subjektiv zu sein… absolut subjektiv, als ob sie vollkommen unfähig wäre, Dinge aus einer anderen Perspektive zu sehen als aus ihrer eigenen."


n "Doch ist letztendlich irgendjemand dazu in der Lage? Vielleicht sind Objektivität und Altruismus bloße Illusionen für Menschen, die sich selbst gern für mitfühlend halten wollen."


n "Genau wie Kunst eine Illusion für Menschen ist, die glauben, dass Realität lediglich ein Schleier für etwas Größeres ist."


n "Selbst wenn man aufhört zu denken, dass sich die Welt um einen dreht oder man anfängt, über seinen Horizont zu schauen, sieht man nur einen anderen, weiteren Horizont, der einem neue Schranken aufweist."


n "\nVielleicht macht sie das im Endeffekt zu einer von uns."


stop ambient fadeout 1.0

nvl clear
nvl hide dissolve

play sound sfx_storebell
$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 0.5

scene bg gallery_int onlayer master
show crowd onlayer master
with locationchange

window show

play music music_ease fadein 3.0

"Ich schreite durch die Tür und finde die Galerie gefüllt mit Leuten voller Illusionen."


"Trotz Saes Bemerkungen während meiner vorigen Besuche dachte ich immer, dass sie sehr geräumig wäre, aber mit so vielen Leuten sieht sie ohne jeden Zweifel überfüllt aus."


show sae smile behind crowd at center onlayer master
with charaenter

"Umgehend bemerke ich Sae, die gerade lebhaft mit einigen älteren Herren diskutiert."


"Eigentlich ist sie ziemlich groß und sieht irgendwie cool aus, darum sticht aus der Masse heraus."


"Es stehen ein paar dutzend Weingläser auf den Tischen entlang der Rückwand, allesamt gefüllt mit burgunderroter Flüssigkeit. Die meisten Gäste nippen bereits an Gläsern."


"Die Prominenten und Kunstkenner vermischen sich freudig und tauschen gnädige Meinungen über Rins Kunst aus, die für die Meisten nur von zweitrangigem Interesse zu sein scheint."


"Ich fühle mich distanziert, ausgeschlossen von den anderen Leuten hier."


"Ich kann nicht von mir behaupten, auch nur ansatzweise ein Sozialchamäleon zu sein, daher ist diese Situation ziemlich nervenaufreibend."


"Da ich mich überhaupt nicht in die Masse einfüge, tue ich einfach so als ob und versuche, so cool und lässig auszusehen, wie ich kann."


"Wie Rin mit all dem wohl umgeht? Wenn ich sie wäre, stünde ich wohl kurz vor einer Panikattacke."


$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg gallery_exhibition onlayer master
show crowd onlayer master
with locationchange

"Während ich meine Nervosität verdränge, versuche ich vorsichtig durch die Masse zu navigieren und werfe dabei verstohlene Blicke auf die gerahmten Bilder an der Wand."


$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

scene rin_exhibition_paintings onlayer master
with locationchange

"Rins Ausstellung nimmt etwa die Hälfte der Wandfläche der Galerie ein. Manche Gemälde kommen mir weniger bekannt vor als andere, doch die meisten erkenne ich."


"Schließlich habe ich bei manchen selbst gesehen, wie sie sie gemalt hat, oder ich erinnere mich, wie Rin sie für ihr Portfolio ausgewählt hat."


"Ich merke, dass auch ein paar der unfertigen Gemälde an der Wand hängen. Vielleicht ist das es, was sie Zufallskunst nennen?"


"Sogar Rins Fehlschläge – wenn man sie so nennen kann – wurden Ausstellungsstücke ihrer Fähigkeiten. Ziemlich paradox."


$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg gallery_exhibition onlayer master
show crowd onlayer master
with locationchange

"Sie selbst ist nirgendwo zu sehen – was seltsam ist, da die Galerie trotz der Menschenmenge ziemlich klein ist."


"Irgendwie ist mir das recht. Ich weiß nicht, wie ich ihr nach gestern gegenübertreten soll. Vielleicht hätte ich nicht einmal kommen sollen."


"Aber ich habe es mehreren Leuten versprochen, Rin eingeschlossen, daher…"


"Verdammt. Es klingt, als würde ich das alles tun, weil mich eine Art instinktiver Korrektheit dazu zwingt, und nicht weil es vernünftig wäre (oder eben nicht)."


scene bg gallery_int onlayer master at right
show sae smile onlayer master at center
show crowd onlayer master at right
with locationchange

"Ich schleiche mich an Sae heran und warte auf eine Ruhepause in der Unterhaltung, damit ich sie auch ansprechen kann."


"Obwohl ihre Stimme fast vollständig vom allgemeinen Hintergrundlärm übertönt wird, höre ich Teile davon, wie sie über Rin spricht."


sa "Ja, sie ist Oberschülerin an einer örtlichen Schule… auch wenn sie nächstes Jahr ihren Abschluss macht, bin ich mir sicher, dass mehrere Kunstschulen daran interessiert wären…"


sa "… ich dachte, es wäre interessant, eine Ausstellung von jemanden zu haben, der noch in einer frühen Phase seiner Entwicklung ist…"


"Es ist so seltsam. Es ist, als wäre Rin eine Art Miniberühmtheit, obwohl dies nichts weiter ist als eine kleine Ausstellungseröffnung in einer kleinen Kunstgalerie in einer kleinen Stadt."


sa "Tatsächlich ist ein Freund von mir aus…"


play sound sfx_impact
with vpunch

mystery "Hisao!"


"Meine Abhöraktion wird von einer vertrauten Stimme und einem vertrauten Schlag auf den Rücken unterbrochen. Ich muss mir über die Quelle nicht lange den Kopf zerbrechen; umdrehen muss ich mich genauso wenig."


hi "Hi Emi."


$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

show emicas invis onlayer master:
    center
    xpos 0.15
with None

show bg gallery_int onlayer master at left
show sae invis onlayer master:
    xpos 0.75
show crowd onlayer master at left
show emicas happy onlayer master at center
with dissolvecharamove

hide sae onlayer master
with None

emi "Hi! Bist du so was wie ein Vertreter des Kunstklubs oder so? Ich sehe hier sonst niemanden aus der Schule…"


hi "Ähm… ehrlich gesagt weiß ich es nicht. In dem Fall bin ich das wohl."


hi "Was ist mit dir?"


show emicas neutral onlayer master
with charachange

emi "Mir mir?"


hi "Ääähhh… "


show emicas angry_up onlayer master
with charachange

emi "Du dachtest, ich interessiere mich nicht für Kunst? Ist es das, Hisao?"


hi "Nein, das meinte ich ni… Na ja, wenn du es so sagst, vielleicht ein bisschen."


hi "Ich meine, obwohl du oft mit Rin zusammen bist, habe ich dich noch nie mit ihr über Kunst reden hören, daher…"


show emicas awayfrown_up onlayer master
with charachange

"Emi wird wütend und schaut sich mit einem unzufriedenen Blick um."


show emicas closedsmile onlayer master
with charachange

emi "Stimmt, ich hab null Ahnung davon. Aber sie kam zu meinem Leichtathletikturnier, darum dachte ich, dass es nur fair wäre auch zu erscheinen."


show emicas wink_close onlayer master
with characlose

"Sie lehnt sich nach vorne und versucht geheimnisvoll auszusehen, bringt aber nur verschwörerisch zustande."


emi "{b}Verstehst{/b} du Kunst?"


hi "Nein. Nein, tu ich nicht."


hi "Überhaupt nicht."


show emicas closedsmile_close onlayer master
with charachange

"Mein betonendes Kopfschütteln entlockt ihr ein Kichern und ebenfalls ein fröhliches Kopfschütteln."


show emicas happy_close onlayer master
with charachange

emi "Ich auch nicht!"


show emicas wink_close onlayer master
with charachange

emi "Hey, lass uns mit Rin reden gehen! Ich wette, du hast sie noch nicht gesehen – ich nämlich auch nicht."


show emicas happy_up_close onlayer master
with charachange

emi "Komm schon!"


show nomiya invis behind emicas onlayer master:
    center
    xpos 0.8
show rin invis onlayer master:
    center
    xpos 1.1
with None


show bg gallery_int onlayer master at center
show crowd onlayer master at center
show emicas neutral_close onlayer master:
    xpos 0.15
show nomiya smile onlayer master:
    xpos 0.55
show rin basic_awayabsent onlayer master:
    xpos 0.85
with dissolvecharamove

"Bevor sie eine Chance hat, mich gewaltsam zu Rin zu zerren, erscheint hinter ihr Nomiya mit Rin im Schlepptau."


"Sie ist in keinster Weise für diesen Anlass gekleidet. Stattdessen trägt sie ihre übliche Schuluniform, und ihre Haare sind ungekämmt."


"Vielleicht passt ihr natürliches Aussehen einfach am besten zu ihr."


show emicas happy_close onlayer master
with charachange

emi "Hallo, Herr Nomiya! Hi Rin!"


"Unbeeindruckt begrüßt Emi ihn fröhlich. Er dreht sich um und schaut verwirrt nach unten."


show nomiya frown onlayer master
with charachange

no "Wer bist du denn?"


show emicas frown_up_close onlayer master
with charachange

emi "Ich bin Emi, von der Schule, Klasse 3-4. Erinnern Sie sich nicht?"


"Sie sieht absolut schockiert darüber aus, dass es jemanden geben könnte, der sie nicht kennt."


show nomiya talk onlayer master
with charachange

no "Oh, entschuldige. Du bist in der gleichen Klasse wie Tezuka, richtig?"


show emicas wink_close onlayer master
with charachange

emi "Jepp!"


show nomiya smile onlayer master
with charachange

no "Du musst mir verzeihen, ich habe Probleme damit, mir die Schüler zu merken, die nicht Kunst wählen."


show emicas closedsmile_up_close onlayer master
with charachange

emi "Kein Problem, kein Problem!"


show emicas happy_close onlayer master
with charachange

emi "Hi Rin!"


show rin basic_deadpan onlayer master
with charachange

rin "Hallo."


show emicas happy_up_close onlayer master
with charachange

emi "Gratuliere zu deinem supercoolen Kunst-Dingsda! Ich bin sicher, dass du ein großer Hit wirst!"


"Sie wirft ihre Arme zur Betonung ungestüm in die Luft, wobei sich mich fast im Gesicht trifft."


show emicas wink_up_close onlayer master
with charachange

emi "Und schau, Hisao ist auch gekommen!"


show rin relaxed_nonchalant onlayer master
with charachange

"Weder sieht mich Rin an noch begrüßt sich mich."


hi "Gratuliere, Rin."


"Sie hält ihren Blick abgewandt und blickt demonstrativ auf ihre Sandalen."


show emicas closedsmile_close onlayer master
with charachange

"Während sie die Spannung zwischen uns nicht wahrnimmt und nichts vom gestrigen Vorfall weiß, quasselt Emi weiter über dies und das mit einer teilnahmslosen Rin."


"Vermutlich ist sie es gewohnt, hin und wieder nicht viel aus ihr herauszukriegen."


stop music fadeout 5.0
$ renpy.music.set_volume(1.0, 3.0, channel="ambient")



show sae invis behind rin onlayer master:
    center
    xpos 1.25
with None

show bg gallery_int onlayer master at right
show crowd onlayer master at right
show emicas invis onlayer master:
    xpos -0.35
show nomiya smile onlayer master:
    xpos 0.25
show rin relaxed_nonchalant onlayer master:
    xpos 0.55
show sae neutral onlayer master:
    xpos 0.8
with dissolvecharamove

hide emicas onlayer master
with None

"Bald darauf wenden sich Nomiya und Sae Rin zu und stellen sie vor."


"Wie schon erwartet fällt mir der Moment der Verwirrung auf, als die Gäste ihre Arme sehen."


show sae smile onlayer master
with charachange

"Sae ist glücklicherweise auf Zack und erzählt kurz von unserer Schule."


"Zweifelnde Gesichter werden rasch zu neugierigen."


"Mann" "Würden Sie uns vielleicht etwas über Ihre Kunst erzählen?"


"Mann" "Ich hielt die Entwicklung für durchaus leicht zu bemerken. Was denken Sie selbst über die Unterschiede zwischen Ihren älteren und den aktuelleren Werken?"


"Mann" "Es ist ziemlich selten für jemanden, der noch so jung ist, sich an Abstraktion zu versuchen."


"Frau" "Es wäre interessant gewesen zu sehen, wie Sie arbeiten!"


"Mann" "Oh, definitiv! Ich nehme an, Sie benutzen ihre Füße? Es muss sehr schwierig gewesen sein, das zu lernen. Sie sollten stolz sein."


show rin basic_surprised onlayer master
with charachange

rin "Ich… ähmmm…"


play music music_rain fadein 8.0

"Mann" "Werden Sie nach der Schule eine Karriere als Künstlerin verfolgen?"


"Sie wird mit so vielen Fragen bombardiert, dass sie nicht einmal darauf hoffen kann, alle zu beantworten."


"Vielleicht ist es auch am besten so. Rin tendiert dazu, recht häufig Unsinn von sich zu geben."


"Mann" "Wo haben Sie denn ihre Ideen her?"


show rin relaxed_boredom onlayer master
with charachange

rin "Das ist die viert… Ich meine, fünftschlechteste…"


"Rin strauchelt weiter mit ihren Worten und sieht aufgrund der vielen erwartungsvollen Fragen zunehmend irritiert aus."


show rin negative_annoyed onlayer master
with charachange

rin "Ah…"


"Alle warten darauf, dass sie etwas sagt, aber sie sieht aus, als hätte sie die Sprache verloren."


"Jede weitere Frage trägt nur zu ihrer Bedrängnis bei."


show rin basic_sad onlayer master
with charachange

"Ich komme nicht dazu, die Frage zu hören, die sprichwörtlich eine zu viel ist."


"Es ist wie ein abgewürgter Motor."


show rin basic_sad onlayer master:
    1.2
    parallel:
        easeout 0.5 ypos 1.2
    parallel:
        "rin basic_lucid" with Dissolve(0.3, alpha=True)
with Pause(1.5)

stop ambient fadeout 7.0

scene ev rin_gallery onlayer master:
    truecenter
    zoom 0.9 subpixel True
    easein 30.0 zoom 1.0
with Dissolve(0.2)
play sound sfx_pillow
with vpunch

"Rin erstarrt nur für eine lange, lange Sekunde, bevor sie auf ihre Knie fällt und dabei den Boden plump wie ein Sack voller Kartoffeln trifft."


"Frau" "Sind Sie in Ordnung?"


rin "Ich weiß es nicht…"


no "Tezuka? Was ist los, Mädchen?"


rin "Ich weiß nicht, was los ist…"


"Eine schreckliche Stille legt sich über die um Rin versammelte Menge."


"Jeder ist gelähmt. Niemand weiß, wie er auf ihren plötzlichen… Anfall, oder so, reagieren soll."


"Sie atmet mit einem tiefen, zitternden Keuchen, als würde ihr die Luft ausgehen, und starrt mit leeren Augen geradeaus."


play sound sfx_rustling
stop music fadeout 1.0

scene bg gallery_int onlayer master at right
show crowd onlayer master at right
show nomiya serious onlayer master:
    center
    xpos 0.25
show rin negative_sad_close onlayer master:
    center
    xpos 0.55 ypos 1.2
    ease 0.8 ypos 1.0
show sae scowl onlayer master:
    center
    xpos 0.8
with locationchange

"Als ich sehe, dass niemand etwas unternimmt, zwinge ich mich dazu, zu Rin zu gehen und sie vom Boden aufzuheben. Ich muss sie stützen, damit sie stehen bleibt."


hi "Willst du etwas frische Luft schnappen gehen? Okay, lass uns ein bisschen nach draußen gehen."


"Auf ihre Antwort warte ich nicht einmal, bevor ich sie an den Schultern packe und sie an dem verblüfft aussehenden Nomiya, an Sae, Emi und den anderen Gästen vorbei ziehe."


hi "Entschuldigt uns."


play sound sfx_storebell
$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 1.0

scene bg gallery_ext onlayer master
with locationchange

"An der Tür trifft die kühle Abendbrise mein Gesicht."


show rin negative_sad_close_ni onlayer master at center
with charaenter

"Ich lasse Rin los, woraufhin sie sich gegen eine Steinwand lehnt und versucht, zu Atem zu kommen."


hi "Bist du in Ordnung?"


show rin negative_confused_close_ni onlayer master
with charachange

rin "Ich konnte nichts sagen…"


"Rin sieht mich noch immer nicht an. Ich sehe ebenfalls weg."


play music music_dreamy fadein 4.0

"Die Straßenlichter und die bunten Neonschilder lassen mich beinahe erblinden und zwingen mich, wieder zurückzusehen."


"Immerhin spricht sie – auch wenn sie ihre Worte nicht an mich richtet."


hi "Was wolltest du denn sagen?"


"Vielleicht können wir uns beide Vorstellen, dass wir zu einem unsichtbaren Freund sprechen."


show rin basic_sad_close_ni onlayer master
with charachange

rin "Ich weiß nicht."


show rin negative_sad_close_ni onlayer master
with charachange

rin "Etwas, das etwas bedeutet hätte."


"…"


"Die Stille hält für eine lange Zeit an."


"Mir ist unwohl dabei, allein mit Rin zu sein. Ich bin nicht gut darin, mir Dinge vorzustellen, die ich nicht existieren, oder eben Dinge auszublenden, die es tun."


hi "Wir sollten wieder reingehen."


hi "Die Gäste, die Sae eingeladen hat, sind dort drin. Sie wollen dich bestimmt treffen und sich mit dir unterhalten."


hi "Du weißt schon, Fragen stellen und so. Über die Gemälde, für die du so hart gearbeitet hast."


show rin negative_angry_close_ni onlayer master
with charachange

rin "Ich will nicht, dass sie mir solche Fragen stellen. Ich kann nie die richtigen Dinge sagen."


hi "Was willst du dann?"


"…"


show rin relaxed_doubt_close_ni onlayer master
with charachange


label de_choiceR32:
menu:
    with menueffect
    rin "Dass man mir keine Fragen stellen müsste."
    "Freust du dich nicht über das Interesse an deinen Gemälden?":





        return m1
    "Aber falls du so jemanden finden würdest, was dann?":


        return m2

label de_R32a:

$ renpy.music.set_volume(0.2, 0.2, channel="ambient")

hi "Aber freust du dich nicht darüber, dass sich Leute für deine Gemälde interessieren?"


hi "Ich meine, hast du nicht deswegen die Ausstellung und all das durchgezogen?"


hi "Natürlich wollen sie dir Fragen stellen, wenn sie es interessant finden."


show rin negative_annoyed_close_ni onlayer master
with charachange

rin "Es ist, als würde man zweimal hintereinander einen Sonnenaufgang haben, wenn man eigentlich nackt im Mondlicht baden will."


show rin negative_angry_close_ni onlayer master
with charachange

rin "Schön, aber…"


"… es reicht nicht. Ich beende den Satz in Gedanken für sie, obwohl ich ihre unpassende Metapher nicht verstehe."


hi "Ich versteh's nicht."


hi "Du solltest versuchen, glücklicher zu sein. Schließlich ist das dein großer Abend."


hi "All diese Menschen sind hier, um deine Gemälde zu sehen. Ich finde, das ist fantastisch."


"Ich warte darauf, dass sie etwas sagt – entweder dafür oder dagegen. Doch Rin grübelt weiter."


"Sie will keine Fragen beantworten, oder mir erklären, was los ist."


"Falls sie etwas zu sagen hatte, bleiben die Worte unausgesprochen."


"Die Worte, die sie nicht sagen kann."


"Ich schaudere im frostigen Wind, der durch die Straßen weht. Sein Heulen füllt die Stille."


hi "Wir sollten wieder reingehen."


hi "Du hast allen Sorgen gemacht."


stop ambient fadeout 0.5
play sound sfx_storebell

scene bg gallery_int onlayer master
show crowd onlayer master
show nomiya talk onlayer master at twoleft
show sae neutral onlayer master at tworight
with locationchange

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0

no "Ah, da bist du ja! Fühlst du dich besser? Hier drin kann es ziemlich heiß werden, da kann so ein überraschender Schwindelanfall schon mal vorkommen."


show nomiya veryhappy onlayer master
with charachange

"Er lacht ungestüm, beinahe widerwärtig."


show nomiya talk onlayer master
with charachange

no "Du solltest etwas trinken, wenn du dich schwach fühlst, Tezuka."


show nomiya talk onlayer master:
    center
    xpos 0.25
show sae neutral onlayer master:
    center
    xpos 0.8
with charamove

show rin basic_lucid onlayer master:
    center
    xpos 0.55
with charaenter

"Rin nickt schwach, aber anscheinend reicht das, um Nomiya davon zu überzeugen, dass es ihr gut geht."


"Er schiebt sie etwas nach vorne, um sie der Person vorzustellen, mit der er sich gerade unterhalten hat."


show nomiya smile onlayer master
with charachange

no "Also, wo waren wir stehengeblieben…"


"Mann" "Ah ja, ich bin sehr erfreut…"


stop music fadeout 8.0

"Ich werde aus der Unterhaltung ausgeschlossen, und der Hintergrundlärm Dutzender anderer Unterhaltungen füllt meine Ohren mit einem undeutlichen Rauschen."


"Sogar Emi ist irgendwohin verschwunden."


"Inmitten einer Menschenmenge zu stehen, ist ein überraschend einsames Gefühl."


"Nicht nur Rin, sondern alle anderen hier scheinen Teil von etwas zu sein, zu dem ich nicht dazugehöre."


"Ich freue mich für sie, wirklich, aber es erweckt in mir das Gefühl, als hätte ich noch gar nichts erreicht."


"Rin ist der lebende Beweis für das Potential eines menschlichen Wesen. Sie hat ihre Behinderung überwunden und sie sogar zu einer Stärke gemacht."


stop ambient fadeout 4.0

"Sie sollte glücklich darüber sein."


"Was ist mein Potenzial?"


"Rin hat es so weit gebracht, aber zu was kann ich es bringen?"


scene black onlayer master
with dissolve


label de_R32b:

$ renpy.music.set_volume(0.2, 0.2, channel="ambient")

hi "Aber falls du so jemanden finden würdest, was dann?"


hi "Denkst du wirklich, dass das so eine Art ein-für-alle-mal Ende wäre? Liebende, die unter einem schlechten Stern starten, und dann glücklich bis ans Ende ihrer Tage leben?"


show rin basic_absent_close_ni onlayer master
with charachange

"Sie reagiert auf meine Frage nur mit einem leeren Blick aus ihren dunklen Augen. Auf meine kaum verhüllte Verbitterung scheint sie nicht zu reagieren."


show rin negative_worried_close_ni onlayer master
with charachange

rin "Nein, das denke ich nicht."


show rin negative_annoyed_close_ni onlayer master
with charachange

rin "Aber wenigstens müsste ich dann nicht allein sein."


"Sie flüstert diese Worte zu den Lichtern der Stadt, doch ich kann sie trotzdem hören."


show rin negative_sad_close_ni onlayer master
with charachange

rin "Ich hätte das nicht tun sollen. Noch nicht."


hi "Die Ausstellung?"


show rin basic_lucid_close_ni onlayer master
with charachange

"Sie nickt und schließt ihre Augen, atmet dabei ruhig aus, als ob sie beweisen müsste, dass sie es kann. Dann spricht sie weiter zu sich selbst."


hi "Warum? Falsche Konstellation der Planeten?"


show rin basic_sad_close_ni onlayer master
with charachange

rin "Nein, das nicht. Ich hab's nachkontrolliert – ich bin heute morgen mit dem rechten, ich meine linken Fuß aufgestanden, und alles andere ging dann auch mit linken – ich meine rechten – Dingen zu."


show rin negative_sad_close_ni onlayer master
with charachange

rin "Es liegt an mir."


show rin negative_worried_close_ni onlayer master
with charachange

rin "Ich habe mich geirrt."


hide rin onlayer master
with charaexit

"Sie stellt sich gerade hin und streckt sich, bevor sie an mir vorbei auf die Straße läuft."


hi "Warte, wo gehst du hin?"


show rin basic_absent_ni onlayer master
with charaenter

"Sie bleibt stehen, dreht sich um und wirft mir einen fragenden Blick zu."


show rin basic_awayabsent_ni onlayer master
with charachange

rin "Schule. Ich gehe."


hi "Was… wieso?"


show rin basic_absent_ni onlayer master
with charachange

rin "Weil ich ich sein will."


$ renpy.music.set_volume(0.4, 1.0, channel="ambient")

hide rin onlayer master
with charaexit

"Rin läuft davon und lässt mich völlig verwirrt zurück."


hi "Rin!"


"Doch… etwas, was sie gesagt hat, hat mich wirklich berührt – oder vielleicht war es die Art, wie sie es gesagt hat."


"Vielleicht war es die Tatsache, dass {b}sie{/b} es gesagt hat."


"Ich will ihr etwas erwidern, bevor ich dieses Gefühl wieder vergesse."


"Wie um mir diesen Wunsch zu erfüllen, bleibt Rin abrupt stehen. Sie dreht sich nicht um. Sie wartet lediglich darauf, dass ich sage, was ich zu sagen habe – auch wenn ich keine Zeit hatte, darüber nachzudenken."


hi "Rin… hör mal. Ich… Ich denke nicht, dass du allein sein musst. Selbst wenn du nie so jemanden findest."


"Ich weiß nicht, ob sie meine Worte gehört hat; jedenfalls reagiert sie in keinster Weise."


"Sie läuft los und lässt die Galerie hinter sich – zum letzten Mal."


play sound sfx_storebell
stop ambient fadeout 0.5

scene bg gallery_int onlayer master
show crowd onlayer master at center
show nomiya frown onlayer master at twoleft
show sae doubt onlayer master at tworight
with locationchange

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0

no "Also? Wo ist Tezuka?"


"Ich kann nur meinen Kopf schütteln, aber da diese Antwort ihm anscheinend nicht ausreicht, muss ich doch etwas sagen."


hi "Sie ist weggelaufen."


show nomiya stern onlayer master
with charachange

no "Was?"


"Die schreckliche Erkenntnis breitet sich auf seinem Gesicht aus wie ein Lauffeuer."


show nomiya serious onlayer master
with charachange

no "Das ist ein Fiasko! Eine Katastrophe!"


no "Was denkt sich dieses Mädchen bloß? Das wichtigste Ereignis ihres Lebens, und sie rennt einfach weg?"


show nomiya stern onlayer master
with charachange

no "Und du! Warum hast du sie nicht aufgehalten? Ich werde dich persönlich verantwortlich machen…"


show sae neutral onlayer master
with charachange

"Sae unterbricht ihn, indem sie ruhig ihre Hände hochhält."


"Es ist gut, dass sie eingeschritten ist; Herr Nomiya fing an, ein paar seltsame Blicke der umstehenden Gäste auf sich zu ziehen."


show sae smile onlayer master
with charachange

sa "Aber, aber, Shinichi. Sie hatte wahrscheinlich nur Lampenfieber. Ich kenne sie nicht so gut wie ihr, aber ich hatte den Eindruck, dass sie etwas eigenartig ist."


sa "Solche Dinge können passieren."


show sae neutral onlayer master
with charachange

sa "Es ist schon in Ordnung. Ich werde erklären, dass sie sich plötzlich schlecht fühlt. Die Gäste werden das sicher verstehen."


show nomiya frown onlayer master
with charachange

no "Aber…"


show sae smile onlayer master
with charachange

sa "Sieh dich um, alle scheinen ziemlich glücklich mit ihrem Gratiswein und Geschwätz zu sein."


show nomiya serious onlayer master
with charachange

no "Den Gästen wird es schon genügen, aber wir verpassen hier Gelegenheiten! Vernetzung, Kontakte knüpfen und Bekanntschaften!"


show emicas invis_close onlayer master:
    center
    xpos -0.35
with None

show bg gallery_int onlayer master at left
show crowd onlayer master at left
show nomiya serious onlayer master:
    xpos 0.5
show sae smile onlayer master:
    xpos 0.9
show emicas frown_close onlayer master:
    xpos 0.15
with dissolvecharamove

"Während die Erwachsenen weiter über etwas streiten, gegen das man nichts tun kann, zupft Emi an meinem Ärmel, um meine Aufmerksamkeit zu bekommen."


"Sie sieht ebenfalls nicht sehr glücklich aus."


show emicas awayfrown_close onlayer master
with charachange

emi "Komm schon."


hi "Wohin?"


show emicas frown_up_close onlayer master
with charachange

emi "Wir finden Rin und treten ihr in den Arsch."


hi "Was?"


show emicas angry_close onlayer master
with charachange

emi "Ich kann's nicht fassen, sie ist so blöd!"


emi "Diese Rin, wie kann sie das nur tun? Ich sag dir, sie hat kein bisschen gesunden Menschenverstand in ihrem Kopf!"


"Emi ist ernsthaft wütend. Es fehlt nur noch der Dampf aus ihren Ohren."


"Ich schätze, ich kann Emi verstehen. Sie ist {b}diese{/b} Art von Mensch."


"„Aufgeben” hat keinen Platz in ihrem Vokabular, und vielleicht denkt sie, es sollte in niemandes Vokabular Platz haben."


hi "Es ist wahrscheinlich das Beste, sie für heute Nacht in Ruhe zu lassen."


show emicas angry_up_close onlayer master
with charachange

emi "Was? Bist du jetzt ein Rin-Experte?"


"Sie richtet sich auf und legt ihre Hände streitlustig auf ihre Hüften."


"Es ist, als ob sie auch mit mir einen Streit anfangen will."


hi "Nein, ich glaube, das geht überhaupt nicht."


hi "Ich glaube einfach nicht, dass ihr ein Tritt in den Arsch etwas bringen würde."


show emicas frown_close onlayer master
with charachange

"Meine melancholische Bemerkung funktioniert überraschenderweise, da Emi ihre Schultern etwas erschlaffen lässt und seufzt."


emi "Das weiß ich."


hi "Tust du?"


stop music fadeout 2.0

show emicas awayfrown_close onlayer master
with charachange

emi "Das letzte Mal, als ich das getan hab, hat es nichts gebracht."


stop ambient fadeout 1.0

scene ev busride_ni onlayer master
with locationskip

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
play ambient sfx_businterior fadein 2.0

"Die Rückfahrt zu Schule in einem leeren Nachtbus verläuft schweigsam."


"Wir beide starren auf die vorbeiziehenden Lichter hinter dem Fenster, ohne ein Wort zu sagen."


stop ambient fadeout 1.0

scene bg school_dormext_full_ni onlayer master
with locationskip

play music music_soothing fadein 0.5

"Das nächtliche Schulgelände ist still, nur erleuchtet vom blassen Mond und den gelben Laternen."


"Vor meinem Wohnheim wünschen wir uns Gute Nacht."


show emicas awayfrown_up_ni onlayer master at center
with charaenter

"Dass Emi reflexartig ihre Fäuste ballt, zwingt mich dazu sicherzustellen, dass sie Rin nicht überfällt, sobald ich sie aus den Augen lasse."


hi "Versprichst du mir, sie nicht auszuschimpfen?"


show emicas angry_up_ni onlayer master
with charachange

"Sie sieht zu mir hinauf. Ihre Augen lodern vor Zorn, den ich mit dem ruhigsten Blick kontere, der mir möglich ist."


"Es ist nur einfach, einer wütenden Frau gegenüberzustehen, wenn man nicht das Ziel ihres Zorns ist."


"Nach einer Minute des ungleichen Starr-Wettbewerbs seufzt sie und schüttelt besiegt ihren Kopf."


show emicas closedsmile_ni onlayer master
with charachange

emi "Du bist zu nett, Hisao."


show emicas weaksmile_ni onlayer master
with charachange

emi "Wusstest du das?"


"Anzeichen eines Lächelns zieren ihre Mundwinkel, als sie das sagt, und sie wirkt viel gelassener."


"Was für ein abrupter Stimmungswandel."


"Vielleicht war sie von Anfang an gar nicht so wütend, wie es den Anschein hatte."


"Vielleicht ist sie auch einfach nur launisch."


hi "Wenn ich das wäre, würde ich dich tun lassen, was du willst."


show emicas wink_ni onlayer master
with charachange

emi "Heißt das, dass du nur zu Rin nett bist?"


"Wir beide verbergen unsere Besorgnis hinter leeren Witzen, aber zumindest bringt es mich in eine gute Stimmung."


"Emi lässt mit einem halb-amüsierten Schmunzeln ihre Augenbrauen wackeln, um mich anzustacheln. Nicht mit mir."


hi "Nein, es heißt einfach, dass ich nur zu dir nicht nett bin."


show emicas angry_up_ni onlayer master
with charachange

emi "HEY!"


stop music fadeout 2.0

hi "Gute Nacht, Emi."


scene black onlayer master
with dissolve


label de_R33:

play music music_daily fadein 0.5

scene bg school_scienceroom onlayer master
with locationchange

"Der letzte Tag vor den Sommerferien endet langsam."


"Naturwissenschaften ist die letzte Prüfung des Trimesters, und danach haben wir frei."


"Die kollektive Sehnsucht nach Freiheit ist in den Klassenzimmern fast spürbar, auch wenn das Wetter ein bisschen wolkig zu sein scheint."


"Vielleicht regnet es heute, wer weiß."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene ev rin_doodle onlayer master
with locationchange

"Weil er ziemlich einfach war, bin ich mit dem Test bereits fertig, also kritzle ich träge auf der Rückseite das Blattes und warte darauf, dass Mutou die Blätter einsammelt."


"Außerdem verhindert das, dass Misha heimlich über meine Schulter meine Antworten abguckt."


"Sie mag den unaufmerksamen Lehrer austricksen, aber ich weiß, dass sie es versucht."


"Ich schätze, es ist ihre beste Chance, den Test zu bestehen. Jedoch lässt mich das keine Gnade empfinden, darum ignoriere ich sie einfach und schaue mich um."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

scene bg school_scienceroom onlayer master
with locationskip

"Es ist still."


"Die einzigen Geräusche im Klassenzimmer sind das leise Rascheln der Blätter und Mutous ständiges Husten."


"Ich nehme meine Umgebung nur noch unterbewusst wahr, und meine Gedanken schweifen ab zu anderen Dingen."







label de_R34:
scene bg school_scienceroom onlayer master
with None

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\nFerien, hm?"


n "Manche Leute werden sogar über die Ferien an der Schule bleiben, andere werden zurück zu ihren Familien fahren."


n "Ich weiß nicht, was ich tun soll. Ich sollte mir ein Zugticket für die Fahrt nach Hause kaufen, aber ich kann mich nicht dazu überwinden."


n "Ich wette, ich bekomme wieder einen Anruf von zu Hause: Mama wird mich drangsalieren, wann ich denn zurückkomme, und ich werde nicht wissen, was ich darauf antworten soll."


n "\nDas ist wirklich mies. So wie die Dinge mit Rin jetzt stehen, kommt es mir so vor, als könnte ich nicht einfach von hier abhauen und so tun, als hätte sich das mit uns erledigt."


n "\nUnd nun hat sie ihre eigenen Probleme. Ich dachte, die Ausstellungseröffnung würde ihr eine Atempause geben, doch ich lag vollkommen falsch."


n "Das Gewirr verdichtet sich anscheinend nur weiter."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

play sound sfx_doorknock

window show

"Ein kurzes Klopfen an der Tür unterbricht die stille aber hektische Stimmung der letzten 15 Minuten der Prüfung."


show muto normal onlayer master at center
with charaenter

$ renpy.music.set_volume(0.2, 0.0, channel="sound")

mu "Herein."


stop music fadeout 1.0
$ renpy.music.set_volume(1.0, 8.0, channel="sound")
play sound sfx_footsteps_hard

show bg school_scienceroom onlayer master at bgleft
show muto normal onlayer master at twoleft
with charamove

show nomiya serious onlayer master at tworight
with charaenter

"Die aufgehende Tür bringt Herrn Nomiya zum Vorschein; sein Sakko weht um ihn herum wie in einer Windböe."


"Er wirft Mutou einen Blick zu, den dieser erwidert."


play music music_tension

show muto irritated onlayer master
show nomiya stern onlayer master
with charachange

"Beide runzeln zeitgleich die Stirn, als die Männer sich gegenseitig mit ihren Blicken abschätzen."


no "Entschuldigen Sie, könnte ich Herrn Nakai für einen Moment ausleihen?"


mu "Entschuldigen {b}Sie{/b}, Herr Nomiya, aber wir sind hier mitten in einer Prüfung."


"Eine kalte Atmosphäre breitet sich plötzlich inmitten des Sommernachmittags aus, als die beiden Männer versuchen, den jeweils anderen niederzustarren."


show nomiya serious onlayer master
with charachange

no "Es ist dringend, und es scheint, als wäre Nakai bereits fertig."


"Beide Männer wenden sich zu mir und starren mich an wie ein Paar Basilisken, die versuchen, einen schmackhaften Snack versteinern zu lassen."


"Es stimmt, dass ich seit einer guten Weile unbeschäftigt bin, somit hat Herr Nomiya recht, aber…"


show muto normal onlayer master
with charachange

mu "Nakai, würdest du deine Antworten gerne noch einmal überprüfen?"


"Mutou spricht mit einer eigenartigen Betonung – er gewichtet bestimmte Wörter, als ob er eine Nachricht senden wollte."


"Der Druck ihrer Blicke lässt mich zügig meinen Kopf schütteln, was offenbar in gewisser Weise als eine Antwort interpretiert wird."


stop music fadeout 6.0

show muto irritated onlayer master
with charachange

mu "Also gut. Nakai, geh mit Herrn Nomiya, wenn ich bitten darf."


mu "Nimm deine Tasche mit, und bring dein Prüfungsblatt zu meinem Schreibtisch."


show muto smile onlayer master
with charachange

mu "Ich wünsche dir schöne Ferien."


hi "Ähm. Äh, Ihnen auch, Herr Mutou."


"Die ganze Welt… Na ja, zumindest der ganze Klassenraum scheint nur für mich den Atem anzuhalten. Die Prüfung wird unterbrochen, bis ich aufstehe, meinen Kram einpacke und zur Tür gehe."


"Ich kann die Blicke auf meinem Nacken spüren. Meine Klassenkameraden denken wahrscheinlich, dass mir eine Art Nachsitzen oder so etwas blüht – am letzten Schultag vor den Sommerferien."


"Was Herr Nomiya von mir will, weiß ich nicht, aber ich kann erraten, dass es wahrscheinlich kein Nachsitzen ist und dass es wahrscheinlich wieder etwas mit Rin zu tun hat."


scene bg school_hallway3 onlayer master
with locationchange

play sound sfx_doorslam
with vpunch

"Nomiya bringt mich nirgendwo hin. Er begnügt sich mit dem Korridor, da er komplett verlassen ist."


show nomiya serious onlayer master at center
with charaenter

play music music_pearly fadein 1.0

no "Weißt du, wo Tezuka ist?"


"Also versucht sie, ihm aus dem Weg zu gehen… War wohl zu erwarten."


"Ob sie wohl begreift, dass sie ihm nicht für immer aus dem Weg gehen kann?"


hi "Ich habe keine Ahnung."


hi "Bestimmt haben Sie auch schon in ihrem Klassenzimmer nebenan gefragt."


show nomiya stern onlayer master
with charachange

no "Natürlich habe ich das! Ich habe in jedem Winkel dieser verfluchten Schule und dem Mädchenwohnheim gesucht."


no "Du bist der Letzte, der sie gestern gesehen hat, und du bist mit ihr befreundet."


show nomiya serious onlayer master
with charachange

no "Also hilf mir. Machst du dir keine Sorgen?"


"Das schon, aber ich weiß nicht, was ich tun könnte."


"Rin hat gestern etwas Unbegreifliches getan, selbst für ihre Verhältnisse."


"Sie schien wirklich verwirrt."


hi "Vielleicht will sie einfach nur etwas Zeit zum Nachdenken. Ich hatte den Eindruck, dass sie es sich bezüglich der Ausstellung noch einmal anders überlegt hat."


"Oder so in etwa. Sie hat wirklich nicht erklärt, was los ist."


show nomiya frown onlayer master
with charachange

no "Noch einmal anders überlegt?"


hi "Weiß nicht. Es kam mir nur so vor."


"Ich bin etwas unehrlich mit Herrn Nomiya, aber das ist nichts, wo ich mich einmischen sollte."


"Er kam zu mir… ja, wieso? Vielleicht denkt er, ich bin eine Art Vertrauensperson für Rin, aber ich glaube nicht, dass ich bei dieser Angelegenheit helfen kann."


show nomiya serious onlayer master
with charachange

"Herr Nomiya schnaubt und kratzt sich verwirrt am Kopf."


no "Was ist nur mit diesem Mädchen? Das passt nicht zu ihr. Sie ist immer so zielstrebig gewesen."


"„Zielstrebig?” Ich glaube nicht, dass man Rin mit diesem Wort beschreiben kann."


"Bestenfalls kam sie mir immer besessen vor."


hi "Äh, ich will nicht unhöflich sein, aber waren Sie nicht derjenige, der Rin in diese Richtung gedrängt hat?"


show nomiya dreamy onlayer master
with charachange

no "Ihr Ziel ist mein Ziel. Das ist der Job eines Mentors."


hi "Mag sein. Ich weiß nur nicht, ob die Malerei sie glücklich machen kann."


show nomiya stern onlayer master
with charachange

no "So etwas zu sagen, ist ziemlich absurd, Nakai."


"Plötzlich klingt er sehr erzürnt. Habe ich etwas Dummes gesagt?"


show nomiya serious onlayer master
with charachange

no "Du verstehst es nicht, oder? Es geht hier nicht ums Glücklichsein. Für jeden Gewinn muss ein Opfer gebracht werden."


show nomiya stern onlayer master
with charachange

no "Es gibt nichts umsonst, aber könnte ich… würde ich es zulassen, dass dieses Mädchen in einem Moment des Zweifels ihr Talent wegwirft? Niemals!"


no "Malerei ist Arbeit wie jede andere. Tezuka lässt es für dich vielleicht wie ein Kinderspiel aussehen, doch sie arbeitet jeden Tag hart, um ihre Kunst zu erschaffen."


no "Um außergewöhnlich zu werden, muss man sich außergewöhnlich anstrengen."


"Je mehr Herr Nomiya redet, umso mehr glaube ich, dass Rin nicht so denkt – auch wenn ich nicht weiß, was in ihrem Kopf vor sich geht."


show nomiya serious onlayer master
with charachange

no "Ich kann sehr gut verstehen, warum sie den verpassen Unterricht und die verpassten Prüfungen in den Sommerferien nachholen wird, um einen Chance zu bekommen, ihre Kunst zu präsentieren."


no "Das ist der Pfad, den sie eingeschlagen hat. Und ihn bis zum Ende zu laufen ist nicht einfach."


no "Ich weiß, dass sie jung ist, und es genauso schwer hat wie all die anderen Kinder hier an dieser Schule, aber das ist keine Ausrede."


"Er ist fertig."


hi "Aber—"


show nomiya smile onlayer master
with charachange

no "Hast du irgendetwas, das für dich ist wie die Kunst für Tezuka?"


hi "Nein…"


"Ganz recht. Ich habe nur vage Vorstellungen von meiner Zukunft; kein Ziel, nach dem ich streben kann; keinen Traum, dem ich hinterherjagen kann."


"Ich bin dem Kunstklub auf der Suche nach etwas beigetreten, für das ich mich interessieren könnte – etwas, das mich inspirieren könnte."


"Habe ich so etwas gefunden?"


"Alles, was ich letztendlich fand… war Rin."


hi "Nein, so eine Leidenschaft habe ich nicht."


show nomiya serious onlayer master
with charachange

no "Dann kannst du es auch nicht verstehen."


"Seine schroffe Aussage erlaubt kein Gegenargument."


hi "Aber… Vielleicht versteht sie sich nicht einmal selbst."


"Dennoch diskutiere ich weiter – möglicherweise nur aus Trotz."


show nomiya stern onlayer master
with charachange

no "Wie könnte sie nicht? Sie hat die letzten Wochen so hart gearbeitet, dass sie sogar aufgehört hat, zur Schule zu kommen. Vom Unterricht ganz zu schweigen. Mach dich nicht lächerlich."


"Ich denke nicht, dass ich mich lächerlich mache. Aber da ich das nicht widerlegen kann, scheint Nomiya diese Runde als seinen Sieg anzusehen. "


show nomiya smile onlayer master
with charachange

no "Jedenfalls war die Eröffnung ziemlich erfolgreich, obwohl Tezuka kaum da war."


no "Viele Leute waren an ihrer Arbeit interessiert, und ein Stück wurde sogar für einen angemessenen Preis verkauft."


hi "Na ja, das ist doch schön, oder?"


show nomiya veryhappy onlayer master
with charachange

no "Sicher, es sind fantastische Neuigkeiten! Ich habe gehofft, sie würde zu Sinnen kommen, wenn sie das hören würde, aber…"


"Er seufzt, nimmt seine Brille ab und säubert sie mit seinem Sakko, bevor er sie sich wieder auf seine Nase setzt."


show nomiya smile onlayer master
with charachange

no "Wie dem auch sei, ich sollte gehen. Dieses Durcheinander muss mit Sae und allen anderen geklärt werden."


no "Falls du Tezuka siehst, sag ihr bitte, dass sie zu mir kommen sollen. Andernfalls wünsche ich dir schöne Ferien."


hi "Danke…"


stop music fadeout 6.0
play sound sfx_footsteps_hard
$ renpy.music.set_volume(0.0, 4.0, channel="sound")

hide nomiya onlayer master
with charaexit

"Nachdem er um die Ecke verschwunden ist, brüte ich darüber, wo Rin wirklich sein könnte."


"Es kommt mir vor, als hätte sie nicht einen, sondern mindestens ein halbes Dutzend dieser „geheimen Orte.”"


"Ich schwanke zwischen dem Verlangen, dieses Durcheinander zu entwirren und es ein für alle Mal sein zu lassen."


"Das unbenutzte Klassenzimmer ist nur ein paar Meter weit weg."


"Was soll ich tun?"


"…"


$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_dooropen

scene bg school_room34 onlayer master
with locationchange

"Als ich die Tür aufdrücke, begrüßen mich aus dem Inneren nur Schatten."


hi "Hallo."




label de_R35:

scene bg school_scienceroom onlayer master
with None

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\nFerien, hmm?"


n "Manche Leute werden sogar über die Feiertage zu Hause bleiben, Manche werden zurück zu ihren Familien fahren."


n "Wahrscheinlich sollte ich die Fahrt nach Hause antreten und meinen Eltern zeigen, dass ich am Leben bin und es mir gut geht."


n "\nAn der Schule gibt es sowieso nicht viel zu tun, schätze ich."


n "Das nächste Trimester wird stressig. Alle werden ernsthaft darüber nachdenken müssen, was sie nach ihrem Abschluss machen wollen."


n "\n\nMich eingeschlossen…"


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

scene ev rin_doodle_all onlayer master
with silentwhiteout

window show

"Ein Blick auf meine Kritzeleien lässt mich sie verwerfen. Es ist ein Chaos aus leblosen Linien, eine Verschwendung von Papier, wenn es nicht die Rückseite meiner Prüfung wäre."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\n\nVielleicht liegt es daran, dass ich gar nicht vorhatte, etwas Spezielles zu zeichnen."


n "Ich wollte nur etwas Zeit totschlagen, daher wurde die Zeichnung genau wie ich."


n "Ziellos."


n "\n\nEs wäre einfacher, wenn ich ein besonderes Talent hätte – wie Rin."


n "Sie hat es leicht."


n "Irgendwie macht mich das neidisch."


n "Es kotzt mich an, dass sie selbst nicht glücklich darüber sein kann."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

scene bg school_scienceroom onlayer master
show muto smile onlayer master at center
with locationskip

window show

mu "Uuuuund… Ende!"


"Mutous Ankündigung des Prüfungsendes entlockt der halben Klasse ein missmutiges Stöhnen."


"Ich kann es ihnen nicht verübeln. Die Prüfung war ganz schön verzwickt."


"Mutou erwartet eine Menge von unserer Klasse, obwohl er überhaupt nicht streng ist. Vermutlich würde er sich freuen, wenn wir alle Wissenschaftler werden."


show muto normal onlayer master
with charachange

mu "Bitte legt eure Stifte weg und gebt eure Blätter nach vorne."


"Das lauteste Stöhnen kommt von dem Tisch neben mir."


show misha invis_close onlayer master:
    center
    xpos -0.2
    ypos 1.13
with None

show bg school_scienceroom onlayer master at bgright
show muto normal onlayer master at tworight
show misha perky_sad_close onlayer master:
    xpos 0.15
with dissolvecharamove

"Mishas Verzweiflung ist fast greifbar."


"Die dunkle Aura verlorener Hoffnung, die von ihrem Platz ausgeht, beängstigt mich. Gleichzeitig lässt sie mich aber auch Mitleid empfinden."


show muto smile onlayer master
with charachange

mu "Also dann, wir haben noch Klassenstunde, bevor ihr entlassen seid, aber ich habe nur ein paar Ankündigungen zu machen, darum sollten wir schnell durch sein…"


"Seine Ankündigungen sind nie wichtig, daher höre ich nur mit einem Ohr zu."


"Misha scheint sogar zu deprimiert zu sein, um so zu tun, als wäre sie aufmerksam."


"Sie liegt zusammengesackt mit ihrem Kopf auf dem Tisch."


hi "Kopf hoch, Misha."


hi "Es sind Ferien! Mach dir keine Sorgen um den Test."


show misha sign_smile_close onlayer master
with charachange

mi "Danke, Hicchan."


"Ihr finsterer Blick wird zu einem kleinen Lächeln. Dann leuchtet ein Funken Begeisterung in ihren Augen auf."


show misha perky_smile_close onlayer master
with charachange

mi "Was machst du über die Sommerferien, Hicchan?"


show misha hips_smile_close onlayer master
with charachange

mi "Ich fahre zu Shicchan nach Hause; die haben diese hammermäßige und supercoole Villa! Ich bin so aufgeregt~!"


show misha hips_grin_close onlayer master
with charachange

mi "Ich bin sicher, dass das die bestesten Sommerferien aller Zeiten werden~!"


"Anscheinend hat sie ihr Elend in ein paar Sekunden komplett vergessen und hüpft auf ihrem Stuhl auf und ab, als würde sie ihre Begeisterung aufladen."


hi "Ich hab keine richtigen Pläne, schätze ich…"


show misha sign_smile_close onlayer master
with charachange

mi "Wirklich~? Vielleicht solltest du—"


show misha perky_confused_close onlayer master
with charachange

"Ein auf ihre Schulter tippender Finger raubt mir Mishas Aufmerksamkeit."


show muto irritated onlayer master
with charachange

"Shizune deutet auf Mutou, der sie beide erwartungsvoll ansieht."


show misha sign_confused_close onlayer master
with charachange

mi "Ups! Sorry, Shicchan. Ich hab nicht bemerkt, dass der Lehrer schon fertig ist, ehehe~."


"Sie räuspert sich und atmet tief ein."


show misha hips_grin_close onlayer master:
    ypos 1.0
with dissolvecharamove

mi "Aufstehen!"


"Ich stehe mit allen auf."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\nSeit ich herkam, habe ich mich die ganze Zeit etwas gefragt."


n "Was denken die an den Rollstuhl gebundenen Schüler über diese tägliche Tradition, die sie nicht „richtig” ausführen können?"


n "Ist es ein Fauxpas, diese Tradition an einem Ort aufrechtzuerhalten, der viele andere aus Zweckmäßigkeit umgeht?"


n "Auch wenn ich nie jemanden gefragt habe, bin ich in diesen kurzen Wochen hier zu dem Schluss gekommen, dass sie sich keinesfalls dadurch beleidigt fühlen."


n "Sie verstehen es."


n "Das mag ich an dieser Schule. Niemand ist wegen etwas zu verklemmt; alle sind so… rücksichts- und verständnisvoll gegenüber anderen."


stop music fadeout 4.0

n "\n\nIch wünschte, die ganze Welt könnte so sein."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

scene black onlayer master
with locationchange

window show

mi "Verbeugeeeen!"


scene bg school_dormhisao onlayer master
with shorttimeskip

play sound sfx_paper
play music music_tranquil fadein 3.0

"Ich blättere die Seite langsam um und lausche dabei dem Rascheln des Papiers, als meine Finger es berühren."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\nIch bin rastlos."


n "Es sind Sommerferien."


n "Kein Unterricht, keine Hausaufgaben, keine Kunstklubtreffen. Nur Freizeit, die ich verbringen kann, wie ich will."


n "Danach fühlt es sich aber nicht an."


n "Ich versuchte, Misha aufzumuntern, aber ich selbst fühle mich nicht allzu heiter."


n "Um ehrlich zu sein, macht mir die Freizeit Angst. Sie erinnert mich an das Krankenhaus und die langen, bedeutungslosen Tage, die irgendwie verbracht werden mussten."


n "Der einzige Unterschied ist, dass ich an die Station gefesselt war – bewacht von cerberusartigen Schwestern."


n "Damals war Lesen eine gute Lösung. Aber der Gedanke, meine Sommerferien mit Bücherlesen zu verbringen, kommt mir… streberhaft vor."


n "Das hat nichts mit der Tatsache zu tun, dass ich sogar jetzt gerade lese… Ich schlage nur etwas Zeit tot und versuche, meine Unruhe zu bekämpfen."


n "Außerdem bin ich mit dem Kopf woanders, aber ich denke an zu viele Sachen gleichzeitig, um auch nur eine davon zu ergründen."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

window show

"Folglich komme ich mit dem Buch, das ich seit Dienstag lese, nur l{w=0.3}a{w=0.3}n{w=0.3}g{w=0.3}s{w=0.3}a{w=0.3}m voran."


"Es kommt mir vor, als bräuchte ich länger, um das Buch zu lesen, als der Autor, um es zu schreiben."


"Ich versuche, es eine Weile wegzulegen und dann wieder ein wenig zu lesen, von vorne zu beginnen, jede Seite zweimal zu lesen…"


"Nichts funktioniert – meine Konzentration liegt bei null."


"Ich gehe nach draußen, um etwas frische Luft zu schnappen und zu überlegen, was ich sonst tun könnte. Das Buch nehme ich mit – nur für alle Fälle."


scene bg school_courtyard onlayer master
with locationskip

"Ich laufe über den Innenhof, vorbei an Schülern auf dem Weg zu dem Tor."


"Ihrem Gepäck nach zu urteilen sind die hastigsten Schüler wohl schon auf dem Weg nach Hause."


"Ich schätze, zu Hause ist halt zu Hause, egal wie gastfreundlich Yamaku ist. Trotzdem hörte ich, dass einige Leute über die Ferien hierbleiben werden."


"Der Innenhof ist so groß, dass sein Zentrum schattenlos bleibt – egal wie hoch oder tief die Sonne steht."


"Ich bleibe in der Mitte stehen und bade in der Wärme."


"Die Helligkeit lässt mich meine Augen zusammenkneifen, als ich in Richtung des Hauptgebäudes sehe."


"Es sieht schon beinahe verlassen aus."


"Yuuko hat heute nicht gearbeitet, darum kann ich erst nach den Ferien neue Bücher aus der Schulbibliothek besorgen."


"Es gibt bestimmt irgendwo eine öffentliche Bibliothek, aber ich fühle mich zu träge, um herauszufinden, wo sie ist."


scene bg school_lobby onlayer master
with locationskip

"Der Korridor ist nahezu ausgestorben, deshalb muss ich mich damit zufriedengeben, zu den Wohnheimen zurückzukehren und meinen gemächlichen Spaziergang früher als erwartet beenden."


"Dann wiederum war ich mir nicht ganz sicher, was ich überhaupt erwartet habe."


scene bg school_girlsdormhall onlayer master
with locationskip

"Aus einen Impuls heraus betrete ich das Mädchenwohnheim, um nachzusehen, ob Rin oder Emi dort sind."


"Keine von beiden ist es, darum gehe ich zurück zu meinem Zimmer, um mich meiner Lethargie hinzugeben."


window hide

scene bg school_dormhisao onlayer master
with locationskip

$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl clear
nvl show dissolve

n "\n\nIch sollte die Dinge mit Rin bereden."


n "Sie beunruhigt mich wirklich."


n "\n\nEinem Konzept wie der Gravitation trotzend, balanciert sie auf der schmalen Linie zwischen Wahnsinn, Unbegreiflichkeit und Instabilität."


n "Rin hat auch auf mich Auswirkungen. Sie fordert mich auf Arten heraus, die ich nicht kannte… oder genauer gesagt, von denen ich hoffte, dass sie nicht existieren."


n "\n\nIch habe angefangen, mich zu fragen, ob diese Gefühle wirklich Liebe sind, oder ob ich mir selbst etwas vorgemacht habe."


n "Das zu erwägen wäre doch sicherlich Irrsinn, oder?"


nvl clear

n "\n\nFür den Rest des Tages kreisen Rin, das Krankenhaus, Yamaku und die Ferien durch meinen Kopf."


n "\nIch kann mich nicht einmal aufs Konzentrieren konzentrieren."


n "\nGedanken scheinen zu kommen und zu gehen, zersplittert in zu kleine Stückchen der Wahrnehmung."


n "\nIch nehme das Buch zur Hand und schaffe es, hundert Seiten zu lesen, aber ich bin mir sicher, dass ich bis morgen keine Erinnerung mehr an die Geschichte haben werden."


n "\nIch versuche, mein Zimmer aufzuräumen, doch selbst das ist mir zu lästig, zu zeitaufwändig, und man muss auf zu viele Kleinigkeiten achten."


n "So ist es meistens. Wenn man „nichts zu tun” hat, tut man nichts. Auch wenn man es könnte."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

scene bg school_dormhisao_blurred_ss onlayer master
show phone mobile onlayer master at center
with shorttimeskip

window show

"Wie erwartet ruft mich meine Mutter an, und ich verspreche ihr schließlich, mich morgen nach einem Zugticket zu erkundigen. Oder, falls das nicht klappt, am Tag danach."


window hide
nvl clear

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

$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl show dissolve

n "\n\nVielleicht gehe ich morgen sowieso ohnehin in die Stadt. Ich könnte etwas shoppen gehen oder so."


n "Ich brauche zwar nichts, aber vielleicht gibt es Sommerangebote, und ich finde… etwas…"


stop music fadeout 10.0

n "\n\n… Warum versuche ich, mich zu zwingen?"


n "Früher war ich damit zufrieden, nichts zu tun zu haben, außer hin und wieder auf dem Feld kicken zu gehen."


n "Nun scheint es, als könnte ich überhaupt nicht zur Ruhe kommen."


n "\nLiegt es daran, dass ich mich verändert habe? Oder dass meine Welt sich verändert hat?"


nvl hide dissolve
nvl clear

scene bg school_dormhisao_ni onlayer master
with shorttimeskip

window show

"Gegen elf lässt mich die Dunkelheit in den Schlaf sinken."


window hide

show pills onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

window show

"Die Tablettenfläschchen stehen harmlos auf meinem Nachttisch aufgereiht. Sie erinnern mich demonstrativ an die Realität."


"Es ist Abend, darum muss ich drei dieser Fläschchen öffnen und vier Tabletten herausnehmen – eine große ovale, zwei kleine runde und eine große flache, die in zwei Hälften geteilt werden muss."
"Ich schließe die Fläschchen wieder und spüle die Tabletten mit einem Schluck frischen Leitungswassers hinunter."


window hide

show pills onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide pills onlayer master
with None

window show

"Das Wasser hinterlässt einen metallischen Geschmack auf meiner Zunge."


"Ich schlucke es trotzdem hinunter und mache mich auf ins Bad."


scene bg school_dormbathroom onlayer master
with locationskip

"Stupides Zähneputzen ist perfekt, um meine Gedanken zu sortieren."


"Einer steigt aus der Masse empor und hebt sich von klar von den anderen ab."


window hide
nvl clear
nvl show dissolve

n "\n\n\n\n\n\n\n\n\nIch will Rin sehen."


n "Ich kann nicht zulassen, dass mein Wutausbruch das letzte bleibt, was vor den Sommerferien zwischen uns passiert ist."


nvl hide dissolve
nvl clear

scene bg school_dormhisao_ni onlayer master
with locationskip

nvl show dissolve

n "\n\n\n\n\n\n\n\nIch muss sie sehen – morgen."


n "Schlaf überkommt meinen verwirrten Verstand leichter als er sollte."


nvl hide dissolve
nvl clear

$ suppress_window_before_timeskip = True

scene black onlayer master
with shuteye


label de_R36:

$ renpy.music.set_volume(1.0, 0.0, channel="music")
$ renpy.music.set_volume(0.7, 0.0, channel="ambient")
play ambient sfx_rain fadein 1.0

scene bg misc_sky_rn onlayer master
show rain normal onlayer master
show hisaowindow onlayer master
with locationchange

"Regen prasselt auf meine Sommerferien nieder, wie eine Unzahl kleiner, schlechter Omen."


"Glücklicherweise bin ich nicht abergläubisch, aber das schlechte Wetter deprimiert auch mich."


"So ist es seit heute Morgen, und es ist kein Ende in Sicht."


"Eine undurchdringliche graue Masse aus Wolken verfinstert den Himmel ebenso wie meine Laune."


"In einem Anflug von Trotz habe ich heute morgen mein Zimmer aufgeräumt. Doch nachdem das erledigt war, habe ich einfach nur noch aus dem Fenster geschaut – in der Hoffnung, dass sich das Wetter bessert."


"Das unablässige Prasseln des Regens auf das Dach und auf den Bürgersteig ist hypnotisierend – ein dumpfes Hintergrundgeräusch, in dem man sich verlieren kann."


"…"


"… …"


$ renpy.music.set_volume(0.4, 1.0, channel="ambient")

scene bg school_dormhisao_rn onlayer master
with locationchange

"Das bringt nichts. Ich muss in die Gänge kommen."


"Soll ich jetzt packen oder später?"


$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg school_dormhallway onlayer master
with locationchange

"Ich entscheide mich für Letzteres und mache mich auf nach draußen. Vor Kenjis Tür mache ich kurz Halt, um den seltsamen, dumpfen Geräuschen auf der anderen Seite zu lauschen. "


show rain normal behind bg onlayer master
with None

"Aus Angst herauszufinden, was er gerade tut, wage ich es nicht zu klopfen."


$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

show bg school_dormext_full_rn as bg2 behind rain onlayer master
hide bg onlayer master
with locationskip

"Dem Regen unter meinem treuen Regenschirm trotzend steuere ich auf das Mädchenwohnheim zu."


$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg school_girlsdormhall onlayer master
with locationskip

play sound sfx_doorknock2

"Ich klopfe an Rins Tür, aber es erfolgt keine Reaktion. Stattdessen öffnet sich die Tür hinter mir."


play sound sfx_dooropen

show emicas invis onlayer master:
    center
    xpos 0.3
with None

show emicas happy onlayer master at center
with dissolvecharamove

play music music_emi fadein 0.5

emi "Hisao? Hi!"


show emicas awayfrown onlayer master
with charachange

emi "Furchtbares Wetter. Ich hab sogar mein Training heute morgen verpasst."


"Sie blickt finster drein, aber ich an ihrer Stelle wäre froh. Emis morgendliches Training ist alles andere als gemächlich."


hi "Oh, hi, ich wollte-"


show emicas neutral onlayer master
with charachange

emi "Falls du nach Rin suchst, ich glaube, sie ist nicht da."


hi "Hast du sie in letzter Zeit gesehen?"


show emicas grin_up onlayer master
with charachange

emi "Ja, gerade heute morgen, als ich sie aufgeweckt hab."


"Als Emi vom Aufwecken spricht, gähnt sie wie ein Katze. Ich komme mir albern vor."


"Natürlich hat sie Rin gesehen. Emi weckt sie, hilft ihr, sich anzuziehen, und macht ihr sogar ab und zu Essenspakete."


"Sie sind wie Schwestern, obwohl sie scheinbar nichts gemeinsam haben."



label de_R36a:

"Wer wohl die ältere von beiden ist? Gegen alle Wahrscheinlichkeit bestimmt Emi."


"Sie ist wirklich gewissenhaft, auch wenn sie wie ein totaler Hohlkopf rüberkommt."


"Warum kommt es mir so seltsam vor, dass hinter diesem Grinsen ein so pflichtbewusstes Mädchen steckt?"



label de_R36x:

show emicas frown_up onlayer master
with charachange

emi "Sie ist vor ein paar Stunden zur Galerie gegangen… hey, hörst du zu?"


"Vielleicht mache ich ein komisches Gesicht oder so, da Emi ihren Kopf schief legt und mich mit großen Augen fragend anschaut."


show emicas neutral onlayer master
with charachange

emi "Hmm?"


"Ihr unschuldiges Gesicht scheint nach meiner Aufmerksamkeit zu fordern."


hi "Ja, ich höre zu…"


show emicas weaksmile onlayer master
with charachange

emi "Kann ich dich was fragen?"


hi "Ja, na klar."


show emicas awayfrown onlayer master
with charachange

"Sie kneift ihre Augenbrauen zusammen und leckt sich über die Lippen, als würde sie sich auf etwas vorbereiten."


show emicas frown onlayer master
with charachange

emi "Warum sorgst du dich so sehr um Rin?"


show emicas neutral onlayer master
with charachange

emi "Ich meine, du hängst mehr mit ihr ab als ich, und wir haben bis vor kurzem sogar manchmal, äh, im selben Bett geschlafen."


hi "Bis sie dich rausgeworfen hat, weil du ihr Haar verwüstet hast?"


show emicas blush onlayer master
with charachange

"Emis Augen weiten sich vor Schreck auf mindestens das Doppelte, wodurch sie noch mehr wie Untertassen aussehen als sonst. Gleichzeitig färbt eine gesunde Röte ihre Wangen und Ohren."


show emicas angry_up onlayer master
with charachange

emi "Sie hat's erzählt? Ohhh… Ich werde diese Rin erwürgen oder etwas anderes Furchtbares…"



"Ich halte mein Lachen zurück, damit sie ihren Zorn nicht auf mich richtet."


show emicas closedsmile onlayer master
with charachange

"Emi erholt sich rasch von der Verlegenheit und scheint Rin im gleichen Moment zu vergeben. Nun liegt ihre Aufmerksamkeit wieder bei mir."


show emicas smile onlayer master
with charachange

emi "Wie auch immer – bist du in sie verliebt oder so?"


"Oh oh. Sie kommt wirklich wie eine ältere Schwester rüber, die einen Verehrer verhört. Emi ist ganz schön neugierig, und das nicht auf eine gute Weise – sofern es eine solche überhaupt gibt."


"Sie und Misha würden ein gutes Team abgeben, um ehrlich zu sein. Eine grauenhafte Vorstellung."


hi "Das ist schon deine zweite Frage, also denke ich nicht, dass ich antworten muss."


"Ich versuche, eine Fassade aus purer, kristalliner Coolness und Gleichgültigkeit zu errichten."


"Ob ich damit wenigstens mich selbst überzeugen kann?"


show emicas evil onlayer master
with charachange

"Jedenfalls wackelt Emi gefährlich mit ihren Augenbrauen und hat ein gemeines Grinsen auf ihren Lippen."


emi "Ist das ein Ja?"


hi "Nein, es ist kein Ja."


show emicas neutral onlayer master
with charachange

"Obwohl sie offensichtlich unzufrieden mit meiner Antwortsverweigerung auf ihre viel zu intime Frage ist, hat sie genug Einfühlungsvermögen, um sich zurückzuhalten."


show emicas wink onlayer master
with charachange

"Jedoch hält sie das nicht davon ab, mir wie ein Kind ihre Zunge herauszustrecken und erneut zu kichern."


show emicas closedsmile onlayer master
with charachange

emi "Wenn das deine Antwort ist, glaube ich nicht, dass ich noch weiter mit dir reden muss."


"Es ist leicht zu erkennen, dass sie nicht wirklich wütend ist."


show emicas happy onlayer master
with charachange

emi "Außerdem muss ich jetzt packen. Mama wird sich Sorgen machen, wenn ich meinen Bus verpasse."


emi "Ciao!"


hi "Ja, mach's gut."


stop music fadeout 4.0

hide emicas onlayer master
with charaexit

play sound sfx_doorclose

"Sie zieht sich in ihr Zimmer zurück und lässt mich allein im Korridor zurück."


"Was zwischen mir und Rin läuft geht sie nichts an, oder?"


"Deswegen habe ich Emi letztendlich nichts von unserem Streit erzählt. Rin hat bestimmt auch nichts gesagt."


"Ich nehme an… selbst wenn sie Freunde sind, gibt es Dinge, über die sie sich nicht unterhalten."


"…"


"Also. Wenn Rin in der Galerie ist, muss ich den ganzen Weg bis dorthin gehen."


"Jetzt, wo ich es geschafft habe, aus meinem Zimmer herauszukommen, wird es vermutlich nicht zu viel Mühe machen, in die Innenstadt zu gehen."


"Ich könnte mir ein Ticket holen gehen, doch der Zug zurück nach Hause muss noch warten – zumindest bis morgen."


show rain normal behind bg onlayer master
with None

"Auf keinen Fall werde ich in diesem Regen Gepäck bis zum Bahnhof tragen. Auch wenn es nicht allzu viel ist."


$ renpy.music.set_volume(1.0, 3.0, channel="ambient")

show bg city_street4_rn as bg2 behind rain onlayer master
hide bg onlayer master
with shorttimeskip

"Regen lässt alle Umrisse sehr unbeständig wirken, als würden sie verblassen."


"Das Stadtbild wird zu einer formlosen Ansammlung von mehreren unscharfen Grautönen anstelle deutlicher Konturen von Gebäuden und Autos."


"Diese Armen Seelen, die bei diesem Wolkenbruch raus müssen, versuchen, so schnell durchzukommen, wie sie können, und bemitleiden sich gegenseitig für ihr geteiltes Schicksal."


show bg gallery_ext_rn as bg2 onlayer master
with locationchange

"Ich laufe um die letzte Ecke. Genauer gesagt die zweiundzwanzigste Ecke, und ich komme mir umgehend bescheuert vor, weil ich mich über meinen eigenen Wortwitz amüsiere."


"Die Tür lädt mich mit einem Versprechen von Wärme ein."


$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
play sound sfx_storebell 
play music music_soothing fadein 0.5

scene bg gallery_int onlayer master
with locationchange

"Das Regenwasser, das von meinem Schirm tropft, macht interessante, fast künstlerische Muster auf dem Boden."


"Abgesehen von meinen Schuhen bin ich nicht nass. Diese haben kleine Pfützen hinter mir hinterlassen, welche das Regenwasser-Kunstwerk vervollständigen."


show nomiya smile onlayer master at twoleft
show sae neutral onlayer master at tworight
with charaenter

"Nomiya ist auch hier und schwatzt im hinteren Teil der Galerie mit Sae. Rin jedoch ist nirgends zu sehen."


"Vielleicht ist sie oben."


"Es sind auch keine Kunden da. Das ist nachvollziehbar in Anbetracht der Unmengen an Wasser, die auf jedermanns Nacken tropfen, der sich heute in dieses Wetter traut."


show sae smile onlayer master
with charachange

sa "Willkommen."


hi "Hallo. Entschuldigen Sie die Störung."


show nomiya talk onlayer master
with charachange

no "Ah, guten Tag Nakai."


show nomiya smile onlayer master
with charachange

no "Bist du den ganzen Weg hierher für einen Besuch gekommen?"


hi "Ah… nein, ich glaube, das kam nur aus einer Laune heraus. Ich war in der Nachbarschaft einkaufen, und dachte mir dann, ich schau mal vorbei."


"Ganz aus Reflex habe ich ihn angeschwindelt. Das überrascht mich selbst."


"Vielleicht will ich auch einfach nicht sagen, dass ich speziell gekommen bin, um Rin zu sehen – auch wenn es offensichtlich sein muss."


show sae doubt onlayer master
with charachange

sa "Herrje, da hast du dir einen schlechten Tag zum Einkaufen ausgesucht. Hättest du gerne etwas Tee, um dich aufzuwärmen."


hi "Danke, aber es geht schon. Wirklich."


hi "Allerdings könnte das Wetter besser sein. Regen am ersten Ferientag ist etwas deprimierend."


show nomiya veryhappy onlayer master
show sae neutral onlayer master
with charachange

no "Hahaha! Nun, ich bin sicher, dass es besser werden wird."


"Nomiya bietet sein herzhaftes, fast schon schroffes Lachen."


hi "Regen scheint ihnen wohl nichts auszumachen, Herr Lehrer."


show nomiya smile onlayer master
with charachange

no "Na ja, ich bevorzuge auch klares Wetter. Ich wollte eigentlich gerade gehen, um jemanden zu treffen, und mir wäre es lieber, wenn mein Sakko nicht nass würde. Es ist ausgesprochen teuer."


show nomiya talk onlayer master
with charachange

no "Aber gewiss bin ich in einer guten Stimmung!"


show nomiya smile onlayer master
with charachange

no "Wie fandest du die Ausstellung? Sie war großartig, nicht wahr?"


hi "Ja, sie war ziemlich ausgefallen."


"Meine lustlose Antwort beflügelt ihn nur noch mehr. Er wandelt durch die Galerie, während er über die Eröffnung faselt."


"Wenn er sich bewegt, spricht er mehr und lauter. Das habe ich auch schon bei den Klubtreffen bemerkt."


show nomiya veryhappy onlayer master
with charachange

no "Wir konnten mit vielen guten Leuten reden und wertvolle Kontakte knüpfen."


show nomiya smile onlayer master
with charachange

no "Eines von Tezukas Gemälden wurde sogar an einen Sammler aus Osaka verkauft."


$ renpy.music.set_volume(0.1, 1.0, channel="ambient")

show rin_exhibition_sold onlayer master at center
with locationchange

"Ich folge seinen Augen zu einer leeren Stelle an der Wand. Ich kann mich nicht einmal daran erinnern, dass dort ein Gemälde gehangen hat."


"Na ja, jetzt ist es weg."


$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

hide rin_exhibition_sold onlayer master
show nomiya talk onlayer master
with charachange

no "Es war Glück, dass es ihr trotz des Schwindelanfalls gut ging."


show nomiya smile onlayer master
with charachange

no "Aber sie ist ein wenig ruhig geworden, darum habe ich ihr gesagt, sie soll sich ausruhen. Andererseits ist sie schon immer ziemlich schüchtern gewesen."


"Schüchtern? Wie auch immer, ich nicke einfach."


show nomiya talktongue onlayer master
with charachange

no "Generell gab es sehr positiven Zuspruch. Vielleicht kriege ich einen meiner Freunde dazu, einen kleinen Artikel in einem Magazin zu schreiben, um-"


sa "Shinichi, deine Verabredung. Du lässt Herrn Takahashi warten."


show nomiya serious onlayer master
with charachange

"Saes Anmerkung lässt ihn stehen bleiben und auf seine Armbanduhr sehen."


"Nomiya runzelt aufgrund der Unterbrechung seiner Tirade missmutig die Stirn."


show nomiya smile onlayer master
with charachange

no "Oh, richtig. Ja, nun, ich mache mich dann auf den Weg. Wir sehen uns im September, Nakai."


hi "Wiedersehen."


hide nomiya onlayer master
with charaexit

play sound sfx_storebell
stop music fadeout 4.0

"Wow. Nomiya gibt echt alles, wenn es um Rins aufkeimende Künstlerkarriere geht."


"Vermutlich braucht es eine Menge zum Erfolg. Aber ich nehme an, sein Job wäre einfacher, wenn Rin etwas kooperativer wäre."


$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\nAuch wenn alles gut für sie läuft, ist sie zu unentschlossen. Wie bei dem „Schwindelanfall” von letzter Nacht."


n "Sie ist einfach durchgedreht oder so etwas, und ich habe nichts getan, um ihr zu helfen."


n "Ich seufze."


n "Es fühlt sich an, als würde sich die Kluft zwischen mir und Rin nur noch weiten."


n "Aus ihr wird etwas Großes werden, während ich mich immer noch fühle, als würde nicht weiterkommen – ungeachtet des Versprechens an mich selbst, etwas aus meinem Leben zu machen."


n "Damit nicht genug. Wir hatten diesen Streit, und je länger wir uns gegenseitig ignorieren, desto schwieriger heilen die Wunden."


n "Falls es das überhaupt ist, was wir wollen. Ich habe nie herausgefunden, was Rin fühlte, und jetzt bin ich mir nicht einmal mehr darüber im Klaren, was ich selbst fühle."


n "Ich wünschte, ich könnte sie verstehen. Doch Rin ist nicht gerade leicht zu lesen."


n "Ich denke nicht, dass sie etwas verbirgt, aber sie scheint meinen Versuchen, zu verstehen, was sie von sich gibt, erfolgreich Widerstand zu leisten."


$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

show sae smile onlayer master
with charachange

window show

sa "Liegt dir etwas auf dem Herzen?"


"Ich begreife, dass ich für wer weiß wie lange gedankenverloren in der Mitte der Galerie gestanden habe."


hi "Ahh… nichts Besonderes…"


"Um sie abzulenken, tue ich so, als würde ich die Gemälde an der Wand vor mir studieren."


$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
play music music_another fadein 0.5

scene rin_exhibition_c onlayer master:
    truecenter
    zoom 1.0 subpixel True
    ease 30.0 zoom 1.1
with locationchange

"Ich habe es schon einmal gesehen."


"Diese nun allzu vertrauten Farbstriche, die sich scheinbar wahllos ineinander schlängeln, verschmelzen und es dabei trotzdem noch schaffen, den den Eindruck zu erwecken, dass etwas hinter den Kulissen geschieht. Sozusagen."


"Rins Stil ist genau wie sie selbst. Abstrakt, unbegreiflich, farbenfroh."


"Mysteriös."


"Muss man ein Künstler sein, um einen Künstler zu verstehen?"


$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg gallery_int onlayer master
with locationchange

hi "Ähm… Ich habe vielleicht doch eine Frage."


show sae smile onlayer master at center
with charaenter

sa "Oh?"


"Sie sieht von dem Magazin auf, welches sie träge durchgeblättert hat. Scheinbar freut sie mein unerwartetes Interesse."


hi "Wie interpretiert man Kunst?"


show sae doubt onlayer master
with charachange

sa "Was meinst du?"


"Ihre Augenbrauen heben sich fragend, als ob die Frage zu kompliziert wäre, um ohne genauere Erklärung beantwortet werden zu können."


hi "Entschuldigung, falls ich etwas Dummes gefragt habe."


hi "Ich glaube nicht, dass ich Kunst verstehe, wie es die Profis tun."


show sae smile onlayer master
with charachange

sa "Oh, dafür gibt es keine Tricks."


"Sae winkt meine Frage mit einer simplen doch effizienten Bewegung ihres Handgelenks ab."


show sae neutral onlayer master
with charachange

sa "Jeder interpretiert Kunst wie er will. Und Interpretation liegt genauso im Auge des Betrachters wie in dem des Erschaffers."


sa "„Profis” haben ihre eigene Methode, weil es so etwas wie Kunsttheorie gibt."


sa "In der Kunst gibt es Muster, genau wie in allem. Wir nehmen an, dass es möglich ist, aus der Betrachtung dieser Muster Schlüsse zu ziehen."


"Ihre Stimme ist wie die einer Lehrerin, die bei ihren Erklärungen zufällige Wörter betont, um die Aufmerksamkeit ihrer Zuhörer zu behalten."


show sae smile onlayer master
with charachange

sa "Ich denke, am Ende ist es recht bedeutungslos."


"Sie scheint fast mit sich selbst zu reden, ist aber dabei laut genug, dass ich sie klar verstehen kann."


sa "Eine gutes Kunstwerk wird dich etwas fühlen lassen. Das ist auch schon alles."


sa "Gefühle ändern und beeinflussen die Kunst, die wir erschaffen und die Kunst, die wir sehen."


hi "Aber…"


show sae neutral onlayer master
with charachange

sa "Ich erzähle dir eine Geschichte."


hi "Müssen Sie das? Die letzte war deprimierend…"


sa "Sie ist wichtig. Hör zu…"


sa "Vor ungefähr hundert Jahren erreichte einen kaum bekannten Maler die Nachricht, dass sein Freund – ein Mann namens Casagemas – Selbstmord begangen hatte."



sa "Dies geschah, während er fort war und seinen Freund für eine Weile nicht gesehen hatte."


sa "Darum muss ihn das offensichtlich härter getroffen haben, als wenn er es unter normalen Umständen gehört hätte."


sa "Danach hat unser Hauptcharakter für vier Jahre nichts anderes als einfarbige Gemälde gemalt, weil er von dieser Nachricht so sehr betroffen war."


sa "Was immer er auch tat, er sprang immer wieder auf die gleiche Farbe zurück, bis sein Schmerz nachließ."


"Sie macht eine kleine Pause, um zu überprüfen, ob ich ihr noch folge."


"Das tue ich – teilweise. Darum gebe ich ihr das Stichwort, für das Geschichtenerzähler zu leben scheinen."


hi "Also…"


"Es ist schwierig von dort aus weiterzumachen, da mir die Frage, die sie hören will, anscheinend nicht einfällt."


"Wie ein Möchtegern-Sokrates dachte sie, sie hätte alle Werkzeuge der Offenbarung vor mir auslegt."


show sae doubt onlayer master
with charachange

sa "Bist du noch nicht drauf gekommen?"


"Nur dass ihr Schüler sich als zu beschränkt herausstellt, um es zu kapieren."


show sae scowl onlayer master
with charachange

"Sie sieht aus, als wäre sie unzufrieden mit meiner Schwerfälligkeit."


sa "Picassos Blaue Periode ist eine der am höchsten gepriesenen der Kunstgeschichte, aber wer weiß, was er gefühlt hat, als er an diesen Meisterwerken gearbeitet hat?"


sa "Trauer? Sehnsucht? Bedauern?"


sa "Niemand weiß es."


sa "Wenn du nun eines seiner Gemälde aus der Blauen Periode siehst, wirst du es nun wahrscheinlich anders interpretieren, als du es getan hättest, bevor ich dir über Picassos Freund Casagemas erzählt habe."


show sae neutral onlayer master
with charachange

sa "Kunst zu erfahren ist etwas Persönliches – nur interaktiv durch Zufälle oder Umstände."


sa "Es gibt für jedes Kunstwerk Millionen von Erklärungen, doch es könnte sein, dass keine von ihnen die Gedanken des Erschaffers widerspiegelt."


show sae smile onlayer master
with charachange

sa "Niemand ist eine Insel, weißt du?"


"Ich nicke, ohne zu verstehen, was die letzte Anmerkung bedeutet hat."


"Ansonsten hat alles Sinn ergeben – außer einer Sache."


"Falls Kunst – wie Rin sagte – Kommunikation ist, aber laut Sae jeder in seiner eigenen Geheimsprache spricht, wie kann irgendjemand dann je auf Kommunikation hoffen?"


"Es scheint so vergeblich… und sinnlos."


"Kunst ist wirklich nichts für mich."


$ renpy.music.set_volume(0.1, 1.0, channel="ambient")

scene bg gallery_exhibition onlayer master
with locationchange

"Sae wendet sich wieder ihrem Kunstmagazin zu. Ich laufe eine Runde durch die Galerie und versuche zu erkennen, was Rin in ihren eigenen Gemälden sehen kann."


"Eine beruhigende Stimmung erfüllt die vom Regensturm eingehüllt Galerie. Durch die großen Fenster und ihre unsichtbare Abgrenzung wirkt es sogar noch gemütlicher."


play sound sfx_storebell
stop music fadeout 2.0

"Ein Klingeln der Glocke unterbricht die friedliche Atmosphäre."


$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg gallery_int onlayer master
with locationchange

show rin relaxed_nonchalant onlayer master at center
with charaenter

"Rin schiebt die Tür mit ihrer Schulter auf und tritt ein."


"Ich hatte fast vergessen, dass sie der Grund war, weswegen ich überhaupt zur Galerie gekommen bin."


show rin relaxed_boredom onlayer master
with charachange

rin "Ich denke, ich bin bereit—{w=0.3}{nw}"


show rin relaxed_surprised onlayer master
with charachange

"Als sie meine Anwesenheit bemerkt, bricht sie mitten im Satz ab."


"Die Totenstille hält für genau eineinhalb Sekunden an. Nicht genug für mich oder Sae, um unsere Münder zu öffnen, doch genug für Rin, um zu reagieren."


show rin negative_annoyed onlayer master
with charachange

rin "Ich gehe spazieren."


hide rin onlayer master
with charaexit

play sound sfx_storebell

"Als sie sich mit einem selbst für sie untypisch gewagten Laufschritt auf nach draußen macht, scheint Rin zu vergessen, dass es immer noch regnet."


show rain normal behind bg onlayer master

"Ohne lange darüber nachzudenken, greife ich meinen Regenschirm und eile ihr hinterher."


play sound sfx_storebell
$ renpy.music.set_volume(1.0, 2.0, channel="ambient")

hide bg onlayer master
show bg city_street4_rn as bg2 behind rain onlayer master
show rin negative_spaciness_close_rn onlayer master
with locationskip

"Ich erwische Rin hinter der Ecke, öffne meinen Regenschirm und hebe ihn über uns beide. Dabei muss ich fast rennen, um mit ihr mitzuhalten."


"Sie protestiert nicht gegen mein Hinterherrennen oder den Schutz meines Regenschirms. Schließlich bremst sie ihren Laufschritt, sodass ich mit ihr mithalten kann, ohne mich selbst zu überanstrengen."


"Ich erhole mich von der Hektik und beurteile die Situation."


"Das letzte Mal, als ich meinen Regenschirm schützend über uns beide gehalten habe, habe ich auch nicht allzu lange darüber nachgedacht."


"Doch nun sammeln sich all die Dinge, die seitdem geschehen sind, in einem eiskalten Ball in meiner Magengrube."


"Ihr so nahe zu sein macht mich unbehaglich, und ich spüre, dass ich etwas aufgeregt werde."


"Es ist schwierig, Worte aus meinen Mund zu bekommen, da er sich plötzlich sehr, sehr trocken anfühlt."


"Dennoch kann ich keinen Rückzieher machen."


hi "Warum rennst du andauernd weg?"


show rin negative_annoyed_close_rn onlayer master
with charachange

rin "Ich will nicht mit dir reden."


hi "Ich will aber mit dir reden."


show rin negative_confused_close_rn onlayer master
with charachange

rin "Jedes Mal tut es weh."


hi "Manchmal ist es eben so."


show rin negative_sad_close_rn onlayer master
with charachange

rin "Es soll nicht wehtun."


hi "Na gut. Wir müssen ja nicht reden."


show rin relaxed_doubt_close_rn onlayer master
with charachange

rin "Was sollen wir sonst tun?"


hi "Lass uns einfach weiterlaufen."


show rin relaxed_surprised_close_rn onlayer master
with charachange

rin "Nur laufen?"


hi "Nur laufen."


show rin basic_absent_close_rn onlayer master
with charachange

rin "Okay."



label de_R37:

play music music_dreamy fadein 2.0
$ renpy.music.set_volume(1.0, 2.0, channel="ambient")
$ renpy.music.play(sfx_rain, fadein=2.0, if_changed=True, channel="ambient")

play sound sfx_whiteout

scene white onlayer master
with Dissolve(1.0)

show rain normal behind white onlayer master
with None

hide white onlayer master
show ev rin_rain_away_close behind rain onlayer master at Fullpan(20.0,dir="up")
with Dissolve(1.0)

"Ein Platschen geht mit unseren Schritten einher, während wir im Regen durch die seichten Pfützen der Straßen laufen."


"Rin, die nun auf ihre gemütliche und entspannte Weise neben mir läuft, scheint die Tatsache, dass sie unnötigerweise Nass wird, kein bisschen zu stören."


"Sie steht teilweise außerhalb des schützenden Regenschirms, obwohl er mehr als groß genug für uns beide ist."


"Es ist, als würde sie nicht einmal bemerken, dass der Regen ihr Hemd durchnässt."


"…"


"Rins Auftreten ruft stets die Vorstellung eine meditativen Ruhe hervor, auch wenn sie innerlich in Aufruhr sein mag."


"Doch ich glaube nicht, dass das Meditation ist. Das ist nur klatschnass werden."


"Ich wünschte, ich könnte auch gelassener sein."


"Ich bin Rin zu nahe gekommen, als dass ich meine übliche Distanziertheit beibehalten könnte."


"Es kommt mir vor, als wäre ich zu einem dieser Menschen geworden, die sich selbst einreden, sie seien objektiv – nur um herauszufinden, dass sie die miesesten Lügner sind."


"Illusionen, um uns selbst zu täuschen – wie kann man jemanden besser dazu bringen, sich für einen guten Menschen zu halten?"


"Vielleicht ist es besser, diese Illusion zu verwerfen."


show ev rin_rain_away_close onlayer master at Position(yalign=0.0)
show ovl rin_rain_hisaotowards_close behind rain onlayer master at Position(xalign=1.0, yalign=0.0)
with charachange

hi "Ich fahre morgen für eine Weile nach Hause, darum dachte ich mir, ich besuche dich davor noch mal."


"Mir hätte ein besserer Gesprächseinstieg einfallen können, aber Rins Abwehrhaltung erschwert mir das."


rin "Das ist gut. Sonst hätte ich vielleicht gedacht, du wärst entführt worden."


hi "Du kannst nicht weiter vor allem wegrennen. Nicht mal vor einem ernsten Gespräch mit mir."


rin "Ich meine immer alles ernst. Außerdem scheine ich gerade sehr langsam zu rennen."


rin "Vielleicht sollte ich Unterricht bei Emi nehmen."


"Es bringt nichts. Als ob man gegen eine Wand redet, die wahllos sarkastischen Nonsens erwidert."


hi "Denk mal an deine Ausstellungseröffnung. Was, wenn du weggerannt wärst?"


"Rin antwortet darauf nicht und geht lediglich weiter – oder sie „rennt langsam”. Und sie flüchtet sich vor mir in ihr Schweigen."


"Mir ist aufgefallen, dass sie eine Gabe dafür hat, in Gesellschaft allein zu sein."


show bg city_street3_rn behind rain onlayer master
hide ev onlayer master
hide ovl onlayer master
with locationchange

"Wir laufen die Straße hinunter, biegen dann links ab, dann dreimal nach rechts und dann wieder links."


"Es ist wie die Nacht vor einiger Zeit. Wir schlagen wahllos Richtungen ein, weil es egal ist, wo wir hingehen."



"Alles, was zählt, ist das Laufen und der Klang der Regentropfen, die auf meinen Schirm prasseln."


"Wasser strömt von den Dächern der Gebäude herab und fließt in breiten Flüssen in die Abwasserkanäle."


"Auch wenn ich versuche, über sie zu steigen, werden meine Füße durch meine Schuhe hindurch nass."


"Wir laufen weiter in einer Stille, die darum fleht, gebrochen zu werden. Allerdings bin ich mir sicher, dass ich der Einzige bin, der so fühlt."


hide bg onlayer master
show ev rin_rain_away behind rain onlayer master
show ovl rin_rain_hisaotowards behind rain at Position(xalign=1.0, yalign=0.0) onlayer master
with locationchange

hi "Warum hast du die Ausstellung gemacht?"


"Rin zuckt einfach mürrisch mit den Schulter und schaut in die andere Richtung. In diesem Moment gebe ich auf."


window hide

hide ovl onlayer master
with charachange

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl clear
nvl show dissolve

n "\n\n\nEs ist zwecklos."


n "\nWas wollte sie erreichen? Was sie am Abend der Eröffnung sagte, ließ mich spüren, dass da etwas… etwas Besonderes war, was sie wollte."


n "Es kam mir vor, als hoffte Rin auf etwas Unerreichbares."


n "Sie setzte die Latte in ihrem Kopf hoch und scheiterte, egal wie sehr den Leuten ihre Arbeit gefiel."


n "Ein wenig Realitätsverlust ist normal; den meisten Menschen geht das so, wenn auch nicht so extrem wie Rin."


n "\nAber das ist kein Grund, in seiner eigenen Welt zu leben und keine Besucher zu empfangen."


nvl clear

n "\n\n\nMan kann die Welt nicht zu seinem eigenen verzerrten, größenwahnsinnigen Kosmos machen, in dem alles so läuft, wie man es will."


n "\nDas frustriert mich am meisten bei Rin."


n "\nSie will, dass die Welt nach ihren Regeln spielt und betrachtet alles, was damit in Konflikt steht, als unbedeutend oder unnötig."


n "Ich kann nicht glauben, wie jemand aus Yamaku nicht ansatzweise verstehen kann, dass die Welt manchmal sehr ungerecht sein kann."


n "Ich bin mir sicher, dass sich noch viele andere wünschen, dass manche Dinge anders wären, aber die können wenigstens den Tatsachen ins Augen sehen."


$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

hide ev onlayer master
show bg city_street4_rn behind rain onlayer master
show rin negative_spaciness_close_rn onlayer master at center
with locationchange

window show

"Ich werfe einen seitlichen Blick auf Rin, die zu unserem kuppelförmigen Schutz hinaufsieht. Mit seiner monotonen Schwärze ist er ein dürftiger Ersatz für den echten Himmel."


"Der Regen fällt unablässig weiter."


"Genau wie die heutigen Wolken macht Rin nicht wirklich den Eindruck, als wollte sie angesehen werden."


"Sie schmollt in Einklang mit dem Himmel, den sie so liebt."


"Ich hätte nicht kommen sollen. Ihre Anwesenheit erinnert mich nur daran, wie wütend ich genau aus diesen Gründen geworden bin. Und dass sich diese Gründe wahrscheinlich niemals ändern werden."


"Auch wenn ich sagen will, dass es mir leid tut; auch wenn ich nicht will, dass wir auseinandergehen, ich kann mich nicht dazu überwinden, es ihr zu sagen."


show bg misc_sky_rn onlayer master
hide rin onlayer master
with locationchange

"Schritt für Schritt gehen wir weiter durch die vom Regen getränkten Straßen."


"Wenn man mit jemand anderen zusammen läuft, kommt es oft vor, dass die Schritte sich aufeinander abstimmten, als gäbe es irgendeinen komischen unterbewussten Pakt."


"Mir ist aufgefallen, dass unsere es nie tun."


window hide

stop music fadeout 5.0
$ renpy.music.set_volume(0.3, 3.0, channel="ambient")

show bg misc_sky_rays onlayer master
show rain light onlayer master
with Dissolve(3.0)

window show

"Die Zeit vergeht. Das Prasseln auf meinem Regenschirm wird schwächer, als sich die Wolken über uns langsam auflösen und das Blau des Himmels enthüllen."


show rain light onlayer master:
    alpha 1.0
    linear 5.0 alpha 0.0
with None

stop ambient fadeout 9.0

"Schließlich lässt der Regen genug nach, dass ich verbleibenden Wassertropfen abschütteln und den Schirm schließen kann."


"Während ich mit dem Mechanismus ringe, hält Rin so plötzlich an, dass ich noch ein paar Schritte weiterlaufe, bevor ich bemerke, dass sie nicht mehr neben mir ist."


"Der blöde Regenschirm scheint blockiert zu sein."


play music music_innocence fadein 6.0

scene ev rin_trueend_normal onlayer master:
    truecenter
    zoom 1.2 rotate -6 subpixel True
    easein 6.0 zoom 1.0 rotate 0
with locationchange

"Als ich mich umdrehe, sehe ich, wie sie mich mit einem teilnahmslosen Gesicht anstarrt."


rin "Ich wollte, dass jemand „Ich weiß, wie du dich fühlst.” zu mir sagt."


rin "Wäre das nicht toll?"


"Ist das eine Antwort auf die Frage von vorhin? Ich bin mir nicht sicher."


hi "Ja… aber warum ist das so wichtig?"


scene ev rin_trueend_sad onlayer master:
    truecenter
    zoom 1.0 rotate 0 subpixel False
with locationchange

rin "Weil ich andernfalls nicht weiß… ob ich das ertragen kann."


"Ich war immer noch dabei, mit meinem Regenschirm zu kämpfen, daher habe ich einfach irgendetwas geantwortet, um die Unterhaltung am Laufen zu halten. Doch was Rin als nächstes sagt, lässt mein Blut gefrieren."


scene ev rin_trueend_closed onlayer master
with locationchange

rin "Wenn jemand einen Witz macht und lacht, lachst du mit ihm, oder? Denn doppelte Freude ist dreifache Freude, oder?"



scene ev rin_trueend_smile onlayer master
with locationchange

rin "Wenn jemand verletzt und traurig ist, tröstet und umarmt man ihn, oder? Denn so—"


rin "…"


"Sie hält mit halboffenem Mund inne. Dann erinnert sie sich wieder daran, ihn zu schließen."


scene ev rin_trueend_normal onlayer master
with locationchange

"Düsterkeit wandert in ihr Gesicht und gleichzeitig in mein Herz."


rin "Ich weiß nicht, warum nie die richtigen Worte rauskommen."


rin "Ich weiß nicht, warum ich nur lachen kann, wenn ich mich selbst dazu bringe."


rin "Ich weiß nicht, warum alles bloß in mir bleibt, selbst wenn es sich anfühlt, als würde ich explodieren."


"Ihr mattes, ausdrucksloses Gesicht bleibt sogar regungslos, als sie das sagt."


"Ihr sonst beständige Stimme wird nur etwas leiser als sonst."


rin "Aber wer… wer würde sich je so fühlen wollen?"


"Rin sieht mich an, und ich bilde mir ein, Traurigkeit in ihren Augen zu sehen, ob sie nur wirklich da ist oder nicht."


rin "Ich nicht."


rin "Ich will mich nicht so fühlen."


"Danach schweigen wir für eine kurze Weile."


"Rin, weil sie alles, was sie sagen wollte, auf einmal gesagt hat. Ich, weil ich keine Ahnung habe, wie ich mit dem Gesagten umgehen soll."


"Ich verstehe nicht, was Rin meint – oder vielleicht tue ich es und will es nur nicht wahrhaben."


"Beides passiert zum ersten Mal, und dann muss es auch noch gleichzeitig sein."


"Die Ironie entgeht mir nicht."


hi "Ich… denke, jeder will verstanden werden. Das ist allgemeingültig."


hi "Aber… das ist unmöglich. Nicht nur für mich, sondern für jeden."


hi "Sae hat das auch gesagt."


hi "Man beeinflusst andere Menschen, genauso wie sie dich beeinflussen. Doch am Ende kann man nur durch seine eigenen Augen sehen."


hi "Alle Menschen… sind allein. Wir benutzen einander nur, um die diese Einsamkeit zu lindern."


"Ich frage mich, warum ich es so formuliert habe. Was Sae gesagt hat, klang einfach glaubwürdig – als ob ich die ganze Zeit schon so gedacht hatte, ohne es zu wissen."


"Es kommt mir so vor, als hätte sie meine Gedanken in klare, schlichte Worte gefasst – und in diese bescheuerte Geschichte über Picasso."


scene ev rin_trueend_closed onlayer master
with locationchange

"Rin lässt ihren Kopf wie eine welkende Blume hängen. Ihr Pony fällt über ihre Augen, sodass ich sie nicht mehr sehen kann."


rin "Warum sagst du das, obwohl du mich das Gegenteil hast fühlen lassen?"


rin "Es ist unfair."


"Die zitternde Stimme, die diese Worte sagt, gehört nicht zu Rin."


scene ev rin_trueend_sad onlayer master
with locationchange

rin "Ich dachte wirklich, du könntest anders sein. Dass ich nicht allein sein müsste."


"Eine bittere Stimme voller Enttäuschung, gesprochen durch zusammengebissene Zähne und eine zitternde Brust."


hi "Es tut mir leid…"


rin "Warum sagst du dann so etwas Unfaires?"


"Ihr fordernder Ton löst keine besonderen Gefühle in mir aus, abgesehen von der Trauer, die schon seit gestern Abend dagewesen ist."


"Sie schüchtert mich überhaupt nicht ein. Nicht mehr."


"Rin ist weder ein Kunstgenie noch ein unberechenbarer, idiotischer Savant, der den Logik-Lappen meines Gehirns mit jedem Wort in Stücke reißen könnte."


"Sie ist nur ein Mädchen, von dem ich dachte, dass ich sie lieben würde. Eine Geliebte, die meine Freundin sein wollte. Eine Freundin, die ich im Stich gelassen habe."


hi "Ich sage es, weil es sich sonst wie eine Lüge anfühlen würde."


scene ev rin_trueend_normal onlayer master
with locationchange

rin "Wieso?"


"Simple Fragen sind die Schwierigsten. Ich muss meine Augen schließen, damit ich meine Gedanken genug ordnen kann, um ihr zu antworten."


hi "Ich bin kein Künstler. Ich kann niemals mit dir auf einer Stufe stehen."


hi "Es gibt eine Welt, die nur du sehen kannst, und um Teil davon zu sein, müsste ich Du werden."


hi "Das kann ich nicht, egal wie sehr du es dir von mir wünschst."


"Rin nimmt meine Erklärung ohne einen Wimpernschlag entgegen."


rin "Ich bin auch keine richtige Künstlerin."


rin "Ich male nur, weil ich mich dann fühle, als könnte ich wirklich etwas fühlen."


scene ev rin_trueend_weaksmile onlayer master
with locationchange

"Sie hält ihren Atem eine Weile an, bevor sie ihn mit einem langen, seufzenden Hauch entweichen lässt."


scene ev rin_trueend_closed onlayer master
with locationchange

rin "Darum werde ich es tun."


rin "Ich hab mich entschieden. Ich werde es tun. Wenn sogar Hisao das sagt, dann werde ich es tun."



hi "Was tun?"


"Rin zeigt Anzeichen davon, dass sie wieder in Selbstgespräche versinkt, aber ich bin froh, dass ich sie sogar jetzt noch in die Realität zurückholen kann."


scene ev rin_trueend_normal onlayer master
with locationchange

rin "Herr Nomiya und Sae haben mit jemandem gesprochen, der eine sehr wichtige Person ist. Ich hab ein Stipendium für eine große Kunstschule in Tokyo bekommen."


rin "Er sagte, ich könnte dorthin wechseln und nach dem Sommer anfangen, wenn ich will."


rin "Ich verstehe nur nicht ganz warum—"


stop music fadeout 10.0

hi "Warte mal, was? Warum hast du nichts gesagt?"


scene ev rin_trueend_smile onlayer master
with locationchange

rin "Hab ich doch gerade. Du bist der Erste, dem ich es gesagt hab, weil ich mich eben erst entschieden hab."


"Sie behält ihre Gelassenheit und sieht wegen meines Einwurfs nur leicht überrascht aus."


"Es ist lächerlich, wie locker sie etwas so Lebensveränderndes sagen kann."


"Ich kann es nicht fassen. Nach dem, was im Februar passiert ist, hatte ich genug Veränderungen für dieses Jahr."


"Auch wenn die Dinge gerade schlecht laufen, will ich nicht, dass sich alles verändert."


hi "Aber was ist mit der Yamaku? Willst du nicht mit allen deinen Abschluss machen?"


"Mein Appell erzielt keine Gefühlsregung."


rin "Wen meinst du mit „allen”?"


hi "Emi, ich, alle!"


"Ich spüre, wie mein Puls beunruhigend ansteigt, und meine Atmung wird schnell und flach."


"Ich will nicht, dass das passiert."



rin "Ihr Leben ist nicht meins."


rin "Du hast gerade gesagt, dass jeder allein ist."


hi "So hab ich das nicht gemeint—"


rin "Du hast immer gesagt, dass man den Tag nutzen soll, dass man anfangen soll, sein Leben zu leben."


rin "Ich muss mein Leben auch leben."


"Rin verdreht meine Worte, um ihre erneute Flucht zu rechtfertigen. Es macht mich wütend."


"Ihre Gelassenheit, Endgültigkeit und Ernsthaftigkeit bei dieser Ankündigung ist unerträglich."


"Als ob man sein Leben mal eben aus einer Laune heraus ändern könnte! Nein!"


hi "Wir kannst du das sagen? Warum versuchst du nicht einmal dazuzugehören?"


"Meine verzweifelte Anschuldigung hat keine Wirkung. Es kommt mir vor, als wäre ich machtlos – als könnte ich nicht zu ihr durchdringen, egal mit welchen Mitteln."


"Rin ist mit ihrer Entscheidung so frustrierend bedingungslos, dass ich sie dafür hassen könnte, wenn ich sie nicht lieben würde. Auch wenn ich nicht mehr weiß, wie ich für sie empfinde."


scene ev rin_trueend_normal onlayer master
with locationchange

rin "Vielleicht bin ich diese Art von Mensch. Die Art, die für sich allein bleibt."


hi "Das akzeptiere ich nicht."


"Ihre gleichgültigen Augen scheint es nicht zu interessieren, ob ich ihre Entscheidung akzeptiere oder nicht."


"…"


"Die Pause lässt mich herunterkommen, um mein Feingefühl wiederzufinden."


"Während ich das tue, enthüllen die sich teilenden Regenwolken die Sonne, die immer noch Zeit hat, um ihre letzten paar warmen Strahlen zu scheinen, bevor sie untergeht."


"Ein Mosaik aus Licht und Schatten erstreckt sich auf den Wänden der Gebäude, den Straßen und dem Zaun, der den Park auf der anderen Seite der Straße umschließt."


"Rins Schatten ist lang genug, um meine Füße zu erreichen."


"Es ist wie in einem dieser Western, in dem zwei Cowboys versuchen, sich gegenseitig niederzustarren, und bereit sind, ihre Waffen zu ziehen."


"Der, der seine Nerven verliert, schluckt Blei."


"Ich bemerke, dass ich im Nachteil wäre, weil die Sonne hinter Rin steht und mich blendet."


scene ev rin_trueend_sad onlayer master
with locationchange

rin "Hasst du mich?"


"Sie zieht zuerst, und ich habe nichts, um zu kontern."


hi "Ich weiß es nicht."


"Habe ich verloren?"


hi "Auch wenn ich es täte, was würde es ändern?"


"Ich ringe nach Worten. Nach Worten, die das Ganze noch retten könnten."
"Ich finde keine."


hi "Du bist meine Freundin, das habe ich dir versprochen. Ich bin nicht die Art von Kerl, der Versprechen vergisst."


hi "Ich denke, das ist das Wichtigste. Wir könnten versuchen, zu—"


scene ev rin_trueend_normal onlayer master
with locationchange

rin "Sag es nicht."


scene ev rin_trueend_hug onlayer master
with locationchange

play music music_friendship fadein 4.0

"Als ob sie vorhersieht, was ich sagen will, wirft Rin sich in meine Arme und presst ihren Körper an mich."


"Ich spüre, wie sie sich auf Zehenspitzen stellt, um auf meine Höhe zu kommen und sich näher anzuschmiegen."


"Der Duft ihrer Haare ist der von Regen und Farbverdünner. Ihr Körper ist kalt wie immer. Ihr Atem an meinem Hals ist heiß wie immer."


"Lustig, wie all das sich so vertraut anfühlt, obwohl Rin als Ganzes es nicht tut."


scene ev rin_trueend_hugclosed onlayer master
with locationchange

rin "Bist du sicher, dass du mich nicht hassen kannst?"


"Rin flüstert so nah in mein Ohr, dass ich die Bewegungen ihrer Lippen an meinem Ohrläppchen spüren kann."


"Das ist Stichelei; Hohn. Wäre das eine andere Situation, bin ich mir sicher, dass es verlockend kitzeln würde, und ich würde dabei kichern – auch wenn ich ein Mann bin."


rin "Dann wäre es einfacher."


hi "Weiß nicht. Ist ziemlich schwierig, wenn du mich so umarmst."


scene ev rin_trueend_sad onlayer master
with locationchange

"Ich frage mich, ob es an meiner mürrischen Stimme liegt, aber sie macht einen Schritt zurück und schaut wehmütig auf ihre kurzen Arme."


"Ich wünschte, sie hätte das nicht getan."


rin "Ich kann niemandem umarmen, Hisao."


rin "Was das angeht bin ich ein schlechter Mensch."


scene ev rin_trueend_normal onlayer master
with locationchange

rin "Darum muss ich gehen."


"Sie entwaffnet mich vollkommen mit drei simplen Sätzen, und ich kann nichts mehr dagegenhalten."


"Und da ich es nicht kann, kann Rin weiterhin tun, was sie will, und wiegt sich vom einen Fuß auf den anderen."


scene ev rin_trueend_smile onlayer master
with locationchange

rin "Ich werde lernen, Menschen auf meine eigenen Weise zu umarmen."


rin "Ich bin sicher, dass ich eine richtige Künstlerin werden kann."


rin "Aber wenn ich das tue… könnte ich vielleicht nicht mehr ich sein."


"Der Anflug eines Lächelns auf ihren Lippen eine Lüge. Ein falsches Zeichen von Zuversichtlichkeit in eine Zukunft, die selbst Rin nicht vorhersehen kann."


"Ich würde es gerne als ein Zeichen von Hoffnung interpretieren, aber ich weiß es besser."


"Rin lächelt einfach weiter ihr unbeholfenes, gezwungenes Lächeln."


rin "Darum… vergiss mich bitte. Dann werde ich auch dich vergessen."


rin "Ich bin mir sicher, dass—{w=0.5}{nw}"


scene ev rin_trueend_sad onlayer master
with locationchange

"Ihr versagen die Worte inmitten von etwas, von dem ich glaubte, dass ich es niemals hören würde."


"Ich glaube nicht, dass ich es überhaupt hören wollte."


"Das ist nicht fair."


"Rin scherzt nicht. Rin meint alles ernst. Aber ich kann es nicht akzeptieren. Ich kann's nicht."


"Dich vergessen? Wie könnte ich das je…?"


"Das würde ich gerne sagen. Aber ich weiß nicht, wie ich danach weitermachen sollte. Mir fällt nichts Gutes ein, also muss ich sie herausfordern."


hi "Wie kannst du so etwas sagen?"


scene ev rin_trueend_normal onlayer master
with locationchange

"Rin hebt ihren Blick, um in meine Augen zu sehen. Ihre Augen sind ernst und tief – ein perfektes Abbild des unerkundeten Territoriums, für das ich sie immer gehalten habe."


"Nicht einmal jetzt kann ich aus diesen starren, jadefarbenen Augen, die nie reflektieren konnten, was sie sehen, ihre Gefühle ablesen."


rin "Es ist einfach. Immerhin bin ich gut darin, Dinge zu vergessen."


"…"


"Ihre Unfairness schnürt mir den Hals zu, doch ich schaffe es, die in meinem Kopf brennende Frage auszusprechen."


hi "Also war es das? Ist das ein Lebewohl?"


"…"


"Rin sah mich weiterhin sanft an, ohne meine Frage zu beantworten."


"In ihren Augen konnte ich sehen, dass sie nicht einmal etwas sagen musste."


"Wir hatten uns nichts mehr zu sagen."


stop music fadeout 12.0

scene ev rin_trueend_gone onlayer master
with locationchange

"Sie drehte sich um und zog davon, ohne zurückzuschauen."


"Die ganze Welt um mich herum veränderte sich. Stück für Stück, aber ich blieb wie angewurzelt zurück."


scene ev rin_trueend_gone onlayer master:
    "ev rin_trueend_gone_ni" with Dissolve(10.0)
with None

"Die Sonne fiel unter den Horizont und warf dabei lange, dünne Schatten auf die Straße."


"In dem schwindenden Licht erschien Rins sich entfernender Rücken wie aus einem fernen Traum."


"Die Kluft zwischen uns wuchs langsam."


"Die kleinen Wellen auf den Pfützen, in die sie getreten war, breiteten sich aus, bis sie die Grenzen ihres winzigen Daseins erreicht hatten und ohne eine Spur verschwanden."


"Ihre Worte blieben tief in meinem Herzen eingefroren."


window hide


label de_R38:


scene bg school_room34 onlayer master
with None

show rin negative_spaciness onlayer master
with charaenter

play music music_drama fadein 6.0

"Sie steht in der Mitte des sonnenbeschienenen Raumes und schaut durch die Lücken in den Vorhängen auf den Hof."


"Wie schon so oft zuckt oder erschrickt sie nicht, sondern wartet nur gelassen darauf, dass ich den ersten Schritt mache."


"Es ist, als würde sie versuchen, ein dauerhafter Teil der Einrichtung zu werden."


hi "Herr Nomiya sucht nach dir."


"Sie dreht den Kopf und wirft mir einen leeren Blick zu; auch ansonsten ist ihr Gesichtsausdruck nichtssagend und unergründlich."


rin "Suchst du auch nach mir?"


hi "Nee, ich hab dich doch schon gefunden, oder nicht?"


rin "Hast du?"


show rin negative_annoyed onlayer master
with charachange

"Sie runzelt die Stirn und sieht so verwirrt aus, dass es mich selbst frage, ob die Frage ernst gemeint war."


"Vielleicht war sie es."


hi "War das jetzt metaphorisch gemeint?"


show rin negative_spaciness onlayer master
with charachange

rin "Meinst du, wie Aale, Höhlen und dunkle, stürmische Nächte?"


show rin negative_sad onlayer master
with charachange

rin "Ich bin schlecht in so was."


"…"


play sound sfx_doorclose

"Die abrupt beendete Begrüßung gibt mir die Gelegenheit, die Tür hinter mir zu schließen und mich auf einen staubbedeckten Schreibtisch zu setzen."


show rin basic_absent onlayer master
with charachange

"Rin bleibt stehen, doch zumindest dreht sie sich um."


"Jedoch wünsche ich mir schnell, dass sie es nicht getan hätte, so erdrückend ist ihr erwartungsvolles Starren."


"Dies ist ihr Ort, und ich bin ein Eindringling, wenn auch ein tolerierter. Trotzdem wartet sie immer noch darauf, dass ich etwas sage."


"Wenn ich nur wüsste was."


"…"


"Die von der Sonne erleuchtete Stille drängt mich zu einer Entscheidung."


"Ich bin hergekommen, ohne wirklich darüber nachzudenken, was ich tun würde – außer Nomiyas kurze Nachricht zu übermitteln, falls Rin hier wäre."


"Sie war es, und nun weiß ich nicht, was ich sonst noch sagen will… oder was ich sonst noch sagen sollte?"


"Ich schwanke für einen Augenblick zwischen meinen zwei Möglichkeiten."


"Dass Rin aufgewühlt ist, macht mich auch unruhig. Eine überraschende Enthüllung – fast so groß wie die Erkenntnis, dass sie wirklich aufgewühlt ist."


"Wahrscheinlich kann ich sowieso nichts sagen, was ihr helfen würde, und vielleicht bin ich sogar teilweise Schuld an ihrem Zustand."


"Bedeutet das, dass ich sie einfach sich selbst überlassen sollte?"


"Sicher nicht."


hi "Also… was ist los?"


"…"


show rin relaxed_nonchalant onlayer master
with charachange

rin "Nichts."


"Sie beginnt sich wegzudrehen, als wollte sie versuchen, diese unerwünschte Unterhaltung körperlich zu verlassen."


hi "Rin, hör auf, mir auszuweichen, oder ich gehe."


show rin relaxed_boredom onlayer master
with charachange

rin "Okay."


hi "Willst du, dass ich gehe?"


show rin relaxed_doubt onlayer master
with charachange

rin "Bist du immer noch wütend?"


"Es hat uns – oder besser mich? – nur zehn Sekunden gekostet, die Unterhaltung so in den Sand zu setzen."


"Ich wünschte, ich könnte die Vergangenheit auslöschen. Oder wenn das nicht geht, sie zumindest komplett vergessen."


"In den letzten paar Monaten habe ich mir das mehr als einmal gewünscht."


hi "Lass uns das erst mal zurückstellen, okay?"


show rin basic_absent onlayer master
with charachange

rin "Wenn du meinst."


hi "Meine ich. Also… Was ist los?"


hi "Sae und Herr Nomiya waren nicht allzu glücklich darüber, dass du gestern einfach weggelaufen bist."


hi "Du hast ihnen einen ganz schönen Schlamassel hinterlassen, und ich schätze, er will eine Art Erklärung."


hi "Es war, als hättest du alles einfach weggeworfen, wofür du hart gearbeitet hast. Und ich kapiere nicht wieso."


show rin basic_deadpanupset onlayer master
with charachange

rin "Hab ich einen Fehler gemacht?"


"Ihre tonlose Antwort ist so weit von dem entfernt, was man üblicherweise als Reaktion auf meinen Vorwurf erwarten würde, dass ich mir nicht einmal sicher bin, ob sie mit mir redet."


"Keiner von uns ist, wie wir mal waren. Dieses versteifte, einengende Gefühl, das ich in letzter Zeit jedes Mal kriege, wenn ich Rin ansehe, scheint sich in ihrem eigenen Verhalten widerzuspiegeln. "


"Ich hasse es, wenn Dinge unwiderruflich schief gehen. Seit Februar habe ich sie gehasst."


"Was soll ich sagen?"


"Ihrer Frage folgt ein fesselndes, fragendes Starren, dass mich seufzen und die Stirn runzeln lässt."


"Unterhaltungen, die niemand führen will, sind die schlimmsten."


hi "Ich weiß es nicht. Ich meine, es ist nicht das Ende der Welt, aber es war wahrscheinlich ziemlich dämlich."


show rin relaxed_nonchalant onlayer master
with charachange

"Sie antwortet mit einem eigenen Seufzen, obwohl ihres nicht annähernd so schwer wie meins ist."


show rin relaxed_sleepy onlayer master
with charachange

rin "Ich konnte es einfach nicht tun."


hi "Aber… Warum? Was stimmt nicht?"


show rin negative_annoyed onlayer master
with charachange

"Eine Stille, eine gerunzelte Stirn, eine leise Stimme."


rin "Lass es gut sein, Hisao."


rin "Ich glaube nicht, dass ich es so erklären könnte, dass es Sinn ergeben würde."


"Jepp, Rin will diese Unterhaltung auch nicht. Vielleicht ist es auch besser so."


"Doch es kommt selten vor, dass sie zugibt, dass sogar sie Grenzen hat."


"Ich dachte immer, dass Rin sich gar nicht bewusst ist, dass sie sich so leicht ablenken lässt oder so oft Unsinn von sich gibt."


"…"


hi "Du erklärst {b}nie{/b} etwas auf eine Weise, in der es einen Sinn ergeben würde."


show rin basic_absent onlayer master
with charachange

rin "Niemand sonst hat mich je darum gebeten."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "Ich schätze, so ist es."


n "Aber ich wollte dich immer verstehen – herausfinden, wer du bist."


n "Das will ich immer noch; siehst du das nicht?"


n "…"


n "Ich weiß, du kannst es nicht – aber ich kann es."




n "Höre ich deswegen nicht damit auf? Es schmerzt dich genauso sehr wie mich. Es ist unwahrscheinlich, dass es einem von uns beiden etwas bringt."


n "Wir haben Dinge getan und Dinge gesagt, die nicht rückgängig gemacht werden können."


n "Es ist, als ob… unsere Nähe uns nur gegenseitig verletzen würde, aber wir machen absichtlich damit weiter."


n "Ist das nicht albern?"


n "Sogar jetzt kann ich noch sehen, dass du dich zwingst, mir zu antworten, obwohl du mir nichts schuldest."


n "Sogar wenn es schwierig ist, über solche Dinge zu reden."


n "Wieso?"


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show

hi "Warum malst du?"


show rin basic_awayabsent onlayer master
with charachange

rin "Ich… Weil ich nicht weiß, was ich sonst tun könnte."


rin "Ich habe das Gefühl, ich hätte keine Wahl… Als ob das die einzige Möglichkeit wäre."


show rin basic_sad onlayer master
with charachange

rin "Als ob nur Meloneneis am Stiel im Laden übrig ist aber man ein Eis am Stiel essen muss."


"Mal abgesehen von ihrer armseligen Metapher – sie hat kaum etwas beantwortet. Wenn überhaupt, ergibt das sogar weniger Sinn, als nichts zu wissen."


hi "Aber… Wenn du nicht malen willst…"


show rin negative_spaciness onlayer master
with charachange

rin "So meine ich das nicht. Du bist an diese Schule gekommen, obwohl du wahrscheinlich keine Herzattacke haben wolltest."


show rin negative_annoyed onlayer master
with charachange

"Sie hält inne und runzelt die Stirn, als ob etwas an dem, was sie gesagt hat, ihr nicht gefallen hat."


show rin basic_lucid onlayer master
with charachange

rin "Zumindest glaube ich, dass du keine haben wolltest."


"Auf ihre vorsichtige Ergänzung folgt eine weitere, kürzere Pause mit einem weiteren, kleineren Stirnrunzeln."


show rin basic_deadpanupset onlayer master
with charachange

rin "Hättest du gerne eine Herzattacke?"


hi "Nein, und die erste wollte ich auch nicht."


show rin basic_deadpansurprised onlayer master
with charachange

rin "Aber es geht dir gut, oder? Oder bist du deswegen immer noch traurig?"


"Rins Frage lässt mich begreifen, dass ich seit Wochen kaum über meine Krankheit nachgedacht habe."


"Abgesehen vom täglichen Einwerfen meiner Medikamente hatte ich keinen Grund, mich um mein kaputtes Herz zu sorgen – wofür ich auch dankbar bin, wirklich."


"Neue Leute kennenlernen, einen neue Schule, eine neue Umgebung… ein neues Leben. All das hat mich eingenommen und meine Vergangenheit verblassen lassen."


hi "Nein… Hah, ich schätze, ich kann nicht ewig an meiner Vergangenheit festhalten."


show rin basic_awayabsent onlayer master
with charachange

rin "Siehst du? Sogar Wassermelonen schmecken nicht wirklich schlecht, wenn man sie essen muss."


"Ihr halb-unsinniger Abschluss scheint das Thema für Rin zu beenden, daher nicke ich einfach als vage Bestätigung."


"…"


"…"


"Es gibt zwei Arten von Stille: Die peinliche, die man brechen will, und die angenehme, die einen nicht stört."


"Die Erste ist schlecht, weil sie deine Gedanken durcheinanderbringt. So wie meine jetzt."


"Rin anzusehen gibt mir ein ungutes Gefühl."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\nIch will mich nicht so fühlen."


n "Rin anzusehen… laugt mich aus. Ich habe wirklich mein Bestes gegeben, sie hat versucht, zu… Ich habe keine Ahnung."


n "Doch nun stehen wir hier, und sie hat ihre Ausstellungseröffnung vergeigt."


n "Es kommt mir vor, als wären wir in einer Sackgasse."


n "Es gibt keine Richtung, in die wir gehen können."


n "Gestern habe ich versucht, zu ihr durchzudringen. Ich hatte befürchtet, es könnte meine letzte Chance sein."


n "Sie ging weg."


n "„Ich will ich sein.” Was zur Hölle heißt das überhaupt? Rin ist definitiv sie selbst. Wenn nicht sie, wer dann?"




n "Ich bin irgendwie erleichtert, dass ich nicht der Schuldige bin, aber es nagt immer noch an mir: Warum ist sie weggelaufen? Es hat gestern keinen Sinn ergeben. Und heute tut es das auch nicht."




n "Die Dinge, die sie gesagt hat, fühlen sich an, als sollten sie Sinn ergeben. Doch sie tun es einfach nicht. Nicht für mich."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show

hi "Weißt du, wegen dem, was du gerade gesagt hast…"


show rin basic_absent onlayer master
with charachange

rin "Was davon?"


hi "Ähm… Das Malen… Sae hat mir mal etwas gesagt… Dass ein wahrer Künstler nicht malt, weil er will, sonder weil er {b}muss{/b}."


hi "Ich habe mich darüber gewundert. Warum {b}müssen{/b} Künstler malen?"


"Meine Frage ist bestimmt ziemlich bescheuert. Zumindest scheint Rins blankes Starren mir das zu vermitteln."


show rin basic_deadpannormal onlayer master
with charachange

rin "Ich weiß nicht. Bin ich eine Künstlerin?"


hi "Na ja, du malst, und du hast auch eine Ausstellung. Ich würde sagen, du bist qualifiziert."


show rin basic_deadpancontemplation onlayer master
with charachange

rin "Ich glaube, ich weiß es immer noch nicht, aber okay."


"Die darauf folgende Denkpause scheint eine halbe Ewigkeit zu dauern."


"Anders als die meisten Menschen schmückt Rin ihre Denkpausen nicht mit Körpersprache aus, oder indem sie „ähm” oder „na ja” oder so etwas sagt."


"Mir ist aufgefallen, dass ich ihre Art vielleicht bevorzuge."
"Die gängige Art nervt mich sogar: Es ist, als wären die Leute so vernarrt in ihre eigene Stimme, dass sie einfach irgendein Geräusch machen müssen, auch wenn sie nur darüber nachdenken, was sie als nächstes sagen könnten."


"Rin… kommt zum völligen Stillstand, während sie nachdenkt. Es ist verwirrend, weil es immer schwierig ist, auf Leute zu reagieren, die geistig weggetreten sind, aber dafür kommt sie weniger anstößig rüber."


show rin basic_lucid onlayer master
with charachange

rin "Ich glaube, ich will, dass jemand sieht, was in mir ist. Nicht so wie Ärzte oder Serienkiller."


show rin basic_absent onlayer master
with charachange

rin "Damit ich mich nicht einsam fühle."


show rin relaxed_boredom onlayer master
with charachange

rin "So was nennt man eine Metapher, weißt du."


hi "Bitte belehr mich nicht über selbstverständliche Dinge."


show rin basic_deadpansurprised onlayer master
with charachange

rin "Es ist nicht selbstverständlich, dass es selbstverständlich ist."


hi "Also präsentierst du jemanden ein Gemälde und erwartest von ihm, dass er auf magische Weise in deine Seele schauen kann?"


show rin negative_angry onlayer master
with charachange

rin "So ist es nicht. So ist es ein bisschen, aber nicht wirklich. Verstehst du nicht?"


hi "Schon… aber auch nicht ganz."


hi "Weißt du, jedes Mal, wenn du mir diese Frage stellst, spüre ich ein kleines bisschen Verzweiflung."


show rin basic_absent onlayer master
with charachange

rin "Welche Frage?"


hi "Ob ich dich verstehe oder nicht."


"Sie scheint von meiner Klarstellung fast überrascht."


show rin basic_lucid onlayer master
with charachange

rin "Oh, das ist keine richtige Frage. Es ist eine von denen, die man nicht beantworten muss."


hi "Rhetorisch."


show rin basic_absent onlayer master
with charachange

rin "Genau, das ist das Wort. Eine Frage, die keine Frage ist, ist eine rhetorische Frage. Wie schön."


rin "Da fällt mir ein, es ergibt nicht wirklich Sinn. Was für eine Frage ist eine, die keine Frage ist?"


hi "Ein Rhetorische."


rin "Was für eine Antwort ist eine, die nichts beantwortet?"


hi "Ist das eine rhetorische Frage?"


show rin basic_deadpanupset onlayer master
with charachange

rin "Du bist nicht witzig."


show rin basic_awayabsent onlayer master
with charachange

rin "Aber wenn sie dir nicht gefällt, soll ich dann stattdessen eine andere stellen?"


show rin basic_lucid onlayer master
with charachange

rin "Allerdings kenne ich keine Guten. Wie wär's mit… „Deine Hose brennt?”"


show rin basic_absent onlayer master
with charachange

rin "Das könnte unsere Geheimsprache sein."


"Rins Albernheit – doppelt so lächerlich durch die Tatsache, dass ich weiß, dass sie es todernst meint – wirft mich wie immer aus der Bahn."


"Sie ist wie eine Art Sicherheitsschloss, das mich davor bewahren soll, zu sehr zum Schwarzseher zu werden. Sie holt meine Gedanken wieder auf den Boden, wo sie hingehören."


"Sie lässt mich verwirrt lächeln – jedoch nur innerlich."


"Auch wenn meine Mundwinkel sich nicht zu einem Grinsen verziehen, bin ich immer noch davon beeindruckt, wie locker sie all meine Versuche, ernst zu sein, ruiniert."


"Könnte sie – wenn sie es wollte – Dinge, die sie plagen und quälen, vergessen und ignorieren?"


"Könnte sie – wenn sie es wollte – frei von der Last sein, die es bedeutet, sie zu sein?"


"Oder bin ich der Einzige, dem es schwer fällt, er selbst zu sein?"


hi "Nein danke."


hi "Aber trotzdem… Die Zeiten, in denen ich das Gefühl habe, mir dir auf einer Wellenlänge zu sein, sind ziemlich selten."


hi "Es fühlt sich an… als gäbe es diese riesige Kluft. Und manchmal gehst du einfach auf die andere Seite, und dann… habe ich keine Möglichkeit mehr, dich von hier aus zu erreichen."


hi "Als ob du hin und wieder ganz woanders bist."


hi "Obwohl du genau hier bist."


"Genau so ist es."


"Da ist eine unüberwindliche Grenze. Eine imaginäre Glaswand, die verhindert, dass wir uns verstehen."


"Es könnte so eine Kluft zwischen allen Menschen geben, doch bei Rin fühlt sie sich noch greifbarer an."


"Rin reagiert nicht auf meine Gedanken. Weder auf die laut ausgesprochenen noch auf die gedachten."


hi "Mit Kunst ist es noch schlimmer."


hi "Ich bin nicht sehr gut darin, das gebe ich zu."


hi "Ich bin dem Kunstklub beigetreten, weil ich dachte, es könnte interessant sein."


hi "Und das war es auch wohl. Ich mag Kunst, ich mag auch deine Kunst, aber genauso wie dich kann ich sie nicht verstehen."


hi "Und ich bin mir ziemlich sicher, dass das niemand wirklich kann."


show rin relaxed_doubt onlayer master
with charachange

"Anscheinend beunruhigt sie das etwas."


rin "Meinst du?"


hi "Ja. Ich schätze, Kunst soll interpretiert und nicht verstanden werden. So würde ich es sagen."


show rin relaxed_sleepy onlayer master
with charachange

rin "Ein trauriger Gedanke."


hi "Ich schätze, es fühlt sich vielleicht wie einer an."


hi "Macht es dich selbst traurig?"


show rin basic_lucid onlayer master
with charachange

"Rin denkt eine Weile darüber nach. Dann schüttelt sie überraschend vehement den Kopf."


show rin basic_deadpannormal onlayer master
with charachange

"Das Erste, worauf sie ihre Augen danach richtet, bin ich."


"Beides freut und erleichtert mich."


hi "Das ist doch gut, oder nicht? Jedenfalls solltest du Herrn Nomiya suchen und dich ordentlich entschuldigen."


hi "Ich denke, er macht sich Sorgen um dich."


hi "Kannst du das tun?"


show rin basic_absent onlayer master
with charachange

"Dieses Mal nickt sie."


stop music fadeout 4.0

"Aber nicht ganz so vehement."


label de_R39:

scene bg school_hallway3 onlayer master
with locationchange

"Der Korridor ist so leer, dass er fast bedrohlich wirkt."


"Nomiyas „Büro” ist der Kunstraum am anderen Ende des Korridors im dritten Stock."


show rin basic_absent onlayer master at center
with charaenter

"Unsere Schritte sind verstörend laut. Die Atmosphäre ist anders als an einem normalen Nachmittag. Es fühlt sich auch an, als wüsste die Schule, dass für einen Monat niemand herkommen wird."


"Die Tür ist offen, doch sie sieht nicht sehr einladend aus."


hi "Ich werde… ähm… draußen warten."


show rin relaxed_nonchalant onlayer master
with charachange

with Pause(0.2)

show rin invis onlayer master at tworight
with dissolvecharamove

hide rin onlayer master
with None

"Nach einem kaum merklichen Nicken schreitet Rin ohne anzuhalten, und natürlich ohne zu klopfen, durch die Tür."


"Vielleicht dauert es deswegen ein paar Sekunden, bis ich die Herrn Nomiyas Stimme aus dem Inneren höre."


no "Da bist du ja!"


rin "Hallo."


"Ein Streit bahnt sich an – sollte ich hierbleiben oder woanders hingehen?"


"Ich bin mir nicht sicher, ob ich sie überhaupt belauschen will."


"…"


show bg school_hallway3 onlayer master at right
with charamove

"Manieren unterliegen der Neugier, darum bleibe ich nah genug, um ihnen zuzuhören."


"Ihr Stimmen hallen zwar durch den Korridor, aber das ist egal."


"Es ist niemand hier außer mir."


play music music_tragic fadein 8.0

no "Liebes Mädchen, was in aller Welt hast du dir nur dabei gedacht, an deinem großen Abend einfach so zu gehen?"


rin "Ich konnte nichts sagen."


"Verglichen mit Nomiyas schimpfendem Ton klingt Rin furchtbar leise und zurückgezogen."


"Ihre Worte scheinen unter seinen zu versinken."


no "Ich muss sagen, dass ich sehr enttäuscht von dir bin, Tezuka."


rin "Es hat überhaupt nichts gebracht."


no "Vergiss all die Dinge, die ich für dich getan habe – aber was ist mit Sae? Was ist mit allen den Gästen, die dich treffen wollten?"


rin "Niemand war da. Sogar Hisao…"


no "Du hast uns zutiefst beschämt, Tezuka."


no "Reputation ist, was zählt. Das weiß du sicherlich, oder?"


rin "Schon okay. Das brauche ich nicht."


no "„Brauchst du nicht!” Was glaubst du schon zu wissen?"


"Rins Antworten scheinen ihn nur noch mehr aufzuwühlen. Seine Stimme wird mit jedem Satz lauter."


no "Der Weg eines Künstlers ist steinig, das kann ich dir versichern! Steinig!"


no "Du musst das große Ganze sehen! Es wird gute und schlechte Zeiten geben!"


rin "Die Dinge sind, wie sie sind. Es wird schon gut gehen, auch wenn—"


no "Du magst jetzt vielleicht denken, dass alles ach so wunderbar und einfach ist, aber wie weit wärst du ohne mich gekommen?"


no "Ich werde nicht immer für dich da sein!"


no "Wenn du auf dem Boden deines mickrigen Zimmers liegst, mit deiner Miete drei Wochen in Verzug bist und seit vier Wochen keine Inspiration hattest – dann wirst du dir wünschen, dass du etwas mehr auf den alten Nomiya gehört hättest."


no "Wenn du weiterhin misst, wie der Schatten deines Stuhles über den Frühling länger wird, weil das alles ist, was deine Trägheit erlaubt – vielleicht wirst du dann anfangen, dich um deine Karriere zu kümmern."


rin "Das ist egal."


no "Du bist nicht entschlossen genug."


rin "Ich bin kein entschlossener Mensch."


no "Du bist kein entschlossener Mensch…"


play sound sfx_impact2
with vpunch

no "Dann verrat mir, warum… warum… WARUM HABEN WIR ALL DIESEN ÄRGER AUF UNS GENOMMEN, WENN ES NICHTS ALS EINEN FLIEGENSCHISS GEBRACHT HAT?"


"Oh Junge, dem Lehrer ist eine Sicherung durchgebrannt."


"Als ich höre, wie er Rin anschreit, kriege ich ein schlechtes Gewissen. Wenn ich mit ihr hineingegangen wäre, wäre er vielleicht nicht so wütend geworden."


"Wenn ich sie nicht hätte wegrennen lassen, wäre er überhaupt nicht wütend geworden."


"Ich könnte immer noch hineingehen und sie retten…"
"Nein… Ich glaube, das kann ich nicht."


"Ich war genauso. Ich habe Rin auch angebrüllt, und jetzt schäme ich mich deswegen mehr denn je."


"Es kam mir bloß gerechtfertigt vor, meinen Ärger an ihr auszulassen, weil… weil ich einfach dachte, es wäre ihr Fehler, dass ich so frustriert war."


"Ich hatte genauso wenig Recht dazu wie Nomiya."


"…"


"Eine schreckliche Stille legt sich über den Korridor."


"Rin hat Nomiya nichts zu sagen."


"Man kann nur raten, ob ihr die Antworten ausgegangen sind oder ob sie weiß, dass zu diskutieren, ihn nur noch wütender machen würde."


"Herr Nomiya hat auch nichts mehr zu sagen, so scheint es. Oder vielleicht ist ihm nur der Atem ausgegangen."


"Für einen Augenblick stelle ich mir vor, wie die beiden sich nur anstarren – einer erfüllt mit loderndem Zorn, die andere erfüllt mit… ja, was nur?"


"Ich kann nicht sagen, wir Rin sich fühlt – jetzt genauso wenig wie zuvor."


"Herr Nomiya scheint auch zu erwarten, dass Rin etwas sagt. Doch da sie es nicht tut, fährt er schließlich in einer leiseren, aber nicht weniger zornigen Stimme fort."


no "Was bringt es, so viel zu arbeiten, wenn am Ende… nichts bei herauskommt?"


"Trotzdem will Rin immer noch nichts sagen."


no "Es tut mir leid. Ich hätte mich nicht so aufregen sollen."


"Er klingt ganz und gar nicht so, als täte es ihm leid. Sein Ton ist eher kalt und scharf, als ob er die Worte ausspucken würde."


no "Scheint so, als hätte ich zu viel erwartet. Du bist also doch keine Künstlerin."


"Jepp, es tut ihm überhaupt nicht leid."


show nomiya serious onlayer master:
    tworight
    alpha 0.0
    parallel:
        linear 1.0 center
    parallel:
        linear 0.4 alpha 1.0
        0.2
        linear 0.4 alpha 0.0
with Pause(1.0)

stop music fadeout 4.0

"Er stürmt aus dem Klubraum und die Treppen hinab, ohne mich zu bemerken."


"Nachdem er weg ist, werfe ich vorsichtig einen Blick in das Klassenzimmer."


scene bg school_nomiya onlayer master at right
show rin basic_awayabsent onlayer master at center
with locationchange

"Rin steht dort verlassen vor dem Lehrertisch."


show rin negative_spaciness onlayer master
with charachange

rin "Ich konnte nicht sagen, dass es mir leid tut."


"Sie sagt das in die feuchte Luft des Klassenzimmers, nicht zu mir."


"Doch da ihr der Raum nicht antworten wird, muss ich es tun."


hi "Das war unfair von ihm… Er war wütend, aber trotzdem…"


"Ich kann mich nicht entscheiden, wie ich meinen Satz beenden soll. Herrn Nomiya zu verachten kommt mir vor, als würde ich mein Verhalten von vor zwei Tagen verachten."


"Dumm, aber im Nachhinein richtig."


show rin negative_spaciness_close onlayer master
with characlose

"Rin antwortet nicht und steht nur wie erstarrt da, darum laufe ich zu ihr."


"Sie hat für sich selbst eingestanden. Irgendwie. Das habe ich nicht erwartet."


"Ich kann nicht sagen, ob es ungebührlich ist oder nicht, aber so oder so hat sie es getan."


"Bei mir hat sie das nie getan."


"Irgendwie wünsche ich mir, sie hätte es. Vielleicht würde ich mich dann nicht so mies fühlen."


"In letzter Zeit scheint es wirklich, als hätte ich mir allerlei Dinge gewünscht."


hi "Rin?"


show rin negative_annoyed_close onlayer master
with charachange

rin "Geh weg."



label de_R40:

scene bg school_nomiya onlayer master at right
show rin negative_annoyed_close onlayer master at center
with None

play music music_sadness fadein 6.0

hi "Wieso… Wie meinst du das?"


show rin negative_angry_close onlayer master
with charachange

rin "Du bist auch wütend auf mich, oder?"


rin "Ich dachte, du wärst mein Freund. Ich dachte, er wäre es auch."


"So habe ich ihre Stimme noch nie gehört. Sie ist bitter und scharf wie Rasierklingen. Dabei schaut sie demonstrativ auf ihre Zehen."


hi "Ich glaube nicht, dass es daran lag."


hi "Er wollte, dass du etwas wirst, was du nicht bist. Und…"


show rin basic_surprised_close onlayer master
with charachange

"Ich atme tief ein und fange endlich ihren Blick ein. Wir sehen uns in die Augen."


hi "… Es tut mir leid. Ich wollte auch, dass aus uns mehr wird… Mehr als Freunde."


hi "Vielleicht konnte ich mich deswegen nicht beherrschen und wurde so frustriert. Genau wie Herr Nomiya."


show rin relaxed_doubt_close onlayer master
with charachange

rin "Wie mehr? Ich bin nichts weiter als ich selbst. Das ist alles, was ich bin. Ich verstehe das nicht."


"Na ja… die Antwort sollte offensichtlich sein, oder?"


"Ich erinnere mich an den Zweck von Freundschaft: Alles zusammen durchzustehen und für deinen Freund da zu sein."


"Habe ich als Freund versagt, indem ich dachte, die Freundschaft könnte die Grundlage für etwas anderes sein?"


"Vielleicht konnte ich es wegen dieser Gedanken nicht aushalten und mich nicht zusammenreißen."


"So haarsträubend wie Rin auch ist und war, ich hätte mich nicht so darauf festfahren sollen – besonders als ich anfing, so für sie zu empfinden."


"Habe ich also versagt?"


"Das scheinen ihre Augen zu fragen."


"…"


hi "Es tut mir leid, Rin."


hi "Vielleicht bin ich nicht in der Lage, dein Freund zu sein."


hi "Ich denke nicht, dass ich je ein guter Freund für dich sein kann."


"Ich sage das, weil es wahr ist. Nicht, weil einer von uns es hören will."


"Es es ist etwas, das gesagt werden muss."


"Die Endgültigkeit meiner Worte schafft eine erschütternde Stille. Was gibt es auch noch hinzuzufügen?"


"…"


show rin negative_confused_close onlayer master
with charachange

rin "Wieso? Wieso passiert das alles?"


show rin negative_sad_close onlayer master
with charachange

rin "Leute tun Dinge, um die ich sie nicht gebeten habe und die ich nicht will, und alle werden immer wütend auf mich. Ich hab keine Ahnung mehr, was los ist, und ich kann nicht aufhören, mich so zu fühlen, als wollte ich vor allem davonlaufen…"


show rin basic_lucid_close onlayer master
with charachange

"Sie schließt fest ihre Augen und atmet tief und ruhig aus."


show rin basic_upset_close onlayer master
with charachange

"Als sich ihre Augenlider öffnen, ist alles, was ich sehen kann, dunkelgrüne Verzweiflung."


rin "{b}Ich hab keine Ahnung, was mit mir nicht stimmt!{/b}"


"Ihr verzweifelter Ausbruch verblüfft mich für einen Moment, und für die Dauer eines Herzschlags sehen wir uns nur an."


"Ihre verwirrten Augen zu sehen, die nach einer Antwort in meinen suchen, macht mich nur traurig. Denn ich weiß, dass ich keine habe."


hi "Ich weiß es auch nicht."


hi "Aber weißt du… Du selbst hast gesagt, dass die Dinge weder richtig noch falsch sind."


hi "Sie sind einfach."


hi "Entweder akzeptiert man sie, versucht sie zu ändern oder gibt auf."


hi "Ich hasse dich nicht. Herr Nomiya hasst dich auch nicht."


hi "Ich denke nur… dass ich die Art von Mensch bin, der aufgibt, wenn er glaubt, nicht weiterzukommen."


hi "Und auch wenn du es hassen magst, so… so stehen die Dinge nun mal."


"Ich sage ziemlich grausame Dinge, doch ich kann mich nicht zügeln. Die Worte rollen von meiner Zunge mit langsamer, harter Gewissheit."


show rin basic_surprised_close onlayer master
with charachange

"Ich kann sehen, wie sie Rin fast wie echte Schläge treffen."


"Ihre Augen, immer noch weit geöffnet vom Schock der Zurückweisung, beginnen feucht zu glänzen."


show rin basic_crying_close onlayer master
with charachange

"Als die Tränen anfangen, ihre blassen Wangen hinunterzulaufen, tut sie nichts, um sie aufzuhalten."


"Während sie eine nach der anderen auf den Boden fallen, steht sie still und starrt mich mit einem von schierem Unglauben erfüllten Blick an."


rin "…"


"Aber die Realität holt mich ein."


show rin negative_crying_superclose onlayer master
with vpunch

"Rin sackt nach vorne, als würde sie jegliche Energie verlieren, und vergräbt ihr Gesicht so tief wie sie kann in meinem Shirt."


"Rin ist schwer und gleichzeitig federleicht. Sie schluchzt oder weint nicht wirklich, sie lehnt sich nur gegen mich und lässt ihre Tränen durch mein Hemd auf die darunter liegende Haut brennen."



"Und ich lasse es zu und lege meine Hand in einer plumpen Umarmung um ihre Schulter, die sie kaum tröstet."


"Ich kann Rins Wirbelsäule mit meinen Fingerspitzen spüren. Wie eine harte und zackige Erinnerung daran, wie verkorkst die Dinge sind."


"Es ist ein erbärmlicher Anblick, wie ihre schmale Schulter in meiner Handfläche bebt. Die Hoffnungslosigkeit, ein Teil der Ursache für Rins Traurigkeit zu sein, zerreißt mein Herz."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\n\n\nEin Mädchen zum Weinen zu bringen, ist das Abscheulichste überhaupt."


n "\nSogar bei Rin. Besonders bei Rin."


n "\nHinter diesem Schleier der Distanziertheit ist Rin auch nur ein menschliches Wesen."


n "Genauso verwirrt, verängstigt und verloren wie jeder andere von uns."


n "Die meiste Zeit scheint es, als könnte man sich keinen Reim darauf machen, was Rin sagt und tut, aber ausnahmsweise glaube ich, dass ich wirklich verstehe, wie sie sich fühlt."


n "\n\nAber man kann es nicht mit Worten ausdrücken, und Worte können es auch nicht besser machen."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear

show bg school_nomiya onlayer master:
    "bg school_nomiya_ss" with Dissolve(8.0)
show rin negative_crying_superclose onlayer master:
    "rin negative_crying_superclose_ss" with Dissolve(8.0, alpha=True)
with None

stop music fadeout 5.0

n "\n\n\n\n\nAlso schweigen wir weiter und warten darauf, dass ihr die Tränen ausgehen."


n "Die Zeit vergeht quälend langsam. Sogar die trägen Staubpartikel in der Luft scheinen zum Stillstand gekommen zu sein."


n "Die obligatorische Wanduhr tickt ablenkend über der Tür."


n "Ich entscheide mich gegen das Sekundenzählen, weil sie mir dadurch nur noch länger vorkommen würden."


n "\n\n…"


play music music_serene fadein 9.0

nvl hide dissolve
nvl clear

show rin basic_crying_superclose_ss onlayer master
with charachange

window show

"Schließlich rührt sich Rin etwas, und während sie sich immer noch in meine Brust gräbt, murmelt sie in mein Hemd."


rin "Lass mich eine Weile so bleiben."


show rin negative_crying_superclose_ss onlayer master
with charachange

rin "Bitte, Hisao."


rin "Gib mir nur einen kurzen Moment."


"Ein warmes Gefühl macht sich in mir breit. Im Moment kann ich nichts für Rin tun, außer für sie da zu sein, aber es ist gut zu wissen, dass sie das – nach allem, was passiert ist – immer noch will."


hi "Klar."


"Also bleibt sie."


"Doch ich kann mich immer noch nicht dazu überwinden, sie näher an mich heranzuziehen, damit ich sie richtig umarmen kann."


"Und zwar, weil mich das nur traurig machen würde und ich nicht weiß, ob ich das ertragen könnte."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\nDie Erkenntnis, dass wir vielleicht nie wirklich werden können, was wir für den jeweils anderen sein wollen, kristallisiert sich in meinem Kopf wie ein Diamant."


n "Ein Stich schießt durch mein Herz wie ein Stromschlag."


n "Sie schmerzt."


n "Diese Klarheit… schmerzt."


n "Was können wir füreinander sein? Welche Bedeutung hat es, sich so verzweifelt aneinander festzuklammern, obwohl es so vergeblich scheint?"


n "Was sollte ich zu Rin sagen? Wie kann ich sie aufmuntern?"


n "So etwas kann ich nicht. Und ich fürchte, wenn ich es könnte, würde es nur noch mehr wehtun."


n "Gewaltsam verdränge ich das alles aus meinen Kopf, weil ich nicht an schmerzliche Wahrheiten denken will."


n "Schon bald beruhigen sich meine Gedanken, und die Traurigkeit löst sich auf. Alles, was übrig bleibt, sind ich und Rin und das zarte Gefühl ihrer Wärme und Sanftheit an meiner Brust."


nvl clear

n "\n\nWann habe ich mich in sie verliebt?"


n "Ich kann mich nicht erinnern, aber ich bin sicher, dass es lange vor der warmen Berührung unserer Lippen war. Dieser Kuss an diesem orangefarbenen Nachmittag, als sie mit einer Erkältung krank im Bett lag und ich sie aus unklaren Gründen besucht hatte."


n "Ihr sorgloses Auftreten, die Aura der Andersartigkeit um sie herum, all die Dinge, die Rin ausmachen… Diese Dinge haben mich mit unwiderstehlicher Kraft angezogen."


n "Wie sie alles Mögliche aufnehmen konnte, und dabei allem nur ihren eigenen Wert zuschreibt; wie sie alles fair und ohne Vorurteil abwägt; wie sie die Welt nur durch ihre eigenen Augen sieht."


n "Das ist etwas, was ich niemals tun konnte. Und Rin war wahrscheinlich mehr eine Muse für mich, als alles andere je für sie eine war."


n "Sie schien mir so frei zu sein – ein echter Freigeist. Während ich, der sich andauernd Sorgen über alles gemacht hat, so verklemmt schien, dass es fast peinlich war."


n "Vielleicht habe ich mich deswegen so sehr an Rin geklammert. Ich wollte versuchen, in ihre Welt zu gelangen, die so anders als mein eigenes, trostloses Leben war."


nvl clear

n "\n\nBevor ich mich versah, hat diese unwiderstehliche Kraft mich gefährlich nah an sie herangezogen, aber es stellte sich heraus, dass sie viel zu fremdartig für mich war."


n "Und ausgerechnet Newton hatte ich vergessen."


n "Die Gravitationskraft ist umgekehrt proportional zum Quadrat der Distanz zwischen zwei Objekten…"


n "Wenn also zwei Mensch etwas füreinander empfinden…"


n "Heh."


n "Auch wenn Gefühle nicht von den Konstanten des Universums beherrscht werden, geht mir die Vorstellung nicht aus dem Kopf, dass ich seit einiger Zeit ein Satellit gewesen bin, der Rins hell leuchtenden Planeten umkreist."


n "\nPlanet Rin."


n "\nDer Gedanke bringt mich fast zum Lachen. Ab und zu scheint sie wirklich von einem anderen Planeten zu sein – ohne grüne Haut und möglicherweise ein paar Tentakel."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

show rin negative_sad_close_ss onlayer master
with charadistant

window show

"Vielleicht wegen meines unterdrückten Lachers löst sich Rin von mir, und ich lasse sie los. Ich spüre die Kälte, als ihre Wärme verschwindet, und eine leichte Verlegenheit, weil ich meinen Gedanken so freien Lauf gelassen habe."


"Ich glaube, dass Rin einen schlechten Einfluss auf mich hat. Wobei ich gleichzeitig froh darüber bin, dass sie nicht wirklich Gedanken lesen kann."


"Rins bittere Tränen sind getrocknet, und sie sieht wieder ein bisschen mehr wie sie selbst aus."


show rin basic_sad_close_ss onlayer master
with charachange

"Jedoch ist der verlorene Blick in ihren Augen immer noch da. Ihr Blick wandert rastlos durch den Raum, bevor er an mir hängen bleibt."


rin "Was ist gerade passiert?"


rin "Kannst du mir das sagen?"


hi "Was? Was meinst du?"


show rin basic_upset_close_ss onlayer master
with charachange

rin "Ich habe geweint."


"Sagt sie zögerlich, als ob sie es selbst nicht glauben würde."


hi "Ja…"


"…"


"Sie starrt mich weiterhin an, als ob sie um Weisung bitten würde, damit sie sich nicht so verloren fühlen muss."


"…"


show rin basic_sad_close_ss onlayer master
with charachange

rin "Warum?"


hi "Du warst traurig."


hi "Willst du das von mir hören? Ist das nicht offensichtlich?"


show rin negative_confused_close_ss onlayer master
with charachange

rin "Ich weiß nicht. Weinen fühlt sich komisch an."


hi "Was? Das glaube ich nicht. Ich meine, alle tun das. Es ist nor—"


"Ich beiße mir auf die Zunge, bevor ich mein Argument über Normalität beenden kann."


"Normen gelten nicht für die Person, mit der ich gerade rede."


show rin negative_worried_close_ss onlayer master
with charachange

rin "Es hat sich immer so falsch angefühlt – anders als das, was in mir ist. Als könnte ich nicht wirklich sagen, was ich fühle."


rin "Also hab ich angefangen zu denken, dass ich vielleicht nicht weiß, was ich fühle. Vielleicht bin ich diejenige, die falsch liegt."


rin "An solche Dinge hab ich gedacht."


show rin negative_sad_close_ss onlayer master
with charachange

rin "Ich dachte… das Malen wäre genug, weil es mir vorkam, als würde ich wenigstens das richtig machen."


rin "Dass alles in mir ein Bild werden könnte, wenn ich mir wirklich Mühe gebe. Und das konnte es."


rin "Aber es fühlt sich nicht mehr so an, als sei es genug. Denn wenn niemand anderes es sehen kann, werde ich immer noch allein sein."


show rin basic_absent_close_ss onlayer master
with charachange

rin "War es falsch, es zu versuchen? Alle sind deswegen echt sauer auf mich geworden."


stop music fadeout 6.0

"Ich habe Rin selten so viel auf einmal sagen gehört."


"Als sie fertig ist, bleibt sie einfach still und sieht so neutral aus, dass es schwer zu glauben ist, dass sie das gerade gesagt hat."


"Ich weiß nicht, was ich denken soll."


"…"


"Rin wollte verzweifelt, dass sich jemand ihre Gemälde ansieht. Man sollte durch sie irgendwie direkt in ihre Seele sehen, um ihre Gefühle zu verstehen."


"Weil… sie dachte, sie könnte sie nicht auf eine andere Weise ausdrücken?"


"Wie kann jemand sagen, ob das richtig oder falsch ist?"


"Könnte es sein, dass sie die ganze Zeit versucht hat, mich zu erreichen, so wie ich versucht habe, sie zu erreichen?"


"…"


"Ich setze mich auf einen Tisch, um nachzudenken – und um meine Beine auszuruhen, die uns beide für eine lange Zeit getragen haben."


play music music_innocence fadein 12.0

hi "Weißt du, wenn ich ein gutes Buch lese oder mir den Sternenhimmel ansehe oder so was, fühle ich manchmal etwas… Tiefgründiges, wie ein… Verdammt, ich weiß nicht, wie ich es beschreiben soll."


hi "Doch in dem Augenblick, in dem ich versuche, es in Worte zu fassen, kommt es mir vor, als würde ich etwas verlieren. Es fühlt sich nicht so real, nicht so wahr an, wie es noch in meinem Kopf war."


hi "Es fühlt sich etwas künstlich an… Verdammt, sogar was ich gerade gesagt hab, fühlt sich künstlich an."


"Ich zeige ein Lächeln, das zwischen Belustigung und Selbstironie schwebt, aber Rin reagiert nicht."


hi "Jedenfalls…"


hi "… könnte es sein, dass niemand seine Gefühle je so ausdrücken kann, dass andere sie verstehen."


hi "Die Realität hat keine Chance, mit dem mitzuhalten, was man selbst im Kopf hat."


hi "Nichts kommt da ran. Nicht einmal deine Gemälde – außer vielleicht für dich."


hi "Aber ich vermute, man kann nicht alles in sich hineinfressen. Man würde sonst wirklich explodieren."


hi "Was ich damit sagen will… Ich glaube nicht, dass es falsch ist, deine Gefühle auszudrücken. Auch wenn du deine Gemälde als Sprachrohr benutzt."


hi "Du kannst von den Leuten nur nicht erwarten, dass sie dich besser verstehen, als wenn du es auf einem anderen Weg getan hättest."


hi "Eigentlich kannst du gar nicht von ihnen erwarten, dass sie dich verstehen."


hi "Weil alles so subjektiv ist. Du siehst die Welt, wie du sie siehst – nicht so wie andere sie sehen."


show rin basic_sad_close_ss onlayer master
with charachange

rin "Aber ist das nicht schrecklich?"


hi "Ich schätze, das ist es. In gewisser Hinsicht."


"…"


show rin relaxed_doubt_close_ss onlayer master
with charachange

"Sie runzelt die Stirn und sieht so gebeutelt aus, wie sie kann. Was nicht viel ist, aber genug für mich, um zu verstehen, dass Rin nicht besonders glücklich darüber ist."


rin "Ich glaube, das könnte mich vielleicht doch traurig machen."


hi "Ja. Ich weiß."


hi "Ich wünschte, ich könnte etwas dagegen tun."


"Ich denke nicht, dass ich verbittert klinge. Und wenn, dann nur ein bisschen."


"Das ist mein Problem. Ich kann nicht sein, was Rin von mir erwartet. Und aus dem gleichen Grund kann sie das für mich auch nicht."


"…"


show rin negative_worried_close_ss onlayer master
with charachange

"Sie macht ein kompliziertes Gesicht und versucht sorgfältig, die passenden Worte zu finden."


"Also kommt es auch bei Rin vor, dass sie sprachlos ist."


show rin basic_sad_close_ss onlayer master
with charachange

rin "Dann kann man wohl nichts machen, glaube ich."


show rin basic_absent_close_ss onlayer master
with charachange

rin "… Aber… wenn du das sagst…"


show rin basic_awayabsent_close_ss onlayer master
with charachange

rin "… fühle ich mich ein bisschen besser."


"…"


"Witzig, wie manche scheinbar unwichtige Dinge in solchen Momenten die Bedeutsamsten sein können."


"Wie zum Beispiel, dass Rins Stimme sehr, sehr leise und kaum hörbar ist, als sie das sagt."


"Und wie sogar ihr kurzer Pony ihre Augen bedecken kann, wenn sie nach unten sieht."


show rin basic_blush_close_ss onlayer master
with charachange

"Und wie sie nicht das tiefe Rot verdecken können, dass auf ihren Wangen erscheint und bis zu den Ohrenspitzen wandert."


"Sie färben sich zu einem sehr interessanten Rotton."


"Es folge eine ohrenbetäubende Stille."


"Es ist sehr peinlich. Als ob ich etwas gesehen hätte, was ich nicht hätte sehen sollen – auch wenn es keine Absicht war."


"Ich weiß nicht, was ich dazu sagen soll, aber es kommt mir vor, als sollte ich das wissen."


"Sie weiß es ebenfalls nicht."


"Trotzdem wirkt es, als könnte es diesen Moment auch nicht zerstören, wenn wir einfach weiter schweigen."


"Als ob wir eine seltsame, wortlose Verbindung hätten, die trotzdem bestehen bleiben würde."


show rin relaxed_nonchalant_close_ss onlayer master
with charachange

"Rin wechselt unruhig von einem Fuß zum anderen und sieht im Raum überall hin, außer zu mir."


"Sie ist diejenige, die letztendlich den Bann bricht."


show rin basic_deadpan_close_ss onlayer master
with charachange

rin "Können wir gehen? Ich will nicht hierbleiben."


hi "Oh, ja, na klar. Wohin?"


"Meine Antwort verschleiert meine Nervosität genauso schlecht wie ihre Frage ihre."


show rin relaxed_sleepy_close_ss onlayer master
with charachange

rin "Du kannst gehen, wohin du willst. Ich will schlafen. Ich hab in den letzten Wochen kaum geschlafen."


show rin basic_lucid_close_ss onlayer master
with charachange

rin "Es fühlt sich an, als wäre ein Rudel aus hellblauen Schmetterlingen in meinen Kopf. Dadurch fällt es mir schwer, richtig zu denken."


show rin basic_deadpannormal_close_ss onlayer master
with charachange

rin "Die Art, von der man denkt, sie wären zu blau, um wirklich zu existieren – wie Emis Höschen heute morgen."


show rin negative_spaciness_close_ss onlayer master
with Dissolve(0.1)

show rin basic_absent_close_ss onlayer master
with Dissolve(0.1)

show rin negative_spaciness_close_ss onlayer master
with Dissolve(0.05)

show rin basic_absent_close_ss onlayer master
with Dissolve(0.05)

show rin negative_spaciness_close_ss onlayer master
with Dissolve(0.05)

show rin basic_absent_close_ss onlayer master
with Dissolve(0.05)

show rin negative_spaciness_close_ss onlayer master
with Dissolve(0.1)

show rin basic_deadpannormal_close_ss onlayer master
with Dissolve(0.2)

"Sie schüttelt ihren Kopf, und ich rechne fast damit, dass ein paar ultramarinfarbene Morphos aus ihren Ohren fliegen."


show rin basic_deadpanamused_close_ss onlayer master
with charachange

"Ihre Mundwinkel verziehen sich zu einem kleinen Lächeln."


rin "Dabei fällt mir ein – bei dem Blau, nicht bei dem Höschen."


show rin basic_deadpandelight_close_ss onlayer master
with charachange

rin "Das Wort für ein Rudel aus Schmetterlingen ist Schwarm. Ich hab's nachgeschlagen."


"Meine Augenbrauen heben sich zu einem fragenden Bogen."


hi "Warum hast du es dann nicht benutzt?"


show rin basic_absent_close_ss onlayer master
with charachange

rin "Mir gefällt das andere Wort besser."


"Warum es dann überhaupt nachschlagen?"


hi "Dann solltest du es auch benutzen, oder?"


show rin basic_awayabsent_close_ss onlayer master
with charachange

"Sie nickt und wird wieder still. Ihr Blick weicht meinem seitlich aus, als ob er vom dunkelorangenen Sonnenlicht angezogen wird, das durch die Fenstern hereinscheint."


"So bleiben wir eine kurze Weile: Ich sehe sie still an, und sie sieht still aus dem Fenster."


hi "Hey… geht's dir jetzt besser?"


show rin basic_absent_close_ss onlayer master
with charachange

"Sie wirft mir einen erneut wehmütigen Blick aus dem Augenwinkel zu. Die Reflektion des Sonnenlichts gibt nicht mehr von ihren inneren Gefühlen preis."


rin "Ich muss darüber nachdenken."


"Ich will diese Unterhaltung fortsetzen und mich an diesen Strohhalmen festhalten, deren Existenz sie endlich offenbart hat."


show rin basic_awayabsent_close_ss onlayer master
with charachange

"Doch Rin schaut weiterhin so gedankenverloren aus dem Fester, dass ich weiß, dass sie mir in keinster Weise eine sinnvolle Antwort geben kann."


"Es ist wie eine Art Verteidigungsmechanismus von ihr, um zu vermeiden, vernünftig sein zu müssen."


"Ihr Verstand ist selbst wie ein Schmetterling. Er flattert davon, wann immer er aufgeschreckt wird."


"Gerade als ich dachte, ich könnte hinter ihren Schleier sehen, springt sie wieder außerhalb meiner Reichweite."


"Vielleicht ist Rin einfach so."


"Vielleicht ist das etwas, das ich einfach akzeptieren sollte, um etwas Seelenfrieden zu erhalten."


hi "Okay."


hi "Ich bringe dich dann zurück zu ins Wohnheim."


show rin basic_absent_close_ss onlayer master
with charachange

rin "Danke."


show rin basic_lucid_close_ss onlayer master
with charachange

rin "Wirklich."


stop music fadeout 12.0

scene bg school_hallway3 onlayer master
with locationchange

"Die leeren Korridore der Schule wirken sehr einsam so ganz ohne Schüler."


"Weniger als eine Stunde nach Beginn der Sommerferien scheint das Gebäude verlassen zu sein, und alles, was die Totenstille der Flure stört, sind unsere Schritte."


"Die Veränderung ist plötzlich, aber sie zeigt, dass das Gebäude nur eine leere Hülle ist – tot, ohne ihre Schüler und Lehrer."


"Es ist, als ob die Schule eine abgeschiedene Welt für uns zwei geworden wäre. Ein menschenleerer Ort erfüllt mit Stille und Kreidestaub."


scene bg school_staircase2_ss onlayer master
show rin relaxed_sleepy_close_ss onlayer master at twoleft
with locationchange

rin "Ich glaube, ich muss mich ändern."


"Sie sagt es aus dem Nichts, während wir die Treppen vom dritten Stock hinabsteigen. Dabei wirkt sie immer noch so, als würde sie das widerspiegeln, was ich gerade eben noch gedacht hatte."


hi "Manchmal müssen Menschen das."


window hide
nvl clear
nvl show dissolve

n "\n\n\n\n\n\n\n\nDas ist das Letzte, was wir an diesem Tag zueinander sagen, obwohl es noch so viel zu bereden gäbe."


n "Und selbst diese Worte gehen in der allumfassenden Stille unter und verschwinden in der stagnierenden Luft, als wären sie nie ausgesprochen worden."


nvl clear
nvl hide dissolve

$ suppress_window_before_timeskip = True

scene black onlayer master
with dissolve


label de_R41:

play music music_dreamy fadein 2.0

scene bg school_dormhisao_rn onlayer master
with charachange

$ renpy.music.set_volume(0.4, 0.0, channel="ambient")
play ambient sfx_rain fadein 1.0

"Der erste Tag der Sommerferien ist eine Enttäuschung."


"Ich bin aufgewacht, und Wasser fiel in biblischen Ausmaßen vom bleiernen Himmel."


"Zu diesem Zeitpunkt war ich noch optimistisch."


"Ein kurzer Sommerschauer, dachte ich. Ein paar Minuten lang Wolkenbruch, dann ist es vorüber."


show rain normal behind bg onlayer master
with None

"Nichts da."


$ renpy.music.set_volume(0.7, 1.0, channel="ambient")

hide bg onlayer master
show bg misc_sky_rn as bg2 behind rain onlayer master
show hisaowindow onlayer master
with locationchange

"Es schüttet unnachgiebig vom blau-grauen Himmel draußen herab. Regenwasser rinnt in kleinen Bächen und Flüssen mein Fensterglas hinunter und sammelt sich auf den Fußwegen zu Miniaturteichen."


"So geht das schon seit zweieinhalb Stunden."


$ renpy.music.set_volume(0.4, 1.0, channel="ambient")

scene bg school_dormhisao_rn onlayer master
with charachange

"Also habe ich halbherzig ein Buch gelesen, zwischendurch halbherzig mein Zimmer aufgeräumt und – nachdem mir beides zu langweilig geworden war – nebenbei meine Sachen gepackt."


"Das Wetter zieht meine Stimmung auch ziemlich runter, sodass es schwierig ist, irgendetwas anständig zu machen."


play sound sfx_impact2

"Dass etwas ziemlich laut gegen meine Tür stößt, weckt mich aus meiner Apathie auf."


"Ich hoffe, es ist nicht Kenji mit seiner verrückten Indoor-Bowlingbahn."


"…"


"Ich höre keine Geräusche mehr vom Flur, bis ich zur Tür gehe und sie öffne."


play sound sfx_dooropen
$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
stop music fadeout 2.0

scene bg school_dormhallway onlayer master
show rin basic_absent onlayer master
with locationchange

"Rin."


"Ich wünschte, sie zu sehen, würde mehr Emotion in mir hervorrufen. Doch zum einen bin ich zu überrascht darüber, dass sie mich besuchen kommt, und zum anderen ist sie patschnass."


"Das Hemd ihrer Schuluniform ist klitschnass, und sie steht in einer selbstgeschaffenen Pfütze."


"Tröpfchen aus Regenwasser tropfen von ihrem kurzen Pony und gleiten ihre Nase hinab, bis sie von ihrer Spitze herunterfallen."


"Tropfen.{w=0.7} Für.{w=0.7} Tropfen."


hi "Ähm… Hi."


hi "Wie fühlst du dich?"


show rin basic_deadpannormal onlayer master
with charachange

rin "Mittelnormal."


play music music_rin fadein 2.0

"Mal von ihrer fragwürdigen Äußerung abgesehen, sieht sie wirklich nicht allzu gut aus."


hi "Du bist ja ganz nass."


show rin basic_absent onlayer master
with charachange

rin "Weil ich von draußen komme. Kennst du das?"


hi "Was hast du draußen verloren? Falls es dir nicht aufgefallen ist, es regnet da Hunde und Katzen."


show rin basic_deadpancontemplation onlayer master
with charachange

rin "Ist es nicht. Allerdings regnet es ziemlich stark. Ich war spazieren."


hi "Ist es das, was du „in Selbstmitleid versinken” nennst?"


show rin basic_deadpanupset onlayer master
with charachange

rin "Du findest, ich bin bemitleidenswert?"


hi "Nein, ich habe damit angedeutet, dass du denkst, dass du es bist."


show rin basic_awayabsent onlayer master
with charachange

rin "Bin ich nicht, und Regen ist nichts Trauriges."


show rin basic_absent onlayer master
with charachange

rin "Gehst du nie im Regen spazieren?"


hi "Schon, aber nur mit passender Ausrüstung – wie zum Beispiel einem Regenschirm."


show rin basic_lucid onlayer master
with charachange

rin "Du musst dir nur vorstellen, du hättest einen blauen Regenschirm mit weißen Streifen."


hi "Könnte schwierig sein, wenn der Regen auf meinen Kopf fällt."


show rin basic_deadpannormal onlayer master
with charachange

rin "Stell's dir einfach fester vor."


"…"


"Jepp, sie ist definitiv wieder die Alte."


"Diese halb-sarkastischen, rücksichtslosen Bemerkungen, die mich regelrecht in Rage bringen, obwohl sie sie nicht so meint. Dieser leere, verträumte Blick, der immerzu mehr erwartet, als er gibt."


"Es sieht ihr… sehr ähnlich."


show rin basic_deadpan onlayer master
with charachange

rin "Ich muss vielleicht reinkommen. Ich brauche etwas Hilfe mit diesem Wasser und den Klamotten."


"Schnell löst mein Gehirn diese Gleichung, und ich stolpere über meine Worte – ein krasser Kontrast zu Rins unbekümmerter Selbsteinladung."


hi "Aber… Emi…"


show rin basic_lucid onlayer master
with charachange

"Rin schüttelt heftig ihren Kopf, wodurch das Wasser überall hinspritzt."


rin "Sie ist gegangen."


show rin basic_awayabsent onlayer master
with charachange

rin "Außerdem würde sie sich nur sorgen und jammern, bis sie sich nicht mehr sorgen und jammern kann – was auch immer ärgerlich lange dauert."


show rin basic_absent onlayer master
show rain normal behind bg onlayer master
with charachange

rin "Es dauert länger, als ich sie jammern hören will, und ich dachte mir, du gehörst wahrscheinlich nicht zu denen, die immer jammern."






$ renpy.music.set_volume(0.4, 1.0, channel="ambient")

hide bg onlayer master
show rin invis_close onlayer master at center
show bg misc_sky_rn as bg2 behind rain onlayer master
show hisaowindow behind rin onlayer master
with locationchange

show rin relaxed_nonchalant_close_rn onlayer master:
    ypos 1.1
with Dissolvemove(0.5)

stop music fadeout 8.0
play sound sfx_rustling

"Sie lässt sich mit einem nassen Plumpsen auf meinen Tisch fallen."


"Ihre durchnässten Kleider machen den Tisch und alles darauf nass, doch das scheint sie nicht zu kümmern."


"…"


hi "Okay. Schön. Ich helfe dir."


hi "Ich habe irgendwo ein Handtuch. Willst du trockene Sachen? Ist eine Uniform okay? Ich bin größer als du, aber…"


show rin basic_lucid_close_rn onlayer master
with charachange

rin "Alles ist okay."


show bg school_dormhisao_rn onlayer master
with locationchange

"Mit etwas Suchen finde ich eine frische Uniform und ein flauschiges Handtuch aus den Tiefen meines Wandschranks."


hide bg onlayer master
with locationchange

"Das Handtuch in der einen Hand und die Uniform in der anderen wende ich mich wieder Rin zu, ohne zu wissen, was ich als nächstes tun soll."


"Irgendetwas stimmt nicht mit mir, ein normaler Typ würde einfach—{w=1.0}{nw}"


show rin basic_absent_close_rn onlayer master
with charachange

rin "Hör auf, dir Gedanken zu machen. Es ist kein Problem."


"Wahrscheinlich hat sie mein zögerliches Auftreten sofort bemerkt."


"Als ob ich für sie vollkommen durchschaubar wäre."


"Ich verdränge meine Nervosität und konzentriere mich auf die Knöpfe an ihrem Hemd – acht Stück, genau wie bei meinem."


"Nur der erste Knopf ist ein Hindernis, und nachdem ich ihn bewältigt habe, knöpfe ich die anderen mit etwas weniger zitternden Händen auf."


$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
play music music_heart fadein 0.5

scene ev rin_wet_pan_down onlayer master:
    center
    yalign 1.0 subpixel True
    easein 20.0 yalign 0.0
with whiteout

"Ich werfe das durchnässte Hemd zur Seite und enthülle Rins blassen Oberkörper, der nur von ihrem hellblauen BH bedeckt ist, und mich augenblicklich daran erinnert, dass sie mir gesagt hat, das sei ihre Lieblingsfarbe."


"Ich versuche, nicht allzu sehr an… Dinge… zu denken, aber es ist schwierig, ihren Körper nicht mit diesen… sagen wir mal… gemischten Gefühlen anzusehen."


"Ich weiß nicht, was ich davon halten soll. Darum betrachte ich sie nur. Rin sieht… zerbrechlich aus."


"Sie ist wie eine Hülle. Ein fragiles Ding, das sich gerade so zusammenhalten kann."


"Ihre Rippen, jede einzelne sichtbar unter ihrer blassen Haut, bewegen sich mit ihrer Atmung rhythmisch auf und ab."


"Rin kam mir immer ziemlich dünn vor, doch nun bemerke ich, dass sie in der manisch-kreative Phase vor der Ausstellungseröffnung vielleicht etwas Gewicht verloren hat."


"Hat sie anständig und genug gegessen? Ersteres bestimmt nicht und letzteres wahrscheinlich nicht."


"Dieses hässliche und doch schöne absolute Minimum eines menschlichen Körpers, das zu jemanden gehört, der mir wichtig ist, ist in sich selbst ein ästhetischer Widerspruch. Seltsamerweise passt das zu ihr."


"Meine Augen folgen ihrem Schlüsselbein zu ihrer Schulter und an ihren Armen hinab, bis diese abrupt enden."


"Nein, es ist weniger als das absolute Minimum. Doch diesem Gedanken folgt schnell ein stechender Schmerz und ein Schuldgefühl dafür, überhaupt so gedacht zu haben."


scene ev rin_wet_arms onlayer master:
    center
    xalign 0.0 subpixel True
    linear 20.0 xalign 1.0
with flash

"Ihre Arme, durch den Mangel an Benutzung zu fast nichts außer Knochen und Haut degeneriert, sehen sehr kurz aus, jetzt wo die langen Ärmel ihrer Uniform sie nicht bedecken."


"Da das in mir keine negative Reaktion hervorruft, denke ich, dass ich mich tatsächlich ziemlich an die vielfältigen physischen Abnormalitäten meiner Schulkameraden gewöhnt habe."





"Ich habe mich immer gefragt, warum Rin ihre Hemdsärmel lang lässt und sie nur mit einem schlichten Knoten dort zusammenbindet, wo der Ellenbogen sein sollte."


"Es scheint ein bisschen unpraktisch, aber andererseits liegt ihr praktisches Denken auch nicht wirklich."


"Vielleicht gefällt es ihr, vielleicht ist es irgendwie wichtig für sie. Vielleicht hat es auch keine tiefere Bedeutung."


"Ich würde sie gerne fragen, und tue es auch fast, aber Rins miserabler Zustand erfordert meine Aufmerksamkeit dringender."


scene ev rin_wet_face_down onlayer master:
    center
    yalign 0.0
with flash

"Sie hat ebenfalls aufgehört zu reden, nachdem wir die Begrüßung hinter uns gebracht haben."


"Ich schätze, Plaudern ist dann unnötig."


scene ev rin_wet_towel_down onlayer master
with charachange

"Ich nehme das Handtuch vom Bett, wickle es ihr um den Kopf und rubbele so lange über ihre Haare, bis das meiste des Regenwassers hoffentlich von dem Stoff aufgesogen worden ist."


scene ev rin_wet_towel_up onlayer master
with charachange

"Sie wirft mir unter dem Handtuch mit teilnahmslosen Augen einen Blick zu."


"Es sieht aus, als wollte sie etwas sagen, ohne es zu sagen."


"Diese Art von Blick ist es."


"Doch von ihrem Gesicht kann ich nicht ablesen, was sie denkt. Darum trockne ich einfach weiter mit dem Handtuch ihre Schultern und Haare."


"Die Stille ist bedrückend, furchterregend."


"Die Kommunikation zwischen uns wurde plötzlich auf die Bewegungen meiner Hände und des Handtuchs reduziert, und Rin bewegt ihren Körper hin und her."


"Meine raue und ihre leise Atmung versuchen einen gemeinsamen Rhythmus zu finden, der einfach nicht da ist."


"Ich glaube, ich kann ihren Herzschlag spüren, oder vielleicht ist meiner nur doppelt so schnell."


"Als ich eine abstehende Haarsträhne hinter ihr Ohr streife, drückt Rin plötzlich ihre Wange an meinen Handrücken."


"Der Kontakt ist elektrisch; ein Stromstoß jagt durch mich hindurch."


scene ev rin_wet_towel_touch onlayer master
with charachange

"Ob sie Trost sucht, Wärme oder einfach nur meine Berührung, kann ich nicht wissen, doch ich kann nicht widerstehen, sie ebenfalls zu berühren und ihre zarte Wange mit meiner Hand zu liebkosen."


"Und mit geschlossenen Augen… küsst sie mich auf die Finger und zählt die Gelenke mit ihren Lippen."


"Ich bin traurig über meine Ausdrucksfähigkeit hinaus."


"Hier sind wir. Junge und Mädchen, beide in einander verliebt – oder so etwas in der Art. Oder vielleicht auch nicht… und doch…"


$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "Etwas ist kaputt, ich kann es in mir und Rin spüren; in der Art, wie sich unsere Blicke lediglich streifen; wie wir vor Kontakt zurückscheuen; in ihrer verschlossenen, schüchternen Haltung und in meiner Art, wie ich sie wie eine Porzellanpuppe berühre – ängstlich, ihre zarte Gestalt zu zerbrechen."


n "Wir sind uns näher, als wir es je waren, und ich bin trotzdem nicht glücklich. Es ist wie gestern."


n "Wann wurde aus Zärtlichkeit und Aussichtslosigkeit ein und dasselbe Wort? Warum rufen Akte der Zuneigung nur Sehnsucht hervor? Wie… warum ist es mit uns dazu gekommen?"


n "„Nein, beantworte das nicht”, würde ich mir gerne sagen, doch gegen die Allwissenheit der Selbstwahrnehmung zu kämpfen, ist eine aussichtslose Sache."


n "Trotzdem… bin ich hier. Rin ist hier. Und es kommt mir vor, als könnte sie in der Lage sein, ihre Probleme zu lösen – was immer sie auch sein mögen."


n "Und wenn sie es kann, wieso sollte ich es dann nicht können? Warum nicht wir zusammen?"


n "Es wirkt, als wäre diesen Schritt zu wagen zu viel, zu schwierig, zu ungewiss."


n "Darum ist alles, was ich im Moment tun kann, sie abzutrocknen, damit sie nicht noch einmal eine Erkältung bekommt."


$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

scene ev rin_wet_face_up onlayer master
with charachange

window show

"Ich streichle ihren Kopf und versuche, ihr Haar zu richten, das sich trotz der Nässe weigert, an Ort und Stelle zu bleiben."


"Ein paar dunkler, glasiger Augen folgen jeder meiner Bewegungen."


hi "Hose auch?"


scene ev rin_wet_face_down onlayer master
with charachange

"Sie nickt als Antwort, lehnt sich zurück und spreizt die Beine mit einer grotesk einladenden Geste. Ein unangenehmes Gefühl steigt meine Wirbelsäule empor wie eine schlechte Vorahnung."


"Allerdings ist das nicht genug, um mich zu ernüchtern, da ich in der Stille anfange, mich zu fühlen, als sei ich von mir selbst losgelöst."


"Ich bewege mich automatisch, ohne auch nur darüber nachzudenken, ob ich es sollte. Ich sollte mit ihr darüber reden, oder zumindest über irgendetwas."


"Die Stille ist ein Bann. Ein Pakt, der uns an diese abgeschiedene Welt gebunden hat, bestehend aus dem dumpfen Geräusch des Regens und dem sanften Gefühl ihrer Haut unter meinen Fingern."


"Der Knopf ihrer Hose ist fest geschlossen, doch er öffnet sich überraschend leicht."


"Die Hose auszuziehen ist schwierig – größtenteils weil sie auf ihr sitzt, ohne die Absicht aufzustehen, um mir die Arbeit zu erleichtern."


scene unlock_evh rin_h2_pan_surprise onlayer master
show evh rin_h2_pan_surprise onlayer master:
    xalign 0.5 yalign 0.0
with whiteout

"Ich knie mich unbequem und erregend zwischen ihre Beine, damit ich rasch ihre nackten Füße trocknen kann. Dass sie für sie so wichtig sind wie Hände für mich, habe ich nicht vergessen."


"Während ich mich mit dem Handtuch von ihren Knöcheln aufwärts arbeite, streift Rin mit ihrem Schenkel gegen meine Wange und stupst mein Kreuz mit ihrer Ferse, um mich näher heranzuziehen."


"Ich sehe aufwärts, um ihren stillen, starrenden Blick einzufangen, der nur darauf gewartet hat, dass ich aufsehe."


"Dieser unaufdringliche, erwartungsvolle Blick scheint zu sagen, dass ich jetzt am Zug bin."


"…"


"Flüchtig streife ich mit meiner Hand die Innenseite ihres Schenkels."


show unlock_evh rin_h2_pan_away onlayer master
show evh rin_h2_pan_away onlayer master
with charachange

"Die Berührung lässt sie scharf Luft einziehen, als hätte sie bisher versucht, ihren Atem anzuhalten."


"Was passiert dann, wenn ich das hier tue?"


show unlock_evh rin_h2_pan_closed onlayer master
show evh rin_h2_pan_closed onlayer master
with charachange

"Der kleine Kuss, den ich auf ihrem Oberschenkel platziere, ist genug, um Rin ihre Fassung verlieren zu lassen. Sie schließt ihre Augen und quiekt fast unhörbar."


"… Willst du das auch? Wäre es jetzt in Ordnung? Diesen Schritt zu wagen?"


show evh rin_h2_pan_closed onlayer master:
    subpixel True
    acdc_warp 8.0 yalign 1.0
with None

"… Was wenn? Wenn ich vielleicht…"


"Vage Gedanken schweben irgendwo in meinem benebelten Hinterkopf."


"Irgendwie macht diese ganze Situation es schwer zu denken – als ob mein Kopf voll mit Watte wäre."


"Aber das ist okay. Es scheint, als wäre Denken etwas, das wir gerade nicht brauchen."


label de_R41h:
show evh rin_h2_nopan_closed onlayer master:
    yalign 1.0
with Dissolvemove(0.5)

$ renpy.music.play(music_heart, fadein=0.5, if_changed=True)

"Da Rins Höschen beträchtlich weniger Stoff hat als ihre Hose, ist es wesentlich einfacher auszuziehen."




"Es verschwindet aus meinem Blickfeld und gleitet ihre Beine hinab."


"Es scheint, als hätte ich mit dem Handtuch schlechte Arbeit geleistet, da Rins Beine immer noch nass vom Regen sind."


"Na ja, was soll's."


show evh rin_h2_hisao_closed onlayer master
with charachange

"Mehr von Instinkt als von Vernunft gelenkt komme ich näher und koste eine andere Art von Feuchtigkeit."


"Sie antwortet mir, den langsamen Bewegungen meiner Zunge auf ihrer Haut, den Küssen auf ihrem Fleisch."


"Ihre Muskeln spannen sich an und lockern sich in diesem Rhythmus, als wäre es unangenehm."


"Zu hören, wie Rin versucht, kein Geräusch zu machen, als ich an ihr sauge, ist… irreal."


"Dieser ganze Morgen war so unwirklich wie die surreale Unfassbarkeit eines Traumes."


"Ich kann nicht glauben, dass ich das gerade tue. Mit ihr, jetzt. Doch ich lasse mich einfach von dem Moment leiten."


"Außerdem gab es schon vor tausend Kilometern kein Zurück mehr."


"Ich bewege mich umher, versuche, mit ihr Dinge anzustellen, ihre Schwachstellen zu finden, sie zu reizen, sie durch Lust in den Wahnsinn zu treiben, weil ich es will."


"Doch weder quietscht sie noch windet sie sich. Vielleicht kann ich Rin nicht noch wahnsinniger machen, als sie schon ist – egal, was ich tue."


"Ihre flatternde, schwere Atmung, gemischt mit unverständlichem Stöhnen, ist die einer Irren. Aber die Ursache bin nicht ich."


"Ich befreie sie nur davon."


"Sie wird feuchter und feuchter. Dabei trinke ich von ihr und spüre, wie es in mir immer heißer wird."


"Ich versuche, ihre tiefsten Stellen zu erreichen. Alles von ihr zu spüren, was ich auf diese Weise erreichen kann."


"Jede meiner Handlungen stößt auf eine andere Reaktion, doch all diese stammen aus purer Lust."


show evh rin_h2_hisao_closed onlayer master:
    subpixel True
    acdc_warp 16.0 yalign 0.0
with None

"Rin ist in Begierde versunken. Gewillt, alles mit sich machen zu lassen, solange ich es jetzt sofort tue."


"Sie nähert sich immer weiter dem Moment der Befreiung, doch der Weg dorthin ist ein Steilhang des Wahnsinns."


"Dennoch geht sie ihn."


"Ihre Muskeln entspannen sich nicht mehr zwischen den Wellen aus ekstatischen Krämpfen."


"Rin wird immer angespannter und kontrahiert so stark, dass es schmerzhaft sein muss. Doch ich gebe nicht nach."


"Ich mache weiter, und ich weiß, dass sie es auch will. Sie will es verzweifelt."


"Ein Bein wickelt sich um meine Schultern und zieht mich näher an sie heran. So nah, dass ich glaube zu ersticken."


"Ich mache weiter, weil es die einzige Möglichkeit ist."


stop music fadeout 8.0
stop ambient fadeout 12.0

"Als ich sie dazu bringe, nach Luft zu schnappen, sie dadurch ihr Bein krampfhaft um meinen Rücken klammert und ihren Verstand dem Gefühl hingibt… Genau in diesem Moment scheine ich alles zu vergessen, was sein sollte; was hätte sein sollen."


"Alles, was ich weiß, ist, dass sie hierhergekommen ist und… irgendwann auch ein Handtuch im Spiel war, glaube ich."


"Nichts davon ist wichtig. Alles, was zählt, ist dieser Moment."


"Ihr Orgasmus durchfährt auch mich und erregt mich auf eine komplett neue Art."


"Es macht mich beklommen, nervös. Ängstlich."


show evh rin_h2_hisao_away onlayer master:
    yalign 0.0
with Dissolvemove(0.5)

"Als sich ihr Körper entspannt, versuche ich, sie erneut dort unten zu küssen, aber es erschreckt sie und lässt sie zusammenzucken."


show evh rin_h2_hisao_surprise onlayer master
with charachange

rin "Nein… Hisao… Das reicht."


rin "Komm her."


scene bg school_dormhisao_rn onlayer master
with locationchange

"Ich stehe auf, um das letzte Stück Kleidung auszuziehen, das Rin noch trägt."


"Sie lehnt sich gegen mich, um zu Atem zu kommen. Dabei kitzelt mich ihr warmer Atem, der durch mein Hemd dringt."


"Blindlings greife ich hinter sie und erfühle mir den Weg zwischen ihre Schulterblätter, um den Verschluss zu finden, der ihren BH festhält."


"Er öffnet sich einfacher als gedacht und fällt irgendwo auf den Boden."


play music music_romance fadein 10.0

scene ev rin_pair_base_clothes onlayer master
show rp_hisao normal onlayer master at truecenter
show rp_rin normal onlayer master at truecenter
with whiteout

"Ihre nackte Haut an meinem Körper ist ein so wunderbares Gefühl, dass ich mehr davon haben will. Also umarme ich sie."


"Rins Haar riecht nach Regen, und ich bemerke, dass ich den Klang des Regens nicht mehr höre."


"Es ist ernüchternd. Das Polster, das uns in unsere eigene Realität gehüllt hat, ist nun fort, und mir wird klar, was gerade passiert."


show rp_hisao frown onlayer master
with charachange

hi "Weißt du, das ist wirklich nichts, was Freunde tun sollten."


"Flüstere ich und bemerke dabei, dass so eine simple Angelegenheit wie Sprechen manchmal überwältigend schwierig sein kann."


show rp_rin talk onlayer master
with charachange

rin "Wirst du nicht mehr mein Freund sein?"


"Sie flüstert das so nah an meinem Ohr, dass es kitzelt."


"Das habe ich zwar nicht gemeint, aber ihr ernster Ton und die Vielschichtigkeit dieser Frage lassen mich innehalten."


show rp_hisao smile onlayer master
with charachange

hi "Nee."


show rp_rin smile onlayer master
with charachange

rin "Ich… glaube, es ist vielleicht in Ordnung. Sogar wenn du es tätest."


"Ich umarme sie und lächle in ihr Haar hinein. Ausnahmsweise mal verstehe ich Rin perfekt."


show rp_rin frown onlayer master
with charachange

rin "Du bist nass."


"Die Wasserreste auf ihrer Haut sind in mein Hemd gesickert."


"Irgendwie machen mich gerade sogar ihre Feststellungen über das Offensichtliche glücklich."


show rp_hisao normal onlayer master
with charachange

hi "Du hast Recht. Bin ich, aber es ist deine Schuld."


show rp_rin normal onlayer master
with charachange

rin "Ich will dich sehen."


play sound sfx_rustling

scene ev rin_pair_base onlayer master
with charachange

"Ich willige ein und trete einen Schritt zurück, um die Knöpfe meines Hemdes zu öffnen – viel schneller als noch bei Rins Knöpfen."


"Ein plötzliches Gefühl der Eile überkommt mich und drängt mich voranzustürmen."


"Jede Sekunde, die ich Rin nicht berühre, ist Verschwendung, eine verlorene Chance."


"Meine Gürtelschnalle stellt sich als Hindernis heraus, obwohl ich sie unter normalen Umständen in einem Augenblick öffnen kann."


show rp_rin closed onlayer master
with charachange

"Während ich daran herumfummle, bemerke ich nicht, wie Rin mit ihrem Fuß näherkommt, bis sie anfängt, mit ihrem Zeh meine Brust entlangzufahren."


show rp_hisao frown onlayer master
with charachange

"Ich schaue hinab, um zu sehen, was sie sich ansieht."


hi "Mein Herz…"


"Reflexartig zucke ich zurück und bedecke das Narbengewebe in der Mitte meiner Brust."


"Das flache Mal, das der Eingriff nach meiner Herzattacke auf meinem Körper hinterlassen hat, ist bereits verheilt, aber… Na ja, es ist kein besonders schöner Anblick – wenn auch nicht unbedingt abstoßend."


"Es ist kaum sichtbar, doch sie hat ein Auges fürs Detail. Hat sie deshalb gesagt, dass sie mich sehen will?"


"Wegen all des Ärgers mit Rin hatte ich es irgendwie vergessen, aber nun kommen die ganzen unangenehmen Dinge, die ich mit meinem Zustand verbinde, wieder zum Vorschein und brausen durch meinen Kopf wie eine Sturzflut."


"Und, oh Gott, all die Geschichten über alte Kerle, die beim Sex Herzattacken bekommen… Was wenn…"


show rp_rin talk onlayer master
with charachange

rin "Hisao."


"…"


"Als ich bemerke, dass ich damit vielleicht gerade die Stimmung vermasselt habe, fallen mir keine passenden Worte ein."


show rp_hisao normal onlayer master
with charachange

hi "Ah… sorry, es ist nur…"


show rp_rin smile onlayer master
with charachange

rin "Lass mich dich berühren."


"Ihre Augen sind temperamentvoll und einladend, als sie dort splitternackt ohne ein Anzeichen von Scham sitzt. Ich hätte nie gedacht, dass Rin so aussehen könnte."


$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\nJepp, so sollte es nicht ablaufen."


n "Obwohl Rin genau hier ist, obwohl es keine Fragen mehr geben sollte, keine Hindernisse, nicht diese irritierende Gefühl, dass andauernd irgendetwas falsch ist…"


n "Das gleiche Gefühl, das mein Herz gestern schon ergriffen hat, taucht auf."


n "Wir sind zusammen – auf eine Art, die sich nur schwer definieren lässt."



n "\nWäre eine Beziehung wie diese in Ordnung? Könnten wir uns je ändern, um uns näherzukommen?"


n "Auch wenn wir für alle Ewigkeit zusammen bleiben, finden wir vielleicht nie zu gegenseitigem Verständnis."


n "Doch so etwas wie Ewigkeit gibt es nicht. Das könnte bedeuten, dass wir nicht für immer zusammen sein werden."


n "Wenn nicht unsere Unterschiede, dann wird der Fluss der Zeit uns mit unaufhaltsamer Kraft auseinanderreißen."


nvl clear

n "\n\nRin ist ein Wesen des Augenblicks, der Laune und des Impulses."


n "\nIch bin nichts dergleichen."


n "\nDas ist eine Tatsache, die ich ganz eindeutig verstehen kann."


n "Wenn schon aus keinem anderen, dann sollte ich den Moment aus diesem Grund ergreifen. Selbst wenn dies der einzige Moment ist, den wir jemals haben werden, sollte ich ihn nicht verderben."


n "Selbst wenn ich nicht vor mir selbst fliehen kann. Rin kann es auch nicht, das weiß ich jetzt."


n "\nWir beide haben Dinge, die wir nicht loslassen können; Dinge, die wir nicht {b}nicht{/b} denken können."


n "Gefühle, die wir nicht {b}nicht{/b} fühlen können."


n "Aber sie erlaubt es sich, mich ohne Hemmung zu wollen. Hier und jetzt."


$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

show rp_hisao frown onlayer master
with charachange

window show

hi "Es tut mir leid, weißt du…"


show rp_rin closed onlayer master
with charachange

rin "Hisao, du musst wirklich aufhören, dir Sorgen zu machen."


"Rin unterbricht mich, bevor ich weitersprechen kann. Und das ist gut so, denn ich weiß nicht, was ich hätte sagen können."


"Ihre Stimme, frei von ihrer sonstigen Verträumtheit, tadelt mich sanft – ohne jegliche Schärfe."


show rp_rin smile onlayer master
with charachange

rin "Du musst wirklich lernen loszulassen."


"Sie beäugt mich ruhig, fast berechnend."


"Ich frage mich, wie ich wohl in ihren Augen aussehe."


"Verdammt. Sie sind so grün, dass es fast wehtut."


"Ich war immer so von ihren Augen verzaubert. Diese mysteriösen, fesselnden Augen, die immer rastloser waren, als gut für sie war."


"Doch ich war von ihnen auch immer eingeschüchtert."


"Ja. Rin ist einschüchternd – auf mehr als nur einer Ebene, und besonders jetzt gerade."


"Sie ist erschreckend klar. Die Gänsehaut auf ihrer Haut sagt aus, dass ihr kalt ist, oder dass sie auch Angst hat."


"So oder so nehme ich mich zusammen, gehe wieder auf Rin zu und umarme sie, um sie wieder in meinen Armen zu spüren und um meine Zweifel zu verbannen."


"Der Anblick ihrer sanften, liebenden Augen scheinen diese Zweifel wie den letzten Winterschnee wegzuschmelzen."


scene evh rin_h_closed onlayer master
with whiteout

"Sie presst ihren Kopf gegen meine Schulter und sucht eine Stelle, auf der sie ruhen kann. Sie lehnt sich gegen mich und ich mich gegen sie."


rin "Lass los."


"Ja."


scene evh rin_h_left onlayer master
with charachange

rin "Du solltest Sachen wie Zukunft und Vergangenheit vergessen. Es ist nicht so, als könntest du diese Dinge ändern."


"Ich wollte ihr etwas sagen, aber ich habe meine Stimme verloren. Darum murmle ich ihr lediglich etwas Unverständliches zu."


rin "Du solltest jetzt einfach bei mir sein."


"Vielleicht hat sie verstanden, was ich sagen wollte, ohne dass ich es sagen musste."


rin "Komm her."


hi "Ich bin hier."


scene evh rin_h_normal onlayer master
with charachange

rin "Komm näher."


"Alle negativen Gedanken fallen von mir ab, darum tue ich es und umarme sie fester."


scene evh rin_h_right onlayer master
with charachange

rin "Näher."


"Ich drücke meinen Unterkörper gegen Ihren."


"Sie verkrampft etwas. Nur ein bisschen."


scene evh rin_h_closed_close onlayer master
with characlose

rin "Näher."


"Ihre letzte Bitte klingt eher wie ein Gebet."


"Es gibt nur eine Art, wie wir uns noch näher sein können als jetzt."


"Ich greife zwischen uns nach unten und führe mich in sie hinein."


scene evh rin_h_strain_close onlayer master
with charachange

"Jeder Muskel in Rins Körper spannt sich zur gleichen Zeit an."


scene evh rin_h_strain onlayer master
with charadistant

"Weder sagt sie etwas noch zuckt sie zusammen, also sinke ich tiefer, und bewege mich schließlich wieder hinaus."


"Und erneut. Und sie bewegt sich mit mir."


"Unsere Bewegungen verschmelzen zu einer, in einem fortwährenden Wechsel aus Vor und Zurück, Rein und Raus."


"Alle Sinne werden schärfer – um das Zehnfache verstärkt."


"Mein Gehirn hat vor langer Zeit aufgehört, all diese Stimulation zu verarbeiten, und nun habe ich keine Wahl, als all das mit meinem ganzen Körper zu fühlen."


"Genauso ist es für Rin auch, ich weiß es. Ich kann es sehen. Ich kann es spüren."


"Sie atmet scharf ein und aus, verliert gänzlich die Fassung und Grazie und atmet warm gegen meine Schulter."


"Zwischen diesen fragilen Atemzügen küsst sie mich manchmal zärtlich, sanft, als wäre sie sich unsicher, wie man das richtig anstellt."


"Doch es gibt kein Zögern."


"Sie klammert sich verzweifelt an mich und zieht mich näher an sich heran, damit ich sie vollständig ausfüllen kann. Sie bewegt sich gegen mich, um mich, sodass es schwierig ist zu sagen, wo ich ende und sie anfängt."


"Wir gehen es langsam an. Unerträglich langsam. Als ob wir alle Zeit der Welt hätten, obwohl wir nur diesen Moment und nichts darüber hinaus haben."


"Diese Gefühl ist—{w=0.7}{nw}"


scene evh rin_h_normal_close onlayer master
with characlose

rin "Warte…"


"Ich höre etwas beunruhigt auf, mich zu bewegen."


"Vielleicht tut es weh, oder…"


scene evh rin_h_right_close onlayer master
with charachange

"Sie sieht mich auf eine Art an, die ich nicht einmal ansatzweise interpretieren kann."


rin "Ist es das?"


hi "… Hä?"


rin "Du hast gesagt, ich muss nicht allein sein."


scene evh rin_h_left_close onlayer master
with charachange

"Ihre Augen schauen mich unschuldig aber irgendwie auch verwirrt an, sodass ich schmunzeln muss und ihren Hinterkopf streichle."


hi "Ja. Genau das meinte ich."


hi "Dass du jemanden hast, zu dem du kommen kannst, wenn du vom Regen durchnässt bist."


hi "Es bedeutet, dass du nicht allein bist."


hi "Wenn es so jemanden für dich gibt."


scene evh rin_h_closed_close onlayer master
with charachange

"Sie antwortet mit einem Kuss, der mich daran erinnert, dass wir ohne besonderen Grund aufgehört haben, uns zu bewegen."


"Also fangen wir von vorne an, fast gleichzeitig, und spiegeln den Rhythmus des jeweils anderen."


"Ich bewege mich schneller. Schneller in sie hinein und schneller aus ihr heraus. Mein Schweiß vermischt sich mit ihrem und glitzert auf unserer Haut wie Diamanten und Perlen."


scene evh rin_h_strain onlayer master:
    truecenter
    zoom 1.2 subpixel True
    easein 20.0 zoom 1.0
with charadistant

"Sie bewegt sich schneller und reibt sich fast schon verzweifelt gegen mich."


"Der berauschende Duft ihrer Lust, das kopfleerende Gefühl, das unsere Körper verbindet, das Gefühl, dass der letzte Rest rationalen Denkens aus meinem Verstand weicht."


"All dies verbrennt mein Bewusstsein genauso wie das unwiderstehliche Gefühl in meinem Körper meine Instinkte verbrennt."


"Während diese Gefühle zunehmen, macht Rin keine Anstalten aufzuhören."


"Sie wickelt ihre Füße um meine Hüfte und zwingt mich so tief in sie hinein wie körperlich möglich. Jeder Millimeter jagt Wellen der Lust durch mein Rückgrat."


"Mein Verstand verdunkelt sich, als die Welt in einem Blitz aus hellem Weiß explodiert."


stop music fadeout 2.0
stop ambient fadeout 2.0

window hide

scene white onlayer master
with Dissolve(2.0)

$ suppress_window_after_timeskip = True

with Pause(4.0)


label de_R42:

window hide None

scene white onlayer master
with None

$ renpy.music.set_volume(0.1, 0.0, channel="music")
play music music_timeskip fadein 4.0

centered_b "Gegenwart{fast}" with Dissolve(4.0)


nb "„Gegenwart” ist flüchtig und bestenfalls ein vages Konzept.\n"

extend "Der Moment zwischen Vergangenheit und Zukunft?\n"

extend "Das hat gar nichts zu bedeuten.\n"

extend "Zu lange über Dinge nachzudenken, die keinen Sinn ergeben, ist Zeitverschwendung.\n"

extend "Darum ist es am besten, in der Gegenwart zu leben.\n"

extend "Außerdem… Für uns, die wir die Zukunft nicht vorhersehen können und die Vergangenheit zu leicht vergessen, ist die Gegenwart wirklich der einzige Beweis unserer Existenz.\n"

extend "Auch wenn Existenz weitergeht, selbst wenn man sie für eine Weile vergisst, ist es hin und wieder gut, den Tag zu nutzen."



centered_alive "Auf diese Weise… kann man sicher sein, dass man…"



show alivetext "Auf diese Weise… kann man sicher sein, dass man…" onlayer master


with None


show alivetext "Auf diese Weise… kann man sicher sein, dass man… am Leben ist." onlayer master


with Dissolve(3.0)

$ renpy.pause()

stop music fadeout 4.0

scene bg school_dormhisao onlayer master
with Dissolve(4.0)

window show Dissolve(2.0)

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_dreamy fadein 4.0

"Ich bin mir ziemlich sicher, dass das Mädchen, das dort halbnackt aus dem Fester meines Zimmers schaut, ein viel besseres Verständnis von „Gegenwart” hat als ich."


"Was mich betrifft… Na ja, ich bin wegen meines gegenwärtigen Zustandes irgendwie verwirrt, da ich versuchen sollte, mein Hemd zu finden anstatt auf Rins Hintern zu starren."


"Aber ich kann einfach nicht aufhören, sie anzusehen."


scene bg misc_sky onlayer master
show hisaowindow onlayer master
show rinpan relaxed_nonchalant_close onlayer master at center
with locationchange

"Sie ist so nah am Glas, dass ihre Nase wahrscheinlich eine Abdruck hinterlassen wird."


"Zumindest tut ihr Atem das, wenn er am vom Regen gekühlten Fensterglas kondensiert, bevor er wieder verschwindet."


"Mein Herumgewirbel, um mich anzuziehen, weckt Rin nicht aus ihrer Nachdenklichkeit. Was auch okay ist, wirklich. Ich habe nicht mehr so viel gegen das Schweigen wie früher."


"Erst nachdem ich fast fertig damit bin, mir mein Hemd zuzuknöpfen, sagt Rin etwas – immer noch ohne mich dabei anzusehen."


show rinpan relaxed_boredom_close onlayer master
with charachange

rin "Lass uns irgendwo hingehen."


hi "Wohin?"


"Ich kann nur annehmen, dass sie mich und nicht das Fensterbrett einlädt, aber damit bin ich wohl auf der sicheren Seite."


show rinpan basic_lucid_close onlayer master
with charachange

rin "Ich hab's."


hi "Was?"


show rinpan basic_deadpan_close onlayer master
with charachange

rin "Hilf mir beim Anziehen."


show rinpan basic_awayabsent_close onlayer master
with charachange

rin "Ich glaube, es ist heute."


show rinpan basic_deadpanupset_close onlayer master
with charachange

rin "Komm schon, Klamotten."


"Klamotten, Klamotten… Was für ein ungeduldiger Ton."


"Ich knie mich hin, um ihren BH vom Boden aufzuheben, der in der Eile des Entkleidens weggeworfen und vergessen wurde."


"Als ich ihn wie einen toten Fisch zwischen meinen Fingern hängen lasse, kriecht die gleiche Zögerlichkeit in meinen Kopf, die mich schon ergriffen hat, als ich Rin ausgezogen habe."


"Kann ich mit Intimität wirklich so schlecht umgehen?"


show rinpan basic_deadpancontemplation_close onlayer master
with charachange

rin "Na komm, Ausziehen ging doch ganz gut. Es ist das gleiche nur andersherum. Wie rückwärts sprechen."


show rinpan basic_deadpan_close onlayer master
with charachange

rin "Chafnie reba tsi ,gireiwsch tkriw."


"Verblüfft von ihrer plötzlichen und gewaltigen Zurschaustellung von Denkvermögen, vergesse ich, ihr Gebrabbel wieder zu entschlüsseln."


"Ich bin mir ziemlich sicher, dass ich auch mit etwas Übung nicht so einfach flüssig rückwärts sprechen könnte."


hi "Ähm, könntest du das noch mal sagen?"


show rinpan basic_lucid_close onlayer master
with charachange

rin "Chafnie reba tsi ,gireiwsch tkriw."


"…"


hi "Geht klar. Na gut, ich werd's mal ausprobieren."


"Rin hatte Recht, der Verschlussmechanismus ist simpel genug. Beim dritten Versuch gelingt es mir, die kleinen Plastikhaken richtig zu verhaken."


hi "So."


show rinpan basic_deadpandelight_close onlayer master
with charachange

rin "Netchir nhi ud tssum tztej."


hi "Was? Bitte hör auf damit, ich spreche kein Rückwärtsisch."


show rinpan basic_lucid_close onlayer master
with charachange

"Sie schüttelt ihren Kopf, als müsste sie das Rückwärts-Denken mit einer physischen Geste vertreiben."


"Ich kenne ein paar Leute, die von so einer Fähigkeit profitieren könnten."


show rinpan relaxed_nonchalant_close onlayer master
with charachange

rin "Ich komme nicht weiter. Du musst ihn richten."


hi "Richten?"


show rinpan basic_deadpan_close onlayer master
with charachange

rin "Hab ich doch gerade gesagt."


hi "Nein, ich hab dich gefragt, was du damit meinst."


show rinpan basic_lucid_close onlayer master
with charachange

rin "Na ja, so, dass sie… in Ordnung sind."


"Oh, in Ordnung sagst du?"


"…"


"Da ich keine Ahnung habe, wann ihre Brüste „in Ordnung” sind, fummle ich letztendlich für eine gute Weile an ihrer Brust herum, ohne wirklich weiterzukommen."


"Nicht, dass ich mich beschweren würde, aber Rin tut es."


show rinpan basic_deadpanupset_close onlayer master
with charachange

rin "Emi kann das besser als du."


"Ihr ungeduldiger Ton geht mir auf die Nerven, auch wenn ich nicht wirklich widersprechen kann. Rin scheint plötzlich in einer furchtbaren Eile zu sein."


hi "Tut mir ja leid. Könnte es daran liegen, dass sie ein {b}Mädchen{/b} ist und sich damit auskennt?"


show rinpan basic_deadpanamused_close onlayer master
with charachange

rin "Ich glaube nicht, sie hat ungefähr genauso viel Brust wie du."


"…"


stop music fadeout 5.0

hide rinpan onlayer master
show rin basic_absent_close onlayer master
with shorttimeskip

"Als ihr BH und ihre Brüste schließlich so „in Ordnung” sind, wie sie sollten, ist der Rest ihrer Klamotten wesentlich leichter anzuziehen."


hide rin onlayer master
with charaexit

"Rin stürmt auf die Tür zu, obwohl ihr Hemd nicht einmal ganz zugeknöpft ist."


"Ohne eine Wahl zu haben, renne ich ihr hinterher."


$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_soothing fadein 2.0
play ambient sfx_parkambience fadein 0.5

scene bg school_gardens onlayer master
with locationskip

"Sobald ich bemerke, dass wir auf dem Weg zu dem Seiteneingang sind, der zum Wald führt, glaube ich zu wissen, wohin Rin will – auch wenn ich nicht sagen könnte, warum sie dorthin will."


"Andererseits kann ich nicht davon ausgehen, dass meine Vermutung auch nur annähernd richtig ist – nicht einmal, wenn man „richtig” sehr großzügig definiert. Schließlich geht es hier um Rin."


$ renpy.music.set_volume(0.6, 0.5, channel="ambient")
$ renpy.music.set_volume(0.8, 0.5, channel="music")

scene bg school_forest1 onlayer master
with locationskip

"Der Wald hinter der Mauer riecht nach Regen. Die letzten Regentropfen tropfen immer noch vom nassen Unterholz auf den Waldboden, obwohl der Regen schon seit einer Weile vorüber ist."


"Rin gibt ein gemütliches Tempo vor, sodass ich genug Zeit habe, die beruhigende Atmosphäre auf mich wirken zu lassen."


"Ich glaube, ich kann hören, wie Rin mindestens drei verschiedenen Bäumen hallo sagt, als sie an ihnen vorbeiläuft. Aber ich ignoriere es – genauso wie die Bäume."


"Wie vermutet, führt sie mich zu dem schmalen Seitenpfad, der zu den Hügelspitzen hinaufführt."


scene bg worrytree onlayer master:
    truecenter
    yalign 1.0
with locationchange

"Ich werfe einen Blick durch das Blätterdach, um einen Regenbogen zu finden, doch es scheint keinen zu geben."


"Es ist perfektes Wetter für Regenbögen. Die Sonne steht tief, und der Regen ist nicht allzu lange her."


"Na ja, was soll's."


$ renpy.music.set_volume(0.7, 0.5, channel="ambient")
$ renpy.music.set_volume(0.6, 0.5, channel="music")

scene bg school_forest2 onlayer master
with locationchange

"Ich senke meinen Blick von den Baumkronen, um den hageren Rücken des Mädchens zu sehen, das langsam den Hügel hinaufsteigt, ohne ihr Gleichgewicht zu verlieren."


"Ein paar Schritte vor mir auf dem Pfad, aber immer noch in meiner Reichweite."


"Ich glaube nicht, dass ich je einen Regenbogen erreichen könnte, aber bei Rin… scheint es weniger unmöglich als gestern noch."


$ renpy.music.set_volume(1.0, 0.5, channel="ambient")
$ renpy.music.set_volume(0.4, 0.5, channel="music")

scene bg school_hilltop_border_summer onlayer master
with locationchange

"Der klare Himmel, der uns über der Wiesenlichtung begrüßt, sieht riesig und wunderschön aus."


"Ein starker Wind hält die Regenwolken vom Dorf fern und bläst sie auf die andere Seite der fernen Berge."


"Der Anblick ist schön, aber…"


"…"


stop music fadeout 6.0

show dandelionsbg thin onlayer master
show dandelionsfg thin onlayer master
with None

"Aus dem Augenwinkel sehe ich kurz einen weißen Fleck durch die Luft fliegen. Als ich mich in die Richtung drehe, ist er bereits verschwunden."


"Ein weiterer folgt, dann ein dritter."


"Bevor ich mich versehe, fliegen überall um uns herum dutzende kleine Büschel aus Weiß."


show rin basic_delight behind dandelionsfg onlayer master at center
with charaenter

rin "Schau, die Blumen."


"Ah. Jetzt verstehe ich."


$ renpy.music.set_volume(1.5, 0.5, channel="ambient")
$ renpy.music.set_volume(1.0, 0.0, channel="music")

scene bg school_hilltop_summer onlayer master
show dandelionsbg dense onlayer master
show dandelionsfg dense onlayer master
with locationchange

play music music_comfort fadein 0.5

"Das Meer aus Löwenzahn, das die Hügelspitze bei unserem letzten Besuch bedeckt hat, hat sich über die Tage verändert."


"Wo vorher ein helles Gelb war, ist nun ein flauschiges Weiß."


"Einige der Blumen haben schon ihre Samen fortgeschickt, doch viele warten immer noch auf einen geeigneten Windstoß."


"Heute mangelt es nicht an diesen Böen. Hin und wieder schütteln sie das Gras gründlich durch, und kurz darauf ist die Luft plötzlich mit Löwenzahnsamen erfüllt."


"Einer nach dem anderen trennen sich die Samen vom Blütenkopf und werden hinfortgetragen."


"Ein alltägliches Ereignis. Jedoch eines, das Rin aus irgendeinem Grund zu faszinieren scheint."


$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

show rin negative_spaciness behind dandelionsfg onlayer master at center
with charaenter

"Sie dreht ihren Kopf von Seite zu Seite und bestaunt die Veränderung, die überall um sie herum passiert, als die Samen davonfliegen."


"Ich betrachte sie ebenfalls. Mein Blick folgt den weißen Büscheln, die mit dem Wind in Richtung Horizont schweben, und ich bilde mir ein, dass ich sie sogar noch sehen kann, nachdem sie schon aus meiner Sicht verschwunden sind."


"…"


show rin basic_awayabsent onlayer master
with charachange

rin "Hisao."


hi "Was denn?"


show rin basic_absent onlayer master
with charachange

rin "Liebst du mich?"


"Ich bin mit einem Mal hellwach und sehe ihr plötzlich sehr ernstes Gesicht, das sich nicht mehr nur die Blumen ansieht."


"Was für eine schwierige Frage, einfach so aus dem Nichts."


"Trotzdem zwingt mich ihre Unverblümtheit zu einer schnellen Antwort."


hi "Ich weiß nicht. Vielleicht tue ich das."


"Vielleicht zu schnell."


show rin basic_deadpannormal onlayer master
with charachange

rin "Was heißt das?"


hi "… Ich weiß es nicht."


show rin basic_lucid onlayer master
with charachange

"Rin seufzt. Vielleicht ist sie mit meiner laschen Antwort nicht zufrieden. Ich wäre es auch nicht."


show rin relaxed_nonchalant onlayer master
with charachange

rin "Ich auch nicht."


show rin relaxed_boredom onlayer master
with charachange

rin "Ich glaube nicht, dass ich viel über Liebe weiß."


hi "…"


hi "… Das ist doch okay, oder?"


show rin basic_lucid onlayer master
with charachange

"„Woher soll ich das wissen?”, scheint ihr Schulterzucken zu sagen. Sie zögert, eine entschlossenere Antwort zu geben."


"Sie bleibt nur eine Sekunde zu lang still, doch selbst diese Sekunde ist nicht genug, um mich vorausdenken zu lassen…"


show rin basic_absent onlayer master
with charachange

rin "Ich liebe dich."


"Diese drei Worte lassen mich erstarren wie ein Hase, der von Scheinwerfern erfasst wird. Aber ich bin kein Hase und ich starre nur in Rins Augen, die viel, viel zu teilnahmslos wirken, für das, was sie gerade von sich gegeben hat."


show rin basic_deadpanupset onlayer master
with charachange

"Allerdings sieht Rin ziemlich ernst aus – bis sie ihre Zunge herausstreckt, ihre Stirn runzelt und mich damit noch mehr verwirrt, als es ihre Worte schon getan haben."


"Warum sieht sie leicht unglücklich aus?"


"War das ein Geständnis ihrer tiefsten Gefühle? Ein Test, um zu sehen, wie ich reagieren würde? Ein Test, um zu sehen, wie sie reagieren würde?"


show rin basic_awayabsent onlayer master
with charachange

rin "Es schmeckt komisch."


hi "… Schmeckt?"


show rin basic_lucid onlayer master
with charachange

rin "Ja. So komisch."


"Sie lacht – ich hoffe aus Nervosität – aber sie hört mittendrin auf, als sie bemerkt, sie seltsam es klingt."


show rin negative_spaciness onlayer master
with charachange

rin "Wie… Ich weiß nicht was. Ich… glaube nicht, dass es ein Wort dafür gibt."


"Rin spricht weiter, als hätten ihre Worte keine Bedeutung. Scheinbar unsinnige Worte fallen von derselben Zunge, die gerade die wichtigeren geformt hat."


show rin negative_worried onlayer master
with charachange

rin "Ein Wort für… ähmmm…"


"Nur, dass."


show rin negative_annoyed onlayer master
with charachange

rin "… es ist wie…"


"Sie die."


show rin basic_deadpanupset onlayer master
with charachange

rin "…"


"Worte nicht finden kann."


show rin basic_sad onlayer master
with charachange

rin "…"


"Rin starrt mich lediglich weiter an und stammelt mit ihren Worten, als wäre ihr Gehirn plötzlich zum Stillstand gekommen."


"Sie sieht furchtbar verwirrt aus – so wie ich mich fühle, während ich auf ihre Erklärung warte."


"Doch sie kommt nicht. Sie blinzelt nur ein paar Mal. Das Flattern ihrer langen Wimpern zieht meine Aufmerksamkeit auf sich, weil der Rest von ihr wie versteinert aussieht."


"Bis ich begreife, wogegen sie angekämpft haben."


show rin basic_crying onlayer master
with charachange

"Es sind wieder diese seltsamen Tränen, die nichts mit Traurigkeit oder Glücksgefühlen zu tun haben. Kein bemitleidenswertes Schluchzen oder Lachen aus Freude."


"Nur Tränen. Spontan und ohne Vorwarnung, wie dieses eine Mal in ihrem Klassenzimmer."


rin "Ah."


"Nur ein paar von Ihnen. Nicht genug, um einen Wirbel darum zu machen. Daher versucht Rin auch nicht, sie zu verbergen – selbst nachdem sie sie bemerkt hat."


"Rin weint und sieht dabei aus, als hätte sie keine Ahnung warum. Und irgendwie wächst ein großes Unbehagen in meiner Brust, als ich in ihre wässrigen Augen sehe, die direkt in meine starren."


"Er versteinert mich ebenfalls – der Schock der Unbegreiflichkeit dieser Situation."


"Ich weiß einfach nicht mehr, was hier gerade passiert."


hi "Rin? Was ist los?"


rin "Ich…"


show rin negative_crying onlayer master
with charachange

"Sie schüttelt verwirrt ihren Kopf und hat Probleme damit, die Wörter aus ihrem Mund hervorzubringen."


show rin basic_crying onlayer master
with charachange

rin "Tschuldige…"


rin "Ich könnte ein wenig Angst vor dir haben."


"Die Worte werden langsam gemurmelt, mit einer leisen Stimme, die dem Gesagten genauso ungläubig gegenübersteht wie ich es tue."


hi "Was? Warum?"


show rin basic_sad onlayer master
with charachange

rin "Ich weiß es nicht. Das zu sagen, hat mir einfach Angst gemacht."


show rin basic_absent onlayer master
with charachange

rin "Menschen weinen, wenn sie Angst haben, oder?"


show rin basic_awayabsent onlayer master
with charachange

rin "Siehst du? Ich kann's auch."


"Nun wendet sie ihren Blick hab und versucht absichtlich, mich nicht anzusehen. Es verwirrt mich – zumindest genauso sehr wie das, was sie von sich gibt."


show rin negative_annoyed onlayer master
with charachange

rin "Ich… Manchmal will ich… bei dir… will ich einfach weglaufen aber ich kann mich nicht bewegen es ist als würden sich meine Beine in Zitronen-Panna-Cotta-Pudding verwandeln und mein Herz fühlt sich an als würde es explodieren und…"


show rin negative_sad onlayer master
with charachange

"Sie lässt melancholisch ihre Schultern hängen."


rin "Ist dir so was schon mal passiert?"


"… Ich erinnere mich an den bleiernen Himmel über dem gefrorenen Wald und den Klang der blattlosen Äste, die aneinander klappern."


"Es ist wie eine Erinnerung aus einem anderen Leben."


hi "Ja. Einmal."


hi "Auch damals hat mein Herz sehr wehgetan."


show rin basic_surprised onlayer master
with charachange

rin "Aber ich dachte, dein Herz-Ding wäre nicht ansteckend?"


"Ich schüttle meinen Kopf und ein winziges, etwas gezwungenes Lächeln erscheint auf meinen Lippen."


"Die andere Krankheit meines Herzens könnte sehr wohl ansteckend sein, und es würde mich kein bisschen kümmern."


hi "Wovor hast du Angst? Ich hätte nie gedacht, dass ich unheimlich wäre."


show rin negative_confused onlayer master
with charachange

"Rin schüttelt verzweifelt ihren Kopf, als ob sie wüsste, dass der Wirrwarr in ihrem Kopf damit nicht einfach so zu lösen ist."


rin "Du gibst mir das Gefühl, ich sollte jemand anderes sein als ich."


show rin negative_sad onlayer master
with charachange

rin "Das ist unheimlich."


show rin negative_worried onlayer master
with charachange

rin "Es passiert, wenn du nett zu mir bist. So wie gestern."


rin "Ich weiß nie, was ich dann machen soll. Es ist schwierig."


"Ihr Stimme ist kaum hörbar. Ein geflüstertes Geständnis, das mir so peinlich wäre, dass ich es nicht einmal denken würde, geschweige denn es laut auszusprechen."


"Rin ist nie jemand gewesen, dem etwas peinlich war, darum spricht sie es laut aus und scheint nur aus Instinkt schüchtern zu sein."


show rin basic_upset onlayer master
with charachange

rin "Aber ich will etwas tun. Nur weiß ich nicht, ob dieses Ich es kann."


"Für einen Moment starren wir uns nur gegenseitig an, als ob wir darauf warten würden, dass der jeweils andere etwas sagt."


"…"


hide rin onlayer master
show rin basic_upset_close as rin2 onlayer master
with characlose

hi "Du bist so blöd."


hide rin2 onlayer master
show rin relaxed_surprised_superclose onlayer master at center
with characlose

"Rins Lippen schmecken salzig und ängstlich."


window hide

play sound sfx_heartslow
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack onlayer master
with Dissolve (0.4)

window show

"Als ich sie umarme, spüre ich, wie mein Herz schmerzhaft in meiner Brust klopft."


window hide

play sound sfx_heartslow
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack onlayer master
with Dissolve (0.4)

$ renpy.music.set_volume(0.5, 1.0, channel="music")
$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

nvl clear
nvl show dissolve

n "\n\nAuch wenn ich froh bin, dass sie solche Dinge sagen kann, machen sie mich trotzdem traurig."


n "Rins Geist, ihre Leidenschaft, ihre Stärke. All diese Dinge, die mir teuer sind, sind die, die sich nicht ändern sollen."


n "Wie sollte ich mit ihnen umgehen? Was wird aus ihnen werden? Ist ihre Zukunft unumstößlich anders als meine?"


n "Diese Ängstlichkeit wird niemals ihren Griff um mein Herz lockern, aber ich denke, ich kann lernen, damit zu leben."


n "Langsam klingt der Schmerz in meinem Herzen ab, und dann gleicht es seinen Rhythmus dem von Rins Herz an."


n "\n\nWir lauschen dem für einige Zeit."


n "…"


$ renpy.music.set_volume(1.0, 1.0, channel="music")
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
stop music fadeout 8.0

nvl hide dissolve
nvl clear

hide rin2 onlayer master
show rin basic_blush_close behind dandelionsfg onlayer master at center
with charadistant

window show

"Nachdem sich unsere Lippen getrennt haben, dauert es eine Weile, bis wir beide merken, dass wir nun etwas sagen können."


"…"


show rin basic_sad_close onlayer master
with charachange

rin "Siehst du?"


show rin relaxed_doubt_close onlayer master
with charachange

rin "Du bist wirklich ein netter Mensch – sogar wenn du es nicht bist."


rin "Das ist das Gruseligste überhaupt."


show rin relaxed_sleepy_close onlayer master
with charachange

rin "Ich glaube… dass deine Nettigkeit alles war, wovor ich je Angst hatte."


"…"


hi "Ist das schlecht? Auch wenn du Angst hast?"


show rin basic_lucid_close onlayer master
with charachange

"Sie denkt eine Weile darüber nach und runzelt dabei die Stirn, als wäre es eine schwierige Matheaufgabe."


show rin basic_deadpanamused_close onlayer master
with charachange

rin "Nein. Mir ist das recht. Es ist okay, solange du es bist."


"Wie ein Gewicht, das von meiner Brust genommen wird, erfreuen ihre Worte mein Herz und füllen es mit… Ich weiß nicht… Glück?"


"Was könnte es sonst sein?"


"Dieses Mal ist mein Lächeln aufrichtig."


hide rin onlayer master
show rin basic_deadpanamused as rin2 behind dandelionsfg onlayer master
with charadistant

"Rin tritt zurück und lächelt mich immer noch sanft an, genauso wie ich sie anlächle."


show dandelion full onlayer master:
    alpha 0.0 xalign 0.5 yanchor 1.0 ypos 1.2 subpixel True
    easein 1.0 ypos 1.0 alpha 1.0
with None
show dandelionbg behind dandelion onlayer master
show dandelions_blurbg behind dandelion onlayer master
show dandelions_blurfg behind dandelion onlayer master
hide dandelionsfg onlayer master
hide dandelionsbg onlayer master
with Dissolve(1.0)

hide rin2 onlayer master
show rin basic_deadpanamused behind dandelionbg onlayer master
with None

"Während sie sich ihr Gesicht an ihrer Schulter abwischt, pflücke ich einen runden, dicken Löwenzahn und bringe ihn an meine gespitzten Lippen."


show dandelion gone onlayer master
with Dissolve(1.0)

"Pfff…"


"Sie verteilen sich im Wind, der sie in die Höhe nimmt, um sie zu einer neuen Heimat zu tragen."


"Kaum zu glauben, dass sie vor ein paar kurzen Wochen noch so anders waren."


"Das ist Veränderung."


"…"


show dandelion gone onlayer master:
    easeout 1.0 alpha 0.0 yanchor 1.0 ypos 1.2
with None

hide dandelionbg onlayer master
hide dandelions_blurbg onlayer master
hide dandelions_blurfg onlayer master
show dandelionsbg dense behind rin onlayer master
show dandelionsfg dense onlayer master
with Dissolve(1.0)

hi "Hey, also sind die Blumen geworden, was sie werden sollten – wie du es das letzte Mal gesagt hast."


hi "Was ist mit dir? Bist du eine wahre Künstlerin geworden? Oder bist du es nicht, weil du weggerannt bist?"


show rin basic_deadpancontemplation onlayer master
with charachange

"Sie hält für eine Weile inne, um über meine Frage zu grübeln."


show rin relaxed_nonchalant onlayer master
with charachange

"… und zuckt mit den Schultern."


"Es bringt mich fast zum Lachen."


"Diese Unbeschwertheit ihrer Geste ist einfach liebenswert. Ein Symbol dafür, wie Rin wahrlich und wirklich, ohne jegliche Einschränkungen, die ganze Last der Welt von ihren Schultern stoßen kann, wenn sie es nur will."


"Sie ist auf alle nur denkbaren – und wahrscheinlich auch ein paar undenkbare – Arten… frei."


"Und ich glaube, ich könnte sie dafür lieben."


show rin basic_absent onlayer master
with charachange

rin "Ich glaube nicht, dass es etwas ausmacht."


show rin basic_deadpandelight onlayer master
with charachange

rin "Lass uns heute einfach die Wolken betrachten."


play music music_twinkle fadein 2.0

scene ev rin_goodend_1 onlayer master
show evbg rin_goodend_base onlayer master:
    center
    subpixel True xalign 0.0
    1.0
    easein 20.0 xalign 1.0
show dandelionsbg dense onlayer master
show rin goodend_1 onlayer master:
    center
    subpixel True xalign -0.5
    1.0
    easein 20.0 xalign 1.0
show dandelionsfg dense onlayer master
show evfg rin_goodend onlayer master:
    center
    subpixel True xalign -1.0
    1.0
    easein 20.0 xalign 1.0
with whiteout

"Sie läuft fünf Schritte, um auf einen großen Felsen zu klettern, damit sie hoch wie möglich stehen kann und stellt sich auf ihre Zehenspitzen."


"Wenn man nach den Wolken greift, zählt jeder Zentimeter."


hi "Sicher, lass uns die Wolken betrachten. Ab und zu ist es gut, etwas zu tun, das man wirklich tun will."


rin "Ja. Du hast wahrscheinlich Recht."


"Ich schaue hinauf zum blauen Himmel hoch über uns."


"Es ist eine tiefe, himmelblaue Weite, die sich über mein gesamtes Sichtfeld und hinaus erstreckt."


"Dennoch bleibt Rin auf ihrem Felsen stehen und starrt auf den fernen Horizont, an dem die Regenwolken weiter von uns weg gleiten."


rin "Ich habe etwas beschlossen."


"Dieser verträumten Stimme, gesprochen zum Wind, der sie zu meinen Ohren trägt, hört man die Entschlossenheit nicht an, aber mir entgeht sie keineswegs."


rin "Es ist doch in Ordnung, ich zu sein."


$ renpy.music.set_volume(0.5, 1.0, channel="music")
$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

window hide
nvl clear
nvl show dissolve

n "\n\n\nEs ist in Ordnung? Ihre Entscheidungen scheinen immer ziemlich… ausgefallen zu sein."


n "Na ja, ich schätze, das ist eine wichtige Erkenntnis."


n "Mit sich selbst ins Reine zu kommen, sich selbst zu akzeptieren, sich mit dem zufrieden zu geben, was man ist."


n "Ein schlichter Vorsatz des Herzens, der für manche Menschen erdrückend schwierig ist – wenn nicht gar unmöglich."


n "Ich begreife sehr wohl, dass ich auch einer dieser Menschen sein könnte."


n "Rin ebenfalls…"


n "Vielleicht sind wir am Ende doch nicht so verschieden."


n "Vielleicht muss man sich erst selbst akzeptieren, damit man jemand anderen akzeptieren kann."


n "Vielleicht ist das ein notwendiger Schritt, den wir bis jetzt noch nicht gemacht haben."


$ renpy.music.set_volume(1.0, 1.0, channel="music")
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

nvl hide dissolve
nvl clear
window show

"Wenn ich sie so auf dem Felsen stehen sehe, glaube ich, dass sie finden kann, wonach auch immer sie suchen mag."


"Und ich kann es auch."


show ev rin_goodend_1b onlayer master
show evbg rin_goodend_base onlayer master:
    subpixel False xalign 1.0
show rin goodend_1b onlayer master:
    subpixel False xalign 1.0
show evfg rin_goodend onlayer master:
    subpixel False xalign 1.0
with charachange

"Der Wind ergreift ihr Haar und ihre Kleidung. Rin öffnet ihre kurzen Arme für eine Umarmung, die so unglaublich winzig ist, aber so groß, wie es ihr jemals möglich sein wird. "


"Für einen Augenblick sieht es so aus, als könnte sie selbst abheben, und ich muss mich zurückhalten, damit ich nicht nach ihrer Schulter greife, um sie zu mir zurückzuziehen."


"Doch dieses Bild ist etwas, das ich nur betrachten kann. Etwas, an das ich mich erinnern werde."


"Rins Ärmel flattern frei im Wind, ihr Haar wird von ihm wild zerzaust, ihre Haut von der untergehenden Sonne berührt."


"Ihre schlanke Gestalt, die ich zu lieben gelernt habe, zittert im kalten Wind, der die kleinen weißen Flecken an ihr vorbeiträgt – jeder Einzelne der Beginn einer neuen Blume."


"All das ist in mein Herz eingraviert."


"Wie diese winzigen, im Wind verstreuten Samen, bin ich mir sicher, dass Rin auch ihren Platz in dieser Welt einnehmen kann, ohne dass sie ihre eigene in sich erschaffen muss."


"Vielleicht glaubt sie es auch, und während sie dem Himmel so nah wie möglich ist, gibt sie der Welt eine große Umarmung."


"Auf mich wirkt es, als könnte die gesamte Welt wirklich dort hineinpassen – zwischen ihre kleinen Arme, in diese allumfassende Umarmung."


show ev rin_goodend_2 onlayer master
show rin goodend_2 onlayer master
with charachange

rin "Hisao?"


"Sie sieht mich auf die gleiche Weise an, wie sie meinem Namen sagt – sorglos über ihre Schulter, mit einer seltsamen Freude in ihrer Stimme und ihren Augen."


show evbg rin_goodend_base onlayer master:
    subpixel True yalign 0.0
    acdc_warp 12.0 zoom 1.15
show rin goodend_2_hires onlayer master:
    subpixel True yalign 0.0 xalign 1.0 zoom 0.769
    acdc_warp 12.0 zoom 1.0
    subpixel False
show evfg rin_goodend onlayer master:
    subpixel True yalign 0.0
    acdc_warp 12.0 zoom 1.45
with None

"Ich blicke in diese mysteriösen, dunklen Augen, die neugierig unter ihrem kastanienbraunen Haar funkeln."


"Obwohl ich zu weit weg bin, um es zu sehen, bin ich mir sicher, dass sie mein Abbild reflektieren."


hi "Was ist denn?"


rin "Wie nennt man das, wenn es sich im Herzen so anfühlt, als wäre alles auf der Welt in Ordnung?"


stop music fadeout 4.0
stop ambient fadeout 4.0

window hide

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
