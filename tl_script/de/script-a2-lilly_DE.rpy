label de_L1:

window hide None

scene black onlayer master
with dissolve

play sound sfx_alarmclock

with Pause(2.0)

scene bg school_dormhisao onlayer master
with openeye

window show

"Das nervige Dröhnen meines Weckers reißt mich aus dem Schlaf. Seine leuchtenden, roten Digitalziffern beleuchten mein Gesicht."


play music music_dreamy fadein 2.0

"Es ist derselbe Wecker, den ich zu Hause hatte – eines der wenigen übrigen Überbleibsel aus der Zeit, bevor ich hierher gekommen bin. Ich hatte gehofft, dass er helfen würde, den Übergang zu meinem neuen Leben zu erleichtern."


"Diese Hoffnung war wohl vergebens."


"Noch halb schlafend schleppe ich mich aus dem Bett, reibe mir den Schlaf aus den Augen und greife nach den Medikamentenfläschchen, die auf meinem Schreibtisch verteilt stehen. Ich schlucke einige Tabletten ohne Wasser hinunter."


"Dieser Vorgang fängt langsam an, automatisch zu verlaufen. Wenn man bedenkt, wie wichtig die Tabletten sind, sollte ich dafür dankbar sein."


$ renpy.music.set_volume(0.5, 2.0, channel="music")

scene bg school_dormbathroom onlayer master
with locationskip

"Deutlich munterer als vorher gehe ich ins Badezimmer."


play ambient sfx_shower fadein 8.0

show steam onlayer master
with charaenter

"Während das Duschwasser aufheizt und meine neue tägliche Routine beginnt, lasse ich meinen Gedanken freien Lauf."


"Erinnerungen an die leuchtenden Farben des Feuerwerks und die zwei Mitschülerinnen, in deren Begleitung ich es gesehen habe, schwirren durch meinem Kopf."
"Es fühlt sich eigenartig an, dass Menschen, die ich kaum kenne, einen so starken Eindruck auf mich gemacht haben."


"Andererseits sind die Umstände alles andere als gewöhnlich. Wenigstens habe ich jetzt jemanden, mit dem ich reden kann – außer meinem Zimmernachbarn."


stop ambient fadeout 2.0

hide steam onlayer master
with charaexit

"Da die Zeit schwindet, die mir bis zum Anfang des Schultages noch bleibt, bereite ich mich auf den Unterricht vor."


$ renpy.music.set_volume(1.0, 3.0, channel="music")

scene bg school_scienceroom onlayer master
with shorttimeskip

"Ich betrete das Klassenzimmer und merke, dass ich immer noch früh dran bin. Fünf oder sechs Schüler sind schon da. Die meisten davon sehen so aus, als würden sie lieber noch im Bett liegen."


"Zu Zeiten wie diesen bin ich dankbar, dass ich ein Morgenmensch bin. Nichtsdestotrotz gibt es zwei Schülerinnen, die so lebhaft wie immer sind."


hi "Hallo Shizune, hallo Misha."


show shizu behind_blank onlayer master at tworight
show misha perky_smile onlayer master at twoleft
with charaenter

"Plötzlich fällt mir auf, dass Shizune mit meinem Gruß nichts anfangen kann, also winke ich noch zusätzlich. Mein Fauxpas scheint sie nicht besonders zu stören."


"Oder überhaupt zu interessieren."


show shizu basic_normal onlayer master
with charachange

shi "…"


show misha hips_grin onlayer master
with charachange

mi "Hallo Hicchan~! Geht es dir gut?"


"Ich kann nur annehmen, dass der Gruß von Shizune kommt. Manchmal ist es schwer zu erkennen, ob Misha für sich selbst oder für Shizune spricht."


hi "Besser als den Meisten hier, denke ich. Ihr beide scheint ja schon putzmunter zu sein."


show misha sign_smile onlayer master
with charachange

show misha perky_smile onlayer master
show shizu basic_frown onlayer master
with charachange

"Misha übersetzt noch, während ich spreche. Wenn ich Shizunes scharfe, schnelle Armbewegungen richtig deute, ist ihre Antwort recht knapp."


"Da diese beiden aus den Vorbereitungen für das Schulfest so eine große Sache gemacht haben, hätte ich meine Worte wahrscheinlich sorgfältiger wählen sollen."


show shizu behind_frown onlayer master
with charachange

shi "…!"


show misha hips_grin onlayer master
with charachange

mi "Weil du ein neuer Schüler bist, waren wir mit dir bisher ein bisschen nachsichtig. Bitte erwarte nicht, dass du dich auch in Zukunft um Arbeit drücken kannst."


"Misha sieht so aus, als wolle sie ihren eigenen Kommentar hinzufügen, aber da Shizune direkt fortfährt, übersetzt sie weiter."


show shizu basic_frown onlayer master
show misha sign_smile onlayer master
with charachange

mi "Obwohl dein Betrag zum Stand der Klasse 3-2 während des Schulfests zu schätzen ist—"


"Wow. Entweder hat sich das schnell herumgesprochen oder diese beiden wissen wirklich alles, was an der Schule vor sich geht."


show misha hips_frown onlayer master
with charachange

mi "—hätten wir es lieber, wenn du deine Bemühungen auf die wichtigen Aufgaben konzentrieren würdest. Und zwar die deiner eigenen Klasse."


"Obwohl ich es ungern zugebe, haben sie nicht ganz Unrecht. Doch ehe ich antworten kann, fügt Shizune etwas hinzu, was Misha zum Lächeln bringt."


show shizu behind_blank onlayer master
with charachange

shi "…"


show misha perky_smile onlayer master
with charachange

mi "Hattest du Spaß beim Schulfest~?"


"Die Strafpredigt ist anscheinend vorbei."


hi "Ja, es war schön. Habt ihr Zwei euch auch amüsiert?"


show shizu behind_smile onlayer master
show misha hips_grin onlayer master
with charachange

"Shizune nickt kurz, während Misha grinst und ihren Kopf hoch und runter wippen lässt. Der krasse Gegensatz ist lustig."


"Aus meinem Augenwinkel sehe ich, wie nach und nach mehr Schüler im Klassenzimmer eintreffen. Ein flüchtiger Blick auf meine Uhr bestätigt, dass sie ein paar Minuten zu spät sind."


show hanako emb_downtimid onlayer master at offscreenright
with None

show misha hips_grin onlayer master at left
show shizu behind_smile onlayer master at Transform(xpos=0.48)
show hanako emb_downsmile onlayer master at Transform(xpos=1.0, xanchor=0.7)
show bg school_scienceroom onlayer master at bgleft
with charamove

"Ich schaue hinüber zu Hanakos Platz und stelle fest, dass sie schon hier ist und zufrieden ein Buch liest. Ich frage mich, wie lange sie schon da sitzt, ohne dass ich sie bemerkt habe."


show misha hips_grin onlayer master:
    ease 1.0 xpos 0.2
show shizu behind_smile onlayer master:
    ease 1.0 tworight
show hanako emb_downsmile onlayer master:
    ease 1.0 offscreenright
show bg school_scienceroom onlayer master:
    ease 1.0 center
with None

hide misha onlayer master
hide shizu onlayer master
hide hanako onlayer master
with Dissolve(1.0)

"Schwere Schritte im Gang kündigen Mutous Ankunft an. Wir beenden unser Gespräch, und ich setze mich auf meinen Platz neben Misha."


"Die Schiebetür öffnet sich, und er betritt schwerfällig das Zimmer. Seine Körperhaltung ist schlechter als üblich, und er kann seine Augen kaum offenhalten. Mein Scherz mit Lilly und Hanako über die Schulbediensteten war wohl fehl am Platz."



play ambient sfx_paperruffling

"Als er seinen Tisch erreicht, öffnen wir alle unsere Bücher, und die erste Unterrichtsstunde der neuen Woche beginnt."


stop music fadeout 3.0
stop ambient fadeout 0.5

with shorttimeskip

play sound sfx_normalbell

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0

"Die Mittagsglocke läutet. Ich reibe mir die Augen und freue mich über die kurze Arbeitspause."


show lilly basic_smileclosed onlayer master at offscreenleft
with None

show bg school_scienceroom onlayer master at bgright
show lilly cane_smileclosed onlayer master at Transform(xanchor=0.2)
with charamove

"Als ich zur Tür schaue, sehe ich dort Lilly mit ihrem Stock in der Hand stehen und geduldig auf Hanako warten. Ihre Anwesenheit überrascht mich überhaupt nicht."


"Da sie gestern nichts dagegen hatten, dass ich mich ihnen anschließe, entscheide ich mich, meine Mittagszeit mit ihnen zu verbringen, anstatt allein zu essen."


show hanako emb_smile onlayer master at Alphain(0.5), Slide(0.5,0.5,0.4,0.5,0.5)
with Pause(0.5)

hide hanako onlayer master
hide lilly onlayer master
with charaexit

"Hanako bewegt sich überraschend schnell, um ihre Freundin zu treffen, und die beiden sind schon im Gang, bevor ich sie einholen kann."


stop ambient fadeout 1.0

scene bg school_hallway3 onlayer master
show lilly back_listen onlayer master at twoleft
show lillyprop back_cane onlayer master at twoleft
show hanako emb_downsmile onlayer master at tworight
with locationchange

show hanako def_shock onlayer master
with vpunch

"Lilly dreht leicht ihren Kopf, als sie das Geräusch von Schritten hinter sich wahrnimmt. Als Hanako dies bemerkt und ihrem Beispiel folgt, zuckt sie vor Schreck zusammen."


show hanako defarms_strain onlayer master
with charachange

ha "Hi… Hisao?"


$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play music music_normal fadein 2.0

show hanako emb_blushtimid onlayer master
with charachange

ha "Ich meine… äh… hallo, Hisao…"


hi "Hallo. Tut mir leid, wenn ich dich erschreckt habe."


show lilly cane_smile onlayer master
hide lillyprop onlayer master
with charachange

"Mit Orientierungshilfe von Hanako wendet sich Lilly mir zu, um mich zu begrüßen."


show lilly cane_smileclosed onlayer master
with charachange

li "Guten Tag, Hisao. Schließt du dich uns an?"


hi "Wenn es euch keine Umstände macht. Es gibt nicht wirklich viel anderes zu tun."


show lilly cane_smile onlayer master
with charachange

"Lilly nickt leicht, als ob sie die Bedenken, dass meine Anwesenheit Umstände machen könnte, zerstreuen wollte."


scene bg school_staircase2 onlayer master
with locationchange

with Pause(0.3)

scene bg school_hallway2 onlayer master
with locationchange

"Wir gehen die Treppen ein Stockwerk hinab und dann den Gang hinunter zu dem üblichen Zimmer. Unser Lauftempo ist ein bisschen schneller als gewöhnlich, da Lilly sich auf Hanako statt auf ihren Stock und die Geländer verlässt."


scene bg school_miyagi onlayer master
with locationchange

"Wie erwartet ist das Zimmer verlassen. Sonnenlicht von draußen erfüllt den Raum, und die Geräusche der anderen Klubs sind kaum zu vernehmen."


"Ich sehe mich um und bemerke ein paar leere Staffeleien, die an eine Wand gelehnt sind. Soweit ich mich erinnern kann, waren sie vorher nicht da. Der Kunstclub benutzt dieses Zimmer wohl als zusätzliches Lager."


show hanako emb_smile onlayer master
with charaenter

ha "Soll ich das Schachspiel herausholen?"


"Hanakos Stimme scheint deutlich weniger angespannt zu sein, wenn sie direkt mit Lilly spricht."


show hanako emb_smile onlayer master at tworight
show bg school_miyagi onlayer master at bgright
with charamove

show lilly cane_weaksmile onlayer master at twoleft
with charaenter

li "Ja. Ich mache Tee, während du die Figuren sortierst."


hi "Äh, ich kann das für dich tun, wenn du willst."


show lilly cane_surprised onlayer master
with charachange

with Pause(0.3)

show lilly cane_planned onlayer master
with charachange

"Sie denkt über mein Angebot kurz nach und stimmt dann mit einem Lächeln zu. Ihr Gesicht ist erstaunlich einfach zu lesen."


show lilly cane_satisfied onlayer master
with charachange

li "Also gut. Danke."


show lilly cane_satisfied onlayer master:
    ease 0.5 ypos 1.3
    "lilly basic_cheerful" with Dissolve(0.5, alpha=True)
    ease 0.5 ypos 1.0
with Pause(1.0)

hide lilly onlayer master
hide hanako onlayer master
with charaexit

"Sie steckt ihren zusammengeschobenen Stock zwischen die Griffe ihrer Tasche und lehnt diese gegen ein Tischbein, bevor sie sich gegenüber von Hanako setzt."


"Während ich den Tee zubereite, höre ich, wie die kleinen, hölzernen Figuren auf dem Brett aufgestellt werden. Ich frage mich, wie gut Lilly in Anbetracht ihrer Situation Schach spielen kann."


"Als ich die dampfenden Teetassen auf den Tisch stelle, haben Lilly und Hanako schon ihre ersten Züge gemacht. Sie knabbern an Sandwiches und Reisbällchen aus ihren jeweiligen Taschen."


$ renpy.music.set_volume(0.5, 2.0, channel="music")

show chessboard onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Das Schachbrett, das sie benutzen, hat in der Mitte jedes Feldes Vertiefungen, passende Stifte auf den Unterseiten der Figuren, und alle schwarzen Felder sind leicht erhöht."


"Die Geschwindigkeit, mit der Lillys Finger über das Brett gleiten und die Positionen der einzelnen Figuren feststellen, lässt mich über den Einfallsreichtum des Designs staunen. Es muss speziell für blinde Spieler gefertigt worden sein."


$ renpy.music.set_volume(1.0, 5.0, channel="music")

show chessboard onlayer master:
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide chessboard onlayer master
with None

hi "Bitte sehr."


scene bg tearoom_everyone_noon onlayer master
show tearoom_hanae happy onlayer master
show tearoom_lillye smileclosed onlayer master
show tearoom_hisaoe hsmile onlayer master
show tearoom_chess onlayer master
with locationskip

"Hanako nickt leicht, als ich eine Tasse neben ihre Seite des Bretts stelle. Lillys Hand wandert etwas seitwärts, also stelle ich vorsichtig die Tasse so hin, dass sie ihre Finger berührt. Sie scheint meine Geste zu schätzen zu wissen."


show tearoom_hisaoe outside onlayer master
with charachange

"Schließlich setze ich mich hin und nippe still an meinem Tee, während die beiden spielen. Der Unterschied zwischen den Spielweisen der beiden ist interessant."


show tearoom_hanae open onlayer master
with charachange

"Hanako betrachtet das Brett ausgiebig, ihr Gesicht eine Maske der Konzentration. Lilly hingegen hält ihren Kopf gerade und bewahrt ihre gelassene Neutralität."


"Mit sanfter Stimme spricht Lilly uns beide an, während sie weiterspielt."


show tearoom_lillye smile onlayer master
with charachange

li "Wie war der Unterricht, jetzt wo das Schulfest vorbei ist?"


show tearoom_hanae shy onlayer master
show tearoom_hisaoe hthink onlayer master
with charachange

"Ich schaue zu Hanako hinüber, um zu sehen, ob sie zuerst antworten wird, aber ich sehe, dass sie mich genauso anschaut."


show tearoom_hisaoe sigh onlayer master
with charachange

hi "Nicht gerade… gut. Die Hälfte der Klasse war kurz vor dem Einschlafen – sogar der Lehrer. Und dann hatten wir obendrein noch einen Test."


show tearoom_hanae happy onlayer master
with charachange

"Hanako stimmt leise zu."


show tearoom_lillye ara onlayer master
with charachange

li "Ich kann mir vorstellen, dass das für dich als neuer Schüler ein bisschen schwierig gewesen sein könnte."


show tearoom_hisaoe lsmile onlayer master
with charachange

hi "Na ja, ich denke, es lief ganz gut. Ich war zwar etwas schockiert, so früh einen Test schreiben zu müssen, aber Naturwissenschaften sind vermutlich mein bestes Fach."


show tearoom_hisaoe hsmile onlayer master
with charachange

hi "Und wie lief es bei dir, Hanako?"


show tearoom_hanae open onlayer master
with charachange

ha "Bei mir? Äh… gut… denke ich…"


"So viel ist sicher: Hanako ist viel zu aufrichtig, um überzeugend zu lügen."


show tearoom_lillye thinking onlayer master
with charachange

"Lillys Lächeln friert kurz ein. Ihrer Reaktion entnehme ich, dass Hanako wohl nicht so gut in der Schule ist, dass sie ohne Vorbereitung klarkommt."


show tearoom_hisaoe lsmile onlayer master
with charachange

hi "Wie war's in deiner Klasse, Lilly?"


show tearoom_lillye giggle onlayer master
with charachange

li "Überraschend gut, um ehrlich zu sein. Es hat nur ein Schüler gefehlt – das war besser, als unsere Lehrerin erwartet hat."


show tearoom_hanae shy onlayer master
show tearoom_lillye smileclosed onlayer master
with charachange

"Da dieses Thema ziemlich erschöpft ist, konzentrieren sich die beiden wieder auf ihr Schachspiel."


show tearoom_hisaoe relief onlayer master
with charachange

"Ich kann nicht sagen, dass ich Schach je für einen Zuschauersport gehalten habe, aber dieses Spiel ist so einzigartig, dass ich es fasziniert verfolge."


show tearoom_hisaoe outside onlayer master
show tearoom_hanae sad onlayer master
with shorttimeskip

"Mit der Zeit wird klar, dass beide gute Spielerinnen sind. Lilly hat zwei Bauern mehr geschlagen als Hanako und hat so – wenn auch knapp – die Oberhand."


show tearoom_hanae open onlayer master
show tearoom_hisaoe hunsure onlayer master
with charachange

"… bis Hanako einen eigenartigen Zug mit ihrer Dame macht. Lilly macht sich ihren Fehler zunutze und schlägt die Figur mit ihrem Springer."


show tearoom_hanae shy onlayer master
with charachange

"Ohne zu zögern benutzt Hanako einen Bauern, um Lillys Turm auf der gegenüberliegenden Seite des Bretts zu schlagen und wandelt ihn anschließend in eine Dame um."


show tearoom_lillye thinking onlayer master
show tearoom_hisaoe lunsure onlayer master
with charachange

"Lilly zögert, als ihre Finger sich über die Figuren bewegen und sie erkennt, dass sie in Hanakos Falle getappt ist. Es ist ein wenig seltsam, zu sehen, wie das Brett nach jedem Zug abgetastet wird, auch wenn es notwendig ist."


"Dass Hanako darauf nicht reagiert, zeigt, dass sie sich daran gewöhnt hat. Anscheinend haben sie und Lilly schon einige Partien Schach miteinander gespielt."


ha "Schach."


show tearoom_hisaoe hsmile onlayer master
with charachange

hi "Gar nicht so übel. Gut gemacht, Hanako."


show tearoom_hanae happy onlayer master
with charachange

"Mein Kompliment überrascht Hanako und lässt sie erröten."


ha "D-Danke. Ich dachte nicht… dass es funktionieren würde."


show tearoom_hisaoe lsmile onlayer master
with charachange

"Ich wende mich wieder Lilly zu. Sie hat hat gerade die Positionen ihrer übrigen Figuren ertastet, um zu versuchen, ihren König aus der Zwickmühle zu befreien."


li "Ich glaube, das ist Schachmatt…"


show tearoom_hisaoe loops onlayer master
with charachange

hi "Hmm?"


show tearoom_hisaoe relief onlayer master
with charachange

"Ich werfe einen zweiten Blick auf das Brett, um dies zu bestätigen."


"Ihr König kann tatsächlich nirgends entkommen, ohne von einer anderen Figur bedroht zu sein. Meine frühere Frage, welche der beiden die bessere Spielerin ist, ist damit wohl beantwortet."


show tearoom_hisaoe sigh onlayer master
with charachange

hi "Stimmt."


show tearoom_lillye weaksmile onlayer master
with charachange

"Lilly gibt einen kleinen Seufzer von sich, während Hanako lächelt. Ihrer Reaktion nach scheint dies das übliche Ergebnis zu sein."


show tearoom_hisaoe lsmile onlayer master
with charachange

hi "Wie lange spielt ihr beide schon Schach?"


show tearoom_hisaoe hsmile onlayer master
show tearoom_hanae sad onlayer master

with charachange

ha "Seit ich… klein war."


show tearoom_lillye smileclosed onlayer master
show tearoom_hisaoe lsmile onlayer master
with charachange

"Lilly nickt zu Hanakos kurzer Antwort."


show tearoom_lillye smile onlayer master
with charachange

li "Kurz nachdem wir uns kennenlernten haben, hat Hanako mir das Spiel beigebracht. Ich kann sie ab und zu schlagen… aber das ist eine Seltenheit. Mir fehlt wohl die richtige Einstellung."


"Wenn Lilly am Beginn der Oberstufe an diese Schule gekommen ist und Hanako getroffen hat, als sie ins Wohnheim gezogen ist, heißt das, dass sie erst seit etwa einem Jahr spielt."


"Wenn ich sehe, auf welchem Niveau Hanako spielt, überrascht es mich kaum, dass Lilly Probleme hat, sie zu schlagen."


show tearoom_hanae happy onlayer master
show tearoom_hisaoe hthink onlayer master
with charachange

ha "Aber… sie ist besser mit Sprachen als ich, also…"


show tearoom_lillye ara onlayer master
show tearoom_hisaoe lthink onlayer master
with charachange

"Lilly lächelt dankbar – wenn auch leicht amüsiert – als Hanako das Kompliment sofort zurückgibt."


show tearoom_lillye weaksmile onlayer master
with charachange

li "Na ja, es ist wie es ist."


stop music fadeout 3.0
play sound sfx_warningbell

"Zu unser aller Überraschung klingelt plötzlich die Schulglocke und kündigt das Ende der Mittagspause an."


show tearoom_lillye thinking onlayer master
show tearoom_hisaoe loops onlayer master
with charachange

li "Hmm, dieses Spiel hat länger gedauert als ich dachte."


hi "Stimmt. Wir sollten uns auf den Weg machen."


show tearoom_hanae shy onlayer master
show tearoom_lillye weaksmile onlayer master
show tearoom_hisaoe thinkclosed onlayer master
with charachange

"Hanako packt ihre Sachen bereits zusammen. Ich nehme Lillys Tasche und halte sie ihr hin. Sie nimmt sie und nickt, setzt sie aber zu meiner Überraschung zurück auf dem Tisch."


play music music_daily fadein 2.0

scene bg school_miyagi onlayer master
show lilly basic_smileclosed onlayer master at twoleft
show hanako basic_normal onlayer master at tworight
with locationskip

li "Hisao, darf ich dich um einen Gefallen bitten? "


hi "Sicher doch."


show lilly basic_smile onlayer master at twoleft
with charachange

li "Hättest du etwas dagegen, wenn ich dein Gesicht kurz abtasten würde?"


hi "Äh… nein, mach nur. Es macht mir nichts aus."


"Auf diese Bitte war ich überhaupt nicht vorbereitet, aber sobald ich mich von der Überraschung erholt habe, erscheint sie mir verständlich. Bis jetzt hat Lilly gar keine Vorstellung, wie ich eigentlich aussehe, und nur so kann sie es herausfinden."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

show ev lilly_touch_uni onlayer master
with GenericWhiteout(0.5,0.1,3.0)

"Lilly hebt ihre rechte Hand. Ich nehme sie in meine und führe sie zu meinem Gesicht, bevor ich sie wieder loslasse."


"Das Zimmer ist völlig still, als Lillys Hand über meine Gesichtszüge gleitet. Sie betastet mein Kinn, meine Wangen, und den Rest meines Gesichts."


"Ich hatte erwartet, dass sich das viel beunruhigender anfühlen würde. Wahrscheinlich liegt das daran, dass ihr Vorgehen einzig und allein praktische Gründe hat und sich funktionell nicht von dem Anschauen eines Gesichts unterscheidet."


"Ihre Hand ist weich, aber ich bin überrascht, wie lang ihrer Finger sind – ganz zu schweigen davon, wie sicher sogar ihre kleinsten Bewegungen sind. Ich habe keinerlei Zweifel daran, dass ihr Tastsinn meinem weit überlegen ist."


"Ihre Hand fährt flüchtig durch meine Haare, bevor sie sie zurückzieht. Ich bin sicher, dass sie sich jeden Zentimeter meines Gesichts eingeprägt hat. Erst jetzt merke ich, dass Hanako uns die ganze Zeit schweigend beobachtet hat."


$ renpy.music.set_volume(1.0, 2.0, channel="music")

scene bg school_miyagi onlayer master
show hanako basic_distant onlayer master at tworight
show lilly basic_weaksmile_close onlayer master at twoleft
with whiteout

li "Danke, dass du mir diesen Gefallen getan hast, Hisao."


show lilly basic_smile_close onlayer master at twoleft
with charachange

li "Ich denke, du bist ziemlich gutaussehend, wenn ich so sagen darf."


"Ihr Kommentar lässt mich leicht erröten, aber dann ziehe ich fragend eine Augenbraue hoch."


hi "Aber wenn du nicht sehen kannst, wie…"


show lilly basic_pout_close onlayer master at twoleft
with charachange

li "Nur weil ich nicht sehen kann, heißt das nicht, dass ich keine eigenen Vorlieben habe."


show hanako emb_timid onlayer master at tworight
with charachange

ha "Äh, wir sollten besser gehen…"


hi "Da ist was dran. Wir sehen dich dann später, Lilly."


scene bg school_hallway2 onlayer master
show lilly basic_smile onlayer master at twoleft
show hanako emb_smile onlayer master at tworight
with locationskip

"Während wir durch die Gänge zu unserem Klassenzimmer zurückwandern, fällt mir auf, dass Hanako leiser zu sein scheint als vorhin – dafür aber auch weniger nervös."


"Lilly, deren Hand auf Hanakos Schulter liegt, nimmt anscheinend ihren selbstbewussteren Gang auch wahr und lächelt."


"Ich denke, wenn ich den Rest meiner Zeit an der Yamaku auf diese Art und Weise verbringen könnte, wäre es gar nicht so schlimm. Schließlich sind kleine, fröhliche Momente mit Freunden alles, was man braucht, um glücklich zu sein."


scene bg school_scienceroom onlayer master
with locationskip

play sound sfx_rumble

"Als ich meinen Tisch erreiche und meine Tasche daneben abstelle, merke ich etwas. Genauer gesagt, mein Magen merkt etwas."


"Ich war so mit den beiden beschäftigt, dass ich glatt vergessen habe, mein Mittagsessen zu kaufen…"


stop music fadeout 2.0

scene black onlayer master
with dissolve



label de_L2:

scene bg school_dormhisao onlayer master
with locationchange

"Samstag. Mein zweitliebster Tag der Woche."


"Das liegt fast ausschließlich daran, dass dies der Tag mit den zweitwenigsten Unterrichtsstunden ist und die Schule mit Anfang der Mittagspause aus ist."


scene bg school_dormhallway onlayer master
with locationchange

"Zuversichtlich öffne ich meine Tür. Ich bin mehr als zuversichtlich, dass ich das schöne Wetter und den kürzeren Schultag genießen werde."


scene bg school_dormhallground onlayer master
with locationchange

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_footsteps_hard

"Zuversichtlich laufe ich den Gang entlang und gehe die Treppen hinab zur Eingangshalle des Wohnheims."


$ renpy.music.set_volume(0.6, 4.0, channel="ambient")

"Zuversichtlich drehe ich mich um, um zu sehen, wessen Fußschritte ich hinter mir höre."


$ renpy.music.set_volume(1.0, 4.0, channel="ambient")

"Meine Zuversicht, dass dies ein angenehmer Tag werden wird… schwindet."


stop ambient
play music music_kenji fadein 0.5

show kenji happy onlayer master:
    center
    xpos 0.4
    easein 0.5 xpos 0.5
with charaenter

ke "Hey, Kumpel. Was geht?"


hi "Nicht viel. Ich freue mich auf den Nachmittag. Und du?"


show kenji happy_close onlayer master at center
with characlose

"Viel zu vertraulich legt er einen Arm um meine hängenden Schultern. Etwas liegt in der Luft."


show kenji neutral_close onlayer master
with charachange

ke "Lass uns nach draußen gehen."


hi "Das wollte ich gerade, bevor du mich aufgehalten hast."


show kenji tsun_close onlayer master
with charachange

scene bg school_dormext_full onlayer master
with locationchange

"Meine Reaktion auf sein Gehabe gefällt ihm nicht. Ich ignoriere ihn, gehe hinaus und steige die Treppen hinab."


"Es dauert nicht lange, bis er mich wieder einholt. Ich frage mich, ob er Geld will oder eine neue Verschwörungstheorie auf Lager hat. Vielleicht beides?"


show kenji tsun onlayer master:
    center
    xpos 0.6
    easein 0.5 xpos 0.5
with charaenter

ke "Ich habe ein Hühnchen mit dir zu rupfen."


hi "Was du nicht sagst."


ke "Es hat mit dieser Blondine zu tun. Du weißt, von wem ich rede."


"Also eine Verschwörungstheorie. Einen Moment überlege ich, ob ich Unwissenheit vortäuschen sollte, aber ich denke, dass das schneller vorbei sein wird, wenn er einfach alles rauslassen kann."


hi "Lilly? Deine Klassenkameradin?"


show kenji rage onlayer master at center
with vpunch

ke "Du bist mit ihr per du?"


"Er scheint von dieser Entwicklung zutiefst schockiert zu sein. Hat er etwa erwartet, dass ich nicht antworten kann?"


show kenji tsun onlayer master
with charachange

"Er reißt sich zusammen und hustet in seine geschlossenen Hand – übertrieben dramatisch, so wie er alles tut."


ke "Na egal. Ich bin hier, um dich zu warnen. Du weißt schon. Von Mann zu Mann."


hi "Vor wem willst du mich warnen? Vor Lilly?"


ke "Ja. Du kennst sie nicht, Mann."


