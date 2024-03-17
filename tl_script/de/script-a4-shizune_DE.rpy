label de_S30:

window hide None

scene bg school_library onlayer master
with locationchange

window show

play music music_happiness fadein 2.0

"Nur einen Tag später beginnt schon das Wochenende."
"Ich lasse einen schweren Stapel Bücher auf den Bibliothekartisch fallen. Der Knall war ungewollt, aber er ist so schwer, dass ich nichts dagegen tun konnte."


$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_impact

show yuuko panic_up onlayer master:
    center
    ypos 1.2 alpha 0.0
    easein 0.25 ypos 1.0 alpha 1.0
with vpunch

show yuuko panic_up onlayer master:
    center
    alpha 1.0
with None

"Yuuko springt so heftig von ihrem Stuhl auf, dass sie fast ihre Brille verliert. Sie kann sie gerade noch festhalten."


show yuuko neutral_up onlayer master
with charachange

yu "Oh, hi."


hi "Entschuldige. Ich bin hier, um endlich all diese Bücher zurückzubringen."


show yuuko worried_down onlayer master
with charachange

yu "Das ist toll, aber ich wünschte, du hättest sie früher zurückgebracht. Es wäre kein Problem, wenn die Bibliothek mehr Exemplare von allem hätte, aber das hat sie nicht… und sie tun so, als ob es mein Fehler wäre."


hi "„Sie”?"


show yuuko panic_down onlayer master
with charachange

yu "Andere Schüler. Sie können… ähm, sehr aufdringlich sein."


hi "Tut mir leid. Ich hab's einfach irgendwie vergessen. Es sind ein paar ziemlich harte Tage gewesen."


show yuuko worried_down onlayer master
with charachange

yu "Oh… Ähm, ich vermute, dass du nicht darüber reden willst…"


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\nKleinlaut wendet sich Yuuko wieder dem Protokollieren der Bücher zu, die ich zurückgebracht habe. Sie behandelt sie mit äußerster Sorgfalt und Genauigkeit, als müsste sie nicht nur Bücher registrieren, sondern eine Bombe entschärfen."


n "Während der letzten paar Tage habe ich über etwas nachgedacht, was Misha gesagt hat. Natürlich habe ich über alles von ihr nachgedacht, aber speziell eine Sache geht mir immer wieder durch den Kopf. Sie sprach darüber, dass sie niemandem mehr verlieren oder auch nur daran denken will, sich von einem Freund trennen zu müssen."


n "Als ich an diese Worte zurückgedacht habe, haben sie mich vollends aus ausgebremst – wie ein heftiger Schlag auf die Wange. Nur noch ein paar Monate, dann machen wir unseren Abschluss. Misha und Shizune waren nahezu unzertrennlich, aber danach sehen sie sich vielleicht nie wieder. Ich frage mich, ob dieser Gedanke das alles losgetreten hat."


n "Wenn Misha versuchen würde, mit Shizune darüber zu reden, würde Shizune wahrscheinlich nicht einen Gedanken daran verschwenden. Es würde sie traurig machen – und darum würde sie versuchen es zu verdrängen. Für jemanden wie Shizune, der schnurstracks seine Sorgen unterdrücken kann, wäre das ein Leichtes."


nvl clear

n "\n\nMisha hat sich als sensibler herausgestellt, als es den Anschein hatte. Es hätte sie erdrückt – umso mehr, weil Shizunes Reaktion ziemlich kalt ausfallen könnte. Ich weiß nicht, ob Shizune es so gehandhabt hätte, aber es ist gut möglich. Und ich kann nachvollziehen, warum sie sich so verhalten würde."


n "Warum Misha von dem Gedanken geplagt wird, dass ein so wichtiger Mensch sich von ihr entfernt, kann ich ebenfalls verstehen. Bis zu jenem Zeitpunkt hatte ich nie über den Schulabschluss nachgedacht."


n "Dann fing ich an, Dinge zu denken wie: „War das wirklich nicht einmal ein Jahr?”. Ich begann, über alle Menschen nachzudenken, die ich getroffen hatte. Nicht nur Shizune und Misha, sondern auch alle anderen. Es waren warme Erinnerungen. Dann stellte ich mir vor, von ihnen getrennt zu sein. Plötzlich konnte ich Mishas Ängste verstehen."


n "\nEs wäre vielleicht schön, mit jemandem darüber reden zu können."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show

hi "Eigentlich hab ich irgendwie Lust dazu."


show yuuko worried_up onlayer master
with charachange

yu "Mit wem?"


"Ich spüre einen offensichtlichen Hauch von Besorgnis in ihrer Stimme."


hi "Mit dir."


show yuuko neurotic_up onlayer master
with charachange

yu "Ah… Wirklich? Bist du dir sicher? W-Warum ich?"


hi "Weil du eine Erwachsene bist."


show yuuko neurotic_down onlayer master
with charachange

yu "Nur deswegen? Ahhhhh… das ist…"


"Zusammenzuckend zappelt sie etwas auf ihrem Stuhl herum und versucht, es sich auf ziemlich unbequem aussehende Weise bequem zu machen. Ich schätze, das kann ich als Einverständnis interpretieren."


hi "Ist es schwierig, erwachsen zu sein?"


show yuuko cry_down onlayer master
with charachange

yu "Ja."


show yuuko panic_down onlayer master
with charachange

yu "Aber ich glaube nicht, dass ich so alt bin… Es ist verblüffend, dass Schüler w-wie du und Shizune jetzt Sachen wie Parfums oder Rasierwasser benutzen. Das habe ich nie… Und ich benutze so was bis heute nicht…"


show yuuko worried_up onlayer master
with charachange

yu "Ähm, außerdem, du hast dein Trauben-Rasierwasser heute nicht aufgelegt."


hi "Jepp, es hat doch nicht so gut zu mir gepasst."


show yuuko worried_down onlayer master
with charachange

yu "Oh, das ist gut. Ich habe dasselbe gedacht… Tut mir leid."


"Yuuko sieht aus, als ob es ihr wirklich leid tut, und ich spüre ein stechendes Schuldgefühl. Trotzdem lächle ich. So eine kleine Lüge kann auf mich zurückfallen, um mir in den Hintern zu beißen."


"Für Misha muss es niederschmetternd gewesen sein, so lange ihre wahren Gefühle zu verschleiern, um Shizune mit einem fröhlichen Gesicht gegenübertreten zu können."


hi "Jemand, den ich kenne, hat erwähnt, dass wir bald unseren Abschluss machen, und mir ist aufgefallen, dass ich noch nie darüber nachgedacht habe."


hi "Ich komme mir bescheuert vor, dass ich mir nie einen Gedanken über solche Sachen gemacht habe."
hi "Ich habe viele tolle Leute getroffen und nie darüber nachgedacht, wie es sein würde, wenn wir alle unseren Abschluss machen und uns vielleicht nie wieder sehen."


show yuuko neutral_down onlayer master
with charachange

yu "Es gibt immer noch andere Wege, wie ihr in Kontakt bleiben könnt…"


hi "Ja, schätze schon. Ich komme mir wie ein Kind vor. Ich weiß, dass alle wahrscheinlich dasselbe durchmachen. Ich wette, du hörst dieses Problem ziemlich oft."


show yuuko worried_down onlayer master
with charachange

yu "N-Nein… So lange arbeite ich hier noch nicht."


show yuuko worried_up onlayer master
with charachange

yu "Bei meinem Abschluss an der Oberschule hatte ich die gleichen Sorgen."
yu "Ähm, ich bin allerdings nicht auf diese Schule gegangen. Ich vermisse meine Freunde auch… und ich wünschte, ich hätte mich öfter bei ihnen gemeldet. Ich hätte mir mehr Mühe geben sollen."


"Yuuko hilft mir nicht wirklich dabei, mich besser zu fühlen, und als sie das in meinem Gesicht sieht, verstummt sie sofort."


hi "Ich will nicht zurückschauen und es dann genauso bereuen müssen."


hi "Ich frage mich, ob Shizune überhaupt über solche Dinge nachdenkt. Manchmal redet sie ausschweifend darüber, dass sie ohne irgendwelche Reue leben will."


show yuuko panic_up onlayer master
with charachange

yu "Wow… Das klingt unmöglich… für mich jedenfalls."


"Ich nicke aber stimme ihr damit nur halb zu."


show yuuko closedhappy_up onlayer master
with charachange

yu "Selbst dann… Ich denke, dass ist auch irgendwie bewundernswert. Fast schon tapfer. Findest du nicht auch?"


hi "„Tapfer” – so kann man es natürlich auch nennen."


show yuuko neutral_down onlayer master
with charachange

"Yuuko schüttelt beharrlich ihren Kopf."


yu "Aber es stimmt. Und es ist auch irgendwie einschüchternd…"


hi "Mensch. Du solltest dich von Oberschülern nicht einschüchtern lassen."


show yuuko worried_up onlayer master
with charachange

yu "Ich versuch's…"


hide yuuko onlayer master
with charaexit

"Sie wendet sich ab, um einen Notizzettel wieder und wieder zu falten. Ziemlich müßiges Verhalten für eine Studentin, aber noch viel wichtiger: Ich frage mich, ob ich etwas Falsches zu ihr gesagt habe."


"Da ich schon so lange mit Shizune zu tun habe, kann ich es nicht lassen, so viel wie möglich in einen Moment der Stille hineinzuinterpretieren."


"Wenn Yuuko die Art von Mensch wäre, die sich nicht von Oberschülern einschüchtern lässt, wäre es wahrscheinlich nicht so einfach, mit ihr zu reden."


"Es ist allzu leicht, ein paar seiner eigenen negativen Eigenschaften ablegen zu wollen. Wenn ich an all meine Bekannten denke, sind es diese Eigenschaften, die ich am meisten mag."


show yuuko worried_up onlayer master at center
with charaenter

yu "Ähm…"


show yuuko smile_down onlayer master
with charachange

yu "Ich glaube, ich bereue es nicht wirklich. Ich denke, es reicht, dass ich mich an die schönen Zeiten erinnern kann."


show yuuko worried_down onlayer master
with charachange

yu "Ich weiß es nicht… Entschuldige."


"Ich bemerke, dass allmählich ein paar Schüler in die Bibliothek trudeln und beschließe, dass meine Zeit um ist."


hi "Nein, das hat geholfen."


hi "Mir kommt es vor, als ob zwei meiner Freunde sich streiten, weil einer von ihnen die Tatsache, dass wir uns nach unserem Abschluss vielleicht nicht mehr sehen können, sehr zu Herzen geht."
hi "Und der anderen scheint es nichts auszumachen, was das Ganze nur noch schlimmer macht."


hi "Ich weiß nicht, wie ich mit dieser Situation umgehen soll. Es scheint nicht die Art von Problem zu sein, bei dem ich mich am Ende für eine Seite entscheiden muss. Aber es könnte dazu kommen, und ich habe keine Ahnung, was ich dann tun soll."


show yuuko neutral_down onlayer master
with charachange

yu "Du solltest ihnen sagen, dass sie sich nicht streiten sollen."


hi "Ich weiß. Streit ist schlecht."


hi "Es sind übrigens nicht Shizune und Misha, nur so nebenbei."


show yuuko worried_up onlayer master
with charachange

yu "Okay… ähm, auch wenn ich das nicht wirklich gedacht habe…"


"Wie peinlich. Auch wenn ich wusste, dass es so kommen würde, kann ich spüren, wie meine Wangen rot werden. Auch so war diese Lüge so was von durchsichtig und offensichtlich. Aber es kann sein, dass das manchmal der richtige Weg ist."


hi "Hast du irgendwelche Bücher über Menschen, die schwere Entscheidungen treffen müssen?"


show yuuko happy_down onlayer master
with charachange

yu "Wir haben eine Menge Selbsthilfe-Bücher…"


"Es ist lustig, dass mich das verblüfft – denn vor ein paar Monaten noch hätte es das nicht."


hi "Ich meinte „über”, nicht „für”. Davon gibt es nicht viele, stimmt's?"


show yuuko worried_down onlayer master
with charachange

yu "Ja. Ähm, nicht viele, meine ich."


stop music fadeout 3.0

"Auch wenn ich deswegen ein paar Bedenken habe, will ich mit Shizune sprechen. Ich weiß nicht, warum mich das so nervös macht, und es widert mich etwas an."


scene bg school_council onlayer master
with locationskip

"Es motiviert mich auch, sie hier und jetzt suchen zu gehen, obwohl das keine allzu große Herausforderung ist. Sie ist im Schülerratszimmer, wie immer."


play music music_pearly fadein 5.0

show shizu behind_blank onlayer master at center
with charaenter

"Beunruhigenderweise ist Misha nicht bei ihr. Als Shizune mich bemerkt und von ihrem Papierkram aufsieht, erkundige ich mich zuerst nach ihr."


show shizu basic_normal2 onlayer master
with charachange

ssh "Ich weiß es nicht."


"Ihr Antwort beinhaltet so viel Ungewissheit, dass ich sie damit einfach nicht davonkommen lassen kann."


his "Sie verpasst eine Menge Unterricht."


show shizu adjust_happy onlayer master
with charachange

ssh "Bist du die Anwesenheitspolizei?"


his "Echt seltsam, dass das von der Schülerratspräsidentin kommt."


show shizu adjust_smug onlayer master
with charachange

"Shizune verbirgt ein Lachen hinter ihrer Hand, und ich fange an zu glauben, dass ich mir vielleicht wegen nichts Sorgen mache. Doch dann geht ihr Lachen langsam in einen ernsteren und nachdenklicheren Gesichtsausdruck über."


show shizu basic_normal onlayer master
with charachange

ssh "Du hast Recht."


show shizu behind_blank onlayer master
with charachange

ssh "Gestern…"


show shizu adjust_happy onlayer master
with charachange

"Ich erhasche die Andeutung eines wissenden Lächelns auf ihrem Gesicht, als sie meine schäbig verschleierte Panik bei diesem Wort erkennt. Obwohl sie sich große Mühe gibt, kann sie es sich bis zum bitteren Ende nicht verkneifen, andere zu überraschen."


"Aber selbst dann erkenne ich an ihrem schnell verschwindenden Lächeln, dass sie größere Sorgen hat."


show shizu basic_angry onlayer master
with charachange

ssh "… bevor ihr beide mich bemerkt habt, habe ich gesehen, worüber ihr gesprochen habt. Ich bin nicht dumm."


show shizu behind_frown onlayer master
with charachange

ssh "Hätte ich es nicht, hätte ich immer noch Misha durchschauen können, während wir zurückgelaufen sind."
ssh "Selbst wenn sie mir später nicht alles erzählt hätte. Sie hat keine große Sache daraus gemacht, aber egal wie man es betrachtet – es ist meine Schuld, nicht wahr?"


his "Was hat sie dir erzählt?"


show shizu adjust_frown onlayer master
with charachange

"Shizune zuckt bei dieser Frage zusammen, obwohl sie sie ganz klar erwartet hat. Ihre Antwort folgt mit einer großen Geste."


show shizu basic_normal2 onlayer master
with charachange

ssh "Eine Menge."


show shizu adjust_frown onlayer master
with charachange

ssh "Zum Beispiel, dass ich egoistisch sein kann. Und verwirrend. Ich versuche zu sehr, Leute um mich zu scharen – und dann stoße ich sie wieder weg."


show shizu basic_normal2 onlayer master
with charachange

ssh "Ich wusste nicht, was ich tun sollte. Ich dachte, sie hätte Recht damit, all diese Dinge zu erwähnen. Darum hab ich ihr einfach zugestimmt, aber das hat es nur verschlimmert."


show shizu behind_sad onlayer master
with charachange

ssh "Ich verstehe es nicht."


"Als sie ihre Brille richtet, sieht sie ziemlich müde aus. Ich hoffe, es liegt nicht daran, dass sie die ganze Zeit Misha gemieden hat. Aber die Möglichkeit schießt mir trotzdem durch den Kopf, wenn man den Verlauf dieser Unterhaltung betrachtet."


show shizu adjust_smug onlayer master
with charachange

ssh "Es ist wahr. Sogar dass es meine Schuld ist, dass der Schülerrat so klein ist und wir immer mit Arbeit überhäuft werden. Vielleicht habe ich mit diesem Verhalten viele Leute aus dem Schülerrat vergrault."


"Shizune wedelt schelmisch mit dem Finger, bekennend, dass „vielleicht” eine Untertreibung ist. Doch so erschöpft wie sie es tut, ist dieser Humor offensichtlich nur zu meiner Beruhigung, und daher nicht aufrichtig."


show shizu basic_normal onlayer master
with charachange

ssh "Lilly zum Beispiel. Sie war die Erste, die beigetreten ist, als ich angefangen habe, Leute für den Schülerrat zu suchen, nachdem alle anderen gegangen waren. Weil sie mich nicht leiden konnten, schätze ich."


show shizu adjust_happy onlayer master
with charachange

ssh "Wir haben es geschafft, das letzte Festival zu organisieren, und haben sogar in letzter Minute zusammen einen Stand betrieben."


show shizu behind_frown onlayer master
with charachange

ssh "Aber ich mochte sie nicht, weil ich sie für selbstsüchtig hielt. Sie hat uns oft im Stich gelassen, um sich um den einen oder anderen Freund zu kümmern, sodass die Probleme der Schule an Misha und mir hängengeblieben sind."


show shizu cross_angry onlayer master
with charachange

ssh "Wenn sie irgendwelche persönlichen Probleme hatte, hat sie uns sitzen gelassen. Sie ist dann in Panik verfallen und kam nicht wieder, bis es gelöst war."


show shizu adjust_angry onlayer master
with charachange

ssh "Sie hat sich zu hundert Prozent darauf fokussiert und sich so sehr darin vertieft, dass sie sich nicht mehr auf irgendwelche Schülerratsarbeiten konzentrieren konnte."


show shizu behind_frustrated onlayer master
with charachange

ssh "Für mich war das das Schlimmste – dass sie so nett sein und doch so viele Menschen als selbstverständlich betrachten konnte."
ssh "Warum dann überhaupt dem Schülerrat beitreten? Es kommt einem so kurzsichtig und egoistisch vor, meinst du nicht?"


show shizu basic_normal2 onlayer master
with charachange

ssh "Aber eigentlich bin ich diejenige, die so ist."


show shizu adjust_frown onlayer master
with charachange

ssh "Wie Misha sagte: Ich versuche immer, die Menschen zu mir zu ziehen und schließe sie dann aus."


show shizu behind_sad onlayer master
with charachange

ssh "Genau so hab ich sie behandelt, was mich zu einer schlechten Freundin macht. Und es kommt mir vor, als hätte ich dasselbe mit dir getan."
ssh "Ich schätze, dann bin ich auch eine schlechte Freundin für dich. Auch wenn Misha sagt, dass du sie genauso gut ersetzen könntest."


show shizu basic_normal2 onlayer master
with charachange

ssh "Ich bin wütend auf mich, dass ich die Dinge so sehr vermasselt habe, dass alles aus den Fugen gerät. Alles, was ich wollte, war…"


stop music fadeout 3.0

"Sie hält inne und sucht nach den richtigen Worten, während sie konzentriert ihre Finger aneinander legt."


show shizu behind_blank onlayer master
with charachange

ssh "… Menschen glücklich zu machen, glaube ich."


show shizu adjust_happy onlayer master
with charachange

ssh "Auch wenn das zu einfach ausgedrückt ist."


"Sie stützt ihren Kopf auf ihre Hand, und ihr Pony fällt über ihre Augen – ihre Augen, die hinter diesen polierten Brillengläsern versteckt sind und in dem schwachen Licht glänzen."


"Das zu denken ist vielleicht unpassend, aber gerade jetzt sieht sie besonders schön aus. Wie ein vollständigerer Mensch."


"Es scheint mir, als wäre das meine erste Chance, auf ihre ausströmenden Gefühle zu reagieren. Misha als Shizunes Übersetzerin ersetzen? Misha muss Witze machen."


"Es hat all meine Kraft gefordert, um bis jetzt mit ihr mitzuhalten. Sie gebärdet Gesten, die ich zuvor noch nie gesehen habe."


"Höchstwahrscheinlich hat sie sich über Jahre des Zusammenseins einige Gewohnheiten von Misha angeeignet. Ich könnte niemals jemanden ersetzen, der ihr so nahe ist."


his "Ich mag dich, weil ich dich mag – nicht, weil ich von dir hereingelegt wurde."


"Obwohl sie sich damit größte Mühe gegeben hat."
"Ich starre weiterhin direkt in ihre Augen. Als ich sie zum ersten Mal gesehen habe, kamen sie mir ein wenig einschüchternd vor. Wie die Augen eines Raubtiers. Das hat sich beruhigenderweise nicht geändert."


show shizu basic_normal onlayer master
with charachange

ssh "Ich will immer noch alle glücklich machen."


his "Angefangen bei Misha?"


play music music_shizune fadein 6.0

show shizu basic_frown onlayer master
with charachange

"Shizune sieht etwas verärgert aus, dass ich andeute, sie würde mit jemand anderem anfangen, und lächelt selbstbewusst, als wäre die Traurigkeit einer Freundin ein körperlicher Widersacher, den sie einfach zur Aufgabe drängen kann."


show shizu behind_frustrated onlayer master
with charachange

ssh "Natürlich. Offensichtlich. Selbstverständlich."



show shizu adjust_noglasses onlayer master
with charachange

"Sie nimmt ihre Brille ab und lehnt sich seufzend zurück in ihren Stuhl. Es ist das erste Mal, dass ich sie ohne Brille sehe, doch sie setzt sie so schnell wieder auf, dass ich gar keinen richtigen Blick erhaschen konnte."


show shizu behind_smile onlayer master
with charachange

ssh "Aber ich bin zu müde, um heute noch damit anzufangen. Gleich als Erstes morgen früh."


show shizu basic_normal onlayer master
with charachange

ssh "Willst du helfen?"


his "Klar."


show shizu adjust_happy onlayer master
with charachange

ssh "Und… ich hab auch noch anderes Schülerrats-Zeug, bei dem du mir helfen könntest, wenn du schon dabei bist."


"Allerdings stellt sich heraus, dass es gar nicht so viel andere Arbeit gibt."


stop music fadeout 2.0
$ suppress_window_after_timeskip = True

scene black onlayer master
with dissolve




label de_S31:

window hide None

scene black onlayer master
with dissolve

with Pause(2.0)

play sound sfx_doorknock

with Pause(2.0)

scene bg school_dormhisao onlayer master
with openeye

window show

play sound sfx_doorknock

"Heute ist Schulfrei. Darum dachte ich, dass ich ausschlafen könnte. Doch leider werde ich um acht Uhr Morgens von einem gnadenlosen Hämmern an meiner Tür aus meinem Schlaf gerissen."


"Zuerst dachte ich, dass es Kenji sein könnte, doch als meine genervten Rufe unbeantwortet bleiben, begreife ich, dass es Shizune ist."


play sound sfx_dooropen

scene bg school_dormhallway onlayer master
show shizu adjust_happy_close onlayer master at center
with locationchange

play music music_another fadein 0.5

show shizu behind_blank onlayer master at center
with charadistant

"Als ich die Tür öffne, tritt sie sofort ein paar Schritte zurück und versteckt etwas hinter ihrem Rücken. Ziemlich verdächtig."


his "Was ist das? Eine Überraschung? So was ist nicht wirklich mein Ding."


show shizu behind_frown onlayer master
with charachange

"Ihr unerfreutes Gesicht sagt mir, dass ich aufhören soll, so ein Spielverderber zu sein. Doch weil sie zu beschäftigt damit ist, mit dem Gegenstand hinter ihrem Rücken zu hantieren, kann sie es nicht gebärden."


show shizu adjust_smug onlayer master
with charachange

"Es muss sie frustriert haben, denn Sekunden später zaubert sie stolz und mit einem Hauch von Bedrohlichkeit den Gegenstand hervor. "


show shizu basic_happy onlayer master
with charachange


ssh "Ta-da. Ein Picknickkorb. Wir können zusammen mittagessen – wir drei."


"Es ist nicht wirklich ein Korb, es sieht eher nach einer Plastiktüte aus. Nach einem kurzen Blick hinein kann ich auch sehen, dass das enthaltene Essen aus dem Laden ist und nicht selbstgemacht. Teilweise kleben sogar noch die Preisschilder drauf."


"Aber sie hat sehr vielfältig eingekauft. Sogar eine kleine Konserve Kaviar. Langsam gefällt mir dieses Mittagessen immer mehr. Ich nehme eine Traube aus der Tüte und werfe sie mir in den Mund."


show shizu adjust_frown onlayer master
with charachange

ssh "Nimm dir nicht einfach so was raus! Ich hab die ganze Nacht damit verbracht, diese ultimative Waffe vorzubereiten."


show shizu adjust_frown onlayer master:
    ease 0.5 ypos 1.2
    ease 0.5 center
with Pause(0.5)

play sound sfx_pillow

show shizu basic_normal onlayer master:
    ypos 1.2
    ease 0.5 center
with charachange

"Shizune legt die Tüte auf den Boden, um ihre Hände frei zu bekommen, und fängt umgehend an, sie zwischen ihren Füßen hin und her zu schieben. Eindeutig etwas, das man nicht mit etwas tun sollte, das man eine „ultimative Waffe” nennt."


show shizu adjust_happy onlayer master at center
with charachange

ssh "Alles Teil meines „Mach-Misha-Wieder-Fröhlich”-Plans. Ich bin die ganze letzte Nacht wach geblieben, um daran zu arbeiten."


show shizu behind_smile onlayer master
with charachange

ssh "Als wir das letzte Mal versucht haben, etwas zu bestellen, hat Misha kaum etwas abbekommen und es als Ausrede benutzt, um früher gehen zu können."
ssh "Diesmal kommt sie mir nicht so leicht davon. Das Essen ist bereits hier; sie wird sich setzen und mit uns essen müssen."


show shizu basic_happy onlayer master
with charachange

ssh "Es ist der perfekte Köder. Sieht das nicht alles unwiderstehlich aus? Ich hab versucht, es selbst zu machen, aber ich weiß nicht, wie man es so schick aussehen lässt."
ssh "Darum hab ich einfach alles gekauft. Sieht doch trotzdem vorzüglich aus, oder nicht? Das sollte es auch."


"Sie ist heute sehr selbstbewusst. Sie ist begeistert von dem Gedanken, Misha wieder aufzumuntern. Auch wenn es seltsam ist, sie so glücklich darüber zu sehen, weiß ich, dass sie genauso unsicher ist wie gestern."


"Der einzige Unterschied ist, dass sie es nun als Art Herausforderung sieht. So kann sie ihre Sorgen zurückstellen und sich unbekümmert voll reinhängen."


"Bisher ist sie damit ganz gut gefahren. Es würde mich nicht überraschen, wenn das ihre einzige Lebensart wäre."


his "Aber es ist etwas früh…"


show shizu adjust_frown onlayer master
with charachange

ssh "Es ist schon acht Uhr morgens. Das ist spät! Sogar Misha steht um acht oder neun auf. Sie geht um 19 Uhr ins Bett, aber das ist unwichtig."


his "Es ist sehr wichtig."


show shizu basic_normal_close onlayer master
with characlose

"Shizune übergeht mich, indem sie meine Hände mit ihren festhält, anstatt mein Statement richtig zu entkräften. Dass sie meine Hände länger als erwartet in ihren hält, fühlt sich wirklich gut an."


show shizu adjust_happy_close onlayer master
with charachange

ssh "Worauf es ankommt ist, dass sie genau jetzt wach ist und irgendwo herumläuft. Lass sie uns suchen gehen."


scene bg school_courtyard onlayer master at bgleft
with locationskip

"Sie spurtet ungeduldig aus meinem Zimmer, während sie mich dabei hinter sich herzieht. Ihre Begeisterung erweckt in mir eher den Eindruck, dass ich einem Großwildjäger auf Safari folge, als jemanden, der eine Freundin finden will."


"Unsere Suche dauert nicht allzu lange. Auch kurzgeschnitten stechen ihre pinken Haare heraus. Dass sie gerade über den Schulhof schlendert, macht es noch einfacher…"
"Jetzt höre ich mich auch noch an wie ein Großwildjäger."


show shizu adjust_happy_close onlayer master at tworight
with charaenter

shi "…!"


hi "Misha!"


show mishashort hips_smile behind shizu at twoleft onlayer master
with charaenter

mi "Hm~?"


hi "Wir haben dich gesucht."


show shizu behind_smile_close onlayer master
with charachange

ssh "Es ist ein schöner Tag für ein Picknick, du solltest uns begleiten. Wir haben sogar Kaviar. Natürlich nicht vom Stör, aber er ist trotzdem sehr lecker."


show mishashort perky_confused onlayer master
with charachange

mi "Kaviar? Stör?"


"Weil sie es anscheinend nervig findet, alles mit nur einer Hand ausführlich zu erklären, gibt sie schnell auf."


show shizu adjust_frown_close onlayer master
with charachange

ssh "Fischeier."


show mishashort sign_confused onlayer master
with charachange

mi "Was?"


show shizu behind_smile_close onlayer master
with charachange

ssh "Sie sind lecker."


show mishashort cross_smile onlayer master
with charachange

mi "Sorry, Shicchan, ich denke, ich passe für heute."


show shizu basic_angry_close onlayer master
with charachange

"Als Misha weiterlaufen will, hält mir Shizune die Tüte entgegen, um ihre Hände frei zu kriegen."


hide shizu onlayer master
with None

show shizu basic_angry_close behind mishashort at tworight onlayer master
with None

show mishashort cross_smile onlayer master:
    ease 1.0 center
show bg school_courtyard onlayer master:
    ease 1.0 center
show shizu basic_angry_close onlayer master:
    ease 1.0 xpos 0.75
with Pause(0.5)
show shizu behind_blank onlayer master:
    tworight
    xpos 0.725
    ease 0.5 xpos 0.75
with charadistant

show mishashort perky_confused onlayer master at Position(xpos=0.35)
show shizu behind_blank onlayer master at Position(xpos=0.65)
show bg school_courtyard onlayer master at Position(xpos=0.43)
with dissolvecharamove

"Sobald sie aus ihren Händen ist, huscht sie vor Misha und schneidet ihr den Weg ab."


show shizu adjust_happy onlayer master
with charachange

ssh "Aber ich hab so viel Essen gemacht."


show mishashort perky_sad onlayer master
with charachange

mi "Sorry, ich hab gerade einfach keinen Hunger."


show shizu behind_blank onlayer master
with charachange

shi "…"


show shizu behind_frown onlayer master
with charachange

ssh "Wann wirst du dann Hunger haben?"


show mishashort hips_frown onlayer master
with charachange

mi "Shicchan, so etwas kann man nicht wissen~."


show shizu adjust_frown onlayer master
with charachange

ssh "Du kannst schätzen."


"Die Spannung zwischen ihnen erzürnt Shizune. Sie versucht, das Problem mit einem Frontalangriff zu lösen, aber diese Methode wird nicht funktionieren."


"Ich hatte gedacht und gehofft, dass Misha sich mittlerweile wieder aufgerappelt hätte, aber ich schätze, dass sie von den Geschehnissen schlichtweg zu tief getroffen wurde."


"In dem Fall kann ihr niemand wirklich helfen. Ich denke, dass Shizune das vielleicht bis zu einem gewissen Grad versteht. Falls nicht, würde sie gar keine Zweifel haben."


"Doch weil sie nicht sprechen kann, habe ich gelernt, ihr Zögern zu erkennen. Es ist eindeutig – sie könnte genauso gut schreien."


show mishashort sign_smile onlayer master
with charachange

hide mishashort onlayer master
with charaexit

stop music fadeout 5.0

"Weil sie diese Diskussion nicht weiterführen will, winkt Misha mit ihren Händen ab und macht sich zügig davon. Shizune kocht still vor Wut. Sie will Misha nicht ziehen lassen, hat aber auch keine Möglichkeit, sie festzuhalten."