"Das ist größtenteils wahr. Ich kenne sie und Hanako seit weniger als zwei Wochen, und bisher haben wir in der Mittagspause nur über banale Dinge wie die Schule geredet."


hi "Ich bin ziemlich sicher, dass du sie auch nicht kennst."


ke "Darum geht es nicht. Du bist derjenige, der so viel Zeit mit ihr verbringt."


"Ich finde es besorgniserregend, dass Kenji, dessen soziale Kontakte wohl gegen null gehen, etwas so Triviales erfahren hat, wie mit wem ich mich angefreundet habe."


"Andererseits… Ich bin neu hier, und sie ist nicht nur Klassensprecherin, sondern auch eine große Blondine."


"Vielleicht sollte ich seine Tirade als eine Warnung ansehen, dass an dieser Schule eine Gerüchteküche existiert und dass ich mich mittendrin befinde."


hi "Wir essen zusammen zu Mittag. Nichts Besonderes."


show kenji neutral onlayer master
with charachange

ke "Hey Kumpel, Schnee von gestern. Siehst du diesen Schnee? Der ist von gestern. Ein Mann muss tun, was ein Mann tun muss, um Informationen zu kriegen."


show kenji tsun onlayer master
with charachange

ke "Ich wollte nur sicherstellen, dass du nicht zu tief in den Schnee gerätst."


hi "Ich verstehe kein Wort, Kenji."


show kenji happy onlayer master
with charachange

ke "Kein Problem. Viele Leute verlieren den Weg. Deshalb bin ich hier – zum Helfen."


scene bg school_gardens onlayer master
show kenji neutral onlayer master
with locationskip

ke "Sei einfach vorsichtig, wenn sie in der Nähe ist, okay? Sie mag zwar harmlos aussehen, aber ich habe von Sachen Wind bekommen. Ziemlich üble Sachen."


show kenji tsun onlayer master
with charachange

ke "Du kennst den Schülerrat, oder?"


"Als er diese Worte ausspricht, scheint er unfreiwillig zu schaudern. Die Vorstellung, ihn und Shizune zusammen in ein Zimmer zu sperren, ist höchst amüsant. Ich frage mich, ob sich die beiden jemals begegnet sind."


hi "Ja, Shizune und Misha sind in meiner Klasse. Aber ich scheine ihren Rekrutierungsversuchen erfolgreich entkommen zu sein."


show kenji happy onlayer master
with charachange

ke "Gut gemacht, Kumpel, gut gemacht."


show kenji tsun onlayer master
with charachange

ke "Aber diese Blondine? Sie war drin. Im Schülerrat. Sie war. Ein. Verdammtes. Mitglied."


hi "Verstehe. Und weiter?"


ke "Und jetzt ist sie es nicht mehr."


stop music fadeout 3.0

hi "…"


ke "Ernsthaft, denk mal darüber nach. Es muss etwas passiert sein."


"Ich bleibe für einen Moment stehen. Wahrscheinlich mache ich mir mehr Gedanken über die Sache als ich sollte."


"Es würde diesen Streit zwischen Shizune und Lilly zumindest teilweise erklären, oder? Nein, nicht wirklich. Auch das Verlassen des Schülerrats muss einen Auslöser gehabt haben."


"Letzten Endes erklärt es kaum etwas. Es deutet nur darauf hin, dass die Feindschaft zwischen den beiden schon länger besteht."


hi "Da ist was dran. Ich verstehe aber immer noch nicht, welche Auswirkung das auf mich hat."


show kenji neutral onlayer master
with charachange

ke "Okay, was ist hiermit: Lilly ist offensichtlich Ausländerin."


hi "Offensichtlich."


ke "Und welche Nationalität hat sie?"


"Ich öffne meinen Mund, um seine Frage zu beantworten, merke aber, dass ich keine Antwort habe. Tatsächlich habe ich mir bisher kaum Gedanken darüber gemacht."


"Da sie keinen Akzent hat und sich wie eine typische Japanerin benimmt, schien es mir nie wirklich wichtig zu sein. Aber jetzt, wo er es erwähnt, bin ich ziemlich neugierig."


hi "Um ehrlich zu sein, ich weiß es nicht. Vielleicht ist sie Engländerin? Engländer mögen Tee."


"Ich sollte wahrscheinlich solche Klischees vermeiden, aber andere Anhaltspunkte habe ich nicht."


show kenji happy onlayer master
with charachange

play music music_kenji fadein 1.0

ke "Du denkst nicht richtig mit. Zum Glück bin ich hier, um für dich zu denken."


hi "Wow, danke."


"Er ignoriert meinen Sarkasmus mühelos."


show kenji neutral onlayer master
with charachange

ke "Beantworte mir diese Frage:"
ke "Welche Gruppe hat eine Menge soziale Macht, ist stinkreich – du weißt, dass alle Blondinen reich sind, oder? – hat eine lange Geschichte von Auseinandersetzungen, und war mal Teil einer viel größeren Organisation?"


hi "Die römisch-katholische Kirche?"


show kenji tsun onlayer master
with charachange

ke "… Na ja, die auch."


show kenji neutral onlayer master
with charachange

ke "Aber außerdem ist da die Mafia. Komm schon! Reich. Ausländerin. Es ist unmöglich, dass sie keine Verbindungen dorthin hat."


"Ich habe Grund, die Logik seiner Schlussfolgerungen anzuzweifeln, aber er scheint nicht aufhören zu wollen."


scene bg school_hallway3 onlayer master
show kenji neutral onlayer master
with locationskip

ke "Weißt du, was ich glaube, wo sie herkommt?"


hi "Italien?"


show kenji tsun onlayer master
with charachange

ke "Das italienische Festland ist für kleine Fische. Sie muss aus Sizilien sein. Alle Mafiosi kommen von dort."


show kenji happy onlayer master
with charachange

ke "Nein, warte: Russland. Verdammt, das könnte schlecht sein. Mit der Mafia dort ist nicht zu spaßen, Kumpel. Überall ehemalige KGB-Agenten, paramilitärische Gruppen, Hardcore-Schmuggel, und-"


hi "Warte, warte, halt, nicht so schnell. Worauf willst du eigentlich hinaus?"


show kenji neutral onlayer master
with charachange

ke "Du weißt nicht, wozu sie fähig ist. Ich werde dir nicht im Weg stehen – so operieren Agenten nicht – aber ich möchte, dass du dich in Acht nimmst."


show kenji tsun onlayer master
with charachange

ke "Wenn die Zeit kommt, werden wir jede Hilfe brauchen, die wir kriegen können. Ich will dich nicht verlieren, mein Waffenbruder."


"Na ja, wenigstens macht er sich Sorgen um mich. Auf seine eigene Art."


stop music fadeout 4.0

show kenji tsun onlayer master:
    center
    easeout 0.5 xpos 0.6 alpha 0.0
with None

"Als sich die Wege zu unseren jeweiligen Klassenzimmern trennen, winke ich zum Abschied, aber ich bin mir nicht sicher, ob er meine Geste wahrnimmt."


scene bg school_scienceroom onlayer master
with shorttimeskip

play ambient sfx_crowd_indoors fadein 2.0

"Während ich die Bücher in meiner Tasche verstaue, sehe ich die Bücher, die ich letzte Woche aus der Bibliothek ausgeliehen habe. Ich könnte sie eigentlich zurückbringen, da ich sie nach nur zwei Tagen schon fertiggelesen hatte."


"Ich überlege kurz, ob ich Hanako einladen soll mitzukommen, aber sie ist schon weg. Ich kann wahrscheinlich sowieso besser lernen, wenn ich allein bin."


"Ich strecke mich kurz, winke ein paar Klassenkamaraden, die mir ebenfalls zuwinken, und verlasse das Klassenzimmer."


stop ambient fadeout 1.0

scene bg school_library onlayer master
with locationskip

"Als ich meine Tasche öffne und die Bücher in das Rückgabefach am Hauptschalter lege, bemerke ich eine fremde Person hinter dem Schalter: eine alte, ergrauende Frau. Sie muss Yuukos Ersatz sein, wenn diese im Café arbeitet."


"Ich mache mich auf die Suche nach einem freien Tisch. Dies ist leichter gesagt als getan, denn obwohl nicht viele Schüler hier sind, sitzen alle an einem eigenen Tisch."


"Ich bemerke einen vertrauten Haarschopf, und gehe zu einem Tisch in der Brailleabteilung hinüber."


show lilly basic_smileclosed onlayer master
with charaenter

"Es ist schwer zu sagen, ob Lilly sich intensiv konzentriert oder nicht. Während ihre Finger über die mit Punkten gefüllten Seiten ihres Buches gleiten, bleibt ihr Gesichtsausdruck seelenruhig."


hi "Hallo. Stört es dich, wenn ich mich hier hinsetze?"


show lilly basic_surprised onlayer master
with charachange

li "Hmm? Oh, nein, überhaupt nicht…"


"Sie unterbricht sich. Offenbar war sie mit ihren Gedanken noch woanders."


play music music_lilly fadein 10.0

show lilly basic_smile onlayer master
with charachange

li "Ah, Hisao."


show lilly basic_smileclosed onlayer master
with charachange

"Sie begrüßt mich mit einem Kopfnicken, als ich mich ihr gegenüber setze, ein Chemiebuch aus meiner Tasche nehme, und schnell zu dem Kapitel blättere, das wir gerade im Unterricht durchnehmen."


"Eine Weile lang sitzen wir und lesen, jeder auf seine eigene Weise."


"Ihre Anwesenheit erinnert mich jedoch an das, was Kenji heute Morgen gesagt hat. Dies und die Tatsache, dass ich noch nie jemanden Braille lesen gesehen habe, lässt mich immer wieder zu ihr hinüberblicken."


"Ich fühle mich deswegen irgendwie schuldig, denn sie hat keine Möglichkeit, meine Blicke wahrzunehmen."
"Ich beschließe, sie einfach zu fragen. Schließlich ist ihre Abstammung nicht gerade ein Staatsgeheimnis, und es gibt noch etwas, das ich gerade erst anhand ihrer Bewegungen bemerkt habe."


hi "Hey, Lilly, darf ich dir eine Frage stellen?"


show lilly basic_smile onlayer master
with charachange

li "Natürlich. Stimmt etwas nicht?"


hi "Ich habe mich nur gefragt… Du bist zumindest teilweise ausländisch, oder?"


show lilly basic_giggle onlayer master
with charachange

"Sie kichert leise und legt ihr Buch hin."


show lilly basic_cheerful onlayer master
with charachange

li "Es amüsiert mich immer, dass Leute mit dieser Frage so vorsichtig sind. Akira hat schon mehrmals erwähnt, dass sie und ich uns vom Aussehen her von den meisten anderen unterscheiden."


show lilly basic_smile onlayer master
with charachange

li "Die Details sind ein bisschen kompliziert, aber ich bin halb Japanerin und halb Schottin."


"… Schottin? Das hätte ich nicht erwartet. Ich muss mir Mühe geben, um nicht laut damit herauszuplatzen."


"Ich versuche, mir das Land vorzustellen. Nach allem, was ich über das Vereinigte Königreich weiß, ist Schottland kein schlechter Platz zum Leben, aber ich bin mir nicht wirklich sicher."


"Meine erste Vermutung, England, war ziemlich nahe dran – zumindest geographisch. Eine Frage bleibt aber noch."


hi "Aber du hast keinen Akzent…?"


show lilly basic_weaksmile onlayer master
with charachange

li "Das sind die erwähnten Details. Ich bin in Japan geboren und aufgewachsen, obwohl meine Mutter Ausländerin ist."


hi "Ah, verstehe."


"Moment mal. Wenn sie nur ins Wohnheim gezogen ist, weil Akira länger arbeitet…"


hi "Deine Eltern wohnen nicht in der Nähe der Schule?"


show lilly basic_reminisce onlayer master
with charachange

"Sie seufzt leise, als ob sie nicht erwartet hätte, dass ich weiter nachfrage. War ihre bisherige Offenheit nur eine Fassade?"


li "Nicht… wirklich. Es ist schon lange her, dass wir uns getroffen haben."


"Ich habe das Gefühl, dass ich noch nicht die ganze Geschichte erfahren habe, möchte aber meine Nase wirklich nicht noch weiter in ihre Angelegenheiten stecken. Ihr Gesichtsausdruck zeigt, dass ihr die Sache etwas unangenehm ist."


hi "Also… sprichst du viel Englisch? Ehrlich gesagt weiß ich nicht viel über Schottland, aber zumindest weiß ich, dass das dort die Hauptsprache ist."


"Es dauert einen Moment, bis sie sich sammelt, dankbar für den Themenwechsel."


show lilly basic_smileclosed onlayer master
with charachange

li "Ganz recht. Als ich jünger war, wurde bei uns zu Hause hauptsächlich Japanisch gesprochen, aber meine Familie hat dafür gesorgt, dass Akira und ich auch unsere schottische Seite kennenlernten."


show lilly basic_smile onlayer master
with charachange

li "Ich spreche fließend Englisch, aber ich lerne es auch in der Schule, hauptsächlich um in Übung zu bleiben und Qualifikationen auf dem Papier zu haben."


hi "Du bist also zweisprachig? Das ist ziemlich beeindruckend."


show lilly basic_weaksmile onlayer master
with charachange

li "So weit würde ich nicht gehen. Eltern zu haben, die die Sprache sprechen, ist ein großer Vorteil, und es ist nicht allzu schwer, englische Bücher in Braille zu kaufen oder zu importieren. Zumindest mit Yuukos Hilfe."


show lilly basic_smileclosed onlayer master
with charachange

li "Es gibt hier außerdem einen ziemlich großen Bedarf an Englischlehrern, was mich ebenfalls motiviert, es gründlich zu lernen."


"Ein Bedarf an Englischlehrern? Für einen Augenblick frage ich mich, warum sie das erwähnt hat."


hi "Du willst also Englischlehrerin werden?"


show lilly basic_cheerful onlayer master
with charachange

"Sie nickt enthusiastisch."


"Es muss schön sein, so konkrete Zukunftspläne zu haben. Ich habe mir nie viele Gedanken über meine Zukunft gemacht, also bin ich ein bisschen neidisch."


hi "Hmm…"


show lilly basic_smile onlayer master
with charachange

li "Stimmt etwas nicht?"


hi "Es ist nur… ich kann mir dich als Englischlehrerin ziemlich gut vorstellen. Es passt zu dir."


show lilly basic_emb onlayer master
with charachange

"Einen Moment lang ist sie sprachlos, dann senkt sie ihr Gesicht ein bisschen und kichert nervös. Das hat sie bisher noch nie getan."


"Wenn man Lillys Rolle als Klassensprecherin und ihre Zuverlässigkeit in Betracht zieht, dann passt eine Lehrerstelle zu ihre Persönlichkeit."


hi "Tut mir leid, das war vielleicht ein bisschen viel. Es stimmt aber."


show lilly basic_weaksmile onlayer master
with charachange

"Sie macht eine wegwerfende Handbewegung und erlangt ihre Fassung schnell wieder."


li "So war das nicht gemeint, es ist nur… Nur eine Person hat das jemals zu mir gesagt."


stop music fadeout 8.0

"Eine kurze, etwas peinliche Stille folgt auf unsere Unterhaltung. Ohne es zu wissen, habe ich schon wieder ein unangenehmes Thema ins Gespräch gebracht."


"Ich sollte versuchen, sie ein bisschen aufzumuntern. Immerhin bin ich für ihren Stimmungswandel verantwortlich."


hi "Möchtest du nachher Mittagessen in der Cafeteria holen?"


"Vielleicht wird es sie aufmuntern, oder sie zumindest von ihrer anscheinend komplizierten Familiensituation ablenken."


show lilly basic_planned onlayer master
with charachange

"Ihrem Lächeln nach zu urteilen, scheint mein Vorschlag die gewünschte Wirkung zu haben."


show lilly basic_ara onlayer master
with charachange

li "Ich weiß den Gedanken zu schätzen, aber das Essen dort…"


"Eine ziemlich schnelle Richtungsänderung unseres Gesprächs. Aber sie hat nicht ganz Unrecht – das Essen dort ist nicht so toll."


hi "Vielleicht das Shanghai? Wir können Hanako fragen, ob sie auch mitkommen will."


show lilly basic_surprised onlayer master
with charachange

li "Äh…"


hi "Was ist los?"


show lilly basic_weaksmile onlayer master
with charachange

li "Ich hatte es fast vergessen, bis du mich daran erinnert hast. Hanako hat bald Geburtstag, und ich wollte morgen in die Stadt fahren und nach einem Geschenk suchen."


hi "Wenn das eine Einladung ist, würde ich dir gerne Gesellschaft leisten."


"Es wäre sicher gut, wenn ich mich in der Stadt ein wenig besser auskennen würde. Da ich noch nie dort war, würde ich mich hoffnungslos verirren, wenn ich allein wäre."


show lilly basic_smile onlayer master
with charachange

"Sie nickt als Zeichen, dass sie mit diesem Plan für den Sonntag einverstanden ist."


"Schließlich wenden wir uns wieder unseren Büchern zu, doch bevor ich wieder anfange zu lesen, werfe ich ihr einen letzten Blick zu."


"Vielleicht mache ich mir zu viele Gedanken über meine Situation. Immerhin hat wohl jeder hier seine eigenen, einzigartigen Probleme."


"Die Gelegenheit, einmal herauszukommen und meinen Kopf freizumachen, wird mir wahrscheinlich guttun."


scene black onlayer master
with dissolve



label de_L3:

play ambient sfx_traffic fadein 10.0

scene black onlayer master
with None

scene bg city_street1 onlayer master at Fullpan(16.0, "left")
with locationchange

"Die ganze Zeit auf den Fernseher in einem Schaufenster zu starren, ist so langweilig, dass ich mich mühelos von dem kitschigen Anblick losreißen kann."


"Nachdem man an der Yamaku gelebt hat, erscheint einem die Stadt wie eine völlig andere Welt."


"Nicht in den Gängen rennen. Sich in den Klassenzimmern immer ruhig und ordnungsgemäß benehmen. Beim Verlassen von Räumen in beide Richtungen schauen."
"Fahrstühle sind nur für bewegungseingeschränkte Schüler. Treppen im Gänsemarsch benutzen."


"Im Vergleich zu solchen strengen – fast militärischen – Vorschriften, ist die Einkaufspassage der Stadt wie ein fremdes Land."


"Während des Festes war an der Schule einiges los, aber die Außenwelt ist noch einmal etwas anderes."


"Es ist seltsam. Da ich vor meinem Unfall in einer Großstadt gewohnt habe, sollte sich das natürlicher anfühlen als es Yamaku und das kleine Dorf jemals sein könnten."


"Dennoch fühlt es sich irgendwie fremd an. Die Hochwege und Wolkenkratzer, die mit dreifach mannsgroßen Werbetafeln bestückt sind, können mich von den Reaktionen der vorbeigehenden Menschenmenge nicht ablenken."


$ renpy.music.set_volume(0.7, 0.5, channel="ambient")

show lilly cane_smileclosed_cas_close onlayer master:
    center
    xpos 0.2
    easein 1.0 twoleft
show bg city_street1 onlayer master at left
with Dissolve(1.0)

"Lilly behält eine Hand auf meiner Schulter und benutzt ihre andere, um ihren Blindenstock mit einer metronomartigen Stetigkeit über den Boden zu bewegen. Ich schaue zu ihr hinüber und sehe, dass sie immer noch ihr neutrales Lächeln zeigt."


"Da ich sie bisher nur in ihrer Schuluniform gesehen habe, hätte ich sie ohne ihren Blindenstock und ihre markanten Haare kaum wiedererkannt, als sie auf der Bank saß und auf mich gewartet hat."


"Ich weiß nicht, ob sie die Blicke der Passanten wegen ihrer Größe, ihres ausländischen Aussehens oder ihrer offensichtlichen Blindheit auf sich zieht. Wahrscheinlich eine Kombination aus allem."
"Was nicht heißen soll, dass irgendeiner dieser Gründe besser wäre als die anderen. Ich fühle mich jedenfalls ziemlich unwohl."


show lilly cane_smile_cas_close onlayer master
with charachange

li "Hast du irgendwelche Ideen, wo wir mit unserer Suche anfangen sollen, Hisao?"


"Ihre sanfte Stimme unterbricht meine Gedanken."


"Ich kann mir nicht vorstellen, dass ihr die Aufmerksamkeit entgeht, die sie auf sich zieht, aber sie scheint davon unbeeindruckt zu sein. Ich habe den Eindruck, dass sie sich gerne im Freien bewegt, also hat sie sich vielleicht daran gewöhnt."


hi "Nicht wirklich. Ich bin zum ersten Mal in dieser Stadt, also kenne ich mich nicht aus."


show lilly cane_listen_cas_close onlayer master
with charachange

"Sie runzelt nachdenklich die Stirn und plant eine Route, die wir nehmen können. Und vermutlich auch einen Weg, mir diese Route zu erklären."


"In der Zeit, die ich mit ihr verbracht habe, ist mir aufgefallen, dass man an ihrer Körpersprache fast gar nicht erkennt, wenn sie in Gedanken versunken ist."


"Ihr Gesichtsausdruck mag sich ändern, aber sie bewegt sich kaum. Sie scheint aber im Allgemeinen wenige ausladende Gesten zu machen, also dachte ich, dass das einfach Teil ihres zurückhaltendes Wesens ist."


show lilly cane_weaksmile_cas_close onlayer master
with charachange

li "Gibt es hier in der Nähe einen großen Elektronikladen?"


"Ich schaue mich kurz um. Zuerst sehe ich nur Bekleidungsgeschäfte, doch nach ein paar Sekunden bemerke ich einen Laden mit einem hellblauen Schild, der eine kurze Strecke entfernt liegt und zu ihrer Beschreibung passt."


hi "Ja, er liegt ein Stück vor uns. Sollen wir in diese Richtung gehen?"


show lilly cane_smile_cas_close onlayer master
with charachange

"Glücklicherweise war das genau die Information, die sie brauchte. Sie nickt, und wir wandern zu Lillys unbekanntem Ziel, indem wir markante Punkte als Wegweiser benutzen."


stop ambient fadeout 2.0

scene ev icecream onlayer master
with shorttimeskip

play music music_happiness fadein 2.0

"Eisstandbesitzer" "Bitte sehr! Einmal Vanille, einmal Schokolade."


scene bg city_street2 onlayer master at center
with locationchange

"Ich reiche das Geld über den Ladentisch und bringe die Eiswaffeln zu dem Geländer, auf dem Lilly sitzt."


"Ich kann nicht fassen, dass sie mich ausgetrickst hat. Sie hat mich nicht nur zu einem Eisstand geführt, sondern auch erreicht, dass ich ihr eins kaufe. Wenigstens hat sie mir das Geld für ihr Eis gegeben."


show lilly cane_smileclosed_cas onlayer master at Transform(xanchor=0.5, xpos=0.2, ypos=0.2, yanchor=0.0)
with charaenter

"Sie wartet geduldig dort auf mich, wo ich sie zurückgelassen habe. Ich schätze, sie wollte aus dem Tag mehr machen als nur eine einfache Einkaufstour."


show lilly cane_smileclosed_cas onlayer master:
    ease 1.0 xpos 0.5 xanchor 0.5 ypos 0.15
show bg city_street2 onlayer master:
    ease 1.0 left
with None

show lilly basic_satisfied_cas_close onlayer master:
    xanchor 0.5 xpos 0.2 ypos 0.2 yanchor 0.0
    ease 1.0 xpos 0.5 xanchor 0.5 ypos 0.15 
show bg city_street2 onlayer master:
    ease 1.0 left
with Dissolve(1.0)

"Ich spreche sie an und lege die Vanille-Eiswaffel langsam in ihre ausgestreckten Hände. Bevor ich loslasse, vergewissere ich mich, dass sie sie wirklich fest im Griff hat."


"Wenigstens ist ihr Geschmack ziemlich normal. Als sie zuerst nach Eis gefragt hat, habe ich mir Sorgen gemacht, dass sie irgendeine seltsame Geschmacksrichtung bestellen würde."


hi "Hier ist dein Wechselgeld."


show lilly basic_smileclosed_cas_close onlayer master at Transform(xalign=0.5, ypos=0.15)
with charachange

li "Schon gut. Behalte es."


"Ich setze an zu protestieren, aber ich beschließe, dass sich das bei einem so kleinen Betrag nicht lohnt. Ich stecke die Münzen in meine Tasche und bessere damit mein mageres Taschengeld ein wenig auf."


show lilly basic_smileclosed_cas_close onlayer master
with charachange

"Lilly gibt keine Anzeichen, dass sie die Absicht hat aufzustehen, also setze ich mich neben sie und fange an, mein Eis zu essen."


hi "Dieses Sommerwetter ist schön. Hoffentlich bleibt es noch eine Weile so."


show lilly basic_weaksmile_cas_close onlayer master
with charachange

li "Du findest das auch? Ich fange an zu glauben, dass ich die Einzige bin, die den Winter bevorzugt."


"Ich denke einen langen Moment über ihre Worte nach."


hi "Ja, das ist gut möglich."


show lilly basic_pout_cas_close onlayer master
with charachange

"Es folgt die beabsichtigte Reaktion. Sie sieht niedlich aus, wenn sie schmollt."


hi "Aber ich kann mir auch nicht vorstellen, was am Winter so gut sein soll. Man kann nicht nach draußen gehen, ohne sich einzumurmeln, und auch wenn man's tut, friert man trotzdem noch."


show lilly basic_reminisce_cas_close onlayer master
with charachange

li "Früher wohnte ich weiter nördlich. Dort gab es viel Schnee, in dem man spielen konnte, also ist auch wenig Nostalgie dabei. Die Hitze gefällt mir auch nicht."


hi "Du kannst wenigstens einen Rock tragen, also beschwer dich nicht."


show lilly basic_giggle_cas_close onlayer master
with charachange

"Sie kichert amüsiert, und wir essen beide weiter an unseren schon schmelzenden Eiswaffeln."


play ambient sfx_crowd_outdoors fadein 2.0

hide lilly onlayer master
show crowd onlayer master at left
with shorttimeskip

"Während wir essen, beobachte ich die vorbeigehenden Menschen und höre hier und da ein paar Gesprächsfetzen heraus."


show lilly basic_satisfied_cas_close onlayer master at Transform(xalign=0.5, ypos=0.15)
with charaenter

"Ich schaue zu Lilly und sehe, dass sie ihr Eis pflichtbewusst von oben nach unten leckt. Dabei bemerkt sie nicht, dass es angefangen hat zu schmelzen."


hi "Es schmilzt."


show lilly basic_surprised_cas_close onlayer master
with charachange

li "Wo genau?"


hi "Ähm… ein wenig nach unten?"


show lilly basic_listen_cas_close onlayer master
with charachange

"Sie senkt ihren Mund von der Spitze der Eiswaffel, hat aber keine Ahnung, wo genau es tropft. Darauf folgt ein Spiel, bei dem ich sie nach links oder rechts führen muss, bis sie es endlich findet."


"Für einen Zuschauer muss die Szene vollkommen bizarr wirken: Ein Mädchen dreht ihre Eiswaffel mit geschlossenen Augen immer wieder herum, während der Junge neben ihr Anweisungen gibt."
"Vielleicht sieht es wie eine merkwürdige Variante eines Kinderspiels aus."


show lilly basic_smileclosed_cas_close onlayer master
with shorttimeskip

"Schließlich sind wir mit unserem Eis fertig und vertreiben uns unsere Zeit mit Smalltalk."


stop music fadeout 3.0

show lilly back_listen_cas_close onlayer master
with charachange

"Plötzlich unterbricht sich Lilly mitten im Satz und legt den Kopf auf für sie typische Weise zur Seite. Es ist ein eindeutiges Zeichen dafür, dass etwas ihre Aufmerksamkeit erregt hat."


show lilly back_smileclosed_cas_close onlayer master
with charachange

li "Ah…"


hi "Was ist los?"


show lilly back_smile_cas_close onlayer master
with charachange

li "Ist Akira irgendwo da drüben? Ich denke, ich habe sie gehört."


show lilly back_smile_cas_close onlayer master at Transform(xpos=0.25)
show crowd onlayer master:
    bgright
    xpos 0.55
show bg city_street2 onlayer master:
    bgright
    xpos 0.55
with dissolvecharamove



"Ich ziehe eine Augenbraue hoch und schaue in die Richtung, in die sie sich gewendet hat. Ich zweifele etwas daran, dass sie in der Lage ist, Akiras Stimme aus diesem Getöse herauszuhören."


show akira basic_boo behind crowd onlayer master:
    tworight
    xpos 0.78 ypos 1.13
with charaenter

"Aber tatsächlich kann ich eine blonde Frau in einem Anzug durch die kleinen Lücken in der sich bewegenden Menschenmasse erkennen."


"Ich hebe eine Hand und winke in einem Versuch, ihre Aufmerksamkeit zu erregen."


hi "Satou! Hey, Satou!"


show akira basic_smile onlayer master
with charachange

"Sie bleibt stehen und schaut in meine Richtung, anscheinend hat sie mein Rufen bemerkt. Dann merke ich, dass jemand neben ihr geht."


"Ich habe aber kein freies Blickfeld auf die andere Person, bevor die beiden anfangen, in unsere Richtung zu kommen."


$ renpy.music.set_volume(0.5, 1.0, channel="ambient")
play music music_ease fadein 4.0

show akira basic_smile onlayer master:
    ease 1.0 ypos 1.0 alpha 0.0
with None

show akira basic_smile as akira2 behind lilly onlayer master:
    tworight
    xpos 0.78 ypos 1.13 alpha 0.0
    ease 1.0 ypos 1.0 alpha 1.0
with Pause(1.0)

hide akira onlayer master
with None

show lilly back_smile_cas_close onlayer master at Transform(yalign=1.0)
with charamove

"Als sie uns erreichen, stehen Lilly und ich auf und stauben uns ab."


show lilly back_giggle_cas_close onlayer master
with charachange

li "Akira?"


hide akira2 onlayer master
show akira basic_laugh behind lilly onlayer master:
    tworight
    xpos 0.78 ypos 1.0
with charachange

aki "Hey ihr Zwei."


show lilly back_giggle_cas_close onlayer master at Transform(xpos=0.1)
show akira basic_smile onlayer master at Transform(xanchor=0.5, xpos=0.6)
show crowd onlayer master at center
show bg city_street2 onlayer master at center
with dissolvecharamove

show hideaki bored behind akira at right onlayer master
with charaenter

"Sie nickt in meine Richtung, eine Geste, die ich schnell erwidere. Mein Blick wandert zu dem jungen Mädchen neben ihr, und unsere Augen treffen sich. Akira legt ihr eine Hand auf den Kopf, eine Bewegung, die sie anscheinend nicht beunruhigt."


show hideaki normal onlayer master
with charachange

hh "Ich glaube nicht, dass wir uns schon begegnet sind. Ich bin Hideaki. Ich freue mich, dich kennenzulernen, Hisao."


"Ein Männername? Na, da habe ich ja noch einmal Glück gehabt. Er verbeugt sich, ist aber in seiner Bewegung wegen Akiras Hand auf seinem Kopf ein wenig eingeschränkt."


show lilly basic_smileclosed_cas_close onlayer master at Transform(xpos=0.18)
with charachange

li "Oh, Hideaki ist auch hier? Geht es dir gut?"


show hideaki thinking onlayer master
with charachange

hh "Akira passt gut auf mich auf, danke."


show akira basic_laugh onlayer master
show hideaki sad onlayer master
with charachange

"Akira grinst, als ob sie diese Aussage bekräftigen will. Sie streicht ihm so kräftig durch die Haare, dass sein Kopf die Bewegung mitmachen muss. Sein düsterer Gesichtsausdruck, während sie das tut, ist recht amüsant."


show akira basic_smile onlayer master
with charachange

aki "Onkelchen ist wieder geschäftlich unterwegs, also nehme ich ihn heute mit auf Stadttour."


show akira basic_boo onlayer master
with charachange

aki "Ich hätte den Tag lieber mit meinem Freund verbracht, aber…"


show hideaki closed_up onlayer master
with charachange

"Hideaki versucht, Akiras Gedanken mit einem Husten umzuleiten."


"Während er das tut, merke ich, dass ich mit meinen eigenen Gedanken abschweife. Sie sind verwandt? Und dann auch noch Cousins? Das erklärt, warum sie sich um ihn kümmert."


hi "Hideaki, woher kennst du eigentlich meinen Namen?"


show hideaki serious onlayer master
with charachange

hh "Akira hat ihn mir gesagt. Da du ein Schüler auf der Yamaku bist, nehme ich an, dass du auf irgendeine Weise körperlich behindert bist?"


hi "Nicht alle Schüler dort sind körperlich behindert…"


"Eine Tatsache, die ich selbst erst vor ein paar Tagen erfahren habe. Ich bedanke mich gedanklich bei Shizune und Misha für die Flut an Informationen über die Schule."


"Durch sie habe ich gelernt, dass die Schule nicht nur bereit ist, praktisch jeden aufzunehmen, der an einer nicht-geistigen Behinderung leidet, sondern auch gesunde Leute nicht diskriminiert."


"Es ist jedoch eher unwahrscheinlich, dass viele gesunde Schüler sich dort einschreiben würden. Obwohl die Ausbildungsstandards ziemlich hoch sind, ist die Schule extrem isoliert und stark darauf fokussiert, körperlich behinderten Schülern zu helfen."


show hideaki angry_up onlayer master
with charachange

hh "Du weichst der Frage aus."


"Er ist verdammt scharfsinnig."


"Bevor ich ein weiteres Wort sagen kann, entscheidet er, es mit Raten zu probieren."


show hideaki evil onlayer master
with charachange

hh "Wenn ich raten müsste… dein Herz?"


$ renpy.music.set_volume(0.5, 0.5, channel="music")
$ renpy.music.set_volume(0.0, 0.5, channel="ambient")

show akira basic_lost onlayer master
show lilly basic_listen_cas_close onlayer master
with charachange

"Akira schaut mich mit milder Neugier an. Ihr Interesse ist ebenfalls geweckt. Das war sicher nur ein Zufallstreffer."


hi "Wie hast du…?"


$ renpy.music.set_volume(1.0, 10.0, channel="music")
$ renpy.music.set_volume(0.5, 10.0, channel="ambient")

show hideaki thinking onlayer master
with charachange

hh "Du hast weder fehlende Gliedmaßen noch offensichtliche Missbildungen, also kommen äußerliche Behinderungen nicht infrage."


show hideaki serious onlayer master
with charachange

hh "Wenn man dein Fehlen von merkwürdigen Angewohnheiten in Betracht zieht, ist es auch unwahrscheinlich, dass du eine geistige Behinderung hast."


show lilly basic_planned_cas_close onlayer master
with charachange

li "Aber Yamaku nimmt keine geistig behinderten Schüler auf."


show hideaki bored onlayer master
with charachange

hh "Ich weiß."


show hideaki serious_up onlayer master
with charachange

hh "Jedenfalls ist eine innere Behinderung die einzige verbleibende Möglichkeit."


show hideaki happy onlayer master
with charachange

hh "Ich wusste nicht, welche du haben könntest, also habe ich geraten. Korrekt geraten, wie sich herausgestellt hat. Und deine Reaktion hat meine Vermutung bestätigt."


show akira basic_smile onlayer master
with charachange

"Nicht wenig verwirrt blicke ich zu Akira. Sie grinst und zuckt mit den Schultern. Offensichtlich findet sie die Schlussfolgerungen ihres Partners lustig."


"Er mag schlau sein, wirkt aber mehr als ein bisschen unsympathisch. Er denkt logisch, aber es mangelt ihm an Taktgefühl. In gewisser Weise erinnert mich sein Verhalten an Shizune – und sein Aussehen irgendwie auch."


show hideaki disapproves onlayer master
with charachange

hh "Darf ich fragen, warum du mich anstarrst? Mein Aussehen ist sicherlich nicht derart außergewöhnlich."


"Ist ihm nicht klar, wie merkwürdig er aussieht? Die Gamaschen und sonstige Kleidung könnte ich ignorieren, aber die Haarschleife ist einfach zu viel."


"Das tut aber nichts zur Sache."


hi "Tut mir leid. Du erinnerst mich nur an jemanden."


play sound sfx_impact

show akira basic_boo onlayer master
show hideaki surprise_up onlayer master
with vpunch

"Akira gibt ihm einen scharfen Stoß mit ihrem Ellbogen."


show akira basic_laugh onlayer master
with charachange

aki "Hab dir doch gesagt, dass ihr beide nicht so verschieden seid."


show hideaki closed_up onlayer master
with charachange

"Er hustet in seine Faust und versucht, seine aufrechte und ernsthafte Haltung beizubehalten."


hh "Wie ich sehe, hast du meine Schwester getroffen. Vielleicht wird dir mein vollständiger Name weiterhelfen."


show hideaki serious onlayer master
with charachange

hh "Ich bin Hideaki Hakamichi. Du denkst wahrscheinlich an meine Schwester, Shizune Hakamichi."


"Oh, er ist also Shizunes Bruder."


"Moment mal. Wenn Hideaki der Sohn von Akiras Onkel ist und Shizune seine Schwester, dann sind Lillys und Shizunes Väter verschwägert. Das heißt…"


hi "Lilly und Shizune sind Cousinen?"


show lilly basic_concerned_cas_close onlayer master
show akira basic_smile onlayer master
with charachange

"Lilly stöhnt. Das ist untypisch für sie; normalerweise ist sie zurückhaltender. Ihre Reaktion bringt ein amüsiertes Grinsen auf das Gesicht ihrer Schwester."


"Damit erscheint die Feindschaft zwischen den beiden in einem ganz anderen Licht. Ich hatte gedacht, es wäre ein einfaches Kommunikationsproblem, aber eine Familienfehde macht alles wesentlich komplizierter."


show akira basic_laugh onlayer master
with charachange

aki "Deine Freunde kannst du wählen, aber nicht deine Familie."


show akira basic_boo onlayer master
with charachange

"Sie zuckt halbherzig mit den Schultern. Anscheinend misst sie dem Streit zwischen den beiden nicht so viel Bedeutung bei, wie ich es tue."


show akira basic_smile onlayer master
with charachange

aki "Es ist wie es ist. Was treibt ihr beide denn an diesem schönen Tag?"


show lilly basic_smileclosed_cas_close onlayer master
with charachange

li "Wir suchen ein Geburtstagsgeschenk für Hanako. Es ist bald soweit, und die Woche über haben wir wegen der Schule keine Gelegenheit."


stop music fadeout 7.0

show akira basic_lost onlayer master
with charachange

"Akira macht ein merkwürdiges Gesicht, so als hätte Lilly gerade behauptet, dass der Himmel nicht blau und Wolken nicht weiß seien."


aki "Ist ihr Geburtstag nicht nächsten Monat, am zehnten Juli?"


show lilly basic_surprised_cas_close onlayer master
with charachange

li "Ja… Warum? Stimmt etwas nicht?"


show akira basic_resigned onlayer master
with charachange

"Akiras Gesicht fällt zusammen. Ihre Miene passt überhaupt nicht zu ihrer ruppigen, eigensinnigen Persönlichkeit."


aki "Unsere Eltern haben dich noch nicht angerufen?"


show lilly basic_oops_cas_close onlayer master
show hideaki confused onlayer master
with charachange

"Während Lilly ahnungslos den Kopf schüttelt, schaue ich Hideaki an, um zu sehen, ob er etwas davon weiß. Er reagiert nur mit einem einfachen Schulterzucken."


show akira basic_boo onlayer master
with charachange

"Einen Moment lang denkt Akira nach, was sie tun soll, dann lächelt sie wieder. Es ist beunruhigend, dass sie ihre Gefühle so schnell und effektiv verstecken kann."


show akira basic_smile onlayer master
with charachange

aki "Hey Kurzer, tut mir leid, aber kannst du 'ne Weile mit Hisao abhängen?"


$ renpy.music.set_volume(0.7, 2.0, channel="ambient")

show hideaki normal onlayer master
with charachange

show lilly basic_oops_cas_close onlayer master:
    parallel:
        easeout 1.0 xpos -0.5
    parallel:
        linear 0.7 alpha 0.0
show akira basic_smile onlayer master:
    parallel:
        easeout 1.0 xanchor 1.0 xpos 0.0
    parallel:
        linear 0.7 alpha 0.0
show hideaki normal onlayer master:
    ease 1.0 center
show bg city_street2 onlayer master:
    ease 1.0 right
show crowd onlayer master:
    ease 1.0 right
with Pause(1.0)

hide lilly onlayer master
hide akira onlayer master
with None

"Er nickt und winkt ihr zu. Akira legt einen Arm auf Lillys Schulter und führt sie außer Hörweite."


"Und damit sind der „Kurze” und ich allein."


hi "Also… schönes Wetter, oder?"


show hideaki thinking onlayer master at center
with charachange

hh "Es scheint so."


"…"


hi "Sie haben uns wohl sitzengelassen."


show hideaki serious onlayer master
with charachange

hh "In der Tat."


"Mein Plauderversuch ist armselig. Ich habe überhaupt keine Ahnung, wie ich mit ihm reden soll, und seine roboterhaften Antworten helfen auch nicht weiter. Verlorene Liebesmüh."


show hideaki triangle onlayer master
with charachange

"Ohne ein weiteres Wort fängt er an, auf den Füßen zu wippen. Offensichtlich ist er von dieser Diskussion gelangweilt. Trotz seines ernsten Auftretens ist er doch wie ein kleines Kind."


"Da ich den Verdacht habe, dass dieses Gespräch vorbei ist, besinne ich mich auf den Grund, warum ich eigentlich hier bin."


hi "Ich gehe auf Geschenksuche. Kommst du mit?"


show hideaki normal onlayer master
with charachange

hh "Es gibt nicht viel anderes zu tun."


stop ambient fadeout 0.5

scene bg city_street3 onlayer master
with shorttimeskip

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 2.0

"Nach kurzer Zeit kommen wir zu einem kleinen Laden neben einem Mini-Markt."


"Ausnahmsweise sind die Schaufenster nicht mit Elektronik und Computerspielen gefüllt, sondern mit Puppen, Stoffbären und allen möglichen hölzernen Kuriositäten."


hi "Othellos… Antiquitäten?"


"Ein Antiquitätenladen? Na ja, wenn es irgendetwas in dieser Stadt gibt, dass zu Hanako passen würde, dann müsste es hier zu finden sein."


"Ich greife nach dem alt aussehenden Türknauf, ziehe meine Hand aber in letzter Minute zurück, als ich merke, dass mein Begleiter verlorengegangen ist."


hi "Kommst du nicht mit rein?"


show hideaki triangle onlayer master at center
with charaenter

hh "Ich bleibe einfach eine Weile hier am Zeitungsstand. Lass dich nicht stören."


"Der Ton seiner Stimme ist eindeutig: Er hat keinerlei Interesse an dem Laden und er fühlt sich auch nicht verpflichtet, mir zu folgen."


hide hideaki onlayer master
with charaexit

"Er zieht ohne ein weiteres Wort davon, und ich stoße die dicke Holztür auf. Über meinem Kopf klingelt eine Ladenglocke."


stop ambient fadeout 0.5
play sound sfx_storebell

scene bg city_othello onlayer master at Fullpan(10.0, dir="left")
with locationskip

play music music_soothing fadein 0.5

"Der muffige Geruch von alten Büchern und Holzregalen ist eindeutig anachronistisch."


"Ich werfe einen Blick auf die Ladentheke neben der Tür. Der Mann mit den graumelierten Haaren, der hinter ihr sitzt, liest schweigend ein zerfetztes Buch. Er passt auf jeden Fall gut zum Aussehen des Ladens."


"Ich wandere langsam durch die Gänge und untersuche die handgefertigten und importierten Kuriositäten einzeln, doch keines der Stücke scheint zu Hanako zu passen."


"Ich gehe in die Hocke und untersuche den uralten Eichenschreibtisch im Schaufenster."


"Mindestens dreißig Puppen, die sich in Größe und Machart stark voneinander unterscheiden, sind zu sehen. Das Einzige, was sie gemeinsam haben, sind die langen, viktorianischen Kleider, die sie tragen."


"Ich drehe das Preisschild einer ungefähr hüfthohen Puppe um."


"… Sie ist nicht in meiner Preislage. Überhaupt nicht."


"Ich prüfe auch die anderen Puppen. Je kleiner sie werden, desto deprimierter werde ich."


"Zumindest bis ich bei der kleinsten ankomme. Sie ist gerade noch erschwinglich, dennoch von hoher Qualität, und besitzt langes, kastanienbraunes Haar und ein kleines, blaues Kleid."


"Ich entscheide, dass es die Art von Geschenk ist, die Hanako schätzen würde: hübsch aussehend aber nicht kitschig."


"Nachdem ich die Puppe vorsichtig aufgenommen habe, entscheide ich, mich weiter im Laden umzuschauen. Ich bin mir nicht sicher, ob es daran liegt, dass mir die Atmosphäre gefällt oder ob ich einfach neugierig bin."


stop music fadeout 2.0

show bg city_othello onlayer master at left
with None

"Ich schaue um die Ecke, bevor ich den nächsten Gang betrete. Die Regale sind voll mit Holzspielzeugen; von Spielzeugautos bis hin zu komplizierten Automaten."


show musicbox closed onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Ich bemerke eine kleine, einfache Holzschachtel, die hinter eine Reihe von Nussknackern versteckt ist, und hebe sie mit meiner freien Hand auf. Sie ist überraschend leicht."


show musicbox open onlayer master:
    ypos 0.5 alpha 1.0
with charachange

play music music_musicbox

"Eine kleine Bewegung reicht, um den Deckel der Spieldose zu öffnen. Im Inneren befindet sich ein kleiner Metallzylinder, der sofort anfängt, sich zu drehen."


"Sekundenlang stehe ich reglos und lausche der handtellergroßen Melodie."


"Während sie spielt, nehme ich das Preisschild zwischen die Finger und schaue darauf. Ich muss mich etwas anstrengen, die winzige Schrift zu lesen."


"Es ist erschwinglich… Mehr oder weniger."


show musicbox closed onlayer master
with charachange

play sound sfx_switch
stop music

show musicbox closed onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide musicbox onlayer master
with None

"Ich fasse mir ein Herz, schließe den Deckel, und mache mich mit der Puppe und der Spieldose auf den Weg zum Ladentisch."


show shopkeep surprised onlayer master at center
with charaenter

"Als ich die beiden Sachen auf dem Ladentisch lege, richtet sich der Mann dahinter auf und schätzt sie kritisch ab. Er kann seine Überraschung, dass jemand in meinem Alter so etwas kauft, nur schlecht verbergen."


show shopkeep thinking onlayer master
with charachange

"Es ist schmerzhaft, aber ich gebe ihm das Geld für meine Einkäufe und verlasse den Laden mit einer kleinen, undurchsichtigen Tasche in der Hand."


play ambient sfx_traffic fadein 0.5

scene bg city_street3 onlayer master
show hideaki serious onlayer master at center
with locationchange

"Ich bin überrascht zu sehen, dass Hideaki draußen steht."


hi "Oh… Hallo. Ich dachte, du wärst am Zeitungsstand."


show hideaki bored onlayer master
with charachange

hh "Akira hat mich angerufen. Sie und Lilly warten am Brunnen auf uns."


"Zumindest ist damit die Frage, wie wir die beiden wiederfinden sollen, beantwortet."


$ renpy.music.set_volume(0.4, 0.5, channel="ambient")

scene bg city_street2 onlayer master
with locationskip

"Wir machen uns auf den Weg zurück zum Brunnen. Hideakis tadellose Körperhaltung und sein Benehmen stehen in einem seltsamen Gegensatz zu seiner Aufmachung."


show lilly cane_reminisce_cas onlayer master at twoleft
show akira basic_boo onlayer master at tworight
with charaenter

"Lilly und Akira stehen dort und warten auf uns. Ihre Gesichtsausdrücke sind schwer zu lesen."


show akira basic_smile onlayer master at tworight
with charachange

aki "Hey. Bereit zum Aufbruch, Kurzer?"


show bg city_street2 onlayer master at bgleft
show lilly cane_reminisce_cas onlayer master at left
show akira basic_smile onlayer master at Transform(xpos=0.55)
with charamove

show hideaki happy onlayer master at right
with charaenter

"Hideakis Laune scheint sich zu verbessern, als er sich wieder Akira anschließt."


show hideaki happy_up onlayer master
with charachange

aki "Ciao Lilly, Hisao. Wünscht Hanako alles Gute zum Geburtstag von mir."


hi "Wird gemacht. Tschüss."


show lilly cane_weaksmile_cas onlayer master
with charachange

li "Auf Wiedersehen, Akira."


hide akira onlayer master
hide hideaki onlayer master
show lilly cane_reminisce_cas onlayer master
with charaexit

show lilly cane_reminisce_cas onlayer master at center
show bg city_street2 onlayer master at bgright
with charamove

"Und damit verschwinden die beiden im Gewühl der Menge."


"Ich drehe mich zu Lilly und merke, dass sie eine kleine Tasche trägt. Jetzt erkenne ich auch, dass etwas anders ist als vorher. Obwohl Lilly normalerweise ihre Emotionen nicht versteckt, sind ihre Miene und ihr Ton gerade schwer zu lesen."


"Es ist mehr als ein bisschen beunruhigend, aber in Anbetracht der Mühe, die sie sich gibt, ihre Gefühle zu verbergen, bezweifle ich, dass ich sie diesbezüglich mit Fragen bedrängen sollte."


hi "Hast du schon ein Geschenk für Hanako gekauft?"


show lilly cane_weaksmile_cas onlayer master
with charachange

li "Ja. Und du?"


hi "Ja."


show lilly cane_sleepy_cas onlayer master
with charachange

li "Sollen wir dann zurück zur Bushaltestelle gehen?"


hi "Okay. Es sollte bald ein Bus zurück nach Yamaku kommen."


"Und damit machen wir uns auf den Weg."


$ renpy.music.set_volume(0.7, 0.5, channel="ambient")

scene bg city_street1 onlayer master
show lilly cane_concerned_cas_close onlayer master at twoleft
with locationskip

"Im Vergleich zu vorher fühlt es sich merkwürdig an. Ich spüre Lillys ungewöhnlich angespannte Hand auf meinem Arm, und die Atmosphäre ist außergewöhnlich unangenehm."


"Das Schweigen setzt sich eine lange Zeit fort. Mir gefällt es wirklich nicht, sie so zu sehen."


show lilly cane_sleepy_cas_close onlayer master
with charachange

li "Wir müssen Hanakos Geburtstagsfeier etwas früher veranstalten. Wäre der Vierte in Ordnung für dich?"


"Da ich keinerlei andere Verpflichtungen habe, nicke ich reflexartig mit dem Kopf. Dann erinnere ich mich, dass eine solche Geste sinnlos ist, und beantworte ihre Frage auch noch mit Worten."


"Sie versucht, sich zu sammeln – eine Aufgabe, die fast mitleiderregend ist, denn es ist ziemlich deutlich, wie weit ihre Gedanken entfernt sind."


show lilly cane_weaksmile_cas_close onlayer master
with charachange

li "Es tut mir leid, Hisao. Du hast gesagt, dass der Bus bald kommen wird, nicht wahr?"


hi "Genau."


"Aber jetzt, wo sie das sagt, habe ich eine Idee."


hi "Hast du heute eigentlich noch etwas vor?"


show lilly cane_oops_cas_close onlayer master
with charachange

li "Ich… glaube nicht. Warum fragst du?"


hi "Das wäre normalerweise der Zeitpunkt, wo ich deine Hand nehme und dich irgendwohin bringe. Aber auch wenn ich das diesmal nicht mache, musst du mir vertrauen. Okay?"


show lilly cane_surprised_cas_close onlayer master
with charachange

"Ich nehme ihre Hand und führe sie vorsichtig zu unserem Ziel. Der abwesende Ausdruck auf ihrem Gesicht weicht einer Mischung aus milder Überraschung und Neugier."


stop ambient fadeout 2.0

scene bg city_karaokeint onlayer master
with shorttimeskip

$ renpy.music.set_volume(1.0, 10.0, channel="ambient")
play music music_another fadein 2.0

"Die Kellnerin stellt die Tasse Tee und die Tasse Kaffee, die ich bestellt habe, auf den Tisch. Ich bedanke mich bei ihr, bevor sie geht."


"Um ehrlich zu sein, hatte ich einfach nur Glück, dieses Café zu finden. Ich wusste nicht wirklich, wo ich hingehen sollte, und habe einfach nach einem Café gesucht, das einigermaßen nett aussah."


"Lilly hat sich inzwischen etwas erholt und kostet vorsichtig den Inhalt ihrer Tasse, während ich einen großen Schluck von dem Kaffee nehme, der vor mir steht."


"Wie erwartet erhellt sich ihr Gesicht, als sie erkennt, welcher Geschmack es ist."


show lilly basic_weaksmile_cas_close onlayer master at Transform(xalign=0.5, ypos=0.15, yanchor=0.0)
with charaenter

li "Mmm… das ist wunderbar!"


show lilly basic_surprised_cas_close onlayer master
with charachange

li "Hisao, woher hast du gewusst, dass…?"


"Ich habe französischen Schwarztee mit Vanillegeschmack bestellt und gehofft, dass es entweder ihre Lieblingssorte ist oder zumindest eine, die sie mag. Ich weiß nicht wirklich viel über Tee, aber es hörte sich so an, als wäre es das Richtige für sie."


"… weil sie Vanilleeis mag. Ich bin wirklich kein Teeconnoisseur."


hi "Es war nur gut geraten. Du trinkst wirklich gern Tee, oder?"


show lilly basic_smileclosed_cas_close onlayer master
with charachange

"Sie setzt ihre Tasse ab und nickt. Das vertraute, kleine Lächeln ist endlich wieder auf ihren Lippen zu sehen."


show lilly basic_smile_cas_close onlayer master
with charachange

li "Ich finde, dass Teetrinken… beruhigend ist."


hi "In Anbetracht deines Teekonsums, bist du sicher, dass du nicht süchtig bist? Koffeinsucht ist heutzutage ziemlich häufig."


show lilly basic_giggle_cas_close onlayer master
with charachange

li "Habe ich jemals das Gegenteil behauptet?"


"Sie kichert, während ich meinen Kopf senke. Wir haben wohl alle unsere Laster, und es gibt schlimmere Dinge, nach denen man süchtig sein kann."


hi "Französischer Schwarztee mit Vanillegeschmack, also? Das muss ich mir merken."


show lilly basic_smileclosed_cas_close onlayer master
with charachange

"Eine Weile lang trinken wir, ohne etwas zu sagen. Es ist beruhigend, jemanden wie sie in der Nähe zu haben, wenn man sich in einer fremden Umgebung befindet – selbst wenn wir beide nur schweigend zusammensitzen."


"Ich frage mich, ob sie das Gleiche empfindet, bis sie ihre Tasse absetzt."


show lilly basic_emb_cas_close onlayer master
with charachange

li "Hisao, darf ich dir eine etwas merkwürdige Frage stellen?"


hi "Das hängt von der Frage ab, glaube ich."


show lilly basic_weaksmile_cas_close onlayer master
with charachange

li "Ich habe mich gefragt… was deine Lieblingsfarbe ist. Schließlich hat jeder eine."


"Beinahe antworte ich, ohne zu merken, warum diese anscheinend banale Frage eigentlich ziemlich merkwürdig ist."


hi "Meine Lieblingsfarbe? Aber…"


show lilly basic_pout_cas_close onlayer master
with charachange

"Sie wirft mir einen schmollenden Blick zu. Obwohl die Antwort an sie zwangsläufig verschwendet scheint, möchte sie wohl, dass ich sie trotzdem gebe. Es schadet ja nicht."


hi "Ich habe schon immer Grün gerngehabt. Ich würde sagen, das ist meine Lieblingsfarbe."


show lilly basic_satisfied_cas_close onlayer master
with charachange

li "Grün, also? An was für Dinge denkst du, wenn du diese Farbe betrachtest?"


hi "Ich denke wohl an… Grasfelder und Bäume im Sommer. Und die Armee mit ihren Tarnanzügen."


show lilly basic_planned_cas_close onlayer master
with charachange

li "Männer scheinen immer das Militär zu lieben."


show lilly basic_smile_cas_close onlayer master
with charachange

li "Aber… es klingt wie eine schöne Farbe. Eine sehr schöne Farbe."


"Sie nickt leicht, als ob sie die Entscheidung für gut befindet. Wenn man bedenkt, wie fremdartig das Konzept von Farben für sie ist, ist es wohl sinnvoll, sie nach Assoziationen zu beurteilen."


hi "Wenn jeder eine Lieblingsfarbe hat, was ist dann deine?"


show lilly basic_smileclosed_cas_close onlayer master
with charachange

li "Weiß. Ich habe gehört, dass das die Farbe von Schnee und Eiscreme ist."


hi "Du bist nicht viel besser als ich, wenn du diese Farbe nur wegen einer Lieblingsspeise gern hast. Aber ich denke, Weiß ist auch schön."


hi "Und da wir gerade von Farben reden – es wird bald dunkel. Lass mich dir beim Aufstehen helfen."


show lilly basic_smile_cas_close onlayer master
with charachange

show lilly basic_smile_cas_close onlayer master at center
with charamove

"Lilly bietet mir ihre Hand an, und ich nehme sie in meine, um ihr hochzuhelfen. Die Sanftheit ihrer Hand im Vergleich zu meiner überrascht mich. Ich bin diese Art von beiläufigem Körperkontakt wirklich nicht gewöhnt."


"Es scheint sie aber nicht wirklich zu stören. Obwohl der Grund dafür offensichtlich scheint, wirkt sie dadurch nur noch damenhafter als ohnehin schon."


"Als ihre Hand in Richtung ihrer Tasche wandert, halte ich sie davon ab."


hi "Keine Sorge. Ich zahle."


show lilly basic_cheerful_cas_close onlayer master at center
with charachange

li "Oh. Danke, Hisao."


"Sie reagiert auf die Geste mit einem ehrlichen Lächeln – eine Belohnung, die viel größer ist als ihre Worte."


stop music fadeout 2.0

scene bg suburb_roadcenter_ni onlayer master
with shorttimeskip

$ renpy.music.set_volume(0.2, 0.5, channel="ambient")
play ambient sfx_cicadas fadein 0.5

"Als wir aus dem Bus aussteigen, ist es vollkommen dunkel."


$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

scene bg school_road_ni onlayer master
with locationskip

"Wir steigen gemeinsam den Hügel hinauf. Die etwas peinliche Stille zwischen uns ist wahrscheinlich auf die Ereignisse des Tages zurückzuführen."


"Obwohl Lillys Verschlossenheit nach dem Treffen mit ihrer Schwester mir immer noch Sorgen macht, empfinde ich die Tatsache, dass es mir gelungen ist, sie ein bisschen aufzumuntern, als einen persönlichen Triumph."


"Aber… es fühlt sich so an, als ob sich die Atmosphäre zwischen uns verändert hat. Es mag nicht viel sein, aber es ist etwas, was keinem von uns bis jetzt aufgefallen ist."


show lilly cane_weaksmile_cas_ni onlayer master at center
with charaenter

li "Das war… ein Date, nicht wahr?"


"Das war es. Das ist uns beiden bewusst. Die Antwort ist so offensichtlich, dass die Frage praktisch rhetorisch ist."


"So peinlich das Gefühl auch ist, glaube ich nicht, dass es etwas Schlechtes ist. Ganz im Gegenteil. Ich weiß nicht, was es ist und kann mir auch nicht sicher sein, aber es fühlt sich an, als wäre es etwas mehr als nur Freundschaft."


"Verständnis? Mitgefühl? Die Suche nach Worten, die es angemessen beschreiben können, ist schwierig. Trotzdem…"


hi "Möchtest du das irgendwann noch einmal machen, Lilly? Ohne Geschenke einzukaufen?"


show lilly cane_emb_cas_ni onlayer master
with charachange