"Während Mishas Rücken in der Ferne immer kleiner wird, frage ich mich, wo sie nun hingeht. Shizune beißt sich frustriert auf die Lippe – fragt sie sich das gleiche?"


"Ich will ihr beruhigend die Hand auf die Schulter legen, doch ich halte mich zurück, da ich nicht weiß, ob das jetzt das Richtige wäre."


"Nicht weil sie zerbrechlich, verletzlich oder traurig aussieht. Im Gegenteil. Nach einer Weile ist ihr Gesichtsausdruck frei von jeglicher Emotion. Lediglich Nachdenklichkeit ist zu sehen. Auf einmal dreht sich schnell um."


play music music_dreamy fadein 4.0

show shizu basic_angry onlayer master at center
show bg school_courtyard onlayer master at right
with dissolvecharamove

ssh "Jetzt wird das ganze Essen im Müll landen."


his "Sieht so aus."


show shizu behind_sad onlayer master
with charachange

ssh "Das macht mich wütend."


"Jedoch ist es offensichtlich, dass Shizune mehr verletzt als wütend ist. Die Tüte, die in meiner Hand baumelt, fühlt sich an, als wäre sie mit Blei gefüllt."


show shizu behind_blank onlayer master
with charachange

$ doublespeak(ssh, his, "Lass uns zusammen ausgehen.", "Dann essen wir es eben.")


show shizu adjust_blush onlayer master
with charachange

shi "…"


show shizu basic_normal onlayer master
with charachange

ssh "Wo willst du hingehen?"


his "Ich weiß nicht."


show shizu behind_blank onlayer master
with charachange

ssh "Das Dach."


show shizu adjust_happy onlayer master
with charachange

ssh "Das ist mein Lieblingsplatz."


"Ein schiefes Lächeln erscheint auf ihrem Gesicht und verschwindet genauso schnell wieder."


play ambient sfx_rooftop fadein 1.0

scene bg school_roof onlayer master
show shizu behind_frown_close onlayer master at center
with shorttimeskip

"Auf dem Dach öffne ich sofort den Kaviar und ignoriere dabei die ganze Zeit Shizunes höhnischen Blick. Schließlich stelle ich ihn postwendend wieder hin."


his "Wo sind die Toastecken?"


show shizu basic_normal2_close onlayer master
with charachange

ssh "Ich hab keine gemacht. Wie gesagt, ich hab alles gekauft."


his "Aber keine Toastecken…"


show shizu adjust_frown_close onlayer master
with charachange

ssh "Warum ist das wichtig? Außerdem verkaufen sie keine Toastecken. Das wäre bescheuert."


his "Ich wette, das tun sie."


show shizu behind_blank_close onlayer master
with charachange

ssh "Vielleicht in Läden für besonders Faule, aber nicht hier. Warum benutzt du nicht einen Tortilla-Chip?"


his "Ein Tortilla-Chip ist nicht das Gleiche."


show shizu basic_frown_close onlayer master
with charachange

ssh "Beide sind dreieckig. Hör auf, dich wie eine Prinzessin aufzuführen. Ich wusste nicht, dass man Kaviar auf eine spezielle Weise isst. Ich höre zum ersten Mal davon."


his "Es ist überhaupt nicht das Gleiche."


show shizu adjust_smug_close onlayer master
with charachange

"So kann ich nicht auf dekadent machen. Und außerdem – wie kann sie das nicht wissen? Sie lebt in einer riesigen Villa. In der Zwischenzeit ergreift Shizune die Gelegenheit, um das halbe Kaviarglas auf einen einzigen Chip zu schaufeln."


his "Hey!"


"Ich wette, so schmeckt es nicht einmal."


show shizu behind_smile_close onlayer master
with charachange

shi "…"


"Es ist viel zu viel Essen für zwei Personen."
"Weil wir während des Essens nicht miteinander kommunizieren können, haben Shizune und ich eine Menge Zeit, um über Misha nachzudenken – die Person, für die wir das alles gemacht haben, die aber nicht hier ist."


show shizu basic_angry_close onlayer master
with charachange

ssh "Es nervt mich, dass sie nicht hier ist. So kann ich nicht mal das Essen genießen."


"Ich schaue auf den noch halb mit Saft gefüllten Plastikbecher neben ihr."


his "Ich dachte, du wolltest nicht, dass das ganze Essen im Müll landet."


show shizu adjust_frown_close onlayer master
with charachange

ssh "Ich wollte auch, dass Misha hier ist. Das war der Sinn des Ganzen. Ich hab mein Ziel nicht erreicht, also schmeckt es auch nicht."


show shizu behind_blank_close onlayer master
with charachange

ssh "Du solltest es essen. Iss mehr."


his "Aber ich wollte die frittierten Sachen. Du hast alle weggegessen, obwohl du sagst, dass es dir nicht schmeckt."


show shizu basic_normal_close onlayer master
with charachange

ssh "Frittierte Sachen sind immer lecker. Die sind eine Ausnahme."


his "Du wirst noch fett."


his "Ich denke, du bist zu aggressiv."


show shizu behind_blank_close onlayer master
with charachange

ssh "Es ist, wie ich dir gestern gesagt habe. Ich versuche nur, sie aufmuntern."


his "Ja, aber es kommt eher so rüber, als würdest du einen Kreuzzug planen."


show shizu basic_normal2_close onlayer master
with charachange

ssh "Ich versuche nur, das Problem zu lösen."


show shizu behind_sad_close onlayer master
with charachange

ssh "… Und ich weiß nicht, wie ich es sonst lösen soll."


show shizu basic_normal2_close onlayer master
with charachange

ssh "Ich fühle mich so machtlos. Ich hasse es. Ich kann sie nicht einmal anschreien, auch wenn ich es wollte. Schreien ist für ernste Situationen, oder?"


his "So ziemlich."


show shizu adjust_frown_close onlayer master
with charachange

ssh "Du solltest Misha für mich anschreien. Du kannst ihr sagen, dass ich will, dass sie aufhören soll, so deprimiert zu sein. Auch wenn sie traurig ist und sich einsam fühlt, ist das kein Grund ewig so niedergeschlagen zu sein."


his "Warum tust du es nicht?"


show shizu basic_frown_close onlayer master
with charachange

ssh "Hab ich schon."


show shizu behind_blank_close onlayer master
with charachange

ssh "Bei einem Würfelspiel."


show shizu basic_happy_close onlayer master
with charachange

ssh "Über-Unter, um genau zu sein. Ich hab gewonnen! Fünf Mal!"


"Nur diese beiden wären so stolz darauf, ein reines Glücksspiel zu gewinnen."


show shizu adjust_frown_close onlayer master
with charachange

ssh "Dann hab ich versucht, mir ihr zu reden, aber offensichtlich lief das nicht allzu gut."


his "Na ja, das Gleiche hab ich auch getan. Versuch und Fehlschlag."


show shizu basic_normal2_close onlayer master
with charachange

ssh "Aber mein Ziel war es immer, alles besser zu machen."


his "Ja, deine Ausstechversuche sind rekordverdächtig."


show shizu behind_frustrated_close onlayer master
with charachange

ssh "Aber ich hatte auch Niederlagen…"


show shizu basic_normal2_close onlayer master
with charachange

ssh "Darum will ich deine Hilfe."


show shizu behind_sad_close onlayer master
with charachange

ssh "Ich weiß nicht mehr, was ich noch tun soll."


"Für jemanden wie Shizune, die seit jeher nur mit der Welt interagiert hat, indem sie jedes Hindernis in ihrem Weg auf die Hörner nimmt, ist das absolutes Neuland."


$ renpy.music.set_volume(0.5, 2.0, channel="music")
$ renpy.music.set_volume(0.5, 2.0, channel="ambient")

window hide

scene bg misc_sky onlayer master at Fullpan(30.0)
with locationchange

nvl clear
nvl show dissolve

n "\n\nIch will ihr sagen, dass sie sich keine Sorgen machen muss. Dass sie klasse darin ist, Menschen aufzumuntern. Denn das hat sie mit mir während meiner ersten Woche hier geschafft."


n "Rückblickend muss ich wie ein Arsch rübergekommen sein – seit dem Moment meiner Ankunft hatte ich ständig miese Laune. Auch wenn ich nicht glaube, dass das unberechtigt war."


n "Obwohl ich monatelang Zeit hatte, es zu verdauen, ist es schwierig, meinen Herzfehler einfach zu akzeptieren. Darüber hinaus hatte ich noch viel weniger Zeit, um über meinen Wechsel an die Yamaku nachzudenken."


n "\n\nDas Festival mit Shizune zu verbringen, hat mir wirklich geholfen, diese Phase zu überwinden. Ich war glücklich. So sehr, dass ich ich das Gefühl vergessen konnte, die ganze Zeit von ihr manipuliert worden zu sein. Nun begreife ich, dass ich es selbst war, der ihr diese Manipulation erlaubt hat."


nvl clear

n "\n\nAuch wenn ich mich fühlte, als wäre ich auf dem absoluten Tiefpunkt, wollte ich nach wie vor wieder ein normales Leben haben. Dessen bin ich mir sicher, weil ich im Moment Freude an dem finde, was ich habe. Ich denke, so ist es für jeden – auch für Misha. Jeder will jemanden haben, der ihn aus seinen Selbstmitleid herausholt."


n "Es ist nur, dass Misha Shizune als diesen Jemand haben wollte. Doch ich denke, Misha glaubt, da sie nicht zusammen sein können, dürfte sie Shizunes Hand nicht ergreifen. Und das frustriert Shizune. Aber wenn sie einen Fremden wie mich aufmuntern konnte, wird sie für Misha alles geben."


n "\nIch kann es auch in ihren Augen sehen. Obwohl sie versucht, es wie jedes andere Problem in ihrem Leben zu behandeln, funktioniert das nicht bei Mishas Depression. Ihre Gedankengänge sind vollkommen unterschiedlich – manchmal vorsichtiger, manchmal rücksichtsloser und verzweifelter. So sehr beschäftigt es sie."


nvl clear

n "\n\n\n\n\nLetzten Endes sage ich nichts. Zum einen, weil so in Zweisamkeit neben ihr zu sitzen so angenehm ist, dass ich diesen Augenblick nicht mit einer Frage unterbrechen will."


n "\n\nUnd zum anderen wegen Feigheit. Ich weiß nicht, ob ihre Aktionen an jenem Tag vielleicht nicht durchdacht oder sogar ein Glücksfall waren – nur eine Ansammlung von Zufällen. Ich fing an zu denken, dass es nicht so war, aber ich weiß nicht, ob das etwas ändern würde. Bei dem Gedanken daran ist mir unwohl."


$ renpy.music.set_volume(1.0, 2.0, channel="music")
$ renpy.music.set_volume(1.0, 2.0, channel="ambient")

nvl hide dissolve
nvl clear

scene bg school_roof onlayer master
with locationchange

window show

stop music fadeout 5.0

"Der Zaun hinter mir erzittert leicht. Als ich daraufhin zu Shizune sehe, ist sie schlafend dagegen gelehnt. Wenn man bedenkt, dass sie die ganze Nacht wach war, ist das keine Überraschung."


"Wo kommt ihre ganze Motivation nur her? Nicht nur im Bezug auf Misha. Ich bin Zyniker, darum ist es schwer für mich zu akzeptieren, dass jemand so stark sein kann."


"Mein erster Gedanke war, dass sie sich vielleicht selbst hasst. Naheliegend wäre es."


"Während ich mich an sie lehne, macht es mich traurig, dass es vielleicht wirklich so ist. Aber es könnte sein, dass wir beide in einer Beziehung gleich sind: Wir wollen bessere Menschen sein."


stop ambient fadeout 2.0

scene black onlayer master
with dissolve

$ suppress_window_after_timeskip = True



label de_S32:

window hide None

scene black onlayer master
with dissolve

scene bg school_dormhisao onlayer master
with openeye

window show

play music music_daily fadein 8.0

"Anscheinend habe ich gestern zu viel gegessen, denn ich wache morgens mit so einer Übelkeit auf, dass man es schon als Problem bezeichnen könnte."


"Allerdings kann ich meine Einkaufstour ins Dorf nicht verschieben. Obwohl ich am liebsten im Bett bleiben würde, zwinge ich mich aufzustehen und mich anzuziehen."


scene bg suburb_roadcenter onlayer master
with locationskip

"Irgendwann zwischen dem Kauf von Zahnpasta und ein paar Lebensmitteln hat mir das Herumlaufen gegen die Übelkeit geholfen. Dann bekomme ich Hunger."
"Nachdem ich fürs Frühstück eine Pause eingelegt habe, fällt mir auf, wie viel Zeit eigentlich verstrichen ist."


"Ich hatte überhaupt nicht erwartet, so lange unterwegs zu sein. Ich weiß nicht einmal mehr, ob ich meine Tür abgeschlossen habe. Ich sollte wirklich zurück."


scene bg school_dormhallway onlayer master
show hideaki bored onlayer master at center
with locationskip

"Als ich wieder bei den Wohnheimen ankomme, entdecke ich Hideaki, der vor der meiner Zimmertür steht."
"Es gibt fast nichts, womit ich weniger gerechnet hätte. Vielleicht hätte ich allein von der Überraschung eine Herzattacke kriegen können. Glücklicherweise bleibt mir das erspart."


show hideaki normal onlayer master
with charachange

"Sobald er mich sieht, grüßt er mich auf seine gleichgültige Art. Ich antworte ihm etwas zu langsam, darum wiederholt er seine Begrüßung ohne zu zögern."


show hideaki triangle onlayer master
with charachange

hh "Hallo."


show hideaki normal onlayer master
with charachange

hh "Stimmt etwas nicht?"


hi "Ich bin nur überrascht, dich hier zu sehen."


"Nicht so überrascht wie ich es hätte sein können, da es unmöglich ist, ihn mit jemand anderem zu verwechseln. Diese seltsamen Klamotten würde ich überall erkennen."
"Wenn ich es mir recht überlege, habe ich mich in letzter Zeit wirklich mit markant aussehenden Menschen umgeben."


show hideaki confused onlayer master
with charachange

"Hideakis Kopf fällt leicht zur Seite. Etwas zu leicht."


hh "Wieso? Ist es ungewöhnlich, dass die Familie einen besuchen kommt?"


hi "Na ja… ja, eigentlich schon."


show hideaki surprise_up onlayer master
with charachange

show hideaki bored onlayer master
with charachange

"Also ist Hideaki doch kein Roboter. Es ist fast so, als wäre er mehr von der Tatsache überrascht, dass sogar er von etwas überrascht sein kann. Doch er erholt sich schnell wieder."


"Nichtsdestotrotz sieht er in diesem kurzen Augenblick seinem Alter entsprechend aus. Diese unbehagliche Seite von ihm wirkt aufrichtiger, und ich hätte nichts dagegen, mehr davon zu sehen."


"Allerdings nicht so sehr, dass ich deswegen nachhaken würde. Nur Shizune wäre so eifrig. Dass mir so etwas überhaupt durch den Kopf geht, beweist nur, dass sie auf mich abfärbt."


hi "Ich hätte gedacht, dass du einen Grund hast. Das ist alles."


show hideaki triangle onlayer master
with charachange

hh "Ich habe einen."


hi "Siehst du? Jedenfalls können wir uns unterhalten, während wir nach ihr suchen. Darum bist du doch hier, oder?"


show hideaki normal_up onlayer master
with charachange

hh "Shizune ist im Schülerratsraum. Ich hab nach dir gesucht. Wir machen vielleicht bald ein Reise – eine Familienreise. Meinst du, dass sie mit uns kommen würde?"


hi "Na ja, ich weiß nicht. Sie ist in letzter Zeit irgendwie auf dem Kriegsfuß mit vielerlei Dingen gewesen. Und sobald sie sich an etwas festgebissen hat, lässt sie so schnell nicht mehr los. Ich schätze, du weißt wovon ich rede."


show hideaki closed_up onlayer master
with charachange

hh "Mhm."


scene bg school_courtyard onlayer master
with locationskip

"Hideaki sieht beim Herumlaufen viel gelassener aus als ich in meiner ersten Woche."


hi "Du bist nicht zum ersten Mal hier?"


"Ich frage einfach. Natürlich könnte der Hang, das nahe Umfeld zu ignorieren, in der Familie liegen. Es würde erklären, warum Hideaki so distanziert von Shizune ist. Ich bekomme den Eindruck, dass es an mehr liegt als nur ihrer Taubheit."


show hideaki bored onlayer master at center
with charaenter

hh "Nein, aber das ist das erste Mal, dass ich soviel herumlaufen kann. Hier ist es irgendwie seltsam. Ich bin auf jemanden gestoßen, der mir sagte, dass Frauen nicht in den Wohnheimen erlaubt seien."


show hideaki disapproves onlayer master
with charachange

hh "Nachdem ich ihm sagte, dass ich keine Frau bin, sagte er mir, dass ich irreführend wäre. Und dann hat er mir unterstellt, ein Auftragsmörder zu sein."


show hideaki normal onlayer master
with charachange

hh "Er warnte mich, dass er nicht nur unbesiegbar sei, sondern auch stark genug, um wahrscheinlich das ganze Gebäude mit einem Schlag zu zerstören."
hh "Oder zumindest das Gemälde an der Wand im Flur herunterfallen zu lassen. Übrigens ist dieses Gemälde an die Wand geschraubt."


hi "Jepp, das ist der Kerl, der mir gegenüber wohnt. Er ist in Ordnung."


show hideaki triangle onlayer master
with charachange

hh "Ach so. Oh, du hast deine Tür offengelassen. Als ich hier ankam, war sie unverschlossen."


"Es ärgert mich etwas, dass Hideaki das weiß. Er kann das nur wissen, wenn er meine Tür auch geöffnet hat. Aber dieser Ärger verfliegt schnell wieder."


hi "Ist egal."


hi "Ich hab nichts zu verbergen und auch nichts, das es sich lohnen würde zu stehlen."


show hideaki happy_up onlayer master
with charachange

hh "Dein Fußball ist ziemlich cool."


hi "Das ist eines der Dinge, die unwichtig sind."


show hideaki serious onlayer master
with charachange

hh "Wenn du ein Fußballspieler bist, ist ein Fußball sehr wichtig."


"Schätze, das ist es. Der Gedanke bringt mich zum Lächeln."


show bg school_lobby onlayer master
show hideaki closed_up onlayer master at center
with locationskip

hh "Ich bin hier, weil mein Vater ein neues Handy gekauft hat und er Shizune Bescheid sagen will – falls sie ihn mal anrufen muss. Ich dachte, das solltest du auch wissen. Immerhin bist du ihr Freund, oder nicht?"


hi "Ja…"


hi "… Wieso?"


show hideaki bored onlayer master
with charachange

hh "Nur falls etwas nicht stimmt oder sie etwas braucht."


"Das meinte ich nicht, aber gut."


hi "Selbst wenn sie etwas bräuchte, würde sie wahrscheinlich nicht anrufen."


show hideaki triangle onlayer master
with charachange

hh "So ist sie einfach."


hi "Nun, wenn du das weißt… Warum kommt ihr dann den ganzen Weg hierher? Er hätte ihr über E-Mail Bescheid sagen können."


show hideaki closed_up onlayer master
with charachange

hh "Er mag keine E-Mails."


hi "Das ist so was von altmodisch. Sag mir nicht, dass er sein Geschäft immer noch mit klassischer Post oder so führt."


stop music fadeout 3.0

"Stille. Nun bin ich an der Reihe, mich unbehaglich zu fühlen. Nimmt Hideaki das wörtlich, oder habe ich den Nagel auf den Kopf getroffen?"


"Quatsch. Ich bin mir sicher, dass es am Ende daraus hinausläuft, dass er seine Tochter sehen und mit ihr in Kontakt bleiben will. Schließlich sind sie immer noch eine Familie. Auch wenn sie sich gegenseitig an die Gurgel gehen."


scene bg school_council onlayer master
show jigoro smug onlayer master at tworight
show shizu basic_normal2 onlayer master at twoleft
with locationskip

play music music_happiness fadein 2.0

"Die Tür zum Schülerratszimmer ist offen, und Hideaki und ich platzen herein, als Jigoro gerade inmitten einer Schimpftirade ist."
"Er wirft einen Blick auf uns, beschließt aber, dass wir es nicht Wert sind, seine Wortlawine auf Shizune zu unterbrechen. Das erschüttert ernsthaft meinen Glauben an meine vorangegangene Vermutung."


show jigoro angry onlayer master
with charachange

hx "Als ich im Schülerrat war, war unser Zimmer kleiner. Und kälter. Als würde man in einem Kühlraum arbeiten. Nicht wie ihr verwöhnten Kinder. Was für eine Vergeudung – hier in eurem riesigen Zimmer zu sitzen und nichts zu tun."


show shizu behind_frown onlayer master
with charachange

shi "…"


hx "Seid ihr nicht nur zu dritt? Das lässt diese vielen Tische nur wie eine unnötige Zurschaustellung von Dekadenz wirken. Abstoßend. Man darf nur so viele Tische benutzen wie man braucht, und keinen Einzigen mehr. Das ist Teil meines Kodex'."


"Es mag seltsam für mich sein, so zu denken, aber… nur die Hälfte der Unterhaltung zu hören ist ziemlich komisch. Und der Kodex ist es auch."


"Jetzt, da ich ankommen bin, ändert er das Thema und fängt an, über seinen Besuchsgrund zu reden."


show jigoro neutral onlayer master
with charachange

hx "Hideaki und ich machen eine Reise."


show shizu basic_normal2 onlayer master
with charachange

shi "…"


show jigoro angry onlayer master
with charachange

hx "Was machst du da? Murmelt jeder, während er Zeichensprache benutzt?"


hi "Nein, ich bin nur ein Anfänger. Es hilft mir nachzudenken. Irgendwie die Macht der Gewohnheit."


hx "Nur ein Anfänger… Unfassbar. Schön."


"Er wendet sich genau im richtigen Moment zu Shizune, um zu sehen, wie sie den Kopf schüttelt."


show jigoro neutral onlayer master
with charachange

hx "Bist du sicher, dass du nicht mitkommen willst?"


show shizu adjust_frown onlayer master
with charachange

"Sie wiederholt die Geste."


show jigoro angry onlayer master
with charachange

hx "Schön."


show jigoro neutral onlayer master
with charachange

hx "Kannst du ihr sagen, dass sie mich anrufen soll, falls sie etwas braucht?"


hi "Ja."


hi "Auch wenn ich glaube, dass eine E-Mail zu schicken viel einfacher gewesen wäre."


show jigoro angry onlayer master
with charachange

hx "Ich lese keine E-Mails auf meinem Handy. Wenn sie nicht spricht, kann sie Hideaki anrufen. Ich denke, wenn man mich erreichen muss, müssen du oder das andere Mädchen mich anrufen… Hmpf. Eigentlich könnt ihr alle drei gleich Hideaki anrufen."


hide jigoro onlayer master
with charaexit

stop music fadeout 3.0

"Und somit dreht er sich prompt um und geht, Hideaki im Schlepptau. Eine lange Fahrt für etwas, das nur fünf Minuten gedauert hat."


"Keiner von ihnen kann seine Gefühle gut zum Ausdruck bringen."
"Bei Shizune müsste ich mich fragen, ob sie es würde, wenn sie könnte. Es erklärt eine Menge, aber sie scheint nicht unglücklich darüber zu sein. Trotzdem frage ich mich, ob sie es vielleicht doch ist."


play sound sfx_doorclose
with Pause(1.0)
show shizu basic_normal onlayer master at center
show bg school_council onlayer master at bgright
with dissolvecharamove

play music music_normal fadein 3.0

"Als die Tür hinter ihnen zufällt, bleiben Shizune und ich allein zurück. Sie atmet tief aus, und das Geräusch scheint in der Stille des Raumes besonders laut zu sein."


show shizu behind_frown onlayer master
with charachange

ssh "Es ist vollkommen lächerlich, mich danach zu fragen, ob ich auf eine Reise mitkommen will. Das Timing könnte nicht schlechter sein. Es überschneidet sich mit den Schülerratswahlen und außerdem hab ich noch nicht einmal Misha aufgemuntert."
ssh "Wenn man das bedenkt, ist es nervig, sich noch um etwas anderes Gedanken machen zu müssen."


his "Ja, aber vielleicht bist du gerade zu fokussiert auf diesen ganzen Kram."


show shizu adjust_frown onlayer master
with charachange

"Shizune rückt grob ihre Brille zurecht."


show shizu behind_frown onlayer master
with charachange

ssh "Absolut – einhundert Prozent korrekt. In dem Augenblick, in dem ich entschieden habe, dass ich Misha aufmuntern werde, ist alles andere in den Hintergrund gerückt, schätze ich."


his "Ich glaube, dein Vater sorgt sich mehr um dich als er vorgibt."


show shizu basic_normal onlayer master
with charachange

ssh "Ich weiß."


his "Na dann könnte es doch einer gute Idee…"


show shizu adjust_frown onlayer master
with charachange

ssh "Nein."


"Und dann wiederholt sie es. Bestimmter – als ob sie es für uns beide sagen würde."


show shizu cross_angry onlayer master
with charachange

ssh "Nein."


show shizu basic_frown onlayer master
with charachange

ssh "Nachdem ich so weit gekommen bin, kann ich keine Pause machen. Ein Urlaub ist nicht drin. Es wäre, als würde ich in einem anderen Leben aufwachen. Gestern war wie ein Urlaub für mich, darum müssen wir jetzt aufs Ganze gehen."


show shizu behind_blank onlayer master
with charachange

ssh "Tut mir leid, aber so bin ich nun mal."