"Die vorsichtige Frage wird von Lilly mit dem gleichen Blick wie vorhin beantwortet."
"Ihre blasse Haut macht die rosige Farbe ihrer Wangen nur noch deutlicher, und obwohl ihr Gesicht immer noch in Richtung der vor ihr liegenden Straße zeigt, senkt sie es, wenn auch nur ein bisschen."


show lilly cane_cheerful_cas_ni onlayer master
with charachange

li "… Okay."


stop ambient fadeout 2.0

scene black onlayer master
with dissolve




label de_L4:

scene bg school_girlsdormhall onlayer master
with locationchange

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

"Mit der Schultasche in der Hand gehe ich den Flur des Mädchenwohnheims entlang."





"Wenn ich es mir recht überlege, ist diese ganze Situation seltsam."


"Obwohl ich über Hanakos kommende Geburtstagsfeier schon eine Zeit lang Bescheid wusste, hatte ich überhaupt keine Idee, wo die Feierlichkeiten stattfinden würden, bis ich heute einen Zettel in dem verlassenen Teeraum fand."


"Ich hole den Zettel hervor und lese ihn noch einmal, um die Anweisungen zu überprüfen. Trotz Lillys Blindheit ist die einfache, schwarze Handschrift ziemlich leserlich, was ihrer beachtlichen Sorgfalt und Mühe zu verdanken ist."


window hide

$ written_note(u"Hisao,\n\nWir werden eine Feier bei mir veranstalten. Bitte komm um 18 Uhr ins Zimmer 225 im Mädchenwohnheim. \nEs tut mir Leid, dass ich dich wegen meiner Pflichten als Klassensprecherin auf diese Weise darüber benachrichtigen musste.\n\n- Lilly Satou", text_args={"color":"#000000"})


window show

"Zögernd gehe ich den Gang entlang, bis ich vor Lillys Zimmer stehe. Ich zögere eine weitere Sekunde, klopfe aber schließlich dreimal kurz an die Tür."


play sound sfx_doorknock2
with Pause(0.5)

"Ein kurzer, dumpfer Wortwechsel findet auf der anderen Seite der Tür statt. Als ich genauer hinhöre, kann ich Hanakos und Lillys Stimmen gerade noch erkennen."


"Als das Gespräch endet, fragt Lilly durch die Tür."


li "Bist du es, Hisao?"


hi "Ja. Ich hab deine Nachricht gekriegt."


li "Du kannst reinkommen, die Tür ist offen."


"Froh, dass ich das richtige Zimmer erwischt habe, drücke ich die Türklinke nach unten und betrete das Zimmer."


play sound sfx_dooropen

"Als die Tür aufschwingt, bleibt mir mein Gruß im Hals stecken."


window hide

play music music_one fadein 10.0

scene ev lilly_bedroom onlayer master:
    truecenter
    zoom 1.1 subpixel True
    ease 15.0 zoom 1.0
with GenericWhiteout(0.5,0.1,4.0)

window show

"Lilly sitzt in ihrem Pyjama an einem niedrigen Tisch in der Mitte des Zimmers. Hanako trägt ein Nachthemd und sitzt ihr gegenüber. Da ich meine normale Schulkleidung anhabe, fühle ich mich ziemlich fehl am Platz."


"Für einen Moment genieße ich den Anblick der beiden Mädchen. Es gelingt mir nur mit Mühe, meinen Blick von Lillys langen, dünnen und blassen Beinen loszureißen."


hi "H-Hallo. Ich… glaube, dass ich alles mitgebracht habe, was wir brauchen."


scene ev lilly_bedroom_large onlayer master:
    xpos -130 ypos -400 subpixel True
    acdc_warp 12.0 ypos -800
with flash

"Sie lächelt und nickt. Ich frage mich, ob ihr überhaupt bewusst ist, was für einen angenehmen Anblick sie bietet. Die dünne, blaue Seide ihres Nachthemds steht ihr wirklich gut und hebt sowohl ihre Augen als auch ihre Kurven hervor."


"Ihre zögernde, fast schüchterne Haltung von gestern Abend ist ihrem neckischen Charakter gewichen. Es ist schön zu sehen, dass ihr Selbstvertrauen zurückgekehrt ist, aber ich denke immer wieder daran, wie sie ausgesehen hat."


scene ev lilly_bedroom_large onlayer master:
    xpos -830 ypos -200 subpixel True
    acdc_warp 12.0 ypos 0
with flash

"Ich schaue zu Hanako, die ihr nervös gegenüber sitzt. Dass sie etwas so Konservatives wie ein Nachthemd trägt, ist nicht überraschend, es sieht aber definitiv niedlich aus."


hi "Hallo, Hanako. Alles Gute zum Geburtstag."


ha "Äh… d-danke."


"Sie ist ungewöhnlich scheu, obwohl sie sonst in meiner Gegenwart recht entspannt ist, nachdem wir uns nun schon seit ein paar Wochen kennen. Es liegt wohl an der außerordentlichen Situation."


scene ev lilly_bedroom onlayer master
with flash

li "Du kannst dich ruhig hinsetzen, Hisao. Ich werde euch beiden Tee einschenken."


hi "Geht klar."


$ renpy.music.set_volume(0.8, 2.0, channel="music")

scene bg school_dormlilly onlayer master
with locationchange

"Lilly nimmt die dampfende, rote Teekanne von der Tischseite und gießt langsam den Inhalt in unsere Teetassen. Ich setze mich neben sie und stelle meine Tasche gegen die nahe Wand."


"Jetzt, wo ich wieder zu Sinnen gekommen bin und meine Hormone sich beruhigt haben, merke ich, dass ich zum ersten Mal in Lillys Zimmer bin."


"Das Erste, was mir auffällt, ist der Geruch, der sich von dem in meinem Zimmer leicht unterscheidet – wahrscheinlich Parfum oder Nagellack… Irgendetwas Mädchenhaftes eben."


"Als nächstes fällt mir auf, wie schlicht es optisch ist. Beige Wände, ein eleganter aber schlichter Schrank, keine Poster oder Wandbehänge… Alles ist deutlich nutzenorientiert – etwas was ich angesichts ihrer Blindheit hätte erwarten sollen."


"Das Einzige, was wirklich ungewöhnlich ist, sind mehrere Bücherstapel, die auf dem Boden liegen und von Knie- bis auf Taillenhöhe reichen. Manche haben aufgedruckte Titel, aber andere sind, mit der Ausnahme von Braille, gänzlich blank."


"Dass die Bücher mit aufgedruckten Titeln einheitlich Englisch sind, ist interessant, aber nicht komplett unerwartet. Sie hat ja schließlich erwähnt, dass ihre Eltern Akira und sie mit der Sprache vertraut machen wollten."


hi "Dein Zimmer sieht schön aus, Lilly."


show hanagown distant onlayer master:
    center
    ypos 1.15
with charaenter

"Ich höre ein paar dankende Worte von neben meiner Schulter. Als ich zurück zu Hanako blicke, fällt mir auf, dass sie ihren Blick auf ihrem Schoß richtet und ihr Nachthemd mit ihren Händen nervös festhält."


"Erst jetzt merke ich warum. Mit ihrer gegenwärtigen Kleidung ist das Ausmaß ihrer Narben weit sichtbarer; sie gehen ihren Hals entlang und bedecken ihre rechte Schulter."


"Obwohl wir diese Feier für sie veranstalten, kriege ich den Eindruck, dass sie es nicht wirklich genießt, jetzt wo ich hier bin."


hi "Also, wie alt wirst du jetzt? Achtzehn?"


show hanagown worry onlayer master
with charachange

"Ihr überraschter Blick und ihre völlige Unfähigkeit, ihre Gefühle zu verbergen, zeigen, dass sie versucht hat, mich geistig zu ignorieren. Diese Situation ist wirklich ziemlich peinlich."


ha "J-Ja."


hi "Auf der positiven Seite bleiben dir nur noch zwei Jahre, bis du Alkohol trinken darfst. Also, wer ist älter? Du oder Lilly?"


show hanagown normal onlayer master
with charachange

ha "Lilly. Sie hatte ihren Geburtstag im… F-Februar. Was ist mit… deinem?"


hi "Früher in diesem Jahr, er ist also schon vorbei."


"Ich erwähne nicht, dass ich meinen Geburtstag im Krankenhaus verbracht habe. Das war… ein besonderer Tiefpunkt des Aufenthalts."


show hanagown distant onlayer master
with charachange

show hanagown distant onlayer master:
    tworight
    ypos 1.15
show bg school_dormlilly onlayer master at bgright
with charamove

show lilly basic_smileclosed_paj onlayer master:
    twoleft
    ypos 1.2 
with charaenter

play sound sfx_teacup

"Wie erwartet ebbt unser Gespräch schnell ab. Es dauert nicht lange, bis Lilly unsere Getränke fertig hat und die drei Teetassen vor uns absetzt."


"Ich hebe meine Tasse auf und merke sofort, dass der Tee viel stärker duftet und schmeckt als der, den wir normalerweise trinken."


hi "Hmm, er schmeckt anders als der Tee, den wir in der Schule haben."


show lilly basic_smile_paj onlayer master
with charachange

li "Es ist eine andere Sorte, als der, den wir dort trinken. Hast du noch nie zuvor Orange Jaipur probiert?"


hi "Nicht… das ich wüsste. Immerhin trinke ich normalerweise Kaffee, so wie ich es während unseres Stadtbesuchs gemacht habe. Das schmeckt aber auch gut."


show hanagown normal onlayer master
with charachange

"Als wir anfangen zu trinken, scheint Hanako sich etwas zu entspannen – oder zumindest ist sie meinetwegen etwas weniger nervös."


"Wir leeren etwa zeitgleich unsere Tassen. Hanako versucht vergeblich, nicht andauernd auf den Kuchen zu schielen, der neben dem Tisch steht und praktisch darum bettelt, vernascht zu werden."


stop music fadeout 4.0

"Wenn ich es mir recht überlege, dann bin ich selbst ziemlich scharf darauf. Aber eins nach dem anderen."


hi "Lilly?"


show lilly basic_planned_paj onlayer master
with charachange

li "Ja, das ist eine gute Gelegenheit."


"Wir beide wissen, was der andere meint. Ich lehne mich zur Seite und grabe in meiner Tasche nach der Puppe, die ich Hanako gekauft habe, während Lilly aufsteht und ihr Geschenk holt."


"Wir verstecken unsere Geschenke in unseren Händen und stellen sie gleichzeitig auf dem Tisch."


show lilly basic_cheerful_paj onlayer master
show hanagown normal_blush onlayer master
with charachange




"Vor Überraschung gelähmt sitzt Hanako schweigend da und schaut sie sekundenlang an."


"Meine kleine Holzpuppe, komplett mit dem viktorianischen Kleid und einem Hut, liegt neben einem hellbraunen, flauschigen Stoffbären von Lilly."


show hanagown distant onlayer master
with charachange

"Sie greift nach ihrem Nachthemd und setzt an zu sprechen, nimmt aber ihren Blick nicht von unseren bescheidenen Geschenken."


show hanagown distant_blush onlayer master
with charachange

ha "D-Danke… Lilly und… Hisao…"


play music music_serene fadein 6.0

scene unlock_ev lilly_hanako_hug_end onlayer master
show black onlayer master
show ev lilly_hanako_hug onlayer master:
    xalign 0.5 yalign 1.0 alpha 0.0 subpixel True
    parallel:
        linear 5.0 alpha 1.0
    parallel:
        easein 15.0 yanchor 0.0 ypos -0.15

with locationskip

"Der Ton ihrer Stimme fängt an, sich zu verändern, als Lilly sich nach vorne beugt und sie sanft umarmt."


"Zu sehen, wie Hanako Lilly so fest umarmt, ist so herzerwärmend, dass ich nicht aufhören könnte zu lächeln, selbst wenn ich wollte."


"Während Lilly ihr Gesicht an Hanakos Kopf lehnt, spricht sie in einem Ton so leise, dass ich sie kaum hören kann."


li "Herzlichen Glückwunsch zum Geburtstag, Hanako."


hi "Alles Gute zum Geburtstag."


"Hanako nickt leicht und hält Lilly eine Zeitlang fest, bevor sie sich von ihr trennt und eine Träne wegwischt."


"Ich nehme an, dass für Hanako die einfache Anwesenheit von irgendjemand, der sie liebt und für sie da ist, besonders ist. Die Tatsache, dass Lilly und ich für sie diese Rolle teilen können, ist etwas, wofür ich immer dankbar sein werde."


scene ev hanako_presents1 onlayer master
with locationskip

"Hanako nimmt die Puppe und den Teddybären zärtlich in die Arme und hält sie gegen ihre Brust, während sie herzlich lächelt."


"Für eine lange Zeit sitzen wir drei in fröhlicher Stille zusammen. Die Ruhe bleibt ununterbrochen, bis Lilly mit sanfter Stimme einen Vorschlag macht."


li "Wollen wir dann den Kuchen anschneiden?"


scene bg school_dormlilly onlayer master
show lilly basic_smile_paj onlayer master:
    twoleft
    ypos 1.2
show hanagown smile onlayer master:
    tworight
    ypos 1.15
with locationskip

"Ihr Vorschlag wird mit zwei erwartungsvollen Blicken beantwortet."


hi "Ich habe nichts dagegen."


ha "Okay."


stop music fadeout 2.0

scene bg school_dormlilly onlayer master
show lilly basic_smileclosed_paj onlayer master:
    twoleft
    ypos 1.2
show hanagown normal onlayer master:
    tworight
    ypos 1.15
with shorttimeskip

hi "Puh, das war lecker."


play music music_dreamy fadein 4.0

"Ich lehne mich zufrieden zurück. Lilly und Hanako scheinen mit dem Essen genauso zufrieden zu sein wie ich. Wir mussten uns etwas anstrengen, haben aber den gesamten Kuchen auf einmal gegessen."


show hanagown normal_blush onlayer master
with charachange

ha "Ich glaube nicht, dass ich noch mehr essen könnte."


show lilly basic_weaksmile_paj onlayer master
with charachange

li "Ich denke, dass ich nächstes Mal einen kleineren Kuchen kaufen werde."


show hanagown smile onlayer master
with charachange

"Hanako und ich lachen, aber ich muss daran denken, dass wir nächstes Jahr um diese Zeit schon unseren Abschluss gemacht haben werden."


"Diese Realität ist etwas deprimierend, da ich endlich das Gefühl kriege, dass in meinem Leben langsam eine Art von Ordnung zurückkehrt."


"Als ich mich in Lillys sauberen und ordentlichen Raum umsehe, fallen mir ihre Bücher wieder auf."


"Das mag vielleicht ein wenig ungestüm sein, aber meine Neugier geht mit mir durch. Ich glaube, dass es ihr ohnehin nichts ausmachen wird."


hi "Hey Lilly, hättest du was dagegen, wenn ich mir eins deiner Bücher anschaue?"


show lilly basic_smile_paj onlayer master
with charachange

li "Das darfst du gerne tun, Hisao."


show lilly basic_planned_paj onlayer master
with charachange

li "Aber wenn du zwei Sprachbarrieren überwinden kannst, bin ich sehr beeindruckt."


hi "Zwei? Braille und… ach ja, Englisch."


show lilly basic_smile_paj onlayer master
with charachange

"Sie nickt."


hi "Ich wusste, dass du Englisch studierst, aber ich bin immer noch erstaunt, wie gut du darin bist."


show lilly basic_giggle_paj onlayer master
with charachange

li "Man könnte sagen, es ist die perfekte Methode, um zu verhindern, dass sich Leute meine Büchersammlung ausleihen."


"Sie sagt es im Scherz, aber ich bin ein wenig enttäuscht. All diese Bücher um mich herum und keine Möglichkeit, sie zu lesen… Es ist, als wollte sie mich quälen."


"Hanako kichert leise, während ich nach dem nächstgelegenen Stapel greife, und nach einem flüchtigen Blick das oberste Buch nehme."
"Auf dem Buchdeckel steht der Titel in großen Buchstaben: „Tod auf dem Nil”. Es ist der einzige gedruckte Text, der zu sehen ist."


$ renpy.music.set_volume(0.5, 0.5, channel="music")
play sound sfx_paper
show ev braille onlayer master at Fullpan(10.0, dir="right")
with locationskip

"Während Lilly und Hanako sprechen, setze ich mich für eine Weile mit dem geöffneten Buch auf meinem Schoß hin."


"Auch wenn ich mich sehr bemühe, die Braille-Pünktchen auf jeder Seite zu ertasten, scheinen sie ineinander überzugehen und zu verschwimmen."


"Ich dachte, dass es viel einfacher sein würde, als es eigentlich ist. Trotzdem kann ich sehen, wie jemand mit einiger Übung und einem empfindlicheren Tastsinn als meinem ziemlich schnell lesen könnte."


$ renpy.music.set_volume(1.0, 0.5, channel="music")

scene bg school_dormlilly onlayer master
show lilly basic_smileclosed_paj onlayer master:
    twoleft
    ypos 1.2
show hanagown normal onlayer master:
    tworight
    ypos 1.15
with locationskip

"Plötzlich bemerke ich eine Stille, die wahrscheinlich schon früher begonnen hat. Ich schaue von den gepunkteten Seiten auf und sehe, wie Lilly mich anlächelt, während Hanako an einer weiteren Tasse Tee nippt."


hi "Stimmt etwas nicht?"


show lilly basic_smile_paj onlayer master
with charachange

li "Ganz im Gegenteil. Deine Neugier ist recht liebenswert."


"Ich bin von dem Lob ziemlich erfreut und fühle, wie meine Wangen ein wenig warm werden."


hi "Danke, aber ich kann einfach nicht anders."


show lilly basic_weaksmile_paj onlayer master
with charachange

li "Um ehrlich zu sein, war ich mir nicht gänzlich sicher, wie du über uns denkst, weil du von einer anderen Schule hierher gewechselt bist."


stop music fadeout 12.0

show lilly basic_reminisce_paj onlayer master
with charachange

li "Wenn du uns bemitleidet hättest, wäre ich schwer beleidigt gewesen."


show hanagown distant onlayer master
with charachange

"In Lillys Stimme liegt eine gewissen Schärfe, die ich am ehesten als Stolz einordnen würde. Ich sehe zu Hanako hinüber. Sie wirkt noch stiller als sonst und schaut in Lillys Richtung statt in meine."


hi "Darüber würde ich mir keine Sorgen machen. Wenn man bedenkt, in welcher Lage ich mich befinde, bin ich so ziemlich der Letzte, die andere bemitleiden sollte."


hi "Die ersten Reaktionen meiner Eltern nach meinem Herzanfall… Niemand sollte so einen Gesichtsausdruck jemals zu sehen bekommen."


show lilly basic_oops_paj onlayer master
show hanagown distant_blush onlayer master
with charachange

"Ich beiße mir auf die Zunge, bevor ich weiterreden kann, aber es ist schon zu spät. Beide Mädchen scheinen unangenehm berührt zu sein, besonders Lilly."


show lilly basic_emb_paj onlayer master
show hanagown worry onlayer master
with charachange

li "Es… tut mir leid. Ich hätte nicht so weit gehen sollen…"


show lilly basic_listen_paj onlayer master
with charachange

$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_doorknock2

"Einige Sekunden lang herrscht ein peinliches Schweigen. Glücklicherweise nimmt die Stille ein Ende, als Lilly den Kopf hebt. Es ist eine Geste, deren Bedeutung ich inzwischen erkenne."


hi "Hörst du etwas?"


show lilly basic_surprised_paj onlayer master
with charachange

li "Die Tür…"


$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_dooropen

show lilly basic_surprised_paj onlayer master:
    left
    ypos 1.2
show hanagown distant_blush onlayer master at Transform(xpos=0.4)
show bg school_dormlilly onlayer master at bgleft
with charamove

"Da wir alle Lillys Sinnen vertrauen, blicken wir in Richtung Tür. Tatsächlich bewegt sich der Türgriff, und eine gelb-schwarze Gestalt schlüpft durch die Türspalte."


show akira basic_laugh onlayer master at right
with easeinright

play music music_running

show lilly basic_listen_paj onlayer master
show hanagown worry onlayer master
with vpunch

aki "Akira Satou ist eingetroffen! Alles Gute zum Geburtstag, Hanako!"


show hanagown worry_blush onlayer master
with charachange

ha "Äh… danke…"


show akira basic_smile onlayer master at Transform(ypos=1.15, xpos=0.8, xanchor=0.5)
with dissolvecharamove

"Akira nimmt am Tisch platz und lässt ihre große Tasche auf den Boden neben sich plumpsen. Sie ist wie immer sehr ungestüm und macht aus ihrem Auftritt fast ein Ereignis."


show hanagown distant onlayer master
with charachange

"Hanako verkrampft sich im ersten Moment etwas, scheint aber nicht sonderlich überrascht zu sein und beruhigt sich schnell wieder."
"Ich nehme an, dass sie Akira schon öfter getroffen hat – keine große Überraschung, wenn man bedenkt, wie nahe sich Akira und Lilly stehen."


"Trotz der Auffälligkeit von Hanakos Narben scheint Akira sich kein bisschen daran zu stören. Andererseits mäßigt sie auch nicht ihr Verhalten, obwohl Hanako von Natur aus schüchtern ist."


show lilly basic_weaksmile_paj onlayer master
with charachange

li "Akira, ich dachte, du hättest gesagt, dass du arbeiten musst. Ist es dir gelungen, einige Zeit freizunehmen?"


show akira basic_boo onlayer master:
    ypos 1.15
with charachange

aki "Na ja, irgendwie schon. Ich habe ein schlechtes Gewissen, dass ich meine Kollegen allein Überstunden machen lasse, also muss ich bald zurück."


show akira basic_smile onlayer master
with charachange

aki "Aber ich hätte auch ein schlechtes Gewissen gehabt, wenn ich nicht zu Hanakos Geburtstagsfeier gekommen wäre, also bin ich vorerst hier."


show hanagown smile onlayer master
with charachange

"Sie grinst Hanako breit an, die stark errötet und ihren Blick nach unten in ihren Schoß richtet. Ihr Mund scheint wiederholt breiter und wieder schmaler zu werden, als ob sie versucht, aus Verlegenheit ein Lächeln zu unterdrücken."


"Ihr Versuch, ihre Dankbarkeit zu verbergen, scheitert größtenteils."
"Alles, was sie fertigbringt, ist ein kleines Kopfnicken, aber in Situationen, wo sie sich für ihr Aussehen schämt, versteckt sie sich immer hinter einem Buch. Im Vergleich dazu ist diese Reaktion richtig extrovertiert."


"Ich nehme an, dass wenige Leute Hanako positive Aufmerksamkeit schenken und bewundere, wie geschickt Akira mit ihr umgeht, dass sie so glücklich aussieht. Im Vergleich dazu habe ich herzlich wenig leisten können."


show akira basic_laugh onlayer master
with charachange

aki "Nun, bevor ich gehen muss…"


play sound sfx_rustling

"Sie greift in die Tasche neben sich, nimmt den Inhalt heraus, und präsentiert ihn mit einer großen Geste."


show wine onlayer master:
    yalign 0.5 xanchor 0.0 xpos 1.0 alpha 0.0
    easein 1.0 alpha 1.0 xanchor 1.0
with Pause(1.0)

"Zwei große Glasflaschen mit langen, französischen Namen auf den Etiketten."


show hanagown normal onlayer master
with charachange

"Hanakos Miene ist eine seltsame Mischung aus Überraschung und Neugier, und ich ahne, dass ich denselben Gesichtsausdruck habe wie sie. Lilly, die die Geschehnisse nicht wahrnehmen kann, tappt wortwörtlich im Dunkeln."


show hanagown normal_blush onlayer master
with charachange

ha "Akira… das ist doch nicht…"


show lilly basic_surprised_paj onlayer master
with charachange

li "Was ist es?"


hi "Wein. Ein roter und ein weißer."


show lilly basic_pout_paj onlayer master
with charachange

li "A-Akira! Das ist…!"


show akira basic_smile onlayer master
with None

show wine onlayer master:
    easeout 1.0 alpha 0.0 xanchor 0.0
with Pause(1.0)

hide wine onlayer master
with None

aki "Nur die Ruhe. Es ist ja nicht so, als wäre Shizune hier, um euch auszuschimpfen."


hi "Lilly hat irgendwie Recht. Das ist auf dem Schulgelände nicht wirklich erlaubt."


hi "… oder überhaupt irgendwo. Hast du vergessen, dass wir noch nicht alt genug sind, um Alkohol trinken zu dürfen?"


show akira basic_laugh onlayer master
with charachange

aki "Das sind starke Worte für jemanden, der beim Anblick der Flasche in seiner Hand beinahe anfängt zu sabbern."


"Da hast sie mich erwischt. Zumindest ein bisschen würde ich wirklich gerne probieren. Und obwohl Hanako noch keine Flasche in der Hand hält, verrät ihr Gesichtsausdruck, dass sie die Idee nicht gerade ablehnt."


show lilly basic_displeased_paj onlayer master
with charachange

"Lilly reibt sich die Stirn. Sie fängt gar nicht erst an zu diskutieren, weil Akira sowieso gewinnen würde, da ihr diese komischen „Regeln” und „Vorschriften” einfach egal sind."


show lilly basic_displeased_paj onlayer master
with charachange

li "Ich flehe dich an: Bitte sag niemandem an dieser Schule auch nur ein Sterbenswörtchen davon."


show akira basic_smile onlayer master
with charachange

aki "Keine Sorge, ich bin doch nicht bescheuert."


show akira basic_boo onlayer master
with charachange

aki "Und damit muss ich mich leider von euch verabschieden. Ich muss bald zurück auf der Arbeit sein."


show lilly basic_oops_paj onlayer master
with charachange

li "Du musst schon weg? Aber du bist doch gerade erst gekommen…"


show akira basic_resigned onlayer master
with charachange

aki "Tut mir Leid, Lilly. Es war schön, euch beide wiederzusehen. Dich auch, Hisao."


hi "Dann bis später."


ha "Ähm… a-auf Wiedersehen… Akira…"


show akira basic_resigned onlayer master at Transform(yalign=1.0)
with charamove

hide akira onlayer master
with charaexit

"Sie steht mit einem Grunzen auf und schlüpft aus dem Zimmer. Und plötzlich sind wir allein mit den beiden Gegenständen auf dem Tisch."


show lilly basic_oops_paj onlayer master:
    twoleft
    ypos 1.2
show hanagown normal_blush onlayer master:
    tworight
    ypos 1.15
show bg school_dormlilly onlayer master at center
with charamove

hi "… Interessant."


show lilly basic_arablush_paj onlayer master
show hanagown normal onlayer master
with charachange

"Während die Eskapaden ihrer Schwester ein nervöses Kichern bei Lilly verursachen, nimmt Hanako eine Weinflasche."


show hanagown distant_blush onlayer master
with charachange

ha "Also…"


hi "Was denkst du, Lilly?"


show lilly basic_weaksmile_paj onlayer master
with charachange

"Sie stützt ihren Ellenbogen auf den Tisch und kneift ihre Nasenwurzel, während sie unsere Lage gründlich durchdenkt. Anscheinend kann sie mit ihrer Schwester wirklich nicht mithalten."


show lilly basic_smile_paj onlayer master
with charachange

stop music fadeout 3.0

li "Na ja… Jetzt sind sie schon hier. Da können wir auch etwas davon probieren."


"Kaum hat sie es gesagt, sehe ich mich im Zimmer um, um Gläser zu finden."


scene bg school_dormlilly_ni onlayer master
with shorttimeskip

play music music_night fadein 0.5

"Ein leises Stöhnen über meinem Kopf erinnert mich, dass Lilly sich vor ein paar Minuten ins Bett zurückgezogen hat, um sich etwas auszuruhen."


"Obwohl ich fast völlig erschöpft bin, gelingt es mir aufzustehen. Ich schleppe mich bis zum Bett, setze mich hin und lehne mich mit dem Rücken dagegen."


show bg school_dormlilly_ni as ovl1 onlayer master:
    xalign 0.5 alpha 0.4 yalign 0.5 zoom 1.0
    ease 1.0 xalign 0.55 alpha 0.5 rotate 1 zoom 1.05
    ease 1.0 xalign 0.5 yalign 0.5 alpha 0.0 rotate 0 zoom 1.0

show bg school_dormlilly_ni as ovl2 onlayer master:
    xalign 0.5 alpha 0.4 yalign 0.5 zoom 1.0
    ease 1.0 xalign 0.45 alpha 0.5 rotate -1 zoom 1.05
    ease 1.0 xalign 0.5 yalign 0.5 alpha 0.0 rotate 0 zoom 1.0

hi "Oh Gott."


show lilly basic_listen_paj_ni onlayer master:
    center
    ypos 1.2
with charaenter

li "Auweia…"


"Lilly stöhnt erschöpft auf."


hi "Zu viel getrunken?"


show lilly basic_concerned_paj_ni onlayer master
with charachange

li "Mein Kopf tut weh."


hi "Jepp, zu viel getrunken."


"Ich lege den Kopf in den Nacken und starre stumpf die Decke an. Was für eine absolute Katastrophe."


"Wie richtige Idioten haben wir den ganzen Abend ein Glas nach dem anderen leergetrunken. Hanako ist einfach zur Seite gefallen und eingeschlafen, und es ist ein Wunder, dass ich mich nicht so schlecht fühle wie Lilly."


show lilly basic_sad_paj_ni onlayer master
with charachange

li "Hey, Hisao? Tut mir leid wegen heute. Ich… dachte nicht, dass das passieren würde."


hi "Schon gut, Lilly. Um die Wahrheit zu sagen, habe ich heute viel Spaß gehabt."


show lilly basic_weaksmile_paj_ni onlayer master
with charachange

li "Wirklich?"


hi "Mmm. Ich glaube, Hanako ging es genauso. Nein, ich bin mir sicher."


show lilly basic_reminisce_paj_ni onlayer master
with charachange

"Nach einer kurzen Stille stöhnt die auf ihrem Rücken liegende Lilly wieder laut auf."


hi "Bist du okay?"


show lilly basic_weaksmile_paj_ni onlayer master
with charachange

li "Wie du schon gesagt hast, habe ich einfach zu viel getrunken. Wie spät ist es?"


hi "Wie spät? Äh, es ist…"


"Ich werfe einen schnellen Blick auf meine Armbanduhr. Ihre Ziffern sind in der Dunkelheit kaum lesbar."


hi "… ungefähr Mitternacht."


show lilly basic_concerned_paj_ni onlayer master
with charachange

li "Die Ausgangssperre ist also in Kraft."


hi "Ja, das habe ich mir schon gedacht. Wir müssen also alle hier übernachten."


"Kaum habe ich die Worte ausgesprochen, höre ich, wie Lilly versucht, aufrecht zu sitzen."


show lilly basic_oops_paj_ni onlayer master
with charachange

li "Hanako…"


hi "Äh, nein, schlaf weiter. Versuch nicht aufzustehen."


show lilly basic_displeased_paj_ni onlayer master
with charachange

li "Hisao, ich muss…"


hi "Deine Verfassung ist weit schlechter als meine. Ruh dich aus."


show lilly basic_oops_paj_ni onlayer master
with charachange

li "Aber was ist mit…"


hi "Ich werde ein paar zusätzliche Decken über sie legen. Mach dir keine Sorgen."


hide lilly onlayer master
with charaexit

"Während ich tief gähne und aufstehe, um die Decken zu holen, höre ich, wie Lilly sich mit einem sanften Plumps wieder hinlegt."


li "Danke, Hisao."


hi "Kein Problem. Es ist das Mindeste, das ich tun kann. Du siehst absolut stockbesoffen aus."


li "Ich bin nicht… voll… nur ein bisschen… müde."


"Sie beginnt zu schmollen und wegen des Alkoholeinflusses fängt ihre Sprache an, undeutlich zu werden. Ich schnappe mir ein paar zusammengerollte Decken, die sich am Ende ihres Bettes befinden."


"Ich bewege mich leise auf Hanako zu, lege die Decken vorsichtig auf ihre friedlich schlafende Gestalt und passe auf, dass ich sie nicht aufwecke."


"Angesichts des starken Alkoholgeruchs in ihrem Atem bezweifele ich jedoch, dass sie aufwachen würde, ganz egal, was ich mache."


"Ich stehe auf und betrachte den Raum ein letztes Mal."


stop music fadeout 4.0

"Ein Junge verbringt die Nacht mit zwei völlig betrunkenen Mädchen im Mädchenwohnheim. Wenn davon jemand Wind kriegen würde, wäre es ein Riesenskandal."


"Während ich mich in Richtung des Bettes bewege, um mich wieder hinzusetzen, werfe ich einen letzten, heimlichen Blick auf Lilly."


"Ihre ausgestreckte, zerzauste Gestalt liegt – etwas zur Seite gedreht – friedlich im Bett."


"Ich gehe in die Hocke, um besser sehen zu können."


play music music_comfort

scene ev lilly_sleeping onlayer master:
    truecenter zoom 1.05 subpixel True
    acdc_warp 20.0 zoom 1.0
with locationchange

"Ihre weiße Haut hebt sich kaum von dem weißen Kissen ab; ihr Gesicht sieht im Schlaf ganz friedlich aus."


"Normalerweise ist sie so selbstsicher und direkt. Sie passt auf Hanako auf und ist immer für sie da – aber jetzt wirkt sie richtig zerbrechlich."


"Ich denke an Hanakos Geschenke zurück."


"Ich dachte, dass es ein schöner Anlass für sie wäre, aber ich hatte nicht erwartet, dass es so rührend sein würde."


"Ein Geburtstag nach dem anderen, Jahr für Jahr."


"Nur sie und Lilly, ganz allein."


"… Anscheinend hat sie nicht nur die Geschenke gerngehabt."


scene bg school_dormlilly_ni onlayer master
with locationchange

"Ich setze mich erneut neben das Bett und ruhe meine müde Arme neben mir aus. Eine unbequeme Nacht liegt vor mir, und ich bin bereit, mich in mein Schicksal zu ergeben."


li "Hey, Hisao."


"Lillys Stimme ist so leise, dass ich sie kaum wahrnehmen kann. Sie muss kurz vor dem Einschlafen sein."


scene ev lilly_sleeping onlayer master:
with locationchange

hi "Ja?"


scene ev lilly_sleeping_smile onlayer master
with charachange

li "Danke."


hi "Danke? Für was denn?"


li "Dass du hier bist."


hi "… Keine Ursache."


scene bg school_dormlilly_ni onlayer master
with locationchange

"Als ich einen tiefen Atemzug höre, wird mir klar, dass Lilly eingeschlafen ist."


"Nachdem ich meine Augen geschlossen habe, dauert es nicht lange, bis der Schlummer auch mich ergreift."


stop music fadeout 2.0

window hide

scene black onlayer master
with shuteye



label de_L5:

window hide None

scene black onlayer master
with Pause(4.0)

stop music

window show

mystery "Hisao?"


mystery "Hisao, bist du…?"


"Die sanfte, kaum hörbare Stimme, die in meine Ohren klingt, weckt mich langsam auf. Ich wünschte, ich könnte häufiger auf diese Weise geweckt werden."


"Mit einem Murmeln öffne ich langsam meine…"


scene bg school_dormlilly onlayer master
show lilly superclose onlayer master
with openeye_shock

show lilly superclose_shock onlayer master
with Dissolve(0.2)

$ doublespeak(hi, li, "Whoa!", "Au!")


play sound sfx_impact2

show lilly superclose_ouch onlayer master
with vpunch

show lilly basic_concerned_paj onlayer master:
    xalign 0.5 yanchor 1.0 ypos 1.2
    ease 0.4 ypos 1.4
with Dissolve(0.2)

"Der unerwartete Anblick eines neugierigen Gesichts nur wenige Millimeter über mir überrascht mich so sehr, dass mein Kopf mit ihrem kollidiert."
"Das hat zur Folge, dass wir beide rückwärts fallen und vor Schmerz aufschreien, was sich bei Lilly eher wie ein Quietschspielzeug anhört als einem Menschen."


hi "Au, au, au."


play music music_happiness fadein 6.0

"Ich reibe mir die Stirn mit einer Hand und stütze mich mit der anderen ab. Lilly liegt einen Meter vor mir und tut dasselbe. In ihrem Gesicht kann man den Schmerz klar erkennen."


hi "Äh… tut mir leid. Dein Gesicht war ein bisschen nah, und ich habe mich erschreckt. Bist du okay?"


show lilly basic_concerned_paj onlayer master:
    ease 1.0 ypos 1.2
with Pause(0.5)

li "Mein Kopf…"


"Anscheinend ist sie nicht wirklich okay. Wenn ich es mir recht überlege, dann bezweifle ich, dass der Aufprall allein für ihre Kopfschmerzen verantwortlich ist."


hi "Hast du einen Kater? Du hast gestern Abend eine ganze Menge getrunken."


show lilly basic_sad_paj onlayer master:
    ypos 1.2
with charachange

"Sie nickt zur Bestätigung wortlos mit dem Kopf, während ich aufstehe."


show lilly basic_concerned_paj onlayer master:
    ease 1.0 ypos 1.0
with Pause(0.5)

"Ich reiche ihr meine Hand und helfe ihr auf. Als ich an ihr vorbei schaue, sehe ich, dass Hanako noch fest schläft."


show lilly basic_reminisce_paj onlayer master at center
with charachange

li "Es ist unfair… ich habe genauso viel getrunken wie du…"


hi "Das habe ich anders in Erinnerung. Und Mädchen haben sowieso eine niedrigere Alkoholtoleranz als Männer."


show lilly basic_displeased_paj onlayer master
with charachange

li "Das macht es nicht besser."


hi "Gut, ich hole dir ein Glas Wasser. Pass einfach auf, dass du nicht über Hanako stolperst."


hide lilly onlayer master
with charaexit

"Ich reibe mir den Schlaf aus den Augen – oder zumindest einen Teil davon – während ich zum nächsten Wasserspender gehe. Es gibt bessere Wege, einen Morgen zu verbringen, als jemand mit einem Kater zu pflegen."


"Es dauert nur ein paar Sekunden, bis sich das Glas gefüllt hat. Das klare Wasser reflektiert den schmalen Lichtstrahl, der die dünnen Vorhänge durchdringt."


"In der Zwischenzeit hat Lilly sich auf den Rand des Bettes gesetzt. Ich steige vorsichtig über die friedlich schlafende Hanako, gehe zu ihr hinüber und platziere das Glas in ihren ausgestreckten Händen."


show lilly basic_weaksmile_paj_close onlayer master:
    center
    ypos 1.2
with charaenter

li "Danke."


hi "Kein Problem."


stop music fadeout 12.0

"Ich setze mich neben sie. Das weiche Bett gibt überraschend stark nach."


"Sie trinkt langsam und systematisch. Es folgt eine lange Stille, während der man nur Hanakos leisen Atem hören kann."


show lilly basic_reminisce_paj_close onlayer master
with charachange

"Obwohl ich mich deswegen schuldig fühle, schaue ich Lillys Gesicht an und versuche, ihren Ausdruck zu lesen. Ihre Stirn ist gerunzelt und sie sieht gedankenverloren aus."


show lilly basic_emb_paj_close onlayer master
with charachange

"Für einen Moment zögere ich, dann lege ich eine Hand auf ihre Schulter in einem Versuch, sie zu beruhigen. Ich habe aber nicht erwartet, dass sie deswegen so stark zusammenzucken würde."


hi "Äh, tut mir leid. Ich wollte dich nicht—"


show lilly basic_sad_paj_close onlayer master
with charachange

"Lilly schüttelt schnell ihren Kopf – auf eine heftigere Art als für sie üblich ist."


"Sie atmet tief ein, um sich zu sammeln, bevor sie ihren Kopf sinken lässt."


show lilly basic_weaksmile_paj_close onlayer master
with charachange

li "Ich muss schrecklich aussehen…"


"Ich fange an zu protestieren, merke aber schnell, dass es sinnlos wäre. Trotzdem möchte ich, dass sie sich weiter öffnet."


hi "Wenn du über irgendetwas sprechen willst, bin ich hier."


show lilly basic_displeased_paj_close onlayer master
with charachange

"Lilly schnaubt selbstironisch, als ob sie sich über ihre eigenen Gefühle lustig machen wollte."


show lilly basic_reminisce_paj_close onlayer master
with charachange

li "In meinem Leben ist… zur Zeit viel los."


show lilly basic_sad_paj_close onlayer master
with charachange

li "Es tut mir leid, dass ich mich in letzter Zeit so eigenartig benehme, besonders als wir in der Stadt waren. Selbst jetzt bin ich immer noch ein wenig verwirrt von allem."


hi "Glaub mir, ich weiß, wie das ist."


show lilly basic_weaksmile_paj_close onlayer master
with charachange

"Sie lächelt wehmütig und stützt eine Wange auf den Rücken ihrer Finger."


li "Wir sind ein paar kaputte, junge Dummköpfe, nicht wahr?"


hi "Ach komm, sag so etwas nicht. Nach dem Schulabschluss werden wir zurück in der echten Welt sein."


"Die echte Welt? Mit meiner Denkweise überrasche ich manchmal mich selbst. Anscheinend empfinde ich diese merkwürdige Abgeschiedenheit von Yamaku und dem umliegenden Dorf im Vergleich zur Außenwelt immer noch nicht als natürlich."


"Vielleicht werde ich das auch nie. Im Nachhinein ist es merkwürdig: Auf diese Weise von der Gesellschaft isoliert zu sein, fühlt sich nicht so schlecht an wie es eigentlich sollte."
"Aufgrund ihres schiefen Lächelns nehme ich an, dass Lilly von dieser Idee ebenfalls amüsiert ist."


"Aber schließlich verschwindet ihr Lächeln."


show lilly basic_displeased_paj_close onlayer master
with charachange

li "Ich werde bald für ein oder zwei Wochen nach Schottland reisen."


hi "War das der Grund, warum wir Hanakos Geburtstagsfeier verlegen mussten?"


"Sie nickt bejahend."


hi "Immerhin wirst du deine Familie wiedersehen können. Freust du dich nicht darauf?"


show lilly basic_concerned_paj_close onlayer master
with charachange

li "Ich habe meine Familie seit sechs Jahren nicht getroffen. Ich weiß nicht mal, wie ich mich ihnen gegenüber verhalten soll."


"Moment… wie war das? Mein Mund hängt offen, während ich versuche, das zu verarbeiten."


play music music_moonlight fadein 6.0

"Wenn sie achtzehn ist, dann bedeutet das, dass sie nur zwölf war, als sie abgereist sind. Es mag sein, dass ich sehr wenig von meinen Eltern gesehen habe, da sie beide viel arbeiten mussten, aber das ist…"


"Ich fühle mich völlig nutzlos, weil ich keine Ahnung habe, wie ich auf diese Enthüllung reagieren soll."


hi "Das ist… Aber… Warum?"


show lilly basic_reminisce_paj_close onlayer master
with charachange

li "Warum sind sie abgereist oder warum laden sie Akira und mich plötzlich ein?"


hi "Beides, denke ich."


show lilly basic_sleepy_paj_close onlayer master
with charachange

li "Die Zentrale des Unternehmens meines Vaters liegt in Schottland, und es gab dort eine offene Führungsposition für ihn. Am Ende musste er dauerhaft dorthin ziehen."


li "Meine Mutter folgte ihm, aber Akira und ich blieben in Japan zurück; sie wegen ihrer Stelle bei der japanischen Filiale der Firma meines Vaters und ich wegen der Schule."


show lilly basic_concerned_paj_close onlayer master
with charachange

li "Was die zweite Frage angeht… Eine meiner Tanten ist schwer krank."


hi "Ah. Das… tut mir leid."


show lilly basic_weaksmile_paj_close onlayer master
with charachange

li "Das muss es nicht. Es fühlt sich merkwürdig an. Wir werden ihretwegen hinüberfliegen, kennen sie aber kaum. Ich kann mich nicht einmal an ihre Stimme erinnern."


"Ebenso merkwürdig ist der völlige Mangel an Abneigung gegenüber einer Familie, die ihr so etwas angetan hat. Wenn ich mich mit ihr vergleiche, dann fühle ich mich etwas klein."


"Aber sie versteckt ihre Emotionen nur hinter einer wehmütigen Fassade. Sie so zu sehen, ist deprimierend."


stop music fadeout 5.0

"Plötzlich weiß ich, was zu tun ist, und stehe auf. Als Lilly die Bewegung des Bettes bemerkt, hebt sie den Kopf und streckt ihre Hand zur Seite, um zu fühlen, wo ich gesessen habe."


show lilly basic_oops_paj_close onlayer master
with charachange

li "Hisao…?"


play sound sfx_rustling

"Ich gehe zu meiner Tasche, die immer noch an der Wand lehnt. Ich löse die Schnalle, hole die Tüte heraus, und entnehme ihr die kleine Spieldose."


hi "Streck deine Hände aus, Lilly."


show lilly basic_surprised_paj_close onlayer master
with charachange

"Sie sieht einen Augenblick lang überrascht aus, folgt dann aber meiner Bitte."


show lilly basic_surprised_paj_close onlayer master:
    ease 1.0 xpos 0.4
show bg school_dormlilly onlayer master:
    center
    ease 1.0 xpos 0.4
with Pause (1.0)

show musicbox closed behind lilly onlayer master:
    alpha 0.0  zoom 0.5  xanchor 0.0 xpos 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.6 alpha 1.0
show boxstrip behind lilly onlayer master:
    alpha 0.0  zoom 0.5  xanchor 1.0 xpos 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.6 alpha 1.0
with Pause (1.0)

"Ich bin von ihrem neugierigen Gesichtsausdruck amüsiert, als ich die Spieldose in ihre offenen Händen lege. So behutsam wie Lilly sie behandelt, könnte man denken, sie würde beim leisesten Windhauch kaputt gehen."


stop music fadeout 2.0

"Wortlos bring sie die Spieldose vor ihr Gesicht. Ihre schmalen Finger ertasten die Umrisse und Muster."


"Schließlich finden ihre Finger die Vertiefung zwischen Deckel und Unterteil der Holzkiste. Mit ihrem Daumen öffnet sie den Deckel."


show musicbox open onlayer master:
    xpos 0.5 ypos 0.6 alpha 1.0
with charachange

play music music_musicbox

"Ich setze mich neben ihr auf das Bett und beobachte schweigend ihr Gesicht."


"Mit leicht geöffnetem Mund sitzt sie völlig regungslos da, während sie sich die leise, blecherne Melodie anhört."


show musicbox closed onlayer master
show lilly basic_smileclosed_paj_close onlayer master:
    xpos 0.4
with charachange

play sound sfx_switch
stop music

show musicbox closed onlayer master:
    ease 1.0 ypos 0.7 alpha 0.0
show boxstrip onlayer master:
    ease 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

show lilly basic_smileclosed_paj_close onlayer master:
    ease 1.0 xpos 0.5
show bg school_dormlilly onlayer master:
    ease 1.0 center
with Pause (1.0)

hide musicbox onlayer master
hide boxstrip onlayer master

"Es dauert eine lange Weile, bis sie den Deckel zuklappt und damit die kleine Aufführung beendet, die in ihren Händen spielt."


"Das sanfte, wehmütige Lächeln auf ihrem Gesicht zeigt, dass ich die richtige Entscheidung getroffen habe."


hi "Betrachte es als Abschiedsgeschenk für deine Reise nach Schottland."


show lilly basic_smile_paj_close onlayer master:
    xpos 0.5
with charachange

li "Das werde ich…"


play sound sfx_rustling

show lilly basic_smile_paj_close onlayer master:
    twoleft
    ypos 1.2
show bg school_dormlilly onlayer master at bgleft
with charamove

"Auf dem Boden vor uns ist ein unruhiges Rascheln zu hören. Die Musik hat Hanako aufgeweckt."


show hanagown distant onlayer master:
    tworight
    ypos 1.3
    easein 1.0 ypos 1.1
with Dissolve(1.0)

"Verwirrt kriecht sie aus den Bettdecken heraus, die ich über sie gelegt habe, und reibt sich die Augen."


hi "Du bist also endlich wach."


show hanagown normal onlayer master:
    ypos 1.1
with charachange

ha "Hmm? Was?"


show lilly basic_planned_paj_close onlayer master
with charachange

"Hanako schaut sich mit halbgeöffneten Augen im Zimmer um. Sie ist geistig keineswegs so wach wie körperlich, und Lilly und ich schmunzeln über ihren benommenen Zustand."


show lilly basic_planned_paj_close onlayer master:
    ease 1.0 twoleft
with Pause(1.0)

show lilly basic_planned_paj onlayer master at twoleft
with charadistant

"Während Lilly vom Bett aufsteht und sich um Hanako kümmert, blicke ich ein letztes Mal im Zimmer herum."


hi "Ich sollte mich besser auf den Weg machen. Wenn jemand beobachtet, wie ich am Morgen das Mädchenwohnheim verlasse, wird es Fragen geben."


show lilly basic_smile_paj onlayer master
with charachange

li "Auf Wiedersehen, Hisao."


show hanagown smile onlayer master
with charachange

ha "Oh… Auf Wiedersehen."


"Ich stehe auf, gehe in Richtung Tür und hebe unterwegs meine nun etwas leichtere Tasche auf."


scene bg school_girlsdormhall onlayer master
with locationchange

"Aber nachdem ich das Zimmer verlassen und den Gang betreten habe, höre ich Lillys Schritte hinter mir."


hi "Hmm? Stimmt was nicht?"


show lilly basic_smileclosed_paj_close onlayer master:
    yalign 1.0 xpos 0.3 xanchor 0.5
    easein 1.0 xpos 0.5
with Dissolve(1.0)

"Wortlos schreitet sie auf mich zu. Ich erstarre, als ich spüre, wie sie ihre Hand über meine Wange gleiten lässt. Es scheint, als ob jeder Nerv das Gefühl ihrer Finger und Handfläche wahrnimmt."


play music music_romance

"Gleich darauf bewegt sie ihr Gesicht neben meines, und ich spüre eine leichte, kurze Berührung ihrer Lippen auf meiner anderen Wange."


"Einen Augenblick lang scheint alles stillzustehen. Gedankenverloren lasse ich die Finger zu meiner Wange wandern, als ob ich versuchen würde, dieses flüchtige Gefühl wieder einzufangen."


hi "Lilly…"


show lilly basic_smile_paj_close onlayer master at center
with charachange

li "Das ist mein Dankeschön an dich, Hisao."


hi "Dein Dankeschön? Aber wofür…?"


show lilly basic_cheerful_paj_close onlayer master
with charachange

li "Für dein Geschenk. Ich wünsche dir einen schönen Schultag."


show lilly basic_cheerful_paj_close onlayer master:
    easeout 1.0 xpos 0.3 alpha 0.0
with Pause(1.0)

hide lilly onlayer master
with None

"Und mit diesen Worten verschwindet sie hinter ihrer Tür und schließt sie leise. Ganz wie gestern Nacht höre ich leise die gedämpften Stimmen von ihr und Hanako."


"…"


"… Ich glaube, dass es mir schwer fallen wird, nach diesem Kuss keinen schönen Tag zu haben."


show bg school_courtyard onlayer master
with locationskip

"Ich verlasse das Mädchenwohnheim mit einem gewissen Elan. Ich glaube, dass es einige Leute gab, die mich dabei flüchtig gesehen haben, aber es schert mich eigentlich wenig."


stop music fadeout 2.0

scene black onlayer master
with dissolve



label de_L6i:

scene black onlayer master
with None

mi "Hicchan~."


hi "Geh weg."


mi "Hicchan~."


hi "Lass mich in Ruhe."


mi "Komm schon, Hicchan~."


hi "Hmph. Lass mich schlafen."


"Nachdem ich zwei Nächte nicht schlafen konnte, ist so ziemlich das Letzte, was ich will, aufgeweckt zu werden, wenn ich es endlich geschafft habe einzuschlafen."


"Es mag die letzte Unterrichtsstunde sein – und mein Kissen nur ein Lehrbuch – aber inzwischen ist mir alles recht, solange ich schlafen kann."


mi "Siehst du, Hicchan, sogar Shicchan will, dass du aufstehst~!"


"Es ist mir völlig egal, was Shizune will. Lass mich in Ruhe."


mi "Mensch, Hicchan, dann muss ich dich…"


"Moment mal, Misha wird doch wohl nicht…?"


mi "… einfach…"


"Das ist gar nicht gut!"


play music music_running

scene bg school_scienceroom onlayer master
show misha hips_grin_close onlayer master at center
with vpunch

hi "ICH BIN WACH! ICH BIN WACH! DU… musst nicht…"


"Ich kann praktisch spüren, wie mein Gesicht feuerrot wird."


"Die Schüler, die sich noch im Klassenzimmer befinden, springen aus ihren Stühlen und starren den brüllenden Narren an, der gerade noch geschlafen hat."


hi "… Verdammt."


play sound sfx_impact2
with vpunch

"Ich lasse meinen Kopf mit einem dumpfen Knall auf die Tischplatte fallen."


show misha cross_laugh_close onlayer master
with charachange

mi "Wahahahahaha~!"


"Mishas unverkennbares, unkontrolliertes Gelächter hallt durch das Klassenzimmer."


show shizu invis behind misha onlayer master:
    center
    xpos 0.95
with None

show misha hips_grin_close onlayer master at twoleft
show shizu adjust_happy onlayer master at tworight
show bg school_scienceroom onlayer master at bgleft
with dissolvecharamove

"Ich werfe einen schwermütigen Blick auf die neben ihr stehende Shizune, die ihre Brille vorsichtig justiert und verzweifelt versucht, ihren missbilligenden Blick aufrechtzuerhalten."


"Ich kneife die Augen zusammen und sehe das schlecht versteckte Grinsen auf ihrem Gesicht."


hi "Et tu, Shizune?"


show shizu behind_blank onlayer master
with Dissolve(0.3)

"Shizune schaut schnell weg, während sie die Arme fest verschränkt. Sie kann sich kaum zurückhalten."


show misha cross_laugh_close onlayer master
with charachange

mi "Wahahahahahaha~!"


"Als Misha einen Blick auf Shizune wirft, verdoppelt sich die Lautstärke ihres Gelächters. Ich schlage resigniert die Hand vors Gesicht."


hi "Ihr beide…"


show misha sign_smile_close onlayer master
with charachange

mi "Wer ist derjenige, der während des Unterrichts eingeschlafen ist, Hicchan~?"


hi "Ja, ja, das war ich."


show misha hips_frown_close onlayer master
with charachange

mi "Die arme Shicchan ist ausgeflippt, während sie versucht hat, dich zu wecken. Stimmt, oder?"


show shizu basic_angry onlayer master
with charachange

"Ich blicke auf die distanzierte Shizune zurück, die Mishas Aussage mit einem Schnauben bestätigt, bevor sie wieder mit verschränkten Armen wegschaut."


hi "Warum wollte Shizune mich aufwecken?"


show misha hips_smile_close onlayer master
with charachange

mi "Shicchan wollte dir die Arbeitsblätter geben, die der Vertretungslehrer ausgeteilt hat."


hi "Arbeitsblätter?"


play sound sfx_paper
show shizu behind_frown_close onlayer master
show misha hips_frown_close onlayer master
show blanknote onlayer master at truecenter
with vpunch

"Plötzlich erscheinen zwei Papierblätter vor meinem Gesicht."


show blanknote onlayer master at Transform(xpos=0.3)
with charamove

"Mit meinen Augen folge ich der Hand, die sie hält, bis zu ihrer noch schmollenden Besitzerin. Sie schaut mit einem finsteren Blick auf mich hinunter. Ich denke, dass ich in diesem Fall wirklich im Unrecht bin."


hi "… Ah. Äh, tut mir leid."


stop music fadeout 8.0

"Keine Chance. Ihr Gesicht bleibt weiter verärgert. Ich lege meine Hände aneinander und senke entschuldigend den Kopf."


hi "Wirklich, wirklich leid."


show shizu behind_frustrated_close onlayer master
with charachange

show blanknote onlayer master:
    easeout 0.5 ypos 0.8 alpha 0.0
with Pause(0.5)

hide blanknote onlayer master
with None

"Sie schnaubt und lässt die Papiere einfach auf den Tisch fallen."


hi "Verdammt."


show shizu adjust_angry_close onlayer master
show misha sign_smile_close onlayer master
with charachange

"Ich blicke über meine Hände nach oben und sehe, wie Shizune und Misha wie wild miteinander gebärden. Ein frustrierter Blick ist auf Shizunes Gesicht zu sehen."


show shizu basic_angry_close onlayer master
with charachange

shi "…!"


"Es sieht weniger wie ein Gespräch und vielmehr wie eine Tirade aus. Eine Tirade, die mit Seitenblicken in meine Richtung betont wird. Zu sagen, dass das Ganze beunruhigend wirkt, ist eine Untertreibung."


hi "Äh…"


show shizu behind_frown_close onlayer master
show misha hips_frown_close onlayer master
with Dissolve(0.3)

"Die beiden hören plötzlich mit dem Gebärden auf. Sie schauen mich gemeinsam an und haben genau denselben, missbilligenden Blick. Mit einer flüssigen Bewegung schießt Mishas Hand plötzlich hoch und dann genauso schnell wieder herunter."


scene black onlayer master
with None

play sound sfx_impact2
play music music_running

"Noch bevor ich mir Gedanken über eine mögliche Abwehrreaktion machen kann, bekomme ich einen Schlag auf den Kopf, der ihn springteufelartig wippen lässt." with vpunch


"Ich fasse mir umgehend an den Kopf – mehr ein Reflex als dass es wirklich wehgetan hat."


hi "Aua! Wofür war das denn?"


scene bg school_scienceroom onlayer master at bgleft
show shizu adjust_smug_close onlayer master at tworight
show misha hips_grin_close onlayer master at twoleft
with openeye

"Ich öffne meine Augen und sehe, wie die beiden einander angrinsen und sich einen erhobenen Daumen entgegenstrecken."


show misha hips_smile_close onlayer master
show shizu behind_smile_close onlayer master
with charachange

mi "Shicchan sagt, dass sie dir jetzt vergibt, Hicchan~!"


hi "Kannst du mir beim nächsten Mal auf eine weniger gewaltsame Art vergeben?"


show misha cross_laugh_close onlayer master
with charachange

mi "Wahahahaha~!"


"Ich schaue die beiden mit einem ausdruckslosen Gesicht an. Misha und Shizune: Eins, Hisao: Null."


show shizu adjust_happy_close onlayer master
with charachange

shi "…"


show misha hips_grin_close onlayer master
with charachange

mi "Oh, Shicchan sagt auch, dass du häufiger nach deiner Post schauen solltest~!"


show letter_insert onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Sie holt einen hellgelben Umschlag hervor und hält ihn mir mit einem ausgelassenen Grinsen hin."


"Komisch. Wer würde mir denn einen Brief schreiben? Wie auch immer, jetzt ist weder die Zeit noch der Ort, um es herauszufinden."


show letter_insert onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide letter_insert onlayer master
with None

"Mein Nickerchen, das so herzlos unterbrochen wurde, kann ich wohl abschreiben. Ich reibe mir die Stirn, stehe langsam auf und stecke die Blätter und den Umschlag in meine Tasche, bevor ich sie mir über die Schulter werfe."


show misha cross_laugh onlayer master at Transform(yalign=1.0, xanchor=0.5, xpos=0.355)
show shizu behind_smile onlayer master at Transform(yalign=1.0, xanchor=0.5, xpos=0.615)
with charadistant

"Ich mache einen Schritt zurück, und verlasse den Raum mit einer kleinen Verbeugung. Misha greift sich vor Lachen an den Bauch, während Shizune mir zum Abschied kurz zunickt."


stop music fadeout 3.0
play ambient sfx_crowd_indoors fadein 0.5

scene bg school_hallway3 onlayer master
show crowd onlayer master
with locationchange

"Ich schließe mich dem hinausdrängenden Schülerstrom an und biege um die Ecke in den Flur ab."