$ renpy.music.set_volume(0.5, 2.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\nIch erinnere mich daran, was Yuuko sagte – dass sie Shizune irgendwie tapfer findet. Ich denke, ich verstehe, was sie meinte, und ich muss ihr zustimmen. Auch wenn man es Rücksichtslosigkeit und Torheit und sinnlose Sturheit nennen könnte, kann man es ebenso gut als „Tapferkeit” bezeichnen."


n "Jedoch erkenne ich einen grundlegenden Fehler in Shizunes Denkweise, den ich bis jetzt noch nicht bemerkt hatte."


n "\nIch bin mir sicher, dass Shizune lange und angestrengt darüber nachgedacht hat, an welcher Stelle sie es so vergeigt hat, dass zwischen ihr und Misha so eine tiefe Kluft entstehen konnte. Allerdings ist es typisch von ihr, sich dadurch nicht ausbremsen zu lassen, sondern sich sofort an die Lösung des Problems zu machen."


n "Dabei ignoriert sie einen großen Teil des Problems vollkommen – nämlich Misha selbst. Wenn Shizune nur von sich selbst ausgeht und Misha als Teil eines Ziels betrachtet, wird die Person Misha dabei verloren gehen. Shizune hat in den letzten paar Tagen eine Menge gesagt, aber nichts davon bezog sich auf Mishas Gefühle."


nvl clear

n "\nShizunes Denkweise ist abnormal. Nur wenige Menschen würden einen Freund zurückweisen und dann erwarten, dass die Dinge einfach wieder ins Lot kommen. Shizune tut genau das. Für sie ist das Leben – um es einfach auszudrücken – unterteil- und gliederbar."


n "Misha hingegen – wie jeder andere auch – sieht das Leben als Ganzes. Eine lange, fortlaufende Reise, in der ein Moment des Herzschmerzes einen auf ewig verfolgen kann."


n "Für Shizune ist ein Ereignis ein Ereignis, und wenige von ihnen überschneiden sich. Das Leben ist unterteilt in Siege, Niederlagen und Entscheidungen, in der jede Einzelne ihre eigene Geschichte hat. Deswegen ist es so abwegig für sie, an Urlaub zu denken. Deswegen kann sie nur die unmittelbaren Gefühle der Menschen anerkennen."


n "Genau so würde jemand denken, der wirklich besessen von dem Gedanken ist, in den Tag hineinzuleben."


n "Gleichermaßen sieht Shizune in Misha eine Freundin, doch ich bezweifle, dass sie bis vor Kurzem mehr in Misha gesehen hat als das. Oder dass sie sie in irgendeiner Weise hinterfragt hat. „Misha ist Misha” würde ihr genügen, auch wenn es für Misha selbst unglaublich erdrückend sein muss."


nvl clear

n "\nIn ihren eigenen Augen ist sie einfach Shizune. Es ist wahrscheinlich, dass sie nicht einmal über die Langzeit-Konsequenzen ihrer Taten nachdenkt, solange sie die Leben Anderer aufstacheln. Doch für Misha muss das fast schon heroisch gewirkt haben. So wie Yuuko – und sogar ich selbst – ihre Tapferkeit bewundern."


n "Und Shizunes Meinung über diese Ansicht ist, dass es gut war, jemandes Leben berühren zu können. Aber da hört es auf. Es ist leicht zu faszinieren, aber viel schwerer diese Faszination aufrechtzuerhalten. Und schon wechselt sie zum nächsten Ereignis."
n "Das Leben als Verkettung von komplett voneinander isolierten Ereignissen zu sehen, hat auch die Tendenz, den Menschen selbst zu isolieren."


n "Auch wenn sie gerade versucht, sich zu bessern – die Tatsache bleibt: Es führte einfach keine Weg dran vorbei, dass Shizune Misha irgendwann verletzt. Die Emotionen, die Misha für Shizune empfindet, waren einfach etwas, das Shizune nicht erfassen konnte, darum hat sie es auch nicht. Kombiniert mit ihrer Persönlichkeit war es unausweichlich."


n "Beide haben mir das alles nach und nach erzählt, seit wir uns kennen gelernt haben."


n "Inmitten der Erwägung ihrer Unterschiede, nimmt in meinem Kopf langsam eine Idee Gestalt an."


$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl hide dissolve
nvl clear
window show

his "Arbeitest du genau jetzt an deinem Plan? In dieser Sekunde?"


his "Dein Plan, um Misha aufzumuntern?"


show shizu basic_happy onlayer master
with charachange

ssh "Na klar. Als ich angeschrien wurde, habe ich mir die ganze Zeit Gedanken darüber gemacht."


show shizu adjust_happy onlayer master
with charachange

"Sie stupst ihre Brille mit einem seltsam triumphierenden Blick ihr Nasenbein hoch und tippt sich daraufhin an die Schläfe."


show shizu behind_smile onlayer master
with charachange

ssh "Multitasking!"


stop music fadeout 4.0

"Ernsthaft? Ist es nicht eher, weil du nichts hören kannst, dass du dich auf so etwas konzentrieren kannst? Na ja, wie auch immer. Ich frage sie, was sie von meiner Idee hält, und es stellt sich heraus, dass wir beide eine ähnliche Idee hatten."


scene black onlayer master
with dissolve



label de_S33:

scene bg school_scienceroom onlayer master at bgleft
with locationchange

play music music_pearly fadein 5.0

"Der erste Schritt ist, Misha in die Enge zu treiben. Auch wenn es mich irgendwie unbehaglich macht – immerhin sprechen wir hier von einem menschliches Wesen."


"Auch wenn mir diese Situation ein wenig wie aus einer Krimiserie vorkommt, ist es dazu gekommen, da es sich als unmöglich herausgestellt hat, mit ihr normal zu reden."


"Aber wir haben zusammen Unterricht. Sogar die allererste Stunde des Tages."


show shizu invis onlayer master:
    center
    xpos 0.75
show mishashort invis_close onlayer master:
    center
    xpos 0.15
with None

show shizu behind_blank onlayer master at tworight
show mishashort perky_confused_close onlayer master at twoleft
show bg school_scienceroom onlayer master at center
with dissolvecharamove

"Obwohl die Ankündigung, dass wir heute in Gruppen arbeiten, etwas auf sich warten lassen hat, stellen Shizune und ich sofort sicher, dass Misha mit uns zusammen arbeitet."


hi "Weißt du, ich finde, Mutou gibt uns verdächtig viel Gruppen- und Eigenarbeit, meinst du nicht?"


show mishashort perky_smile_close onlayer master
with charachange

mi "Hm~, aber es ist einfach, von daher ist es okay, oder nicht~?"


hi "Findest du? In letzter Zeit gab es aber auch anderen Kram, über den ich nachgedacht habe, und der nicht okay ist."


"Misha nickt nach jedem Satz und ignoriert einfach alles."


show mishashort sign_confused_close onlayer master
with charachange

mi "Ich hab darüber nachgedacht, und~… ich arbeite nicht genug, wenn ich mit dir und Shicchan zusammen bin! Ich gebe mir heute mehr Mühe. Darum~! lenk mich bitte nicht ab, Hicchan~. Ich muss mich konzentrieren~."


show shizu behind_frustrated onlayer master
with charachange

"Das war eine ärgerlich durchschaubare Ausrede. Shizune sieht ebenfalls nicht sehr glücklich aus, da Misha sich nicht darum gekümmert hat, irgendetwas davon zu gebärden und stattdessen nur einen Stift in ihrer Hand herumgewirbelt hat."


"So wie sie dabei gezittert hat, bin ich mir sicher, dass sie es getan hat, damit sie nicht unbeabsichtigt gebärdet."


"So wie Misha aussieht, abgelenkt und unruhig, bezweifle ich, dass sie aus Bosheit nicht für Shizune übersetzen will. Auch wenn es offensichtlich immer noch eine Methode ist, um Shizune von sich zu distanzieren."


hi "Shizune will mit dir reden."


show mishashort perky_sad_close onlayer master
with charachange

mi "…"


show mishashort perky_confused_close onlayer master
with charachange

mi "Kann das nicht bis später warten, Hicchan?"


show shizu basic_angry onlayer master
with charachange

ssh "Nein."


hi "Warum nicht jetzt?"


show mishashort sign_confused_close onlayer master
with charachange

mi "Wir sind mitten im Unterricht~…"


"Jetzt wirbelt sie in beiden Händen einen Stift. Ich fange an zu glauben, dass ihr Gestikulieren eine Art nervöser Tick geworden ist. Das ist kein guter Ersatz, auch wenn der Anblick ihres zweihändigen Stifteinsatzes ziemlich beeindruckend ist."


hi "Dann nach dem Unterricht."


scene bg school_scienceroom onlayer master at bgleft
with shorttimeskip

"Nach dem Unterricht zögere ich keine Sekunde, es wieder anzusprechen."


show shizu invis onlayer master:
    center
    xpos 0.75
show mishashort invis_close onlayer master:
    center
    xpos 0.15
with None

show shizu behind_frown onlayer master at tworight
show mishashort perky_sad_close onlayer master at twoleft
show bg school_scienceroom onlayer master at center
with dissolvecharamove

"Während alle anderen aus dem Klassenzimmer eilen und uns drei allein zurücklassen, schaut Misha zunehmend länger in alle möglichen Richtungen – außer nach vorne."


hi "Willst du etwas essen gehen?"


show mishashort hips_frown_close onlayer master
with charachange

mi "Warum fragen du und Shicchan mich die ganze Zeit, ob ich etwas essen gehen will~, Hicchan~?"


hi "Weil wir beide zu Cafeteria gehen, und es lange her ist, seit wir das letzte Mal zusammen gegessen haben. Also warum nicht?"


show mishashort perky_confused_close onlayer master
with charachange

mi "Geht es um den Schülerrat?"


show shizu behind_blank onlayer master
with charachange

shi "…"


show mishashort perky_sad_close onlayer master
with charachange

"Sie interpretiert Shizunes fehlende Antwort als Eingeständnis und fängt an zu gebärden:"


show mishashort hips_frown_close onlayer master
with charachange

mi "Shicchan, denkst du auch mal an etwas anderes?"


stop music fadeout 5.0

hide mishashort onlayer master
with charaexit

"Bevor Shizune antworten kann, geht sie. Ich muss sagen, nach dem, was gerade eben passiert ist, bin ich nicht mehr so zuversichtlich."


show shizu behind_blank onlayer master at center
show bg school_scienceroom onlayer master at bgleft
with charamove

"Keiner von uns hat erwartet, dass es reibungslos abläuft, aber es wäre schön gewesen."


show shizu adjust_frown onlayer master
with charachange

"Als ob sie meine Gedanken liest, spielt sie eine Weile mit ihrer Brille, bevor sie gebärdet."


show shizu basic_angry onlayer master
with charachange

ssh "Ich weiß, was du denkst – aber nein, wir sollten ihr jetzt keinen Abstand geben. Ich hab dir gesagt, dass ich nicht so leicht aufgeben werde."


his "Na ja, ich frage mich nur langsam, ob das alles nicht zu früh ist."


show shizu behind_frown onlayer master
with charachange

ssh "Bekommst du kalte Füße?"


show shizu adjust_frown onlayer master
with charachange

ssh "Nun, ich werde nicht aufgeben. Das würde bedeuten {b}sie{/b} aufzugeben."


show shizu behind_blank onlayer master
with charachange

ssh "Es gibt eine schmale Grenze zwischen jemanden helfen und ihn ersticken. Aber ich will einfach, dass Misha sich zusammenreißt und aufhört, sich so komisch zu verhalten."


show shizu basic_normal onlayer master
with charachange

ssh "Ich weiß, dass sie es kann. Selbst wenn sie es versuchen will – Menschen ändern sich nicht über Nacht. Wenn sie es könnten, wäre die Welt ein viel einfacherer Ort."


his "Okay, du hast gewonnen."


his "Dann sollten wir uns jetzt wohl aufteilen und nach ihr suchen."


"Obwohl ich der Einzige bin, der sie wirklich finden sollte."


show shizu adjust_happy onlayer master
with charachange

play music music_tranquil fadein 3.0

ssh "Wenn ich sie zuerst finde, rufe ich dich auf deinem Handy an."


"Lächelnd holt Shizune ihr Handy heraus, um es einzuschalten und vorzubereiten."
" Ich sehe, dass sie eine extrem hohe Anzahl an ungelesenen Nachrichten hat, und ihrem Gesichtsausdruck zufolge weiß sie das ebenfalls. Sie wirbelt es ein paar Mal an seinem Band herum und verzieht ihr Gesicht."


show shizu behind_frown onlayer master
with charachange

ssh "Ich benutze das Ding nicht gerne."


show shizu basic_angry onlayer master
with charachange

ssh "Warum kann ich nicht einfach mit meinen Fingern schnippen?"


his "Und was dann? Ich bin kein Hund. Und so weit wie ein Handysignal kommt es auch nicht."


show shizu behind_smile onlayer master
with charachange

his "Du hast eine Menge Spaß daran, nicht wahr?"


"Sie schüttelt den Kopf und fährt fort."


show shizu adjust_happy onlayer master
with charachange

ssh "Wo sie hingehen wird ist offensichtlich. Auf dem Schulgelände kannst du nicht nach ihr suchen – sie würde so weit wie möglich weg wollen."


show shizu behind_blank onlayer master
with charachange

ssh "Das Teehaus? So früh am Tag ist es meistens leer; Misha liebt es, dorthin zu gehen, wenn sie keine Lust auf den Unterricht hat, und sie liebt die Parfaits dort."


"„Du weißt wirklich eine Menge über sie.”"
"Das würde ich gerne sagen, aber sie würde mehr in diese Worte hineininterpretieren als ich ausdrücken wollte – vielleicht auch etwas Negatives. Darum nicke ich einfach und drehe mich um, um zu gehen. Dann spüre ich, wie sie mich am Ärmel festhält."


show shizu basic_normal_close onlayer master
with characlose

hi "Was?"


"Ich habe die Frage ausgesprochen, bevor mir einfällt, dass sie mich nicht hören kann."


show shizu behind_smile_close onlayer master
with charachange

ssh "Es ist schön, dass ich das alles nicht mehr allein machen muss, weil ich dir vertrauen kann. Ich bin wirklich glücklich."


"Das zu hören, macht mich glücklich. Mir fällt keine Antwort darauf ein, und ich nicke lediglich."


play ambient sfx_crowd_indoors fadein 2.0

scene bg school_lobby onlayer master
show mishashort perky_confused onlayer master:
    center
    xpos 0.6
    ypos 1.05
show crowd onlayer master
with locationskip

"Als ich nach draußen gehe, erhasche ich einen flüchtigen Blick auf pinkes Haar hinter dem Kopf eines anderen Mädchens. Als ich mich auf den Weg dorthin mache, begreife ich, dass dies nicht der Weg ist, der vom Schulgelände hinunterführt."


"Es ist der Weg zum Schülerratszimmer. Wenn ich Shizune aus dem Weg gehen wollte, würde ich nicht dorthin gehen."


"Es ist seltsam, dass Misha dann in diese Richtung geht. Vielleicht will sie mit Shizune reden."


"Wenn das so ist, muss ich mich fragen, ob den Dingen ihren Lauf zu lassen gar keine so schlechte Idee wäre. Besonders wenn es in eine gute Richtung zu gehen scheint."


show mishashort invis as mishafront onlayer master:
    center
    xpos 0.6
    ypos 1.05
with None

show mishashort invis onlayer master at center
show mishashort hips_smile as mishafront onlayer master at center
with Dissolvemove(0.7)

hide mishashort onlayer master
hide mishafront onlayer master
with None

show mishashort hips_smile onlayer master at center
with None

"Plötzlich stoppt Misha, dreht sich um und überrascht mich."


show mishashort hips_grin onlayer master
with charachange

mi "Überraschung, Hicchan~! Hast du nach mir gesucht? Das dachte ich mir schon~!"


"Ich wollte sagen „Hey, ich hab gerade nach dir gesucht”, aber ich schätze, das hat sich damit erledigt."


show mishashort hips_grin onlayer master:
    easeout 0.7 xpos 1.0 alpha 0.0
with Pause(0.7)

"Sie hat nicht einmal ihren Satz beendet, da stürmt sie an mir vorbei in Richtung Ausgang. Ich muss zugeben, dass Misha wesentlich scharfsinniger ist, als ich erwartet hatte. Und dazu noch überraschend schnell."


stop ambient fadeout 2.0

scene bg school_courtyard onlayer master
with locationskip

"Auch wenn ich mir damit mehr zumute, als ich wahrscheinlich sollte, schaffe ich es, sie auf halber Strecke zur Tür einzuholen."


hi "Du bist gerade wirklich die rüpelhafteste Frau auf der ganzen Welt."


hi "Könntest du für einen Moment mal aufhören immer wegzurennen? Ich will mit dir reden."


show mishashort cross_smile onlayer master at center
with charaenter

"Leicht amüsiert dreht sich Misha zu mir um, und hebt ihre Hände, als ob sie mir sagen wollte, dass ich fortfahren soll. Nun, da ich ihre Aufmerksamkeit habe, ist es jedoch schwierig, die richtigen Worte zu finden."


hi "Wo gehst du jetzt hin?"


show mishashort sign_smile onlayer master
with charachange

mi "Zum Shanghai~."


hi "Kann ich dann mit dir kommen?"


show mishashort perky_confused onlayer master
with charachange

"Ihre Antwort lässt eine gefühlte Ewigkeit auf sich warten. Es ist fast, als könnte ich meiner Armbanduhr beim Ticken zuhören."


show mishashort hips_smile onlayer master
with charachange

mi "Na gut, Hicchan."


stop music fadeout 3.0

"Ich bekomme den Eindruck, dass sie nur zugestimmt hat, weil sie für heute genug vom Streiten hat."


scene bg suburb_shanghaiint onlayer master
show mishashort perky_smile onlayer master:
    center
    ypos 1.02
with shorttimeskip

with Pause(0.2)

play sound sfx_storebell
show mishashort perky_confused onlayer master:
    ease 0.1 ypos 1.0
    ease 0.2 ypos 1.02
with Pause(0.3)

"Als wir dort ankommen, kommt ein Pärchen nach uns herein, und Misha schreckt wegen des Lärms leicht auf."


show mishashort perky_smile_close onlayer master at Position(ypos=1.1)
with dissolvecharamove

"Als sie sieht, dass es nicht Shizune ist, kommt sie wieder zur Ruhe und setzt ihr gewohntes Lächeln auf, um ein Parfait bei Yuuko zu bestellen. Dann setzt sie sich in die nächstgelegene Sitzecke."


hi "Du bist zu schnell weggerannt. Du hättest dir zumindest anhören können, was sie zu sagen hat."


show mishashort hips_frown_close onlayer master
with charachange

"Mishas erzürnte Reaktion verrät mir, dass sie vielleicht Angst vor dem hatte, was Shizune sagen wollte."


mi "Warum tut ihr beide das, Hicchan?"


hi "Weil Shizune immer noch deine Freundin bleiben will. Für sie ist das irgendwie, als würde man einen Nuklearsprengkopf von einem U-Boot aus abfeuern – man braucht zwei Schlüssel dafür."


show mishashort perky_confused_close onlayer master
with charachange

mi "…"


hi "Und was soll sie sonst tun?"


"Sie gebärdet nicht mehr automatisch alles, was sie sagt. Und ich bin mir sicher, dass das der Grund ist, weswegen Shizune so viele Schwierigkeiten mit ihr hat."


hi "Als sie versucht hat, mit dir darüber zu reden, wolltest du nicht zuhören."


show mishashort perky_sad_close onlayer master
with charachange

play music music_night fadein 6.0

"Mishas schuldige Miene sagt mir, dass ich ins Schwarze getroffen habe."


hi "Hasst du Shizune wirklich so sehr?"


show mishashort sign_confused_close onlayer master
with charachange

mi "Nein, Hicchan. Das hab ich dir schon mal gesagt."


show mishashort perky_confused_close onlayer master
with charachange

"Sie antwortet ohne zu zucken, während sie träge mit einem Löffel spielt."


hi "Ja, ich weiß."


hi "Ich bin mir sicher, dass sie das auch weiß. Aber ich frage mich, ob es vielleicht einfacher wäre, wenn du es tätest."


hi "Das Einzige, woran sie die letzte Woche wirklich gedacht hat, ist, wie sie dich glücklich machen kann. Immerhin hängt sie noch an dir. Aber gestern dachte sie, dass es am einfachsten wäre, wenn du sie einfach hassen würdest."


hi "Da du ihr nicht gesagt hast, dass du sie hasst, denkt Shizune, dass ihr beide immer noch Freunde bleiben könnt. So ist sie; sie denkt nur in Extremen."


"Ihr Parfait beginnt zu schmelzen. Die Zutaten vermischen sich in kleinen Flüssen, die mich an im Zeitraffer wachsende Wurzeln eines Baumes erinnern."


show mishashort cross_frown_close onlayer master
with charachange

mi "Das ist bescheuert. Shicchan ist nicht so dumm, Hicchan. Mach dich nicht lächerlich~."


hi "Es hat nichts mit Intelligenz zu tun. Kluge Leute können dumme Dinge tun."
hi "Und überhaupt, hab ich nicht Recht? Ich war entsetzt, als wir uns letzte Woche unterhalten haben, aber am Ende war ich erleichtert, weil es sich angehört hat, als würde alles wieder wie immer werden."


hi "Ich hatte nicht erwartet, dass ihr beide direkt danach einen Streit haben würdet."


show mishashort perky_confused_close onlayer master
with charachange

mi "Das war kein Streit, Hicchan. Ich hab sie einfach nur angeschrien."


"Ich habe mitbekommen, dass Misha nie wirklich ihre Betonung ändert, nur die Lautstärke. Sie spricht so leise und schuldbewusst, dass ich kaum glauben kann, dass es von ihr kam."


hi "So oder so habe ich mich gefreut, weil ich dachte, dass ihr Zwei immer noch Freunde bleiben könnt. Schließlich braucht sie dich."


show mishashort sign_confused_close onlayer master
with charachange

mi "Hm~. Nein, braucht sie nicht, Hicchan."


hi "Ach so? Wie willst du das wissen? Es gibt eine Menge Dinge, die Shizune nicht…"


"Ausspricht? Sagt? Erwähnt? Ich mache mir Sorgen, dass es die Stimmung ruinieren würde, wenn ich das Falsche sage."
"Ich habe es endlich geschafft, eine Unterhaltung mit ihr zu bewerkstelligen, und will es nicht versauen. Ich frage mich, ob dies für sie die erste ehrliche Unterhaltung mit mir ist."


hi "Nur weil sie es dir nicht gesagt hat, heißt das nicht, dass sie dich nicht mag."


show mishashort hips_frown_close onlayer master
with charachange

mi "Das ergibt keinen Sinn…"


hi "Doch, das tut es. Denn andernfalls würde sie dir Widerworte geben."


show mishashort hips_grin_close onlayer master
with charachange

mi "Wahaha~."


hi "Denkst du nicht? Sie sucht mit jedem Streit, warum also nicht mit dir? Offensichtlich weil du ihre Freundin bist und sie dich schätzt. Außerdem ist Shizune genauso verletzt."


hi "Sie ist einfach nur furchtbar darin, ihre Gefühle zu zeigen. Und wenn, dann tut sie es meistens auf die falsche Art. Aber trotzdem mag sie dich."


show mishashort perky_confused_close onlayer master
with charachange

mi "Hicchan, erinnerst du dich, als ich sagte, dass ich Shizune nicht hassen oder verärgern will?"
mi "Um die Wahrheit zu sagen~, tue ich letzten Endes beides. Jetzt ist es, als wäre eine Art… wie soll ich sagen… Unbeholfenheit zwischen uns. Es ist schwer zu erklären."


hi "Ihr beide seid so dickköpfig. Du hast darüber gesprochen, wie du dich nicht mit Shizune auseinanderleben willst, aber dann lässt du genau das geschehen."


hi "Und Shizune ist genauso schlimm. Sie will, dass du ihre Freundin bist, aber sie respektiert dich zu sehr, um so aggressiv vorzugehen, wie sie es bei anderen tun würde."


"Ich bin mir sicher, dass Misha es als Gleichgültigkeit interpretiert, dass Shizune ihr so viel Raum gibt."


show mishashort perky_sad_close onlayer master
with charachange

mi "Ich hab's bereits verbockt, Hicchan. Es wird wieder passieren~, dessen bin ich mir sicher. Wenn ich es so betrachte, weiß ich nicht, was ich tun soll."
mi "So oder so fühlt es sich an, als würde ich am Ende alles nur schlimmer machen. Dann wäre es doch vielleicht besser, wenn ich gar nichts tue, stimmt's~?"


hi "Sei nicht albern. Warum denkst du überhaupt so? Sei doch mal optimistischer."


"„Es sollte dir leicht fallen”, will ich sagen, aber das wäre zu anmaßend."


show mishashort hips_smile_close onlayer master
with charachange

mi "Hicchan~, ich wusste gar nicht, dass du so optimistisch bist. Hätte ich nie erwartet."


hi "…"


show mishashort perky_smile_close onlayer master
with charachange

mi "Du bist immer so düster, wenn ich versuche, dich zu überraschen."


hi "Nein, das ist erst seit Kurzem so. Wirklich. Ich hasse es mittlerweile einfach, wenn Leute so ohne Weiteres aufgeben."


show mishashort cross_grin_close onlayer master
with charachange

mi "Haha~."


show mishashort perky_smile_close onlayer master
with charachange

mi "„Mittlerweile”, hmm~?"


hi "Es macht mich wütend, wenn Menschen aufgeben. Früher dachte ich, dass Aufgeben so etwas wie Wegrennen ist, da die Leute es immer so beschreiben. Aber wenn ich heute drüber nachdenke, ist es eher so, als würde man etwas wegwerfen."


hi "Sieh es mal so: Wenn man vor etwas wegläuft, ist es irgendwie immer noch da. Weißt du, ich war im Krankenhaus, und ich wollte nicht einfach nur vor meinen Problemen davonlaufen – ich wollte nie wieder an sie denken."


"Misha nimmt einen Löffel von ihrer grauen Eispampe. Ist ihr gerade erst wieder eingefallen, dass das Parfait noch da ist? Oder könnte es sein, dass sie es so mag?"


hi "Jedenfalls will ich darauf hinaus, dass du das nicht tun darfst. Menschen sind zu sentimental, als dass man ihre Erinnerungen einfach so wegwerfen dürfte."


hi "Es ist unmöglich. Shizune kann sich das Leben als nichts anderes vorstellen als Sieg und Niederlage. Glaubst du nicht, dass sie sich wünscht, sich nie an die Niederlagen erinnern zu müssen?"


hi "Aber man kann sich das nicht aussuchen. Das ist, als würde man in einer Blase leben wollen. Das schlimmste daran ist, dass deine Denkweise so verschwenderisch ist. Sie macht dich so pessimistisch, dass du vor allem Angst hast."


stop music fadeout 4.0

hi "Komm schon."


"Ich schnappe mir ihre Hand und winke Yuuko mit der anderen herbei, um für unser Essen zu bezahlen."


show mishashort sign_confused_close onlayer master
with charachange

mi "Wo gehen wir jetzt hin?"


hi "Zurück zur Schule bevor die Mittagspause vorbei ist. Aber vorher will ich noch einen Abstecher woandershin machen."


scene bg school_gate onlayer master:
    right
    subpixel True
    linear 30 left
with locationskip

play music music_comfort

"Etwas mehr als zehn Minuten vor Ende der Mittagspause erreichen Misha und ich das Schultor. Obwohl man unser Schritttempo bestenfalls als „zügig” beschreiben kann, fühle ich mich erschöpft."


hi "Ich wollte nicht mal wirklich an diese Schule, weißt du. Ich hatte keine Wahl. Als ich vor diesen Toren stand, bin ich mir sicher, dass ein Teil von mir dachte: „Was für ein deprimierender Ort.”"


hi "Doch sie sieht überhaupt nicht deprimierend aus. Na ja, ich dachte zu jener Zeit immer noch, dass ich alles wüsste. Ich hab mich praktisch wie ein anderer Mensch gefühlt."


hi "Wenn ich könnte, würde ich zurückgehen und meinem alten Ich sagen, dass er aufhören soll zu denken, er könne alles mit einem einzigen Blick einschätzen und sich zu verhalten, als ob sein Leben vorbei wäre und er nie wieder Spaß haben könnte."


scene bg school_gardens onlayer master:
    right
    subpixel True
    linear 30 left
with locationskip

"Auf dem Schulgelände treiben sich immer noch vereinzelt einige Leute herum. Typisch für die Mittagspause."


hi "Dann haben du und Shizune mich beim Aufbau der zwei Festivals helfen lassen. Was für eine Menge Arbeit das war. Ich dachte: „Ich hab keine Zeit für so was.”"


hi "Doch wenn ich darauf zurückblicke, hatte ich gar nicht so viel zu tun. Ich hatte auch nichts besseres zu tun. Ich hätte die Zeit einfach allein verbracht."


scene bg school_scienceroom onlayer master:
    right
    subpixel True
    linear 30 left
with locationskip

"Als nächstes schleife ich sie zu unserem Klassenzimmer, das leer ist – bis auf Mutou, der versucht, ein Sandwich zu essen, bevor der Unterricht weitergeht."


hi "Jedes Mal, wenn ich an euch beide gedacht habe, hab ich mir gewünscht, dass ihr mich in Ruhe lassen würdet – egal ob hier, oder…"


scene bg school_lobby onlayer master
with locationskip

"Wir überlassen Mutou seinem Mittagessen und machen uns auf zum nächsten Verkaufsautomaten."
"Da ich noch fünf Minuten Zeit habe, genehmige ich mir noch eine Limo. Ich habe die gesamte Mittagspause mit Misha verbracht – mehr Zeit als Shizune und ich seit Tagen mir ihr verbringen konnten."


hi "… auf dem Weg zur Cafeteria, oder wenn ihr mich immer nach dem Unterricht entführt habt."


hi "Mir ist nie aufgefallen, dass wir nur circa vier Mal miteinander geredet haben. Es war alles wirklich nur in meinem Kopf. Ich begreife das jetzt erst nach und nach."


show mishashort hips_smile onlayer master at center
with charaenter

mi "Ich erinnere mich daran, Hicchan. Aber~ ich kenne diese Orte auch alle."


hi "Warte, lass mich meine Führung abschließen. Uns bleibt kaum Zeit. Ach ja, willst du was zu trinken?"


scene bg school_staircase2 onlayer master
with locationchange

"Auf unserem Weg zum Treppenhaus freue ich mich darüber, dass ich sie nicht mehr an der Hand ziehen muss."


hi "Auf Treppen wird dir schwindlig, stimmt's?"


show mishashort perky_sad_close onlayer master at twoleft
with charaenter

mi "Genau~."


hi "Ich schätze, dann reicht es bis hierher."


show mishashort perky_sad_close onlayer master:
    ease 1.0 ypos 1.2
with Pause(1.0)

"Ich lehne mich gegen die Wand, während Misha sich mir gegenüber auf die Stufen setzt."


hi "Vermisst du je die Leute, mit denen du mal zur Grund- oder Mittelschule gegangen bist?"


show mishashort perky_confused_close onlayer master
with charachange

mi "Nein."


"Das kam schnell. Sie musste nicht einmal darüber nachdenken. Ich zucke reflexartig zusammen."


hi "An meiner alten Schule hatte ich mehr Freunde, aber ich rede nicht mehr mit ihnen. Es fühlt sich fast an, als wäre es eine Ewigkeit her. Was auch wirklich traurig ist."


hi "Manchmal möchte ich wieder mit ihnen reden, aber ich weiß, dass ich das nicht kann. Ich habe Angst, ich schäme mich – solche Sachen eben."
hi "Sie sind zu weit weg, um sie besuchen zu können. Manchmal denke ich, ich sollte sie anrufen, aber von den meisten habe ich keine Telefonnummer."


hi "Und wir sind nicht wirklich im Guten auseinander gegangen. Also warum sollten sie mich wiedersehen wollen?"


hi "Es kommt mir vor, als sollte ich es einfach vergessen, aber ich denke trotzdem daran und bereue, dass ich mir nicht mehr Mühe gegeben habe, mit ihnen in Kontakt zu bleiben."


hi "Und ich fange an zu denken, dass es vielleicht falsch ist, vergessen zu wollen. Es wäre eine Beleidigung für all die Menschen, mit denen ich Spaß hatte, und eine Verschwendung all der schönen Zeiten."


hi "Wie ich schon gesagt habe: Auch wenn es schlechte Zeiten gab, ist es in Ordnung, wenn man auf sie als glückliche Erinnerungen zurückschauen kann."


hi "Aber damals hab ich gar nicht darüber nachgedacht. Darum war es, als hätte ich von heute auf morgen keine Freunde mehr gehabt."
hi "Ich hab einfach zugelassen, dass ich all meine Freunde verliere – und das hat sich furchtbar angefühlt. Ich würde es wirklich hassen, wenn du und Shizune das gleiche durchmachen müsstet. Das ist alles."


show mishashort perky_sad_close onlayer master
with charachange

mi "„Das ist alles~.”"


hi "Es macht mich traurig, daran zu denken, dass du das gleiche tun wirst und deine Freundin abweist. Besonders weil du nicht so weit von Shizune weg bist. Ich meine, ihr wohnt sogar im gleichen Wohnheim."


mi "Freundin, hm~…"


show mishashort perky_confused_close onlayer master
with charachange

mi "Bist du nicht auch mein Freund, Hicchan?"


hi "Sicher."


hi "Du hast das alles zwar verschlafen, aber das Feuerwerk damals beim Festival war wirklich toll."


hi "Es war das erste Mal, dass ich ein Feuerwerk auf diese Art gesehen habe. Und es war auch das erste Mal seit Langem, dass ich den Himmel wieder richtig gesehen habe. Die Sterne habe ich vorher auch noch nie wirklich betrachtet."


"Doch während ich im Krankenhaus war, habe ich ein Buch über sie durchgeblättert und viel gelernt."


"Zum Beispiel, dass Sterne nicht einfach nur brennen – sie sind eher wie eine konstante Kette von Explosionen."
"Sie sind so weit weg, dass ein paar der Sterne, die man sehen kann, schon vor Tausenden von Jahren erloschen sind, denn ihr Licht erreicht die Erde jetzt erst."


"Ich habe eine Nachbildung gesehen, die die Größe unseres Planeten mit der unserer Sonne vergleicht, und diese dann wiederum mit anderen Sonnen. Japan war auf dieser kleinen Erde in diesem Buch nicht einmal erkennbar."


hi "Weißt du, was ich nie bemerkt hatte?"


show mishashort perky_smile_close onlayer master
with charachange

"Sie sieht mich erwartungsvoll an."


hi "Ihr Funkeln ist unglaublich."


show mishashort hips_grin_close onlayer master
with charachange

mi "Ahahaha~."


hi "Das ist mein Ernst."


show mishashort perky_confused_close onlayer master
with charachange

mi "Warum tust du das, Hicchan?"


hi "Was meinst du?"


show mishashort cross_frown_close onlayer master
with charachange

mi "Ich bin nicht blöd."


hi "Ich weiß es nicht. Aus mehreren Gründen. Weil du Shizunes Freundin bist? Und weil mir gefiel, wie nah ihr euch standet?"
hi "Und vielleicht versuche ich dir zu sagen, dass wir alle unsere Tiefpunkte haben, aber dass es dumm wäre aufzugeben. Jedenfalls scheint es die Mühe wert zu sein."


show mishashort sign_smile_close onlayer master
with charachange

mi "Das ist der einzige Grund?"


hi "Und du bist meine Freundin."


show mishashort hips_smile_close onlayer master
with charachange

mi "Das war's?"


hi "Darf ich nicht etwas ohne Grund machen?"


show mishashort hips_grin_close onlayer master
with charachange

mi "Wahaha~. Darfst du, darfst du~, Aber~ ich will es wissen."


hi "Na ja, was willst du sonst hören?"


play sound sfx_warningbell
stop music fadeout 3.0

"Bevor Misha antworten kann, klingelt die Glocke, weshalb ich mich am Ende mit einem Lachen von ihr zufriedengeben muss."


scene black onlayer master
with dissolve




label de_S34:

scene black onlayer master
with dissolve

"Ich sehe Misha in den nächsten Tagen seltener. Aber ich mache mir keine Sorgen, denn wenn ich sie sehe, sieht sie jedes Mal ein bisschen mehr nach ihrem alten Ich aus."


"Sobald es klar genug ist, dass ich keine Angst haben muss, dass mein Wunschdenken meine Sinne trübt, fange ich an, wieder gelassener zu werden."


window hide

with Pause(1.0)

scene bg school_dormhisao onlayer master
with openeye

window show

"Am Sonntag wache ich sehr früh und mit einem schummrigen Gefühl auf. Letzte Nacht bin ich wohl auch zu früh schlafen gegangen. Mit meinen Vorhängen stimmt auch etwas nicht – sie wollen nicht komplett zu gehen."


"Deswegen kann ich nicht einmal versuchen wieder einzuschlafen. Jedes Mal blendet mich die Sonne. Ich bin mir sicher, dass ich wahrscheinlich deshalb heute morgen so früh aufgewacht bin."


play sound sfx_doorknock

"Sich so schlecht und müde zu fühlen, ist die perfekte Welle der Frustration. Daher bin ich fast froh, als jemand an meiner Tür klopft."


scene bg school_dormhallway onlayer master
show kenji neutral onlayer master at center
with locationchange

play music music_kenji fadein 0.5

"Es ist ein vertrauter Besucher, der einen fast vollständig gegessenen Apfel in seiner Hand hält. Er beißt ein letztes Mal ab, versucht ihn in meinen Mülleimer zu werfen und verfehlt ihn total. Der Apfel zerplatzt zwei Meter zu hoch an der Wand."



"Fairerweise muss ich sagen, dass die meisten Stückchen danach doch noch in den Mülleimer fallen, aber ich bin mir ziemlich sicher, dass niemand so dreist ist, dass er mit Absicht darauf abzielen würde."


show kenji happy onlayer master
with charachange

ke "Perfekter Wurf!"


show kenji neutral onlayer master
with charachange

ke "'Sgeht, Mitbewohner?"


hi "Ich bin nicht dein Mitbewohner, wir wohnen nicht im selben Zimmer."


show kenji tsun onlayer master
with charachange

ke "Das ist unwichtig."


hi "Ist es nicht, du solltest wenigstens den Unterschied zwischen im selben Gebäude und im selben Zimmer wohnen kennen."


show kenji neutral onlayer master
with charachange

ke "Ich muss dein Zimmer benutzen."


hi "Wofür?"


"Ich hab's vergeigt, ich hätte „auf keinen Fall” sagen sollen."


show kenji tsun onlayer master
with charachange

ke "Der Schülerrat bringt mir nach wie vor meine Post, obwohl ich ihnen gesagt hab, dass sie sie in mein Schließfach oder so legen sollen."


ke "Aber sie schieben sie immer noch unter meiner Tür durch, ohne dass ich es bemerke. Darum lege ich mich heute auf die Lauer, um sie auf frischer Tat zu ertappen – wie ein Detektiv oder ein Safari-Jäger."


show kenji neutral onlayer master
with charachange

ke "Ich muss für heute in deinem Zimmer abhängen und durch das kleine Guckloch schauen, oder ich werde sie nicht auf frischer Tat ertappen. Und morgen vielleicht auch."


show kenji happy onlayer master
with charachange

ke "Es wird super. Wir bestellen uns Pizza – an beiden Tagen. Oder sollten wir nur einen Tag Pizza bestellen und am anderen etwas anderes? Nur was? Und welcher Tag ist der Pizza-Tag?"


hi "Heute nicht. Nie. Du weißt, ich bin im Schülerrat. Warum hast du mich nicht einfach danach gefragt?"


"Wenn er es hätte, hätte ich es sehr leicht herausfinden können und müsste Kenji nicht in mein Zimmer lassen."
"Es wäre eine Win-Win-Situation, nur dass er mir auf diese Weise wohl keine Pizza abluchsen könnte. Wahrscheinlich war genau das Kenjis Absicht."


"Aber… Nein, ich bezweifle es. Unmöglich, dass er so etwas Ausgeklügeltes planen könnte."


show kenji tsun onlayer master
with charachange

ke "Du weißt es?"


hi "Wann sie die Post zustellen? Na ja, nein. Üblicherweise geben sie mir meine Post einfach, wenn ich zum Schülerrat gehe."
hi "Worauf ich hinauswill ist, dass ich es herausfinden könnte, wenn ich sie danach frage. Dann wüsste ich es und könnte es dir sagen. So findet man etwas heraus. Man fragt."


show kenji neutral onlayer master
with charachange

ke "Nicht Höhlenmenschen. Oh ja, darauf fällt dir keine Antwort ein, was? Schachmatt."


hi "… Benutz dein eigenes Guckloch."


show kenji tsun onlayer master
with charachange

ke "Was, wenn sie mich sehen?"


hi "Können sie nicht, so funktionieren Gucklöcher. Sie sind wie ein Einwegspiegel."


show kenji happy onlayer master
with charachange

ke "Im Ernst? Na ja… Niemals. Sie werden sowieso erwarten, dass ich in meinem Zimmer bin. Sie werden meine Anwesenheit spüren und wissen, dass ich da bin. Sie würden niemals erwarten, dass ich im Zimmer gegenüber bin. "


hi "Ich werde zum Schülerratszimmer gehen und dir deine Post holen – jetzt gleich."


show kenji tsun onlayer master
with charachange

ke "Dann kann ich dich wohl nicht gehen lassen."


hi "Das ist bescheuert. Was, wenn ich mal aufs Klo muss?"


show kenji neutral onlayer master
with charachange

ke "Deine Spielchen funktionieren bei mir nicht."


scene bg school_dormhisao onlayer master
with locationchange

"Ich setze mich an meinem Schreibtisch und fange mit meinen Hausaufgaben für das Wochenende an."


hi "Weißt du, irgendwann wirst du auch rausgehen müssen, daher kannst du nicht ewig hierbleiben, oder mich für immer hier festhalten. Ich meine, vor allem ist das mein Zimmer."


show kenji neutral onlayer master at tworight
with charaenter

ke "Ja, das glaube ich auch. Um wie viel Uhr kommt normalerweise die Post?"


hi "Jetzt."


show kenji tsun onlayer master
with charachange

ke "Warum sind Frauen so langsam?"


hi "Warum scherst du dich überhaupt so sehr um die Post? Erwartest du etwas?"


show kenji neutral onlayer master
with charachange

ke "Ich erwarte immer etwas… Heute allerdings nicht."


hi "Willst du, dass sie etwas verschicken? Benutzt du die Post überhaupt?"


show kenji tsun onlayer master
with charachange

ke "Auf keinen Fall! So kriegen sie dich doch. Ich hab keine Post mehr verschickt, seit ich acht war. Da hab ich einen Brief an Lego geschickt und sie gebeten, Dragonball Legos zu machen."


show kenji happy onlayer master
with charachange

ke "Sie antworteten, dass sie die Rechte dafür nicht bekämen und gaben mir ein paar Gutscheine. Das war's absolut wert, aber danach hab ich sichergestellt, dass ich unterm Radar bleibe."


show kenji neutral onlayer master
with charachange

ke "Du verschickst keine Post, oder?"


hi "Ich hab letzte Woche meinen Eltern geschrieben."


show kenji tsun onlayer master
with charachange

ke "Aber so kriegen sie dich doch!"


hi "Stimmt, ich hätte es wissen müssen. Vielleicht haben sie mir deswegen am nächsten Tag diesen Mikrochip eingepflanzt."


show kenji neutral onlayer master
with charachange

ke "Also… waren die Gerüchte wahr."


"Ich würde gerne wissen, aus welcher Gerüchteküche er die hat."


hi "Ich mach nur Spaß. Das war ein Witz."


show kenji tsun onlayer master
with charachange

ke "Ein Witz? Verdammt. Du würdest mit mir scherzen? Ich schätze, so fühlt es sich an… verarscht zu werden."
ke "Ich hätte nie gedacht, dass mir das mal passiert. Das ist ein ernsthaftes Problem. Mann, ich denke, du kannst die Tiefen meines Dilemmas nicht verstehen."


ke "Es ist eine Aufführung in vielen Akten. Komplizierte Akte mit vielen Akteuren. Es ist wirklich schwierig, okay?"
ke "Nachdem ich fertig bin, werde ich zur Feier einen ganzen Fisch essen. Ahhhh, scheiße. Eigentlich wollte ich Pizza bestellen. Will ich immer noch. Kann ich Fisch auf der Pizza haben? Machen die das mittlerweile?"


hi "Du wirst sie bezahlen. Du hast mir mein Geld immer noch nicht zurückgegeben, und außerdem hab ich gerade eh keinen Hunger."


show kenji neutral onlayer master
with charachange

ke "Nicht in der Stimmung für Pizza? Das ist schlichtweg unmöglich, Jungchen."


show kenji tsun onlayer master
with charachange

ke "Trotzdem muss es Pizza sein. Ich bin in der Pizza-Phase meines Lebens. Vorher war ich in einer Eiscreme-Phase, aber meine Freundin hat mir immer den Erdbeerteil von meinem Fürst-Pückler-Eis weggegessen."


"Die Hälfte der Zeit ist es schwierig zu sagen, ob er es ernst meint. Ich kann seinen Gesichtsausdruck nur sehen, wenn er nicht gerade seine Nase an die Tür presst."


hi "Das bezweifle ich. Hey, du weißt, dass ich eine Freundin hab, oder? Und zwar nicht Iwanako, sondern die Schülerratspräsidentin."


show kenji neutral onlayer master
with charachange

ke "Schnee von gestern."


hi "Was? Ernsthaft?"


show kenji happy onlayer master
with charachange

ke "Ich hab meine Quellen."


show kenji tsun onlayer master
with charachange

ke "Wie auch immer… Dann dämmerte es mir, dass ich von all dem Eis dick geworden bin. Es war ein böses Erwachen. Als ob man an einem Strand schläft und von einer Welle getroffen wird, die deine Sandburg zerstört."


show kenji neutral onlayer master
with charachange

ke "Ich fing mit Joggen an. Musste die Kilos loswerden. Aber vielleicht… bin ich in Wirklichkeit vor mir selbst weggelaufen."


play sound sfx_doorknock
stop music
show kenji rage onlayer master:
    tworight
    ease 0.3 twoleft
with vpunch

"Ein plötzliches und andauerndes Klopfen lässt ihn weit genug rückwärts springen, um gegen die Wand hinter ihm zu knallen. Ich nutze die Gelegenheit, um die Tür zu öffnen."


play sound sfx_dooropen

scene bg school_dormhallway onlayer master
show shizu behind_blank onlayer master
with locationchange

ssh "Guten Morgen. Wie geht es dir?"


ke "Ich hab gehört, dass sie nicht ungeladen eintreten können, wenn du Salz vor die Eingangstür streust."


play music music_comedy fadein 4.0

scene bg school_dormhisao onlayer master
show kenji neutral onlayer master at center
with whip_left

hi "Ich werde kein Salz vor meine Eingangstür streuen."


show kenji happy onlayer master
with charachange

ke "Aber… du denkst darüber nach. Gut."


scene bg school_dormhallway onlayer master
show shizu behind_blank onlayer master
with whip_right

his "Guten Morgen. Bist du hier, um die Post zuzustellen?"


show shizu adjust_happy onlayer master
with charachange

"Shizune nickt und wedelt zwischen unseren Gesichtern mit ein paar Briefumschlägen. Ich nehme sie ihr ab, damit sie ihre Hände für eine Unterhaltung frei hat."


show shizu basic_normal2 onlayer master
with charachange

ssh "Woher wusstest du das?"


hi "Du hast sie ziemlich offensichtlich hinter deinem Rücken versteckt."


ke "Was versteckt?"


scene bg school_dormhisao onlayer master
show kenji tsun onlayer master at center
with whip_left

hi "Die Post."


scene bg school_dormhallway onlayer master
show shizu basic_normal2 onlayer master
with whip_right

with Pause(0.2)

show shizu adjust_smug onlayer master
with charachange

ssh "Schon okay, ich hab sowieso nicht wirklich versucht, sie zu verstecken."


hi "Das passt nicht zu dir. Sonst sagst du doch immer: „Man sollte bei allem, was man tut, sein Bestes geben.”"


ke "Mädchen ergreifen die Initiative? Und was ist mit mir? Ich hab diesen Spruch seit Jahren benutzt. Wo sind meine Lorbeeren, Alter?"


ke "Ich kreiere literarisches Gold und ihr Frauen klaut es einfach und leiert es aus wie ein billiges Sommerkleid. Ihr seid alle wie der Picard für meinen Kirk. Oder ihr könntet sogar Janeway sein."


show shizu behind_frown onlayer master
with charachange

ssh "Nicht die ganze Zeit über. Machst du dich etwa lustig über mich?"


show shizu adjust_happy onlayer master
with charachange

"Nachdem sie Kenji letztlich bemerkt, winkt sie ihm zu."


scene bg school_dormhisao onlayer master
show kenji tsun onlayer master at center
with whip_left

hi "Hey, Kenji, die Schülerratspräsidentin sagt hi."


show kenji neutral onlayer master
with charachange

ke "Hi."


scene bg school_dormhallway onlayer master
show shizu behind_blank onlayer master at center
with whip_right

ssh "Stell mich ihm vor. Ich hab keine Ahnung, was er gesagt hat, aber es sah selbstsicher aus."


"Oh ja, niemand ist besser darin, solche Sachen selbstsicher zu sagen."


hi "Das hab ich schon. Ich hab dich sogar mit Titel vorgestellt. Das ist Kenji, der Kerl von gegenüber. Sein Zimmer ist direkt hinter dir. Jedenfalls – hast du seine Post auch?"


show shizu adjust_happy onlayer master
with charachange

ssh "Ich bringe dir nur deine, weil sie schon da war. Ich hab frühen Zugriff! Es ist alles eine Frage der Lage. Betrachte es als einen Vorteil, im Schülerrat zu sein."


"Das hört sich nicht sehr fair an. Sie nutzt ihre Position ziemlich oft aus – zumindest was kleinere Dinge angeht."



label de_S34a:

ssh "Ich bin noch nie in deinem Zimmer gewesen. Sieht interessant aus."



label de_S34b:

ssh "Das ist das erste Mal, dass ich dein Zimmer richtig sehen kann."


"Das ist eine offenkundige Lüge, andernfalls hätte sie es viel schneller gebärdet. Ich bin mir sicher, dass sie selbst weiß, dass es nicht das erste Mal ist."



label de_S34c:

show shizu basic_frown onlayer master
with charachange

ssh "Warum darf er dein Zimmer sehen und ich nicht? Ist das ein Männerding?"


hi "Ein Mann zu sein heißt nicht, dass man einem Geheimbund angehört."


ke "Sollte es. Mit Ringen. Ringe mit riesigen Wappen. Und Gold!"


show shizu adjust_smug onlayer master
with charachange

ssh "Bist du sicher? Bist du dir wirklich sicher? Ich dachte immer, es gäbe eine geheime Männerbruderschaft."


ke "Warum ignoriert sie mich? Lass mich ihr vom Klub der Kerle erzählen. Außerdem – was soll das mit diesen Handzeichen? Versucht sie, mich zu verhexen oder so?"


scene bg school_dormhisao onlayer master
show kenji tsun onlayer master at center
with whip_left

hi "Nein, halt dich da raus. Ich müsste alles, was du sagst, für sie übersetzen, und ich weiß nicht mal, ob ich das hinkriegen würde."
hi "Außerdem würde sie es wahrscheinlich missverstehen und dann würdest du wahrscheinlich die Antwort missverstehen. Und dann müsste ich deinen Konter übersetzen."


show kenji happy onlayer master
with charachange

ke "Konter? Warum sollte ich kontern? Greift sie mich an?"


scene bg school_dormhallway onlayer master
show shizu behind_frustrated onlayer master at center
with whip_right

ssh "Was sagt er?"


hi "Er sagt, dass er keinen Konter hat."


show shizu basic_normal onlayer master
with charachange

ssh "Konter für was? Ich hab noch nicht mal anfangen, ihn herauszufordern."


"Mir gefällt nicht, wie sie das sagt. So wirkt es, als ob sie es noch vorhat. Aber mit was? Es ist egal, da es sowieso nicht gut ausgehen würde."


hi "Hör auf Streit zu suchen."


show shizu adjust_frown onlayer master
with charachange

ssh "Ich hab deine Freunde noch nie getroffen. Warum darf ich nicht? Es sieht aus, als wäre er… heißblütig."


"So wie er herumfuchtelt vermute ich, dass es dumm wäre, von Shizune etwas anderes zu erwarten. Jedenfalls wechsle ich besser das Thema."


"Zwar wird es bei ihr wahrscheinlich nicht funktionieren, aber ich bin mir sicher, dass sie noch aus einem anderen Grund hier ist, als nur meine Post abzugeben."


"Wenn es etwas Kleines wäre, hätte sie sich nicht einmal die Mühe gemacht zu klopfen."


hi "Du bist nicht nur hergekommen, um mir meine Post zu bringen und meine Freunde vollzulabern, oder?"


play sound sfx_snap

"Shizune schnipst mit gespielter Frustration mit ihren Fingern. Es ist so erschreckend laut wie immer."


show shizu basic_normal onlayer master
with charachange

ssh "Du hast Recht."


show shizu behind_smile onlayer master
with charachange

ssh "Lass uns wieder irgendwo hingehen."


hi "Hast du schon etwas im Hinterkopf?"


show shizu adjust_smug onlayer master
with charachange

ssh "Du hast wieder Recht. Lass uns zum üblichen Platz gehen."



"Sie zückt eine Tasche mit sorgfältig eingewickelten Behältern. Ich schätze, sie sind mit Essen gefüllt, und diesmal sieht es nicht nach Gekauftem aus. Sie setzt sie zwischen ihren Füßen ab und fährt fort."


show shizu behind_smile onlayer master
with charachange

$ doublespeak (ke, ssh, u"Ist das für mich?", u"Das war die echte Überraschung. Siehst du?")


show shizu adjust_smug onlayer master
with charachange

ssh "Am Ende muss ich einfach besser sein als alle anderen."


"Ich stimme zu – so wie man das eben tut, wenn jemand etwas sagt, das mehr über diese Person verrät, als beabsichtigt war."


show kenji invis onlayer master:
    center
    xpos 0.0
with None

show shizu behind_smile onlayer master at tworight
show kenji tsun onlayer master at twoleft
show bg school_dormhallway onlayer master at bgright
with dissolvecharamove

ke "Okay, schön. Wenn ihr mich beide ignorieren wollt, bin ich raus. Wie grausam. Das werdet ihr bereuen!"


stop music fadeout 2.0

hide kenji onlayer master
with charaexit

scene ev shizu_roof onlayer master at shizu_roof_in
with shorttimeskip

play ambient sfx_rooftop fadein 1.0
play music music_soothing fadein 0.5

"Kurze Zeit später befinden wir uns auf dem Schuldach."


"Ist es normalerweise um diese Zeit an so einem schönen Tag am Wochenende menschenleer?"
"Nein, natürlich nicht. Das kann eigentlich nur an Shizune liegen. Nicht, dass man mehr als ein Warnschild an der Tür brauchen würde, um das Dach leer zu kriegen."


"Die leeren Plastikbehälter, die Shizune für unser Essen gepackt hatte, liegen neben mir. Es war ein weiteres stilles Essen, da wir wegen der Stäbchen in unseren Händen nicht viel reden konnten."


"Der Wind ist heute ziemlich stark, obwohl er nicht so heftig weht, dass es ein Problem wäre."
"Er bläst die Plastiktüte unter den leeren Behältern weg und lässt sie etwas herumtanzen, bevor sie über mein Bein fliegt und sich an der Spitze von Shizunes Schuh verfängt."


show ev shizu_roof_towardsangry onlayer master at shizu_roof_in
with charachange

"Umgehend greift sie nach ihr und fängt an zu gebärden, gar nicht amüsiert, dass ich darüber lache – auch wenn sie selbst versucht, es sich zu verkneifen. Da die Tüte sie aber behindert, muss sie sich schließlich daraufsetzen, um fortfahren zu können."


ssh "Sehr witzig."


show ev shizu_roof_towardsnormal onlayer master at shizu_roof_in
with charachange

ssh "Wie war es?"


show ev shizu_roof2_towardsnormal onlayer master at shizu_roof_in
with charachange

his "Das Essen? Hat vertraut geschmeckt."


show ev shizu_roof2_towardsangry onlayer master at shizu_roof_in
with charachange

ssh "Also war es schlecht."


show ev shizu_roof_towardsangry onlayer master at shizu_roof_in
with charachange

his "Nein, nein. Als du das letzte Mal so ein Essen gemacht hast, war es genau das Gleiche."


"Nicht ganz gleich. Die frittieren Garnelen waren neu."


ssh "Es ist das Einzige, von dem ich weiß, wie man es macht. Aber ich sollte mich verbessert haben."


his "Wie oft hast du es denn schon gemacht?"


show ev shizu_roof_towardsnormal onlayer master at shizu_roof_in
with charachange

ssh "Das ist das zweite Mal."


his "Dass du dieses Gericht machst?"


show ev shizu_roof onlayer master at shizu_roof_in
with charachange

ssh "Dass ich koche."


show ev shizu_roof_smile onlayer master at shizu_roof_in
with charachange

ssh "Das nächste Mal bist du dran."


show ev shizu_roof_towardsangry onlayer master at shizu_roof_in
with charachange

"Es macht mich unruhig, wie sie die ganze Zeit an der Ecke der Tüte zupft. Ich glaube, ich weiß, warum sie es tut."


show ev shizu_roof2_towardsangry onlayer master at shizu_roof_in
with charachange

his "Ärgert es dich wirklich so sehr?"


show ev shizu_roof2_towardsnormal onlayer master at shizu_roof_in
with charachange

ssh "Ich will sie richtig einpacken."


show ev shizu_roof_towardsnormal onlayer master at shizu_roof_in
with charachange

his "Schon okay, ich mache es."



"Während ich sie aufhebe, bemerke ich, dass sie eine Menge Essen mitgebracht haben muss, um all diese Behälter zu füllen. Ich habe nicht einmal viel gegessen. Shizune muss einen gesunden Stoffwechsel haben, um das alles unterzubringen."


stop music fadeout 1.0
play sound sfx_impact

scene black onlayer master
with vpunch

"Obwohl ich gerade erst für eine Sekunde auf den Beinen gewesen bin, ist es lange genug, um über meinen eigenen Füße zu stolpern. Ich schaffe es gerade so, meinen Fall zu bremsen und lande schließlich auf allen Vieren neben Shizunes Schoß."


scene bg school_roof onlayer master
with locationchange

play sound sfx_heartslow
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack onlayer master
with Dissolve (0.7)

"Als ich versuche, mich aufzuraffen und mir dabei behutsam die Hand an die Brust halte, kann ich an nichts anderes denken als den Schmerz in meinen Knien – und dass dieser Sturz mich hätte umbringen können. Mir ist übel."


"Shizune hilft mir, aufrecht zu stehen, indem sie mich helfend an der Schulter festhält – wobei ich bemerke, dass sie mich seltsam beäugt. Unglücklicherweise ist sogar diese leichte Berührung genug, um mich zu erschrecken."


show shizu basic_normal2_close onlayer master:
    center
    ypos 1.1
with charaenter

ssh "Bist du okay?"


"Ich nicke, aber wir setzen uns nicht wieder nebeneinander hin."
"Natürlich ist es mit einer Menge Stille verbunden, mit Shizune allein zu sein, aber nun bemerke ich es erst so richtig. Das typische Zeichen von Unbehaglichkeit. Wiedereinmal ist sie diejenige, die das Eis bricht."


show shizu behind_smile_close onlayer master
with charachange

ssh "Ich hab erwartet, dass du etwas Unanständiges versuchst."


hi "…"


show shizu behind_sad_close onlayer master
with charachange

"Und schon ist die Stimmung wieder peinlich."


his "Wie geht es Misha?"


show shizu basic_normal_close onlayer master
with charachange

play music music_twinkle fadein 6.0

ssh "Misha scheint jetzt fröhlicher zu sein, wieder wie ihr altes Ich. Ich dachte, das wäre eine guter Anlass, um zu feiern. Und um dir zu danken, dass du ihr geholfen hast."


"Ihre Hand zögert etwas beim letzten Teil."


his "Du denkst zu sehr wie eine Geschäftsfrau."


show shizu behind_blank_close onlayer master
with charachange

ssh "Ich kann nichts dafür, so wurde es mir beigebracht."


show shizu adjust_happy_close onlayer master
with charachange

ssh "Ich bin froh, dass du nach Misha fragst. Es wäre passender zu sagen, dass sie „wieder wie vorher” ist. Nur für dich wäre das die „alte Misha”."


show shizu basic_normal_close onlayer master
with charachange

ssh "Die Misha, die du kennst, ist vollkommen anders als die, an die ich denke, wenn ich an mich an unser erste Begegnung zurückerinnere. Auch wenn ich finde, dass sie fröhlich und lächelnd besser aussieht, ist sie normalerweise nicht so."


show shizu behind_blank_close onlayer master
with charachange

ssh "Ich frage mich – ist es für dich genauso?"


"Ich antworte nicht."


his "Na ja, wenn Misha glücklich ist, dann ist es egal – solange es am Ende geklappt hat. Dein Plan hat funktioniert."


his "Du kanntest sie genauso gut, wie du gesagt hast. Du wusstest alles, was sie sagen würde. Aber wenn es deine Idee war, dass ich für dich rede, macht mich das dann nicht zu deiner Marionette? In dem Fall hätte ich nichts beigetragen."


show shizu cross_angry_close onlayer master
with charachange

ssh "Stimmt nicht. Du hattest die Idee zuerst."


show shizu basic_frown_close onlayer master
with charachange

ssh "Ich lag falsch. Jetzt, wo ich darüber nachdenke, betrachte ich die Dinge oft aus einem ganz falschen Licht. Das weißt du sicherlich. Manchmal behandle ich alles wie einen Wettkampf zwischen mir und allen anderen. Selbst wenn es sinnlos ist."


"Manchmal?"


show shizu behind_blank_close onlayer master
with charachange

ssh "Ich weiß sehr gut, wie einfach es ist, jemanden zu ignorieren, wenn derjenige mit dir nur per Zeichensprache kommunizieren kann."
ssh "Ich hätte um Hilfe bitten sollen, aber ich war mir so sicher, dass ich es allein hinkriegen würde. Du hast etwas sehr Tapferes getan – auch wenn du dir den Verdienst nicht anrechnen lassen willst."


show shizu basic_normal_close onlayer master
with charachange

ssh "Abgesehen davon bist du in letzter Zeit irgendwie bewundernswert geworden."


"Es ist komisch, von ihr gelobt zu werden, obwohl sich ihr Gesichtsausdruck in keinster Weise geändert hat."


show shizu adjust_frown_close onlayer master
with charachange

ssh "Aber!"


show shizu basic_happy_close onlayer master
with charachange

ssh "Dir zufolge „ändern sich Menschen nicht so leicht”. Hab ich Recht?"


"Sie zwinkert. Offensichtlich findet sie großen Gefallen an diesem Gespräch."


his "Erzählt Misha dir alles?"


show shizu behind_blank_close onlayer master
with charachange

ssh "Fast alles."


his "Ich schätze, du wirst mir jetzt sagen, dass ich damit falsch liege, nicht wahr?"


show shizu basic_normal2_close onlayer master
with charachange

ssh "Ja und nein."


show shizu adjust_frown_close onlayer master
with charachange

ssh "Ich war diejenige, die Misha das als erste gesagt hat. Aber sie hat es zu weit getrieben und die Bedeutung verändert. Sich zu ändern ist zwar nicht einfach, aber sie tut gleich so, als wäre es unmöglich."


show shizu basic_normal_close onlayer master
with charachange

ssh "Wenn man es Stück für Stück angeht, ist es möglich. Ich denke darüber nach, weniger wetteifernd zu sein."


his "Aber ich dachte, dir macht das Spaß?"


show shizu behind_smile_close onlayer master
with charachange

ssh "Vielleicht ein bisschen. Darum habe ich explizit „weniger” gesagt."


"Sie lehnt sich gegen den Zaun. Es gibt Dinge, die ich ihr sagen will, doch jetzt scheint irgendwie nicht der richtige Zeitpunkt dafür zu sein. Ich habe da so eine Ahnung. Ich weiß, dass sie noch nicht fertig ist."


show shizu basic_normal2_close onlayer master
with charachange

ssh "Viele Leute glauben, dass ich alles zu ernst nehme."


show shizu adjust_happy_close onlayer master
with charachange

ssh "Na ja… ich hab immer gedacht, dass ich gerade so genug tue."



"Das Geräusch des Zaunes, als sie sich gegen ihn drückt und die Knöpfe ihrer Ärmel gegen ihn klimpern, ist seltsam beruhigend. Genau wie die Brise, die sanft hinter mir aufzieht. Ich kann Menschen unter uns hören."


show shizu basic_normal_close onlayer master
with charachange

"Shizunes Augen huschen ebenfalls nach unten, und ich frage mich, ob sie immer noch darüber nachdenkt, was ihr eigentlich durch ihre Taubheit entgeht."
"Die aufmerksamkeiterregende Art, wie sie mit ihren Fingern schnippt, beweist, dass sie versteht, wie andere Menschen Ton wahrnehmen."


show shizu invis_close onlayer master at center
with dissolvecharamove

hide shizu onlayer master
with None

"Es muss merkwürdig sein, etwas zu begreifen, es aber nie selbst erfahren zu können."
"Sie beginnt langsam, am Rand des Daches entlangzulaufen, und lässt dabei immer noch ihre Knöpfe gegen den Zaun klimpern. Es ist vollkommen unrhythmisch – jedoch nicht, weil sie es nicht versucht."


show shizu invis_close onlayer master at twoleft
with None

show shizu basic_normal_close onlayer master at center
with dissolvecharamove

"Während sie das tut, verliere ich mich in Gedanken, und werde dann unsanft aufgeweckt, als sie mit ihrer kompletten Runde fertig ist und mir auf die Schulter tippt."


show shizu behind_blank_close onlayer master
with charachange

ssh "Weißt du noch, worüber wird geredet haben?"


his "Wann? Eben gerade? Na sicher doch."


show shizu basic_angry_close onlayer master
with charachange

ssh "Es ist fast zehn Minuten her."


show shizu adjust_frown_close onlayer master
with charachange

ssh "Als ich dich zum ersten Mal sah, schienst du sehr gefallen daran zu finden, in Selbstmitleid zu versinken."


"Das tut weh – auch wenn es wahr ist."


show shizu behind_smile_close onlayer master
with charachange

ssh "Entschuldige."


show shizu basic_normal_close onlayer master
with charachange

ssh "Ich wollte dich vom ersten Moment an aufmuntern. Allerdings hatte ich Angst, dass es für die Katz wäre. Irgendwie hatte ich das Gefühl, dass es schwierig werden würde, deine Einstellung zu ändern."


show shizu behind_smile_close onlayer master
with charachange

ssh "Aber du hast sie geändert. Das hat mich ziemlich überrascht, und ich dachte auch, dass du ziemlich einfach zu beeinflussen wärst."
ssh "Trotzdem war ich überrascht. Das hat mich dazu gebracht, viele Dinge zu überdenken. Wie zum Beispiel… dass sich am Ende vielleicht alles doch gelohnt hat."


his "Alles?"


show shizu adjust_happy_close onlayer master
with charachange

stop music fadeout 4.0

ssh "Darum mag ich dich."


his "Verstehe."


"Es ist schön, das endlich zu wissen."


stop ambient fadeout 2.0

scene black onlayer master
with dissolve



label de_S35:

scene bg school_council_ss onlayer master at right
show mishashort hips_smile_close_ss onlayer master at closeleft
show shizu behind_blank_close_ss onlayer master at closeright
with locationchange

play music music_ease

hi "… Und vergesst nicht – ihr müsst diesen Job ernst nehmen. Zu viele Leute glauben, dass man einfach faulenzen kann und dass es nicht wichtig ist. Das ist eine gefährliche Denkweise."


show mishashort cross_frown_close_ss onlayer master
with charachange

mi "Absolut~. Man kann es nicht zu ernst nehmen~! Ihr müsst zu jeder Zeit nach dem Besten streben und positiv denken. Denn wenn ihr irgendwelche Anzeichen von Schwäche zeigt, werden die Leute anfangen, euch für unfähig zu halten, wisst ihr~."


show mishashort sign_confused_close_ss onlayer master
with charachange

mi "Und schon bald werdet ihr nichts mehr bewerkstelligen können, weil euer Einfluss Stück für Stück auf andere umverteilt wird. Dann habt ihr nichts mehr. Das ist das letzte Mal passiert~."


show mishashort hips_grin_close_ss onlayer master
with charachange

mi "Also~! Denkt dran~, es mag wie ein leichter Job wirken, aber in diesen Zimmer können wahre Gemetzel stattfinden. Ahaha~. Und außerhalb davon."
mi "Beim Umgang mit Schulpersonal genauso! Schon der Versuch, einen Haushaltsbericht von einem Klassensprecher zu bekommen, kann manchmal ein Kampf auf Leben und Tod sein."


hi "… Genau. Fressen oder gefressen werden. Und in der Grube gibt es keine Freunde und ihr nehmt keine Gefangenen… Bist du dir da sicher? Ist das so richtig?"


show shizu basic_angry_close_ss onlayer master
with charachange

ssh "Du wirkst nicht begeistert genug. Ich muss sicherstellen, dass es richtig ankommt. Noch einmal – mit Elan!"


show aoi_keiko onlayer master:
    yalign 1.0 xanchor 0.5 xpos 0.0 alpha 0.0
with None

play sound sfx_flash

show bg school_council_ss onlayer master at left
show mishashort invis_close onlayer master at Position(xpos=1.1)
show shizu invis_close onlayer master at Position(xpos=1.6)
show aoi_keiko onlayer master:
    center
    alpha 1.0
with Dissolvemove(0.5)

"Shizune verdreht ihre Hand zur Betonung, als wäre sie ein Dirigent, womit sie sichtlich die beiden zuhörenden Mädchen vor uns einschüchtert."
"Wenn man bedenkt, dass das alles angefangen hat, weil eine von ihnen gefragt hat, ob sie ihren Job nicht etwas zu ernst nimmt…"


ssh "Habt ihr verstanden?"


hi "Habt ihr verstanden? Tut so, als ob ich schreie."


"Aoi" "Okay, okay! Aaargh! Dieser Schülerrat ist so abgedreht."


"Keiko" "Jawohl, Sir."


hi "„Sir”? Mit wem redet ihr beiden eigentlich?"


play sound sfx_flash

show bg school_council_ss onlayer master at right
show mishashort hips_smile_close_ss onlayer master at closeleft
show shizu adjust_frown_close_ss onlayer master at closeright
show aoi_keiko onlayer master:
    yalign 1.0 xanchor 0.5 xpos 0.0 alpha 0.0
with Dissolvemove(0.5)

ssh "Er ist nicht abgedreht! Ihr müsst es euch wie einen Job vorstellen. Wenn ihr wollt, stellt euch vor, dass sie euch mit dem Recht bezahlen, dieses tolle Büro zu benutzen."


play sound sfx_flash

show bg school_council_ss onlayer master at left
show mishashort invis_close onlayer master at Position(xpos=1.1)
show shizu invis_close onlayer master at Position(xpos=1.6)
show aoi_keiko onlayer master:
    center
    alpha 1.0
with Dissolvemove(0.5)

hi "Wollt ihr noch eine Standpauke?"


"Aoi" "Neeeeeiiin…"


ssh "Ihr dürft jetzt gehen."


stop music fadeout 5.0

scene bg school_council_ss onlayer master
show mishashort perky_smile_ss onlayer master:
    twoleft
    ypos 1.1
with shorttimeskip

"Und so ist die einstündige Schülerratseinführung vorüber."
"Persönlich dachte ich, dass sie circa fünfzig Minuten zu lang war. Und ich fand auch lustig, dass eine Führung durch die Schule, die wir alle schon seit einer Weile besuchen, mit dabei war. Aber ich schätze, es konnte nicht schaden."


"Ich rechne damit, dass Shizune sich in ihren Stuhl fallen lässt, da sie schon den ganzen Tag angespannt war, aber sie sie tut es nicht. Stattdessen läuft sie weiterhin im Zimmer auf und ab."


show shizu invis onlayer master:
    center
    xpos 1.0
with None

play music music_shizune fadein 1.0

show shizu adjust_frown_ss onlayer master at tworight
with dissolvecharamove

ssh "Die haben noch einen weiten Weg vor sich! Im Moment sind sie ein Witz."


show mishashort sign_confused_ss onlayer master:
    twoleft
    ypos 1.1
with charachange

mi "Eh?"


hi "Was?"


show shizu behind_frustrated_ss onlayer master
with charachange

ssh "Die glauben, sie könnten der neue Schülerrat sein? Die sind so unkoordiniert. Man kann den Mangel an Erfahrung regelrecht sehen. Das war bisher unser bestes Jahr; ich glaube nicht, dass sie das Zeug haben, um unsere Nachfolger zu werden."


show shizu basic_frown_ss onlayer master
with charachange

ssh "Und ich weiß, dass da noch mehr sind als nur diese beiden Mädchen. Wo sind die? Die sind wie das stark vermarktete aber mittelmäßige, heftig kritisierte Nachfolgeprodukt eines gefeierten low-budget Geheimtipps."


show mishashort perky_confused_ss onlayer master
show shizu behind_blank_ss onlayer master:
    ypos 1.1
with dissolvecharamove

"Schließlich bremst sie sich und setzt sich hin."


hi "Wirst du es vermissen?"


show shizu basic_normal_ss onlayer master
with charachange

ssh "Selbstverständlich."


show mishashort perky_sad_ss onlayer master
with charachange

mi "Hm~… Ich wäre auch glücklicher, wenn ich nicht fort müsste."


show mishashort hips_smile_ss onlayer master
with charachange

mi "Ich mag es, im Schülerrat zu sein, auch wenn es ermüdend sein kann."


hi "Ja, es ist definitiv ermüdend."


show mishashort hips_grin_ss onlayer master
with charachange

mi "Nur weil Shicchan immer mehr tun will, als sie eigentlich muss~."


show shizu adjust_frown_ss onlayer master
with charachange

ssh "Wenn ich nur das absolute Minimum getan hätte, hätten wir das ganze Jahr nur Flyer verteilt, Umfragen eingesammelt und die nächste Schülerratswahl geplant, damit der nächste Schülerrat auch ein ganzes Jahr mit Nichtstun verbringen kann."


show shizu behind_frown_ss onlayer master
with charachange

ssh "Sollte ich es dazu kommen lassen? Macht euch nicht lächerlich. So ein Schülerrat hätte kein bisschen Einfluss, mit dem man ein paar Rädchen drehen könnte."


show shizu adjust_happy_ss onlayer master
with charachange

ssh "Ich bin einfach nur froh, dass, obwohl ich sie noch härter rannehmen muss, diese beiden nicht schlecht sind. Zwar sind sie noch nicht soweit, aber der Schülerrat sollte in guten Händen sein."


hi "Woher willst du das wissen?"


show shizu behind_smile_ss onlayer master
with charachange

ssh "Nach dem Festival haben sie mich gefragt, ob wir auch ein Halloween-Event organisieren könnten – etwas wie ein Geisterhaus oder so in der Art. Sie hatten auch einen Haufen anderer Ideen."


show shizu adjust_smug_ss onlayer master
with charachange

ssh "Natürlich war meine Antwort „nein”. Ich hab Misha ihnen sagen lassen, dass sie es selbst machen sollen, wenn sie es so sehr wollen. Aus irgendeinem Grund waren sie daraufhin wütend."


show mishashort cross_laugh_ss onlayer master
with charachange

mi "Ahaha~."


hi "Natürlich waren sie wütend, wenn du sowas sagst."


"Und Misha die Botschaft übermitteln zu lassen, hat es sicher auch nicht besser gemacht."


show mishashort cross_smile_ss onlayer master
show shizu behind_blank_ss onlayer master
with charachange

ssh "Ich war auch wütend."


show shizu basic_frown_ss onlayer master
with charachange

ssh "Auf einmal wollen sie so viel. Wenn sie so sehr ein Geisterhaus, oder ein traditionelles Café, oder eine Fahrt an den Strand, oder sonst ein klischeehaftes Event haben wollten – warum haben sie es dann nicht selbst organisiert?"
ssh "Es war, als hätten sie mich ausgenutzt."


show shizu behind_frown_ss onlayer master
with charachange

ssh "Ich hatte so hart für die Organisation dieser Festivals gearbeitet, und als Dank kamen sie mir mit: „Das war nett, aber könntest du jetzt das tun? Und wie wäre es damit? Das will ich wirklich.”"


show mishashort sign_smile_ss onlayer master
with charachange

mi "Allerdings hatte Shicchan Unrecht~."


show shizu basic_happy_ss onlayer master
with charachange

ssh "Richtig. Sie wollten dem Schülerrat beitreten, damit sie es umsetzen können. Ich habe sie eifersüchtig gemacht und angestachelt. Das kann auch eine Art Motivation sein."


show shizu adjust_happy_ss onlayer master
with charachange

ssh "Der Wunsch, etwas Großes zu vollbringen, breitet sich aus – auch wenn sie es nur tun, um es mir zu zeigen. Jedenfalls haben sie beschlossen, die Herausforderung anzunehmen."


show shizu behind_blank_ss onlayer master
with charachange

ssh "Ich bin beeindruckt. Na ja, fürs Erste zumindest. Ich müsste das ein bisschen länger beobachten, um zu sehen, wie sie sich machen."


play sound sfx_snap

show shizu adjust_happy_ss onlayer master
show mishashort perky_confused_ss onlayer master:
    ease 0.1 ypos 1.05
    ease 0.1 ypos 1.1
with vpunch

"Plötzlich schnippt sie mit ihren Fingern, wodurch Misha blitzartig von ihrem Stuhl aufspringt. Interessant, ich schätze, es ist unmöglich, sich daran zu gewöhnen."


show shizu basic_happy_ss onlayer master
with charachange

ssh "Ach ja! Wir wollten doch eine Party für die Zügel-Übergabe an den neuen Schülerrat feiern, oder nicht? Warum machen wir das nicht jetzt? Oder planen es zumindest jetzt und feiern dann morgen."


hi "Aber sie haben das Amt doch noch gar nicht übernommen. Das war sogar das Erste, was du ihnen gesagt hast: „Ihr habt noch nicht das Sagen.” Es wirkt etwas voreilig."


show shizu adjust_frown_ss onlayer master
with charachange

shi "…"


show shizu behind_blank_ss onlayer master
with charachange

ssh "Misha, was meinst du?"


show mishashort hips_smile_ss onlayer master
with charachange

mi "Hmmm~, ich stimme da zu, es ist zu früh. Außerdem~ glaube ich nicht, dass ich teilnehmen könnte. Sorry~! Eigentlich wollte ich sogar gerade gehen."


ssh "Warum kannst du nicht?"


show mishashort hips_grin_ss onlayer master
with charachange

mi "Kein~ Kommentar~!"


show shizu adjust_frown_ss onlayer master
with charachange

ssh "Komm schon, sag es mir."


show mishashort perky_confused_ss onlayer master
with charachange

mi "Na ja… okay~!"


"Gut standgehalten, Misha."


show mishashort sign_confused_ss onlayer master
with charachange

mi "Ich hab drüber nachgedacht, und~… selbst wenn ich nicht mitfeiern wollte, würde ich ja sagen~! Normalerweise~. So bin ich nun mal. Ich sollte wirklich damit aufhören, und ich denke, jetzt ist ein guter Zeitpunkt, damit anzufangen."


show mishashort perky_sad_ss onlayer master
with charachange

mi "Wenn es eine Abschiedsfeier ist, dann will ich erst recht nicht. Es wäre zu traurig~. Ich will stattdessen etwas anderes machen. Und schließlich, Hicchan, werden du und Shicchan morgen immer noch hier sein. Das fühlt sich falsch an."


show mishashort hips_grin_ss onlayer master
with charachange

mi "Außerdem hab ich andere Schulangelegenheiten, die ich heute noch erledigen muss~! Ich kann sie nicht so einfach ignorieren."


show shizu adjust_frown_ss onlayer master
with charachange

ssh "Wir können es verschieben."


show mishashort hips_frown_ss onlayer master
with charachange

mi "Nein. Kein verfrühter Abschied~!"


"Als sie das sagt, sieht sie sehr entschlossen aus."


hi "Aber wolltest du jetzt nicht gehen?"


show mishashort hips_grin_ss onlayer master
with charachange

mi "Hm~? Oh, stimmt ja~! Wahaha~!"


show mishashort perky_smile_ss onlayer master at twoleft
with Dissolvemove(0.7)

show mishashort sign_smile_ss onlayer master
with charachange

mi "Okay, also, keine verfrühten Abschiede, okay?"


show shizu behind_blank_ss onlayer master
with charachange

ssh "Ich hab es kapiert."


show mishashort hips_grin_ss onlayer master
with charachange

mi "Okay, bis dann~!"


stop music fadeout 4.0

hide mishashort onlayer master
with charaexit

show bg school_council_ss onlayer master:
    subpixel True
    center
    parallel:
        "bg school_council_ni" with Dissolve(5.0)
    parallel:
        ease 5.0 bgleft
show shizu behind_blank_ss onlayer master:
    subpixel True
    parallel:
        "shizu behind_blank" with Dissolve(5.0, alpha=True)
    parallel:
        ease 5.0 xpos 0.5
with None

"Somit verbleiben lediglich Shizune und ich allein im Schülerratszimmer."


play music music_dreamy fadein 4.0

with Pause(2.0)

"Der Sonnenuntergang geht langsam in das Dunkel der Nacht über, während wir beide schweigend nach den passenden Worten suchen."


show bg school_council_ni onlayer master at bgleft
show shizu adjust_frown onlayer master:
    center
    subpixel False ypos 1.1
with Dissolvemove(0.5)

ssh "Wäre das wirklich so schlimm?"


his "Wäre es. Ich hab so noch nicht drüber nachgedacht, aber Misha hat Recht. Partys haben eine gewisse Stimmung, und diese wäre traurig. Eine traurige Party klingt nicht wirklich nach viel Spaß."


show shizu basic_angry onlayer master
with charachange

ssh "Warum wäre sie traurig?"


"Ist das eine Fangfrage? Dessen bin ich mir sicher. Shizunes Augen bohren sich in meine und warten mit einem distanzierten, analytischen Blick auf meine Antwort."
"Diesen Blick habe ich seit einer Weile nicht gesehen, aber er fühlt sich dennoch vertraut an. "


"Ich überlege mir meine Antwort genau, aber gleichzeitig frage ich mich, was hinter dieser Frage steckt."


"Es könnte sein, dass Shizune es genauso deprimierend findet. Oder es könnte sein, dass sie nicht nachvollziehen kann, warum es für jemanden traurig sein könnte. Bei Shizune ist beides möglich."


his "Mir ging durch den Kopf, dass es zu Ende ist, wenn du deinen Abschluss machst. Es wird das Ende des Schülerrats sein. Ich hab mich gefragt, ob du genauso denkst."


show shizu behind_frown onlayer master
with charachange

ssh "Stell dich nicht so an. Freu dich lieber drauf. Ich werde keine Schülerin mehr sein, also werden die Erwartungen auch ganz anders sein. Die Erwartungen anderer und vor allem meine eigenen Erwartungen. Klingt doch aufregend!"


show shizu adjust_frown onlayer master
with charachange

ssh "Was den Schülerrat betrifft, sollte er in guten Händen sein. Es gibt nichts, weswegen ich traurig sein müsste."


his "Ich glaube dir nicht. Es ist noch nicht mal eine Woche her, dass du wegen des Abtritts des Schülerrats ziemlich mitgenommen ausgesehen hast."
his "Es ging nicht darum, ihn an ein paar Grünschnäbel abzutreten, sondern darum, die Schülerratsarbeit komplett aufzugeben."


show shizu behind_smile onlayer master
with charachange

"Unerwarteterweise lächelt Shizune."


his "Also streitest du es nicht ab."


his "Dann ergibt das keinen Sinn. Warum würdest du das feiern wollen?"


show shizu basic_normal onlayer master
with charachange

ssh "Ich versuche darüber hinwegzukommen. Außerdem… Abschiedsfeiern sind sehr wichtig. Man sagt, der erste Schritt ist der wichtigste, aber es bis zum Ende durchzuziehen ist genauso wichtig, oder?"


his "Ich schätze, das ist wahr."


show shizu adjust_smug onlayer master
with charachange

ssh "Außerdem sehe ich es nicht als ein Lebewohl. Trotzdem ist es ein Ereignis. Es gehört sich, dass man es richtig würdigt."


show shizu behind_blank onlayer master
with charachange

stop music fadeout 4.0

ssh "Tust du es endlich mal?"


his "Was meinst du?"


show shizu basic_normal onlayer master
with charachange

ssh "Mich küssen, natürlich."


his "Meinst du das mit „richtig würdigen”?"


show shizu behind_blank onlayer master
with charachange

ssh "Es wäre normal, oder? Es passt in so einer Situation."


"Es ist Zeit, entschlossen zu handeln. Wenn ich es nicht tue, wird mein Herz mit Sicherheit explodieren."


show shizu adjust_blush_close onlayer master
with charachange

"Ich küsse sie sofort; so schnell, dass ich nicht einmal Zeit habe, es richtig zu genießen. Obwohl sie darauf vorbereitet war, läuft sie knallrot an. Ich spüre eine ähnliche Hitze, die meinen Hals und meine Wangen hinaufwandert."


play music music_one fadein 4.0

scene evh shizu_undressing_clothed_stare onlayer master
with whiteout

"Ich lehne mich für einen weiteren Kuss nach vorn, doch zur gleichen Zeit springt sie schelmisch auf den Schrank hinter ihr. Allein, in der vollkommenen Stille des Raumes, schauen wir uns für eine Weile einfach an."


show evh shizu_undressing_clothed_kiss onlayer master
with charachange

"Dieses Mal küsse ich sie länger. Ihr Lippen sind sanft und trocken und öffnen sich ein kleines Stück. Um dieses Gefühl zu genießen, bleiben mir nur ein paar Augenblicke, denn kurz darauf fängt Shizune an, meinen Kuss heftig zu erwidern."


"Als ich in ihrem Kuss versinke, streift ihr Pony gegen meine geschlossenen Augenlider. Durch ihre Kleidung kann ich ihre Figur spüren, was mich sie nur noch stärker festhalten lässt."


show evh shizu_undressing_clothed_blush onlayer master
with charachange

"Es bedarf etwas Anstrengung, um uns vom jeweils Anderen zu lösen. Wir beide erröten – von dem Kuss und von dem Gedanken daran, was gleich folgen wird, und ich bin bei Weitem nicht der Einzige, der etwas schwerfälliger atmet."


"Als Shizune beginnt, meine Krawatte loszubinden, fange ich, an ihre Bluse aufzuknöpfen. Es dauert einen Weile, bis ich den Dreh raus habe. Ich habe mir vorher nie wirklich Gedanken darum gemacht, wie die Blusen unserer Schule funktionieren."


"Shizunes Bluse liegt etwas eng an, deswegen hängen für einen kurzen Moment auch ihre Arme fest."
"Ich schäle Shizune aus ihrer Bluse heraus – auch wenn das durch ihren Versuch, sich dabei gleichzeitig herauszuschlängeln, nicht gerade einfach ist. Der Anblick ist ein bisschen skurril."


play sound sfx_rustling

show evh shizu_undressing_unclothed_closed onlayer master
with charachange

"Sobald Shizunes Arme frei sind, befreit sie sich von ihrem Hemd. Sie öffnet den Verschluss ihres Rocks und zieht ihn an ihren Beinen hinab, bis er ihr an den Knien hängt. Das Einzige, was sie jetzt noch bedeckt, sind ihr BH und ihr Höschen."


"Ihre Figur ist kurvig und straff, und die gesunde Farbe ihrer Haut kontrastiert mit dem Schwarz ihrer Unterwäsche. Es ist ein traumhafter Anblick, besonders wegen des Mondlichts, das hinter ihr durch das Fenster scheint."


show evh shizu_undressing_unclothed_blush onlayer master
with charachange

"Sie schaut auf meine Brust und öffnet die Knöpfe meines Hemdes – einen nach dem anderen."
"Der Vorgang wird im hohen Maße von meinen Händen verlangsamt, die sich an ihren Schenkeln auf und ab bewegen. Es ist ein wenig amüsant, auf diese Weise mit ihr zu spielen."


show evh shizu_undressing_unclothed_kiss onlayer master
with charachange

"Schließlich – endlich – fällt mein Hemd auf den Boden. Shizune überrascht mich, indem sie mich ruckartig und ohne Vorwarnung für einen tiefen Kuss an sich zieht, doch ich erwidere die Geste ebenso schnell."


show evh shizu_undressing_unclothed_talk onlayer master
with charachange

ssh "Warum bist du heute wagemutiger als auf dem Dach?"


ssh "Oder in deinem Zimmer?"


"Ich versuche, mir eine gute Antwort einfallen zu lassen, aber das ist gar nicht so leicht. Soll ich etwa sagen, dass Bürokratie mich in Wallung bringt?"


"Nachdem mein Hemd nun beseitigt ist, macht Shizune mit meinem Gürtel weiter, und anstatt ihre Frage zu beantworten, helfe ich ihr dabei. Ich glaube nicht, dass uns die Antwort an diesem Punkt noch etwas bringen würde."


scene bg school_council_ni onlayer master
with locationchange

"Der Gürtel löst sich leicht und fällt mit einem metallischen Klirren auf den Boden."
"Ich lehne mich für einen weiteren Kuss nach vorne und fahre dabei langsam mit meinen Händen ihre Seiten hoch. Doch dann taumelt sie plötzlich vorwärts, wodurch ich rückwärts stolpere."


"Nichts lag meinen Gedanken ferner als die harte Kante des Tisches hinter mir, bis ich spüre, wie sie mir in den unteren Rücken bohrt."
"Ich habe nicht einmal bemerkt, dass er da war. Ich packe Shizune noch etwas fester, während wir uns rückwärts auf die Tischfläche fallen lassen."


label de_S35h:

show evh shizu_pushdown onlayer master
with charachange

"Ich verkneife mir ein Seufzen, als sich Shizune siegreich über mich lehnt. Sie hat wieder einmal gewonnen."


"Ich bin abgelenkt, bis Shizunes BH auf mich herabfällt, als ob er aus dem Himmel gefallen wäre. Trotz meiner größten Bemühungen, es nicht zu tun, muss ich lachen, und es ist ansteckend genug, dass Shizune es mir gleichtut."


"Von ihrem BH befreit sind ihre Brüste größer als ich gedacht hätte – auch wenn sie unter ihrer Bluse schon erkennbar groß waren. Sie hebt den BH mit ihren Fingern auf und schnippst ihn weg, während meine Hände über ihren Körper gleiten."


"Während sie mit ihren Knien meine Beine auf dem Tisch spreizt, streift sich Shizune ihr Höschen ab, wobei meine Hände unbewusst zu ihrer Hüfte wandern, um ihr dabei zu helfen."
"Ich erhasche einen kurzen Blick auf meine Uhr. Es waren erst ein paar Minuten, doch es fühlt sich sehr viel länger an."


"Sie lässt sich nach unten sinken – näher und näher, bis sich unsere nackten Oberkörper berühren. Ihr Brüste fühlen sich auf der Narbe über meinem Herzen seltsam an."


window hide

show evh shizu_straddle_open onlayer master
with whiteout

with Pause(7.0)

window show

"Als Shizune sich aufsetzt, spüre ich, wie ich in sie hineingleite und wir uns vereinigen, während ihre Brüste sich von meinem Oberkörper lösen. „Ein Angriff an zwei Fronten”, fällt mir nüchtern zu dieser Lage ein. Das passt nur zu gut zu ihr."


show evh shizu_straddle_tease onlayer master
with charachange

ssh "Ich sollte jetzt einfach aufhören und dich in deiner Lust schmoren lassen."


"Sagt sie, als sie damit anfängt, sich gegen mich zu reiben. Das Gefühl lässt mich scharf einatmen. Sehr witzig Shizune. Bald schon verlieren sich meine Gedanken."


show evh shizu_straddle_closed onlayer master
with charachange

shi "… sss."


"Shizune beißt sich auf die Lippen, um ihre Stimme zu dämpfen. Eine ungewollte Stimme. So viel habe ich noch nie von ihr gehört, und als sie bemerkt, dass sie ihr herausgerutscht ist, errötet sie."


"Um es zu verschleiern, fängt sie an, sich heftiger zu bewegen, wodurch ich heftiger gegen sie stoße und meine Erektion tiefer in sie eindringt."


"Dieses plötzliche Gefühl bringt mich dazu, ihr meine Hüften entgegenzustoßen. Shizune kämpft gegen mich an und versucht, mich wieder festzunageln, als ich es schaffe, meine Arme unter meinem Rücken frei zu kriegen."


show evh shizu_straddle_smile onlayer master
with charachange

"In diesem Augenblick bewegen sich ihren Hüften als Antwort noch intensiver auf und ab."


"Der Klang von Shizunes sanftem, unterdrücktem Stöhnen und der Anblick ihrer üppigen Brüste, die bei jeder ihrer Hüftbewegungen auf und ab springen, wird in der Stille des Schülerratszimmers von Sekunde zu Sekunde erregender."


shi "Mhhpff…"


shi "… Nn…"


"Ich halte es kaum noch aus. Das angenehme, sich anstauende Gefühl zwischen meinen Beinen, multipliziert Shizunes Gewicht auf mir, erschwert es mir zu denken. Meine Hüften beginnen, sich von allein zu bewegen."


"Shizunes Hände drücken meine auf den Tisch. Jede ihrer Bewegungen ist wie eine Art Vorstoß."


"Die Tisch unter uns rumpelt unter unserem Gewicht. Ich denke nicht, dass er zusammenbrechen wird, aber es ist ziemlich laut."


show evh shizu_straddle_come onlayer master
with charachange

"Nicht, dass Shizune es bemerken würde. Ihr Tempo wird nur noch schneller, sodass es sich fast schon so anfühlt, als würde sie mich mit ihrer Energie quer über den Tisch schieben. Ohne Vorwarnung kommen ihre Bewegungen zu einem finalen Höhepunkt."


scene bg school_council_ni onlayer master
with locationchange
with vpunch

"Plötzlich hört sie auf und fällt mit so einer Wucht auf mich, dass, wenn sie sich dabei nicht selbst abgebremst hätte, ich bestimmt bewusstlos geschlagen worden wäre."
"Die schlimmste vorstellbare Situation: Jemand kommt zufällig herein, während wir K.O. sind."


"Ich bin überrascht, aber nicht genug, um zu vergessen, dass wir beide nackt sind. Genauso wenig wie die plötzliche und schmerzhafte Unterbrechung gerade."


"Warum musste das passieren? War es mit Absicht, um mich in meiner Lust schmoren zu lassen? Shizune atmet verlegen aus. Anscheinend ist sie auch wieder zu Sinnen gekommen."


show shizu behind_blank_nak onlayer master
with charaenter

ssh "Entschuldige, ich bin gestolpert. Oder ausgerutscht. Oder so etwas in der Art."


his "Dachte ich mir schon. Ist die Tür abgeschlossen?"


hide shizu onlayer master
with charaexit

"Sie steigt zügig vom Tisch herunter und huscht zur Tür, um sie zu überprüfen. Sie schließt sie dann ab, wieder auf, und schließt sie dann noch einmal ab. Um sicher zu gehen, zieht sie noch einmal am Türknauf."
"Als sie sich endlich sicher ist, macht sie eine bizarre Bewegung mit ihrer Hand."


with charaenter

ssh "Sicher!"


his "Freut mich, dass du alles so locker sehen kannst."


show shizu behind_frown_nak onlayer master
with charachange

ssh "Ich hab das nicht mit Absicht gemacht. Warum übernimmst du dann nicht die Führung?"


show shizu behind_smilelow_nak onlayer master
with charachange

ssh "Komm schon."


hide shizu onlayer master
with charaexit

"Ich packe Shizune an ihren Schultern und versuche diesmal, sie auf den Tisch zu legen."
"Ihr Gesicht verzieht sich, als die Kante des Tisches gegen ihren Rücken stößt, so wie es bei mir der Fall war. Sie entscheidet sich dazu, sich selbst auf den Tisch zu helfen."


scene evh shizu_table_smile onlayer master
with dissolve

"Dies ist auch das erste Mal, das ich Shizune unbekleidet vor mir liegen sehe. Die Konturen ihres Schlüsselbeins und ihrer Brüste sind herrlich. Meine Augen wandern von ihnen bis zu ihren wohlgeformten Hüften herab. Eine grazile Sanduhrfigur."


"Ich fahre mit meinen Händen von den Schultern abwärts entlang ihrer Kurven."


"Langsam dringe ich bis zum Anschlag in Shizune ein. Sofort umgeben mich eine intensive Wärme und Enge. Daraufhin nehme ich meine Stoßbewegungen wieder auf, um dort weiterzumachen, wo wir aufgehört haben."


"Jedes Mal, wenn unsere Hüften sich bei jedem Stoß berühren und wir uns aneinander festhalten, spüre ich eine unglaubliche Hitze von ihrem Körper auf meiner Haut."


"Darüber hinaus bin ich nun empfindlicher als zuvor. Und um das zu kompensieren, stoße ich härter in sie."


scene evh shizu_table_normal onlayer master
with charachange

"Meine Hände gleiten um ihre Hüftkurven, die ich dabei auch noch vorsichtig kitzle."
"Ich verliere fast das Gleichgewicht, als sie so heftig reagiert, dass sie ihre Hüften ruckartig emporhebt und wieder zurück in meinen Schritt fallen lässt. Beinahe wären wir beide auf dem Boden gelandet."


"Ich bewege meine Hände nach oben und greife nach ihren Brüste, so wie ich es schon immer tun wollte. Sie fühlten sich größer an als sie aussehen. Weich und perfekt geformt – sie passen nicht einmal in meine Hände."


"Sie windet sich unter mir, als ich meine Finger über ihre Nippel schnellen lasse, ergreift meine Finger und zieht mich näher zu sich. Es fühlt sich an, als würde ich mit ihr Ringen. Aus diesem Griff gibt es kein Entkommen."


"Seit dem ersten Moment, in dem sich unsere Hände berührt haben, waren wir vermutlich verbunden."


"Ob sie mich von einem Schülerrats-Event zum nächsten geschleift hat, oder wir uns als Liebende an den Händen gehalten haben – ich glaube, es war immer dasselbe. Das Selbstvertrauen, das sie allein dadurch übermittelt, wie sie meine Hand ergreift."


"Ihre Hände beben auf der Tischfläche und versuchen, sich in sie zu graben. Sie wickelt ihr Bein um meinen Rücken und drückt uns enger zusammen, wodurch wir noch enger verbunden werden und ich in ihr eingeschlossen werde."


show evh shizu_table_comeopen onlayer master
with charachange

"Ihre inneren Wände sind unbeschreiblich heiß und eng, und so wie sie sich gegen mich stößt, verstärkt es die Reibung nur noch. Das ist zu viel des Guten."


show evh shizu_table_comeclosed onlayer master
with whiteout

stop music fadeout 4.0

"Allzu bald ist das Gefühl vorüber."
"Alles, was ich danach tun kann, ist in ihr zu bleiben und meine Hände auf dem Tisch ruhen zu lassen – zum einen wegen Energiemangel und zum anderen, weil ihre Beine mich noch immer festhalten. Shizune hingegen lächelt fast verträumt."


"Der Anblick bringt mich ebenfalls zum Lächeln. Ihre Beine senken sich langsam, sodass ich mich herauswinden kann."


label de_S35x:

scene bg school_council_ni onlayer master
with locationchange

"Erschöpft lehne ich mich gegen einen Tisch und versuche, wieder zu Atem zu kommen, bevor ich mich wieder anziehe."


"Ich bemerke ein dumpfes, heißes Klopfen in meiner Brust, als ich mein Hemd wieder zuknöpfe. Das gibt allem, was gerade passiert ist, einen schlechten Nachgeschmack."


show shizu behind_smile_nak onlayer master
with charaenter

ssh "Es war ein Glücksfall, dass Misha nicht hier sein konnte, nicht wahr?"


his "Hast du heute einen Clown gefrühstückt?"


his "Ich frage mich, was sie zu tun hatte."


show shizu behind_blank_nak onlayer master
with charachange

"Shizune bewegt ihren Finger langsam durch die Luft und deutet auf die Tür."


ssh "Geh es dir selbst ansehen."


his "Warum sagst du es mir nicht einfach?"


show shizu behind_smile_nak onlayer master
with charachange

ssh "Es ist interessanter, wenn du es selbst siehst. Sehen ist Glauben."


his "Na sicher. Clever. Vielleicht tue ich das. Was ist mit dir? Bleibst du heute den ganzen Tag hier? Es wird langsam spät."


show shizu behind_blank_nak onlayer master
with charachange

ssh "Es kommt mir wie meiner letzter Tag als Schülerratspräsidentin vor, daher werde ich heute vielleicht hier übernachten."
ssh "Es könnte meine letzte Gelegenheit sein, nach einem langen Tag und dem Versuch, eine Frist einzuhalten, an meinem Schreibtisch einzuschlafen."


his "Das ist komisch."


his "Ich werde in meinem Bett schlafen."


ssh "Im Sitzen zu schlafen ist eine Fähigkeit. Eine sehr nützliche."


his "Richtig."


scene bg school_lobby_ni onlayer master
with locationchange

"Nachdem ich den Raum verlassen habe, denke ich wirklich einen Augenblick lang nach, ob ich nachsehen soll, was Misha gerade so treibt."
"Einfach weil Shizune so geheimnisvoll getan hat, als ob sie eine Zeitmaschine oder so etwas baut. Aber am Ende entscheide ich mich dagegen."





label de_S36:

scene bg school_courtyard_ni onlayer master
with locationskip

"Um diese Zeit des Jahres ist die Nachtluft besonders angenehm. Sie ist frisch und etwas feucht, aber nicht so kühl, als dass man dadurch schnell wieder ins Warme flüchten will. Dazu ist es noch so spät, dass der Hof vollkommen menschenleer ist."


"Nachdem Shizune und ich uns voneinander verabschiedet haben, mache ich mich auf den Rückweg zum Wohnheim. Ich bin dort aber noch nicht einmal angekommen, bevor meine Gedanken wieder woandershin wandern."


"Nachzusehen, was Misha gerade so im Schilde führt, scheint doch keine so schlechte Idee zu sein. Ich habe sowieso nichts Besseres zu tun. Keine Hausaufgaben. Nichts mehr zu lesen. Und darüber hinaus will ich es einfach wissen."


scene bg school_lobby_ni onlayer master
with locationchange

"Das ist nicht das erste Mal, dass ich nach Schulende im Hauptgebäude bin. Doch meistens verlasse ich es dann mit Shizune und Misha nach einem langen Tag im Schülerrat. Allein habe ich es noch nie betreten."


"Es ist still. Ein Wort, mit dem ich diese Hallen normalerweise nicht beschreiben würde. Sie sind etwas unheimlich. Ein Licht beginnt, vor mir aufzuleuchten. Sieht aus, als würde gleich etwas Horrorfilmmäßiges passiert."


play sound sfx_rustling
with vpunch

"Als ich eine Hand auf meiner Schulter spüre, erstarre ich reflexartig."


"Misha ist es nicht – andernfalls wären Hände über meine Augen gelegt, begleitet von einem geträllerten „Wer bin ich?”. Also, wer ist es? Ich hoffe, dass es nicht Kenji ist, oder zumindest jemand, den ich kenne, oder das wird ziemlich bizarr werden."


show shizu invis_close onlayer master at tworight
with None

show shizu behind_blank_close_ni onlayer master at center
with dissolvecharamove

play music music_happiness fadein 4.0

"Wer auch immer es ist, tritt rasch vor mich. Es ist Shizune."


hi "Was tust du hier?"


"Ich bin so erleichtert, dass ich vergesse, es zu gebärden."


show shizu adjust_frown_close_ni onlayer master
with charachange

"Shizune legt einen Finger auf ihre Lippen."
"Ich schätze, obwohl sie nicht hören kann, hat sie eine Vorstellung davon, was Lautstärke ist, und kann an meinem Gesichtsausdruck erkennen, dass ich ziemlich laut war. Und scheinbar ist laut zu sein gerade keine gute Idee."


"Aber warum ist dann ausgerechnet Misha ihre Übersetzerin?"


his "Oh, sehr witzig. Warum bist du hier?"


show shizu basic_normal_close_ni onlayer master
with charachange

ssh "Ich hab auf dich gewartet. Ich wusste, dass du kommen würdest. Auch wenn es eine Weile gedauert hat."


his "Du hast auf mich gewartet?"


show shizu behind_blank_close_ni onlayer master
with charachange

ssh "Hab ich doch gerade gesagt, aber das ist unwichtig. Wir müssen schleichen, wenn wir nicht von Misha entdeckt werden wollen. Sag mir Bescheid, wenn ich nicht leise genug bin, okay?"


show shizu basic_normal_close_ni onlayer master
with charachange

"Daraufhin fängt Shizune an, sich auf Zehenspitzen langsam durch die Halle zu bewegen. Ich klopfe ihr leicht auf die Schulter, um ihre Aufmerksamkeit zu bekommen."


his "Das ist nicht leise."


his "Warum müssen wir leise sein?"


show shizu behind_frustrated_close_ni onlayer master
with charachange

"Sie antwortet nicht – wahrscheinlich weil Gebärden und Schleichen gleichzeitig nicht ganz so einfach ist."


scene bg school_hallway3_ni onlayer master
with locationskip

"Bevor ich mich versehe, stehen wir vor unserem Klassenzimmer."


stop music fadeout 0.5
play sound sfx_snap
with vpunch

"Plötzlich erschüttert ein Geräusch wie das Knallen einer Peitsche die Luft, gefolgt von einem vertrauen, frustrierten Jammern."


"Ich bin mir sicher, dass so ein Knall nicht gut für mein Herz ist. Ganz davon abgesehen, dass in dieser Stille alles ungefähr eine Million Mal lauter klingt."
"Es kommt aus dem Klassenraum. Um einen Blick hineinwerfen zu können, schlängle ich mich neben Shizune."


scene ev misha_nightclass onlayer master:
    center
    xpos 0.4
show ovl misha_nightclass_aperture onlayer master at left
with silentwhiteout

play music music_comedy fadein 0.5

mu "Kannst du bitte aufhören, deinen Stift zu werfen? Wie kann man einen Stift überhaupt so laut werfen?"


ssh "Er sieht wirklich durcheinander aus."


"Was für eine Untertreibung. Ich habe Mitleid mit Mutou. Trotz einer Wand und einer dicken Klassenzimmertür konnte sogar ich hören, wie Mishas Stift die Schallmauer durchbricht."
"Wahrscheinlich hat es sein Trommelfell zerrissen und einen Abdruck in der Wand hinterlassen."


show ev misha_nightclass onlayer master:
    ease 1.0 xpos 0.23 xanchor 0.0
show ovl misha_nightclass_aperture onlayer master:
    ease 1.0 right
with None

mi "Ich werfe ihn nicht~. Wenn ich nervös werden, drehe ich ihn gerne, aber~… dann vergesse ich, dass ich ihn in der Hand hab, und…"


mu "Das ist egal. So oder so sollten keine Stifte durch die Gegend fliegen. Davon habe ich schon während der regulären Schulstunden genug; nach Feierabend brauche ich das nicht."


mi "R-Richtig~! Tut mir leid."


mu "Wie auch immer, hör auf Dinge zu werfen, zu schmeißen oder sie fallenzulassen – bitte. Lehrer haben auch etwas zu tun."


scene bg school_hallway3_ni onlayer master
show shizu behind_blank_close_ni onlayer master at center
with locationchange

"Ich bemerke, dass Shizune sich das gleiche Schauspiel ansieht. Mutou schreit mit voller Kraft und Misha ist einfach Misha."


"Ich kann sie halbwegs gut durch die Tür hören. Aber offensichtlich kann Shizune überhaupt nichts hören. Darum frage ich mich, wie das ganze für sie aussieht."


"Sie muss es wissen, da sie die Lage gut genug begreift, um es mich auch sehen lassen zu wollen. Aber ich frage mich, ob sie ab und zu denkt, dass ihr etwas entgeht und sie sich deshalb viel mehr anstrengend muss, um das Beobachtete zu verstehen."


show shizu basic_normal_close_ni onlayer master
with charachange

ssh "Sieht aus, als würde sie Nachhilfeunterricht nehmen. Hab ich Recht?"


his "Ja."


"Antworte ich, obwohl ich weiß, dass die Frage rein rhetorisch ist."


show shizu behind_smile_close_ni onlayer master
with charachange

ssh "Misha sagte mir, dass sie später einmal wirklich eine Lehrerin für Zeichensprache sein will. Wenn sie eine Empfehlung bekommt, kann sie dafür im Ausland studieren. Darum arbeitet sie so hart. Ihre Noten waren immer eher schlecht."


his "Jetzt fühle ich mich schuldig. Ich habe noch nicht einmal drüber nachgedacht, was ich eigentlich werden will."


show shizu adjust_smug_close_ni onlayer master
with charachange

ssh "Ich auch nicht!"


"Die fröhliche Art, wie sie das gebärdet, passt ganz und gar nicht zu ihr. Und es ist offensichtlich eine Lüge."


show shizu basic_normal2_close_ni onlayer master
with charachange

ssh "Lass uns gehen, ich will nicht gesehen werden. Es wäre problematisch, wenn wir erwischt werden, wie wir hier draußen wie zwei Idioten stehen."


his "Wohin? Zum Schülerratsraum?"


show shizu adjust_happy_close_ni onlayer master
with charachange

stop music fadeout 3.0

show shizu invis_close onlayer master at tworight
with dissolvecharamove

"Sie schüttelte ihren Kopf und eilt dann in das gegenüberliegende Klassenzimmer."


scene bg school_room34_ni onlayer master
with locationchange

his "Tolles Versteck."


show shizu behind_blank_ni onlayer master at center
with charaenter

ssh "In letzter Zeit bist du ungewohnt sarkastisch. Wenn die Tür zu ist, ist es ein Gutes. Außerdem – war das nicht interessant?"


his "Ja, aber ich bin nicht wirklich überrascht."


play sound sfx_doorclose


show shizu adjust_smug_ni onlayer master at Position(ypos=1.1)
with dissolvecharamove

"Ich schließe die Tür hinter uns, was Shizune zu einem lautlosen Lachen veranlasst, während sie sich in einen Stuhl fallen lässt. Für eine Sekunde deprimiert es mich. Ich will ihr echtes Lachen hören."


show shizu behind_smile_ni onlayer master
with charachange

play music music_innocence fadein 10.0

ssh "Ich war es. Ich habe auf Misha herabgesehen. Ich hätte nicht gedacht, dass sie überhaupt ein Ziel hat."
ssh "Aber ich habe mir voreilig ein Urteil gebildet und lag damit falsch. Ich dachte, Misha wäre so planlos wie ich. Ich war dumm. Ich habe verloren."


show shizu basic_normal_close_ni onlayer master
with charachange

"Shizune pausiert, um mit ihren Knöcheln zu knacken. Dann faltet sie ihre Hände übereinander und lehnt sich in ihrem Stuhl nach vorne."
"In der abnormalen Stille des Gebäudes kann ich sogar durch den Flur und zwei Türen wieder hören, wie Mutou Misha anschreit."


"Shizunes Augen sind auf meine fixiert. Starr hinter ihren glänzenden Brillengläsern beobachten sie meine Reaktion auf ihre Worte."


"Das ist ein Test. Sie bildet sich selten ihre Meinung über Leute, anhand deren Antworten auf Fragen. Was bei ihr zählt, sind die Antworten auf Feststellungen."


"Im Nachhinein ergibt das Sinn. Shizunes Unfähigkeit zu sprechen – genauso wie ihre allgemeine Persönlichkeit – bedeuten, dass sie alles „Gesagte” auch wirklich meint."


"Aus diesem Grund bezweifle ich manchmal, dass sie irgendetwas ohne Hintergedanken sagt."


"Das klingt bemerkenswert paranoid. Sogar Kenji würde das denken. Unglücklicherweise denke ich so sehr darüber nach, dass ich vergesse, ihr zu antworten."
"Sie fasst es so auf, als gäbe es keine. Bei diesem Test gab es ein verstecktes Zeitlimit – ein kürzeres als sonst."


show shizu adjust_smug_close_ni onlayer master
with charachange

ssh "Wie ich es mir gedacht habe."


his "Was meinst du?"


show shizu behind_blank_close_ni onlayer master
with charachange

ssh "Du stimmst mir nicht zu?"


his "Nicht wirklich, das ist es nicht. Ich verstehe es nicht."


show shizu basic_normal2_close_ni onlayer master
with charachange

ssh "Ich will den Leuten meinen Willen aufzwingen."


"Wie erfrischend ehrlich."


show shizu behind_frown_close_ni onlayer master
with charachange

ssh "Schau mich nicht so komisch an. Das ist nicht immer meine Absicht gewesen."


show shizu basic_normal_close_ni onlayer master
with charachange

ssh "Am Anfang war mir einfach langweilig. Ich wollte sehen, wie jemandes Leidenschaft für etwas aufflammt. Dann könnte ich versuchen, sie darin zu schlagen. Ich wollte ihre Überzeugung testen."


show shizu adjust_frown_close_ni onlayer master
with charachange

ssh "Aber das war unmöglich. Niemand auf dieser Schule kann sich für etwas begeistern. Sie wollen alle für sich allein bleiben."


show shizu behind_frustrated_close_ni onlayer master
with charachange

ssh "Ich konnte das nicht glauben. So war es doch viel zu langweilig. Ich konnte einfach nicht fassen, dass es wirklich Leute mit so einer trostlosen Einstellung gibt. Das geht weit über „nicht anecken wollen” hinaus."


show shizu adjust_angry_close_ni onlayer master
with charachange

ssh "Sie mussten einfach irgendwelche Interessen haben. Sie hatten ganz bestimmt etwas verborgen. Ich wollte es entlarven, offenlegen und ans Licht zerren."


show shizu behind_blank_close_ni onlayer master
with charachange

ssh "Einer der besten Wege, um Leute zum offen sein zu bewegen und sie aufzumuntern, ist ihnen offen mit einer Geschichte über dich selbst zu begegnen. Und dann bringst du sie behutsam dazu, von sich selbst zu erzählen."


show shizu adjust_happy_close_ni onlayer master
with charachange

ssh "Es ist wie ein Geben und Nehmen, aber mit etwas Manipulation. Das macht es interessant."


show shizu behind_blank_close_ni onlayer master
with charachange

ssh "Ich kann das nicht tun. Wenn ich versuche, Misha über mich reden zu lassen, lässt mich das in meinen Augen arrogant wirken."
ssh "Die Nachricht muss über einen Botschafter mitgeteilt werden. Ich stehe also neben Misha und sage ihr, dass sie jemandem von mir erzählen soll."


show shizu adjust_frown_close_ni onlayer master
with charachange

ssh "Man muss keine Gebärdensprache verstehen, um das zu erkennen. Würde ich so etwas miterleben, würde ich denjenigen auch für arrogant halten."


show shizu basic_angry_close_ni onlayer master
with charachange

ssh "Ich war frustriert. Mir fiel kein Weg ein, wie ich mich mit jemandem außer Misha unterhalten konnte. Niemand wollte sich mir öffnen."


show shizu behind_frown_close_ni onlayer master
with charachange

ssh "Ich kam zu dem Schluss, dass ich die Menschen nicht dazu bringen konnte, sich mir anzuvertrauen oder an mich zu glauben."
ssh "Ich kann nur Dinge erschaffen, sie Leuten zeigen und darauf hoffen, sie damit glücklich zu machen. Oder ich könnte energischer sein und hoffen, dass ich irgendwann jemandem näherkomme."


"Ich schätze, das wäre dann ich. Irgendwie deprimierend."


show shizu basic_normal_close_ni onlayer master
with charachange

ssh "Irgendwann habe ich dann vermutlich angefangen, Misha zu ignorieren – oder sie weniger als Person, sondern eher als eine Erweiterung meiner selbst zu sehen. Ich glaube, ich habe einfach vorausgesetzt, dass sie da ist."


show shizu behind_sad_close_ni onlayer master
with charachange

ssh "Ich vergaß, dass Misha die ganze Zeit da war und sich mir geöffnet hat. Sie hat jeden Tag hundert Prozent gegeben."


show shizu basic_angry_close_ni onlayer master at center
with Dissolvemove(0.7)

ssh "Ich habe das, wonach ich gesucht habe, übersehen, weil es direkt vor mir lag."
ssh "Wie dumm von mir. Ich bin wirklich arrogant geworden. Deswegen habe ich verloren. Ich bin kurzsichtiger, als ich es damals gewesen bin. Ich bin in die falsche Richtung gegangen."


"Sie schreitet mittlerweile fast grübelnd auf und ab. Sie hat noch so viel Energie, dass stillzustehen sie fast verrückt macht."


"Wenn man ihr zwei Drähte geben würde, könnte Shizune bestimmt eine Glühbirne zum Leuchten bringen. Es ist komisch, dass ich so einen fröhlichen Gedanken habe, während sie so ernst ist."


show shizu adjust_frown_close_ni onlayer master
with charachange

ssh "Und trotzdem erzählt mir Misha, dass ich ihre Inspiration sei. Ist das nicht lachhaft? Ich bin kein Mensch, der andere inspirieren kann."


show shizu behind_blank_close_ni onlayer master
with charachange

ssh "Auch wenn ein Mensch, der dich inspiriert, seine Fehler hat, kann man das akzeptieren. Ich habe darüber nachgedacht. Es gibt sogar annehmbare Scheinheiligkeit."


show shizu basic_normal2_close_ni onlayer master
with charachange

ssh "Zum Beispiel… Wenn dein Held ein Sportler ist, aber unfair, könnte man ihn immer noch wegen seiner athletischen Fähigkeiten respektieren, auch wenn er als Mensch seine Mängel hat."


play sound sfx_snap
show shizu adjust_angry_close_ni onlayer master
with charachange

ssh "Aber…"


"Sie schnippt mit ihren Fingern. In diesem leeren Raum klingt es wie ein Donnerschlag. Shizune nimmt sich ein paar Sekunden Zeit, um ihre Finger zu strecken. Da fällt mir auf, dass sie zuvor noch nie so viel gebärdet hat."


show shizu cross_angry_close_ni onlayer master
with charachange

ssh "Wenn jemand wie ich keine Ziele hätte, wäre das absolut inakzeptabel. Es wäre die größte Heuchelei von allen. Und Heuchler verdienen keine Verantwortung für andere, wenn sie nicht einmal für sich selbst Verantwortung übernehmen können."


"Wie unglaublich pessimistisch. Darüber nachzudenken, macht mich wütend."


"So muss ich vor ein paar Monaten auf andere gewirkt haben. Ich hätte mein damaliges Ich gehasst."


"Und das Lustige daran ist, dass Shizune und Misha mich davon abgebracht haben. Ich bin mir sicher, dass ohne sie alles ganz anders ausgegangen wäre – und das nicht zum Besseren."


"In letzter Zeit kommt es mir so vor, als würden wir unser Elend genauso teilen wie wir uns gegenseitig unterstützen – aber ich denke, das gehört dazu, wenn man Freunde hat und sich nahesteht."


his "Trotzdem bist du die Anführerin."


show shizu behind_frown_close_ni onlayer master
with charachange

ssh "Nur, weil es niemand anderes sein will."


his "Aber trotzdem bist du es. Jedenfalls schenken die Leute dir ihr Vertrauen. Macht es das eigentlich nicht noch wichtiger?"


his "So oder so bist du die Anführerin. Du bist die inspirierende Figur, oder wie auch immer du es nennen willst. Du bist verantwortlich für das, was du zähmst."


his "Das habe ich mal irgendwo in einem Buch gelesen."


show shizu basic_normal_close_ni onlayer master
with charachange

ssh "Das ist clever."


"Shizune scheint ihre Gefühle nur auf ihrem Gesicht zu zeigen, wenn sie es auch wirklich will. Aber ich glaube nicht, dass sie es sarkastisch meint."


show shizu adjust_frown_close_ni onlayer master
with charachange

ssh "Allerdings will ich niemanden „zähmen”."


his "Die Anführerin zu sein oder bewundert zu werden. Das ist das gleiche."


show shizu behind_frustrated_close_ni onlayer master
with charachange

ssh "Ich wollte nie die Anführerin sein, es ist einfach dazu gekommen."


his "Das glaube ich nicht. Du versuchst doch immer, mehr und mehr Verantwortung zu übernehmen."


show shizu adjust_frown_close_ni onlayer master
with charachange

ssh "Halt, halt. Ich wollte damit nicht sagen, dass es mir keinen Spaß macht."
ssh "Ich lege keinen Wert darauf, die Anführerin sein, aber ich hab auch nichts dagegen. Ich lege keinen Wert darauf, die Beste sein, aber ich hab auch nichts dagegen. Aber du hast Recht mit dem Verantwortung wollen."


show shizu basic_happy_close_ni onlayer master
with charachange

ssh "Natürlich will ich mehr davon. Wenn ich Verantwortung habe, fühle ich mich lebendig. Darum bin ich auch dem Schülerrat beigetreten: Ich kann es einfach nicht ab, wenn ich nicht unter Druck stehe."


show shizu behind_blank_close_ni onlayer master
with charachange

ssh "Dennoch bin ich nun die Anführerin. Ich dachte immer, Anführerin sein, heißt Befehle geben, aber es ist viel mehr als das."


show shizu adjust_frown_close_ni onlayer master
with charachange

ssh "Es heißt, ein Ziel zu haben. Wenn ich kein Ziel habe, ist es sinnlos. Die Leute würden mir nur zu meinem eigenen Vergnügen folgen. Es wäre egoistisch."


"Eine merkwürdig moralische Sichtweise für jemanden, der es so sehr liebt, andere zu übertrumpfen."


show shizu basic_normal2_close_ni onlayer master
with charachange

"Sie lässt ihr Kinn auf ihren Fingern ruhen und brütet angestrengt über ihre Probleme."
"Shizune sieht entwaffnend kindisch aus; ihr Gesichtsausdruck ist ein bisschen drollig, da es so offensichtlich ist. Genau deswegen sieht es ihr aber auch nicht ähnlich."


his "Das Ziel kommt mit der Zeit. Ich denke, du bist dazu bestimmt, eine Anführerin zu sein. Mit etwas anderem würdest du dich nicht zufrieden geben; es würde dich nur langweilen."


show shizu basic_frown_close_ni onlayer master
with charachange

"Shizune erwidert nichts, doch anhand ihres genervten Gesichtsausdrucks glaube ich, dass ich richtig geraten habe."


his "Ich habe darüber nachgedacht, dass ich auch etwas Orientierung brauche."


show shizu adjust_happy_close_ni onlayer master
with charachange

ssh "Wurde dir erzählt, dass es wichtig ist, etwas zur Gesellschaft beizutragen?"


"Was für eine ungewöhnliche Antwort. Sie kommt so unerwartet, dass ich nicht weiß, was ich darauf entgegen soll. Und sie beunruhigt mich auch, obwohl ich nicht weiß warum. Möglicherweise weil sich das so gar nicht nach Shizune anhört."


"Darum beginne ich zu bezweifeln, dass das überhaupt Shizunes Gedanke ist."
"Ich frage mich, wer ihr das gesagt hat. Na ja, wahrscheinlich war es ihr Vater. Aber es ist auch möglich, dass sie selbst darauf gekommen ist. Falls ja, liegt es dann an ihrer Taubheit?"


his "Warum fragst du das?"


show shizu behind_blank_close_ni onlayer master
with charachange

ssh "Einfach so."


his "Das glaube ich dir nicht."


his "Aber du hast wahrscheinlich Recht."


show shizu basic_normal_close_ni onlayer master
with charachange

ssh "Verstehe."


show shizu adjust_frown_close_ni onlayer master
with charachange

ssh "Ich weiß nicht, ob ich das genauso sehe. Ich hasse es."


"Ich vermute, dass sich jeder nach einer Bestimmung sehnt. Wenn ich zurückdenke, ergibt es Sinn, dass Shizune keine hat. Andernfalls wäre all ihre Energie auf etwas gerichtet gewesen."


"Da sie nichts hatte, worauf sie sie konzentrieren konnte, hat sie mit ihr wild um sich geschossen. Das erinnert mich an eine abgetrennte Starkstromleitung im Sturm: Blindwütig und funkenspeiend, jedoch ziellos und gefährlich. Genau wie Shizune."


"Ich würde gerne sagen, dass das der Grund ist, warum sie aus allem einen Wettkampf machen muss, aber… so ist sie wahrscheinlich einfach. Ein Ziel zu haben, auf das sie diese Energie lenken kann, ist lediglich die nächste Stufe."


show shizu behind_blank_close_ni onlayer master
with charachange

ssh "Wie wäre es damit? Ich könnte in die Wirtschaft gehen. Meine Familie ist gut vernetzt, darum sollte es nicht allzu schwierig sein… Das klingt etwas unethisch und vetternwirtschaftlich, oder?"


his "Ein bisschen."


show shizu adjust_frown_close_ni onlayer master
with charachange

ssh "Jedenfalls werde ich keinen Leerlauf haben. Ich werde hart arbeiten, bis ich ganz oben angekommen bin."


ssh "Wenn ich so viel Geld wie möglich hab, so viel, dass ich nicht einmal weiß, was ich damit anfangen soll, gehe ich zur nächsten Stufe über. Natürlich nachdem ich es eine Weile gehortet habe, versteht sich. Wie ein Drache im Märchen."


his "Du willst eine…?"


show shizu basic_happy_close_ni onlayer master
with charachange

ssh "Wohltäterin werden!"


hi "…"


show shizu adjust_smug_close_ni onlayer master
with charachange

ssh "Tss tss. Was dachtest du denn? Dass ich ein Geizhals werden will?"


show shizu behind_blank_close_ni onlayer master
with charachange

ssh "Na ja, stimmt schon, das ist Teil des Plans. Aber unterstell mir nicht, dass ich auf dieser Stufe aufhören würde."


stop music fadeout 8.0

"Shizune sieht nach wie vor nervös aus. Sicherlich; selbst wenn sie ihr Problem anscheinend so zügig gelöst hat, kann niemand so schnell über seine Sorgen hinwegkommen. Niemand kann seine Probleme so einfach lösen."


"Das Wichtige ist, dass es aussieht, als hätte sie fest beschlossen, es zu versuchen. Noch ist es schwer zu sagen, ob dieser Drang einen guten oder schlechten Ursprung hat."


"Doch nun hat sie etwas, an das sie sich festklammern kann. Das glaube ich aufrichtig. Ich freue mich für sie. Und zur gleichen Zeit ist mir etwas kalt. Denn jetzt hinke ich hinterher. Jetzt bin ich der Einzige ohne ein Ziel."


$ suppress_window_after_timeskip = True

scene black onlayer master
with dissolve



label de_S37:

window hide None
nvl clear

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_daily fadein 0.5

scene bg school_dormhisao_bw onlayer master
with dissolve

nvl show dissolve

n "\n\n\n\n\n\n\n\n\nSeit dieser Woche gab es keine weiteren Zwischenfälle."


nvl clear

n "Natürlich dachte ich das die Woche davor auch. Seit ihrer Aussprache verstehen sich Misha und Shizune wieder so gut, dass ich mir fast ein wenig verloren vorkam. Ich hatte beinahe schlaflose Nächte deswegen."


n "Doch zum Glück waren meine Sorgen unbegründet. Und dann, bevor ich mich versah, gab es so viel in der Schule zu tun, dass ich es sogar schaffte, mich von ihnen abzulenken. Dann ging alles wieder seinen normalen Gang."


n "Ich lag falsch. Ich hatte Shizunes und Mishas sorgfältig versteckte Schwachstellen gesehen, doch sie waren immer noch stark."


n "Nun werden wir bald unseren Abschluss machen. Ich fühle mich an dieser Schule so wohl, dass ich das lange Zeit verdrängt habe. Als das nicht mehr möglich war, war ich traurig und wollte nicht darüber nachdenken. Darum tat ich es auch nicht. Nicht bis vor Kurzem."


n "Ungefähr vor einer Woche fing ich an, eine Liste von Leuten zu schreiben, von denen ich mich vor meinem Abschluss verabschieden sollte. Die erste Regel, die ich mir auferlegte habe, war, dass ich sie ohne bestimmte Reihenfolge aufschreiben würde, wie zum Beispiel unwichtig bis hin zu wichtig."


n "Irgendwie ist es trotzdem dazu gekommen, auch wenn die Liste kürzer ausgefallen ist, als ich erwartet hatte. Kenji ist irgendwo in der Mitte."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

scene bg school_dormhisao onlayer master
show kenji neutral onlayer master at center
with locationchange

window show

ke "Sie haben gesagt, dass ich irgendwann meinen Abschluss machen muss. Nun, ich hab's ihnen gezeigt. Ich hab hier lang genug mietfrei gelebt. Wenn man die steigenden Grundstückskosten bedenkt, kann man wohl sagen, dass ich am Ende gewonnen hab."


show kenji happy onlayer master
with charachange

ke "Nein, weißt du was? Ich habe gewonnen. Die Geschichte wird mich als den Sieger anerkennen."


hi "Sieger wovon?"


ke "Ich hab es geschafft, unterm Radar zu bleiben und durch die Lücken zu schlüpfen. Ich hab das System geschlagen."


hi "Wenn du es so sagst, klingt es, als wärst du einfach vor dem System weggerannt."


ke "Manchmal ist Wegrennen die größte Form des Sieges – wie bei den Olympischen Spielen."


"Ich bin zu Müde, um mit ihm debattieren. Wem will er etwas vormachen? Jeder weiß, dass Kugelstoßen auf jeden Fall die beste olympische Disziplin ist."


hi "Was du damit also sagen willst ist, dass du sie nicht vermissen wirst?"


show kenji neutral onlayer master
with charachange

ke "Was vermissen?"


hi "Die Schule, Holzkopf."


show kenji tsun onlayer master
with charachange

ke "Nein. Wie ich dir schon gesagt hab, diese Schule hat zu viele Feministinnen. Sie ist nicht mehr zu retten. Aber immerhin kann ich verschwinden, bevor die kritische Masse erreicht ist."
ke "Ich werde erst zurückkommen – Jahre später – wenn sie mir zu Ehren eine Statue errichten."


hi "Machen die hier dieses 10-Jahre-Später-Klassentreffen-Ding?"


show kenji neutral onlayer master
with charachange

ke "Woher soll ich das wissen? Wahrscheinlich. Wie auch immer, ich muss jetzt packen. Pass auf dich auf, Mann."


hi "Du hättest vor einer Woche schon packen sollen – so wie ich."


"Nicht, dass es viel zu packen gab."


show kenji tsun onlayer master
with charachange

ke "So läuft das nicht. Du solltest alles erst in letzter Minute erledigen. Männer sind besser darin, alles im letzten Moment zu machen, denn die letzte Minute kann produktiver sein als die ganze Woche davor. Das ist unsere Geheimstrategie."


show kenji neutral onlayer master
with charachange

ke "Pffff, du wirst den Weg eines Mannes nie verstehen."


hi "Pass du auch auf dich auf."


show kenji happy onlayer master
with charachange

show kenji invis onlayer master at right
with dissolvecharamove

play sound sfx_doorslam

hide kenji onlayer master
with vpunch

"Er salutiert, huscht dann rückwärts durch die Tür und knallt sie so laut hinter sich zu, dass es wahrscheinlich das ganze Wohnheim gehört hat. Mir ist aufgefallen, dass das hier eine Menge Leute tun. Vielleicht ist das Brauch an dieser Schule."


"„Pass auf dich auf.” Das war das erste Mal, das ich so etwas von ihm gehört habe. Meistens enden unsere Unterhaltungen mit etwas wie „ciao” oder „ich zahl's dir später zurück, Mann.”"
"Na ja, manchmal war er etwas nervig, aber er wird mir fehlen. Ich streiche ihn gedanklich von meiner Liste."


"Mittlerweile ist die Liste sehr kurz, und noch einmal widerstehe ich der Versuchung, einer bestimmen Rangfolge nachzugehen. Wie schon gesagt, das hatte ich nie vor."


scene bg school_dormhallway onlayer master
with locationchange

"Darum gehe nun nach Shizune und Misha sehen. Mir fällt nur ein Ort ein, wo sie sein könnten. Das Schülerratszimmer natürlich."


play ambient sfx_crowd_indoors fadein 2.0

scene bg school_lobby onlayer master
show crowd onlayer master
with locationskip

"Als ich an der Ecke abbiege, remple ich beinahe gegen eine kleine Gruppe von Schülern. Für eine Sekunde blitzt in mir ein bitteres Gefühl auf. Denn nach allem, was ich weiß, hätte das tödlich sein können."


"Es ist der neue Schülerrat. Es sind nicht viele, aber weit mehr als drei. Das ist gut, denn das bedeutet, dass es genug sind, dass jeder seinen eigenen Titel haben kann."


"Es wäre cool gewesen, wenn ich ein kleines Tischschild mit meinem Namen und Titel darauf gehabt hätte. Allerdings glaube ich nicht, dass sie das noch machen. Oder je gemacht haben – leider."


"Während ich nachdenke, umstellt mich der neue Schülerrat. Wenn jemand sich das vom Weiten aus ansehen würde, wäre es ein ziemlich unheimlicher Anblick."


"Vielleicht sind sie gekommen, um es mir heimzuzahlen, dass ich sie ständig „der neue Schülerrat” genannt habe. Ich habe nur für Shizune übersetzt, aber ich schätze, dass ich weniger faul und etwas taktvoller hätte sein sollen. Ich bereue nichts."


"Aber sie danken mir nur für „alles, was ich getan habe”."


"Mir wird gedankt. Das sollte mich glücklich machen, wenn man bedenkt, wie oft ich selbst gedacht habe, dass im Schülerrat zu sein ein vollkommen undankbarer Job sei. Es macht mich auch glücklich, nur kann ich es nicht richtig genießen."


$ renpy.music.set_volume(0.5, 1.0, channel="music")
$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

window hide
nvl clear
nvl show dissolve

n "\n\nIch frage mich, wie die Dinge gelaufen wären, wenn unser Schülerrat so groß geworden wäre, wir der, der uns nun ersetzen wird."


n "Selbst wenn sie nur zwei, drei weitere Mitglieder gefunden haben, sind es genug, um feste Rollen haben zu können. Nicht wie bei uns, wo Shizune die Präsidentin zu sein schien und das war's."


n "Dass der neue Schülerrat mir dankt, fühlt sich seltsam an. Es ist, als würde man nach Hause kommen und sehen, dass ein Baum gewachsen ist, den man jahrelang gepflegt hat. Aber es kommt mir so vor, als hätte ich diesen Baum nicht genug gepflegt. Ich frage mich, was ich noch hätte tun können."


n "Es würde Shizune wahrscheinlich zur Weißglut treiben, dass ich mich so distanziert von allem fühle, was ich im Schülerrat getan habe. Oder dass ich andeuten würde, nicht genug getan zu haben. Aber es ist wahr. Ich bin ihr nur gefolgt."


n "\nGewissermaßen fühle ich mich also, als würde ich diesen besagten Baum aus weiter Ferne sehen. Als ob ich ihn aus dem Fenster eines vorbeifahrenden Zuges sehe."


$ renpy.music.set_volume(1.0, 1.0, channel="music")
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
stop music fadeout 4.0

nvl hide dissolve
nvl clear
window show

"Ich habe diesen Gedanken schon zu lange nachgehangen. Als ich mich von ihnen losreiße, bemerke ich, dass ich immer noch dort stehe – umringt vom neuen Schülerrat."
"Ich tue das Einzige, wozu ich in der Lage bin, und entschuldige mich fürs Abschweifen. Dann danke ich wiederum ihnen."


stop ambient fadeout 0.5

scene bg school_council onlayer master
with locationchange

play music music_normal fadein 3.0

"Während sie davongehen, betrete ich den Schülerratsraum, der nun viel unordentlicher aussieht, aber anscheinend einen Computer bekommen hat."




"Es ergibt Sinn; ich weiß noch, dass eines der Mädchen darüber geredet hat, einen Computer einzusetzen, um all die langweilige Dateneingabe, die Shizune macht, etwas erträglicher zu machen."


"Jedoch weiß ich nicht mehr, welche von ihnen das gesagt hat. Aoi scheint die ehrgeizigere zu sein, Keiko wiederum wirkt ernster. Na ja, ist ja mittlerweile auch egal."


"Ich bin nicht allein im Raum, doch anstatt der erwarteten Shizune finde ich lediglich Misha vor. Sie sitzt auf Shizunes Schreibtisch, wie Shizune es selbst oft tut, und lässt ihre Beine vor und zurück baumeln."


show mishashort invis onlayer master:
    center
    ypos 1.2
with None

show mishashort hips_grin onlayer master at center
with Dissolvemove(0.5)

"Als sich unsere Augen treffen, springt sie auf und nimmt unerklärlicherweise eine Superheldenpose ein."


mi "Hi, Hicchan~! Ich bin überrascht, dich hier zu sehen~!"


hi "Was treibst du hier?"


show mishashort cross_smile onlayer master
with charachange

mi "Du zuerst~!"


hi "Ich hab nach Shizune gesucht."


show mishashort cross_grin onlayer master
with charachange

mi "Ich auch~! Ich dachte, sie würde hier sein, aber stattdessen hab ich Hicchan bekommen~!"


hi "Na so was, danke."


show mishashort sign_smile onlayer master
with charachange

mi "Wahaha! Nun~, das ist gut. Wirklich, wirklich~. Ich wollte sowieso mit dir reden."


hi "Über was?"


"Ich nehme mir etwas Zeit, um meinen Blick durch den Raum schweifen zu lassen. Ich sehe eine Kochplatte. Die lassen es sich wirklich gut gehen."


show mishashort perky_sad onlayer master
with charachange

mi "Ich wollte Entschuldigung sagen~, natürlich~. Für all den Ärger, den ich dir und Shicchan bereitet habe."


hi "Nenn es nicht „Ärger”."


show mishashort sign_confused onlayer master
with charachange

mi "Okay~, okay~."


hi "Und entschuldige dich nicht bei Shizune."


show mishashort hips_smile onlayer master
with charachange

mi "Ahaha~. Okay~, okay~. Aber deswegen bin ich nicht hier, Hicchan. Ich würde mich nicht bei Shicchan entschuldigen. Aber da du hier bist, würde ich dir gerne eine Frage stellen."


show mishashort perky_confused onlayer master
with charachange

mi "Hicchan, was glaubst du braucht es, damit Shicchan glücklich ist?"


hi "Weltherrschaft, offensichtlicherweise."


show mishashort cross_laugh onlayer master
with charachange

mi "Wahaha~"


show mishashort hips_smile onlayer master
with charachange

mi "Auch wenn du es als Spaß meinst, Hicchan~… Nein, selbst wenn sie es könnte, würde es Shicchan nicht glücklich machen. Höchstens für eine kurze Zeit."


show mishashort sign_smile onlayer master
with charachange

mi "Hicchan, hast du je von Künstlern gehört, die beim Anblick ihrer gerade fertiggestellten Gemälde in Tränen ausbrechen? Solche Leute gibt es wirklich auf der Welt, weißt du~!"


show mishashort perky_smile onlayer master
with charachange

mi "Es ist mir ganz plötzlich wieder eingefallen. Es ist genau wie bei Shicchan – jetzt wo ich darüber nachdenke. Wann immer Shicchan sich eine Herausforderung stellt und sie meistert, tut sie so, als hätten ihre Fähigkeiten keine Bedeutung mehr."


show mishashort perky_confused onlayer master
with charachange

mi "Ich frage mich~ – ist es, weil sie nichts Dauerhaftes erschaffen kann?"


show mishashort perky_sad onlayer master
with charachange

mi "Es ist genau wie bei diesen Künstlern – sie wollen der Nachwelt ein Kunstwerk hinterlassen~, ein wirklich herausragendes~, aber sie können das nicht."
mi "Wenn ich zurückblicke, ist es ziemlich offensichtlich~, aber~ ich hab es vorher nie erkannt. Und jetzt habe ich Angst. Ich frage mich, ob Shicchan jemals glücklich sein wird."


hi "Nein, da bin ich anderer Meinung. Ich denke, die liegst falsch. Shizune ist eigentlich öfter glücklich, als ich gedacht hatte."


hi "Ich finde es ehrlich gesagt ziemlich beeindruckend. Normalerweise denken Leute nicht über so etwas nach, bis sie mittelalt oder am Sterben sind. Dann denken sie sich: „Ich will etwas hinterlassen.” oder „Ich will in Erinnerung bleiben.”"


"So wie ich."


"Ich habe das ganze nur etwas übersprungen. Mein Leben war kurz und schien nach meiner Herzattacke sogar noch kürzer."


"Ich habe nicht darüber nachgedacht, was ich zurücklassen würde, weil ich sehr schnell dachte, dass es so gut wie nichts sein würde. Darum war alles, was es für mich noch zu tun gab, in meiner eigenen Verbitterung zu schmoren."


hi "Shizune will bereits jetzt irgendwo ihren Fußabdruck hinterlassen. Doch sie will es tun, indem sie andere Menschen unterstützt. Deswegen sind Feste für sie so wichtig. Sie will sogar eine Wohltäterin werden."


hi "Ich denke, das ist die beste Art zu leben – an dem fortzubestehen, was man anderen gibt. Und wenn es aus einem selbstsüchtigen Grund ist, ist das auch okay."


hi "Shizune ist bereits glücklich, denn falls sie ein Ziel erreicht, wird es immer jemanden geben, der es sehen und sich daran erinnern kann. Genau das macht sie glücklich."


"Misha seufzt, lässt ihre Arme steif an ihren Seiten herabhängen und hebt dann einen Zeigefinger in die Luft."


show mishashort sign_sad onlayer master
with charachange

mi "Früher dachte ich immer… hm~… ich wäre vielleicht in der Lage, Shizune glücklich zu machen. Und früher war ich auch in einer guten Position, um das zu tun. Da ich ihre Übersetzerin war, konnte ich immer bei ihr sein. Vielleicht…"


show mishashort perky_confused onlayer master
with charachange

mi "Und~, ich dachte, ich täte es, indem ich… na ja… Shicchans Schatten werde. "


show mishashort perky_sad onlayer master
with charachange

mi "Ich hab's weiter versucht, auch wenn sie mich zurückgewiesen hat."
mi "Ich fühlte mich, als wäre ich hilflos und könnte nur zusehen, wie Shizune ihr Leben weiterlebt und sich mehr und mehr von mir entfernt. Obwohl ich es einfach hätte akzeptieren sollen, hatte ich Angst."


mi "Es ist schwierig. Vielleicht hätte ich Shicchan zumindest verstehen können."


show mishashort cross_smile onlayer master
with charachange

mi "Doch es sieht so aus, als hätte ich am Ende vollkommen falsch gelegen~… Ich wusste das nicht mal, oder hab mir keine Gedanken drum gemacht… Shicchan würde das eine glatte Niederlage nennen."


show mishashort cross_frown onlayer master
with charachange

mi "Okay~, ich bin durch. Das war's Hicchan~. Aber~! Da du derjenige bist, der Shicchan von allen am besten kennt, darfst du sie nicht zum Weinen bringen. Sonst werde ich sauer~!"


show mishashort hips_smile onlayer master
with charachange

mi "Sobald das hier vorüber ist, gehe ich ins Ausland. Ich hab sogar Empfehlungsschreiben. Ich glaube auch nicht, dass ich ohne die weit kommen würde~! Vielleicht studiere ich ja und werde dort eine Gebärdensprachelehrerin? Wer weiß~!"


show mishashort hips_grin onlayer master
with charachange

mi "Das heißt~! Du musst auf Shicchan aufpassen, okay?"


stop music fadeout 8.0

"Mishas Lächeln ist so aufrichtig wie immer, doch sie hat sich offenbar verändert. Der Blick in ihren Augen ist der eines viel aufmerksameren Mädchens. Es scheint zu stimmen, dass Not weise macht. Es erinnert mich an den Blick in Shizunes Augen."


"Ich frage mich, was Shizune wohl durchgemacht hat, um zu der Person zu werden, die sie jetzt ist. Ich kann nur raten. Oder vielleicht war sie auch schon immer so."
"Nun will ich sie mehr denn je sehen und schlage Misha vor, dass wir zusammen nach ihr suchen sollten."


"Natürlich ist das nur ein Vorwand, um mehr Zeit mit einer Freundin zu verbringen."
"Es ist seltsam, dass es noch gar nicht so lange her ist, dass wir drei in der straffen Routine eines Schülerratstages zusammen herumgelungert haben. Dennoch fühlt es sich an, als wäre es Ewigkeiten her."


"An die Zukunft zu denken, kann die Bilder verzerren, die man von der Vergangenheit hat."


"Apropos Bilder…"


scene bg school_courtyard onlayer master at bgleft
show yuuko neutral_up onlayer master at center
with locationskip

play music music_ease fadein 8.0

"Draußen, mit einer winzigen, modern aussehenden Kamera in der Hand, steht Yuuko herum. Die Kamera wäre kaum zu sehen, wenn sie nicht metallisch genug wäre, um das Sonnenlicht zu reflektieren."
"Misha ruft nach ihr. Ich dachte, wir wollen nach Shizune suchen?"


show yuuko neutral_up onlayer master at tworight
show bg school_courtyard onlayer master at center
with charamove

show mishashort hips_grin onlayer master at twoleft
with charaenter

mi "Hi~ hi~!"


show mishashort cross_smile onlayer master
with charachange

mi "Was tust du hier~?"


show yuuko closedhappy_down onlayer master
with charachange

yu "Ich mache nur Fotos von allen."


show mishashort hips_grin onlayer master
with charachange

mi "Das sieht man~!"


"Peinlich. Misha, ich werde nie vergessen, wie du mich gelehrt hast, dass jemand so viele Geheimnisse haben kann, und trotzdem einen riesigen Mangel an Taktgefühl."


hi "Wo ist mein Foto?"


show yuuko worried_up onlayer master
with charachange

yu "D-Du willst eine Kopie? Ich… weiß nicht. Na ja… Nur wenn du versprichst, es geheimzuhalten. Sonst wollen alle Eins."


show mishashort cross_smile onlayer master
with charachange

mi "Das ist mir in der Grundschule passiert, nur da waren es Süßigkeiten~!"


show yuuko smile_up onlayer master
with charachange

yu "Okay… dann mache ich jetzt ein Foto von euch."


hi "Ah, warte, ich bin noch nicht bereit. Ich hab nur Spaß gemacht."


show mishashort sign_smile onlayer master
with charachange

mi "Hicchan~, mach ein Peace-Zeichen~!"


hi "Das werde ich nicht."


play sound sfx_camera
with cameraflash

"Der Kamerablitz leuchtet auf und blendet mich."


show mishashort perky_confused onlayer master
show yuuko worried_down onlayer master
with charachange

"Yuuko geht hinter der Kamera in Deckung und stöhnt frustriert auf. Wenn man draußen ist, sollte man den Blitz eigentlich nicht anmachen."


show yuuko invis onlayer master at right
with dissolvecharamove

"Sie fängt an, sich unnötig zu entschuldigen und macht sich dann still davon."


hi "Ah, warte."


show yuuko worried_up onlayer master at tworight
with dissolvecharamove

yu "Ja?"


show mishashort sign_smile onlayer master
with charachange

mi "Hast du Shicchan hier irgendwo gesehen~?"


show yuuko neutral_up onlayer master
with charachange

yu "Ja… Vor dem Tor."


hi "Danke."


"Ich habe kaum Zeit, es auszusprechen, bevor ich Misha hinterhereilen muss."


play ambient sfx_crowd_outdoors fadein 3.0

scene bg school_gate onlayer master
show crowd onlayer master at center
show shizu behind_blank onlayer master at center
with locationskip

"Glücklicherweise nicht allzu lange. Das Tor ist kaum eine Gehminute weg von hier, auch wenn sogar das manchmal ermüdend für mich sein kann. Wir entdecken Shizune mit dem Schülerrat. Wahrscheinlichen danken sie ihr gerade auch."


$ renpy.music.set_volume(0.3, 1.0, channel="ambient")

show shizu adjust_frown onlayer master
with charachange

hide crowd onlayer master
with charaexit

"Sobald sie uns sieht, scheucht sie sie davon. Was sehr einfach ist, da ich bezweifle, dass einer von ihnen Zeichensprache versteht oder benutzen kann. Darum sollte weggeschickt zu werden nicht allzu tragisch für sie sein."


"Was in mir wiederum die Frage aufwirft, warum sie ihr danken würden, ohne jemanden dabei zu haben, der es kann. Aber der Gedanke zählt."


show mishashort invis behind shizu at twoleft onlayer master
with None

show mishashort hips_grin onlayer master:
    xpos 0.36
show shizu adjust_blush onlayer master
with Dissolvemove(0.4)

show bg school_gate onlayer master at bgright
show mishashort perky_smile onlayer master at twoleft
show shizu behind_smile onlayer master at tworight
with dissolvecharamove

"Misha fällt Shizune sofort um den Hals und lehnt sich dann neben ihr gegen das Tor. Ich hingegen beschließe, etwas zurückzubleiben und sie sich unterhalten zu lassen. Immerhin wollte Misha die ganze Zeit mit Shizune reden. Ich kann warten."


show bg school_gate onlayer master at right
show shizu invis onlayer master:
    xpos 0.4
show mishashort invis onlayer master:
    xpos 0.0
with dissolvecharamove

"Ich wende mich sogar ab, damit ich ihre Unterhaltung nicht „belausche”."


"Irgendwann verliere ich das Zeitgefühl."


"Als ich auf meine Uhr sehe, sind bereits zehn Minuten vorbei. Ich frage mich, ob sie fertig sind, und als ich mich umdrehe, stehen sie hinter mir."


show bg school_gate onlayer master at bgright
show mishashort perky_smile onlayer master at twoleft
show shizu behind_blank onlayer master at tworight
with dissolvecharamove

ssh "Woran denkst du gerade?"


his "Langweilige, philosophische Dinge, über die ich nicht reden will. Keine Sorge, ich mach mir nicht allzu viel Gedanken darum."


show shizu adjust_smug onlayer master
with charachange

ssh "Gut. Zu so einer Zeit wie dieser philosophisch zu werden, wäre das Schlimmste, was du tun kannst."


hi "Sicher. Ich will hier nur noch ein bisschen rumstehen. Es ist entspannend."


show mishashort hips_grin onlayer master
with charachange

mi "Wahaha~! Es war~ eine anstrengende Woche."


hi "Nicht wirklich, nicht für mich."


$ renpy.music.set_volume(0.5, 1.0, channel="music")
$ renpy.music.set_volume(0.1, 1.0, channel="ambient")

window hide
nvl clear
nvl show dissolve

n "\n\n\n\nIch weiß, dass sie viel zu tun gehabt haben müssen. Aber ich denke, ich weiß jetzt, was ich tun will. Und als es mich traf, fühlte ich mich nicht besonders aufgedreht oder war in irgendeiner Weise besorgt."


n "Das Gegenteil ist der Fall. Zum erstem Mal seit langem bin ich zur Ruhe gekommen. Dieses Gefühl will ich noch ein bisschen länger auskosten."


n "\nIch glaube, dass ich hier unterrichten will."


n "\nSobald mir dieser Gedanke kam, sah ich vor meinem inneren Auge eine lange, kurvenreiche Straße – eine ungewisse Straße, die bis hier hin zurückführt."


nvl clear

n "\n\n\n\nIch frage mich, ob ich in der Zukunft jemanden wie mich treffen kann. Erfüllt mir Verbitterung."


n "Ich will mit diesem Jemand reden, da ich nicht mit mir selbst reden kann. Ich will ihm sagen, dass das Leben zu kurz ist – etwas, das mir nicht gesagt werden konnte, sondern nur gezeigt. Ich will es ihm ohne Mitleid sagen."


n "Ich bin mir sicher: Wenn ich bemitleidet worden wäre, dann wäre ich nur etwas mehr gestorben. Wenn ich an diese erste Woche denke, denke ich immer noch daran, wie gut es gelaufen ist. So gut, dass man es nur das Resultat von Güte nennen könnte. Ich will anderen die gleiche Güte zeigen."


n "\nUnd außerdem will ich weiterhin Shizune verfolgen."


$ renpy.music.set_volume(1.0, 1.0, channel="music")
$ renpy.music.set_volume(0.3, 1.0, channel="ambient")

nvl hide dissolve
nvl clear

show mishashort perky_smile onlayer master
with charachange

window show

mi "Was hat der neue Schülerrat gewollt, Shicchan~?"


"Tagträumen ist schwierig, wenn man mit Mishas Stimme zurechtkommen muss."


hi "Ich wusste nicht, dass sie jemanden haben, der Zeichensprache kann."


show shizu behind_smile onlayer master
with charachange

ssh "Haben sie nicht. Ich glaube, es war wahrscheinlich einfach nur ein Abschied, darum weiß ich es zu schätzen – auch wenn ich es ihnen nicht sagen konnte."


show shizu basic_normal onlayer master
with charachange

ssh "Woher wusstet ihr, dass ich hier bin?"


hi "Sollte es ein Geheimnis sein? Na ja, wir haben einfach Yuuko gefragt. Hat sie von dir auch ein Foto gemacht?"


show shizu behind_blank onlayer master
with charachange

ssh "Ja, ohne mich zuerst zu fragen. Aber da es selten ist, dass Yuuko mal etwas Spontanes macht, lasse ich es durchgehen."


play sound sfx_snap
show shizu basic_sparkle onlayer master
with charachange

"Sie schnippt mit ihren Fingern – eher weil sie es mag als wegen eines Einfalls."


show shizu behind_smile onlayer master
with charachange

ssh "Wir sollten ein Foto mit uns Dreien machen."


show shizu adjust_happy onlayer master
with charachange

ssh "Wir haben noch kein Schülerratsfoto gemacht. Jetzt ist die perfekte Gelegenheit."


show shizu basic_normal onlayer master
with charachange

ssh "Aber wenn ich mir dieses Bild in einem Jahr noch mal ansehen muss, will ich nicht, dass wir auf mich zurückblicken."


mi "Hm~? Was soll das heißen, Shicchan?"


show shizu adjust_frown onlayer master
with charachange

ssh "Bilder sollen den Moment einfangen, oder nicht? Ohne Zweifel. Sie sind keine Portraits. Nur herumzustehen wäre zu steif. Es würde nicht einmal einfangen, wie ich mich fühle."


show shizu behind_smile onlayer master
with charachange

ssh "Ich glaube, dass wir uns wiedersehen werden. Darum ist das kein Anlass für ein ernstes Foto. Es sollte eine Art „Bis Später”-Foto sein; nichts Großes. Es sollte etwas… fröhlicheres sein."


hi "Auweia."


show shizu basic_happy onlayer master
with charachange

ssh "So hier. Macht mit."


show shizu adjust_smug onlayer master
with charachange

show shizu behind_smile onlayer master
with charachange

"Shizune posiert wie ein Musketier – so schnell, dass ich mir sicher bin, dass auch sie selbst weiß, wie albern es ist."


show mishashort cross_laugh onlayer master
with charachange

mi "Ahahaha~!"


hi "Müssen wir wirklich so eine… kitschige Pose machen?"


show shizu adjust_happy onlayer master
with charachange

ssh "Mir fällt keine bessere Pose ein. Misha, such Yuuko!"


show mishashort sign_smile onlayer master
with charachange

mi "Ich mag die Pose auch nicht, aber irgendwie hat sie was~."


hi "Das ergibt nicht mal Sinn."


show mishashort invis onlayer master:
    xpos 0.0
with dissolvecharamove

"Sie ist bereits weg, und kehrt dann mit Yuuko im Schlepptau zurück."


show yuuko invis onlayer master:
    center
    xpos -0.2
with None

show bg school_gate onlayer master at left
show shizu behind_smile_close onlayer master:
    xpos 0.83
show mishashort hips_grin onlayer master at center
show yuuko neutral_up onlayer master at left
with dissolvecharamove

"Der Blitz ist aus. Eine rote LED blinkt drei Mal über Yuukos Finger, nachdem sie den Knopf gedrückt hat. Shizune wirft uns beiden einen Blick zu, um sicherzustellen, dass das Timing passt. Synchronisiert die Uhren. Wir springen."


play sound sfx_camera
$ renpy.music.set_volume(0.0, 0.5, channel="ambient")

scene ev shizu_goodend onlayer master
with cameraflashlong

ssh "Ich wette, es ist ausgezeichnet geworden."


ssh "Okay…"


mi "Lasst uns jetzt noch eins mit Yuuko machen~!"


yu "N-Nein, bitte…"


hi "Das ist nicht nötig."


"Von diesem Foto will ich auch eine Kopie."


"Wahrscheinlich sterbe ich früher als ein Durchschnittsmensch. Mein Leben könnte jederzeit unerwartet erlöschen."
"Wenn das so ist, dann habe ich keine Zeit zu verlieren. Ich will so viel wie möglich leben. Genauso will ich andere Leute wegen meiner Schöpfungen und Taten lächeln sehen."


"Stellvertretend durch das Glück anderer zu Leben, hört sich doch gar nicht so schlecht an. Freude durch das Glück eines anderen Menschen zu finden auch nicht."
"Das ist für mich der einfachste Weg, wie ich mein eigenes Leben ausfüllen und es einzigartig machen kann."


"Vielleicht ist dies der Sinn, den Shizune für sich selbst gefunden hat, auch wenn es nur eine Theorie von mir ist. Menschen sind in ihrem Leben oft allein und ohne Orientierung."


"Aber sie können in glücklichen Momenten Zuflucht finden. Sie können das Leben anderer Menschen bereichern – wie ein Halt an einer Zugstrecke. Und dann werden sie zu einer Erinnerung auf deren Lebenspfad."


"Diese individuellen Momente können dazu beitragen, dass man später auf ein erfülltes Leben zurückblicken kann. Jeder Freund, jedes Fest, jedes fröhliche Treffen und jede fröhliche Trennung."


"Eines Tages will ich Shizune fragen können, ob ich Recht habe. Ich will die Zeit, die ich habe, mit ihr verbringen. Und am Ende will ich, dass Shizune für sich selbst lächelt."


$ renpy.music.set_volume(0.3, 1.0, channel="ambient")

scene bg school_gate onlayer master at left

show mishashort perky_smile at twoleft onlayer master
show shizu behind_smile_close at tworight onlayer master


with locationchange

hi "Ich liebe dich."


"Ich halte inne und frage mich, ob sie mich ansehen wird – verwirrt und fragend, warum ich das so plötzlich sage. Sie tut es nicht."


hi "Organisieren die irgendwelche Klassentreffen hier?"


show shizu adjust_happy_close onlayer master
with charachange

ssh "Natürlich tun sie das."


show mishashort sign_smile onlayer master
with charachange

mi "Ein Schülerratsmitglied sollte das wissen~!"


show shizu behind_smile_close onlayer master
with charachange

ssh "Aber wir treffen uns vorher, okay?"


show shizu adjust_happy_close onlayer master
with charachange

ssh "Wir alle drei."


show mishashort hips_grin onlayer master
with charachange

mi "Richtig~!"


hi "Genau."


show shizu basic_happy_close onlayer master
with charachange

ssh "Yuuko! Mach du auch die Pose!"


show shizu adjust_happy_close onlayer master
with charachange

ssh "Danach können wir Tee trinken gehen."


"Shizune lacht, als gäbe es keine Sorgen auf dieser Welt, und Mishas Lachen vereint sich so spielend mit ihrem, als wäre es ihr eigenes. Wir werden uns wiedersehen."


stop ambient fadeout 2.0
stop music fadeout 2.0







label de_S38:

play music music_pearly

scene bg school_scienceroom onlayer master
with locationchange

"Am nächsten Tag ist Misha wieder im Unterricht, auch wenn sie immer noch ziemlich düster dreinschaut. Nicht dass ich erwartet hätte, dass sie sich auf magische Weise wieder besser fühlt. Nach dem, was passiert ist, wäre das unmöglich."


"Dieses Mal ist Shizune diejenige, die nicht da ist. Zuerst finde ich es fast lustig, dass wenn plötzlich die eine da ist, die andere es nicht ist. Doch wenn ich darüber nachdenke, ist daran gar nichts lustig."
"Im Gegenteil: Es ist der Grund, warum ich mich nicht auf meine Aufgaben konzentrieren kann."


"Es könnte sein, dass sie nur krank ist. Oder sie könnte auch einfach den Unterricht schwänzen. Es könnte auch etwas Ernsteres sein, und es reizt mich, Misha danach zu fragen, doch letztendlich tue ich gar nichts."


"Weil ich Angst hatte, dass Misha etwas Unüberlegtes tut, bedaure ich es nicht, gestern eingeschritten zu sein."


play sound sfx_normalbell

"Doch nun glaube ich, dass ich ihr etwas Freiraum geben sollte. Schließlich klingelt die Glocke, und Misha steht mit allem anderen zur Mittagspause auf. Ich beschließe, mein Mittagessen heute in einem leeren Klassenraum zu essen… nur nicht in diesem."


scene bg school_hallway3 onlayer master
with locationchange

"Unglücklicherweise haben eine Menge anderer Schüler die gleiche Idee, darum gibt es nicht allzu viele leere Klassenzimmer. Gerade als ich kurz davor bin, den Plan zu verwerfen, finde ich endlichen einen dunklen Raum am Ende des Flures."


scene bg school_miyagi onlayer master
show lilly back_surprise onlayer master:
    center
    ypos 1.15
with locationchange

"Als ich jedoch die Lichter anschalte, bemerke ich, dass dieser auch nicht leer ist."
"Lillys Kopf dreht sich in meine Richtung. Erst verstehe ich nicht, wie sie mich bemerkt hat, aber dann begreife ich, dass sie wahrscheinlich gehört hat, wie ich den Schalter betätige."


show lilly basic_listen onlayer master
with charachange

li "Hallo."


hi "Hey, Lilly. Ich dachte nicht, dass hier noch jemand anderes wäre."


show lilly basic_weaksmile onlayer master
with charachange

li "Bist du das, Hisao?"


hi "Ja, aber das wusstest du wahrscheinlich schon."


"Ich mache kehrt, was Lilly schnell das Wort ergreifen lässt."


show lilly basic_smile onlayer master
with charachange

li "Du musst doch nicht gleich gehen. Wir können beide im selben Raum Mittagessen. Ich würde sogar lieber mit jemanden zusammen essen."


"Ich war gerade im Begriff, sie zu fragen, woher sie wusste, dass ich hier Mittagessen wollte, doch ich schiebe den Gedanken wieder beiseite. Es ist einfach gesunder Menschenverstand, und ich will nicht so wirken, als wäre ich leicht zu beeindrucken."


show lilly basic_smile_close onlayer master:
    center
    ypos 1.1
with characlose

"Ich setze mich Lilly gegenüber an den Tisch, nachdem ich ihn so gedreht habe, dass er in ihre Richtung zeigt."
"Ich habe gehört, dass unser Verstand eine Menge von dem, was wir sehen, ergänzt – basierend auf dem, was wir einmal gesehen haben oder was wir erwarten."


"Größtenteils wegen der Effizienz, sodass nicht alles, was man sieht, einzeln verarbeitet werden muss."


"Lilly scheint nie ein Geräusch hinterfragen zu müssen. Daher frage ich mich, ob ihr Verstand den Kontext jedes Mal ergänzt. Oder schert sie sich nicht darum und akzeptiert die Dinge einfach so, wie sie sind?"


"Auf ihrem Tisch sind lediglich ein paar Kekse und eine Thermoskanne mit Tee. Sie scheint ein leichtes Mittagessen zu bevorzugen. Ich beiße von meinem Sandwich ab. Ein Teil des Belags fällt am hinteren Ende heraus."


show lilly basic_ara_close onlayer master
with charachange

li "Wir haben lange nicht miteinander geredet, ich bin überrascht, dass du dich noch an meinen Namen erinnerst."


hi "Mmmppffmm?"


show lilly basic_smileclosed_close onlayer master
with charachange

li "Im Schülerrat muss es sehr stressig zugehen."


hi "Es ist jede Woche anders. Manche Wochen sind ziemlich ruhig, in manchen spiele ich mit dem Gedanken, mich krank zu melden."


"Warte kurz, Lilly, ich brauche eine Sekunde, um nach dem Verschlingen meines Sandwiches wieder Luft zu kriegen."


show lilly basic_smile_close onlayer master
with charachange

li "Und wie war es in letzter Zeit?"


hi "Unvorhersehbar."


play sound sfx_snap

show lilly basic_oops_close onlayer master
with vpunch

"Ich schnippe mit meinen Fingern, was sie ihrem Gesichtsausdruck nach zu urteilen gar nicht gut findet."


show lilly basic_reminisce_close onlayer master
with charachange

li "Ich denke, dass du zu viel Zeit mit diesen Beiden verbringst."


hi "Ich schätze, das ist eins von Shizunes Markenzeichen. Ich persönlich mag es."


show lilly basic_displeased_close onlayer master
with charachange

li "Ich ignoriere es."


"Ihr Ton hat sich kein bisschen verändert, doch Lillys Stimmung ist offensichtlich abgerutscht."


hi "Scheint nicht so einfach zu sein. Ich hab versucht herauszufinden, wie sie es so laut hinkriegt, aber ich glaube, ich ruiniere damit meine Gelenke."


show lilly behind_displeased_close onlayer master
with charachange

li "Selbst wenn es so laut wäre, dass es die Fenster zerspringen lässt, würde ich es ignorieren. Ich bin keine trainierte Seerobbe; diesen Luxus habe ich."


hi "Bist du deswegen immer noch wütend?"


"Ich stelle die Frage so vorsichtig und diplomatisch wie möglich, obwohl ich eigentlich nur frage, um meine Neugier zu stillen."


show lilly basic_weaksmile_close onlayer master
with charachange

li "Nein, natürlich nicht – obwohl ich Shizune nicht leiden kann."


show lilly basic_reminisce_close onlayer master
with charachange

li "Wir waren für kurze Zeit zusammen im Schülerrat."


hi "Hab ich gehört."


show lilly basic_sleepy_close onlayer master
with charachange

li "Ich wünschte, du wärst nicht so voreilig beigetreten."


show lilly basic_listen_close onlayer master
with charachange

li "Mir gefällt es nicht, wie Shizune den Schülerrat führt. Wusstest du, dass sie die meisten der alten Mitglieder vergrault hat? Darum glaube ich, dass sie versucht, sich mit Menschen zu umgeben, die ihr nicht widersprechen."


show lilly basic_reminisce_close onlayer master
with charachange

li "Und das tun sie auch nicht. Es ist wie gegenseitige Abhängigkeit."


"Ich bin mir sicher, dass Shizune von Lillys Meinung weiß. Immerhin kann ich mich erinnern, wie sie das einige Male explizit abgestritten hat. Das fand ich schon immer seltsam."


"Man sagt, je spezifischer ein Dementi ist, desto wahrscheinlicher ist es, dass die Anschuldigungen wahr sind."
"Ich denke, dass ich in diesem Fall anderer Meinung bin. Shizune ist die einzige Person, bei der man ihre Meinung als nicht ganz so objektiv bezeichnen könnte."


hi "Hast du ihr das gesagt?"


show lilly basic_displeased_close onlayer master
with charachange

li "Schon sehr oft."


"Lilly hält inne, um den letzten Schluck ihres Tees auszutrinken. Ich liege mit meinem eigenen Mittagessen zurück, daher nutze ich diese Pause aus, um so viel wie möglich zu essen."


show lilly basic_sleepy_close onlayer master
with charachange

li "All ihre Freunde haben mit dem Schülerrat zu tun. Wie Misha."


li "Ich hörte, dass die Dinge zwischen ihr und Misha heikel sind. Hatten sie einen Streit?"


hi "Nicht wirklich."


show lilly basic_surprised_close onlayer master
with charachange

li "Ist das so?"


show lilly basic_reminisce_close onlayer master
with charachange

li "So oder so bringt es nichts, sie zwingen zu wollen, sich zu versöhnen. Immer alles frontal anzugehen, ist Shizunes Art, aber in der echten Welt funktioniert das nicht."
li "Irgendwann ist es nicht mehr Tapferkeit oder gute Absicht, sondern einfach nur noch Sturheit."


hi "Das ist ein bisschen pauschal, meinst du nicht?"


show lilly basic_smileclosed_close onlayer master
with charachange

li "Hm, mag sein."


show lilly basic_weaksmile_close onlayer master
with charachange

li "Was glaubst du, passt am besten zu Tee? Kekse oder Milchbrötchen? Ich mag beides – auf unterschiedliche Art. Ich könnte mich beim besten Willen nicht entscheiden."


show lilly basic_displeased_close onlayer master
with charachange

li "Ich mag keine Menschen, die mich andauernd dazu zwingen wollen, mich für eine Seite zu entscheiden, oder die aus allem einen Wettkampf machen wollen."


li "Als ich dem Schülerrat beigetreten bin, dachte ich, man würde lediglich dazu beitragen, dass alles reibungslos abläuft und anderen Menschen helfen – so wie als Klassensprecher."


show lilly basic_reminisce_close onlayer master
with charachange

li "Stattdessen bestand jeder Tag daraus, Shizune mit Misha als Megafon herumstolzieren zu sehen, wie sie darüber redet, den letzten Schülerrat zu übertrumpfen und immer mehr und größere Events zu organisieren."


hi "Aber dann wollt ihr ja beide im Grunde genommen das Gleiche. All das macht die Dinge erst aufregend."
hi "Ich hab es am Anfang auch nicht gleich begriffen, aber sie tut das alles nicht für ihr Ego. Die Leute mögen Feuerwerk, Soba-Hütten, kandierte Äpfel, und auch Feste im Allgemeinen."


hi "Je mehr der Schülerrat macht, desto mehr Zuständigkeit gibt uns die Schule. Es bedeutet mehr Arbeit, aber auf eine Weise auch mehr Freiheit."


hi "Wenn du es schaffst, so ein großes Festival auf die Beine zu stellen, dann trauen sie dir auch andere Dinge zu und lehnen nicht alles von vorneherein ab."


hi "Wie auch immer, mittlerweile will ich das auch. Es gibt genug sinnlose Aufgaben, aber es auch gibt Momente, die das alles wert sind, wenn alles am Ende Früchte trägt."
hi "Es gibt mir etwas zu tun. Wenn ich tagein tagaus nur zu Schule gehen würde, würde ich wahrscheinlich explodieren."


show lilly basic_weaksmile_close onlayer master
with charachange

li "Ich glaube, Yamaku ist da viel weniger streng als andere Schulen."


"Aber Yamaku ist keine von den „anderen Schulen”."


"Irgendwie ist die Schule fast nicht streng genug… Gott, ich fange an, wie eine gewisse andere Person zu denken."


"Wenn ich ein anderer Mensch wäre, würde ich diese Unbekümmertheit sicher erdrückend finden – auch wenn sie an anderen Schulen einfach der normale Lebensalltag wäre."


"Aber hier wäre diese Ereignislosigkeit noch stärker zu spüren. Es würde sich anders anfühlen – immerhin bin ich kein normaler Mensch."


"Und daran würde ich jedes Mal erinnert werden, wenn ich das Blut in meinen Schläfen pulsieren fühle. Ich würde mich bevormundet und schwach fühlen, und meine Verbitterung würde nur wachsen."


hi "Ja, sicher."


hi "Was ich sagen will, ist, dass ich glaube, endlich zu verstehen, worum es bei allem geht. Du tust Shizune wirklich Unrecht."


show lilly basic_sleepy_close onlayer master
with charachange

li "Das mag sein, doch was ihr Verhalten anderen Leuten gegenüber angeht, hat sie noch einiges an sich zu arbeiten."


"Leider fällt es mir schwer, darauf ein Gegenargument zu finden."


show lilly basic_smile_close onlayer master
with charachange

li "Weißt du, wie spät es ist? Ich gehe gern zehn Minuten bevor die Glocke klingelt zum Klassenzimmer."


hi "Dann bist du genau pünktlich, wenn du jetzt losgehst."


show lilly invis_close onlayer master at center
with dissolvecharamove

stop music fadeout 4.0

"Sie entschuldigt sich und geht. Danach bleibe ich noch einen Moment sitzen und lausche, wie das Klicken ihres Blindenstocks auf dem Boden in dem Gemurmel der anderen sich unterhaltenden Schüler im Flur untergeht."


"Ich bin erschöpft und habe vollkommen vergessen, dass ich heute mit Shizune reden wollte."


scene black onlayer master
with dissolve




label de_S39:

scene bg school_hallway3 onlayer master
with locationchange

"Am nächsten Tag gehe ich nach dem Unterricht direkt zum Schülerratszimmer, um mit Shizune zu reden."


"Auch wenn sie im Unterricht ist – sie in der Tür oder im Flur abzufangen und mit ihr eine Unterhaltung zu haben, könnte ein wenig hinderlich sein."


scene bg school_lobby onlayer master
with locationchange

"Darum ist es besser, sich mit ihr im Schülerratszimmer zu treffen. Beim Weg dorthin lasse ich mir Zeit und besorge mir noch einen Saft vom Verkaufsautomaten."


"Dazu gehe ich in meinem Kopf noch einmal alles durch, was ich ihr sagen will. Es ist nichts allzu Wichtiges – nur ein paar Fragen über die anstehenden Events."


scene bg school_council onlayer master
with locationchange

play music music_rain fadein 8.0

"Als ich dort ankomme ist die Tür unverschlossen."
"Fast würde ich denken, dass der Raum leer ist, wenn ich nicht Shizunes abgelegte Tasche auf ihrem Tisch sehen könnte, und dahinter lugt ihr Kopf hervor. Es sieht aus, als hätte sie sich ein kleine Festung gebaut."


show shizu basic_normal onlayer master at center
with charaenter

"Shizune winkt mir von hinter ihrer Tasche zu, bevor sie sie mit einem Finger aufhebt und aus dem Weg räumt."


"Doch danach fixiert sie wieder eine Checkliste, als würde sie den Sinn des Lebens in sich tragen, und tippt dabei mit ihrem Stift auf den Tisch."


show shizu adjust_frown onlayer master
with charachange

ssh "Was brauchst du?"


his "Ich wollte sehen, ob ich bei irgendetwas behilflich sein kann. Zum Beispiel das ganze Zeug da – was ist das?"


"Ich deute auf die mittelgroßen Ordnerstapel neben ihr, doch sie winkt abweisend mit ihrer Hand."


show shizu behind_blank onlayer master
with charachange

ssh "Ich krieg das schon allein hin."


his "Und was ist mit den Wahlen?"


his "Außerdem – wo ist Misha?"


show shizu behind_sad onlayer master
with charachange

shi "…"


show shizu basic_normal2 onlayer master
with charachange

ssh "Sie gehen voran. Und Misha hab ich gesagt, dass ich mich allein um alles kümmern werde."


his "Wieso?"


"Shizune dreht langsam einen Stift in ihrer Hand und führt ihn durch jeden ihrer Finger wie eine Nadel durch einen Stofffetzen."


show shizu behind_blank onlayer master
with charachange

ssh "Einfach so."


his "Wirklich?"


show shizu adjust_frown onlayer master
with charachange

ssh "Einfach so."


"Zur Verdeutlichung gebärdet sie es noch einmal, um den Eindruck zu ersticken, dass sich dahinter noch mehr verbergen könnte. Doch genau das tut es, da sie sich definitiv nicht normal verhält."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\n\n\n„Warum bestrafst du mich auf einmal mit Schweigen?”, ist das Erste, was mir dazu einfällt, auch wenn das gerade kaum die Zeit für Humor ist. Es beschreibt, wie ich mich fühle. Wir können nicht normal miteinander kommunizieren, darum schätze ich die paar Wege, die uns zur Verfügung stehen. So ausgeschlossen zu werden tut weh."


n "Es ist offensichtlich, dass es heute ziemlich unmöglich sein wird, mit Shizune zu reden – welche Gründe sie auch immer dafür hat. Über ihre Sturheit hinaus scheint sie noch deprimiert zu sein, doch so wie unsere Unterhaltung bereits verläuft, sehe ich mich nicht in der Lage herauszufinden, weswegen sie deprimiert ist."


n "\nIrgendwie macht mich das nur noch neugieriger. Und das bedeutet, dass ich Misha fragen muss. Das Problem ist nur, dass ich nicht wirklich weiß, wo Misha in ihrer Freizeit hingeht."


$ renpy.music.set_volume(1.0, 1.0, channel="music")
stop music fadeout 3.0

nvl hide dissolve
nvl clear

scene bg school_lobby onlayer master
with shorttimeskip

window show

"Nachdem ich viel mehr Leute gefragt habe, ob sie ein Mädchen mit hellen pinken Haaren bemerkt haben, als nötig sein sollte und viel mehr negative Antworten als erwartet bekommen habe, finde ich endlich ein Pärchen, das sie gesehen hat."


scene bg school_cafeteria onlayer master
show mishashort perky_smile onlayer master at center
with locationchange

play music music_moonlight fadein 8.0

"Als ich die Cafeteria erreiche, wo Misha anscheinend die ganze Zeit über gewesen ist, habe ich die Schule bereits zwei mal durchkämmt und bin daher sehr erschöpft."
"Mir fällt auf, dass ich vorher schon an ihr vorbeigelaufen bin und sie nur nicht hinter einer Säule gesehen habe."


hi "Warum findest du mich immer eher als ich dich?"


show mishashort hips_smile onlayer master
with charachange

mi "Du hast nach mir gesucht, Hicchan?"


show mishashort hips_grin onlayer master
with charachange

mi "Hm~… Wer weiß~? Ich glaube, das ist einfach Zufall."


hi "Weißt du, das Prinzip von Zufällen besteht darin, dass sie nicht konsistent sind."


show mishashort cross_laugh onlayer master
with charachange

mi "Hahaha~."


hi "Hast du gerade ein besonders spätes Mittagessen?"


show mishashort sign_smile onlayer master
with charachange

mi "Ich bin in der Mittagspause nicht zum Essen gekommen, also ja~! Aber~ ich esse nicht allzu viel – so kann ich noch Abendessen essen."


show mishashort perky_smile onlayer master
with charachange

mi "Wolltest du mit mir über etwas reden, Hicchan?"


"Ich verschwende keine Zeit."


hi "Jepp. Der Grund, warum ich hier bin… Hast du bemerkt, dass Shizune heute etwas launisch gewesen ist?"


show mishashort perky_confused onlayer master
with charachange

mi "Das gleiche wollte ich dich fragen, Hicchan~."


show mishashort perky_sad onlayer master
with charachange

mi "Na ja~, außer dass sie schon seit ein paar Tagen so gewesen ist."


hi "Verstehe."


show mishashort sign_confused onlayer master
with charachange

mi "Hicchan, glaubst du, es ist wegen etwas, was ich getan hab? Glaubst du, ich hab Shicchan wütend gemacht? So wie letztes Mal?"


hi "Nein. Jedenfalls scheint sie mehr auf mich wütend zu sein."


"Das ist keine Lüge, wirklich nicht. Leider laufen meine Versuche, sie davon zu überzeugen, nicht allzu gut. Auf ihre eigene Art ist Misha ebenfalls ziemlich dickköpfig."


scene bg school_dormhisao_ss onlayer master
with locationskip

"Letztendlich gehe ich einfach zurück auf mein Zimmer. Die letzten paar Tage waren nichts als eine Reihe von frustrierenden Erfahrungen. Sie haben mich ausgelaugt."
"Ich bin so müde, dass ich mich für ein Nickerchen entscheide, und hoffe, dass mir im Schlaf vielleicht etwas einfällt."


stop music fadeout 3.0

window hide

scene black onlayer master
with shuteye

with Pause(1.0)
with shorttimeskip
with Pause(1.0)

scene bg school_dormhisao_ni onlayer master
with openeye

window show

play music music_night fadein 1.0

"Als ich aufwache, fühle ich mich erholter, habe aber immer noch keine Klarheit. Das Einzige, was sich verändert hat, ist, dass es draußen dunkel ist."


"Ich öffne das Fenster ein wenig, und mir fällt auf, dass das Wetter immer noch ziemlich angenehm ist. Nachdem ich meine Pillen für die Nacht eingenommen habe, mache ich einen kleinen Spaziergang zu den Verkaufsautomaten."


scene bg school_lobby_ni onlayer master
with locationskip

"Alles, was ich normalerweise kaufen würde, ist ausverkauft. Darum drücke ich mit meiner Hand wahllos auf die Knöpfe, bis etwas herauskommt."


scene bg school_courtyard_ni onlayer master
with locationchange

"Die Lichter im Hauptgebäude sind aus – auch die im Schülerratszimmer. Nur eine beiläufige Beobachtung."


play sound sfx_rustling

"Während ich selbst in Gedanken versunken bin, höre ich hinter mir ein Rascheln. So eine Szene kenne ich schon aus Filmen, daher ist dieses Geräusch äußerst unheilvoll – besonders bei Nacht."


show kenji happy_ni onlayer master at center
with charaenter

"Glücklicherweise ist es nur Kenji, der ungewohnt gut gelaunt aus den Büschen schlendert."


ke "Hey."


hi "Was zur Hölle? Lauerst du öfters Leuten bei Nacht auf und sagst beiläufig „hey”?"


show kenji neutral_ni onlayer master
with charachange

ke "Nein, das wäre sonderbar. Ich wusste, dass du es warst. Ich kann im Dunkeln extrem gut sehen. Vielleicht weil ich ein Übermensch bin."


hi "Was machst du dann hier?"


show kenji tsun_ni onlayer master
with charachange

ke "Ich könnte dich das Gleiche fragen. Was machst DU hier?"


"Ich überlege, ob ich ihm einfach die Wahrheit sage, doch entscheide mich schnell dagegen. Das zu erklären, würde zu lange dauern."


hi "Den Mond anheulen."


show kenji neutral_ni onlayer master
with charachange

ke "Das mach ich manchmal auch. Allerdings ist der Mond heute nicht zu sehen."


"Ich höre ihn kaum, da ich noch etwas gereizt bin, weil er meinen nächtlichen Spaziergang unterbrochen hat."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\nIch habe Shizune nach Strich und Faden belogen, als ich sagte, dass alles in Ordnung sei. Oder um genauer zu sein, als ich es gebärdete. Und zur exakt selben Zeit habe ich mit Misha eine komplett andere Unterhaltung geführt."


n "Diese Unterhaltung könnte Shizune wütend machen – verständlicherweise. Aber es ist unmöglich, dass sie davon erfahren konnte. Sogar Mishas Hände, die normalerweise all ihre Gedanken gebärden, waren komplett still. Auch wenn sie es nicht gewesen wären, stand ich direkt vor ihr, sodass Shizune sie nicht sehen konnte."


n "Der einzige Weg, mit dem Shizune unserer Unterhaltung hätte zuhören können, wäre Lippenlesen. So ziemlich das Erste, nach dem ich zu Anfang meines Zeichensprachekurses gefragt habe, war Lippenlesen – rein aus Neugier. Es ist weder einfach noch perfekt… darum habe ich die Möglichkeit bis jetzt nie in Betracht gezogen."


n "\nEs würde Sinn ergeben, und der Raum für Missverständnisse beim Lippenlesen würde es nicht besser machen."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show

ke "… also habe ich begriffen, dass ich den Mantel der Dunkelheit nutzen kann, um Milch zu kaufen."
ke "Normalerweise gehe ich nur raus, wenn es regnet oder ich mich in einem Meer aus Fahrradfahrern oder Touristen verbergen kann. So wie jetzt geht das viel einfacher… Allerdings gebe ich nun zu viel Geld für Milch aus."


show kenji happy_ni onlayer master
with charachange

ke "Du wirkst irgendwie trübselig oder neben der Spur oder so. Denk nicht zu viel nach, ein Mann muss Taten sprechen lassen! Du kannst den ganzen Tag über Zeugs nachdenken, aber die Situation zu ändern, indem man etwas tut, ist der beste Weg."


ke "Ich tue die ganze Zeit Dinge, ohne darüber nachzudenken. Darum nannten sie mich in der Mittelschule „verursacht viele Probleme”. Ich dachte, das wäre cool. Klingt wie ein Indianer-Name."


hi "Ich hab da nicht wirklich Lust zu."


show kenji neutral_ni onlayer master
with charachange

ke "Hast du 'nen schlechten Tag?"


hi "Ja, ich weiß nicht. Ich bin gerade irgendwie abgelenkt."


stop music fadeout 7.0

hide kenji onlayer master
with dissolve

"So abgelenkt, dass ich bis zu seinem Verschwinden nicht begreife, dass sein Rat eigentlich ein sehr guter war. Ich denke, Shizune hätte mir denselben Vorschlag gemacht. Doch inzwischen ist es zu spät, um ihm freundlich zu danken."


"Und dazu habe ich noch in dem unhöflichsten Ton überhaupt geantwortet. Ich komme mir einfach wie ein Esel vor."


"Zurückblickend habe ich diese letzten paar Tage jeden meiner Schritte bereut."
"Das Schlimmste daran ist, dass ich mir nicht die Zeit genommen habe, mich über sie aufzuregen und dabei aus ihnen zu lernen. Das führt lediglich – führte lediglich – zu mehr Bedauern."


scene black onlayer master
with dissolve



label de_S40:

play music music_dreamy fadein 2.0

scene bg school_dormhisao onlayer master
with locationchange

play sound sfx_doorknock2

"Während ich mich am nächsten Morgen anziehe, höre ich ein Klopfen an der Tür. Zügig ziehe ich mir den Rest meiner Sachen an und öffne sie, ohne wirklich darüber nachzudenken, wer dahinter stehen könnte."


scene bg school_dormhallway onlayer master
show shizu basic_normal onlayer master
with locationchange

"Es ist Shizune."


show shizu behind_blank onlayer master
with charachange

ssh "Misha hat mir gesagt, dass du nach mir gesucht hast."


"Es verletzt mich etwas, dass ich nicht einmal ein „guten Morgen” bekomme, aber das ist keine allzu große Sache."


his "Habe ich."


show shizu basic_normal2 onlayer master
with charachange

ssh "Aber du hast mich gestern doch gefunden."


"Shizunes Finger fahren an dem Riss in der Wand entlang. Es scheint, als versucht sie ihr Bestes, um distanziert zu wirken."


show shizu adjust_smug onlayer master
with charachange

ssh "Nun, ich hab es dir nicht einfach gemacht, nicht wahr?"


his "Schon okay."


show shizu behind_blank onlayer master
with charachange

ssh "Darum bin ich hier. Heute können wir reden. Auch wenn… ich irgendwie woanders hingehen will."


his "Was ist mit Unterricht?"


show shizu adjust_smug onlayer master
with charachange

ssh "Keine Sorge, keine Sorge."


show shizu basic_normal2 onlayer master
with charachange

ssh "Wie wäre es, wenn wir einen Spaziergang um die Schule machen? Alles außer dem Hauptgebäude wird menschenleer sein. Die Glocke zur ersten Stunde sollte genau jetzt klingeln."


"Ich werfe einen kurzen Blick auf meine Uhr und sehe, dass sie Recht hat."


his "Okay."


stop music fadeout 6.0

show shizu basic_angry onlayer master
with charachange

shi "…"


his "Stimmt etwas nicht?"


show shizu behind_blank onlayer master
with charachange

ssh "Warum denkst du, dass etwas nicht stimmt?"


his "Weil du offensichtlich verärgert bist. Ich sehe es einfach."


his "Darüber wollte ich mit dir reden."


show shizu basic_normal2 onlayer master
with charachange

"Shizune knackt kurz mit ihren Knöcheln, während ich gebärde."


show shizu behind_blank onlayer master
with charachange

ssh "Anscheinend bin ich leichter zu durchschauen, als ich gedacht hatte. Ich hab so gut wie möglich versucht, es zu verbergen. Kannst du erraten, was ich jetzt gerade denke?"


hide shizu onlayer master
with charaexit

"Ich antworte nicht, und Shizune geht langsam Richtung Tür – wahrscheinlich um mir zu sagen, dass ich ihr folgen soll. Ihre Hände sind hinter ihrem Rücken gefaltet, und sie streckt sich nach hinten, als würde sie jeden Augenblick rückwärts umkippen."


scene bg school_courtyard onlayer master
with locationchange

"Draußen sehe ich, dass Shizune Recht hat. Die Schule ist vollkommen verlassen. Auch wenn es nicht das erste Mal ist, dass ich die Schule so sehe, ist es irgendwie unheimlich."


scene bg school_backexit onlayer master at right
with locationchange

"Shizune tut fast so, als wäre ich nicht da. Sie durchstöbert einen Verkaufsautomaten und nimmt einen umständlichen, gewundenen Weg, bis wir hinter dem Hauptgebäude ankommen."


show shizu invis_close onlayer master at tworight
with None

show shizu basic_normal_close onlayer master:
    ypos 1.05
with dissolvecharamove

"Schließlich lehnt sie sich gegen eine Wand und sieht mich an, aber es ist, als hätte ich vergessen, wie man eine Unterhaltung beginnt."


play music music_sadness fadein 8.0

show shizu behind_blank_close onlayer master
with charachange

ssh "Es gibt ein Sprichwort: „Man weißt nicht, wie sehr man es vermasselt hat, bis man es vermasselt.”"


his "Von wem ist das?"


show shizu basic_normal2_close onlayer master
with charachange

ssh "Ich denke, von mir."


show shizu basic_angry_close onlayer master
with charachange

"Nachdem sie ihren Gedankengang noch einmal überdenkt, winkt sie frustriert ab."


show shizu behind_blank_close onlayer master
with charachange

ssh "Okay, ich formuliere es anders."


show shizu basic_normal_close onlayer master
with charachange

ssh "Als ich jünger war, mussten wir in der Schule Poster für den Umwelttag machen. Es gab ein anderes Mädchen in meiner Klasse, das von allen für die beste Künstlerin gehalten wurde."


show shizu behind_blank_close onlayer master
with charachange

ssh "Es war nicht so, dass sie besser als alle anderen Zeichnen konnte. Sie konnte nur so unglaublich viel in ein einzelnes Bild stecken."


show shizu adjust_frown_close onlayer master
with charachange

ssh "Ich wollte besser sein als sie, darum habe ich unzählige Poster gemacht, bis ich letztendlich mein Bestes hinbekam. Ich musste die Beste sein und das beste Poster haben. Am Ende mochten alle mein Poster am meisten – sogar der Lehrer."


show shizu basic_normal_close onlayer master
with charachange

ssh "Eine Woche später war es bedeutungslos. Ich habe es in den Müll geworfen."


show shizu behind_blank_close onlayer master
with charachange

ssh "Ich glaube, ich habe dir so etwas schon mal erzählt."


his "Ja."


show shizu basic_angry_close onlayer master
with charachange

ssh "Wenn ich mich fühle, als hätte ich etwas abgeschlossen, wünschte ich, ich könnte einfach reinen Tisch machen. Ob ich es geschafft habe oder nicht. Ich habe Misha eine Menge durchmachen lassen, und dich habe ich auch mit reingezogen."


show shizu adjust_frown_close onlayer master
with charachange

ssh "Und jeder Moment, an dem ich diese dämliche Situation hätte lösen oder sogar ganz verhindern können, verfolgt mich."


show shizu behind_sad_close onlayer master
with charachange

ssh "Das ist das schlimmste Gefühl. Besonders wenn es mir so vorkommt, als hätte ich nichts richtig und alles falsch gemacht. So wie vor Kurzem. Es ist die schlimmste aller Niederlagen. Ich fühle mich auf ganzer Linie wie eine Versagerin."


show shizu basic_normal2_close onlayer master
with charachange

ssh "Ich wünschte, ich könnte alles ungeschehen machen, was ich bisher getan habe, und einfach allein sein. Ich habe zwei Jahre lang mit Mishas Gefühlen gespielt und dich ein Jahr lang aus egoistischen Gründen an der Nase herumgeführt."


his "Es ist in Ordnung."


show shizu adjust_frown_close onlayer master
with charachange

ssh "Nein, ist es nicht. Du verstehst nicht. Ich habe gerade darüber nachgedacht. All meine Taten fühlen sich so an, als müsste ich jemand anderen besiegen. Oder sogar alle anderen."
ssh "Wenn das so ist, was habe ich dann für eine Beziehung zu anderen Menschen? Sie fühlen sich fast genauso an."


"Ich kann sehen, worauf das hinausläuft."


show shizu behind_sad_close onlayer master
with charachange

ssh "Worauf ich hinaus will, ist, dass ich durch meinen Egoismus sehr viele Leute verletzt habe. Und nun will ich für eine Weile ein wenig Distanz zu anderen Leuten haben."


his "Sogar zu mir?"


"Sie hält inne."


show shizu basic_normal_close onlayer master
with charachange

ssh "Ja."


"Nach einer noch längeren Pause ergreife ich noch einmal das Wort."


his "Verstehe."


his "Das ist das Egoistischste, was du tun könntest."


his "Du triffst wieder einmal ganz allein eine Entscheidung."


show shizu basic_normal2_close onlayer master
with charachange

shi "…"


"Für eine Minute sieht es so aus, als würde sie über die bestmögliche Antwort nachdenken, aber am Ende nickt sie einfach. Ich denke, das ist auch die bestmögliche Antwort."


"Es passt zu gut zu ihr, sogar jetzt noch umständlich zu antworten. Aber endlich ohne Ausreden."


"All meine Emotionen brodeln in mir. Ich sehe einen mit brodelndem Wasser gefüllten Kessel vor mir. Er ist so nah, dass ich ihn berühren kann, und ich spüre die Hitze, die von ihm ausstrahlt."
"Ich freue mich über diese Ablenkung, da ich weiß, dass kein Einspruch und keine Verhandlung möglich sind."


show shizu adjust_frown_close onlayer master
with charachange

ssh "Du hast mir gesagt, dass alles in Ordnung ist, aber das stimmte nicht, nicht wahr?"


show shizu behind_sad_close onlayer master
with charachange

ssh "Wenn es so war, dann kann ich dir nie wieder glauben."


hi "In Ordnung."


show bg school_backexit onlayer master at center
show shizu invis_close onlayer master:
    xpos 0.85
with dissolvecharamove

"Ich kümmere mich nicht einmal darum, es zu gebärden, und stehe auf. Meine Hände sind in meinen Hosentaschen und spielen mit etwas Kleingeld. Ich spüre die kalten Morgenluft auf meinem Gesicht."


scene ev shizu_badend onlayer master:
    xalign 0.0 yalign 0.5 zoom 1.1 subpixel True
    acdc_warp 10.0 zoom 1.0
with locationchange

"Als ich mich zu ihr umdrehe, sieht sie sehr einsam aus. Es erinnert mich an mich selbst. Diesen Gesichtsausdruck hatte früher ich. Vielleicht trage ich ihn gerade selbst."
"Es kommt mir vor, als würde das Bild eines so einsamen Mädchens für immer in meinem Gedächtnis bleiben."


"Jeder Moment, in dem ich das Problem hätte lösen oder sogar ganz verhindern können, verfolgt mich. Ein freudloses Lächeln ziert mein Gesicht."


stop music fadeout 4.0

window hide

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