$ renpy.music.set_volume(0.7, 0.5, channel="ambient")

show hanako emb_downtimid onlayer master at center
with charaenter

"… wo ich plötzlich Hanako gegenüberstehe."


hi "Whoa. Äh, hallo, Hanako."


show hanako emb_timid onlayer master
with charachange

ha "Guten Tag… Hisao."


show hanako emb_downtimid onlayer master
with charachange

"Während die Schüler, die an uns vorbeigehen, eifrig miteinander plaudern, herrscht zwischen uns Stille. Sie zappelt ständig herum, und ihr Blick klebt förmlich an ihren Schuhen."


"Ich greife meine Nasenwurzel mit meinen Fingern und blinzele ein paar Mal, um meinen Kopf freizukriegen. So wie die Dinge stehen, schaffe ich es kaum, wach zu bleiben."


hi "Hanako, du möchtest etwas sagen. Was gibt's?"


show hanako emb_blushing onlayer master
with charachange

ha "Ä-äh… ich wollte dir… das hier geben…"


hi "Hmm?"


show hanako basic_worry onlayer master
with charachange

"Sie hält mir ein kleines, rechteckiges Blatt Papier entgegen. Ich blinzele wieder, während ich versuche, mit kaum geöffneten Augen den Text zu entziffern. Langsam gelingt es mir, die Handschrift zu enträtseln."


window hide

$ written_note("\nEier x2\nBrotlaib x1\nVollkorngetreideflocken x1\nWalnüsse x1\n")


window show

play music music_happiness fadein 0.5

hi "… Eine Einkaufsliste?"


"Ich blicke nach oben und ziehe eine Augenbraue hoch."


show hanako emb_timid onlayer master
with charachange

ha "Normalerweise gehe ich mit Lilly einkaufen, aber heute schaffe ich es nicht, also…"


hi "Du willst, dass ich Besorgungen für dich erledige?"


show hanako defarms_shock onlayer master
with charachange

ha "E-Es ist okay, wenn du es nicht machen willst! Ich dachte nur, dass, vielleicht, äh…"


"Sie gerät in Panik. Ich seufze. Schon wieder eine Schlacht verloren – allerdings dieses Mal fast ohne Gegenwehr."


"Ich lächle müde und lege eine Hand auf ihren Kopf, um sie zu beruhigen."


hi "Schon gut. Ich hatte sowieso vor, einkaufen zu gehen. Willst du nur die Sachen, die auf der Liste stehen?"


show hanako def_worry onlayer master
with charachange

"Sie nickt und verbeugt sich zweimal sehr tief, als ob sie ihre Dankbarkeit absolut klar machen will."


show hanako cover_distant onlayer master
with charachange

ha "W-Wir wollten uns um sechs Uhr vor dem Schultor treffen… Danke. Ich wollte es selbst holen, aber ich muss für den Test morgen lernen."


hi "Test? Ach ja, stimmt, Naturwissenschaft. Wie läuft's bei dir in diesem Fach?"


show hanako cover_bashful onlayer master
with charachange

"Ihre Miene erhellt sich ein bisschen."


show hanako basic_bashful onlayer master
with charachange

ha "Ich verbringe… mehr Zeit damit als vorher. Ich glaube, dass ich… es schaffe."


hi "Das ist gut. Mach weiter so."


show hanako basic_smile onlayer master
with charachange

"Sie fängt ebenfalls an zu lächeln, und sogar viel aufrichtiger als ich."


"Ich habe volles Vertrauen, dass ich einen guten Test schreiben kann, ohne dafür zusätzlich lernen zu müssen. Aber die Tatsache, dass sie sich so viel Mühe gibt, statt nur in der Bibliothek zu lesen, ist ermutigend."


hi "Ich hol dir deine Sachen und bringe sie dir heute Abend. Bis dann."


stop music fadeout 3.0
$ renpy.music.set_volume(1.0, 3.0, channel="ambient")

hide hanako onlayer master
with charaexit

"Mit einem kleinen Winken verabschieden wir uns und gehen unsere getrennte Wege."


"Ich werde meine Hausaufgaben machen, bevor ich Lilly treffe. Es sollte möglich sein, sie rechtzeitig zu erledigen."


stop ambient fadeout 1.0

scene bg school_gate_ss onlayer master
with shorttimeskip

play music music_soothing fadein 2.0

"Meine Beschäftigung mit einer besonders kniffligen Mathematikaufgabe hat zur Folge, dass ich ein bisschen spät für mein Treffen mit Lilly bin."


"Zugegeben, es sind nur ein paar Minuten, aber trotzdem gehe ich den Weg über den Schulhof und zum Tor sehr zügig."


scene bg school_road_ss onlayer master
with locationchange

"Ich biege nach rechts ab und fange an, in Richtung des kleinen Dorfes zu wandern. Ein paar Schüler gehen in der entgegengesetzten Richtung zur Bushaltestelle."


"Ich stecke meine rechte Hand in meine Tasche, während ich im orangefarbenen Sonnenlicht der Abenddämmerung die Straße entlanggehe."


"Glücklicherweise fängt die brütende Sommerhitze an nachzulassen und wird von einer angenehmen, kühlen Brise ersetzt."


show lilly back_listen_ss onlayer master at center
show lillyprop back_cane_ss onlayer master at center
with charaenter

"Als ich die Hände hoch über meinen Kopf strecke, kommt eine vertraute Gestalt mit einem Stock in der rechten Hand in Sicht."


hi "Ah, Lilly."


show lilly cane_listen_ss onlayer master
hide lillyprop onlayer master
with charachange

"Sie bleibt stehen, dreht sich um, und legt leicht den Kopf zur Seite, als sie versucht herauszufinden, aus welcher Richtung die Stimme kam."


hi "Hey. Ich bin's."


"Ich hole sie schnell ein, und als wir gemeinsam weitergehen, passe ich mich ihrem langsamen Lauftempo an."


show lilly cane_smile_ss onlayer master
with charachange

li "Guten Tag, Hisao."


hi " Hallo."


scene bg misc_sky_ss onlayer master at Fullpan(10.0, dir="right")
with locationchange

"Ich werfe einen Blick zum Himmel."


"Ein ausgeprägter Orangeton verfärbt die Wolken und taucht den Gehweg in sein Licht. Weiter unten am Hügel fallen die langen Schatten der Bäume über die breite Straße."


scene bg school_road_ss onlayer master
show lilly cane_smileclosed_ss onlayer master
with charachange

li "Also, Hisao, was führt dich hier hierher?"


hi "Ich gehe nur ins Dorf, um Lebensmittel zu holen. Hanako hat mich geschickt."


show lilly cane_surprised_ss onlayer master
with charachange

li "Hanako hat dich geschickt?"


hi "Ja, sie hat gesagt, dass sie für einen Test morgen lernen muss. Ich wollte sowieso ins Dorf, also kann ich ihre Sachen einfach mitkaufen."


"Unerwähnt bleibt, dass Lilly beim Essen kaufen wirklich Hilfe brauchen könnte, aber diese Tatsache ist so offensichtlich, dass keiner von uns beiden sie erwähnen muss."


show lilly cane_weaksmile_ss onlayer master
with charachange

li "Es ist gut zu hören, dass sie dafür lernt."


hi "Ich habe dasselbe gedacht, als sie mich gebeten hat, dich zu begleiten."


hide lilly onlayer master
with charaexit

"Wir gehen weiter die Straße entlang, während das vertraute Geräusch ihres Stocks durch die Luft hallt. Abgesehen von dem gelegentlich vorbeifahrenden Auto und den Blättern, die in den Ästen rascheln, herrscht eine herrliche Stille."


"Gott sei Dank kann ich mich zum heute endlich mal entspannen."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene evbg lilly_sunsetwalk onlayer master:
    truecenter subpixel True zoom 0.9
    acdc_warp 20.0 zoom 1.0
show evfg lilly_sunsetwalk onlayer master:
    truecenter subpixel True zoom 0.85
    acdc_warp 20.0 zoom 1.0
with locationskip

"Ich sehe zu Lilly hinüber."


"Ihr porzellanartiges Gesicht scheint immer eine gewisse entspannte Zuversicht auszustrahlen. Ich nehme an, dass man dasselbe auch von ihrer Persönlichkeit sagen könnte."


"Während sie schweigend geht, ihr Gesicht auf die Straße vor ihr gerichtet, blicke ich voraus und genieße die kühle Brise, die über mein Gesicht weht."


"Dies ist wahrscheinlich der beruhigenste Moment, den ich hatte, seit sich mein Leben so grundsätzlich geändert hat."


"Und ich erlebe ihn, während ich Lebensmittel einkaufen gehe. Was für ein seltsames Leben."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

scene bg school_road_ss onlayer master
with locationskip

"Ich spüre in meiner Tasche den zerknüllten Zettel, der gegen meine Hand reibt, und ziehe ihn heraus, um seinen Inhalt zu überprüfen."


hi "Lass mal sehen… Eier, Brot, Getreideflocken, Walnüsse, Kopfsalat, geschnittener Schinken…"


show lilly cane_weaksmile_ss onlayer master
with charaenter

li "Das ist ziemlich viel, um es ganz allein nach Hause zu tragen."


hi "Ja. Wie viel isst dieses Mädchen denn überhaupt?"


"Es dauert einen Moment, bis mir plötzlich klar wird, dass noch jemand anderes neben mir geht."


hi "W-Warte, ich meine…"


show lilly cane_giggle_ss onlayer master
with charachange

"Sie lacht rückhaltlos."


show lilly cane_planned_ss onlayer master
with charachange

li "Meine Güte, Hisao."


"Ihr Kichern unterstreicht ihre Worte, obwohl sie sich nicht viel Mühe gibt, es zu unterdrücken."


show lilly cane_satisfied_ss onlayer master
with charachange

li "Du bist heute ziemlich direkt, nicht wahr?"


hi "Ja, da hast du mich erwischt. Trotzdem ist das ziemlich viel."


show lilly cane_smileclosed_ss onlayer master
with charachange

li "Normalerweise gehe ich mit Hanako einkaufen, also weiß ich, was sie kauft. Es ist jede Woche das Gleiche."


hi "Hmm. Ist sie eine gute Köchin?"


show lilly cane_weaksmile_ss onlayer master
with charachange

"Sie kichert nervös."


li "Letztendlich bin ich diejenige, die normalerweise kocht. Früher tat ich es für Akira, also ist es kein Problem, es auch für Hanako zu tun."


hi "Du kannst kochen? Aber…"


show lilly cane_cheerful_ss onlayer master
with charachange

"Ein kurzes, amüsiertes, trällerndes Summen kommt von neben mir. Ich frage mich, ob sie von meinen Kommentaren wirklich so häufig amüsiert ist wie es scheint oder ob sie einfach will, dass ich meine Scheu verliere, ihre Blindheit anzusprechen."


show lilly cane_smileclosed_ss onlayer master
with charachange

li "Es gibt natürlich Möglichkeiten. Einige Mahlzeiten sind schwerer zuzubereiten als andere, weil ich nicht sehen kann, was ich mache, aber normalerweise dauert es nur etwas länger. Finger können zum Beispiel sehr nützliche Messinstrumente sein."


"Das ergibt Sinn, aber sie muss sicher sehr vorsichtig sein, um sich nicht zu verletzen."
"Ich frage mich, wie oft das schon passiert ist, wenn man bedenkt, dass sie anscheinend seit Jahren allein kocht, während Akira gearbeitet hat und ihre Eltern weg waren."


"Mit diesen Worten verläuft sich das Gespräch."


"Im Gegensatz zu Hanakos peinlichem Schweigen scheint Lilly wirklich damit zufrieden zu sein, zu sagen, was sie denkt und still zu bleiben, wenn es nichts zu sagen gibt."


"Die rutschige Straße unter meinen Füßen leuchtet in orangefarbenem Licht, und das vereinzelt herumliegende Laub knirscht, wenn wir darüber laufen. Mein Schlafmangel verfolgt mich und macht sich in Form eines tiefen Gähnens bemerkbar."


show lilly cane_smile_ss onlayer master
with charachange

li "Hast du gestern Nacht nicht viel geschlafen?"


hi "Ich konnte die letzten zwei Nächte überhaupt keine Auge zukriegen. Wahrscheinlich Schlafstörungen."


stop music fadeout 8.0

show lilly cane_oops_ss onlayer master
with charachange

"Lilly sieht plötzlich besorgt aus. Es fühlt sich zwar jedes Mal wie ein persönliches Versagen meinerseits an, wenn sie sich Sorgen um mein Wohlergehen macht, aber es ist trotzdem schön zu wissen, dass sich jemand um mich sorgt."


li "Du hast Schlafstörungen? Willst du damit nicht zu Doc gehen?"


hi "Nee, nicht nötig. Das ist mir schon ein paar Mal passiert. Meine Medikamente bringen manchmal meinen Schlafrhythmus durcheinander."


show lilly cane_concerned_ss onlayer master
with charachange

li "… Oh. Es… tut mir leid."


hi "Komm schon, du bist doch nicht dafür verantwortlich. Zumindest werde ich heute Nacht keine Probleme beim Einschlafen haben."


show lilly cane_sleepy_ss onlayer master
with charachange

li "Du machst mir manchmal Sorgen."


hi "Ich… mache dir Sorgen?"


"Ich kratze mir den Nacken. Irgendwie möchte ich dieses Thema ansprechen."


hi "Hey, Lilly…"


show lilly cane_smile_ss onlayer master
with charachange

li "Hmm?"


hi "Das mag sich komisch anhören, aber… bitte versuch, mein Herzproblem zu vergessen."


show lilly cane_oops_ss onlayer master
with charachange

"Sie sieht ein wenig verloren aus. Das kann ich ihr kaum übel nehmen."


hi "Was ich damit meine, ist… behandle mich deswegen nicht anders."


show lilly cane_emb_ss onlayer master
with charachange

"Sie beugt den Kopf leicht, und ihre weißen Wangen erröten fast unmerklich."


li "Es ist nur allzu natürlich, sich Sorgen um die Leute in seinem Umfeld zu machen…"


hi "Na ja, es ist trotzdem schön zu wissen, dass es da draußen so jemanden gibt."


show lilly cane_smileclosed_ss onlayer master
with charachange

"Es mag etwas peinlich sein, das zu sagen, aber es ist die Wahrheit. Lilly atmet tief durch, um ihre Fassung wiederzuerlangen, und lächelt sanft, aber ihre Wangen bleiben gerötet."


"Den Rest des Weges zum Laden legen wir wortlos zurück."


scene bg suburb_konbiniint onlayer master
with shorttimeskip

play music music_daily fadein 4.0

"Verkäuferin" "Herzlich willkommen!"


hi "Ich werde wohl zuerst meine Sachen und dann während der zweiten Runde Hanakos Sachen holen."


show lilly cane_smileclosed onlayer master at center
with charaenter

"Ich nehme zwei abgenutzte Einkaufskörbe von dem Stapel neben dem Eingang und gebe einen an Lilly weiter."


show lilly cane_smileclosed onlayer master at Transform(ypos=800)
with charamove

show lilly basic_smileclosed onlayer master at Transform(ypos=800)
with charachange

show lilly basic_smileclosed onlayer master at center
with charamove

"Genau wie sie es das letzte Mal getan hat, legt sie ihn auf den Boden und schiebt ihren zusammengeschobenen Blindenstock zwischen die Griffe des Korbes, bevor sie ihn mit der rechten Hand wieder aufhebt."


$ renpy.music.set_volume(0.5, 0.5, channel="music")

show lilly basic_smileclosed onlayer master at Slide(0.5,0.5,0.3,0.5,1.0, time_warp=_ease_time_warp)
with None

show lilly basic_smileclosed_close onlayer master at Slide(0.5,0.5,0.3,0.5,1.0, time_warp=_ease_time_warp)
with Dissolve(1.0)

"Als sie mich am Arm nimmt, bin ich überrascht, wie schnell diese Art von Kontakt zur Gewohnheit geworden ist. Das liegt sicher hauptsächlich daran, dass es einfach notwendig ist."


show lilly basic_smile_close onlayer master at twoleft
with charachange

li "Wollen wir?"


$ renpy.music.set_volume(1.0, 2.0, channel="music")

hi "Klar doch."


"Keine der vereinzelten Personen, die uns im Laden begegnen, beachtet uns. Das ist angenehm im Vergleich mit der Stadt, wo die Leute geflüstert und uns angestarrt haben."


show lilly basic_smileclosed_close onlayer master
with charachange

"Jedes Mal, wenn wir einen neuen Gang erreichen, frage ich Lilly schnell, was sie braucht. Ich hole dann ihre Artikel zusammen mit meinen eigenen und stecke sie in die jeweiligen Körbe."


"Es ist ein eigenartiges Gefühl, dass jemand bei etwas so Einfachem wie Einkaufen so abhängig von mir sein könnte. Hanakos Anwesenheit ist praktisch ein Muss, wenn sie die Artikel aussuchen will, die sie braucht."


hi "Gut, ich habe so ziemlich alles, was Hanako und ich benötigen. Brauchst du noch etwas, Lilly?"


show lilly basic_smile_close onlayer master
with charachange

li "Nein, das sollte alles sein."


hi "Also, nichts wie ab."


"Seltsamerweise gibt es eine kilometerlange Warteschlange. Da der Laden zu klein ist, um mehr als eine Kasse zu rechtfertigen, sieht es so aus, als ob wir eine Weile warten müssen."


hi "Verdammt."


show lilly basic_surprised_close onlayer master
with charachange

"Lilly wendet neugierig den Kopf in meine Richtung, da sie den Grund für meine Beschwerde nicht sehen kann."


hi "Die Schlange ist wirklich lang. Sieht so aus, als müssten wir warten."


show lilly basic_weaksmile_close onlayer master
with charachange

li "Wie eigenartig."


"Resigniert nehmen wir unseren Platz am Ende der Schlange ein."


$ renpy.music.set_volume(0.5, 10.0, channel="music")

"Eine Person ist fertig, die Schlange bewegt sich vorwärts. Die nächste Person ist fertig, die Schlange bewegt sich vorwärts."


"Als wir endlich an der Reihe sind, bin ich so kurz vor dem Einschlafen, dass Lilly mir leicht auf die Schulter klopfen muss, damit ich mich vorwärts bewege."


show lilly basic_oops_close onlayer master
with charachange

li "Hisao… Hisao!"


$ renpy.music.set_volume(1.0, 0.3, channel="music")

hi "Hmm? Äh, tut mir leid."


show lilly basic_displeased_close onlayer master
with charachange

"Sie gibt einen kurzen, fassungslosen Seufzer von sich, während ich mich vorwärts bewege und meine und Hanakos Einkäufe in getrennte Tüten packen lasse."


"Verkäuferin" "Danke! Beehren Sie uns wieder!"


stop music fadeout 5.0

scene bg suburb_konbiniext_ni onlayer master
show lilly basic_smileclosed_ni onlayer master
with locationskip

"Als wir den Laden verlassen, hält Lilly eine einzige Tüte, während ich mich damit abquäle, vier zu tragen. Ich habe wortwörtlich die Hände voll, und es ist eine Menge Arbeit, aber glücklicherweise sind die Einkäufe alle leicht."


"Sogar ohne dass ich in den Himmel schaue, ist offensichtlich, dass überraschend viel Zeit vergangen ist. Der Weg ist dunkel und wird von Straßenlampen beleuchtet."


show lilly cane_smile_ni onlayer master
with charachange

"Nachdem Lilly ihren Stock herausgeholt hat, verlassen wir die wohlige Wärme des Ladens und nehmen den Weg, den wir gekommen sind, zu den Wohnheimen zurück."


scene bg school_road_ni onlayer master
with locationskip

play music music_dreamy fadein 8.0

"Obwohl keine Autos auf der Straße fahren, kompensieren die vollen Tüten den Geräuschmangel reichlich, da sie ständig quietschen und gegeneinander prallen."


show lilly cane_ara_ni onlayer master
with charaenter

li "Meine Güte, Hisao. Es ist schön zu wissen, dass du dich gut ernährst."


hi "Ich bin schließlich ein Junge im Wachstum und muss so viel essen, wie ich kann!"


show lilly cane_weaksmile_ni onlayer master
with charachange

li "Hmm… es muss schön sein, ein Mann zu sein."


hi "W-Wie bitte?"


"Entweder hat sie meine Überraschung über ihren völlig unerwarteten Kommentar nicht bemerkt oder sie ignoriert sie absichtlich, denn sie spricht unbeirrt weiter."


show lilly cane_smile_ni onlayer master
with charachange

li "An dein Gewicht denkst du beim Essen nicht wirklich oft, oder?"


hi "Ich verstehe, was du meinst. Ich denke, Frauen neigen dazu, sich mehr um solche Sachen zu kümmern als Männer."


show lilly cane_smileclosed_ni onlayer master
with charachange

li "Genau. Um ehrlich zu sein, macht es mich etwas neidisch."


hi "Na ja, es ist nicht gerade so, als ob wir es völlig ignorieren können."


"Sie nickt bejahend, und wir spazieren weiter."


hi "Hmm, das stimmt."


show lilly cane_smile_ni onlayer master
with charachange

li "Was ist los?"


hi "Hanako hat erwähnt, dass dein Geburtstag dieses Jahr schon vorüber ist. Hast du da etwas Besonderes unternommen?"


show lilly cane_listen_ni onlayer master
with charachange

"Sie macht eine lange Pause, während sie das an das Ereignis zurückdenkt."


show lilly cane_weaksmile_ni onlayer master
with charachange

li "Nicht wirklich. Hanako und ich hatten einfach abends nach der Schule eine kleine Feier."


hi "Du weißt schon, dass dein Geburtstag ein großes Ereignis sein soll?"


"Sie ganz allein mit Hanako… Das hört sich nach einem ziemlich einsamen Geburtstag an."


"Für mich haben sich Geburtstage immer wie ein Familienereignis angefühlt. Meine Eltern haben sich dann trotz ihren Vollzeitstellen immer Mühe gegeben, an dem Tag frei zu bekommen oder zumindest am Vorabend hineinzufeiern."


"Ich muss daran denken, wie Lilly erzählt hat, dass sie ihre Familie lange nicht mehr gesehen hat und später sogar aus Akiras Haus ausgezogen ist."


"Aber ich nehme an, dass es in alltäglichen Situationen wie dieser ähnlich ist. Wenn man bedenkt, dass sie die Packungen nicht lesen kann, wäre der Lebensmitteleinkauf ohne Begleitung sehr mühsam."


"Letztendlich hat sie nur Hanako und mich. Und Akira, wenn sie nicht arbeitet."


"Wie dem auch sei, sie scheint auch viele nicht ganz so enge Freunde unter den Schülern zu haben, ganz abgesehen von Leuten wie Yuuko."


"Dass es eine solche Grenze zwischen denen gibt, die ihr nahestehen, und denen, mit denen sie nur gesellschaftlich verkehrt, scheint ihre eigene, persönliche Entscheidung zu sein."


"Es ist ein bisschen demütigend zu sehen, in welchem Ausmaß Lillys Leben genau so läuft, wie sie es will und geplant hat."


"Aber Hanako ist für sie da, um ihren Geburtstag zu feiern, und ich helfe ihr beim Einkaufen. Es ist wohl eine seltsame Art von Symbiose."


show lilly cane_oops_ni onlayer master
with charachange

li "Alles in Ordnung, Hisao?"


hi "Was meinst du?"


li "Du bist plötzlich sehr still geworden."


hi "Ah, tut mir leid. Ich habe nur nachgedacht."


show lilly cane_smileclosed_ni onlayer master
with charachange

li "Oh?"


label de_choiceL6_1:
menu:
    with menueffect
    "Ah, jetzt habe ich ihre Neugier geweckt. Darüber zu reden wäre aber ziemlich persönlich…"
    "Vermeide das Thema.":




        return m1
    "Sag die Wahrheit.":


        return m2

label de_L6a:


hi "Ich dachte nur gerade über ein paar Sachen nach, die mir passiert sind. Mach dir keine Sorgen."


stop music fadeout 2.0

show lilly cane_listen_close_ni onlayer master
with characlose

li "Hmm?"


"Sie lehnt sich noch weiter zu mir hinüber, sodass ich zur Seite ausweichen muss."


hi "Komm schon, hast du so etwas noch nie gemacht?"


show lilly cane_cheerful_close_ni onlayer master
with charadistant

li "Es hört sich so an, als würdest du etwas verheimlichen…"


play music music_lilly fadein 4.0

"Argh. Warum muss dieses Mädchen so scharfsinnig sein?"


"Ich blicke in ihr Gesicht und sehe ein süßes, verspieltes Lächeln darauf."


"Sie… spielt mit mir? Trotzdem würde ich dieses Gesprächsthema mit ihr gerne vermeiden."


hi "Ich hab dir doch gesagt, es ist nichts."


show lilly cane_displeased_close_ni onlayer master
with charachange

"Lilly drückt ihr Missfallen mit einem Stirnrunzeln aus."


li "Ist das so?"


hi "Ja, so ist es."


show lilly cane_surprised_close_ni onlayer master
with charachange

li "Du bist ein sehr schlechter Lügner, Hisao."


hi "Das stimmt, aber gerade deshalb lüge ich nicht. Ich bin ein sehr vertrauenswürdiger Mensch."


show lilly cane_weaksmile_close_ni onlayer master
with charachange

li "Dessen bin ich mir sicher. Allerdings glaube ich, dass ich dir dieses eine Mal vergeben kann."


hi "Vergeben? Für was denn?"


show lilly cane_giggle_close_ni onlayer master
with charachange

with Pause(0.2)

show lilly cane_smile_ni onlayer master
with charadistant

"Sie kichert ein bisschen, bevor sie still weitergeht. Worüber denkt sie jetzt nach?"


stop music fadeout 4.0

"Ich lasse meine Schultern hängen und schaue in den dunklen Himmel hinauf."


"Ich glaube, das ist etwas, über das ich mir selbst klar werden muss, statt mich immer auf sie zu verlassen."


label de_L6b:


hi "Es ist nur… Ich dachte darüber nach, wie du anscheinend alles in deinem Leben unter Kontrolle hast. Sogar Hanako verlässt sich auf dich. Ich muss zugeben, dass selbst ich mich irgendwie auf dich verlassen habe, als ich hier angekommen bin."


hi "Ich denke, dass das eine gute Charaktereigenschaft ist."


"Ich wende mich ihr zu und beobachte ihre Reaktion."


stop music fadeout 2.0

show lilly cane_listen_close_ni onlayer master
with characlose

"Lilly zwingt sich dazu, nach vorne zu schauen und runzelt heftig die Stirn. Sie sieht etwas peinlich berührt aus, als ob sie versucht, die richtigen Worte zu finden."


hi "… Lilly?"


show lilly cane_weaksmile_close_ni onlayer master
with charachange

li "Ich würde dir danken, aber… die Annahme, dass ich mich nicht auf andere Leute verlasse, ist übertrieben. Wenn du denkst, dass Hanako sich einfach auf mich verlässt, ohne eine Gegenleistung zu erbringen, dann irrst du dich."


"Obwohl es größtenteils so ist, wie ich es mir gedacht habe, scheint es ihr schwerzufallen, die Worte auszusprechen."


"Wenn sie sich so sehr bemüht hat, ihre Unabhängigkeit zu bewahren – genauso wie jede Person in ihrer Lage, blind oder nicht, es getan hätte – dann fällt es ihr vielleicht schwer, über ihre eigene Bedürfnisse zu sprechen."


"Erst jetzt bemerke ich, dass es etwas gibt, was sie nicht erwähnt hat. Ich entscheide mich, das anzusprechen – eher als Scherz, um zu vermeiden, dass unser Gespräch zu persönlich wird."


hi "Ach? Und was ist mit mir?"


play music music_lilly fadein 2.0

show lilly cane_smile_ni onlayer master
with charadistant

"Plötzlich läuft sie mir voraus, dreht sich um und versperrt mir den Weg."


show lilly behind_cheerful_ni onlayer master
with charachange

"Sie lächelt und hält die Hände hinter dem Rücken, während sie sich nach vorne lehnt."


li "Bei dir ist das etwas anderes."


show lilly back_giggle_ni onlayer master
show lillyprop back_cane_ni onlayer master
with charachange

"Mit diesen Worten dreht sie sich wieder um und läuft mir mit frischem Elan weiter voraus."


"Alles, was ich tun kann, ist eine Augenbraue hochziehen und verwirrt lächeln. Ich glaube, dass ich diese spielerische, neckende Seite von ihr noch nicht gesehen habe."


"Also… ist es bei mir etwas „anderes”. Ich weiß nicht, wie sie das genau gemeint hat, aber wie ich sie kenne, war diese Mehrdeutigkeit absichtlich."


"Unsere Beziehung verändert sich – und sei es nur, weil ich angefangen habe, mehr auf eigenen Füßen zu stehen und mehr über die Situation der Leute in meinem Umfeld wissen will."


"Warum das so ist… Wahrscheinlich eine Mischung aus persönlicher Neugier und einem Verlangen, einen Weg zu finden, wie ich mit meiner eigenen Situation umgehen kann."


"Was Lilly angeht bin ich mir aber weniger sicher. Deshalb hat ihre Aussage, die meinen eigenen Gefühlen so nahekommt, mich so sehr aus der Bahn geworfen."


"Während ich beobachte, wie sie die Straße entlanggeht, und ihr Stock von links nach rechts tappt, entscheide ich mich, die Angelegenheit fürs Erste ruhen zu lassen, und einfach zu lächeln."
"Das ist eine schöne Seite von ihr, und ich möchte sie nicht vergessen."


stop music fadeout 2.0

label de_L6c:


scene bg school_girlsdormhall onlayer master
with shorttimeskip

play music music_normal fadein 4.0

"Schließlich erreichen wir das Mädchenwohnheim. Meine beiden Arme tun mir wegen des Gewichts der ganzen Lebensmitteltüten weh."


hi "Hah… wir sind endlich da. Puh."


show lilly invis onlayer master:
    right
    xpos 0.95
with None

show lilly cane_smileclosed onlayer master at right
with dissolvecharamove

"Ich bücke mich und wische mir mit dem Handrücken den Schweiß von der Stirn. Lilly hält vor ihrer Tür inne, setzt die Tüte auf dem Boden ab und fischt in ihrer Tasche nach dem Schlüssel."


show lilly cane_smile onlayer master
with charachange

li "Danke, Hisao. Ich weiß deine Hilfe sehr zu schätzen."


hi "Ach was, ist doch eine Kleinigkeit."


show lilly cane_smileclosed onlayer master
with charachange

li "Es mag eine Kleinigkeit für dich gewesen sein, aber für mich war es… auf jeden Fall mehr."


show lilly invis onlayer master:
    right
    xpos 1.05
with dissolvecharamove

play sound sfx_doorclose

hide lilly onlayer master
with None

"Und mit diesen Worten tritt sie durch die Tür und schließt sie hinter sich."


"Ich blinzele. Das war einfach nur ein ehrlicher Dank, aber ich werde das Gefühl nicht los, dass da irgendwie noch mehr ist."


"Wie dem auch sei… Es gibt noch etwas, was ich tun muss, bevor ich mir darüber Gedanken machen kann."


scene bg school_dormhanako_ni onlayer master
show hanako emb_timid_close onlayer master:
    center
    xpos 0.45
show hanako_door_base onlayer master at right
show hanako_door_door onlayer master at left
with locationchange

play sound sfx_doorknock2

"Ich drehe mich zur Tür von Hanakos Zimmer und klopfe zweimal in rascher Folge. Die Tüten, die ich noch in der Hand habe, rascheln dabei."


play sound sfx_dooropen

show hanako_door_door onlayer master:
    xpos -0.05
with charamove

"Nach ein paar Sekunden öffnet sich die Tür langsam. Wenn man nicht genau hingesehen hätte, könnte man meinen, dass sie sich überhaupt nicht bewegt hat."


"Ich lege den Kopf zur Seite und versuche, durch die winzige Spalte zwischen der Tür und dem Rahmen zu spähen."


hi "Hallo Hanako, ich hab deine Sachen."


show hanako basic_normal_close onlayer master at Position(xpos=0.4)
with charachange

ha "Ah!"


show hanako_door_door onlayer master:
    xpos -0.3
show bg school_dormhanako onlayer master
with dissolvecharamove

"Und damit öffnet sie die Tür vollständig, sodass ihr schlichtes Zimmer über ihre Schulter deutlich zu sehen ist. Das Zimmer ist spärlich dekoriert und wahrscheinlich noch langweiliger als meins."


"Ich strecke den rechten Arm aus, und das Gewicht der beiden Tüten zieht ihn fast wieder herunter."


show hanako emb_smile_close onlayer master
with charachange

ha "D-Danke, Hisao."


show hanako emb_downtimid_close onlayer master
with charachange

ha "Es tut mir leid, dass du sie… den ganzen Weg hierher tragen musstest."


hi "Schon gut, mach dir keine Sorgen darüber. Verlang bloß nicht, dass ich das jeden Tag mache, okay?"


show hanako basic_normal_close onlayer master
with charachange

"Während ich fröhlich schmunzele, gebe ich ihr die Tüten. Nach der ersten Gewichtsübertragung schafft sie es problemlos, die Last zu tragen."


hi "Ich gehe dann mal los. Nacht, Hanako."


show hanako cover_bashful_close onlayer master
with charachange

ha "Gute Nacht. Ähm, b-bis morgen… in der Schule…"


show hanako_door_door onlayer master at left
with charamove

play sound sfx_doorclose

"Mit den Lebensmitteln immer noch in den Händen, verbeugt sie sich tief, tritt zurück und schließt die Tür."


stop music fadeout 5.0

scene bg school_dormext_full_ni onlayer master
with locationskip

"Auf dem Weg zu meinem eigenen Wohnheim nehme ich eine Tüte in die andere Hand, um das Gewicht auszugleichen."


"Dabei kann ich Lillys fröhliches Lächeln einfach nicht aus dem Kopf kriegen. Als ich sie zum ersten Mal getroffen habe, hätte ich es für unmöglich gehalten, dass sie so sein könnte."


"Es fühlt sich wirklich so an, als ob wir einander in den paar Wochen, seit ich sie und Hanako kennengelernt habe, nähergekommen sind."


"Die Zeit, die ich jeden Tag mit ihr verbringe. Die kleinen Momente von Freude und des Glücks, die ich erlebe, während ich ihr näherkomme."


"Obwohl ich alles andere als sicher bin, glaube ich, dass das mehr als nur normale, freundschaftliche Gefühle sind."


scene bg school_dormhisao onlayer master
with locationskip

"Nachdem ich in mein Zimmer zurückgekehrt bin, packe ich meine Lebensmittel weg und mache mich bettfertig."


show letter_insert onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Ich tausche die Bücher in meiner Tasche mit denen aus, die ich morgen brauchen werde. Dabei fällt mir der gelbe Umschlag in die Hände, den Misha mir vorhin gegeben hat."


"Ich war heute von so vielen Dingen abgelenkt, dass ich mich nicht früher damit beschäftigen konnte. Ich frage mich, wer mir geschrieben haben könnte."


"Der Name, der die Hinterseite des Umschlags säuberlich ziert, lässt mir das Blut in den Adern gefrieren. Ich habe ihre Handschrift so lange nicht mehr gesehen, dass es ziemlich unwahrscheinlich ist, dass ich sie erkannt hätte."


"„Iwanako.”"


"Warum hat sie mir geschrieben? Mir fallen keine guten Gründe dafür ein."


"Ich bin versucht, den Brief überhaupt nicht zu öffnen, aber das würde nichts bringen. Wenn ich ihn einfach ignorieren würde, dann würde allein seine Existenz an mir nagen, bis ich etwas dagegen unternehme."


scene ev hisao_letter_open onlayer master
with shorttimeskip

play music music_rain fadein 6.0

"Ich schaue auf das Blatt Papier, das auf meinem Tisch liegt. Sein helles, sommerliches Muster strahlt mich fröhlich an."


"Die Beschriftung ist rosa und beißt sich mit dem gelben Sonnenblumenrand der Karte. Die Handschrift ist ordentlich und die Schriftzeichen wurden außergewöhnlich sorgfältig geschrieben."


"Als man mir den Brief gegeben hat, habe ich kaum darüber nachgedacht, aber jetzt kann ich seinen Inhalt nicht aus dem Kopf kriegen."


window hide
nvl clear
nvl show dissolve

n "\n\n\nObwohl ich gerne sagen würde, dass ich nicht weiß, warum sie eine so altmodische Kommunikationsform benutzt hat — ein Telefonanruf oder eine E-Mail wären schneller und einfacher gewesen — scheint die Antwort eindeutig zu sein, wenn man den Inhalt bedenkt."


n "Ein Brief lässt einen bequemen Abstand zwischen dem Absender und dem Empfänger. Im Gegensatz zum Telefon, ist es nicht nötig, an einem Gespräch teilzunehmen. Und anders als bei einer E-Mail erwartet man kaum eine sofortige Antwort."


n "\nAussagen wie „Im Moment sind alle Drittklässler schon sehr angespannt wegen der Abschlussprüfungen” und „Es ist so seltsam, dass wir plötzlich die Ältesten sind, nicht wahr?” sind nur Geplauder. Und wir hätten plaudern können, wenn sie einfach irgendeine der Nachrichten, die ich ihr aus dem Krankenhaus geschickt habe, beantwortet hätte."


n "Aber das Ende ist der wahre Grund, warum sie dies geschickt hat. Genauer gesagt die letzten paar Zeilen, die fast ein nachträglicher Einfall zu sein scheinen."


nvl clear

n "\n\n\n\n\n\n\n„Ich frage mich, ob wir uns irgendwann einmal wiedersehen. Vielleicht wäre es besser, wenn nicht?”"


n "Es ist eine Aussage, die wehtun sollte. Ich habe schon immer gehört, dass Beziehungen böse enden könnten, aber das hier fühlt sich eher an wie eine Bestätigung von etwas, das wir beide schon wussten."


n "Es ist das vorangehende Geplauder, das mich etwas unsicher macht. Und egal, wie lange ich hier sitze und auf dieses helle, sommerliche Blatt Papier hinunterblicke, ich werde daraus nicht schlau."


nvl clear

n "\n\n\n\n\n\n\n\n„Trotzdem, wenn du mir antworten willst, schreib mir bitte zurück.”"


n "Es ist nur zu offensichtlich, dass man auf diese Art von Brief nicht antworten soll. Letzten Endes ist dieser Brief nicht mehr als ein einfaches Abstreifen der Verantwortung; eine letzte, selbstberuhigende Aussage, mit der sie sich klarmacht, dass unsere Beziehung vorbei ist."


stop music fadeout 3.0

nvl hide dissolve
nvl clear

scene bg school_dormhisao onlayer master
with locationchange

window show

"Daher habe ich kein Problem damit, Brief und Umschlag zu einem Ball zusammenzuknüllen und in den Mülleimer zu werfen, um sie endlich loszuwerden."


"Ich gehe mit gemischten Gefühlen ins Bett. Dieser Geist aus meiner Vergangenheit hat meinen angenehmen Abend völlig verdorben."


"Ironischerweise dauert es eine Weile, bis ich einschlafen kann."


scene black onlayer master
with dissolve

$ suppress_window_after_timeskip = True


label de_L7:

window hide None

scene black onlayer master
with dissolve

nvl show dissolve

n "\n\n\n\nIch schwitze heftig. Der gefürchtete Moment steht vor der Tür."



$ renpy.music.set_volume(0.7, 0.0, channel="music")
play music music_tension fadein 6.0

n "Meine Muskeln spannen sich mit jedem Ticken der Uhr weiter an. Von Minute zu Minute sträuben sich mir mehr Nackenhaare."


n "Er greift nach mir. Ich kann ihn spüren."


play sound sfx_slide

n "\n\n{image=vfx/reddash.png}{color=#FF0000}{b}Der Tod.{/b}{/color}"


n "\n\nDer Tod kommt in der Form eines einzigen Blattes Papier."


$ renpy.music.set_volume(1.0, 0.5, channel="music")

nvl clear
nvl hide dissolve

scene bg school_scienceroom onlayer master at bgright
with locationchange

window show

"Ich nehme den kleinen Papierstapel von der Schülerin, die vor mir sitzt, entferne das oberste Blatt, und reiche den Rest nach hinten."


"Ich schaue mir die obere rechte Ecke des Blattes an und stelle fest, dass sich meine Befürchtungen innerhalb eines kleinen, roten Kreises bewahrheitet haben."


stop music
play sound sfx_thunder
with vpunch

"Dreiundvierzig."


"Ich lasse den Kopf hängen und seufze schicksalsergeben. Während ich im Flütsterton fluche, spüre ich die Aura eines ähnlichen Gefühls von der ganzen Klasse. Seltsamerweise hellt das meine Stimmung ein wenig auf."


"Geteiltes Leid ist halbes Leid, vermute ich."


"Die Lehrerin öffnet den Mund und die Klasse macht sich auf den unvermeidlichen, verbalen Angriff gefasst…"


play music music_normal fadein 1.0

play sound sfx_normalbell

"… wird aber in allerletzter Minute gerettet."


"Wir beeilen uns, unsere Taschen zu holen und schnellstens in die Mittagspause zu gehen, aber die Lehrerin setzt uns noch einen Schuss vor den Bug."


"Lehrerin" "Wir werden die Testergebnisse in der nächsten Unterrichtsstunde besprechen. Ich glaube, dass ich nicht erwähnen muss, dass es eine ziemlich intensive Besprechung wird."


"Ein kollektives Stöhnen hallt von den Wänden wider, und wir schlurfen niedergeschlagen aus dem Zimmer."


scene bg school_hallway3 onlayer master at bgright
with locationchange

"Während ich den Gang entlanggehe, schiebe ich das Blatt in meine Tasche und zerknittere es dabei. Dass gestern so ein lästiger Brief auf meinem Tisch gelandet ist, war schlimm genug – und jetzt das."


hi "Ich hasse Englisch…"


stop music fadeout 0.7

mystery "HI—{w=0.3}SA—{w=0.3}O!"


"Eine strenge, weibliche Stimme ruft mich von hinten."


play music music_tension

"Ich bleibe auf der Stelle stehen. Mein Gesicht versteinert sich. Ich kann praktisch fühlen, wie mein Gehirn sich von meinem Körper trennt."


"Meine Augen bewegen sich langsam nach rechts. Ich versuche, einen Blick auf die körperlosen Stimme zu erhaschen."


stop music fadeout 0.3

"… nichts?"


"Mein Gesicht entspannt sich langsam wieder. Ich entscheide mich, das Risiko einzugehen, meinen Kopf etwas zu drehen—"


play sound sfx_impact

hi "WAAAAH!" with vpunch


"Ich springe in die Luft, lasse meine Tasche fallen und schreie überrascht auf."


"Nachdem ich mich erholt und die Fassung wiedererlangt habe, drehe ich mich um und sehe… Ich hätte es ahnen sollen."


hi "Emi."


play music music_running

show emi excited_proud onlayer master at center
with charaenter

emi "Erwischt, Hisao."


"Sie steht mit einem diebischen Grinsen und ausgestreckten Händen da. Sie ist diejenige, die mich gerade mit den Zeigefingern in die Rippen gepiekst hat."


"Ich schaue mit einem dunklen Blick zu ihr hinunter und reibe mir frustriert den Kopf."


hi "Dir ist hoffentlich klar, dass das keine Art ist, jemanden zu begrüßen."


show emi sad_pout onlayer master
with charachange

emi "Du hast keinen Sinn für Humor."


hi "Ich habe meinen Sinn für Humor im Englischunterricht zurückgelassen. Du kannst dich bei Frau Miyagi beschweren, wenn du willst, dass ich ihn zurückkriege."


show emi sad_shy onlayer master
with charachange

"Sie schmollt und schaut mich mit ihrem besten Welpenblick an. Obwohl ich dank Lilly eine Resistenz gegen diese Taktik aufgebaut habe, steigert Emis kurze Statur die Wirkung so stark, dass ich nachgeben muss."


hi "Also, wie geht's? Du hast dich eine Zeit lang nicht blicken lassen."


show emi basic_closedgrin onlayer master
with charachange

emi "Alles beim Alten. Ich renne so schnell, dass niemand morgens mit mir laufen will."


show emi basic_annoyed onlayer master
with charachange

emi "Das nervt wirklich."


"Ihre Bescheidenheit amüsiert mich immer wieder."


show emi basic_grin onlayer master
with charachange

emi "Obwohl…"


"Oh oh."


show emi sad_shy onlayer master
with charachange

emi "Du weißt doch, was ich denke, oder, Hisao?"


"Dass ich meine Gefühle so offen zeige, ist einer meiner schlechtesten Angewohnheiten. Sie hat mich durchschaut."


"Glücklicherweise kommt jemand auf uns zu, der mir einen Ausweg bieten kann."


hi "Oh, hallo Hanako."


show emi sad_shy onlayer master at twoleft
show bg school_hallway3 onlayer master at center
with charamove

show hanako emb_downtimid onlayer master at tworight
with charaenter

"Ich winke ihr zur Begrüßung zu und versuche mein Bestes, so auszusehen, als hätte ich Emis schmollendes Gesicht nicht bemerkt. Sie winkt kurz zurück."


show hanako emb_smile onlayer master
with charachange

ha "H-Hallo, Hisao… Emi."


show emi basic_closedgrin onlayer master
with charachange

emi "Hey Hanako."


hi "Sag Lilly, ich bin gleich da."


hi "Wo wir gerade von Mittagsbegleitung sprechen, Emi, es ist seltsam, dich ohne Rin zu sehen."


show emi basic_shock onlayer master
show hanako defarms_shock onlayer master
with vpunch

emi "Ah! Rin!"


stop music fadeout 3.0

hide emi onlayer master
with easeoutleft

"Ohne ein weiteres Wort vergisst Emi uns komplett und saust den Gang hinunter. Anscheinend hat sie vergessen, dass Rin auf sie wartet."


"Hanako und ich sind sprachlos. Wir können nur hilflos dastehen und zuschauen, wie dieses Bündel von anscheinend grenzenloser Energie davonflitzt."


play music music_running

show emi basic_closedgrin onlayer master at left
with easeinleft

emi "Ach ja, Hisao…"


"Kurz bevor sie um die Ecke zum Treppenhaus verschwindet, hält sie plötzlich an und wendet sich uns noch einmal zu."


show emi excited_proud onlayer master
with charachange

emi "Ich hasse Englisch auch."


stop music fadeout 4.0

hide emi onlayer master
with easeoutleft

"Und damit verschwindet sie."


"Alles, was mir bleibt, ist den Kopf hängen zu lassen und einen langen Seufzer von mir zu geben."


show hanako basic_smile onlayer master
with charachange

"Ich höre ein kurzes Kichern hinter mir, drehe mich um und sehe, wie Hanako in die Richtung der Ecke lächelt, um die meine Angreiferin gebogen ist."


play music music_daily fadein 4.0

show hanako basic_smile onlayer master at center
show bg school_hallway3 onlayer master at bgleft
with charamove

"Ich hebe meine Tasche vom Boden auf und wische sie schnell ab."


hi "'Tag. Bis du in letzter Zeit sehr beschäftigt?"


show hanako def_worry onlayer master
with charachange

ha "Du magst kein… Englisch?"


hi "Hmm? Oh, äh, nö. Wir haben doch gerade den Englischtest zurückgekriegt, und Emi hat mich erwischt, während ich über die Ergebnisse gegrübelt habe."


show hanako emb_downsad onlayer master
with charachange

ha "Ah, tut mir leid…"


"Sie wendet ihren Blick schuldbewusst ab. Ein zufälliger Betrachter würde denken, dass sie mich gerade aus Versehen an einen toten Bekannten erinnert hat."


hi "Komm schon, es ist nicht deine Schuld. Wie sieht es bei dir in dem Fach aus?"


show hanako emb_sad onlayer master
with charachange

"Sie hebt ihren Kopf, vermeidet aber immer noch, mir direkt in die Augen zu sehen."


show hanako basic_worry onlayer master
with charachange

ha "In Ordnung… denke ich."


"Eine peinliche Stille folgt. Das scheint in Hanakos Gegenwart häufiger vorzukommen."


show hanako basic_bashful onlayer master
with charachange

ha "Oh, Lilly hat gefragt, ob du… uns beim Mittagessen auf dem Dach Gesellschaft leisten willst?"


"Na ja, warum nicht? Ich habe keine dringenden Termine, um die ich mich kümmern müsste."


hi "Klar. Ich bin gleich bei euch."


show hanako cover_distant onlayer master
with charachange

ha "Äh, dann… hole ich mal mein Mittagsessen aus der Cafeteria…"


hi "Na dann los. Du brauchst dazu nicht meine Erlaubnis, weißt du?."


show hanako basic_smile onlayer master
with charachange

ha "O-Okay. Ich… gehe dann mal."


hide hanako onlayer master
with charaexit

stop music fadeout 5.0

"Sie gibt eine scheue Antwort, nickt kurz und verschwindet in Richtung der Cafeteria."


play ambient sfx_crowd_indoors fadein 2.0

show crowd onlayer master:
    bgleft
    alpha 0.0
    parallel:
        ease 1.0 center
    parallel:
        linear 2.0 alpha 1.0
with None

show bg school_hallway3 onlayer master at center
with dissolvecharamove

"Ich nehme an, dass sie heute vergessen hat, ihr Mittagsessen mitzubringen. Während ich durch die Gänge wandere, kommen immer mehr Schüler aus den Klassenzimmern und gehen an mir vorbei in dieselbe Richtung wie Hanako."


"Als ich endlich die Treppe erreiche, muss ich mich an einer eifrig plaudernden Gruppe von Schülern vorbeidrängen."


stop ambient fadeout 0.5

scene bg school_staircase1 onlayer master
with locationchange

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_rooftop

"Endlich schaffe ich es, mich durch die Menge zu drängen, und steige die Treppen hinauf. Vor Erleichterung sacke ich ein bisschen zusammen und verlangsame mein Lauftempo, bevor ich die Tür zum Dach öffne."


play sound sfx_door_creak
$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

scene bg school_roof onlayer master
show white onlayer master
with locationchange

hi "Ah, verdammt!"


"Die grelle Sommersonne blendet mich einen Moment lang, und ich wende meine Augen ab."


show white onlayer master:
    alpha 1.0
    linear 10.0 alpha 0.0

show lilly basic_smile behind white onlayer master:
    left
    ypos 1.2
show emi basic_grin behind white onlayer master:
    center
    ypos 1.15
show rin basic_absent behind white onlayer master:
    right
    ypos 1.17
with charaenter

mystery "Hmm?"


play music music_soothing fadein 8.0

"Langsam gewöhnen sich meine Augen an die Helligkeit, und meine Umgebung nimmt endlich Form an."


"Lilly, Emi und Rin sitzen zusammen auf dem Schuldach. Die Baumwipfel des Waldes, der Yamaku umgibt, sind hinter dem Sicherheitsgitter sichtbar."


show emi basic_closedgrin onlayer master
with charachange

emi "Ah, Hisao!"


show lilly basic_smileclosed onlayer master
show rin basic_deadpannormal onlayer master
with charachange

"Lilly nickt kurz zur Begrüßung; Rin langsam und bedächtig."



"Ich gehe auf die ziemlich ungleiche Gruppe zu und bewundere die Geschwindigkeit, mit der Emi den Rest ihrer halb aufgegessenen Banane verputzt."


hi "Hallo. Es ist merkwürdig, euch drei so zusammensitzen zu sehen."


show lilly basic_weaksmile onlayer master
with charachange

li "Es scheint ein Tag voller Zufälle zu sein. Emi und Rin wollten auf dem Dach essen, genau wie Hanako und ich."


show emi basic_annoyed onlayer master
with charachange

emi "Ihr habt ihn gestohlen! Das war unser Platz!"


hi "Beruhige dich. Man kann einen Platz in der Schule nicht stehlen."


"Ich setze mich neben Lilly, wodurch wir Vier einen Halbkreis bilden."


show rin basic_deadpanupset onlayer master
with charachange

rin "Ich denke, dass sie Recht hat."


hi "Du auch?"


show rin basic_deadpan onlayer master
with charachange

rin "Der Schmetterling ist ihr Komplize."


hi "Der Schmetter…"


"Ich schaue mich um und sehe, dass tatsächlich ein kleiner, gelber Schmetterling durch mein Blickfeld schwebt."


hi "Kannst du mir erklären, wie genau dieser Schmetterling Lilly geholfen haben soll, diesen Platz zu „stehlen”?"


show rin basic_lucid onlayer master
with charachange

rin "Er hat uns belauscht und es ihr berichtet."


"Ich hätte von Rin kein folgerichtiges Denken erwarten sollen. Trotzdem schadet es niemandem, wenn ich weiterhin mitspiele."


hi "Du behauptest, dass sie mit Schmetterlingen reden kann?"


show rin basic_awayabsent onlayer master
with charachange

rin "Es gibt Leute, die mit Pferden reden können. Die nennt man Pferdeflüsterer."


show rin basic_deadpanamused onlayer master
with charachange

rin "Lilly muss eine Schmetterlingsflüsterin sein."


"Ich vergrabe meinen Kopf in den Händen, während Emi ihrer merkwürdigen Kameradin widerspricht. Sie scheint Rins Sinn für Humor nicht zu teilen."


show emi basic_confused onlayer master
with charachange

emi "So funktioniert Tierflüstern nicht!"


"Während Emi und Rin ihre Neckerei fortsetzen, wende ich mich Lilly zu, die eifrig ihre kleine Büchse mit Curry und Reis aufisst."


hi "Wieso seid ihr heute überhaupt hier oben?"


show lilly basic_smile onlayer master
with charachange

li "Ein wenig frische Luft ab und zu schadet niemandem."


show emi basic_shock onlayer master
with charachange

emi "Ah!"


"Emi bricht ihren vergeblichen Versuch ab, Rin das Konzept von Logik beizubringen."


show emi sad_annoyed onlayer master
with charachange

emi "Deshalb sind wir auch hier heraufgekommen!"


"Etwas sagt mir, dass sie allein die Idee hatte und Rin nur von Emi hier hochgeschleppt wurde. Andererseits trifft das wohl auch auf Lilly und Hanako zu."


show lilly basic_weaksmile onlayer master
with charachange

li "Aber, aber. Wir können doch teilen."


$ renpy.music.set_volume(0.001, 1.0, channel="music")

play sound sfx_door_creak

show lilly basic_surprised onlayer master
show emi basic_hes onlayer master
show rin basic_awayabsent onlayer master
with charachange

"Kaum hat sie die Worte ausgesprochen, ist das Knarren der Tür zu hören. Unsere Aufmerksamkeit richtet sich auf die Gestalt, die gerade dort erschienen ist."


show lilly basic_surprised onlayer master:
    xanchor 0.5 xpos 0.4
show emi basic_hes onlayer master:
    xpos 0.68
show rin basic_awayabsent onlayer master:
    xpos 1.08
show bg school_roof onlayer master at bgright
hide white onlayer master
with charamove

show hanako basic_distant onlayer master:
    xanchor 1.0 xpos 0.0 yalign 1.0
    easein 3.0 xanchor 0.0 xpos -0.06
    ease 1.0 ypos 1.17
with None

"Hanako läuft langsam zu uns hinüber. Ihre Augen sind auf den Boden fixiert; die Aufmerksamkeit, die auf sie gerichtet ist, ist ihr sichtlich unangenehm. Als ihre Augen die von Rin treffen, wird sie zusehends angespannter."


"Ich kann nicht anders, als eine Augenbraue hochzuziehen, als sie zu uns hinüberläuft und sich neben mich setzt. Sie tut ihr Möglichstes, nicht hochzuschauen – sogar als sie in das Brot aus der Cafeteria beißt."


show rin basic_absent onlayer master
show emi basic_grin onlayer master
show hanako basic_normal onlayer master:
    xanchor 0.0 xpos -0.06 ypos 1.17
with charachange

hi "Also, woher kennt ihr euch überhaupt?"


$ renpy.music.set_volume(1.0, 8.0, channel="music")

show lilly basic_smileclosed onlayer master
show rin basic_awayabsent onlayer master
with charachange

li "Emi ist an dieser Schule wegen ihrer athletischen Begabung ziemlich bekannt. Sie ist mit Abstand das schnellste Mitglied der Leichtathletikmannschaft, und hat bei dem Turnier letzte Woche sogar Miki Miura geschlagen."


"Miki Miura… das gebräunte Mädchen, das in der ersten Reihe meiner Klasse sitzt. Angesichts ihrer Größe und ihres durchtrainierten Körpers ist Emis Sieg noch beeindruckender."


show emi excited_amused onlayer master
with charachange

"Ich schaue zu Emi hinüber. So stolz wie sie dreinschaut ist es offensichtlich, dass sie sich dieser Tatsache bewusst ist."


show emi excited_happy onlayer master
with charachange

emi "Also, Hisao. Wie ist deine Englischnote?"


"Autsch."


show rin basic_absent onlayer master
with charachange

hi "Kein Kommentar."


show emi basic_annoyed onlayer master
show rin basic_awayabsent onlayer master
with charachange

emi "Pah~."


"Sie bläst ihre Wangen auf und schmollt, kommt aber ziemlich schnell wieder auf die Beine. Rein bildlich gesprochen natürlich."


show emi excited_proud onlayer master
with charachange

emi "Also gut, wenn ich dir meine Note sage, dann musst du mir deine sagen. Einverstanden?"


stop music fadeout 4.0

show rin basic_absent onlayer master
with charachange

hi "Schon gut, schon gut."


show emi basic_closedhappy onlayer master
show rin basic_awayabsent onlayer master
with charachange

emi "Okay, ich werde bis drei zählen, dann sagen wir beide unsere Ergebnisse."


show emi excited_joy onlayer master
with charachange

emi "Eins…{w=1.0} Zwei…{w=1.0} Drei!{w=1.0}{nw}"


show emi basic_closedgrin onlayer master
with charachange

$ doublespeak (hi, emi, u"…", u"Zweiunddreißig!")


"Ich grinse sie frech an."


play music music_comedy

show hanako cover_smile onlayer master
show lilly basic_cheerful onlayer master
show rin basic_amused onlayer master
show emi excited_sad onlayer master
with charachange
with vpunch
play sound sfx_impact

emi "Ah! Du bist gemein! Gemein, gemein, gemein, gemein!"


show rin basic_absent onlayer master
with charachange

hi "Du hast es gesagt, nicht ich. Trotzdem ist es irgendwie erstaunlich, dass du eine noch niedrigere Note hast als ich."


show emi sad_grit onlayer master
show rin basic_awayabsent onlayer master
with charachange

emi "Grr~!"


"Sie sieht aus wie ein kleiner Terrier, der einen Eindringling anknurrt – nicht gerade der furchterregendste Anblick."


show lilly basic_displeased onlayer master
show hanako basic_normal onlayer master
with charachange

li "Wie dem auch sei, bei einer Prüfung mehr als zweiunddreißig Prozent zu erreichen, ist kein Grund zum Angeben – von weniger ganz zu schweigen. Egal in welchem Fach."


show rin basic_absent onlayer master
with charachange

hi "Ja, Lilly."


show rin basic_awayabsent onlayer master
show emi sad_shy onlayer master
with charachange

emi "Tut mir leid, Lilly."


show lilly basic_smile onlayer master
with charachange

li "Ich kann dir mit deinem Englisch helfen, wenn du willst. Es wäre mir ein Vergnügen, wenn—"


show emi basic_closedgrin onlayer master
with charachange

emi "Nee, nee, geht schon. Aber danke für das Angebot. Wirklich."


show lilly basic_reminisce onlayer master
show hanako basic_smile onlayer master
show rin basic_deadpanamused onlayer master
with charachange

"Lilly sieht etwas enttäuscht aus. Sie hat wohl gehofft, ihr Wissen weitergeben zu können. Aber nach dem schlecht versteckten Gelächter von uns anderen zu urteilen, gibt es weder für sie noch für Emi allzu viel Mitleid."


stop music fadeout 0.5
$ renpy.music.set_volume(0.0, 4.0, channel="ambient")

window hide

play sound sfx_heartslow
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.7)

window show

"Aber als ich dasitze und glücklich lache, spüre ich, wie meine Stimme abgeschnitten wird, als meine Brust sich plötzlich zusammenzieht."


window hide

play sound sfx_heartslow
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.7)

window show

"Ein paar Sekunden lang sitze ich schweigend da, meine gesamte Konzentration auf meinem Herzschlag gerichtet. Obwohl der Schmerz nicht schlimm ist, fühlt es sich an, als würde er heftiger werden."


play music music_tragic fadein 0.5

window hide

play sound sfx_heartslow
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.2)

with Pause(0.7)

play sound sfx_heartfast
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.2)

window show

"Tief durchatmen… tief durchatmen…"


window hide

play sound sfx_heartfast
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.2)

window show

"Ich blicke kurz auf und versuche, zumindest einen Teil meiner Aufmerksamkeit auf meine Umgebung zu richten. Dann sehe ich, wie Emi plötzlich erstarrt, als sie aus dem Augenwinkel den Ausdruck von Schmerz auf meinem Gesicht bemerkt."


show emi basic_hes onlayer master
with charachange

emi "Hey Hisao… bist du okay?"


show hanako def_worry onlayer master
show lilly basic_surprised onlayer master
show rin basic_deadpanupset onlayer master
with charachange

hi "Ja, es geht… mir gut…"


window hide

play sound sfx_heartfast
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.2)

window show

"Ich schaue wieder nach unten, strenge mich stärker an, mich zu beruhigen und balle die Fäuste in einem Versuch, den Schmerz zu betäuben."


window hide

play sound sfx_heartfast
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.2)

with Pause (0.7)

play sound sfx_heartslow
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.2)

stop music fadeout 4.0

window show

"Es dauert eine kurze Zeit, aber glücklicherweise fängt der Schmerz an nachzulassen."


$ renpy.music.set_volume(0.5, 4.0, channel="ambient")

"Als ich wieder nach oben blicke, sehe ich nur eine Reihe von ernsten Gesichtern. Ich glaube, dass ich das erklären sollte."


play music music_rain fadein 10.0

hi "Arrhythmie. Mir geht's gut, es ist… nur ein Herzflimmern."


show lilly basic_listen onlayer master
with charachange

li "Bist du dir ganz sicher? Sollen wir Doc holen?"


show hanako def_worry onlayer master:
    ypos 1.0
with ease

"Hanako nimmt das als Zeichen, steht schnell auf, und läuft los in Richtung Treppenhaus."


hi "Hanako, warte! Lilly, es geht mir gut."


show rin basic_deadpan onlayer master
with charachange

rin "Du siehst wie eine nasse, runzlige Tomate aus."


hi "Hä?"


"Als ich mir mit der Hand an die Stirn fasse, kann ich die Schweißperlen dort spüren und tupfe sie mit meiner Manschette ab."


hi "Danke. Wie ich schon sagte, es geht mir gut. Ich bin nur irgendwie… anfällig, denke ich."


show hanako basic_worry onlayer master
with charachange

show hanako basic_worry onlayer master:
    ypos 1.17
with charamove

show emi sad_shy onlayer master
show rin basic_deadpanupset onlayer master
show lilly basic_sleepy onlayer master
with charachange

"Die ganze Stimmung hat sich verändert. Statt Fröhlichkeit gibt es jetzt betrübte Mienen, und die Situation ist so unangenehm, dass niemand weiß, wie er reagieren soll."


"Und natürlich ist das Ganze mir zu verdanken. Es musste gerade jetzt passieren, während ich mit anderen zusammen bin."


stop music fadeout 8.0

show lilly basic_weaksmile onlayer master
with charachange

li "Oh, Emi?"


show emi basic_hes onlayer master
show rin basic_awayabsent onlayer master
with charachange

emi "Hmm?"


"Sie schaut auf; ein Trinkpäckchen auf dem halben Weg zu ihrem Mund."


show lilly basic_smileclosed onlayer master
with charachange

li "Ich habe dir noch nicht von meinem Testergebnis erzählt, oder?"


show emi basic_annoyed onlayer master
with charachange

emi "Na ja, du bist halb Ausländerin, also zählt dein Testergebnis sowieso nicht."


"Ich ziehe eine Augenbraue hoch und wende mich neugierig Lilly zu."


show rin basic_absent onlayer master
with charachange

hi "Was war denn dein Testergebnis?"


show lilly basic_cheerful onlayer master

"Sie setzt ein freches Grinsen auf."


show rin basic_awayabsent onlayer master
show lilly basic_planned onlayer master
with charachange

li "Einhundert Prozent. Höchstpunktzahl."


play music music_lilly fadein 0.5

"Unglaublich. Vor Staunen bleibt mir der Mund offen hängen."


"Wenn man bedenkt, dass diese Prüfungen selbst für einige Muttersprachler wahn- sinnig schwer sind, kann ich mir nur vorstellen, dass sie einen Teil des Wörterbuches auswendig gelernt hat oder so was. Vielleicht hat sie ein Talent fürs Auswendiglernen."


show rin basic_absent onlayer master
with charachange

hi "Das ist…"


show rin basic_awayabsent onlayer master
show emi sad_pout onlayer master
with charachange

emi "Siehst du? Nur jemand, der halb Ausländer ist, kann eine so gute Note kriegen."


show rin basic_absent onlayer master
with charachange




show rin basic_awayabsent onlayer master
show emi basic_closedsweat onlayer master
with charachange

emi "Äh…"


show lilly basic_giggle onlayer master
show hanako basic_smile onlayer master
with charachange

"Lilly und ich grinsen und amüsieren uns auf Emis Kosten, da sie genauso reagiert hat wie ich, als ich zum ersten Mal in dieses Fettnäpfchen getreten bin. Aber Lillys ausländische Abstammung bringt mich auf etwas anderes."


show rin basic_absent onlayer master
with charachange

hi "Ah, stimmt ja… Du reist morgen nach Schottland ab, nicht wahr?"


show rin basic_awayabsent onlayer master
show lilly basic_smile onlayer master
with charachange

li "Ganz recht. Emi hat einige Gerüchte darüber gehört. Es hat sich anscheinend schnell herumgesprochen, wenn man bedenkt, dass ich erst vor ein paar Tagen einer Freundin in meiner Klasse davon erzählt habe."


show emi sad_grin onlayer master
with charachange

emi "Es muss schön sein, um die halbe Welt in den Urlaub zu fahren."


show emi excited_happy onlayer master
with charachange

emi "Hey, kannst du etwas für mich kaufen, wenn du da bist?"


show rin basic_absent onlayer master
with charachange

hi "Sei doch nicht so schüchtern."


show lilly basic_giggle onlayer master
with charachange

"Lilly kichert fröhlich. Offensichtlich hat sie Emis direkte Art erwartet."


"Der Rest unseres Mittagessens geht wie zuvor weiter. Glücklicherweise kehrt die Heiterkeit, die vor meinem Herzflattern vorhanden war, vollständig zurück."


stop music fadeout 8.0

scene bg school_roof onlayer master
show lilly basic_smileclosed onlayer master:
    center
    ypos 1.2
with shorttimeskip

"Die anderen verabschieden sich nacheinander, bis nur noch Lilly und ich übrig sind."


hi "Hey, Lilly?"


"Sie packt ihre letzten Sachen in ihre Tasche und lässt den Verschluss einrasten, bevor sie den Kopf leicht hebt."


show lilly basic_smile onlayer master
with charachange

li "Hmm?"


hi "Äh… Danke, dass du die Stille vorhin gebrochen hast. Ich wollte selbst etwas sagen, wusste aber nicht wirklich was."


"Ich wünschte, ich würde mich nicht so niedergeschlagen anhören, aber nach dem Brief gestern, dem vermasselten Test, und nun meinem Herzflattern fällt mir das wirklich schwer."


show lilly basic_weaksmile onlayer master
with charachange

"Sie lächelt gutmütig und nickt. Ich hoffe, dass sie es nicht mitbekommen hat, aber wie ich sie kenne, ist das eher unwahrscheinlich."


li "Emi ist stark, aber auch nur ein Mensch. Wir machen uns Sorgen um dich, Hisao."


hi "Moment mal, warum sollte ich euch Sorgen machen?"


$ renpy.music.set_volume(0.5, 2.0, channel="ambient")

show lilly basic_displeased onlayer master
with charachange

"Ihr Lächeln verschwindet und sie wird unangenehm ernst."


li "Hisao, wir kennen deine Situation."


li "Im Gegensatz zu…"


show lilly basic_concerned onlayer master
with charachange

"Sie unterbricht sich, da sie unsicher ist, ob sie weitersprechen sollte. Ich lächle schwach und lege meine Hand auf ihre Schulter."


play music music_twinkle fadein 10.0

hi "Tu es nicht. Es reicht, dass ich mir darum Sorgen mache. Ich will nicht, dass euch das auch noch zu schaffen macht."


show lilly basic_oops onlayer master
with charachange

li "Aber…"


hi "Wenn ihr euch um mich Sorgen macht, dann muss ich mir Sorgen um eure Sorgen machen. Wenn… das einen Sinn ergibt."


hi "Es geht mir gut, okay?"


show lilly basic_reminisce onlayer master
with charachange

"Einen Augenblick lang sieht sie gedankenverloren aus, während sie überlegt, wie sie reagieren soll."


show lilly basic_weaksmile onlayer master
with charachange

li "Hisao, hast du noch Papier von deiner Lebensmittelpackung übrig?"


hi "Ich… denke schon? Ich seh mal nach."


play sound sfx_rustling

"Ich wühle in meiner Tasche nach den Resten meines Mittagsessens herum. Schließlich finde ich ein quadratisches Stück Papier von meiner Sandwichverpackung."


"Mit hochgezogener Augenbraue und einem fragenden Blick lege ich das Quadrat vorsichtig in Lillys Hand. Wortlos tastet sie es ab, um die Ränder zu ertasten."


show lilly basic_smile onlayer master
with charachange

li "Das müsste groß genug sein…"


"Da wir beide auf dem Schuldach sitzen und die verbleibende Zeit bis zum Unterrichtsbeginn immer knapper wird, legt sie den Gegenstand auf dem Boden und fängt mit ihrer Arbeit an."


show lilly basic_smileclosed onlayer master
with charachange

"Schweigend schaue ich zu, wie ihre Finger sich mit erstaunlichem Geschick über das kleine Quadrat bewegen. Eine kleine Falte hier, ein größere Falte dort… ihre Fingerspitzen arbeiten langsam aber gewissenhaft."


"Ich schaue auf und sehe, dass ihr Ausdruck gelassen und friedlich ist. Die Tatsache, dass ihr Gesicht deutlich oberhalb des Blattes vor ihr gerichtet ist, macht den Anblick Ihrer Arbeit noch seltsamer."


"Nachdem sie eine letzte Falte gemacht und damit ihre Arbeit anscheinend beendet hat, lässt sie die Schultern ein bisschen sinken. Aber erst als sie den Gegenstand in ihren Händen hochhält, erkenne ich, was es ist."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene white onlayer master
with dissolve

with Pause(0.1)

scene ev lilly_crane onlayer master:
    truecenter
    zoom 1.1 subpixel True
    ease 15.0 zoom 1.0
with Dissolve(4.0)

"Ein kleiner Origami-Kranich."


"Dank des Papiers, das benutzt wurde, ist er hellbraun. Das Ergebnis sieht ziemlich zierlich und präzise aus."


hi "Du kannst Origami?"


li "Ich habe es mir selbst beigebracht, als ich jünger war. Es hat meine Fingerfertigkeit etwas verbessert."


hi "Hmm…"


"Ein wenig verblüfft nehme ich den kleinen Vogel vorsichtig aus ihren blassen Händen, als ob er beim leisesten Windhauch zerbrechen würde. Er scheint ziemlich gut gefaltet zu sein und hält problemlos seine Form."


$ renpy.music.set_volume(1.0, 2.0, channel="music")

scene bg school_roof onlayer master
show lilly cane_smile onlayer master at center
with locationskip

"Wir greifen beide nach unseren Taschen und gehen durch die Tür, wobei Lilly ihren Blindenstock ausfährt."


stop ambient fadeout 2.0

scene bg school_hallway3 onlayer master
with locationskip

"Ich halte Lillys Werk vor mein Gesicht, um es genauer zu betrachten, während wir den Gang entlanggehen. Um sich zu orientieren, streift sie mit ihrer Hand an den silbernen Geländern entlang."


"Wenn sie sich selbst Origami beigebracht hat, um ihre Handfertigkeit zu verbessern, und die Verwendung von Händen ihr so viel bedeutet in Anbetracht ihrer Situation… Ach, so ist das."


"Als ich die Bedeutung des Vogels begreife, lächle ich."


"„Alle, die hier sind, mussten ihren eigenen Weg finden, um mit ihrer Situation fertigzuwerden. Hier bist du nicht allein, wenn du Probleme hast.”"


hi "Danke, Lilly. Ich schätze das wirklich sehr."


show lilly cane_cheerful onlayer master
with charaenter

"Sie lächelt süß und nickt. Es ist typisch für sie, keine Worte zu benutzen, wenn keine benutzt werden müssen."


show lilly cane_smileclosed onlayer master
with charachange

li "Ich möchte einfach nur, dass du auf dich aufpasst, Hisao."


hi "Keine Sorge, das werde ich."


show lilly cane_smile onlayer master
with charachange

li "Versprochen?"


hi "Versprochen."


hide lilly onlayer master
with charaexit

stop music fadeout 7.0

"Und damit trennen sich unsere Wege."


"Um ehrlich zu sein, weiß ich nicht, was ich lästiger finde: Dass ich jederzeit tot umfallen könnte oder dass das alle wissen."


"Ich nehme an, dass ich einfach in den Tag hineinleben muss. Das unerwartete Geschenk in meiner Hand erinnert mich daran, dass ich nicht allein hier bin. Selbst wenn ich so bin, wie ich bin, bin ich nicht allein."


"Wenn sie sich Sorgen machen – wenn irgendjemand sich Sorgen macht – werde ich lächeln."


"Ich werde genug lächeln, um sicherzustellen, dass all ihre Sorgen verschwinden."


scene black onlayer master
with dissolve



label de_L8:

scene black onlayer master
with dissolve

play sound sfx_normalbell

scene bg school_scienceroom onlayer master
show muto normal onlayer master at center
with locationchange

"Das Klingeln der Schulglocke lässt die ganze Klasse erleichtert aufatmen."


play music music_happiness fadein 2.0

"Der Großteil des Morgens fiel einer langatmigen Vorlesung über Stöchiometrie zum Opfer. Angesichts der unerträglichen Hitze im Klassenzimmer scheint dieses Thema völlig unpassend."


hide muto onlayer master
with charaexit

"Da ihm bewusst ist, dass der Versuch, uns irgendetwas Weiteres beizubringen, die reinste Zeitverschwendung wäre, gibt Mutou für heute auf und fängt an, das Unterrichtsmaterial von seinem Tisch zu räumen."


$ renpy.music.set_volume(0.7, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 0.5

show hanako basic_normal onlayer master at center
with charaenter

"Während inhaltsloses Geplauder das Klassenzimmer füllt, merke ich, wie Hanako aufsteht und auf meinen Tisch zu kommt. Sie ist in letzter Zeit weit weniger zurückgezogen – eine Entwicklung, mit der ich sehr zufrieden bin."


show hanako basic_smile onlayer master
with charachange

ha "Hallo, Hisao."


hi "Hey. Wollen wir Lilly abholen gehen? Sie muss sich langsam auf den Weg machen, wenn sie ihren Flug noch erwischen will."


show hanako cover_worry onlayer master
with charachange

ha "Äh… Wegen Lilly…"


show hanako basic_worry onlayer master
with charachange

ha "Sie hat gesagt, dass sie vielleicht von ihren Klassenkameraden aufgehalten wird."


"Das ist durchaus möglich. Der Unterricht geht in ihrer Klasse oft ein bisschen früher zu Ende, also würde Lilly normalerweise einfach zu unserem Klassenzimmer kommen. Ihre Mitschüler verabschieden sie wahrscheinlich noch."


hi "Na ja, schon gut. Wir können ausnahmsweise mal vor ihrem Klassenzimmer warten, oder?"


show hanako emb_smile onlayer master
with charachange

"Sie kichert und stimmt mit einem Kopfnicken zu. Wir nehmen unsere Sachen und machen uns auf dem Weg zum Klassenzimmer der 3-2."


stop ambient fadeout 1.0

scene bg school_hallway3 onlayer master
with locationchange

"Als wir unser Ziel erreichen, bleibe ich stehen und beobachte die amüsante Szene, die sich im Raum abspielt."


"Eines der kleineren Mädchen der Klasse hat Lilly enthusiastisch umarmt. Ihr Kopf reicht kaum bis an Lillys Kinn. Ihre zahlreichen anderen Freunde sind um sie herum versammelt. Lilly lächelt einfach gütig und erwidert die Umarmung."


"Lilly ist anscheinend ziemlich beliebt. Im Vergleich zu Shizunes strenger aber fairen Diktatur über Klasse 3-3 scheint Lilly für Klasse 3-2 eine Mutterfigur zu sein."


"Auf seinem Sitzplatz in der hinteren Ecke des Klassenzimmers packt Kenji seine Sachen ein. Sein absichtlich kühles Verhalten ist wie erwartet. Es besteht kein Zweifel, dass er von der Aufregung über Lillys Abreise nicht begeistert ist."


"Als ich neben mich schaue und merke, dass Hanako meinem Blick folgt, entscheide ich mich, das Zimmer endlich zu betreten."


$ renpy.music.set_volume(0.7, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 0.5

scene bg school_room32 onlayer master
show crowd onlayer master at center
show lilly basic_surprised onlayer master at center
with locationchange

hi "Tag, Lilly. Ich bin's nur. Und Hanako ist bei mir."


show lilly basic_surprised onlayer master at twoleft
show crowd onlayer master at bgleft
show bg school_room32 onlayer master at bgleft
with dissolvecharamove

show hanako emb_downtimid onlayer master at tworight
with charaenter

"Hanako schrumpft deutlich, als sie mit dem Getöse um Lilly konfrontiert wird. So sehr sie sich auch bemüht, bezweifle ich, dass sie ihre Sozialphobie jemals ganz überwinden wird."


show hanako emb_emb onlayer master at tworight
with charaenter

ha "Hallo…"


"Es gelingt Lilly, unsere Position ziemlich gut abzuschätzen, und ihre Klassenkameradin trennt sich wortlos von ihr. Lilly steht leichter Frust ins Gesicht geschrieben, und das kann ich ihr auch nicht verdenken."


show lilly basic_smileclosed onlayer master
with charachange

li "Hallo Hisao, Hanako. Haben wir noch etwas Zeit bis zum Flug?"


"Ich werfe einen schnellen Blick auf meine Uhr. Wenn ich die Fahrt zum Flughafen einrechne, bleiben uns noch gute zehn bis fünfzehn Minuten mit Sicherheitspuffer."


hi "Ja, wir haben noch ein paar Minuten totzuschlagen. Noch würde ich keine Angst haben, den Flug zu verpassen."


"Klassenkameradin" "Ah, ist das Hanako?"


"Auweia. Ich glaube, dass wir unabsichtlich in Lillys soziales Netz verwickelt worden sind."


"Anhand ihrer fensterscheibenähnlichen Brille nehme ich an, dass dieses Mädchen genau wie Kenji nicht blind, sondern nur stark sehbehindert ist. Ihr kurzes, grob geschnittenes Haar und ihr nervöser Ausdruck ergänzen einander ziemlich gut."


show hanako def_shock onlayer master
with charachange

ha "H-Hallo… äh…"


"Sie nimmt Hanakos Hand und schüttelt sie enthusiastisch. Ich kann wirklich nicht verstehen, wie Mädchen so vertraut mit Leuten umgehen können, die sie nur als Freunde von Freunden kennen."


"Während Hanako diesen Gruß nervös erwidert, sehe ich mich in dem Raum nach meinem kurzen, übertrieben angezogen Zimmernachbarn um."
"So sehr ich auch suche – anscheinend hat er sich aus dem Klassenzimmer geschlichen, ohne dass es jemand mitbekommen hat."


"Für einen Moment frage ich mich, in welchen Berufen er von dieser einen Fähigkeit, die er hat, profitieren könnte, aber dann konzentriere ich mich auf wichtigere Angelegenheiten."


show lilly basic_smile onlayer master
show hanako cover_distant onlayer master
with charachange

"Lilly scheint sich über die Begeisterung zu freuen, die Hanako bei ihren Klassenkameraden erweckt hat – auch wenn sie etwas besorgt aussieht."
"Sie mag es zwar nicht sehen können, aber Hanako scheint weit weniger nervös zu sein als ich erwartet hätte."


"Ich mogele mich durch die Schar von Mitschülern und schaffe es endlich, sie zu erreichen."


hi "Mach dir keine Sorgen, Hanako geht es gut."


show lilly basic_weaksmile onlayer master
with charachange

li "Danke. Ich fürchtete, sie wäre von ihnen überwältigt."


"Mitschüler" "Keine Sorge, wir werden vorsichtig sein!"


show lilly basic_concerned onlayer master
with charachange

"Wir schneiden gleichzeitig Grimassen. Hanakos nervöses Grinsen bleibt auf ihrem Gesicht eingefroren, als ein paar weitere Mädchen sich nähern, um sie zu treffen."


"Es ist irgendwie verblüffend, wenn man bedenkt, dass sie vor einem knappen Monat von einer solchen Situation komplett überfordert gewesen wäre."
"Als wir uns zum ersten Mal in der Bibliothek begegnet sind, ist sie davongelaufen – und zu dem Zeitpunkt waren wir komplett allein."


hi "Hast du alles, was du brauchst?"


show lilly basic_smile onlayer master
with charachange

li "Alles ist eingepackt. Ich muss es nur in meinem Zimmer abholen. Und Hanako und ich müssen uns umziehen."


hi "Dann sollten wir uns besser auf den Weg machen. Hanako?"


show hanako cover_bashful onlayer master
with charachange

"Hanako hebt blitzschnell den Kopf und schaut in unsere Richtung. Sie ist offensichtlich dankbar für den Vorwand, sich von der kleinen Gruppe zu befreien, die sich um sie versammelt hat."


show hanako basic_bashful onlayer master
with charachange

stop music fadeout 2.0

ha "Ich k-komme!"


stop ambient fadeout 0.5

scene bg hosp_ext onlayer master
with shorttimeskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0
play music music_tranquil fadein 3.0

"Die lange Taxifahrt zum Flughafen ist überraschend angenehm, obwohl wir uns zusammenquetschen müssen, um zu dritt auf den kleinen Rücksitz zu passen. Andererseits ist „obwohl” vielleicht nicht das passende Wort."


"Während wir aussteigen, zahlt Lilly das Fahrgeld. Hanakos Augen huschen nach links und rechts. Glücklicherweise befinden sich nicht so viele Leute in der Nähe, da sich die meisten im Hauptgebäude aufhalten, anstatt draußen herumzuschwirren."


show akira basic_boo onlayer master at tworight
show hideaki bored onlayer master:
    yalign 1.0 xanchor 0.5 xpos 0.9
with charaenter

"Akira und Hideaki sind leicht zu finden. Sie sind an einen Zaun gelehnt und vertreiben sich die Zeit, indem sie miteinander sprechen. Eine große, schwarze Reisetasche mit Rädern und ausziehbarem Griff, steht ganz in ihrer Nähe."


show hideaki surprise_up onlayer master
with charachange

"Hideaki bemerkt uns als erster. Er macht Akira auf uns aufmerksam, die uns mit übertriebener Begeisterung zuwinkt."


show akira basic_laugh onlayer master
with charachange

aki "Hey! He~y!"


"Während wir auf die beiden zugehen, greife ich Lillys Reisetasche für sie und verdiene mir damit ein dankbares Kopfnicken."


show akira basic_smile onlayer master
show hideaki normal onlayer master
with charachange

aki "Ich habe all meine Sachen hier. Hast du deine? Und dein Ticket?"


show lilly basic_smileclosed_cas onlayer master at twoleft
with charaenter

li "Mach dir keine Sorgen, ich habe alles. Und du?"


show akira basic_laugh onlayer master
with charachange

aki "Jepp. Ich bin startbereit."


show hideaki evil onlayer master
with charachange

hh "Ganz so problemlos war es nicht, wenn ich das sagen darf."


play sound sfx_impact

show akira basic_kill onlayer master
show hideaki ohshit onlayer master
with vpunch

"Als Reaktion auf seine spitze Bemerkung wird er von einer festen Hand am Kragen gepackt und mitgeschleift."


show akira basic_boo onlayer master
show hideaki sad onlayer master
with charachange

aki "Haha, ja, ich habe irgendwie vergessen, dass ich meinen Flugschein in der Hosentasche gelassen habe. Und zwar in der Tasche einer Hose, die ich bereits in die Wäsche geworfen hatte…"


show lilly basic_concerned_cas onlayer master
with charachange

li "Oh nein…"


show akira basic_laugh onlayer master
with charachange

aki "Kein Grund zur Panik. Wusstest du, das du Flugtickets heutzutage ausdrucken kannst, wenn du sie online bestellst? Ist wirklich cool."


show hideaki bored onlayer master
with charachange

"Hideakis gequälter Ausdruck deutet darauf hin, dass man diese Lösung nicht gerade schnell gefunden hat. Na ja, es hätte schlimmer kommen können."


show lilly basic_weaksmile_cas onlayer master
with charachange

li "Wir sollten uns auf den Weg machen. Der Check-in hat wahrscheinlich schon begonnen."


show akira basic_lost onlayer master
with charachange

stop music fadeout 2.0

aki "Ja, du hast Recht."


"Ihre Stimmen klingen beide ein wenig wehmütig. Ganz abgesehen von den Leuten, die sie zurücklassen, ist ein Familientreffen nach all diesen Jahren für wohl ein ziemlich großes Ereignis für sie."


show hanako emb_sad_cas onlayer master at center
with charaenter

play music music_serene fadein 4.0

ha "Lilly…"


"Zum Abschied hüllt Hanako Lilly in eine einfühlsame Umarmung – eine Geste, die wärmstens erwidert wird. Lilly und ich umarmen einander kurz und verabschieden uns."


"Neben uns treten Akira und Hideaki nach einer kleinen Umarmung und ein paar Worten voneinander zurück. Das Ganze hätte bestimmt einen netteren Eindruck gemacht, gäbe es nicht den fast komischen Größenunterschied zwischen den beiden."


show lilly basic_smile_cas onlayer master
show akira basic_smile onlayer master
show hanako emb_downtimid_cas onlayer master
show hideaki normal onlayer master
with charachange

"Nachdem alles, was man zum Abschied sagen muss, gesagt ist, nimmt Lilly den Arm ihrer Schwester, und sie gehen gemeinsam durch die riesigen Glastüren."


show lilly back_smileclosed_cas onlayer master
with charachange

li "Auf Wiedersehen, Hisao, Hanako!"


show akira basic_laugh onlayer master
with charachange

aki "Bis denne! Mach keinen Unsinn, Kurzer!"


hide lilly onlayer master
hide akira onlayer master
with charaexit

"Wir winken ihnen zum Abschied, bis sie in der sich bewegenden Menschenmenge verschwunden sind."


"Und dann… sind wir allein."


hi "Nun… Das war's wohl."


show hideaki bored onlayer master
with charachange

"Ich drehe mich zu Hideaki, nur um zu sehen, dass er sich schon auf den Weg macht."


hi "Bis später."


show hideaki bored_up onlayer master
with charachange

show hideaki invis onlayer master:
    xpos 1.0
with dissolvecharamove

hide hideaki onlayer master
with None

"Er hebt eine Hand zum Abschied – auf eine Art, die mich irgendwie an Akira erinnert. Schließlich stehen Hanako und ich allein draußen."


show hanako emb_timid_cas onlayer master
with charachange

"Ich lege meine Hand auf ihre Schulter. Sie wirft einen abwesenden Blick in Richtung des Flughafeneingangs, als könnte sie noch einen Blick auf die beiden erhaschen, ehe sie verschwinden."


hi "Keine Sorge, die Zeit wird schnell vergehen."


show hanako basic_normal_cas onlayer master
with charachange

"Sie zögert einen Moment, nickt dann aber zustimmend."


"Während die Sommersonne uns mit ihrer sengenden Hitze quält, machen wir uns auf den Weg zur nahegelegenen Bushaltestelle."


hide hanako onlayer master
with charaexit

"Es ist wirklich merkwürdig. Gerade als ich angefangen habe, Lilly mit anderen Augen zu sehen, geht sie auf eine Art Wallfahrt in ihre Vergangenheit."


"Aber in gewisser Hinsicht habe ich genau dasselbe getan, seitdem ich nach Yakamu gekommen bin."


"Egal wie viel ich über alles nachdenke, was mir passiert ist – ich bin kaum ungewöhnlich. Jeder Mensch hat eigenen Umstände und ist auf seinem eigenen Weg dorthin gelangt, wo er jetzt ist."


"Aber ich weiß immer noch nicht, wie ich weitermachen soll. Mein Leben wurde praktisch auf null gestellt, und ich kann immer noch nichts finden, was die Leere in mir füllen kann."


"Vielleicht ist Lillys Abreise etwas Gutes für mich. Wenn ich mich nicht auf sie stützen kann, muss ich mehr für mich selbst tun. Ich muss auch für Hanako da sein."


"Die Monate, die ich im Krankenhaus verbracht habe, schienen getrennt von der Realität zu existieren. Es fühlt sich seltsam an, dass die Dinge sich auf einmal so schnell verändern. Aber gerade deshalb sollte ich meinen Fokus nicht verlieren."


"Bei meinem Versuch, mein Leben wieder aufzubauen, darf ich mir keine Gelegenheit durch die Finger gehen lassen."


stop music fadeout 3.0
stop ambient fadeout 3.0

window hide

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
