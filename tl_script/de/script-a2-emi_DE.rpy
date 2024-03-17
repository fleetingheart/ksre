
label de_E3:

window hide None

scene black onlayer master
with dissolve

$ renpy.music.set_volume(1.0,0.0, "ambient")
play sound sfx_alarmclock

window show

"Das Piepsen meines Weckers reißt mich aus dem Schlaf, und ich frage mich, woher ich die Motivation zum Aufstehen nehmen soll."


scene bg school_dormhisao onlayer master
with openeye

"Bis zum Unterricht ist es noch lange hin, aber ich habe Emi versprochen, von nun an morgens mit ihr Laufen zu gehen."


"Laufen interessiert mich eigentlich nicht wirklich – weder als Hobby noch als möglicherweise lebensverlängerndes Training."


"Aber ich fühle mich verpflichtet, mein gestriges Versprechen an Emi einzuhalten, und so ziehe ich eine kurze Trainingshose und ein T-Shirt an."


scene bg school_courtyard onlayer master
with locationskip

"Die kühle Morgenluft weht mir ins Gesicht, und die Morgensonne bringt den Tau auf dem Gras zum Glitzern, sodass ich einen Moment lang fast geblendet bin."


"Während ich auf dem Weg zum Sportplatz bin, kommt mir ein unangenehmer Gedanke."


"Was, wenn mir Emi mit all dem nur einen Streich spielen will?"


"Würde mich das wirklich überraschen?"


"Verdammt, ich würde das vielleicht auch machen – mit dem „Neuen”."


"Im günstigsten Fall haben Emi und Rin nur gewettet, ob ich wirklich auftauche oder nicht."


scene bg school_track onlayer master
with locationchange

"Ich fühle mich ein wenig beklommen, als der Sportplatz in Sicht kommt."


show emi basic_annoyed_gym onlayer master at center
with charaenter

play music music_emi fadein 1.0

emi "Du bist spät dran!"


"Zu meiner Erleichterung sieht es so aus, als wäre Emi schon hier."


hi "Nach meiner Uhr nicht. Eigentlich sind wir beide zu früh."


show emi basic_closedhappy_gym onlayer master
with charachange

emi "Mist. Du hast mich ertappt."


"Emi sitzt auf der Tribüne. Sie trägt schon ihre Sportsachen und wartet geduldig, bis ich herangekommen bin."


hi "Ich bin froh, dass du auch wirklich hier bist. Ich hatte schon Angst, das wäre vielleicht ein Scherz oder so was."


show emi basic_grin_gym onlayer master
with charachange

emi "Nee, ich würde nie jemanden für nichts so früh aus dem Bett holen."


show emi excited_proud_gym onlayer master
with charachange

emi "Außerdem schuldet mir Rin nun 500 Yen. Sie hat nicht geglaubt, dass du wirklich auftauchen würdest."


"Ich wusste es!"


"Aber es ist schön, dass zumindest Emi auf meiner Seite war."


show emi gymbounce_once onlayer master
with Dissolve(0.1)

"Emi hüpft von der Tribüne und fängt an, sich aufzuwärmen."


play sound sfx_gymbounce

show emi gymbounce onlayer master
with Dissolve(0.05)

"Sie ist bemerkenswert geschmeidig, fast wie eine Tänzerin."


"Ich will auch anfangen mich aufzuwärmen, aber dann fällt mir ein, dass ich nicht mehr genau weiß, wie man das richtig macht."


"Es ist eine Ewigkeit her, dass ich mich für irgendetwas aufgewärmt habe – wenn man mal meinen einen Versuch letzte Woche außer Acht lässt."


"Und sogar da… Ich glaube, ich habe mich davor nicht wirklich richtig aufgewärmt."


"Und wieder zeigen sich die Auswirkungen meines langen Krankenhausaufenthaltes."


"Ich kann aber auch nicht sagen, dass ich vorher besonders aktiv war, also bin ich vielleicht einfach nur griesgrämig."


show emi basic_closedgrin_gym onlayer master at center
with charachange

"Emi kichert, als sie mir beim Aufwärmen zuschaut."


show emi basic_grin_gym onlayer master
with charachange

emi "Nein, nein, nein, Hisao, du musst das länger halten!"


hi "Ich versuch's ja! Es tut ein bisschen weh."


show emi excited_proud_gym onlayer master
with charachange

emi "Ha! Das ist nur, weil du außer Form bist. Du musst beweglicher werden, etwa so."


hide emi onlayer master
with charamoveoutbottom

"Zur Demonstration beugt sich Emi nach unten bis ihr Kopf zwischen ihren Beinen ist."


"Gott segne dich, Emi."


hi "Verstehe. Das ist es also, worauf ich hinarbeiten soll?"


show emi basic_closedgrin_gym onlayer master
with charamoveinbottom

emi "Natürlich! Beweglichkeit ist für jeden Läufer wichtig. Je beweglicher du bist, desto schneller kannst du laufen."


"Das ergibt für mich keinen Sinn, aber Emi scheint daran zu glauben."


"Mit Emis Hilfe schaffe ich es, mich ordentlich aufzuwärmen."


show emi basic_grin_gym onlayer master
with charachange

"Mir fällt auf, dass sie ihren Mund zusammenzieht, wenn sie überlegt, wie sie mir etwas am besten erklären kann."


"Es sieht bezaubernd aus."


show emi excited_proud_gym onlayer master
with charachange

emi "Nicht schlecht, Hisao. Komm, wir sollten mit dem Laufen anfangen."


show emi excited_happy_gym onlayer master
with charachange

emi "Wir fangen mit 1.600 Metern an, okay?"


show emi basic_happy_gym onlayer master
with charachange

emi "Das heißt, vier Runden auf der Laufbahn, verstanden?"


hi "Hört sich gut an."


show emi basic_happy_gym onlayer master:
    center
    easeout 0.5 xpos 0.4 alpha 0.0 
with None

stop music fadeout 2.0

"Das sollte nicht allzu schwer sein, oder?"


scene bg school_track_on onlayer master
with locationchange

"Ich erinnere mich dunkel daran, einmal im Sportunterricht vier Runden gelaufen zu sein."


"Ja, das war nicht so schlimm."


play music music_running fadein 0.5

scene bg school_track_running onlayer master
with Dissolve(2.0)

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

play ambient sfx_emijogging fadein 1.0

"Emi gibt eine recht zügige Geschwindigkeit vor, und ich laufe hinter ihr her."


$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

show emi basic_grin_gym onlayer master at left
with charamoveinleft

emi "Versuch mitzuhalten, okay Hisao?"


hi "Klaro."


$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi onlayer master
with charamoveoutleft

"Wir erreichen die erste Kurve ohne Probleme, aber ich kann schon fühlen, dass mein Puls sich leicht beschleunigt."


"Bei der zweiten Kurve habe ich schon angefangen, durch den Mund zu atmen."


"Emi scheint noch gar nicht außer Atem zu sein."


"Als ob sie ihre Überlegenheit noch unterstreichen will, dreht sie sich um und fängt an, rückwärts zu laufen."


$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

show emi basic_closedgrin_gym onlayer master at center
with charaenter

emi "Geht's dir noch gut, Hisao?"


hi "Ging… mir nie besser."


show emi excited_proud_gym onlayer master
with charachange

emi "Ach wirklich? Vielleicht sollte ich dann einen Zahn zulegen, hmm?"


hi "Ach… nein… du brauchst dich nicht…"


hi "… meinetwegen… überan…strengen."


"Mein schwerer Atem und mein Keuchen machen das weniger überzeugend als ich gehofft hatte. Emi lächelt nur und dreht sich wieder um."


show emi excited_proud_gym onlayer master at left
with charamove

emi "Du bist der Boss, Hisao. Wir bleiben bei diesem Tempo."


$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi onlayer master
with easeoutleft

"Ich habe das Gefühl, dass man sich über mich lustig macht."


"Wenn ich nicht so furchtbar außer Form wäre, wäre ich wohl beleidigt."


"In der dritten Runde kommt mein Atem nur noch keuchend."


"Außerdem bin ich schweißgebadet. Ekelhaft."


"Wir kommen um die Kurve und beginnen die vierte Runde. Emi schaut zu mir zurück und grinst."


$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

show emi basic_closedgrin_gym onlayer master at left
with charamoveinleft

emi "Und los geht's!"


play ambient sfx_emisprinting

hide emi onlayer master
with easeoutleft

$ renpy.music.set_volume(0.3, 0.5, channel="ambient")

"Sie rennt mit blitzartiger Geschwindigkeit los, während ich mich stur an mein langsameres Tempo halte."


"Bis ich an der ersten Kurve angekommen bin, läuft sie schon um die zweite."


"Während ich mich über die Gegengerade kämpfe, läuft Emi weiter und schließt zu mir auf."


play ambient sfx_emijogging

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

show emi excited_proud_gym onlayer master
with charamoveinright

emi "Komm schon, Hisao! Du schaffst es!"


$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi onlayer master
with charamoveoutleft

"Ich würde ihr gerne antworten, aber ich muss mich zu sehr darauf konzentrieren, Luft in meine Lungen zu bekommen, und das Brennen in meinen Beinmuskeln zu ignorieren."


"Ein Teil von mir will etwas sagen wie „Vielleicht kannst {b}du{/b} das, aber ich sterbe hier gleich.”"


"Aber ich bezweifle, dass ich dazu gerade in der Lage wäre."


"Emi hält mit mir Schritt, während ich um die zweite Kurve laufe und die Ziellinie überquere."


stop ambient fadeout 1.5

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

stop music fadeout 5.0

show bg school_track_on onlayer master
show emi basic_happy_gym onlayer master
with locationchange

"Anscheinend hat ihr Sprint sie ins Schwitzen gebracht."


"Durch den Schweiß ist ihr Hemd ein wenig durchsichtig geworden. Es sieht so aus, als würde sie einen schwarzen Sport-BH tragen."


"Ich fühle mich ein wenig schuldig, weil ich einem Mädchen auf die Brust gestarrt habe, aber meine Beine und meine Brust brennen so stark, dass ich diesen Gedanken schnell vergesse."


show emi excited_proud_gym onlayer master
with charachange

emi "Nicht schlecht für den ersten Versuch, Hisao."


play music music_happiness fadein 0.5

hi "N… nett von dir… das zu sagen."


"Emi scheint zwar nicht gerade außer Atem zu sein, atmet aber doch zumindest etwas schwerer als vor unserem Lauf."


"Das muss an ihrem Sprint liegen."


show emi basic_grin_gym onlayer master
with charachange

emi "Hey, ich muss noch ein paar Sprints machen. Du solltest noch einmal um das Feld laufen, um dich abzukühlen."


emi "Dann dehnen wir uns noch mal, und dann sind wir fertig, okay?"


hi "Hört sich toll an."


"Meine Beine brennen, und mein Atem geht immer noch schwer, aber zu meiner Überraschung scheint mein Herz die Anstrengung gut vertragen zu haben."


"Ein weiterer Triumph der Medizin nehme ich an."


show emi basic_closedhappy_gym onlayer master
with charachange

emi "Du solltest die Hände hinter den Kopf nehmen. Dann kriegst du besser Luft."


$ renpy.music.set_volume(0.3, 1.0, channel="ambient")

play ambient sfx_emipacing

hide emi onlayer master
with charamoveoutleft

"Überraschenderweise hat sie Recht. Ich fange an, um das Feld zu laufen – froh, dass mein Atem langsam wieder zurückkommt."


$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

show emi blur onlayer master at offscreenright
with None

show emi blur onlayer master at offscreenleft
with move

$ renpy.music.set_volume(0.3, 0.5, channel="ambient")

hide emi onlayer master
with None

"Ich nehme einen verschwommenen Schatten wahr, als Emi an mir vorbei sprintet."


"Ihr beim Laufen zuzuschauen ist absolut faszinierend."


"Es ist nicht nur, dass sie auf Prothesen läuft – obwohl das auch interessant ist."


show ev emi_run_face_zoomin onlayer master
show ev emi_run_face as unlockstub behind ev onlayer master
with dissolve

"Das wirklich Interessante ist, wie ihr Gesicht sich verändert."


"Ich sehe sie immer nur kurz, wenn sie vorbei läuft, aber ihre Augen sprühen vor Leben und einer Art wilder Freude."


"Es ist, als gäbe es auf der ganzen Welt nichts außer ihr und der Laufbahn."


stop ambient fadeout 0.5

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

scene bg school_track_on onlayer master
with locationchange

"Bis ich auf der Zielgerade bin, scheint Emi mit ihren Sprints fertig zu sein."


"Sie atmet nun auch schwer, aber auf ihrem Gesicht ist ein zufriedenes Grinsen. Sie winkt mir fröhlich zu, als ich auf sie zugehe."


show emi basic_grin_gym onlayer master at center
with charaenter

emi "Man fühlt sich besser, nicht wahr?"


hi "Ja, wirklich."


show emi sad_grin_gym onlayer master
with charachange

emi "Läufst du noch 'ne Runde mit mir? Ich muss ja auch noch abkühlen."


"Ein Teil von mir würde sich lieber hinsetzen und sich nicht mehr bewegen, aber ich habe das Gefühl, das wäre eine schlechte Idee."


"Außerdem… wenn ich mich jetzt hinsetze, komme ich vielleicht nicht mehr hoch."


hi "Klar, warum nicht?"


"Emi nimmt ihre Hände nun auch hinter ihren Kopf. Sie sieht sehr entspannt aus."


"Durch diese Armposition wird ihr Hemd ein winziges Stück nach oben gezogen, sodass ich einen Streifen ihres Bauches sehen kann."


"Ich versuche, wie ein Gentleman zu handeln und nicht hinzuschauen, aber der Kontrast zwischen ihrer Haut und ihren roten Sporthosen ist irgendwie fesselnd."


show emi basic_grin_gym onlayer master
with charachange

emi "Also wie fühlst du dich, Hisao?"


hi "Um ehrlich zu sein, überraschend gut. Mir tut alles weh, und ich bin müde, aber… überraschend gut."


"Und sobald ich es ausspreche, merke ich, dass es wahr ist."


"Ja, ein Teil von mir will sich hinlegen und sterben, aber ich fühle mich, als hätte ich etwas erreicht."


"Es ist wie ein Glühen, das durch meinen Körper geht, trotz aller Schmerzen."


show emi excited_proud_gym onlayer master
with charachange

emi "Ja, das ist der Endorphin-Kick."


hi "Endorphin-Kick?"


show emi basic_hes_gym onlayer master
with charachange

emi "Ja, das hat was zu tun mit… Adrenalin?"


"Während wir weiterlaufen, überlegt Emi einen Moment lang und versucht, sich zu erinnern."


show emi basic_closedgrin_gym onlayer master
with charachange

"Dann zuckt sie mit den Schultern und grinst mich an."


show emi basic_grin_gym onlayer master
with charachange

emi "Ehrlich gesagt, ich weiß es nicht mehr genau. Ist aber ein gutes Gefühl, oder?"


show emi basic_happy_gym onlayer master
with charachange

stop music fadeout 0.5
play sound sfx_heartstop

emi "Besser als Sex, stimmt's?"


"Ich öffne meinen Mund, um zu antworten, bevor ich registriert habe, was sie gerade gesagt hat."


hi "…"


"Emi beobachtet einen Moment lang mein Gesicht, bevor sie laut loslacht."


play music music_comedy fadein 1.0

show emi excited_laugh_gym onlayer master
with charachange

emi "'Tschuldigung! Ich konnte nicht widerstehen! Du lässt dich zu leicht auf den Arm nehmen!"


hi "Warum habe ich mich noch mal bereit erklärt, mit dir zu laufen?"


"Emi lacht nur noch lauter. Sie greift nach meinem Unterarm und zieht ihn zu sich heran, um besser auf meine Uhr schauen zu können. Ich Gesicht wird sofort ernst, als sie die Uhrzeit sieht."


show emi basic_shock_gym onlayer master
with charachange

emi "Oh nein! Wir sollten uns besser beeilen, Hisao!"


show emi basic_closedsweat_gym onlayer master
with charachange

emi "Der Unterricht geht in einer Stunde los, und ich muss noch duschen!"


hi "Das sollte ich wahrscheinlich auch tun…"


show emi basic_hes_gym onlayer master
with charachange

emi "Ich muss auch noch bei Doc vorbeischauen… Vielleicht schreibt er mir ja eine Entschuldigung fürs zu spät kommen!"


hi "Warum musst du zu Doc?"


show emi basic_closedgrin_gym onlayer master
with charachange

"Emi zeigt auf ihre Prothesen, als ob das alles erklären würde."


show emi basic_grin_gym onlayer master
with charachange

emi "Es ist wichtig, nach Hautreizungen zu schauen."


emi "Vom Schweiß oder von der Reibung oder so was, weißt du?"


show emi excited_amused_gym onlayer master
with charachange

emi "Normalerweise gehe ich nur nach dem Training, aber wenn wir in Zukunft auch morgens laufen, werde ich wohl zweimal am Tag zu ihm müssen."


"Warte mal, heißt das, Emi macht diese morgendlichen Trainings erst, seit ich hier bin?"


hi "Wenn dir eine andere Zeit besser passen würde…"


show emi sad_grin_gym onlayer master
with charachange

emi "Sei nicht albern! Ich wollte schon lange anfangen, auch morgens zu laufen."


emi "Aber wenn man niemanden hat, der mit einem läuft, ist es schwer, in eine Routine zu kommen."


show emi basic_grin_gym onlayer master
with charachange

emi "Es ist immer schwerer ein Vorhaben aufzugeben, wenn man damit jemand anderen im Stich lassen würde, weißt du?"


show emi basic_closedgrin_gym onlayer master
with charachange

emi "Also wirst du morgens mein Laufpartner sein!"


show emi excited_proud_gym onlayer master
with charachange

emi "Wir brauchen beide das Training, also passt das gut, findest du nicht?"


hi "Ja, perfekt."


"Aber musste ich es sein?"


"Na ja, ich denke, ich kann mich nicht beschweren. Es macht Spaß, mit Emi zusammen zu sein."


"Und sie hat Recht. Ich brauche die Bewegung. Ist sogar ein Befehl von Doc."


show emi basic_happy_gym onlayer master
with charachange

"Emi winkt mir noch kurz zum Abschied zu."


emi "Ich bin dann weg! Komm zum Mittagessen zu uns, okay?"


hi "Was?"


show emi basic_closedhappy_gym onlayer master
with charachange

emi "Mittagessen! Du weißt schon, die Mahlzeit? Mitten am Tag? Komm bei uns vorbei!"


hi "Wo?"


show emi basic_grin_gym onlayer master
with charachange

emi "Auf dem Dach. Rin gefällt es dort oben."


hi "Wann?"


show emi basic_annoyed_gym onlayer master
with charachange

emi "In der Mittagspause, wann sonst? Das war eine dumme Frage."


hi "Ja, aber irgendwie musste ich alle drei Fragen stellen – nur der Vollständigkeit halber."


show emi excited_laugh_gym onlayer master
with charachange

"Emi lacht und grinst. Ich glaube, ich habe noch nie ein Mädchen so viel Lächeln sehen."


show emi excited_happy_gym onlayer master
with charachange

emi "Nicht schlecht, Hisao. Man sieht sich!"


play ambient sfx_emisprinting

hide emi onlayer master
with easeoutleft

stop ambient fadeout 2.0
stop music fadeout 8.0

"Und damit rennt sie wie eine Rakete in Richtung des Schulgebäudes."


"Sieht aus, als ob sie zuerst zu Doc will."


scene bg school_dormbathroom onlayer master
with locationskip

"Ich eile zurück in mein Zimmer, um unter die Dusche zu hüpfen, nur um dann herauszufinden, dass das Wasser einen Moment zum Warmwerden braucht."


play ambient sfx_shower
with vpunch

"Der Schock des kalten Wassers bringt mich fast um."


show steam onlayer master
with Dissolve(2.0)

"Schließlich wird das Wasser etwas wärmer, und ich verbringe eine angenehme Zeit damit, meine Muskeln etwas zu lockern."


"Mein Herz macht nach dem Laufen überraschenderweise überhaupt keine Probleme."


"Ich denke mal, das ist etwas Gutes, auch wenn ich mich ein bisschen wie eine Memme fühle."


"Ich meine, wenn mein Herz mir Probleme machen würde, hätte ich wenigstens eine Ausrede außer „Ich bin nicht in Form.”"


"Ich werde wohl mit diesem Laufen weitermachen müssen, oder Emi liegt mir damit ewig in den Ohren."


"Erst als ich aus der Dusche komme und mich abtrockne, bemerke ich, dass ich nur noch zehn Minuten habe, um mich anzuziehen und zum Unterricht zu kommen."


"Verdammt."



label de_E4:

scene bg school_dormbathroom onlayer master
show steam onlayer master
with None

stop ambient fadeout 1.0

scene bg school_scienceroom onlayer master
with shorttimeskip

window show

play sound sfx_normalbell

"Die Zeiger der Uhr befreien mich endlich von der Eintönigkeit eines weiteren wahnsinnig interessanten Vormittags."


"Von meinem Stuhl aufzustehen ist ein größeres Problem, als ich erwartet hatte."


"Nach dem Laufen heute Morgen bringen mich meine Beine um."


"Vielleicht war das doch keine so tolle Idee."


"Immerhin habe ich nun einen Riesenappetit."


play ambient sfx_crowd_indoors fadein 1.0

scene bg school_hallway3 onlayer master
show crowd onlayer master
with locationchange

"Ich bin schon auf halben Weg zur Cafeteria, als mir einfällt, dass ich mein Mittagessen bei mir habe."


"Meine Eltern haben mir ein paar Fertiggerichte mitgegeben, als ich hier eingezogen bin. Nun bin ich froh darüber."


"Der Gang ist voll mit Schülern, die alle zur Cafeteria wollen."


"In die andere Richtung zu gehen ist wie Schwimmen gegen den Strom – aber ich habe eine Verabredung auf dem Dach."


stop ambient fadeout 4.0

scene bg school_staircase1 onlayer master
with locationchange

"Ich brauche einen Moment, um die Treppe zum Dach zu finden, aber ich wette, dass Emi und Rin sowieso noch nicht dort oben sind."


"Ich glaube sogar, dass ich Emi in der Menge gesehen habe, die zur Cafeteria gelaufen ist."


play sound sfx_door_creak
$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 0.5

scene bg school_roof onlayer master at bgright
with locationchange

"Ich trete durch die Tür auf das Dach und hole tief Luft."


"Die frische Luft, die mir ins Gesicht und um den Körper weht, lindert die Schmerzen in meinen Beinen fast ein wenig."


show rin basic_awayabsent onlayer master at center
with charaenter

rin "Vielleicht wenn ich mich auf den Kopf stelle…"


$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_rin fadein 1.0

"Ein Teil von mir wäre gerne überrascht, dass Rin schon hier ist."


hi "Was soll das bringen?"


show rin basic_deadpan onlayer master
with charachange

rin "Sachen in den Wolken."


hi "Könntest du sie nicht einfach… richtig herum anschauen?"


show rin basic_deadpanupset onlayer master
with charachange

"Rin verdreht ihre Augen und sieht dabei fast etwas frustriert aus."


rin "Dann würde ich aber keine neue Perspektive kriegen."


hi "Wäre „auf dem Kopf stehend” überhaupt einen neue Perspektive?"


show rin basic_delight onlayer master
with charachange

"Aha! Das hat sie nicht erwartet. Rin sieht nachdenklich aus."


rin "Du könntest Recht haben. Vielleicht von der Seite."


hide rin onlayer master
with charamoveoutbottom

"Als Rin sich auf die Bank legt, um in den Himmel zu starren, gebe ich auf."


play sound sfx_impact2
with vpunch

show emi basic_closedgrin onlayer master at center
with charaenter

"Zum Glück stürmt in diesem Moment Emi mit zwei Taschen in der Hand durch die Tür."


"Sie reißt fast die Tür aus den Angeln."


show emi basic_hes onlayer master
with charachange

emi "Tut mir leid, dass es so lange gedauert hat! Da waren hunderte von Leuten in der Schlange."


show emi basic_grin onlayer master
with charachange

show emi basic_grin onlayer master at twoleft
show bg school_roof onlayer master at center
with charamove

"Sie lässt die eine Tasche vor Rin fallen und setzt sich auf die Bank neben sie."


hi "Du kaufst Rins Essen für sie?"


show emi basic_closedgrin onlayer master
with charachange

emi "Ja, manchmal. Ich würde sie ja als Gegenleistung auch ab und zu mal zum Essen Kaufen schicken, aber ich wüsste nicht, wie sie es tragen soll."


show rin basic_deadpan onlayer master at tworight
with charamoveinbottom

rin "Außerdem würde ich ihr nie Mittagessen kaufen."


"Wenn Rin sich durch Emis Kommentar beleidigt fühlt, lässt sie es sich nicht anmerken. Emi rümpft die Nase."


show emi basic_annoyed onlayer master
with charachange

emi "Wie undankbar."


"Ich bin mir nicht sicher, ob die beiden nur Spaß machen oder ob ich den Anfang eines Streits miterlebe."


show emi basic_closedgrin onlayer master
show rin basic_amused onlayer master
with charachange

"Die zwei Mädchen starren sich einen Moment lang angespannt an und fangen dann an zu grinsen."


show rin basic_awayabsent onlayer master
with charachange

rin "Hey, Emi, denkst du, dass man eine neue Perspektive bekommt, wenn man auf dem Kopf steht?"


"Hatte ich diese Konversation nicht schon einmal?"


show emi basic_hes onlayer master
with charachange

"Emi sieht nachdenklich aus. Anscheinend denkt sie ernsthaft über die Frage nach."


"Nach einer langen, profunden Pause spricht sie."


show emi basic_closedsweat onlayer master
with charachange

emi "Ich habe keine Ahnung."


"Na ja, zumindest geht es ihr genau wie mir."


stop music fadeout 4.0

show emi excited_happy onlayer master
with charachange

emi "Hey, Hisao, du kommst doch zu dem Sportfest, oder?"


"Die Frage kommt ohne Vorwarnung und erwischt mich auf dem falschen Fuß."


hi "Äh… Ich weiß noch nicht?"


show rin basic_absent onlayer master
show emi sad_annoyed onlayer master
with charachange

emi "Ehrlich, Hisao, nachdem ich mir all die Mühe gemacht habe, dein morgendliches Training zu planen, kommst du nicht ein mal zu meinem Leichtathletikturnier?"


show rin basic_awayabsent onlayer master
with charachange

"War sie nicht diejenige, die mich gebeten hat, mit ihr zu laufen?"


"Im Grunde hat sie mir nicht mal eine Wahl gelassen."


hi "Warte, nein, das hab ich nicht gesagt…"


play music music_ease fadein 3.0

show emi basic_closedgrin onlayer master
show rin basic_absent onlayer master
with charachange

"Sie strahlt mich an, als hätte ich ihr gerade zehn Millionen Yen versprochen."


show emi basic_closedhappy onlayer master
with charachange

emi "Also kommst du doch! Das ist toll!"


hi "Das habe ich auch nicht gesagt!"



show rin basic_deadpan onlayer master
with charachange

rin "Ich gehe auch hin, also sorge ich dafür, dass er kommt, Emi."


show emi basic_grin onlayer master
show rin basic_absent onlayer master
with charachange

emi "Gute Idee, Rin! Vielleicht können wir dann nach dem Turnier ja noch was Essen gehen oder so was."


"Ich fühle mich, als wäre ich gerade hereingelegt worden, aber nicht von diesen beiden."


"Es ist eher, als würde mich irgendeine Kraft von außen unwiderruflich auf mein Schicksal zusteuern."


"… Oder vielleicht sollte ich weniger Bücher über Verschwörungstheorien lesen. Sonst höre ich mich irgendwann genauso an wie Kenji."


"Jedenfalls sieht es so aus, als müsste ich dort nun aufkreuzen."


"Ich glaube, ich könnte es nicht ertragen, die beiden zu enttäuschen."


"Sie würden mir das ewig vorhalten."


hi "Wann ist das noch mal?"


show emi basic_annoyed onlayer master
with charachange

emi "Nächste Woche, Dummerchen! Das hab ich dir doch vor ein paar Tagen erst erzählt."


hi "Nein, hast du nicht."


show emi sad_shy onlayer master
with charachange

emi "Hab ich das vergessen? Na ja, du vergisst nicht zu kommen, oder?"


hi "Natürlich nicht! Ich trage es mir sogar in meinen Kalender ein oder so was!"


show rin basic_lucid onlayer master
with charachange

"Rin nickt weise."


show rin basic_deadpancontemplation onlayer master
with charachange

rin "Das ist bestimmt eine gute Idee, weißt du. Es sei denn, die Zeit läuft plötzlich anders."


show emi basic_confused onlayer master
with charachange

emi "Kann sie das?"


show rin relaxed_nonchalant onlayer master
with charachange

"Rin zuckt mit den Schultern."



show rin negative_spaciness onlayer master
with charachange

rin "Ist bis jetzt noch nie vorgekommen, aber man weiß nie…"


show emi basic_closedgrin onlayer master
with charachange

"Dieses Mal zuckt Emi mit den Schultern."


show emi basic_closedhappy onlayer master
with charachange

emi "Ich nehme an, wenn das passiert, können wir auch nichts daran ändern."


show rin basic_deadpannormal onlayer master
with charachange

rin "Es sei denn, du bist ein Zeitreisender oder so was."


hi "Ihr glaubt doch nicht ernsthaft, dass so etwas passieren könnte, oder?"


show emi basic_confused onlayer master
with charachange

emi "Tun wir nicht, glaube ich… oder?"


show rin relaxed_nonchalant onlayer master
with charachange

"Rin zuckt wieder mit den Schultern. Das scheint ihre Standardreaktion auf alles zu sein."


show rin basic_deadpandelight onlayer master
with charachange

rin "Ich denke nicht. Aber ich behalte mir das Recht vor, meine Meinung jederzeit zu ändern."


"Für Rins Verhältnisse ergibt diese Aussage beunruhigend viel Sinn."


"Die Tatsache, dass mir das auffällt, macht mir ein wenig Angst."


"Ich frage mich, ob Emi sich immer so fühlt."


show emi basic_closedgrin onlayer master
with charachange

"Wenn sie das tut, lässt sie sich nichts anmerken. Sie nickt nur."


show emi basic_grin onlayer master
with charachange

emi "Wie erwartet."


show rin basic_deadpanupset onlayer master
with charachange

rin "Was soll das denn heißen?"


show emi sad_grin onlayer master
with charachange

"Dieses Mal zuckt wieder Emi mit den Schultern."


"Es ist, als ob sie Rins eigene Waffen gegen sie verwenden würde."


show emi excited_proud onlayer master
with charachange

emi "Deine Antwort ist einfach nur genau so, wie ich sie von dir erwartet hätte."


show rin negative_worried onlayer master
with charachange

rin "Bin ich wirklich so berechenbar?"


show emi basic_closedgrin onlayer master
with charachange

"Emis Grinsen grenzt fast schon an Häme."


emi "Nö, es ist nur deine Unberechenbarkeit, die berechenbar ist."


show rin relaxed_nonchalant onlayer master
with charachange

rin "Ach so, das ist in Ordnung."


play sound sfx_warningbell

"Ich habe keine Chance festzustellen, ob Rin das ernst meint oder nicht, weil die Glocke läutet."


"Ich habe gar nicht gemerkt wie schnell die Mittagspause vorbei gegangen ist."


"Die Zeit mit den beiden war einfach zu interessant."


show emi basic_shock onlayer master
with vpunch

"Emi springt mit einem panischen Ausdruck im Gesicht auf."


emi "Oh nein! Ich muss noch in meinem Zimmer vorbei, und mein Notizbuch für nächste Stunde holen!"


show rin basic_deadpandelight onlayer master
with charachange

rin "Nun wünschst du dir sicher, du hättest einen Zeitmaschine, oder?"


"Rin sagt das so selbstzufrieden, als ob sie gerade eine Diskussion gewonnen hätte."


"Emi ignoriert Rins Kommentar."


show emi basic_hes onlayer master
with charachange

emi "Tut mir leid, Hisao, aber könntest du unseren Müll wegräumen?"


show emi basic_closedsweat onlayer master
with charachange

emi "Normalerweise räume ich selbst auf, aber ich muss mich beeilen!"


hi "Klar, kein Problem."


hide emi onlayer master
with easeoutleft

"Emi schießt mit der Eile davon, die ich inzwischen von ihr erwarte."


hide rin onlayer master
with charaexit

"Ich frage Rin gar nicht erst, warum sie nicht hilft. Sie scheint schon mit etwas anderem beschäftigt zu sein, während sie davongeht."


"Sie ist es wahrscheinlich gewohnt, dass Emi sich um das Aufräumen kümmert, und irgendwie bezweifle ich, dass Emi sie je auf das Thema angesprochen hat."


"Das Zusammenräumen unserer Reste dauert nicht lange, und so habe ich genug Zeit, um den Müll wegzuwerfen und zum Unterricht zu kommen."


stop ambient fadeout 1.0

scene bg school_scienceroom onlayer master
with locationskip

"Misha begrüßt mich mit einem Winken und einem verschlagenen Grinsen, als ich zur Tür herein komme."


show misha cross_grin onlayer master at center
with charaenter

mi "Hab dich gar nicht in der Cafeteria gesehen, Hicchan."


hi "Ja, da war's mir zu voll."


show misha hips_grin onlayer master
with charachange

"Mishas Grinsen wird noch breiter."


mi "Ach wirklich? Bist du sicher, dass du nicht bei einem verbotenen Ren-dez-vous warst?"


hi "W… was? Wovon redest du?"


show misha sign_smile onlayer master
with charachange

mi "Du warst auf dem Dach, oder? Und sogar mit Rin {b}und{/b} Emi! Du Casanova, du!"


hi "Wir… wir haben nur Mittag gegessen, das ist alles!"


show misha cross_laugh onlayer master
with charachange

"Misha lacht laut auf, was die Aufmerksamkeit einiger unserer Klassenkameraden auf uns lenkt."


mi "Wahahaha! Du siehst so niedlich aus, wenn du rot wirst, Hicchan!"


show misha cross_grin onlayer master
with charachange

"Sie zwinkert mir verschwörerisch zu."


show misha cross_smile onlayer master
with charachange

mi "Keine Sorge, dein Geheimnis ist bei mir sicher."


hi "Es gibt kein Geheimnis!"


show misha perky_confused onlayer master
with charachange

mi "Ach?"


"Misha sieht enttäuscht aus, grinst dann aber schnell wieder."


show misha hips_grin onlayer master
with charachange

mi "Wir werden ja sehen~!"


"Ich habe keine Ahnung, wovon sie redet, aber zum Glück kommt unser Lehrer herein, und der Unterricht beginnt."


stop music fadeout 2.0



label de_E5:

scene bg school_scienceroom onlayer master
with shorttimeskip

play sound sfx_normalbell

"Ein weiter Schultag geht endlich zu Ende."


"Ich hatte es nicht erwartet, aber ich habe es geschafft, bis zum Ende wach zu bleiben."


"Ich bin mir ziemlich sicher, dass das als Wunder durchgeht."


"Meine Beine scheinen einen Moment lang ihren Dienst zu verweigern."


"Sieht aus, als hätte das Training mich ziemlich ausgelaugt."


scene bg school_hallway3 onlayer master
with locationchange

"Ich gehe den Flur entlang auf dem Weg zu meinem Zimmer."


scene bg school_dormhisao onlayer master
with locationskip

"Ich setze mich und mache eine Zeit lang halbherzig meine Hausaufgaben. Ich fühle mich dabei wie ein Aasgeier an einem besonders widerlichen Kadaver."


"Er weiß, dass er so etwas normalerweise isst, aber er ist sich nicht sicher, ob er nicht doch etwas vom Lieferservice bestellen sollte."


"Ich glaube, ich schaffe das nicht, aber es ist wichtig, damit fertig zu werden."


hi "Hmm, mal sehen… Was sollte ich mir noch einmal anschauen?"


"Ich weiß, dass ich auf verlorenem Posten kämpfe, aber ich kämpfe trotzdem."


"Halb fertig mit meinen Matheaufgaben lege ich meinen Bleistift zur Seite."


"Das klappt so nicht. Ich brauche eine Ablenkung."


"Dummerweise sind meine Optionen für Ablenkungen ziemlich dünn gesät."


"Ich habe im Moment keine Lust zu lesen."


"Kenji ist zu dieser Zeit normalerweise nicht in seinem Zimmer."


"Wenn ich ins Schülerratsbüro gehe, werden diese beiden mich nur wieder zum Arbeiten einspannen."


"Und weiß der Himmel, wo die anderen alle sind, außer…"


"Na ja, ich denke, das wäre eine Möglichkeit."


"Ich ziehe meine Schuhe an und gehe zum Sportplatz. Emi wird wahrscheinlich dort sein."


play music music_tranquil fadein 3.0

scene bg school_track_ss onlayer master
with locationskip

"Das Leichtathletiktraining geht gerade zu Ende, als ich am Sportplatz ankomme."


"Die Sonne senkt sich dem Horizont entgegen."


"Ist es wirklich schon so spät?"


show emi basic_grin_gym_ss onlayer master at center
with charaenter

emi "Was machst du denn hier, Hisao?"


show emi excited_proud_gym_ss onlayer master
with charachange

emi "Spionierst du mir etwa nach?"


"Ich zucke mit den Schultern. Um ehrlich zu sein, bin ich nicht sicher, warum ich hier bin."


hi "Ich hatte nichts Besseres zu tun."


"Ich denke mal, das trifft es ganz gut."


"Momentan ist Emi die einzige Person, die mir einfällt, die ich besuchen könnte."


show emi basic_annoyed_gym_ss onlayer master
with charachange

emi "Ich bin also dein letzter Ausweg oder was?"


show emi sad_angry_gym_ss onlayer master
with charachange

emi "Keine coolen Leute da, also besuche ich mal Emi, dachtest du das?"


"Sie sieht sogar richtig wütend aus."


"Da bietet sich mir doch die Chance, sie ebenfalls etwas auf den Arm zu nehmen."


hi "Wenn man es so sieht… Ja, das bist du wohl."


show emi sad_annoyed_gym_ss onlayer master
with charachange

"Emi schmollt und reißt ihre Augen zu ihrem patentierten Welpenblick auf."


hi "Ein Scherz! Das war nur ein Scherz!"


show emi basic_closedgrin_gym_ss onlayer master
with charachange

emi "Also hast du mir doch nachspioniert!"


"Moment mal, was?"


hi "Das hab ich nicht gemeint!"


hi "Warum sollte ich dir auch nachspionieren? Es ist ja nicht so, dass man dir nachspionieren müsste."


hi "Wenn du nicht schläfst oder im Unterricht bist, bist du hier, oder?"


"Das bringt Emi zum Lachen."


show emi basic_happy_gym_ss onlayer master
with charachange

emi "Na ja, ich denke, das ist nicht komplett falsch – aber du hast das Essen vergessen. Das mache ich auch, weißt du?"


"Ich nicke, da hat sie wohl Recht."


show emi sad_grin_gym_ss onlayer master
with charachange

emi "Außerdem hänge ich auch manchmal mit Rin 'rum… Es könnte also schon etwas schwieriger sein, mir nachzuspionieren."


hi "Was unternehmt ihr Zwei überhaupt zusammen? Ihr scheint nicht viel gemeinsam zu haben."


show emi basic_closedgrin_gym_ss onlayer master
with charachange

"Sie stützt die Hände in ihre Hüften und schaut mich herablassend an."


show emi basic_grin_gym_ss onlayer master
with charachange

emi "Das denkst du. Ich hab eine ganze Menge geheime Hobbys, weißt du?"


hi "Ach wirklich? Was denn zum Beispiel?"


show emi sad_grin_gym_ss onlayer master
with charachange

"Emi legt ihren Kopf zur Seite, als ob sie versucht sich zu erinnern, was sie in ihrer Freizeit macht."


show emi basic_closedgrin_gym_ss onlayer master
with charachange

emi "Na ja, Rin und ich gehen manchmal zusammen shoppen."


"Ich denke, das ergibt Sinn. Emi ist schließlich ein Mädchen. Aber Rin?"


hi "Rin begleitet dich?"


show emi basic_grin_gym_ss onlayer master
with charachange

emi "Wir machen normalerweise einen Abstecher zu einem Laden, der Malerzubehör verkauft."


emi "Außerdem mag sie dieses Musikgeschäft, wo sie so ganz seltsam klingendes Zeug verkaufen."


show emi basic_closedhappy_gym_ss onlayer master
with charachange

emi "Sie sagt, es hilft ihr beim Konzentrieren."


"Das ergibt wieder etwas mehr Sinn."


hi "Aha. Noch irgendwelche geheimen Hobbys?"


show emi excited_proud_gym_ss onlayer master
with charachange

"Emi hebt ihren Finger."


emi "Na na, warum sollte ich dir alle meine geheimsten Geheimnisse verraten? Wir kennen uns doch kaum!"


"Irgendwie habe ich das Gefühl, dass Emi sonst keine Hobbys hat."


"Trotzdem hat das meine Frage noch nicht ganz beantwortet."


hi "Auch wenn du ein paar Hobbys hast, verstehe ich nicht, warum du so viel mit Rin zusammen bist."


hi "Ich meine, sie ist ziemlich seltsam, oder nicht?"


"Dieser Kommentar lässt Emi laut auflachen."


show emi basic_closedhappy_gym_ss onlayer master
with charachange

emi "Ha! Das ist die Untertreibung des Jahres!"


hi "Also warum? Ich meine, du kannst doch viel besser mit Leuten reden und so, also hätte ich gedacht, dass du mit ganz vielen Leuten rumhängen würdest, aber ich sehe dich immer nur mit Rin."


show emi sad_annoyed_gym_ss onlayer master
with charachange

"Emi widerspricht ungewöhnlich heftig."


emi "Hey, ich hänge mit vielen Leuten außer Rin rum! Da siehst du mich nur nicht, weil wir keine Fächer zusammen haben."


hi "Gut, aber das erklärt immer noch nicht, warum du mit Rin rumhängst."


"Ich bin mir nicht einmal sicher, warum ich das eigentlich wissen will."


"Wahrscheinlich wegen dieses seltsamen Gesprächs in der Mittagspause."


show emi basic_confused_gym_ss onlayer master
with charachange

"Emi zuckt mit den Schultern. Einen Moment lang sieht sie aus wie Rin."


stop music fadeout 4.0

emi "Liegt wohl daran, dass wir ähnliche Einstellungen haben."


"Wenn man mich fragen würde, was die unwahrscheinlichste Antwort auf meine Frage wäre… das wäre sie."


hi "Wie meinst du das?"


emi "Es ist wie…"


play music music_emi fadein 1.0

show emi basic_grin_gym_ss onlayer master
with charachange

emi "Okay, Rin malt und so, richtig?"


hi "Ja…"


"Ich bin mir nicht sicher, worauf sie hinaus will."


show emi basic_closedgrin_gym_ss onlayer master
with charachange

emi "Na ja, und ich laufe."


hi "Und?"


show emi basic_happy_gym_ss onlayer master
with charachange

emi "Und… deshalb sind wir uns ähnlich."


hi "…"


hi "Ich kann dir nicht folgen."


show emi basic_annoyed_gym_ss onlayer master
with charachange

"Emi runzelt die Stirn, als ob sie sich ihre Antwort zurecht legt."


emi "Na ja, vielleicht liegt es daran, dass wir Dinge aus den gleichen Gründen tun."


hi "Hä?"


show emi sad_grin_gym_ss onlayer master
with charachange

emi "Du weißt schon, wir leben unsere Leidenschaften."


hi "Also du läufst leidenschaftlich gerne, und Rin malt leidenschaftlich gerne, ist es das?"


emi "Na ja, so ähnlich. Lass mich nachdenken…"


show emi basic_closedgrin_gym_ss onlayer master
with charachange

emi "Nun, Rin hat es mir einmal erklärt, aber ich weiß nicht, wie viel davon ich verstanden habe."


"Das überrascht mich nicht. Ich denke, eine Erklärung von Rin würde wohl jeden verwirren."


show emi basic_grin_gym_ss onlayer master
with charachange

emi "Sie sagt, wir beide verfolgen ein Extrem."


emi "Wie… Sie versucht immer eine neue Möglichkeit zu finden, ein bestimmtes Gefühl auszudrücken oder so."


show emi sad_grin_gym_ss onlayer master
with charachange

emi "Und ich laufe, wegen des Gefühls, das ich dabei kriege."


emi "Und weil wir uns beide durch nichts aufhalten lassen, verbindet uns das irgendwie."


hi "Wie meinst du das „durch nichts aufhalten lassen”?"


show emi basic_confused_gym_ss onlayer master
with charachange

"Emi schaut mich überrascht an und zeigt auf ihre Beine."


emi "Du weißt schon, weil ich eine Läuferin bin. Und Rin ist eine Malerin, obwohl sie keine Arme hat."


emi "Wir respektieren also gegenseitig unsere Entschlossenheit."


show emi basic_closedhappy_gym_ss onlayer master
with charachange

emi "Und deshalb hängen wir zusammen rum."


show emi sad_grin_gym_ss onlayer master
with charachange

emi "Denke ich."


"Na ja, ich bin mir nicht sicher, ob ich das genau verstanden habe… aber Emis verlegener Miene nach zu urteilen, weiß sie das selbst nicht genau."


emi "Ganz ehrlich, ich mache mir darüber nicht so viele Gedanken."


emi "Wir kommen einfach gut miteinander klar; ich denke, das ist alles, worauf es wirklich ankommt."


"Da hat sie wohl Recht."


"Mir fällt da noch eine weitere Frage ein, und da ich nichts besseres zu tun habe, stelle ich sie."


hi "Sag mal, wie bist du eigentlich zum Laufen gekommen?"


show emi basic_closedgrin_gym_ss onlayer master
with charachange

emi "Oh, ich laufe schon, seit ich ganz klein war!"


show emi basic_grin_gym_ss onlayer master
with charachange

emi "Mein Vater war Läufer, und sobald ich gehen konnte, hat er mir beigebracht, wie man läuft."


show emi sad_grin_gym_ss onlayer master
with charachange

emi "Es war so eine Vater-Tochter-Sache, weißt du?"


show emi sad_depressed_gym_ss onlayer master
with charachange

stop music fadeout 10.0

emi "Unser gemeinsames Hobby."


"Ein Schatten huscht über ihr Gesicht, und ich bin schockiert, sie… traurig zu sehen."


"Ist zwischen den beiden etwas vorgefallen?"


show emi basic_shock_gym_ss onlayer master
with charachange

emi "Mann, ich habe kaum noch Zeit."


show emi basic_closedsweat_gym_ss onlayer master
with charachange

emi "Tut mir leid, aber ich muss noch ein paar Runden laufen, bevor ich zu Doc gehe!"


play ambient sfx_emipacing

hide emi onlayer master
with easeoutleft

$ renpy.music.set_volume(0.3, 1.0, channel="ambient")

"Sie rennt über die Laufbahn; ihre Haare wehen im Wind."


"Sie scheint jetzt viel schneller zu laufen als heute Morgen."


"Als sie auf die Gegengerade einbiegt, sehe ich kurz ihr Gesicht."


scene ev emi_run_face_zoomout_ss onlayer master
with locationchange

"Es sieht fast so aus wie heute Morgen, aber ihre Augen wirken irgendwie entschlossener."


"Sie hat wohl Recht."


"Ich weiß wirklich nicht viel über sie."


scene bg school_track_ss onlayer master
with locationchange

"Ich schaue ihr eine Weile beim Laufen zu und stehe dann auf, um zurück auf mein Zimmer zu gehen."


emi "Hey!"


"Sie sieht mich gehen und winkt, um auf sich aufmerksam zu machen."


emi "Nicht vergessen! Morgen früh um die gleiche Zeit, verstanden?"


hi "Geht klar."


stop ambient fadeout 2.0

"Ich gehe zurück auf mein Zimmer."


"Die Hausaufgaben warten."



label de_E6:

scene bg school_track_ss onlayer master
with None

scene bg school_dormhisao_ni onlayer master
with shorttimeskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

"Ich kann nicht einschlafen."


"Mein Körper ist zwar müde, aber meine Gedanken halten mich wach, und so starre ich in meinem finsteren Zimmer die Decke an."


"Verzweifelt versuche ich, meine Gedanken in irgendwelche Bahnen zu lenken, in der Hoffnung, dass mein Gehirn auch irgendwann müde wird."


"Alles, was mir einfällt, ist, dass mir nichts einfällt."


"Das bringt so nichts."


"Ich frage mich, ob das eine Nebenwirkung meiner Medikamente ist, aber es wäre schon etwas seltsam, wenn die sich erst jetzt bemerkbar machen würde."


"Vielleicht habe ich mich auch nur noch nicht so gut an meine neue Umgebung gewöhnt wie ich dachte."


"Ich habe keine Ahnung, aber warum auch immer – ich bin wach, und ich sollte eigentlich schlafen."


"Das ist lächerlich."


play sound sfx_switch

scene bg school_dormhisao onlayer master
with Dissolve(0.2)

"Ich ignoriere meine steifen Glieder, verlasse mein Bett und schaue auf meine Uhr."


"Vier Uhr morgens. Letztes Mal, als ich nachgeschaut habe, war es erst eins. Vielleicht habe ich ja doch ein wenig geschlafen."


"Ich weiß es nicht."


"Ich ziehe mich an und verlasse mein Zimmer."


"Vielleicht tut mir ja ein Spaziergang gut."


scene bg school_courtyard_ni onlayer master
with locationskip

"Ich bin überrascht, wie kühl die Nachtluft ist – verglichen mit der relativen Wärme tagsüber."


"Ich kann beinahe meinen Atem sehen, während ich über den Schulhof wandere und darauf warte, dass entweder die Sonne aufgeht oder ich einschlafe."


"Momentan wäre mir egal, was zuerst passiert."


scene bg school_track_ni onlayer master at left
with locationchange

"Ich finde mich auf dem Sportplatz wieder – wo Emi zum ersten Mal nicht gerade am Laufen ist."


"Ich sollte nicht überrascht sein; es ist sogar für ihre Verhältnisse zu früh."


"Die Sitze auf der Tribüne sind kalt, aber im Moment finde ich das Gefühl angenehm."


show bg school_track as overlay onlayer master:
    left
    alpha 0.0
    linear 15.0 alpha 0.5
with None

"Die Sonne zeigt sich langsam am Horizont, und ich weiß mit fürchterlicher Gewissheit, dass ich heute keinen Schlaf mehr finden werde."


"Die stärker werdenden Sonnenstrahlen beginnen mich aufzuwärmen, und ich beobachte, wie der Tau auf dem Boden zu dampfen beginnt."


"Meine Gedanken beruhigen sich ein wenig."


stop music fadeout 2.0

scene black onlayer master
with shuteye

window hide

with Pause(3.0)

play sound sfx_rustling

window show hpunch

"Irgendjemand schüttelt mich."


emi "Hey, wach auf!"


hi "Hä? Wo? Was?"


scene bg school_track onlayer master
show emi basic_shock_gym_close onlayer master at center
with openeyefast

"Ich bin wohl doch noch eingeschlafen."


show emi basic_annoyed_gym_close onlayer master
with charachange

emi "Was machst du denn hier draußen? Du holst dir noch eine Erkältung oder so was!"


play music music_dreamy fadein 4.0

"Ich reibe mir die Augen und sehe mich Emi gegenüber, die sich mit einem besorgten Gesichtsausdruck über mich beugt."


"Ich bin immer noch ziemlich kaputt, also ist meine Antwort mehr ein Gemurmel."


hi "Konnte nicht schlafen. Hab den Sonnenaufgang angeschaut."


show emi basic_confused_gym_close onlayer master
with charachange

emi "Hört sich an, als würde es von Rin kommen."


"Ich zucke mit den Schultern und fühle, wie steif ich bin, nachdem ich über eine Stunde auf einer Bank geschlafen habe."


hi "Tut es das? Keine Ahnung."


show emi basic_grin_gym_close onlayer master
with charachange

"Emi grinst, als sie meine (etwas griesgrämige) Antwort hört."


show emi basic_closedgrin_gym_close onlayer master
with charachange

emi "Also du konntest nicht schlafen? Sieht so aus, als müsste ich dich heute härter rannehmen!"


"Obwohl ich sie erst seit etwa einer Woche kenne, bin ich mir sicher, dass diese Art, ein Problem anzugehen, typisch für Emi ist."


hi "Hey, mein Körper war nach dem Tag gestern total erschöpft!"


hi "Nur mein Gehirn ist nicht zur Ruhe gekommen."


show emi basic_confused_gym_close onlayer master
with charachange

emi "Ich sehe da keinen Unterschied. Wenn du genug läufst wird dein Gehirn auch müde."


"Ich stelle mir ernsthaft die Frage, ob es eine gute Idee ist, das frühmorgens zu machen."


"Ich weiß nicht, ob meine Noten das mitmachen, wenn ich mein Gehirn dermaßen auslauge."


show emi basic_closedgrin_gym_close onlayer master
with charachange

with vpunch

show emi basic_closedgrin_gym onlayer master
with charadistant

"Emi hilft mir beim Aufstehen. Sie ist erstaunlich kräftig für jemanden ihrer Größe."


emi "Nun komm schon, Hisao! Wir haben noch was vor uns!"


"Ehrlich gesagt weiß ich nicht, ob ich heute dazu in der Lage bin."


"Ich meine, ich habe ganz offensichtlich kaum geschlafen… und als ich dann doch geschlafen habe, war das auf der Tribüne!"


hi "Ich weiß nicht… Sollte ich heute wirklich laufen?"


show emi basic_annoyed_gym onlayer master
with charachange

"Emi starrt mich verärgert an."


"Gott, steh mir bei."


show emi sad_annoyed_gym onlayer master
with charachange

emi "Was redest du da? Natürlich solltest du laufen!"


emi "Wie willst du sonst deine Verspannungen loswerden?"


show emi basic_annoyed_gym onlayer master
with charachange

emi "Du hast auf der Tribüne geschlafen, Herrgott noch mal!"


emi "Der beste Weg, solche Muskelschmerzen loszuwerden, ist ein wenig zu laufen."


emi "Nun hör auf, dich auf der Tribüne zu verstecken und komm mit runter!"



"Es ist sinnlos, zu widersprechen. Ich bin mir ziemlich sicher, dass sie mich umbringen würde, wenn ich nicht tue, was sie sagt."


"Ich steige die Tribüne hinunter und folge ihr zur Laufbahn."


scene bg school_track_on onlayer master
with locationchange

"Die Wärme der Sonne ist inzwischen deutlich zu spüren. Ich finde das sehr angenehm."


"Emi und ich fangen an uns aufzuwärmen, und ich muss mich wieder beherrschen, um sie nicht anzustarren."


"Wenn ich in Zukunft jeden Tag so aufwachen muss, könnte ich mich vielleicht daran gewöhnen."


show emi basic_annoyed_gym onlayer master
with charachange

emi "Weißt du, Hisao, es ist nicht nett, so zu starren."


hi "Ich habe nicht gestarrt! Ehrlich!"


"Emi zieht eine Augenbraue hoch und sieht mich nachdenklich an, als ob sie meine Antwort genau abwägen würde."


"Einen kurzen Moment lang fürchte ich um mein Leben."


show emi basic_closedhappy_gym onlayer master
with charachange

"Aber dann lächelt sie, lacht und schüttelt langsam den Kopf."


show emi basic_grin_gym onlayer master
with charachange

emi "Also ehrlich, du hättest es nicht ganz so energisch leugnen müssen."


stop music fadeout 5.0

"Anstelle einer Antwort klatsche ich in die Hände und wechsle das Thema."


hi "So! Das reicht jetzt mit Aufwärmen, oder?"


show emi sad_grin_gym onlayer master
with charachange

"Emi zuckt beiläufig mit den Schultern."


emi "Fühlst du dich aufgewärmt? Das ist es nämlich worauf es ankommt."


"Na ja, ich fühle mich bereit für den Lauf, wenn sie das meint."


hi "Ja, meinetwegen kann's losgehen."


show emi basic_grin_gym onlayer master
with charachange

emi "Genau wie gestern, okay?"


emi "Wir laufen vier Runden mit konstantem Tempo."


show emi basic_closedhappy_gym onlayer master
with charachange

emi "Versuch nicht, besonders schnell zu laufen, halte einfach deine Geschwindigkeit, verstanden?"


hi "Du bist der Boss."


play music music_running fadein 0.5

show emi basic_grin_gym onlayer master
with charachange

play ambient sfx_emijogging

hide emi onlayer master
with charamoveoutleft

$ renpy.music.set_volume(0.5, 2.0, channel="ambient")

"Emi grinst wieder, und wir laufen los."


scene bg school_track_running onlayer master
with Dissolve(2.0)

"…"

"…"

"Ich glaube, ich sterbe."


"Wir haben noch nicht einmal unsere erste Runde fertig, und meine Beine brennen schon."


"Mein Atem ist nur noch ein raues Keuchen."


"Ich fühle, wie der Schweiß mir die Stirn hinunter läuft – und wir sind gerade mal um die zweite Kurve."


$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

show emi basic_closedgrin_gym onlayer master at left
with charamoveinleft

emi "Komm schon, Hisao! Du hast noch drei Runden!"


$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi onlayer master
with easeoutleft

"Ich kann das nicht…"


"Ich kann das nicht."


"Ich kann das nicht!"


"Ich glaube, ich kotze gleich."


"Irgendwie sind wir nun auf der zweiten Runde. Emi schwitzt noch nicht einmal."


"Wie schafft sie das nur so mühelos?"


"Aus irgendeinem Grund bewege ich mich immer noch vorwärts."


"Sie ist wie eine Maschine."


"Dritte Runde. Was ist mit der zweiten passiert?"


$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

show emi excited_proud_gym onlayer master at left
with charamoveinleft

emi "Fast geschafft, Hisao!"


$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi onlayer master
with easeoutleft

"Lügnerin! Wir haben noch zwei!"


"Es hilft nichts."


hi "Ich… ka… kann… nicht… mehr."


$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

show emi basic_annoyed_gym onlayer master
with charamoveinleft

"Emi wirbelt herum und läuft rückwärts weiter."


"Ihr Gesicht ist so wütend, wie ich es noch nie gesehen habe."


show emi sad_angry_gym onlayer master
with charachange

emi "Sag das nie!"


emi "Wenn du das sagst, hast du schon verloren."


show emi sad_angry_gym onlayer master at left
with charamove

emi "Beweg dich! Solange du lebst, kannst du dich auch noch bewegen, verdammt noch mal!"


$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi onlayer master
with easeoutleft

"Wortwahl, Fräulein! Wir sind nun auf der vierten Runde."


"Sie will anscheinend wirklich, dass ich durchhalte."


"Weiterlaufen, Beine! Immer weiterlaufen! Sie fühlen sich so träge an."


"Ich laufe durch Schlamm… durch Sirup… durch Teer."


"Ich kann nicht weiterlaufen."


"Ich werde weiterlaufen!"


$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

show emi basic_grin_gym onlayer master at left
with charamoveinleft

emi "Endspurt, Hisao! Gib alles!"


$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi onlayer master
with easeoutleft

"Ich bewege meine Beine so schnell, wie sie bereit sind, mich zu tragen."


"Sie wollen mir immer wieder den Dienst verweigern."


"Irgendwie komme ich doch vorwärts."


"Irgendwie erreiche ich die Ziellinie."


stop ambient fadeout 0.5

show emi excited_happy_gym onlayer master at center
with charaenter

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

emi "Das war's, Hisao! Ich wusste, dass du es schaffst!"


"Der Zorn, den Emi noch vor einer Runde gezeigt hat, ist verflogen und durch Stolz ersetzt worden."


"Sie strahlt richtig, als ob sie gerade eine Goldmedaille gewonnen hätte oder so etwas."


scene bg school_track_on onlayer master
show emi excited_happy_gym onlayer master at center
with vpunch

"Ich komme zum Stillstand, falle vornüber auf meine Hände und Knie und schnappe nach Luft."


"Mein Herz klopft so heftig wie schon lange nicht mehr."


stop music fadeout 1.0

play sound sfx_heartslow
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack onlayer master
with Dissolve (0.2)

"Ich glaube so schlimm war es nicht, seit…"


play sound sfx_heartslow
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack onlayer master
with Dissolve (0.2)

"Oh Gott."


scene black onlayer master
with shuteyefast

play sound sfx_heartfast
show heartattack onlayer master
with Dissolve (0.1)

hide heartattack onlayer master
with Dissolve (0.2)

"Bitte beruhige dich, Herz!"


play sound sfx_heartfast
show heartattack onlayer master
with Dissolve (0.1)

hide heartattack onlayer master
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack onlayer master
with Dissolve (0.1)

hide heartattack onlayer master
with Dissolve (0.2)

"Ganz langsam werden. Ruhig."


play sound sfx_heartfast
show heartattack onlayer master
with Dissolve (0.1)

hide heartattack onlayer master
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack onlayer master
with Dissolve (0.1)

hide heartattack onlayer master
with Dissolve (0.2)

"Ich huste, und irgendwie schleicht sich ein Grinsen auf mein Gesicht."


play sound sfx_heartfast
show heartattack onlayer master
with Dissolve (0.1)

hide heartattack onlayer master
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack onlayer master
with Dissolve (0.1)

hide heartattack onlayer master
with Dissolve (0.2)

"Und so geht es also zu Ende, hm?"


play sound sfx_heartfast
show heartattack onlayer master
with Dissolve (0.1)

hide heartattack onlayer master
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack onlayer master
with Dissolve (0.1)

hide heartattack onlayer master
with Dissolve (0.2)

"Versuchen, in Form zu bleiben?"


play sound sfx_heartfast
show heartattack onlayer master
with Dissolve (0.1)

hide heartattack onlayer master
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack onlayer master
with Dissolve (0.1)

hide heartattack onlayer master
with Dissolve (0.2)

"Was für eine Ironie."


play sound sfx_heartfast
show heartattack onlayer master
with Dissolve (0.1)

hide heartattack onlayer master
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack onlayer master
with Dissolve (0.1)

hide heartattack onlayer master
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack onlayer master
with Dissolve (0.1)

hide heartattack onlayer master
with Dissolve (0.2)

"Ich bin fast soweit aufzugeben."


play sound sfx_heartslow
show heartattack onlayer master
with Dissolve (0.1)

hide heartattack onlayer master
with Dissolve (0.8)

play sound sfx_heartslow
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack onlayer master
with Dissolve (0.8)

play sound sfx_heartslow
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack onlayer master
with Dissolve (0.2)

"Aber dann fühle ich, wie mein Herz sich beruhigt."


"Zwei Hände greifen mir unter die Arme und ziehen mich hoch."


scene bg school_track_on onlayer master
show emi basic_confused_gym_close onlayer master at center
with openeye

"Ich hebe meinen Kopf und sehe Emi vor mir stehen. Ihr Gesicht zeigt eine Mischung aus Freude und Sorge."


emi "Auf die Beine!"


show emi sad_grin_gym_close onlayer master
with charachange

emi "Komm schon, so kommst du nie wieder zu Atem."


"Irgendwie schaffe ich es, aufzustehen. Ich versuche meine Arme über meinen Kopf zu heben, aber sie fühlen sich schwer wie Blei an."


"Ich fange an, um das Sportfeld zu gehen. Emi bleibt ganz in meiner Nähe, als ob sie Angst hätte, dass ich umkippe."


"Das ist gar nicht mal so unwahrscheinlich."


"Ich fühle mich furchtbar und sage das auch."


show emi basic_closedhappy_gym_close onlayer master
with charachange

"Emi lacht."


show emi basic_happy_gym_close onlayer master
with charachange

emi "Aber du hast es zu Ende gebracht, oder?"


show emi basic_grin_gym_close onlayer master
with charachange

emi "Du hast gesagt, du schaffst es nicht, aber du hast es doch geschafft."


emi "Ist es das nicht wert?"


"Da bin ich mir nicht sicher, und ich habe nicht wirklich genug Atem, um das zu sagen."


"Aber das leichte Grinsen von vorhin ist immer noch auf meinem Gesicht."


"Was soll's, wenn mein Herz schwach ist?"


"Ich habe diesen Morgen trotzdem überlebt."


"Vielleicht werde ich den morgigen auch überleben."


scene bg school_track onlayer master
with shorttimeskip

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")

play ambient sfx_emisprinting

"Sobald sie sich sicher ist, dass ich nicht plötzlich umkippen werde, beginnt Emi mit ihren Sprints."


"Ich habe keine Ahnung, wie zum Teufel sie es schafft, Sprints zu laufen, nachdem sie schon eine Meile gerannt ist. Sie ist einfach viel besser in Form als ich es bin."


"Während ich meine Runde gehe, beobachte ich wieder einmal Emi beim Sprinten."




scene ev emi_run_face_zoomin onlayer master
with locationchange

"Es ist seltsam, aber sie ist wie verwandelt, wenn sie an ihre Grenzen geht."


"Letztes Mal sind mir ihre Augen aufgefallen, aber dieses Mal erregt ihr Mund meine Aufmerksamkeit."


"Das ist nicht ihr normales Grinsen."


"Sie lächelt immer noch, aber nun ist es irgendwie angespannt."


"Es ist fast schon grimmig, als ob sie auf verlorenem Posten kämpft und sie das überhaupt nicht kümmert."


"Sie legt noch einen Zahn zu, genau wie gestern."


"Der Schweiß rinnt ihr über das Gesicht, aber sie läuft weiter."


"Schließlich öffnet sie ihren Mund, als sie nicht mehr genug Luft durch die Nase bekommt."


"Als sie wieder an mir vorbei läuft, mit schwingenden Armen und leicht geöffneten Lippen…"


"… sieht sie wunderschön aus."


stop ambient fadeout 2.0

scene bg school_track onlayer master
with shorttimeskip

play music music_normal fadein 3.0
$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

"Nachdem wir beide ein paar Runden zum Abkühlen gelaufen sind, verwandelt sich Emi zurück in ihr normales Ich."


"Die Verwandlung, die ich gesehen habe, ist vorbei."


show emi basic_happy_gym onlayer master at center
with charaenter

emi "Keine schlechte Leitung heute, Hisao."


"In ihrer Stimme klingt fast schon Bewunderung."


hi "Wie meinst du das? Ich hätte aufgegeben, wenn du mich nicht angeschrien hättest."


show emi sad_shyblush_gym onlayer master
with charachange

"Emi wird ein wenig rot; anscheinend ist ihr der Gefühlsausbruch peinlich."


emi "Das tut mir leid, es ist nur… Ich kann es nicht ausstehen, wenn Leute aufgeben wollen."


emi "Besonders bei so etwas."


show emi sad_grin_gym onlayer master
with charachange

emi "Wenn jemand sagt „Ich kann nicht mehr,” obwohl er in dem Moment ganz offensichtlich noch am Laufen ist, ist das dumm."


emi "Das ist alles, worum es mir geht."


hi "Was? Dumme Dinge sagen?"


show emi basic_annoyed_gym onlayer master
with charachange

"Emi streckt mir die Zunge heraus."


emi "Idiot. Ich meine, dir zu zeigen, dass du am Leben bist."


"Mir zeigen, dass ich am Leben bin, hmm? Ich wusste nicht, dass das so schmerzhaft sein muss."


"Aber trotzdem fühlt es sich ziemlich gut an."


show emi excited_proud_gym onlayer master
with charachange

emi "Außerdem war das heute einer der schwierigsten Tage."


hi "Wie meinst du das?"


show emi basic_grin_gym onlayer master
with charachange

emi "Immer, wenn man mit einem Training beginnt, ist der erste Tag hart, der zweite Tag ist {i}richtig{/i} hart, und am dritten Tag wird es dann leichter."


emi "Es gibt zwar immer wieder Tage, die richtig hart sind, aber die kommen immer seltener vor."


hi "Also wird das irgendwann ganz einfach sein, hmm?"


show emi basic_closedhappy_gym onlayer master
with charachange

emi "Ja, na klar."


show emi basic_closedgrin_gym onlayer master
with charachange

emi "Aber dann musst du die Schwierigkeit erhöhen, sonst kommst du nicht voran."


emi "Du wirst nur selbstzufrieden und hast kein Erfolgsgefühl mehr."


hi "Also muss ich dann mehr als nur vier Runden laufen, hmm?"


show emi excited_proud_gym onlayer master
with charachange

emi "Jup! Aber erst mal noch nicht – du musst vorsichtig sein, weißt du?"


"Emi scheint eine Idee zu haben, und ihre Miene hellt sich auf."


show emi basic_closedhappy_gym onlayer master
with charachange

emi "Ich hab's!"


hi "Was hast du?"


show emi basic_happy_gym onlayer master
with charachange

emi "Du kommst mit mir zu Doc! Dann fällst du nicht tot um oder so was!"


"Wie reizend."


hi "Äh… Wann?"


show emi basic_grin_gym onlayer master
with charachange

emi "Jetzt gleich natürlich! Du musst doch auch noch duschen und alles, oder? Wir haben also nicht mehr viel Zeit!"


"Sie greift meine Hand, läuft los und schleift mich hinter sich her."


stop music fadeout 2.0


label de_E7:

scene bg school_nurseoffice onlayer master
show nurse neutral onlayer master at center
with shorttimeskip

nk "Mein Gott, hast du es aber heute eilig, Emi!"


play music music_nurse fadein 2.0

"Ich habe keine Ahnung, wie wir so schnell in Docs Büro gekommen sind, aber hier sind wir."


show nurse neutral onlayer master at twoleft
show bg school_nurseoffice onlayer master at bgleft
with charamove

show emi basic_grin_gym onlayer master at tworight
with charaenter

"Doc grinst Emi an und scheint mich komplett zu ignorieren."


show nurse grin onlayer master
with charachange

nk "Weißt du, du hast noch reichlich Zeit, um zu duschen und zum Unterricht zu kommen."


show nurse concern onlayer master
with charachange

nk "Kein Grund, so durch die Gänge zu rennen. Ich konnte dich schon kilometerweit hören!"


"Irgendwie hört es sich nicht so an, als würde er wirklich mit Emi schimpfen."


"Es ist mehr, als wäre das bei den beiden reine Gewohnheit."


"Emi tut so, als hätte sie ein schlechtes Gewissen, aber ich kenne sie inzwischen gut genug, um mich nicht täuschen zu lassen."


show emi excited_sad_gym onlayer master
with charachange

emi "Tut mir leid! Ich werd's nie wieder tun!"


show nurse grin onlayer master
show emi basic_closedhappy_gym onlayer master
with charachange

"Doc und Emi lachen beide über irgendeinen Insiderwitz."


show emi basic_grin_gym onlayer master
show nurse neutral onlayer master
with charachange

"Dann scheint er mich zu bemerken."


show nurse fabulous onlayer master
with charachange

nk "Ah, hallo Hisao."


show nurse neutral onlayer master
with charachange

nk "Was führt dich zu mir?"


hi "Na ja, ich habe-{w=.3}{nw}"


show emi basic_closedgrin_gym onlayer master
with charachange

emi "Hisao ist nun offiziell mein Trainingspartner."


"Ich fange an zu erklären, aber Emi unterbricht mich."


show emi basic_happy_gym onlayer master
with charachange

emi "Ich dachte, er sollte auch bei dir vorbei schauen, damit er nicht stirbt oder so was."


show nurse fabulous onlayer master
with charachange

"Doc hebt mit gespieltem Entsetzen die Augenbrauen."


nk "Ja, das wäre schlecht. Dann wäre ich bald meinen Job los, nicht wahr?"


show nurse neutral onlayer master
show emi basic_grin_gym onlayer master
with charachange

nk "Nun, Hisao, dann lass uns dich mal anschauen."


nk "Hebst du bitte dein T-Shirt hoch?"


"Mir wird plötzlich bewusst, dass Emi noch mit uns im Zimmer ist, und obwohl ich versuche, mir nichts anmerken zu lassen, werde ich rot."


"Doc spürt mein Unbehagen, aber es scheint ihn nur zu amüsieren."


show nurse grin onlayer master
with charachange

nk "Sind wir etwa schüchtern?"


"Er schaut entschuldigend zu Emi."


nk "Tut mir leid, Emi. Ich habe versucht, dir eine Gratisvorstellung zu verschaffen, aber es hat anscheinend nicht geklappt."


show emi basic_annoyed_gym onlayer master
with charachange

"Emi versteift sich leicht und schaut Doc genervt an."


emi "Du bist ein Arschloch."


show emi excited_proud_gym onlayer master
with charachange

"Sie verbeugt sich entschuldigend vor mir."


emi "Ich warte draußen, okay Hisao?"


hide emi onlayer master
with charaexit

show nurse grin onlayer master at center
show bg school_nurseoffice onlayer master at center
with charamove

"Ich stammele irgendetwas, dass es nicht so schlimm ist und dass sie ruhig bleiben kann, aber sie ist schon zur Tür hinaus, und Doc lacht, als er ihr hinterherschaut."


show nurse fabulous onlayer master
with charachange

nk "Ha! Ich hab's immer noch drauf!"


hi "Ich kann Ihnen nicht folgen."


show nurse grin onlayer master
with charachange

"Er lacht noch einmal, als wäre es ein Witz, den ich nicht verstehen kann."


nk "Ich kann sie immer noch verlegen machen. Das ist so eine Art Wettkampf, den wir schon ziemlich lange austragen."


"Das hört sich irgendwie ziemlich unheimlich an, und es scheint, als ob das Doc auch aufgefallen ist."


show nurse concern onlayer master
with charachange

nk "Ähm. Wenn ich darüber nachdenke… Das klang jetzt vielleicht schlimmer, als es in Wirklichkeit ist."


hi "Ich habe gar nichts gesagt…"


nk "Nein nein, du hast Recht. Ich sollte es dir erzählen, damit du keinen falschen Eindruck bekommst."


show nurse neutral onlayer master
with charachange

nk "Ich bin ziemlich neu hier, weißt du? Ich wurde im gleichen Jahr angestellt, als Emi hier angefangen hat."


nk "Davor habe ich Emi während ihrer Rehabilitierung nach ihrem Unfall betreut."


"Moment mal, was?"


show nurse concern onlayer master
with charachange

nk "Man musste ihre Beine nach einem schweren Autounfall amputieren. Sie wäre fast gestorben, wie-"



"Er verstummt abrupt. Ich brauche einen Moment, um diese unerwarteten Informationen zu verarbeiten."


nk "Nun, das sollte ich wirklich nicht erzählen. Jedenfalls kennen wir uns schon ziemlich lange."


nk "Also haben wir eine etwas familiärere Beziehung als einfach nur Arzt und Patientin."


"Er scheint etwas verlegen zu sein, als hätte er etwas Dummes getan."


"Sieht aus, als wäre er deswegen richtig besorgt. Ich winke ab, um ihn wissen zu lassen, dass es nicht so schlimm ist."


hi "Keine Sorge, ich verspreche, dass ich sehr diskret sein werde."


"Ich hatte mich schon gefragt, wie Emi ihre Beine verloren haben könnte, und das war eines der Szenarios, die mir eingefallen sind."


"So viele Möglichkeiten gibt es ja nicht, aber nun wirklich die Fakten zu hören… Es ist immer noch ein wenig schockierend."


show nurse neutral onlayer master
with charachange

nk "Na ja… Danke. Du bist ein guter Junge, Hisao."


nk "Ich verstehe, warum Emi sich mit dir angefreundet hat."


show nurse fabulous onlayer master
with charachange

nk "Sie ist ziemlich schwer unterzukriegen, weißt du?"


hi "Wie meinen Sie das?"


nk "Du hast nicht gesehen, wie sie wieder Laufen gelernt hat. Sie hat viel mehr getan als alle anderen im Krankenhaus. Sie hat sich geweigert, aufzugeben."


nk "Normalerweise dauert es Jahre, bis man an den Punkt kommt, wo man überhaupt wieder ans Laufen denken kann. Emi hat das alles in etwa einem Jahr geschafft."


"Er sieht beinahe so aus, als wäre er stolz auf sie – wie ein Vater, dessen Tochter einen Wettbewerb gewonnen hat."


show nurse neutral onlayer master
with charachange

nk "Verdammt, sie hätte es wahrscheinlich noch schneller geschafft, wenn wir sie nicht zurückgehalten hätten."


hi "Zurückgehalten? Warum?"


show nurse concern onlayer master
with charachange

stop music fadeout 4.0

nk "Weil sie so lange trainiert hat, dass ihre Beine angefangen haben zu bluten, wo sie mit den Prothesen in Kontakt kamen."


nk "Das ist ein echtes Problem – deswegen kommt sie auch jeden Tag nach dem Training zu mir."


nk "Ganz zu schweigen von dem Risiko von Infektionen, wenn sie eine Wunde am Bein hat und die Prothesen schmutzig sind."


show nurse neutral onlayer master
with charachange

nk "Aber genug davon."


show nurse fabulous onlayer master
with charachange

play music music_nurse fadein 2.0

nk "Wenn wir nicht bald fertig sind, denkt Emi noch, dass wir was aushecken."


"Während er das sagt, zwinkert er und hört meine Brust ab."


"Das Stethoskop ist viel zu kalt."


"Er hätte es aufwärmen sollen, bevor er es benutzt."


"Nach kurzer Zeit richtet er sich zufrieden auf."


show nurse neutral onlayer master
with charachange

nk "Nun, das hört sich ganz gut an, Hisao. Hattest du beim Laufen irgendwelche Schmerzen?"


hi "Nein, nicht wirklich. Ich hatte aber Schwierigkeiten Luft zu kriegen – und gegen Ende war mein Herz auch ziemlich am Rasen."


show nurse concern onlayer master at center
with charachange

"Doc runzelt die Stirn, als ich das erzähle, aber dann zuckt er mit den Schultern."


show nurse neutral onlayer master at center
with charachange

nk "Das ist wahrscheinlich, einfach weil du außer Form bist… Aber wenn das nicht besser wird, sagst du es mir, okay?"


nk "Verlang dir nicht zu viel ab, und wenn du irgendwelche Brustschmerzen hast, kommst du direkt zu mir, okay?"


"Ich ziehe mein T-Shirt wieder an, und Doc geht zur Tür, um Emi hereinzurufen."


show nurse neutral onlayer master at twoleft
show bg school_nurseoffice onlayer master at bgleft
with charamove

show emi basic_annoyed_gym onlayer master at tworight
with charaenter

emi "Warum hat das denn so lange gedauert? Jetzt komme ich zu spät!"


stop music fadeout 2.0

show nurse fabulous onlayer master
with charachange

"Doc wirft mir einen bedeutungsvollen Blick zu."


show nurse grin onlayer master
with charachange

nk "Ich habe nur versucht, Hisao zu verführen. Das ist alles."


play music music_comedy fadein 0.5

show emi sad_annoyed_gym onlayer master
with charachange

emi "Was!? Habe ich dir nicht gesagt, du sollst nicht immer meine Freunde verführen?"


"Ich hätte erwartet, dass Emi darauf schockiert reagiert, aber sie scheint nur genervt zu sein und schimpft Doc aus wie ein Kind, das aus der Keksdose genascht hat."


"Währenddessen versuche ich nicht schon wieder rot anzulaufen."


show nurse fabulous onlayer master
with charachange

nk "Ich versuche mich in Zukunft zurückzuhalten, aber ich fürchte, unser junger Hisao hier könnte für das weibliche Geschlecht auf ewig verloren sein!"


stop music fadeout 0.5

hi "Ganz bestimmt nicht!"


with Pause(3.0)

play music music_comedy fadein 0.5

show nurse grin onlayer master
show emi excited_laugh_gym onlayer master
with charachange

"Ich wollte das eigentlich nicht laut sagen, aber sowohl Doc als auch Emi schauen mich ein paar Sekunden lang an und brechen dann in lautes Gelächter aus."


show emi basic_happy_gym onlayer master
with charachange

emi "Ich hab dir doch gesagt, dass er lustig ist, oder?"


"Hä? Sieht aus, als würde Emi mit Doc über sehr viele Dinge reden."


show nurse fabulous onlayer master
show emi basic_grin_gym onlayer master
with charachange

nk "Nun, Hisao, du solltest am besten los. Du musst noch duschen, bevor der Unterricht losgeht, nicht wahr?"


"Verdammt! Er hat Recht, und es sieht aus, als hätte ich nur noch eine halbe Stunde!"


hi "Danke für alles. Wir sehen uns später, Emi!"


scene bg school_nursehall onlayer master
with locationchange

stop music fadeout 5.0

"Ich stürze aus dem Raum, während Doc Emi hilft, ihr die Prothesen abzunehmen."


"Als ich schon auf dem Flur bin, höre ich gerade noch seine Stimme."


nk "Emi, du musst wirklich vorsichtiger sein…"


scene bg school_dormhisao onlayer master
with locationskip

"Ich schaffe es zurück in mein Zimmer und dusche in Rekordzeit. Mir fällt auf, dass ich schon seit vier Stunden wach bin, und der Unterricht hat noch nicht einmal angefangen."


"Das wird ein sehr, sehr langer Tag werden."


"Ich hoffe, dass ich nicht im Unterricht einschlafe."


$ suppress_window_after_timeskip = True

scene black onlayer master
with dissolve


label de_E8:


window hide None

scene black onlayer master
with dissolve

show bg school_dormhisao onlayer master
with openeye

window show

play music music_pearly fadein 5.0

"Anstelle meines Weckers weckt mich heute die Morgensonne vor meinem Fenster. Heute muss Sonntag sein."


"Emi hat mich freundlicherweise an den Wochenenden von meinen Trainingseinheiten entbunden."


"Ich weiß nicht, ob ich gestern überhaupt aufgewacht bin oder ob ich den ganzen Tag durchgeschlafen habe."


"Meine Beine protestieren heftig, als ich sie aus dem Bett schwinge."


"Dieses ganze Rennen hat mich wirklich ausgelaugt."


"Dennoch kann ich nicht leugnen, dass Emi mich nicht angelogen hat."


"Es ist etwas einfacher geworden."


"Ich hatte ja Bedenken, dass mir das Laufen schnell auf die Nerven gehen würde, aber bisher war es nicht so schlimm."


"Na ja, es war ja nur eine Woche."


"Ich denke, ich habe noch genug Zeit, den Klang meines Weckers fürchten zu lernen."


"Nicht dass ich jetzt noch aussteigen könnte."


"Wie Emi schon sagte, es ist schwieriger mit etwas aufzuhören, wenn da noch jemand anderes ist."


"Und ehrlich gesagt glaube ich nicht, dass ich mit einer enttäuschten Emi umgehen könnte."


"Sie müsste mich wahrscheinlich nur mit diesem Welpenblick anschauen, und ich würde mir furchtbar gemein vorkommen."


"Da fällt mir ein… Sollte ich heute nicht irgendwo hingehen?"


$ renpy.music.set_volume(0.3,2.0,channel="music")

scene bg school_track_fb onlayer master
show emi basic_closedhappy_gym_fb onlayer master at center
show noiseoverlay onlayer master
with flashback

emi "Hey, du kommst doch zu meinem Leichtathletikturnier am Sonntag, oder?"


show emi basic_grin_gym_fb onlayer master
with charachange

emi "Was rede ich denn da, natürlich kommst du."


show emi sad_grin_gym_fb onlayer master
with charachange

emi "Oder?"


"Wieder dieser Welpenblick."


hi "Natürlich komme ich!"


hi "Ich bin dir was schuldig, nicht wahr?"


show emi excited_proud_gym_fb onlayer master
with charachange

emi "Genau! Also nicht vergessen, okay?"


$ renpy.music.set_volume(1.0,2.0,channel="music")

scene bg school_dormhisao onlayer master
with flashforward

"Verdammt, heute ist Emis Leichtathletikturnier!"


"Ich sollte mich besser beeilen, wenn ich ihren Lauf nicht verpassen will, wenn sie schon der einzige Grund ist, warum ich überhaupt hingehe."


"Sonst wäre mein ganzer Besuch dort sinnlos."


scene bg school_courtyard onlayer master
show crowd onlayer master
with shorttimeskip

play ambient sfx_crowd_outdoors fadein 3.0

"Und so stehe ich kure Zeit später inmitten einer Menschenmenge, die alle sehen wollen, wie unsere Leitathletikmannschaft gegen das Team einer anderen Schule wie dieser antritt."


$ renpy.music.set_volume(0.5, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

nvl clear

nvl show dissolve

n "\nIch geb's zu, es ist fast schon tröstlich, zu wissen, dass wir nicht die einzige Schule dieser Art sind."


n "Wenn man sieht, dass es {b}zwei{/b} Schulen voller… defekter Jugendlicher geben kann…"


n "… Man fühlt sich irgendwie nicht mehr so defekt."


n "Man fühlt sich auch nicht mehr so einzigartig. In den meisten Fällen wäre das wohl etwas Schlechtes, aber in diesem Fall ist es das mit Sicherheit nicht."


n "Das ist wohl der Reiz der Yamaku."


n "Lerne, dass du nicht einzigartig bist… Verdammt, lerne, dass es eine Menge andere gibt, die alles geben würden, um deine Probleme zu haben statt ihrer eigenen."


n "Einige der Leute hier sind nicht hier, weil ihnen ein Bein fehlt oder weil sie ein Herzproblem haben."


n "Einige von ihnen sind hier, weil sie in zwei Jahren sehr wahrscheinlich tot sind – vielleicht in drei, wenn sie Glück haben."


n "Und das auch nur, wenn sie die richtige Pflege erhalten."


n "Es ist ein schwacher Trost, sagen zu können „Na ja, zumindest habe ich eine gute Chance zu überleben, bis ich mit der Uni fertig bin,” aber es ist zumindest ein Trost."


$ renpy.music.set_volume(1.0, 2.0, channel="ambient")
$ renpy.music.set_volume(1.0, 2.0, channel="music")
nvl clear

nvl hide dissolve

window show

stop music fadeout 3.0

"Ich sehe Rin am Aufgang zur Tribüne stehen, und das reißt mich aus meinen ziemlich morbiden Gedanken."


show rin basic_deadpannormal onlayer master at center
with charaenter

rin "Du bist gekommen."


hi "Na klar. Ich hab doch gesagt, dass ich komme, oder?"


show rin basic_deadpanamused onlayer master
with charachange

rin "Das heißt nicht unbedingt, dass du es auch tust."


show rin basic_awayabsent onlayer master
with charachange

rin "Viele Leute sagen Dinge, die sie nicht ernst meinen."


hi "Nun, ich zumindest nicht."


play music music_soothing fadein 0.5

show rin relaxed_boredom onlayer master
with charachange

"Rin zuckt mit den Schultern. Anscheinend langweilt sie unser Gespräch, und sie macht auf dem Absatz kehrt und geht zurück auf die Tribüne."


rin "Ich schulde Emi nun Geld."


hi "Warum das?"


show rin basic_absent onlayer master
with charachange

rin "Ich hätte nicht gedacht, dass du kommst."


rin "Emi schon."


show rin basic_awayabsent onlayer master
with charachange

rin "Also schulde ich ihr 500 Yen."


hi "Ihr Zwei wettet ganz schön oft, nicht wahr?"


"Ein weiteres Achselzucken meiner armlosen Gefährtin."


show rin basic_deadpan onlayer master
with charachange

rin "Ich denke nicht."


scene bg school_track onlayer master
show crowd onlayer master
show rin basic_deadpan onlayer master
with locationchange

"Wir betreten die Tribüne und Rin nickt in Richtung der oberen Ränge."


show rin negative_spaciness onlayer master at center
with charaenter

rin "Da oben."


show rin basic_deadpancontemplation onlayer master
with charachange

rin "Ich bin runtergekommen, um zu sehen, ob du kommst."


"Wegen der Wette nehme ich an."


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

"Neben Rin sitzt eine ältere Frau – wohl die Mutter von irgendjemanden, nehme ich an."


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

rin "Was zum Essen?"


show rin relaxed_nonchalant onlayer master
with charachange

rin "Ich hatte mich schon gewundert, was ich da unten wollte."


show meiko happy onlayer master
show rin basic_awayabsent onlayer master
with charachange

"Die Frau lacht, und wieder kommt sie mir bekannt vor."


"Wo habe ich sie schon mal gesehen?"


show meiko smile onlayer master
with charachange

emm_ "Na ja, du warst ja schon immer jemand, der eine Sache holen will und mit einer anderen zurückkommt."


emm_ "Aber wo hab ich denn meine Manieren. Ich habe mich noch gar nicht vorgestellt."


emm_ "Ich bin Meiko Ibarazaki, Emis Mutter."


show meiko happy onlayer master
with charachange

emm "Freut mich, dich kennenzulernen."


"Nun, das erklärt alles."


"Sie sieht aus wie eine größere, ältere und besser bestückte Emi."


"Abgesehen davon, dass ihre Haare einen Tick dunkler sind als Emis, ist die Ähnlichkeit wirklich unverkennbar."


show rin basic_absent onlayer master
show meiko smile onlayer master
with charachange

hi "Tut mir leid, Ich bin Hisao. Hisao Nakai."


hi "Und Sie müssen sich wirklich nicht entschuldigen, dass sie sich nicht vorgestellt haben, Frau Ibarazaki."


hi "Das wäre in dieser Situation doch Rins Aufgabe, oder?"


show meiko happy onlayer master
show rin basic_awayabsent onlayer master
with charachange

"Emis Mutter lacht erneut."


emm "Ich nehme an, du kennst Rin noch nicht sehr lange?"


show meiko smile onlayer master
with charachange

emm "So etwas sollte man besser nicht von ihr erwarten."


show meiko wink onlayer master
with charachange

emm "Ich nehme an, sie hat andere Dinge im Kopf."


show rin basic_deadpannormal onlayer master
with charachange

"Rin nickt, zufrieden mit dieser Einschätzung."


show rin basic_deadpan onlayer master
with charachange

rin "Sie hat Recht."


show rin basic_lucid onlayer master
with charachange

rin "Ich habe gerade über Sonnenuntergänge nachgedacht."


show meiko happy onlayer master
show rin basic_awayabsent onlayer master
with charachange

emm "Siehst du? Es liegt also an uns, uns bekannt zu machen und so weiter."


"Ich nicke, weil mir nichts besseres einfällt."


"Frau Ibarazaki lehnt sich ein wenig in ihrem Sitz zurück und hebt eine Augenbraue."


$ renpy.music.set_volume(0.0, 0.5, channel="ambient")

show meiko serious onlayer master
with charachange

stop music fadeout 0.8

emm "Also, seit wann seid ihr beiden zusammen?"


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

hi "Vielleicht."


show rin basic_awayabsent onlayer master
with charachange

emm "Also ist die Romanze noch frisch, nicht wahr?"


show rin basic_absent onlayer master
with charachange

hi "Moment, darum geht es nicht, das-"


show meiko happy onlayer master
show rin basic_awayabsent onlayer master
with charachange

"Ein weiteres Lachen."


show meiko smile onlayer master
with charachange

emm "Ich weiß, aber es ist so lustig zu sehen, wie du dich windest."


show meiko wink onlayer master
with charachange

emm "Es tut mir leid. Vergib einer alten Frau ihre kleinen Freuden."


"Alte Frau?"


"Sie sieht für mich alles andere als alt aus."


"Es ist offensichtlich, von wem Emi ihr jugendliches Aussehen hat."


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


"Sieht aus wie der 400-Meter-Lauf."


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

"Emi fliegt wie ein Geschoss von ihrem Startblock und ist mit dem bloßen Auge kaum noch klar zu erkennen."


"Es ist fantastisch. Schon als die Läuferinnen auf der innersten Spur zusammenkommen, setzt sich Emi an die Spitze des Feldes."


"Als sie um die letzte Kurve läuft, haben einige andere Läuferinnen zu ihr aufgeschlossen."


"Aber all ihre Mühen sind umsonst, denn nach Emis Schlussspurt liegen sie alle mindestens eine halbe Sekunde zurück."


scene ev emitrack_finishtop onlayer master:
    xalign 0.5 yalign 0.0 zoom 4.0 subpixel True
    0.2
    linear 0.3 zoom 1.05
    easein 8.0 zoom 1.0
with flash

stop ambient fadeout 1.0
play sound sfx_crowd_cheer

"Frau Ibarazaki johlt, schreit und klatscht und benimmt sich generell so wie alle anderen Eltern, die ihre Kinder anfeuern."


"Emi verlässt die Laufbahn. Sieht aus, als wäre sie mit ihrer Leistung zufrieden."


play music music_daily fadein 2.0

scene bg school_track onlayer master at bgright
show meiko happy onlayer master at twoleft
show rin basic_deadpandelight onlayer master at tworight
with locationchange

"Ich juble zusammen mit den anderen."


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


hi "Du scheinst dich ja wirklich für so was zu interessieren. Das hätte ich nicht gedacht."


show rin basic_deadpansurprised onlayer master
with charachange

"Rin schaut mich fragend an."


rin "Warum sollte ich das nicht?"


hi "Kein besonderer Grund. Ich dachte nur, so was wie Sport wäre nichts für dich."


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

rin "Emi ist am meisten Emi wenn sie läuft."


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


"Als sie an den Startblock herantritt, scheint sich ihr ganzer Körper zu entspannen, aber es ist eine unechte Entspannung."


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


"Nach ein paar Sekunden ist alles vorbei, aber in diesen wenigen Sekunden habe ich wohl etwas erlebt, was für Emi sehr persönlich ist."


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


show meiko worry onlayer master
show rin basic_awayabsent onlayer master
with charachange

emm "Nein, Emi hat ihr Talent einzig und allein von ihrem Vater."


"Als sie Emis Vater erwähnt, sieht Frau Ibarazaki wehmütig, fast traurig aus."


emm "Er hat ihr das alles beigebracht, weißt du?"


show rin basic_absent onlayer master
with charachange

hi "Ja, das hat sie mir erzählt."


"Ich bin mir nicht sicher, ob es unhöflich von mir wäre, nach Emis Vater zu fragen."


"Aber wenn ich mich an ihren Gesichtsausdruck vor ein paar Tagen erinnere, muss ich einfach fragen."


hi "Wenn ich fragen darf – wo ist ihr Vater jetzt?"


"Emis Mutter zögert. Sie möchte offensichtlich die Frage nicht beantworten, will aber auch nicht unhöflich sein."


show meiko serious onlayer master
show rin basic_awayabsent onlayer master
with charachange

emm "Er… ist nicht mehr da."


hi "Es tut mir leid, Ich wollte keine schlechten Erinnerungen wachrufen."


show rin basic_absent onlayer master
with charachange

hi "Es ist nur, dass Emi ein wenig traurig zu sein schien, als sie ihn erwähnt hat."


show meiko worry onlayer master
show rin basic_awayabsent onlayer master
with charachange

emm "Das überrascht mich nicht, wenn man bedenkt…"


hi "Hmm?"


emm "Sie standen sich sehr nahe."


show rin basic_absent onlayer master
with charachange

hi "Verstehe."


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

"Ich gebe zu, dass ich einen Moment lang geträumt habe."


"Ich hätte fast den Anfang des Staffellaufes verpasst. Aber als ich nach unten schaue, kann ich Emi nicht finden."


hi "Ich dachte, Emi läuft auch in der Staffel."


show rin basic_deadpan onlayer master
with charachange

rin "Sie ist die Schlussläuferin."


show rin basic_deadpannormal onlayer master
with charachange

rin "Es dauert noch eine Weile, bis sie dran ist."


hi "Ah."


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

"Das Rennen beginnt, und ich feuere Emis Teamkameraden an, während der Stab in den Händen der Läufer seine Runden um den Platz macht."


play ambient sfx_emisprinting

scene ev emitrack_running onlayer master:
    truecenter zoom 1.0 subpixel True
    ease 20.0 zoom 1.05 xalign 0.0 yalign 0.0
with locationskip

"Schließlich sprintet Emi zur letzten Übergabe auf die Bahn."


"Und wieder bin ich sprachlos, wie elegant sie beim Laufen aussieht."


"Es ist sieht wirklich wunderschön aus."


"Dieser Ausdruck von Entschlossenheit und Furchtlosigkeit auf ihrem Gesicht verstärkt diesen Eindruck nur noch."


"Das ist Emi wenn sie am emisten ist."


stop ambient fadeout 1.0
play sound sfx_crowd_cheer

show ev emitrack_finish onlayer master
with locationskip

"Aber dann, als sie die Ziellinie überquert, sehe ich, dass sie leicht stolpert."


"Es war kaum zu sehen, aber sie ist definitiv gestolpert."


$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

scene bg school_track onlayer master
show rin negative_worried onlayer master at center
with locationskip

"Rin zieht scharf die Luft ein, und sieht einen Moment lang richtig besorgt aus."


rin "Oh, Emi…"


hi "Glaubst du, sie hat sich verletzt?"


show rin basic_surprised onlayer master
with charachange

rin "Du hast es auch gesehen?"


show rin negative_confused onlayer master
with charachange

rin "Es muss ganz schön schlimm sein."


show rin negative_annoyed onlayer master
with charachange

"Sie runzelt die Stirn, als ob sie überlegt, was als nächstes zu tun ist."


"Schließlich ist das wohl doch zu ermüdend, und sie zuckt wieder mit den Schultern."


show rin basic_deadpanupset onlayer master
with charachange

rin "Na ja, lass uns runter gehen."


rin "Wir müssen ja die Siegerin krönen."


show rin basic_deadpanamused onlayer master
with charachange

rin "Sieh zu, ob du einen Lorbeerzweig findest."


hi "Das wird nicht leicht."


show rin basic_deadpannormal onlayer master
with charachange

"Rin zuckt mit den Schultern."


show rin basic_deadpan onlayer master
with charachange

rin "Zumindest haben wir es versucht."


"Na ja, wir haben uns nicht wirklich viel Mühe gegeben."


"Eigentlich gar keine… Aber was soll's."


stop music fadeout 5.0
stop sound fadeout 5.0
play ambient sfx_crowd_outdoors fadein 2.0

scene bg school_track_on onlayer master
show crowd onlayer master
show rin basic_awayabsent onlayer master at center
with locationskip

"Emi ist umringt von ihren Teamkameraden, die ihr alle zu ihrem Lauf gratulieren."


"Rin scheint zu warten, bis Emi bemerkt, dass wir da sind."


"Ach ja, sie kann Emi wohl kaum zuwinken."


"Allerdings bin ich mir nicht sicher, ob Rin so etwas tun würde, auch wenn sie Arme hätte."


"Es ist wohl einfach nicht ihr Stil, Aufmerksamkeit auf sich zu lenken – oder überhaupt eine Regung zu zeigen, die über Schulterzucken hinausgeht."


"Jedenfalls habe ich keine Lust zu warten, also winke ich Emi zu. Sie schaut zu uns herüber und grinst mich – oder besser uns – fröhlich an."


show bg school_track_on onlayer master at bgright
show crowd onlayer master at bgright
show rin basic_awayabsent onlayer master at tworight
with charamove

play music music_emi fadein 1.0

show emi basic_closedhappy_gym onlayer master at twoleft
with charaenter

emi "Hey, ihr seid gekommen!"


show emi excited_proud_gym onlayer master
with charachange

emi "Ich glaube, Rin schuldet mir wieder Geld, hm?"


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

rin "Als ich gesagt habe „Sieh zu, ob du einen Lorbeerzweig findest.”"


show rin basic_deadpandelight onlayer master
with charachange

rin "Hör doch zu, wenn man mit dir redet."


"Ich zucke mit den Schultern. Anscheinend färbt Rin auf mich ab."


hi "Sieht aus, als wäre es doch meine Schuld, Emi."


show emi basic_closedhappy_gym onlayer master
show rin basic_awayabsent onlayer master
with charachange

"Emi lacht Rin und mich an."


show emi basic_happy_gym onlayer master
with charachange

emi "Schon okay, Ich bin sicher, du wirst es irgendwie wiedergutmachen."


show rin basic_absent onlayer master
with charachange

hi "Äh, klar."


show rin basic_awayabsent onlayer master
show emi excited_amused_gym onlayer master
with charachange

emi "Prima! Also, wie war ich?"


show rin basic_absent onlayer master
with charachange

"Ich fange mich gerade noch rechtzeitig, bevor ich mit etwas wie „wunderschön” oder „fantastisch” herausplatze und wähle das deutlich sicherere „sehr beeindruckend.”"


show emi basic_closedgrin_gym onlayer master
with charachange

"Emi scheint mit diesem Urteil zufrieden zu sein."


"Ich erwähne nicht, wie viel beeindruckender ihre Leistung angesichts ihrer fehlenden Beine ist. Ich denke, das weiß sie auch selbst."


"Außerdem habe ich das Gefühl, dass ich ihre Leistung damit irgendwie schmälern würde."


show emi basic_grin_gym onlayer master
show rin basic_awayabsent onlayer master
with charachange

emi "Schön, das zu hören! Ich hatte schon Angst, ich hätte bei der Staffel etwas zu langsam ausgesehen, aber es lief wohl doch alles okay, hm?"


show rin basic_absent onlayer master
with charachange

hi "Um ehrlich zu sein, da war—{w=.4}{nw}"


play sound sfx_impact

show rin basic_deadpanupset onlayer master
with vpunch

"Rin tritt mir gegen das Schienbein, bevor ich meinen Satz beenden kann."


show emi basic_confused_gym onlayer master
with charachange

emi "Was sollte das denn?"


show rin basic_deadpancontemplation onlayer master
with charachange

rin "Er hat es bemerkt. Am Ende."


show emi basic_annoyed_gym onlayer master
with charachange

emi "Hmm, das ist schlecht."


show emi sad_grin_gym onlayer master
with charachange

emi "Da wird Doc wohl nachher mal draufschauen müssen."


show emi sad_grit_gym onlayer master
with Dissolve(0.2)

show emi sad_grin_gym onlayer master
with charachange

"Ihre Stimme hört sich sorglos an, als wäre das nichts besonderes, aber plötzlich bemerke ich ein leichtes Zucken in ihrem Gesicht."


"Als ob sie versuchen würde, uns zu verheimlichen, dass sie Schmerzen hat."


"Dann fällt mir auch noch auf, dass sie ziemlich flach atmet."


"Sie ist anscheinend wirklich verletzt."


"Sie muss meinen besorgten Blick bemerkt haben, weil sie auf mich zu kommt und mir freundschaftlich auf die Schulter schlägt."


show emi basic_closedgrin_gym_close onlayer master
show rin basic_deadpannormal onlayer master
with characlose

emi "Hey, du siehst ein wenig besorgt aus!"


show emi basic_grin_gym_close onlayer master
with charachange

emi "Es geht mir gut, wirklich!"


emi "Nur ziemlich müde von dem ganzen Laufen, das ist alles."


show emi excited_proud_gym_close onlayer master
with charachange

emi "Und komm schon, ein bisschen Schmerz wird mich schon nicht umbringen."


hi "Ach nein?"


show emi basic_closedgrin_gym_close onlayer master
with charachange

"Emi grinst, und einen Moment lang sieht sie aus wie während ihres Sprints – wild und unbesiegbar."


"Oder kurz, einfach wunderschön."


show emi basic_grin_gym_close onlayer master
with charachange

emi "Jedenfalls bisher nicht."


hi "Na dann. Dann sollte ich mir wohl keine Sorgen machen, hm?"


show emi basic_closedhappy_gym_close onlayer master
with charachange

emi "Natürlich nicht! Ich bin Emi Ibarazaki, das schnellste Wesen auf keinen Beinen! Ich bremse für niemanden!"


hi "Beeindruckend."


show emi basic_closedgrin_gym_close onlayer master
with charachange

"Emi kichert, dann scheint ihr etwas einzufallen."


show emi basic_grin_gym_close onlayer master
with charachange

emi "Ach ja, bevor ich es vergesse…"


emi "Rin und ich wollen nächsten Sonntag was unternehmen, um den Sieg heute zu feiern!"


show emi excited_proud_gym_close onlayer master
with charachange

emi "Du solltest mitkommen!"


show emi sad_grin_gym_close onlayer master
with charachange

emi "Normalerweise machen wir das immer am Tag darauf, aber weil das Turnier dieses Mal an einem Sonntag ist, hab ich Unterricht und Hausaufgaben und all das Zeug."


show emi basic_closedgrin_gym_close onlayer master
with charachange

emi "Und natürlich unser Training morgen früh."


hi "Ja, natürlich."


hi "Ach ja. Deine Mutter lässt dir ausrichten, dass sie stolz auf dich ist."


hi "Sie will dich heute Abend noch anrufen."


show emi basic_happy_gym_close onlayer master
with charachange

emi "Ich wusste doch, dass ich sie auf der Tribüne gesehen habe!"


show emi basic_closedhappy_gym_close onlayer master
with charachange

emi "Ich bin froh, dass sie es geschafft hat!"


show emi sad_grin_gym_close onlayer master
with charachange

emi "Früher ist immer mein Vater mit zu den Turnieren gekommen, aber Mama hat das jetzt übernommen."


show emi sad_shy_gym_close onlayer master at Transform(function=tf_lefttremble)
with Dissolve(0.1)

"Sie zittert leicht, und mir fällt auf, dass sie immer noch ganz verschwitzt ist."


"Außerdem ist inzwischen eine frische Brise aufgekommen."


"Mir ist überhaupt nicht kalt, und ich habe meine Jacke dabei, also lege ich sie ihr wortlos um die Schultern."


play sound sfx_rustling

show emi basic_shock_gym_close onlayer master at twoleft
with vpunch

with Pause(0.5)

show emi basic_grin_gym_close onlayer master
with charachange

"Emi ist etwas überrascht, aber dann grinst sie mich an."


show emi basic_closedhappy_gym_close onlayer master
with charachange

emi "Hey, danke!"


show emi sad_grin_gym_close onlayer master
with charachange

emi "Es wurde gerade wirklich etwas kühl."


hi "Ja, sah so aus."


"Gerade als ich mich frage, ob man es falsch verstehen könnte, dass ich Emi meine Jacke gegeben habe, kommt ein Junge in der Uniform der Leichtathletikmannschaft auf uns zu."


"Teamkamerad" "Hey, Emi! Du verpasst noch die Preisverleihung!"


show emi basic_closedgrin_gym_close onlayer master
with charachange

emi "Ach ja, danke!"


show emi basic_grin_gym onlayer master
show rin basic_awayabsent onlayer master
with charadistant

"Sie wendet sich Rin und mir zu."


emi "Ihr müsst dazu nicht hier bleiben. Das dauert immer ewig."


show emi basic_closedgrin_gym onlayer master
with charachange

emi "Außerdem solltest du dich an deine Hausaufgaben machen, wenn du nicht zu lange aufbleiben willst, Hisao."


show emi excited_proud_gym onlayer master
with charachange

emi "Nicht vergessen! Morgen früh Training!"


show rin basic_absent onlayer master
with charachange

hi "Wie könnte ich?"


show emi basic_closedhappy_gym onlayer master
show rin basic_awayabsent onlayer master
with charachange

emi "Stimmt. Immerhin verbringst du Zeit mit {b}mir{/b}."


play sound sfx_emirunning

hide emi onlayer master
with easeoutleft

stop sound fadeout 3.0

show bg school_track_on onlayer master at center
show crowd onlayer master at center
show rin basic_awayabsent onlayer master at center
with charamove

"Damit winkt sie uns kurz und rennt hinüber zur Preisverleihung, um ihre Medaillen entgegenzunehmen – oder was auch immer heutzutage als Medaille durchgeht."


scene bg school_courtyard onlayer master
show crowd onlayer master
show rin relaxed_nonchalant onlayer master at center
with locationskip

stop music fadeout 7.0

"Rin und ich entfernen uns vom Sportplatz. Auf dem Weg zu den Wohnheimen ist Rin immer noch tief in ihre Gedanken versunken."


"Als ich mich von ihr verabschiede, fängt sie an zu sprechen."


show rin basic_deadpan onlayer master
with charachange

rin "Ich denke, du wirst diese Jacke wahrscheinlich nicht wiederkriegen."


hi "Ich bin sicher, dass ich sie früher oder später zurückkriege."


show rin basic_deadpannormal onlayer master
with charachange

rin "Interessant. Du nimmst es, wie es kommt, was?"


show rin basic_deadpandelight onlayer master
with charachange

rin "Genau wie Emi."


hide rin onlayer master
with charaexit

"Mit dieser seltsamen Bemerkung dreht sie sich um und betritt ihr Wohnheim."


"Ehrlich, war das wirklich so eine große Sache?"


"Emi war kalt, und wenn ich mich nicht irre, hatte sie Schmerzen."


"Zumindest eines dieser Probleme konnte ich lösen, also war das doch selbstverständlich."


"Na ja, wenn ich Pech habe, kriege ich die Jacke wirklich nicht zurück."


"Rin hat vermutlich Recht."


"Dennoch mache ich mir über diese Sache nicht wirklich Sorgen."


"Immerhin ist es in letzter Zeit immer wärmer geworden."


"Ich brauche keine Jacke."


"Seltsam. Ich glaube, früher bin ich immer etwas verantwortungsvoller mit meinen Sachen umgegangen."


"„Genau wie Emi,” hm?"


"Vielleicht ist das ja nicht wirklich was Schlechtes."


stop ambient fadeout 2.0

scene black onlayer master
with dissolve


label de_E9:

scene bg school_nurseoffice onlayer master
show nurse concern onlayer master at center
with locationchange

nk "Du hast doch nicht etwa vergessen, deine Medizin zu nehmen, oder?"


play music music_nurse fadein 0.5

nk "Ich höre da ein leises Herzgeräusch."


nk "Du solltest dich die nächsten Tage etwas zurückhalten."


"Docs Worte schmerzen mehr als die Erschöpfung nach meinem morgendlichen Training es je könnte."


"Mich ein paar Tage zurückhalten?"


"Ich wusste, ich hätte nichts sagen sollen."


"Ich starre zu Boden und fühle mich wie ein Vollidiot."


"Natürlich habe ich vergessen, meine Medizin zu nehmen."


"Ich habe mich die letzten Tage so beeilt, um vor Emi auf dem Sportplatz zu sein."


"Nach dem Turnier vor ein paar Tagen war ich… inspiriert."


"Also bin ich immer noch Aufwärmrunden gelaufen, bevor Emi aufgekreuzt ist."


"Aber dann hatte ich heute, als wir zusammen gelaufen sind, leichte Brustschmerzen."


"Es war nur ganz leicht, und es hat nur eine Sekunde gedauert, deshalb habe ich es Doc gegenüber erwähnt."


hi "Ehrlich, es war nicht so schlimm."


hi "Ich meine… Ich konnte ganz normal weiterlaufen und meine Runde beenden, also kann es gar nicht so schlimm gewesen sein…"


"Warum fühlt sich das an wie eine Ausrede?"


"Noch wichtiger: Warum habe ich das Gefühl, mich rechtfertigen zu müssen, weil ich trotz der Schmerzen weitergelaufen bin?"


"Es läuft wohl darauf hinaus, dass ich nicht wollte, dass Emi sich Sorgen macht. Aber sie sah trotzdem besorgt aus."


"Ich weiß nicht woran sie gemerkt hat, dass etwas nicht in Ordnung war, aber sie behauptet, ich wäre etwas gestolpert."


"Sie hat darauf bestanden, dass ich das Doc erzähle, und nun habe ich ein schlechtes Gewissen, weil ich ihr überhaupt Sorgen bereitet habe."


"Doc schüttelt entgeistert den Kopf, während Emi vor dem Zimmer auf und ab läuft."


nk "Hisao, ich weiß, es ist schwer für dich, in deine neue Routine hineinzukommen, aber wenn du nicht große Probleme kriegen willst, solltest du dir mehr Mühe geben."


nk "Du kannst es dir nicht leisten, deine Tabletten zu vergessen, und du darfst dir nicht zu viel zumuten."


hi "Aber wie soll ich denn besser werden, wenn ich mich nicht anstrenge?"


"Ich habe keinen Schimmer, wo das herkam."


"Doc scheint eine Ahnung zu haben."


show nurse fabulous onlayer master
with charachange

nk "Hmm, wo hab ich das nur schon mal gehört?"


show nurse grin onlayer master
with charachange

"Er lacht und klopft mir auf die Schulter."


nk "Ha! Ich glaube, sie färbt auf dich ab."


show nurse concern onlayer master
with charachange

"Sein Gesichtsausdruck ändert sich erneut, und er ist schlagartig wieder ernst."


nk "Schau mal, ich sage nicht, dass du dich nicht anstrengen sollst."


nk "Aber das heißt nicht, dass du deine Medikamente nicht nehmen sollst, und es heißt nicht, dass du nicht aufhören solltest, wenn dein Herz dir Probleme macht."


nk "Ich würde es vorziehen, wenn es keine Todesfälle gäbe, solange ich hier arbeite."


show nurse neutral onlayer master
with charachange

nk "Ein hehres Ziel, um ehrlich zu sein, aber ich liebe Herausforderungen."


"Ich gebe es nicht gerne zu, aber er hat Recht."


"Ich muss an meine Medikamente denken."


hi "Sie haben Recht. Tut mir leid, dass ich Ihnen Sorgen gemacht habe."


show nurse fabulous onlayer master
with charachange

nk "Wer hat sich denn Sorgen gemacht? Du bist doch ein cleverer Junge, oder?"


show nurse neutral onlayer master
with charachange

nk "Ich weiß, dass du verantwortungsbewusst sein kannst, Hisao. In einer Situation wie deiner muss man schnell lernen, verantwortungsbewusst zu sein."


hi "Ich weiß, ich weiß."


"Ein verschlagener Ausdruck schleicht sich auf sein Gesicht."


show nurse fabulous onlayer master
with charachange

nk "Ich nehme an, deine morgendlichen Trainings mit Emi beginnen dir Spaß zu machen, hm?"


hi "Ja, sie haben mir wirklich geholfen."


hi "Ich meine… Bis heute habe ich mich viel gesünder gefühlt."


hi "Außerdem ist es wirklich beeindruckend, Emi laufen zu sehen. Haben Sie sie beim Turnier gesehen?"


hi "Sie war unglaublich!"


show nurse grin onlayer master
with charachange

"Doc nickt und grinst die ganze Zeit."


nk "Das war sie, Hisao. Ich habe die ersten paar Rennen gesehen, dann hatte ich was zu erledigen, aber sie hat mir alles erzählt."


show nurse fabulous onlayer master
with charachange

nk "Übrigens, nett von dir, ihr deine Jacke zu leihen."


hi "Hm? Ach ja, das war doch selbstverständlich."


"Ich hatte das ehrlich gesagt ganz vergessen. Ich habe sie immer noch nicht zurück."


show nurse neutral onlayer master
with charachange

"Doc grinst, als hätte er gerade einen Scherz gemacht."


nk "Für dich vielleicht, aber Emi wusste das wirklich zu schätzen."


nk "Und ich weiß, dass sie dir sehr dankbar ist, dass du morgens mit ihr läufst."


"Das erwischt mich jetzt etwas auf dem falschen Fuß. Klar, sie hat erwähnt, dass es mit einem Partner einfacher ist, sich an einen Plan zu halten, aber ich hätte jetzt nicht gedacht, dass ich ihr damit einen Gefallen tue."


hi "Ich dachte, sie tut mir einen Gefallen, indem sie mir hilft, die ärztlichen Anweisungen zu befolgen."


nk "Sie gibt sich mehr Mühe, wenn du dabei bist."


nk "Wenn jemand mit ihr zusammen läuft, strengt sie sich mehr an."


nk "Und wenn du dabei bist, strengt sie sich noch mehr an, weil… Na ja, weil du es bist."


hi "Was zum Teufel soll dass heißen?"


show nurse grin onlayer master
with charachange

nk "Aha, das wüsstest du wohl gerne, nicht wahr?"


"Er lacht wie ein größenwahnsinniger Bond-Schurke."


show nurse neutral onlayer master
with charachange

nk "Nein, im Ernst – einfach, weil du ihr Freund bist."


nk "Wenn Rin mit ihr laufen würde, würde sie sich sicher genauso anstrengen."


nk "Na ja, wahrscheinlich."


nk "Aber darum geht es nicht."


nk "Es geht darum, dass du ihr hilfst, auch wenn dir das nicht bewusst ist."


show nurse fabulous onlayer master
with charachange

nk "Und dafür ist sie dir dankbar, auch wenn sie es nie sagt."


hi "Wie meinen Sie das – „auch wenn sie es nie sagt?”"


show nurse neutral onlayer master
with charachange

nk "Emi redet nicht sehr viel, aber sie und ich, wir kennen uns nun schon lange genug, dass ich meistens weiß, was sie auf dem Herzen hat."


"Ich gebe zu, dass ich keine Ahnung habe, wovon er redet."


"Emi ist eigentlich immer ziemlich gesprächig."


hi "Aha."


"Doc bemerkt plötzlich, dass er abschweift und verstummt. Er sieht ein wenig verlegen aus."


show nurse fabulous onlayer master
with charachange

nk "Na ja, jedenfalls musst du nicht mit deinem Training aufhören."


show nurse neutral onlayer master
with charachange

nk "Geh einfach ein paar Tage anstatt zu rennen. Bis sich alles wieder beruhigt hat."


show nurse concern onlayer master
with charachange

nk "Und nimm deine verdammte Medizin!"


scene bg school_nursehall onlayer master
with locationchange

stop music fadeout 0.3
play sound sfx_impact

show emi basic_confused_gym_close onlayer master
with vpunch

"Ich lache, als ich sein Büro verlasse, und laufe geradewegs gegen Emi."


show emi basic_confused_gym onlayer master
with charadistant

hi "Ups, tut mir leid."


show emi basic_hes_gym onlayer master
with charachange

emi "Bist du in Ordnung? Was hat Doc gesagt?"


emi "Musst du ins Krankenhaus?"


show emi basic_shock_gym onlayer master
with charachange

emi "Oh Gott, es war meine Schuld, nicht wahr?"


show emi basic_closedsweat_gym onlayer master
with charachange

emi "Ich habe zu viel von dir verlangt, oder?"


show emi excited_sad_gym onlayer master
with charachange

emi "Ich bin ein schrecklicher Mensch!"


"Die Worte kommen wie ein Schwall aus ihrem Mund. Sie ist ganz aufgeregt."


"Ich hätte ehrlich gesagt nicht gedacht, dass sie sich so viele Sorgen um mich macht."


"Ich muss sie irgendwie beruhigen… aber wie zum Teufel soll ich das anstellen?"


"Ich tue das einzige, was mir in diesem Augenblick einfällt."


show emi basic_shock_gym_close onlayer master
with characlose

play music music_serene fadein 6.0

"Ich nehme sie in den Arm. Sie versteift sich etwas, also streiche ich ihr beruhigend über den Kopf – zumindest hoffe ich, dass es beruhigend wirkt."


hi "Hey, ganz ruhig!"


hi "Es geht mir gut, okay? Keine Sorge."


show emi basic_hes_gym_close onlayer master
with charachange

"Ich kann spüren, wie sich Emi entspannt, während ich ihr weiterhin versichere, dass es mir gut geht."


"Sie legt ihre Arme um mich, als ob sie ganz sicher gehen will, dass ich nicht plötzlich tot umfalle."


"Der Duft ihrer Haare… Sie riechen nach Schweiß, oder wie Adrenalin riechen sollte. Es ist der Geruch von Aktivität."


"Und ein Hauch von Erdbeere. Von ihrem Shampoo, nehme ich an."


hi "Ich muss nur daran denken, meine Medikamente zu nehmen, das ist alles."


hi "Mach dir keine Sorgen, es ist nicht deine Schuld."


show emi sad_depressed_gym_close onlayer master
with charachange

emi "Bist du sicher?"


"Ihre Stimme klingt dumpf, aber das liegt hauptsächlich daran, dass ihr Gesicht momentan an meine Brust gepresst ist."


hi "Ja, ich bin sicher. Ich muss nur die nächsten paar Tage etwas kürzer treten."


"Mir wird plötzlich bewusst, wie nahe wir einander sind."


"Mir wird außerdem bewusst, wie gut sich diese Nähe anfühlt."


"Ich kann spüren, wie sich Emis Herzschlag beruhigt, und ich muss mich beherrschen, um nicht mein Kinn auf ihren Kopf zu legen."


show emi sad_grin_gym_close onlayer master
with charachange

emi "Gott sei Dank!"


emi "Ich habe mir wirklich Sorgen gemacht, Hisao."


stop music fadeout 1.5

show nurse concern behind emi onlayer master:
    center
    xpos 0.0 xanchor 0.3
    easein 0.5 xanchor 0.2
with Dissolve(0.5)

nk "Emi, kommst du bald mal rein?"


show nurse grin onlayer master
with charachange

nk "… Oh, tut mir leid. Störe ich?"


show emi basic_shock_gym onlayer master
with vpunch

"Wir springen auseinander, als ob der jeweils andere gerade Feuer gefangen hätte."


show emi basic_hes_gym onlayer master
with charachange

"Emi streicht nervös ihr Haar zurück und lacht."


play music music_emi fadein 1.0

emi "Natürlich nicht!"


show emi sad_shy_gym onlayer master
show nurse fabulous onlayer master
with charachange

emi "Wir äh… sehen uns dann später, okay?"


show emi basic_closedgrin_gym onlayer master
with charachange

emi "Oh, und Hisao?"


hi "Hmm?"


show emi basic_annoyed_gym_close onlayer master
with characlose

with hpunch

emi "Nimm deine verdammte Medizin!"


"Den letzten Satz unterstreicht sie mit einem Hieb gegen meine Schulter."


hi "Ja, schon gut, ich werde dran denken."


hi "Bis später."


show nurse grin onlayer master
with charachange

"Doc grinst wieder, als ob er über einen Witz lacht, den ich nicht verstanden habe, und winkt mir zum Abschied zu, während ich mich mit rotem Gesicht auf den Weg zurück in mein Zimmer mache."


stop music fadeout 8.0

scene bg school_dormhisao onlayer master
with locationskip

"Ich brauche eine Dusche."


"Eine Kalte – in Anbetracht der Gedanken, die mir durch den Kopf schwirren."


"Sie war so weich…"


"Meine Pillen warten auf mich, als ich mein Zimmer betrete."


"Ich schlucke sie, ohne lange darüber nachzudenken."


"Ich weiß nicht, warum ich nicht selbst daran gedacht habe, sie nach meinem Training zu nehmen. Irgendwie dachte ich wohl, nach dem Aufstehen oder gar nicht."


"Aber nein, man muss sie nur einmal am Tag nehmen. Die genaue Zeit ist egal."


"Meine Gedanken driften wieder zu der Umarmung im Flur."


"Es ist seltsam, normalerweise sollte man denken, dass jemand nach dem Training stinken würde, aber irgendwie war Emis Geruch… passend. Diese Schweißnote passte irgendwie zu ihr."


"Ich brauche wirklich eine Dusche."


scene black onlayer master
with dissolve

$ suppress_window_after_timeskip = True


label de_E10:

window hide None

scene bg school_roof onlayer master
with locationchange

nvl clear

nvl show dissolve

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0

n "\nSchon seltsam, dass es für mich inzwischen so normal ist, in der Mittagspause aufs Dach zu gehen."


n "An meiner alten Schule hätte ich so etwas nie gemacht."


n "Damals habe ich lieber allein gegessen… Nein, das stimmt nicht ganz. Obwohl ich lieber allein war, habe ich gerne andere Leute beobachtet."


n "Ich dachte immer, das wäre für jemanden wie mich normal, aber ich habe mich wohl geirrt."


n "Allerdings dachte ich damals auch, ich hätte ein ganz normales Herz. So kann man sich irren."


n "Ich kenne mich wohl selbst nicht allzu gut."


n "Jetzt bin ich also auf dem Dach, um mit anderen Leuten zu Mittag zu essen."


n "Und sie sind beide Mädchen, was mich noch mehr wundert."


n "Seltsamerweise fühle ich mich Emi und Rin näher als allen Leuten an meiner alten Schule."


n "Irgendwie habe ich das Gefühl, dass sie mich wenigstens besuchen würden, wenn ich wieder ins Krankenhaus käme."


$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

nvl hide dissolve

nvl clear

window show

"Ich konzentriere mich wieder auf die Aussicht von hier oben und vertreibe diese Gedanken aus meinem Kopf."


"Eine leichte Brise weht, und die Sonne steht hoch am Himmel."


"Der Himmel selbst ist tiefblau, und es ist kaum eine Wolke zu sehen. Es ist angenehm warm geworden, und als ich mich hinsetze, um auf meine Freunde zu warten, schließe ich die Augen und genieße das Gefühl der Sonnenstrahlen auf meiner Haut."


$ renpy.music.set_volume(0.1, 2.0, channel="ambient")

window hide

scene black onlayer master
with shuteye

with Pause(4.0)

window show

"Von weit her nehme ich Stimmen wahr."


emi "… scheint eingeschlafen zu sein, Rin."


rin "Vielleicht tut er nur so, um uns in Sicherheit zu wiegen."


emi "Warum sollte er das tun?"


rin "Keine Ahnung."


emi "Trotzdem hast du Recht."


emi "Wir sollten ihn treten oder so was, um sicherzugehen, dass er wirklich schläft."


stop music fadeout 1.0

hi "Hä? Was?"


$ renpy.music.set_volume(0.5, 5.0, channel="ambient")

scene bg school_roof onlayer master
show rin basic_absent onlayer master at tworight
show emi excited_happy_close onlayer master at twoleft
with openeye

play music music_ease fadein 3.0

"Emi ragt vor mir auf, wie das nur ein zierliches Mädchen wie sie kann, und starrt mich aufmerksam an."


show emi basic_closedgrin_close onlayer master
with charachange

emi "Oh, du bist wach. Dann brauchen wir dich also nicht zu treten."


show rin basic_deadpan onlayer master
with charachange

rin "War das ein Teil deines Plans?"


hi "Wovon redest du?"



show emi basic_grin_close onlayer master
with charachange

"Emi zuckt mit den Schultern; ihre beiden Zöpfe wackeln bei der Bewegung mit."


show emi basic_closedhappy_close onlayer master
with charachange

emi "Das weiß ich auch nicht genau."


show emi sad_grin_close onlayer master
with charachange

emi "Du musst ziemlich müde sein, um hier oben einzuschlafen."


show emi basic_closedgrin_close onlayer master
with charachange

emi "Obwohl es anscheinend ziemlich gemütlich ist."


show emi basic_closedgrin_close onlayer master:
    yanchor 0.9
with ease
with vpunch

"Sie lässt sich neben mir auf die Bank fallen und fängt an zu essen."


show rin basic_absent onlayer master
with charachange

show rin basic_absent onlayer master:
    yanchor 0.77
with charamove

"Rin sitzt uns gegenüber – das macht mir aber die Tatsache, dass Emi neben mir sitzt, nur noch deutlicher bewusst."


"Wenn ich es nicht besser wüsste, könnte ich schwören, dass Rin das absichtlich getan hat."


"Ich konzentriere mich auf mein Essen, und versuche den Großteil des Gespräches zwischen Rin und Emi auszublenden."


"Trotz meiner Bemühungen ertappe ich mich aber dabei, dass ich immer zu Emi hinüber schiele, wenn sie spricht."


show emi basic_grin_close onlayer master
with charachange

"Mir fällt auf, wie sie den Mund spitzt, wenn sie über etwas nachdenkt; wie sie die Augen leicht zusammenkneift, als würde ihr das beim Denken helfen."


show rin basic_deadpan onlayer master
with charachange

show emi basic_grin_close onlayer master at Transform(function=tf_leftrock)
with None

show emi basic_closedhappy_close onlayer master at Transform(function=tf_leftrock)
with charachange

"Rin sagt etwas, das Emi zum Lachen bringt, und – vielleicht zum ersten Mal – fällt mir auf, wie sie mit ihrem gesamten Körper lacht, wie sie vor und zurück schaukelt, den Kopf zurück wirft und fast von der Bank fällt."


"Ich sehe bestimmt extrem aufdringlich aus."


show emi basic_confused_close onlayer master
with charachange

"In diesem Moment bemerke ich, dass Emi mich anschaut. Ihre Stimme ist etwas nach oben gegangen, also hat sie mir wahrscheinlich gerade eine Frage gestellt."


hi "Hmm? Entschuldige, ich war gerade etwas abwesend."


show rin basic_deadpannormal onlayer master
show emi basic_annoyed_close onlayer master
with charachange

"Emi rollte ihre Augen, während bei Rin eine leicht hochgezogene Augenbraue das einzige Zeichen ist, dass sie überhaupt aufgepasst hat."


emi "Ich habe gefragt, ob ihr in eurer Klasse auch eine Berufsumfrage bekommen habt."


show emi basic_grin_close onlayer master
with charachange

emi "Du weißt schon, so was wie „Was willst du nach der Schule machen?”"


hi "Ich glaube nicht… Vielleicht kriegen wir sie morgen."


show emi excited_happy_close onlayer master
with charachange

emi "Was würdest du reinschreiben?"


"Das ist eine sehr gute Frage."


"Ich bin immer davon ausgegangen, dass ich nach der Schule studieren werde, aber ich habe keine Ahnung, was genau."


"Und mit der Herzattacke und allem habe ich mich eher darauf konzentriert, jeden Tag zu nehmen wie er kommt, anstatt langfristige Pläne zu machen."


"Ich denke, ich kann langsam wieder anfangen, meine Zukunft zu planen."


"Ich hatte immer gerne zumindest eine grobe Vorstellung von meiner Zukunft, also sollte ich mir mal Gedanken machen."


"Natürlich ändert das nichts daran – jetzt im Moment habe ich absolut…"


hi "… Keine Ahnung."


hi "Ich dachte immer, in der Uni wird mir schon was einfallen. Das, oder ich werde einfach Salaryman. Das machen ja viele."



"Aber will ich das auch wirklich? Das ist eine gute Frage."


"Ich denke, es gibt nichts, was ich unbedingt machen will."


show emi basic_closedhappy_close onlayer master
with charachange

emi "Hört sich nicht so an, als wärst du davon sehr begeistert, oder?"


show emi basic_closedhappy_close onlayer master at Transform(function=tf_leftrock)
with None

"Sie lacht, als sie das sagt, und ihr Lachen fesselt mich wieder."


"Es ist einfach so… mädchenhaft. Hoch und kichernd, wie ein… na ja, entschuldigung für das Klischee – wie ein Glockenspiel."


"Es blubbert nur so aus ihr heraus; es fängt in ihrem Bauch an und steigt ihren Hals empor."


"Ich kann nicht anders – ich muss einfach mitlachen. Es ist ansteckend."


hi "Ja, ich denke, mit der Salaryman-Idee bin ich nicht wirklich glücklich."


hi "Aber um ehrlich zu sein, habe ich mir in letzter Zeit nicht viele Gedanken über die Zukunft gemacht."


hi "Ich glaube, zur Zeit lebe ich mehr von einem Tag in den anderen."


show emi basic_grin_close onlayer master
with charachange

"Emi denkt darüber einen Moment nach und grinst dann."


emi "Das ist eine sehr gute Idee, Hisao!"


show emi excited_proud_close onlayer master
with charachange

emi "Ich habe einfach „Pirat” hingeschrieben."


"Einen Augenblick bin ich wie vom Donner gerührt, dann fange ich an zu lachen."


"Ich beruhige mich und schaffe es, eine Frage herauszubringen."


hi "Das ist… Das ist nicht wirklich dein Ernst, oder?"


show emi sad_annoyed_close onlayer master
with charachange

"Emi tut beleidigt."


emi "Na ja, ich hab doch schon die passenden Beine, also dachte ich mir…"


show rin basic_amused onlayer master
with charachange

"Sogar Rin scheint das lustig zu finden."


show emi basic_annoyed_close onlayer master
with charachange

emi "Wartet nur ab, ich werde der Schrecken der Sieben Meere sein!"


emi "Ich werd's euch allen zeigen!"


show emi basic_closedhappy_close onlayer master
with charachange

emi "Ich habe auch schon meine Piratensprache geübt!"


show emi basic_closedhappy_close onlayer master at offscreenleft
with ease

hide emi onlayer master
with None

show emi basic_closedhappy behind rin at offscreenleft onlayer master
with None

show emi basic_annoyed onlayer master at left
with ease

"Sie springt plötzlich auf und fängt an, auf dem Dach auf und ab zu stolzieren und Befehle zu brüllen."


show emi basic_annoyed onlayer master at center
with ease

emi "Harr, ihr Halunken, gebt ihnen eine Breitseite mit den Neunpfündern!"


show emi basic_annoyed onlayer master at twoleft
with ease

emi "Wir machen Kleinholz aus ihnen!"




show rin basic_deadpanamused onlayer master
with charachange

rin "Weißt du überhaupt, was Neunpfünder sind?"


show emi basic_confused onlayer master
with charachange

"Rins unerwartete Frage lässt Emi abrupt innehalten."


show emi sad_shy onlayer master
with charachange

emi "Nicht wirklich."


show emi basic_closedgrin onlayer master
with charachange

emi "Aber es kommt nur darauf an, überzeugend zu klingen!"


play sound sfx_warningbell

show emi basic_hes onlayer master
show rin basic_awayabsent onlayer master
with charachange

"Das Läuten der Schulglocke hält sie davon ab, ihr Argument noch weiter fortzuführen."


hide emi onlayer master
with easeoutleft

"Emi stürmt sofort davon und lässt Rin und mich allein auf dem Dach zurück."


show rin basic_awayabsent onlayer master:
    xpos 0.5
show bg school_roof onlayer master at bgleft
with charamove

show rin basic_deadpancontemplation onlayer master
with charachange

"Rin starrt mich einen Moment lang intensiv an."


hi "Ist… Ist irgendwas?"


show rin basic_lucid onlayer master
with charachange

"Rin überlegt einen Augenblick angestrengt."


"Nach einer längeren Pause schüttelt sie den Kopf."


show rin basic_deadpannormal onlayer master
with charachange

rin "Nö."


hi "Oh, äh…"


extend " Warum starrst du mich dann so an?"


show rin basic_awayabsent onlayer master
with charachange

"Rin schüttelt noch einmal den Kopf."


rin "Nö, ich versteh's nicht."


hi "Was verstehst du nicht?"


show rin basic_deadpan onlayer master
with charachange

rin "Das mit dem Anstarren. Ihr beiden scheint es zu verstehen, aber ich nicht."


"Na toll. Sie hat gesehen, wie ich Emi angestarrt habe. Nun denkt sie wahrscheinlich, ich wäre pervers oder so was."


"Obwohl… Wahrscheinlich nicht. Wir reden hier immerhin über Rin."


"Trotzdem habe ich das Bedürfnis, mich zu verteidigen."


hi "Ich habe nicht gestarrt, ich war nur müde."


show rin basic_deadpancontemplation onlayer master
with charachange

"Das bringt Rin sogar ein wenig zum Kichern, aber sie sagt nichts."


hi "Nein, wirklich! Ich war nur… abgelenkt, das ist alles."


show rin basic_lucid onlayer master
with charachange

rin "Mmm."


stop music fadeout 4.0

"Froh, diese Unterhaltung beenden zu können, mache ich mich auf den Weg zurück zum Unterricht."


stop ambient fadeout 2.0

scene bg school_scienceroom onlayer master
show misha cross_grin onlayer master at twoleft
show shizu behind_blank onlayer master at tworight
with locationskip

"Ich werde von dem schrecklichen Duo Shizune und Misha begrüßt. Sie sehen aus, als hätten sie etwas mit mir vor."


"Na ja, Shizune zumindest."


"Misha sieht einfach so aus, als würde sie jeden Moment anfangen zu lachen."


play music music_shizune fadein 3.0

show misha perky_smile onlayer master
with charachange

mi "Wieder mal auf dem Dach gewesen, Hicchan?"


show misha hips_frown onlayer master
with charachange

mi "Du weißt, dass das gefährlich ist, oder~?"


show shizu basic_angry onlayer master
with charachange

shi "…"


show misha sign_smile onlayer master
with charachange

mi "Stimmt~!"


show misha hips_smile onlayer master
with charachange

mi "Die Schule ist nicht verantwortlich für irgendwelche Verletzungen, die ihr euch dort oben zuziehen könntet!"


show misha cross_frown onlayer master
with charachange

mi "Außerdem könnten wir melden, dass ihr gegen die Regeln verstoßt~!"


show misha cross_frown_close onlayer master
with characlose

"Misha beugt sich zu mir herüber und flüstert verschwörerisch."


show misha sign_smile_close onlayer master
show shizu behind_smile onlayer master
with charachange

mi "Aber das werden wir nicht, Hicchan!"


show misha hips_grin_close onlayer master
with charachange

mi "Ihr drei seid zu süß zusammen~!"


show misha cross_laugh onlayer master
with charadistant

"Sie richtet sich wieder auf, und lacht, weil ich plötzlich rot anlaufe."


mi "Wahahaha~!"


show misha cross_grin onlayer master
with charachange

mi "Man kann dich so leicht ärgern, Hicchan~!"


hi "Hey, komm schon."


hi "Ich bin immer noch neu hier… irgendwie."


hi "Ist es nicht gemein, so auf dem Neuen rumzuhacken?"


show misha hips_grin onlayer master
with charachange

mi "Nö~!"


show misha sign_smile onlayer master
with charachange

mi "Das soll dir helfen, dich an deine neue Umgebung anzupassen!"


hi "Ah, verstehe."


hi "Na ja… Müsst ihr euch dabei wirklich so viel Mühe geben?"


show misha hips_grin onlayer master
with charachange

mi "Jepp!"


show misha hips_smile onlayer master
with charachange

mi "Ah! Davon abgesehen, Hicchan, wir haben dich heute Morgen gesucht, aber du warst nicht auf deinem Zimmer!"


hi "Natürlich nicht. Ich war entweder beim Training oder schön pünktlich hier in der Klasse."


hi "Anders als ihr."


show shizu basic_angry onlayer master
show misha hips_frown onlayer master
with charachange

"Shizune sieht verärgert aus, und einen Herzschlag später Misha ebenfalls – zumindest versucht sie, verärgert auszusehen."


mi "Das lag an unserer Arbeit für den Schülerrat! Du solltest dankbar sein, dass wir so hart für dich arbeiten~!"


hi "Oh, das bin ich, das bin ich. Also, wofür braucht ihr mich?"


"Ich hoffe mal, dass das nicht ein weiterer Versuch ist, mich für ihre Drecksarbeit einzuspannen."


show misha sign_smile onlayer master
with charachange

mi "Wir wollten dir etwas geben~, aber weil du nicht da warst, haben wir es in deinem Zimmer gelassen!"


hi "Etwas? Was denn genau?"


show misha hips_grin onlayer master
with charachange

mi "Oh, das wirst du schon sehen, wenn du zurückkommst, Hicchan~! Wahahaha~!"


hide misha onlayer master
hide shizu onlayer master
with charaexit

"Unsere Unterhaltung endet, als Mutou den Raum betritt und wir zu unseren Plätzen gehen."


stop music fadeout 10.0

"Erst als ich an meinem Tisch sitze und der Lehrer angefangen hat, über irgendetwas zu reden, fällt mir etwas Seltsames ein."


"Wie hat Rin das gemeint, „Ihr beiden scheint es zu verstehen?”"


"Hat Emi auch auf irgendetwas gestarrt?"


"Einen Moment lang überlege ich, ob Emi mich vielleicht genauso angestarrt hat wie ich sie."


"Das ist natürlich lächerlich."


"Trotzdem kann ich nicht leugnen, dass ich nichts dagegen hätte, wenn es so wäre…"


"Aber es ist besser, nicht darüber nachzudenken. Kein Grund, mir unnötige Hoffnungen zu machen."


"Wann habe ich überhaupt angefangen, mir solche Hoffnungen zu machen?"


"Ich schüttele meinen Kopf, um diese Gedanken zu vertreiben, und konzentriere mich auf den Unterricht."


scene bg school_dormhallway onlayer master
with shorttimeskip

"Nach dem Unterricht mache ich mich auf den Weg zu meinem Zimmer. Mutou hat uns heute eine Menge Hausaufgaben gegeben."


play sound sfx_impact2

show kenji tsun onlayer master at left
with vpunch

"Aber bevor ich meine Tür öffnen kann, werde ich plötzlich von Kenji abgefangen, der gerade mit einem Stapel Papier aus seinem Zimmer stürzt."


ke "Hey, wir müssen reden."


play music music_kenji fadein 1.0

ke "Deine Stelldicheins auf dem Dach, Mann."


ke "Die müssen aufhören."


hi "Was?"


ke "Du bist immer auf dem Dach mit diesen beiden Amputierten!"


ke "Das sind Frauen, Mann! Es wird dich noch umbringen, wenn du dich weiter mit ihnen abgibst!"


hi "Ich kann dir nicht folgen."


show kenji neutral onlayer master
with charachange

"Kenji seufzt und rückt seine Brille zurecht, bevor er einen Versuch startet, mir seine Gedankengänge näherzubringen."


ke "Schau mal, wir sind Freunde, also sage ich dir das zu deinem eigenen Besten."


ke "Aber wenn ich vorhätte, jemanden umzubringen, würde ich ihn von einem Dach werfen und dafür sorgen, dass es wie ein Unfall aussieht."


show kenji tsun onlayer master
with charachange

ke "Und wenn ich auf diese Idee gekommen bin, kannst du dir sicher sein, dass sie auch darauf gekommen sind."


ke "Sie sind schlau – fast so schlau wie ich."


hi "Verstehe."


show kenji happy onlayer master
with charachange

ke "Gut!"


ke "Ich bin froh, dass wir darüber gesprochen haben."


show kenji neutral onlayer master
with charachange

ke "Leih mir 500 Yen."


hi "… Wie bitte?"


show kenji tsun onlayer master
with charachange

ke "Ich muss mir was zu Trinken holen, Mann!"


ke "Ich bin schon den ganzen Tag hier drinnen, und das Leitungswasser ist nicht sicher, wie du bestimmt weißt."


ke "Also brauche ich was aus der Dose, verstehst du? Aber dazu brauche ich 500 Yen."


show kenji neutral onlayer master
with charachange

ke "Und da ich dir mit meinem guten Rat gerade das Leben gerettet habe, kannst du mir wenigstens 500 Yen geben."


"Wenn er dafür verschwindet, sind 500 Yen ein Schnäppchen."


stop music fadeout 6.0

show kenji happy onlayer master
with charachange

show kenji happy onlayer master:
    easeout 0.5 alpha 0.0 xanchor 0.2
with None

"Ich gebe Kenji das Geld. Er nickt mir dankbar zu und rennt dann den Gang hinunter – nicht ohne vorher seine Tür abzuschließen."


"Was für ein anstrengender Kerl. Ich sollte besser gehen, bevor er es sich anders überlegt."


scene bg school_dormhisao onlayer master
with locationchange

"Hm?"


"Als ich die Tür schließe, trete ich mit meiner Ferse auf etwas, was auf dem Boden liegt."


"Es ist ein grellbuntes Stück Papier. Das muss das „etwas” sein, das Misha vorhin erwähnt hat."


"Wahrscheinlich ein Flugblatt vom Schülerrat, das sie unter der Tür durchgeschoben hat."


"Aber als ich es aufhebe, stelle ich fest, dass ich mich geirrt habe."


"Irgendjemand hat mir doch wirklich einen altmodischen, handgeschriebenen Papierbrief geschrieben."


"Wer macht denn so was heutzutage noch? Aber so ungewöhnlich es auch ist, das ist definitiv ein Brief in meiner Hand."


"Ich wollte eigentlich meine Hausaufgaben fertig machen, etwas zu Abend essen und dann früh zu Bett gehen, um morgen früh fit fürs Training zu sein."


"Aber dieser Brief macht mich natürlich neugierig. Ich setze mich an meinen Schreibtisch, um ihn mir genauer anzusehen."


scene ev hisao_letter_closed onlayer master:
    xalign 0.5 yalign 0.5 zoom 1.1 subpixel True
    acdc_warp 10.0 zoom 1.0
with locationchange

play music music_rain fadein 5.0

"Das ist das erste Mal, dass ich Post kriege, seit ich hier an der Yamaku bin, also wäre es auch etwas Besonderes, wenn es nicht so etwas Ungewöhnliches wie ein handgeschriebener Brief wäre."


"Was mich noch unruhiger macht, ist der Name des Absenders, der deutlich auf der Rückseite des Umschlags steht."


"„Iwanako.”"


"Ich habe keine Ahnung, warum sie mir schreiben sollte. Ich hatte keinen Kontakt mit irgendjemandem aus meiner alten Schule, seit ich gewechselt bin, und Iwanako ist die letzte Person, von der ich einen Brief erwarten würde."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\n\n\n\nDas letzte Mal, dass ich Iwanako gesehen habe, war furchtbar unangenehm – richtig peinlich. Sie kam zu mir ins Krankenhaus, hat mir netterweise einen Apfel geschält und wir haben eine halbe Stunde nur dagesessen und uns angeschwiegen."


n "Sie hat sich verabschiedet und mir nicht in die Augen geschaut, als sie die Tür geschlossen hat."


n "Es war wohl ein passender Abschluss für die Reihe von Besuchen, die wohl uns beiden ziemlich wehgetan haben."


n "Jedes Mal, wenn sie mich im Krankenhaus besucht hat, wollte ich mit ihr reden, aber irgendetwas hat mich immer davon abgehalten."


n "Jedes Mal, wenn ich nicht mit ihr gesprochen hatte, ist es beim nächsten Mal noch schwieriger gewesen."


nvl clear

n "\n\n\n\nSie sah aus, als hätte sie ein schlechtes Gewissen, und ich wollte nichts sagen, was sie verletzen könnte, und mir sind nie die richtigen Worte eingefallen."


n "Ich glaube, Iwanako hat sich die Schuld für meinen Herzanfall gegeben. Das ist natürlich lächerlich, aber das zu wissen und es auch zu glauben sind zwei verschiedene Dinge."


n "Ich habe ihr gesagt, dass es nicht ihre Schuld war. Sie hat genickt, und ich glaube, sie hat wirklich verstanden, dass früher oder später irgendetwas passiert wäre, was meinen Herzanfall ausgelöst hätte."


n "Trotzdem hat sie jedes Mal so furchtbar traurig ausgesehen, wenn sie diese Tür geöffnet hat und in mein Zimmer gekommen ist."


n "Also habe ich es nie fertig gebracht, die Dinge zu sagen, die ich sagen wollte. Am Ende hat sie das vielleicht noch mehr verletzt."


$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl hide dissolve
nvl clear

scene ev hisao_letter_open onlayer master
with locationchange

window show

"Vorsichtig öffne ich den Umschlag und nehme den zusammengefalteten Brief heraus."


window hide

$ written_note("Lieber Hisao,\n\nWie geht es dir? Ich hoffe, dir geht es gut, und dir gefällt es an deiner neuen Schule. Alle hier vermissen dich. Fast unsere gesamte zweite Klasse ist nun zusammen in Klasse 3-1, also haben wir uns von Anfang an gut einfinden können. Ich bin sicher, du wärst auch in diese Klasse gekommen.")


$ written_note("Im Moment sind alle Drittklässler schon sehr angespannt wegen der Abschlussprüfungen, obwohl es noch so lange hin ist. Die Lehrer liegen uns ständig damit in den Ohren – sogar der alte Herr Tachibana, der übrigens dieses Jahr unser Klassenlehrer ist. Hättest du das gedacht? Ich war mir sicher, dass er nach unserem zweiten Jahr in Pension gehen würde, aber er nervt immer noch alle wegen der Prüfungen.\n")


$ written_note("Ich glaube, das ist der Hauptgrund warum alle Drittklässler so nervös sind. Ich muss zugeben, dass ich auch langsam mein Selbstvertrauen verliere, obwohl ich in Prüfungen bisher immer recht gut abgeschnitten habe.\n\n\n\n\n")


$ written_note("Es ist so seltsam, dass wir plötzlich die Ältesten sind, nicht wahr? Die Zeit ist so schnell vergangen. Ich frage mich, wo sie hin ist. Die neuen Erstklässler sehen so jung und irgendwie unschuldig aus. Ich frage mich immer wieder, ob ich in meinem ersten Jahr genauso war. Ich habe schon das ganze erste Trimester so ein nostalgisches Gefühl.\n\n\n")


$ written_note("Es gibt noch andere Dinge, die ich dir sagen will. Ich schreibe dir, weil ich das Gefühl hatte, dass ich dir nach dem Vorfall im Winter noch vieles hätte sagen sollen. Ich bedaure wirklich, dass ich es dir nicht persönlich sagen konnte, und ich habe dafür keine Entschuldigung…\n\n\n\n\n")


window show

"Okay, ich glaube, ich habe genug gelesen."


scene bg school_dormhisao onlayer master
with locationchange

"Ich zerknülle das Papier und werfe es durch den Raum. Ich verfehle den Papierkorb knapp, und der Brief rollt stattdessen unter meinen Nachttisch."


"Das war eine Entschuldigung dafür, dass sie mich im Stich gelassen hat. Nur, dass ich die jetzt nicht mehr wirklich brauche."


"Meine Zeit im Krankenhaus liegt schon lange hinter mir, und im Hier und Jetzt, gibt es Wichtigeres für mich."


stop music fadeout 8.0

"Emi zum Beispiel."


"Es war kein tolles Gefühl, von allen verlassen zu werden, aber es belastet mich nicht mehr."


"Um ehrlich zu sein, habe ich schon ewig nicht mehr an das Krankenhaus gedacht, bevor dieser Brief ankam. Es ist fast schon ärgerlich, dass ich ihn gekriegt habe."


"Ich muss auch noch für Prüfungen lernen. Ich habe keine Zeit für die Vergangenheit."


"Und nun zu den Hausaufgaben…"


scene black onlayer master
with dissolve



label de_E11a:

scene black onlayer master
with None

hi "Was haben wir heute überhaupt vor?"


play music music_daily fadein 1.0

scene bg school_girlsdormhall onlayer master
with dissolve

"Ich warte geduldig im Flur des Mädchenwohnheims vor Emis und Rins Zimmern."


"Emi hilft Rin anscheinend gerade beim Anziehen."


"Ich nehme an, das ergibt Sinn, denn ich habe keine Ahnung, wie sich Rin sonst anziehen sollte."


emi "Picknick!"


hi "Picknick?"


emi "Das hab ich doch gerade gesagt!"


hi "Hört sich ziemlich aufregend an."


emi "Ich weiß, nicht wahr?"


"In diesem Moment meldet sich Rin zu Wort."


rin "Der Himmel sieht heute bedrohlich aus."


"Das ist mir auf meinem Weg hierher auch aufgefallen. Obwohl es heute früh sonnig war, ist es jetzt am Nachmittag ziemlich düster."


"Die Luft ist so drückend wie vor einem schweren Regenguss."


"Ich frage mich, ob ich meinen Schirm hätte mitbringen sollen…"


hi "Da hat sie Recht."


hi "Emi, bist du sicher, dass du riskieren willst, vom Regen überrascht zu werden?"


"Ich weiß nicht, warum ich überhaupt gefragt habe."


show emi basic_shock onlayer master:
    center
    xpos 0.9
    easein 0.5 xpos 0.7
with charaenter

"Emi steckt ihren Kopf aus der Tür. Sie sieht geschockt aus, dass ich auch nur vorgeschlagen habe, unser Vorhaben abzusagen."


emi "Natürlich!"


show emi basic_annoyed onlayer master
with charachange

emi "Soll mich das Regenrisiko etwa aufhalten?"


"Ich muss über ihre kämpferische Antwort lächeln. Es ist fast, als würde sie den Regen herausfordern."


"Wenn Mutter Natur nun zur Tür herein kommen würde, würde Emi wahrscheinlich einen Streit mit ihr anfangen."


"… oder sie zumindest zu einem Wettlauf herausfordern."


"Emi scheint heute geradezu aggressiv fröhlich zu sein."


show rin basic_absent onlayer master:
    center
    xpos 0.9 alpha 0.0
    ease 1.0 xpos 0.7 alpha 1.0
show emi basic_annoyed onlayer master at twoleft
show bg school_girlsdormhall onlayer master at bgleft
with charamove

"Rin kommt heraus auf den Flur. Sie sieht aus wie immer."


hi "Na dann, sind wir alle fertig?"


show emi basic_closedhappy onlayer master
with charachange

emi "Ich bin fertig!"


show rin basic_deadpannormal onlayer master:
    tworight alpha 1.0
with charachange

"Rin nickt und sagt ein einzelnes Wort."


show rin basic_deadpan onlayer master
with charachange

rin "Korb."


hi "Wie bitte?"


show rin basic_deadpannormal onlayer master
with charachange

rin "Der Korb. In Emis Zimmer. Du sollst ihn tragen."


show emi basic_hes onlayer master
with charachange

"Emi hält sich verlegen eine Hand vor den Mund."


show emi basic_closedsweat onlayer master
with charachange

emi "Ohmeingott! Den hätte ich fast vergessen! Gut mitgedacht, Rin!"


show emi basic_closedsweat onlayer master at offscreenleft
with ease

with Pause(0.3)

show emi basic_closedgrin onlayer master at twoleft
with ease

"Emi huscht in ihr Zimmer und kommt mit einem anscheinend gut gefüllten Picknickkorb zurück."


with vpunch

"Als sie ihn mir übergibt, bemerke ich, dass er auch ziemlich schwer ist. Herrgott, wie viel Essen hat sie eingepackt?"


"… Besser gefragt, wo hat sie das Geld für all das her?"


hi "Also, können wir los?"


show emi basic_grin onlayer master
with charachange

emi "Jepp!"


show rin basic_awayabsent onlayer master
with charachange

"Rin nickt erneut, und wir verlassen das Wohnheim."


scene bg school_courtyard_rn onlayer master
with locationskip

"Ich lege unwillkürlich die Stirn in Falten, als ich sehe, wie grau der Himmel in den letzten zehn Minuten geworden ist."


"Dennoch scheint sich Emi von so nebensächlichen Dingen wie der Farbe des Himmels nicht beunruhigen zu lassen. Sie hopst richtig beim Gehen."


"Da fällt mir ein…"


hi "Wohin gehen wir?"


"Emi bleibt abrupt stehen und schaut mich verlegen an."


show emi sad_shy_rn onlayer master at center
with charaenter

emi "Weißt du, darüber habe ich mir noch nicht wirklich Gedanken gemacht."


emi "Was meinst du, Hisao?"


"Na ja, da ist die Ecke, wo wir am Schulfest gegessen haben, aber es wäre nett, wenn wir das Schulgelände mal verlassen könnten. Ich weiß aber nicht, ob es im Dorf gute Plätze für Picknicks gibt."


"Als ich gerade meinen Mund öffnen will, schlägt Rin unerwarteterweise etwas vor."


show emi sad_shy_rn onlayer master at twoleft
show bg school_courtyard_rn onlayer master at bgleft
with charamove

show rin basic_deadpan_rn onlayer master at tworight
with charaenter

rin "Im Dorf ist ein Park in der Nähe des Kunstladens."


show emi basic_closedhappy_rn onlayer master
with charachange

emi "Tolle Idee, Rin! Den hatte ich total vergessen!"


"Krise abgewendet."


hi "Weißt du, wie wir da hinkommen, Rin?"


show rin basic_deadpannormal_rn onlayer master
with charachange

"Rin zuckt mit den Schultern."


show rin basic_awayabsent_rn onlayer master
with charachange

rin "Sehr wahrscheinlich."


show emi excited_amused_rn onlayer master
with charachange

emi "Das reicht mir!"


"Mir wäre etwas mehr Sicherheit lieber… aber was soll's."


hi "Geh voraus, Rin."


scene bg school_gate_rn onlayer master
with locationchange

"Wir verlassen das Schulgelände und nehmen die Straße hinunter ins Dorf."


scene bg school_road_rn onlayer master
with locationchange

"Der Korb ist etwas schwer. Ich hoffe, dass es nicht zu weit bis zum Park ist."


scene bg suburb_roadcenter_rn onlayer master
with locationchange

"Wir kommen an dem Kunstladen vorbei, und Rin verlangsamt ihren Schritt etwas."


"Emi bemerkt die Veränderung und bleibt stehen."


show emi basic_grin_rn onlayer master at twoleft
show rin relaxed_nonchalant_rn onlayer master at tworight
with charaenter

emi "Willst du reingehen, Rin?"


show rin basic_awayabsent_rn onlayer master
with charachange

"Rin zuckt mit den Schultern."


show rin basic_deadpan_rn onlayer master
with charachange

rin "Ich brauche grade nichts."


show emi excited_proud_rn onlayer master
with charachange

emi "Bist du gaaaanz sicher?"


show rin basic_delight_rn onlayer master
with charachange

show rin basic_deadpandelight_rn onlayer master
with charachange

"Ein sehr schwaches Lächeln huscht über Rins Gesicht, aber sofort ist ihr normaler Gesichtsausdruck wieder da."


show rin basic_deadpan_rn onlayer master
with charachange

rin "Das Leben ist voller Unwägbarkeiten, aber in diesem Fall bin ich mir zumindest ziemlich sicher."


show rin basic_deadpanamused_rn onlayer master
with charachange

rin "Danke für das Angebot."


show emi basic_closedhappy_rn onlayer master
with charachange

emi "Na ja, ich muss ja nicht den Korb tragen."


show emi basic_grin_rn onlayer master
with charachange

emi "Aber ich wette, Hisao hätte auch nichts dagegen gehabt, oder?"


hi "Oh, natürlich nicht. Der ist ja auch nicht wirklich schwer."


"Ich hebe den Korb an, um das zu demonstrieren."


show emi excited_laugh_rn onlayer master
with charachange

"Emi unterdrückt ein Lachen und zeigt auf den Park, bei dem wir inzwischen angekommen sind."


$ renpy.music.set_volume(0.02, 0.0, channel="ambient")
play ambient sfx_rain fadein 15.0

scene bg suburb_park_rn onlayer master at bgright
with locationchange

emi "Oh, an den erinnere ich mich!"


show emi basic_closedhappy_rn onlayer master
with charachange

emi "Habe ich dich hier nicht dieses eine Mal getroffen, Rin?"


show emi basic_closedhappy_rn onlayer master at twoleft
show bg suburb_park_rn onlayer master
with charamove

show rin basic_deadpannormal_rn onlayer master at tworight
with charaenter

"Rin zieht ihre Augenbrauen leicht nach oben."


show rin basic_deadpan_rn onlayer master
with charachange

rin "Vielleicht."


show rin relaxed_boredom_rn onlayer master
with charachange

rin "Ich würde mich nur ungern festlegen."


show rin relaxed_nonchalant_rn onlayer master
with charachange

rin "Mit Erinnerungen ist das so eine Sache, weißt du?"


"Wer sagt's denn, wir haben es doch tatsächlich geschafft, heil anzukommen."


"Die Sonne ist immer noch nirgends zu sehen, aber weder Emi noch Rin scheint das zu stören."


scene ev picnic_normal onlayer master:
    yalign 1.0 subpixel True
    easein 8.0 yalign 0.0 
with whiteout







"Wir finden einen schönen Platz, um uns niederzulassen, und ich setze erleichtert den Korb ab."


"Es gibt eine erstaunliche Menge an Essen. Vielleicht sollten noch einige von Emis Teamkollegen dazukommen?"





emi "Ich verhungere gleich! Haut rein!"


"Sie stürzt sich auf das Essen, als hätte sie seit Jahren nichts mehr gegessen."


stop music fadeout 2.0

play sound sfx_thunder

show ev picnic_rain onlayer master:
    yalign 0.0
with charachange





$ renpy.music.set_volume(0.2, 0.5, channel="ambient")

show rain light onlayer master
with dissolve

"Ich greife gerade selbst nach dem Essen, als ich den ersten Regentropfen auf meinem Handrücken spüre."


hi "Oh oh."


hi "Sieht aus, als würde das Wetter uns doch noch einen Streich spielen."


hide ev onlayer master
show bg suburb_park_rn behind rain onlayer master
show emi sad_grit_rn behind rain onlayer master:
    twoleft
    ypos 1.15
show rin basic_absent_rn behind rain onlayer master:
    tworight
    ypos 1.2
with flash

"Emi starrt gen Himmel, als würde das reichen, um den Regen zu stoppen."


"Fast glaube ich, dass sie es schaffen kann. Ihr Starren ist wirklich furchteinflößend."


show emi basic_annoyed_rn onlayer master
with charachange

emi "Das soll es mal versuchen."


show emi sad_angry_rn onlayer master
with charachange

emi "Hörst du mich, Himmel? Hör auf der Stelle mit dem Regen auf!"


"Trotz des befehlenden Tons scheint der Himmel nicht vorzuhaben, auf Emi zu hören."


$ renpy.music.set_volume(0.5, 4.0, channel="ambient")

show rain medium onlayer master
with dissolve

"Stattdessen wird der Regen stärker. Rin rümpft angewidert die Nase angesichts dieser Entwicklung."


show rin basic_deadpan_rn onlayer master
with charachange

rin "Bedauerlich."


show emi basic_confused_rn onlayer master
with charachange

emi "Wie meinst du das?"


show rin basic_deadpannormal_rn onlayer master
with charachange

"Rin zuckt mit den Schultern."


show rin relaxed_nonchalant_rn onlayer master
with charachange

rin "Ich könnte das malen, wenn ich nicht hier draußen wäre. Ist nur schade, dass ich das verpasse."


"Sie scheint weder wütend noch verärgert zu sein, nur ein wenig enttäuscht."


show emi basic_closedhappy_rn onlayer master
with charachange

"Emi lacht über Rins Kommentar."


show emi basic_grin_rn onlayer master
with charachange

emi "Wir hätten vielleicht doch in dieses Kunstgeschäft gehen sollen, hm?"


$ renpy.music.set_volume(1.0, 6.0, channel="ambient")

show rain normal onlayer master
with dissolve

"Der Regen wird wieder ein wenig stärker; vielleicht ist er beleidigt, dass wir noch nicht geflüchtet sind."


"Trotz der warmen Temperaturen ist der Regen ziemlich kalt. Ich wünschte, ich hätte meinen Schirm mitgebracht."


hi "Hey, wir sollten besser irgendwo ins Trockene gehen."


show emi basic_confused_rn onlayer master
show rin basic_absent_rn onlayer master
with charachange

emi "Wir sind jetzt schon ziemlich nass, Hisao."


hi "Ja, aber wir könnten uns abtrocknen und vielleicht warten, bis der Sturm vorbei ist. Du willst dich doch nicht erkälten, oder?"


show emi basic_annoyed_rn onlayer master
with charachange

"Emi überlegt einen Moment. Ich weiß, dass ein Teil von ihr hier im Regen bleiben will – einfach aus Trotz."


"Zu ihrem Pech kümmert sich das Wetter kaum darum, was wir tun."


show emi basic_closedgrin_rn onlayer master
with charachange

emi "Da hast du wohl Recht."


show emi sad_grin_rn onlayer master
with charachange

emi "Wo könnten wir hingehen?"


"Ich weiß keine Antwort. Die Gegend ist für mich immer noch ziemlich neu."


"Obwohl ich mich an die Schule selbst inzwischen recht gut gewöhnt habe, ist die Umgebung noch eine Unbekannte für mich."


"Ich kenne nur diesen Kunstladen, und das auch nur, weil wir gerade daran vorbeigelaufen sind."


show emi basic_closedgrin_rn onlayer master
with charachange

"Zum Glück schnippt Emi bald triumphierend mit den Fingern."


show emi basic_happy_rn onlayer master
with charachange

emi "Ich hab's! Es gibt hier in der Nähe ein Teehaus!"


emi "Wir können einen Tee trinken und uns abtrocknen, kein Problem!"


"Das hört sich wirklich nicht schlecht an."


hi "Großartig! Weißt du, wo es ist?"


show emi basic_grin_rn onlayer master
with charachange

"Emis Nicken sieht recht zuversichtlich aus."


show emi basic_closedgrin_rn onlayer master
with charachange

emi "Klar, weiß ich!"


show emi basic_hes_rn onlayer master
with charachange

emi "Glaube ich."


show emi excited_laugh_rn onlayer master
with charachange

emi "Aber so oder so ist es ein Abenteuer, oder?"


hi "Ein Abenteuer, hm? Na ja, ein kleines Abenteuer kann wohl nicht schaden."


"Ich denke, solange wir aus dem Regen rauskommen, bin ich glücklich."


show emi basic_grin_rn onlayer master at twoleft
show rin basic_absent_rn onlayer master at tworight
with dissolvecharamove

"Zumindest ist der Picknickkorb nun etwas leichter."


hi "Geh voraus!"


show bg suburb_roadcenter_rn onlayer master
hide rin onlayer master
hide emi onlayer master
with locationchange

"Rin und ich folgen Emi, als sie sich einigermaßen zuversichtlich ihren Weg durch die Gassen sucht."


show emi basic_confused_rn behind rain at center onlayer master
with charaenter

emi "Und hier jetzt links…"


show emi excited_joy_rn onlayer master
with charachange

emi "Da! Das Shanghai!"


"Emi strahlt triumphierend und zeigt auf das Teehaus."


show bg suburb_shanghaiext_rn onlayer master
hide emi onlayer master
with locationchange


label de_E11x:

"Jetzt wo ich es sehe, fällt mir ein, dass ich schon einmal hier war. Drinnen ist es ziemlich voll; liegt sicher an dem plötzlichen Regen."



play sound sfx_storebell
stop ambient fadeout 0.5
play music music_jazz fadein 2.0

scene bg suburb_shanghaiint onlayer master
with locationchange

$ renpy.music.set_volume(0.7, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0

with Pause(1.0)

show yuukoshang neutral_down onlayer master at center
with charaenter

yu "Willkommen! Kann ich-"


show yuukoshang happy_down onlayer master
with charachange

yu "Oh, ihr seid es."


"Yuuko scheint Emi zu kennen."


show yuukoshang happy_down onlayer master at tworight
show bg suburb_shanghaiint onlayer master at bgright
with charamove

show emi basic_closedhappy onlayer master at twoleft
with charaenter

"Emi grinst strahlend, erfreut, dass Yuuko sich an sie erinnert."


show emi basic_grin onlayer master
with charachange

emi "Hallo Yuuko! Hast du noch Plätze für uns?"


show yuukoshang neutral_down onlayer master
with charachange




label de_E11y:

"Drinnen ist es ziemlich voll; liegt sicher an dem plötzlichen Regen."


play sound sfx_storebell
stop ambient fadeout 0.5
play music music_jazz fadein 2.0

scene bg suburb_shanghaiint onlayer master
with locationchange

$ renpy.music.set_volume(0.7, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0

with Pause(1.0)

show yuukoshang neutral_down onlayer master at center
with charaenter

yu "Willkommen! Kann ich-"


"Zu meiner Überraschung stelle ich fest, dass die Kellnerin niemand anderes ist als Yuuko."


"In ihrer Uniform sieht sie zumindest so aus. Es ist kaum zu glauben, dass das die Bibliothekarin an unserer Schule ist."


"Hat sie zwei Jobs? Muss wohl so sein, oder?"


show yuukoshang happy_down onlayer master
with charachange

yu "Oh, ihr seid es."


"Yuuko scheint Emi zu kennen."


show yuukoshang happy_down onlayer master at tworight
show bg suburb_shanghaiint onlayer master at bgright
with charamove

show emi basic_closedhappy onlayer master at twoleft
with charaenter

"Emi grinst strahlend, erfreut, dass Yuuko sich an sie erinnert."


show emi basic_grin onlayer master
with charachange

emi "Hallo Yuuko!"


hi "Hi, Yuuko. Ich wusste gar nicht, dass du auch hier arbeitest."


show yuukoshang worried_down onlayer master
with charachange

yu "Kenne ich Sie?"



show yuukoshang worried_up onlayer master
with charachange

yu "Sie kommen mir bekannt vor, aber ich glaube nicht, dass ich Sie schon einmal hier drin gesehen habe."


hi "Äh, wir haben uns bei deinem anderen Job kennengelernt. In der Bibliothek der Yamaku. Erinnerst du dich?"


show yuukoshang happy_up onlayer master
with charachange

"Ihre Augen weiten sich."


show yuukoshang closedhappy_down onlayer master
with charachange

yu "Ja, genau! Schön, dich wiederzusehen…"



show yuukoshang panic_down onlayer master
with charachange

yu "Oh nein, das ist schlecht!"


show yuukoshang panic_up onlayer master
with charachange

yu "Ich hätte mich an das Gesicht eines Kunden erinnern müssen! Es tut mir leid… Es tut mir furchtbar leid!"


"Yuuko wechselt in Sekundenbruchteilen von Erkenntnis zu Panik und verbeugt sich mehrmals schnell hintereinander. Ich kann gerade noch ausweichen, bevor unsere Köpfe zusammenstoßen."


hi "Achtung, hey, beruhige dich!"


hi "Hör zu, ich war doch gar kein Kunde, als wir uns zum ersten Mal getroffen haben. Ich war noch nie zuvor im Shanghai, also ist alles in Ordnung."


"Nicht gerade die beste Logik, aber sie scheint sich etwas zu beruhigen."


show yuukoshang worried_down onlayer master
with charachange

yu "Glaubst du wirklich?"


hi "Äh, ja, ich bin mir sicher. Ganz sicher. Richtig, Mädels?"


show emi basic_closedgrin onlayer master
with charachange

"Emi hat dieses kleine Drama sichtlich amüsiert beobachtet."


show emi excited_proud onlayer master
with charachange

emi "Klar stimmt das!"


show yuukoshang neutral_up onlayer master
with charachange

yu "Na ja, dann…"


show emi basic_happy onlayer master
with charachange

emi "Also Yuuko, hast du noch Plätze für uns?"


show yuukoshang neutral_down onlayer master
with charachange


label de_E11z:

$ renpy.music.set_volume(0.3, 3.0, channel="ambient")

"Yuuko nickt und führt uns zu einem Tisch in der Ecke. Sie gibt uns noch ein paar kleine Handtücher, bevor sie unsere Bestellung aufnimmt."


show yuukoshang happy_down onlayer master
with charachange

yu "Was wollt ihr haben?"


show emi basic_closedhappy onlayer master
with charachange

emi "Kuchen! Und Tee auch noch, denke ich."


show yuukoshang neutral_down onlayer master
with charachange

yu "Was für ein Kuchen?"


show emi excited_proud onlayer master
with charachange

emi "Ich lass mich überraschen!"


show yuukoshang worried_up onlayer master
with charachange

"Yuuko sieht aus, als würde ihr bei dem Gedanken unwohl, jemanden überraschen zu müssen, aber sie nickt und wendet sich Rin zu."


show rin invis onlayer master:
    yalign 1.0 xpos 1.0 xanchor 0.6
with None

show yuukoshang neutral_down onlayer master:
    xpos 0.55 
show emi basic_grin onlayer master at left
show rin basic_absent onlayer master at right
show bg suburb_shanghaiint onlayer master at center
with dissolvecharamove

yu "Und für dich?"


show rin negative_spaciness onlayer master:
    right alpha 1.0
with charachange

rin "Ich nehme einen Strohhalm. Meine Füße sind ganz nass."


show yuukoshang worried_up onlayer master
with charachange

yu "Wie bitte?"


show rin basic_awayabsent onlayer master
with charachange

rin "Strohhalme zum Trinken. Einen bitte."


show yuukoshang worried_down onlayer master
with charachange

"Yuuko ist sich offensichtlich nicht sicher, was sie davon halten soll. Sie spielt nervös mit ihrem Kuli und dem Notizblock und sieht aus, als wollte sie anfangen zu weinen, bevor sie sich mir zuwendet."


show yuukoshang neutral_down onlayer master
with charachange

yu "Und du?"


hi "Nur Tee, denke ich."


"Emi würde mir wahrscheinlich was erzählen, wenn ich Kuchen bestellen würde."


show emi sad_depressed onlayer master
with charachange

emi "Ach, komm schon, Hisao! Ich will nicht als einzige was zu Essen bestellen, da komme ich mir so gefräßig vor!"


hi "Ich versuche doch nur, gesund zu essen."


hi "Ist doch deine Anweisung."


show emi basic_closedgrin onlayer master
with charachange

emi "Na ja… Heute hast du frei! Du kannst morgen wieder gesund essen!"


hi "Na dann… Ich denke, ich nehme doch ein Stück Kuchen."


show yuukoshang neurotic_up onlayer master
with charachange

"Yuuko sieht leicht irritiert aus, dass ich meine Meinung geändert habe."


yu "Welche Sorte?"


"Ich schiele zu Emi hinüber und grinse."


hi "Ich lass mich überraschen."


show yuukoshang smile_down onlayer master
with charachange

"Yuuko seufzt und nickt."


yu "In Ordnung. Eure Bestellung kommt gleich."


show emi basic_grin onlayer master at left
show yuukoshang neutral_down onlayer master
show rin basic_awayabsent onlayer master
with shorttimeskip

"Obwohl so viel los ist, kommt unsere Bestellung wirklich ziemlich schnell."


show emi excited_joy onlayer master
with charachange

emi "Danke, Yuuko!"


"Yuuko nickt dankbar."


stop music fadeout 4.0

show yuukoshang happy_down onlayer master
with charachange

yu "Das ist ein anderer Begleiter als sonst, nicht wahr?"



"Was? Anderer Begleiter?"


show emi basic_hes onlayer master
with charachange

"Emi muss meine Verwirrung bemerkt haben, denn sie sieht etwas verlegen aus."


emi "W-Was? Oh ja, das stimmt wohl."


show emi sad_grin onlayer master
with charachange

emi "Das ist Hisao, ein Freund von mir."


hi "Wir kennen uns."


show yuukoshang smile_down onlayer master
with charachange

yu "Hm. Wie klein die Welt ist."


show yuukoshang neutral_down onlayer master
with charachange

yu "Na ja, sagt Bescheid, falls ihr noch etwas braucht."


hide yuukoshang onlayer master
with charaexit

show emi sad_grin onlayer master at twoleft
show rin basic_awayabsent onlayer master at tworight
with charamove

"Damit huscht Yuuko davon, um die anderen Tische zu bedienen, und ich denke über ihren Kommentar nach."


"Anderer Begleiter? Hmm, das kann schon sein, oder? Emi ist ziemlich beliebt, wie ich gehört habe."


"Es war wahrscheinlich dieser Kerl aus der Leichtathletikmannschaft."


"Das ist doch dämlich. Ich kann einfach Emi fragen."


show rin basic_absent onlayer master
with charachange

play music music_comedy fadein 0.5

hi "Also, wer ist dieser andere Begleiter, hm? Hast du einen geheimen Liebhaber oder so was?"


show emi basic_closedhappy onlayer master
show rin basic_awayabsent onlayer master
with charachange

"Emi lacht wieder, aber dieses Mal habe ich das Gefühl, dass es mehr aus Nervosität ist als echt."


show emi basic_grin onlayer master
with charachange

emi "Das war nur der Kapitän der Leichtathletikmannschaft. Er kommt gerne nach dem Training hierher."


show emi basic_closedgrin onlayer master
with charachange

emi "Und wenn es etwas zu besprechen gibt, komme ich manchmal mit."


"Hmm, das hört sich sehr verdächtig an…"


show rin basic_absent onlayer master
with charachange

hi "Oh, verstehe."


"Ich könnte das Thema wechseln, aber ich kann der Versuchung nicht widerstehen, noch einmal nachzusetzen."


hi "Also hast du {b}doch{/b} einen geheimen Liebhaber!"


hi "Ich wusste es!"


show rin basic_deadpanamused onlayer master
with charachange

"Rin beobachtet unseren Schlagabtausch leicht amüsiert, dann murmelt sie etwas, das ich nicht ganz mitbekomme."


rin "… jedenfalls."


show emi basic_confused onlayer master
with charachange

$ doublespeak(emi,hi,"Was?", "Hm?")


show rin basic_surprised onlayer master
with charachange

"Rin kommt zurück von… wo immer ihre Gedanken auch unterwegs gewesen sein mögen."


rin "Hm?"


hi "Was hast du gerade gesagt?"


show rin basic_deadpan onlayer master
with charachange

rin "Hm."


hi "Nein, davor."


show rin relaxed_nonchalant onlayer master
with charachange

rin "Keine Ahnung."


hi "Oh. Na ja."


hi "Okay."


show emi basic_grin onlayer master
show rin basic_deadpannormal onlayer master
with charachange

"Ich wechsle das Thema, aber mir fällt auf, dass Emi erleichtert zu sein scheint, dass Rin unsere Unterhaltung unterbrochen hat."


"Vielleicht bin ich ein wenig zu weit gegangen…"


"Unsere Unterhaltung kommt zum Erliegen, als Emi und ich uns mit unseren Kuchen beschäftigen."


"Ich habe Erdbeere, und er schmeckt überraschend gut."


play sound sfx_slide2

show emi excited_happy_close onlayer master
with characlose

show emi basic_closedgrin onlayer master
with charadistant

"Emi scheint der gleichen Meinung zu sein, denn plötzlich stibitzt sie mit ihrer Gabel ein Stück davon."


hi "Diebin!"


show emi excited_proud onlayer master
with charadistant

emi "Piratin. Das ist ein Unterschied."


hi "Wir sind nicht auf See!"


show emi basic_closedgrin onlayer master
with charadistant

emi "Na ja, nein. Aber da draußen ist eine Menge Wasser, und das reicht, oder?"


show emi sad_grin onlayer master
with charadistant

emi "Außerdem kannst du was von meinem haben. Ich glaube, es ist Preiselbeere oder so was."


show emi sad_depressed onlayer master
with charadistant

emi "Ich hätte Erdbeere bestellen sollen. Ich mag Erdbeeren."


hi "Nimm dir ruhig von meinem, wenn du willst."


"Und irgendetwas zwingt mich hinzuzufügen:"


hi "Nachdem du das ja eh schon getan hast."


show emi basic_closedgrin onlayer master
with charadistant

"Emi streckt mir die Zunge heraus, aber das hindert sie nicht daran, sich meinen Kuchen zu schnappen. Ich probiere auch von ihrem."


"Es ist Himbeere, und ziemlich gut."


show rin relaxed_boredom onlayer master
with charachange

rin "Der Regen hat nachgelassen."


"Sieht so aus, als hätte Rin Recht."


"Und genau zur rechten Zeit. Ich bin mit meinem Essen fertig und Emi anscheinend auch."


hi "Nun, wir sollten bezahlen und uns auf den Weg machen, bevor es wieder losgeht."


stop ambient fadeout 1.0

scene bg suburb_shanghaiext_rn onlayer master
with locationchange

"Es dauert ein paar Minuten, bis Yuuko uns bemerkt, aber das Bezahlen und der Aufbruch gehen dann recht schnell."


show emi basic_grin_rn onlayer master at center
with charaenter

emi "So, wollen wir zurück in den Park?"


"Mir fällt fast die Kinnlade herunter."


hi "Machst du Witze? Es fängt sicher gleich wieder an zu regnen!"


"Ich glaube, ich habe sogar gerade ein paar Regentropfen gespürt."


show emi sad_grin_rn onlayer master
with charachange

emi "Hmm… Du könntest Recht haben."


show emi basic_closedgrin_rn onlayer master
with charachange

emi "Na ja gut, ich will mal nicht so sein, aber ich habe jetzt ein Picknick gut, verstanden?"


"Ich weiß nicht, ob das mir galt oder Rin, oder uns beiden."


hi "Schon gut."


show emi excited_proud_rn onlayer master
with charachange

emi "Und nun Beeilung! Ich wollte noch ein paar Runden laufen, und es wäre schön, wenn ich das ohne Regen tun könnte."


hi "Ich dachte, heute wäre dein freier Tag!"


$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
stop music fadeout 6.0

show emi sad_depressed_rn onlayer master
with charachange

emi "Na ja…"


"Emi zögert plötzlich mit ihrer Erklärung."


show emi sad_grin_rn onlayer master
with charachange

emi "Ich brauche das Training."


show emi basic_grin_rn onlayer master
with charachange

emi "Und ich muss sowieso die Kalorien von diesem Kuchen verbrennen."


"Warum habe ich das Gefühl, dass sie etwas verschweigt?"


hi "Bist du sicher? So viel Kuchen war es doch gar nicht…"


show emi basic_closedgrin_rn onlayer master
with charachange

emi "Nein, es war nicht so viel Kuchen für {b}dich{/b}. Ich habe das meiste davon gegessen."


"Da hat sie Recht."


label de_choiceE11:
menu:
    with menueffect
    "Trotzdem denke ich, ich sollte ihr zumindest anbieten, mit ihr zu laufen…"
    "Anbieten, mit Emi zu laufen.":






        return m1
    "Nichts sagen.":


        return m2

label de_E11b:


hi "Hey, ich laufe mit dir."


hi "Ist doch eine gute Gelegenheit, oder?"


show emi basic_annoyed_rn onlayer master
with charachange

"Emi schüttelt energisch den Kopf."


mi "Nein, Hisao. Du sollst dich doch diese Woche schonen, weißt du noch?"


emi "Ich lasse nicht zu, dass du dich überanstrengst."


"Ich habe das Gefühl, sie ist besser darin, Ratschläge zu geben als sie anzunehmen."


hi "Wie du meinst, Emi."


"Ist wohl besser, nicht zu diskutieren."


label de_E11c:


"Sieht so aus, als würde sie jetzt gerade lieber allein sein."


"Ich behalte mein Angebot lieber für mich."


label de_E11d:


stop music fadeout 12.0

scene bg school_dormext_full_rn onlayer master
with locationskip

play ambient sfx_rain fadein 2.0
show rain normal onlayer master
with Dissolve(2.0)

"Als wir uns dem Mädchenwohnheim nähern, fängt es wieder an zu regnen."


show emi sad_annoyed_rn behind rain at center onlayer master
with charaenter

"Emis Gesicht verdunkelt sich etwas."


emi "Och menno…"


emi "Blöder Regen."


hi "Ach, es wird sicher bald wieder nachlassen. Dann kannst du immer noch laufen gehen, oder?"


show emi basic_grin_rn onlayer master
with charachange

"Emi scheint amüsiert zu sein."


show emi excited_proud_rn onlayer master
with charachange

emi "Als ob ich nicht im Regen laufen würde."


hi "Das solltest du nicht tun! Du könntest dich erkälten!"


show emi basic_grin_rn onlayer master
with charachange

"Emi winkt sorglos ab."


emi "Lächerlich! Ich werde nie krank."


show emi basic_closedgrin_rn onlayer master
with charachange

emi "Mein Immunsystem ist viel zu stark für so was."


"Ich muss einfach lachen."


hi "Na ja, dann sehen wir uns morgen, okay?"


show emi basic_happy_rn onlayer master
with charachange

emi "Ja!"


show emi basic_grin_rn onlayer master
with charachange

emi "Danke, dass du mitgekommen bist! Oh, und dass du den Picknickkorb getragen hast!"


show emi excited_amused_rn onlayer master
with charachange

emi "Ich bringe ihn morgen zum Mittagessen mit, dann können wir auf dem Dach picknicken!"


hi "Hört sich gut an. Bis dann!"


hide emi onlayer master
with charaexit

"Emi nimmt mir den Korb ab und stürmt durch die Tür."


"Rin schenkt mir ein halbes Nicken und schlendert dann ebenfalls hinein."


"Verdammt, es ist nass hier draußen."


"Ich muss dringend in mein Zimmer und trockene Klamotten anziehen."


stop ambient fadeout 2.0

scene bg school_dormhallway onlayer master
with locationskip

"Bald stehe ich vor meiner Tür, aber plötzlich steht Kenji mit einem Stapel Bücher in den Händen vor mir."


show kenji neutral onlayer master at center
with charaenter

ke "Hey, Kumpel, kannst du mir mal kurz helfen?"


hi "Hm?"


play music music_kenji fadein 0.5

with vpunch

"Er drückt mir einfach so die Bücher in die Hand, während er nach seinem Zimmerschlüssel sucht."


show kenji happy onlayer master
with charachange

ke "Danke, du rettest mir das Leben."


ke "Wenn es dich nicht gäbe, müsste ich meine Tür unverschlossen lassen, und das würde nur Ärger bedeuten."


show kenji tsun onlayer master
with charachange

ke "Die perfekte Gelegenheit, mir eine Falle zu stellen oder vielleicht einfach eine Bombe zu legen, wenn sie sich nicht die Finger schmutzig machen wollen."


ke "Das wollen sie wahrscheinlich nicht."


ke "Sie könnten sich ja einen Fingernagel einreißen, wenn sie versuchen, mich zu erstechen."


ke "Frauen."


"Mein Gehirn erwägt, die verbale Flut zu verarbeiten, die über mich hereinbricht, entscheidet sich dann aber dafür, weiterhin unwissend zu bleiben."


hi "Ah… ha."


show kenji happy onlayer master
with charachange 

ke "Wo warst du überhaupt die ganze Zeit, Mann?"


show kenji neutral onlayer master
with charachange 

ke "Ich hätte deine Hilfe brauchen können, als ich die alle aus der Bibliothek geholt habe!"


ke "Ich habe an deine Tür geklopft, aber du warst nicht da."


hi "Oh, tut mir leid."


"Nicht wirklich. Du denkst wohl, ich wäre so eine Art Packesel."


hi "Ich war mit Emi und Rin unterwegs."


show kenji rage onlayer master
with charachange

"Kenji stolpert erschrocken rückwärts."


"Es sieht aus, als hätte ich gerade seinen Hund erschossen – wenn er einen Hund hätte."


ke "Die beiden Amputierten wieder?"


show kenji tsun onlayer master
with charachange

ke "Was habt ihr dieses Mal gemacht?"


hi "Na ja, am Ende waren wir im Shanghai-"


"Ein Schrei der Verzweiflung hält mich vom Weiterreden ab."


show kenji rage onlayer master
with vpunch

ke "Das Shanghai?"


ke "Warum das Shanghai?"


ke "Nein nein nein nein, Mann, du kannst nicht einfach in das verdammte Shanghai gehen!"


ke "Das ist der gefährlichste Platz im ganzen Dorf!"


ke "Ein richtiges Bollwerk ihrer besten Agentinnen!"


ke "Ich weiß es! Ich bin ihnen begegnet!"


ke "Sie werden vor nichts haltmachen, um dich in Sicherheit zu wiegen, und dann BAM!"


play sound sfx_impact2
with vpunch

"Er schlägt zur Bekräftigung gegen seine Tür."


ke "Brieftasche weg. Busfahrkarte? Weg. Identität? Verdammt noch mal {b}weg{/b}, Mann!"


show kenji tsun onlayer master
with charachange

ke "Versprich mir, dass du da nie wieder hin gehst!"


"Er scheint so vehement gegen das Shanghai zu sein, dass ich bereit bin, ein wenig zu lügen, um in mein Zimmer zu kommen."


hi "Klar, ich werde nicht wieder hingehen."


"Oder zumindest werde ich dir nie wieder erzählen, dass ich hingegangen bin."


"Das scheint meinen bebrillten Zimmernachbarn zu besänftigen."


show kenji neutral onlayer master
with charachange

ke "Gut, gut."


show kenji happy onlayer master
with charachange

ke "Tut mir leid, dass ich mich so aufgeregt habe, aber ich kenne die Gefahr dort zu gut, um dich noch einmal in die Höhle des Löwen wandern zu lassen."


ke "Du bist einmal lebend wieder heraus gekommen, aber zweimal… Damit würdest du dein Schicksal herausfordern."


hi "Ja, äh… Ich muss mich umziehen und… äh… Hausaufgaben machen. Also… Wir sehen uns später."


show kenji tsun onlayer master
with charachange

ke "Hm?"


show kenji neutral onlayer master
with charachange

ke "Oh, klar. Wie du meinst."


"Mir fällt plötzlich ein, dass ich immer noch seine Bücher halte."


hi "Die nimmst du besser."


"Einer der Titel fällt mir ins Auge, irgendwas über Kryptographie."


"Was für ein Spinner."


stop music fadeout 6.0

show kenji neutral onlayer master:
    center
    easeout 0.5 xpos 0.3 alpha 0.0
with None

"Kenji schnappt sich seine wertvolle Fracht und verschwindet durch seine Tür."


$ renpy.music.set_volume(0.1, 0.0, channel="ambient")
play ambient sfx_rain fadein 1.0

scene bg school_dormhisao onlayer master
with locationchange

"Ich öffne meine eigene Tür und gehe in mein Zimmer, dankbar, endlich aus meinen nassen Klamotten herauszukommen."


"Der Regen draußen wird wieder stärker, und ich hoffe, dass Emi nicht in diesem Wetter laufen gegangen ist. Es schien ihr Ernst damit zu sein, allein zu laufen. Ich wundere mich nur, ob ihr Bein ihr immer noch Probleme macht."


"Ich versuche, mich zu erinnern, ob ich sie heute irgendwann humpeln gesehen habe, aber mir fällt nichts dazu ein. Wahrscheinlich habe ich den Tag einfach zu sehr genossen, auch wenn es geregnet hat."


"Und wenn ich an die Ereignisse des heutigen Tages denke, wandern meine Gedanken immer wieder zu meiner Trainingspartnerin."


"Ihre Weigerung, sich unsere Pläne durch den Regen vermiesen zu lassen, war unglaublich süß."


"Aber da war noch etwas anderes."


"So eine unerschütterliche Einstellung, den Tag so zu nehmen, wie er kommt."


"Das mag ich an ihr."


"Vielleicht muss ich das auch ein wenig lernen."


stop ambient fadeout 2.0
scene black onlayer master
with dissolve

$ suppress_window_after_timeskip = True



label de_E12a:

window hide None

scene black onlayer master
with dissolve

play sound sfx_alarmclock

with Pause(2.0)

scene bg school_dormhisao onlayer master
with openeye

window show

"Das Klingeln meines Weckers reißt mich aus meinem Traum von Piraten und anderem Zeug, an das ich mich nicht mehr erinnern kann."


scene bg school_track onlayer master
with locationskip

play music music_pearly

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

"Ich bin noch ein wenig verschlafen, und ich habe das Gefühl, dass ich länger als sonst brauche, um mich anzuziehen und zum Sportplatz zu kommen."


"Ein Blick auf meine Uhr sagt mir, dass ich Recht hatte. Ich bin wirklich ein wenig zu spät."


"Die Sache ist…"


"Emi ist nicht da."


"Das ist seltsam. Sie sollte eigentlich hier sein."


"Sie sollte definitiv hier sein."


"Ich meine, ich war {b}zu spät{/b}."


"Sieht aus, als wäre ich nicht der einzige, der heute Morgen Probleme beim Aufstehen hatte."


"Mir fällt ein, dass es gestern nicht mehr aufgehört hat zu regnen. Ist sie trotzdem noch laufen gegangen?"


label de_E12b:


"Sehr wahrscheinlich. Emi ist vieles aber nicht vorsichtig. Sie hat sich wahrscheinlich gedacht, dass der Regen nicht aufhören würde und wollte deshalb nicht, dass ich mit ihr laufe."


"Ich wäre trotzdem gerne mit ihr gelaufen – auch im Regen."


"Verdammt, zumindest hätte ich sie überreden können hereinzukommen, als es ganz schlimm wurde. Aber genau darum wollte sie mich ja nicht dabeihaben."


label de_E12c:


"Ich hätte ihr anbieten sollen mit ihr zu laufen."


"Dann hätte ich ihr das ausreden können, oder ich wüsste zumindest, ob es ihr gut geht. Was wenn sie vom Blitz getroffen wurde oder so was?"


"Ich würde mir das nie verzeihen."


"…"


"Okay, das ist jetzt wahrscheinlich etwas übertrieben."


"Emi ist ja nicht blöd. Nicht einmal sie würde während eines Gewitters draußen bleiben."


"Soweit vertraue ich ihrem Urteilsvermögen."


label de_E12d:


"Dennoch wüsste ich gerne wo sie ist."


"… Na ja, da kann man nichts machen. Ich sollte mich besser aufwärmen und anfangen und hoffen, dass Emi noch auftaucht – mit einem Grinsen im Gesicht und einer Ausrede."


scene bg school_track_running onlayer master
with shorttimeskip

show bg school_track_on onlayer master
with Dissolve(3.0)

"Auf meiner Abkühlrunde muss ich mir eingestehen, dass Emi nicht mehr kommen wird."


"Und ich habe immer noch keine Ahnung, wo sie ist. Die Sorge nagt an mir, und gleichzeitig frage ich mich, warum ich eigentlich so besorgt um sie bin."


"Das Laufen hat mich eine Weile davon abgelenkt, aber jetzt, wo ich fertig bin, fange ich wieder an, mir Sorgen zu machen."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl clear

nvl show dissolve

n "\n\nEs war seltsam, ohne sie zu laufen."


n "Es hat mich richtig nervös gemacht."


n "Mir wird plötzlich klar, dass ich nicht nur laufe, um gesund zu bleiben, sondern auch, um mit Emi zusammen zu sein – wenn ich so darüber nachdenke, ist Emi wahrscheinlich der größere Grund."


n "Das ist so eine Sache, die eigentlich ganz offensichtlich ist, aber irgendwie ist es mir nie bewusst geworden."


n "Sie ist wirklich jemand, mit dem ich sehr gerne zusammen bin."


n "Das ist nicht wirklich eine welterschütternde Erkenntnis."


n "Trotzdem bin ich leicht schockiert."


n "Wann ist das passiert?"


n "Na ja, keine Zeit darüber nachzudenken – obwohl ich diese neuen Entwicklung gerne näher beleuchten würde, ist es mir zur Zeit wichtiger, herauszufinden, was mit Emi los ist."


n "Ich frage einfach Doc, wenn ich bei ihm bin."


$ renpy.music.set_volume(1.0, 2.0, channel="music")
stop music fadeout 2.0

nvl clear
nvl hide dissolve

scene bg school_nurseoffice onlayer master
show nurse neutral onlayer master at center
with shorttimeskip

nk "Nun, du scheinst gut in Form zu sein, Hisao."


hi "Schön, das zu hören."


"Ich ziehe mein T-Shirt wieder an und stehe auf."


"Aber anstatt zu gehen wie sonst immer stelle ich noch eine Frage."


hi "Übrigens, wo ist denn Emi? Sie war heute Morgen nicht da."


hi "Geht es ihr gut?"


show nurse concern onlayer master
with charachange

"Obwohl ich tapfer versuche, die Sorge in meiner Stimme zu verbergen, sehe ich an Docs Grinsen, dass ich kläglich versagt habe."


nk "Heißt das, sie hat dir nichts gesagt?"


nk "Sie liegt krank im Bett."


hi "Wie? Krank?"


show nurse neutral onlayer master
with charachange

"Doc zuckt mit den Schultern."


nk "Ja, sie kam heute Morgen mit Fieber zu mir ins Büro."


nk "Um ehrlich zu sein, wundert es mich, dass sie es bis hierher geschafft hat."


show nurse concern onlayer master
with charachange

nk "Als sie hier ankam, hat sie fast gekocht."


nk "Ich glaube, sie wollte es dich irgendwie wissen lassen, aber sie hat mich gebeten, dir zu – ach verdammt!"


stop music fadeout 2.0

show nurse neutral onlayer master
with charachange

"Doc lächelt verlegen, und er scheint es sogar zumindest ein bisschen ehrlich zu meinen."


nk "Ich habe ihr gesagt, ich würde beim Sportplatz vorbeischauen und dir Bescheid sagen. Tut mir leid."



play music music_nurse fadein 1.0

show nurse fabulous onlayer master
with charachange

nk "Aber wir müssen Emi ja nicht erzählen, dass ich es vergessen habe, oder?"


"Ich grinse verschlagen zurück."


hi "Nein, natürlich nicht."


hi "Das eignet sich zu gut zum Erpressen."


hi "Ich hebe es mir auf, falls ich mal einen Gefallen brauche."


show nurse grin onlayer master
with charachange

"Doc lacht."


nk "Na ja, ich glaube, das habe ich verdient."


nk "Aber weißt du, ich hätte sooo viel, womit ich dich erpressen könnte, von dem du keine Ahnung hast."


show nurse fabulous onlayer master
with charachange

nk "Also nicht zu gierig, werden, okay?"


"Mein Gesichtsausdruck bringt ihn wieder zum Lachen."


show nurse grin onlayer master
with charachange

nk "War nur Spaß, Hisao."


show nurse concern onlayer master
with charachange

nk "Aber ernsthaft – erzähl Emi nicht, dass ich es vergessen habe, okay?"


hi "Das Geheimnis ist bei mir sicher."


show nurse neutral onlayer master
with charachange

nk "Gut. Und nun raus hier."


hi "Moment, eine Frage habe ich noch."


show nurse fabulous onlayer master
with charachange

nk "Schieß los."


hi "Wird es ihr bald wieder besser gehen?"


show nurse grin onlayer master
with charachange 

nk "Oh ja, definitiv."


show nurse neutral onlayer master
with charachange 

nk "Ihr Fieber war hoch, aber als sie zurück auf ihr Zimmer gegangen ist, war es schon wieder am Sinken."



nk "Ich werde wahrscheinlich in der Mittagspause noch mal nach ihr sehen, um sicher zu gehen, aber ich gehe davon aus, dass sie heute Abend wieder auf den Beinen ist – egal was ich sage."


hi "Hmm, vielleicht sollte ich nach dem Unterricht mal bei ihr vorbeischauen."


"Es dauert eine Sekunde, bis mir bewusst wird, dass ich laut gedacht habe."


show nurse fabulous onlayer master
with charachange

"Doc hebt eine Augenbraue und schaut mich einen Moment lang forschend an."


nk "Hmm…"


show nurse neutral onlayer master
with charachange 

nk "Na ja, das wäre vielleicht gar keine schlechte Idee."


nk "Du könntest mir Bescheid sagen, wenn es ihr wieder schlechter gehen sollte."


show nurse concern onlayer master
with charachange

nk "Aber keine krummen Sachen, verstanden? Ich weiß, was du für Medikamente nimmst."


"Ich glaube, das war eine Drohung, aber ich bin mir nicht sicher."


stop music fadeout 7.0

scene bg school_nursehall onlayer master
with locationchange

"Egal. Ich versichere Doc, dass meine Absichten durch und durch ehrenhaft sind und verlasse sein Büro."


"Interessant, dass Doc mich als potentiellen Verehrer für Emi sieht."


"Noch interessanter ist, dass mich das so freut."


"Ich brauche eine Dusche."


scene bg school_scienceroom onlayer master
with shorttimeskip

play sound sfx_normalbell

"Die Glocke läutet zur Mittagspause, und ich habe irgendwie keine Lust aufs Dach zu gehen."


"Ich wette, Rin weiß wo Emi ist, und in dem Fall wird sie wohl kaum dort sein."


"Wir hätten wohl auch kaum etwas, worüber wir uns unterhalten könnten, wenn sie da wäre. Wahrscheinlich wäre sie sowieso lieber allein, damit ich nicht aus Versehen ihre Gedankengänge störe oder so was."


"Dummerweise habe ich auch keine große Lust auf die Cafeteria."


"Ich denke, ich gehe stattdessen in die Bibliothek."


"Ich brauche sowieso ein neues Buch, nachdem ich mein anderes gestern vor dem Schlafengehen fertig gelesen habe. Vielleicht finde ich ja mehr von dem gleichen Autor."


scene bg school_library onlayer master
with locationskip

play music music_happiness fadein 2.0

"Ich liebe Bibliotheken."


"Sie riechen nach Staub und Papier und Tinte."


"All die Geschichten und Fakten und Meinungen, die an diesem Ort gesammelt werden, bringen die Atmosphäre zum Knistern."


"Ich weiß noch nicht genau, wie die Bibliothek hier aufgebaut ist. Bisher habe ich hauptsächlich Bücher gelesen, die ich mitgebracht habe, also suche ich nach der Bibliothekarin, um sie um Hilfe zu bitten."


"…"


"Hmm. Sieht aus als wäre sie nicht hi—{w=0.5}{nw}"


show yuuko smile_down onlayer master:
    center
    xpos 0.4
    easein 0.5 center
with charaenter

yu "… kann es einfach nicht fassen."


"Yuuko sieht ziemlich abgelenkt aus, als sie aus einem der Gänge hervorkommt."


hi "Äh, entschuldige."


show yuuko neutral_down onlayer master
with charachange

yu "Oh, kann ich dir helfen?"


hi "Ich suche eigentlich nach einem Buch…"


show yuuko panic_up onlayer master
with charachange

yu "Ich auch!"


show yuuko smile_down onlayer master
with charachange

yu "„Kryptographie für Fortgeschrittene.” Wir haben es gerade erst hereinbekommen, und nun ist es weg."


show yuuko worried_up onlayer master
with charachange

yu "Und ich wollte es sooo gerne lesen!"


hi "Kryptographie?"


show yuuko neurotic_up onlayer master
with charachange

yu "Ja, mein… Äh, das heißt…"


yu "Dieser Kerl, den ich kannte. Kenne. Äh."


yu "Ich weiß nicht, wie ich es sagen soll…"


hi "Spring einfach zum Ende."


show yuuko smile_down onlayer master
with charachange

yu "Er hat mein Interesse für Kryptographie geweckt, aber jetzt ist das Buch weg, und ich glaube es wurde gestohlen!"


hi "Klingt ja furchtbar."


show yuuko worried_up onlayer master
with charachange

yu "Ja, besonders, weil ich nun die ganze Bibliothek danach absuchen muss!"


yu "Obwohl es wahrscheinlich gar nicht mehr hier ist!"


hi "Hört sich an, als wärst du… beschäftigt."


show yuuko neurotic_up onlayer master
with charachange

yu "Etwas."


show yuuko neurotic_up onlayer master:
    center
    easeout 0.5 alpha 0.0 xpos 0.6
with None

"Sie verschwindet in einem anderen Gang, und ich finde mich damit ab, selbst nach meinem Buch suchen zu müssen."


"Hmm, genug Auswahl ist ja da."


stop music fadeout 2.0

hide yuuko onlayer master
with shorttimeskip

"Ach Mann, wo bin ich denn hier gelandet?"


"Das sind nicht mal gedruckte Bücher! Die sind alle in Braille."


"Ist wohl zu erwarten an so einer Schule, aber ehrlich gesagt ist es ein wenig ärgerlich."


li "Tut mir leid, ist da jemand?"


"Eine melodische Stimme kommt aus einer der Arbeitsnischen hinter mir."


show lilly basic_displeased onlayer master at center
with charaenter

"Als ich näher komme, sehe ich, dass Lilly dort ein Buch liest, während ich hier durch die Gänge gestapft bin."


hi "Oh nein, ich sollte mich entschuldigen. Ich wollte nicht so viel Lärm machen."


show lilly basic_ara onlayer master
with charachange

li "Ach, bist du das, Hisao?"


show lilly basic_smile onlayer master
with charachange

li "Ich habe schon länger nichts mehr von dir gehört."


show lilly basic_pout onlayer master
with charachange

li "Ich dachte schon, du hättest mich ganz vergessen."


hi "Äh, tut mir leid."


play music music_lilly fadein 4.0

show lilly basic_giggle onlayer master
with charachange

"Lilly lacht auf ihre kultivierte Art und schüttelt den Kopf."


show lilly basic_smile onlayer master
with charachange

li "Das war nur ein Scherz, Hisao."


li "Nach dem, was ich so höre, warst du sehr beschäftigt."


show lilly basic_cheerful onlayer master
with charachange

li "Frühsport mit Emi Ibarazaki {b}und{/b} Mittagessen auf dem Dach, wenn ich mich nicht irre."


hi "Heh, ja."


hi "Hat sich ganz schön schnell herumgesprochen."


show lilly basic_weaksmile onlayer master
with charachange

li "Das und ich kriege die arme Hanako gar nicht mehr dazu, mit auf das Dach zu kommen."


show lilly basic_displeased onlayer master
with charachange

li "Ihr seid immer dort oben und nehmt den Platz für euch in Anspruch."


"Sie tadelt mich sachte, aber es ist ziemlich offensichtlich, dass sie mich nur wieder aufziehen will."


"Trotzdem habe ich irgendwie das Bedürfnis, mich zu entschuldigen."


hi "Tut mir leid, wir könnten woanders zu Mittag essen, wenn das ein Problem-"


show lilly basic_ara onlayer master
with charachange

li "Oh nein, mach dir keine Gedanken."


show lilly basic_smile onlayer master
with charachange

li "Hanako und ich haben auch noch andere Dinge, die wir in der Mittagspause tun können."


li "Zum Beispiel hier in der Bibliothek lesen, wie du siehst."


hi "Oh, Hanako ist auch hier? Ich habe sie gar nicht gesehen."


show lilly basic_smileclosed onlayer master
with charachange

"Lilly lächelt geheimnisvoll."


li "Oh, sie ist hier irgendwo."


show lilly basic_smile onlayer master
with charachange

li "Aber ich bin überrascht, Hisao. Du bist hier und nicht auf dem Dach."


li "Was führt dich in die Bibliothek?"


hi "Na ja, Emi ist krank, also fällt das Mittagessen auf dem Dach flach…"


show lilly basic_giggle onlayer master
with charachange

"Lilly hebt eine Augenbraue bei meiner Erklärung, dann kichert sie wieder."


li "Ach, die arme Rin muss sich ja richtig außen vor fühlen."


hi "So ist es nicht!"


show lilly basic_weaksmile onlayer master
with charachange

li "Da bin ich mir sicher. Emi bringt immer Leben in alle Gruppen, in denen sie ist."


show lilly basic_sad onlayer master
with charachange

li "Es tut mir leid zu hören, dass sie krank ist. Wie geht es ihr denn?"


"Irgendwie habe ich das Gefühl, dass Lilly nur aus Höflichkeit nachfragt, aber ich antworte trotzdem."


hi "Doc sagt, das wird wieder. Ich gehe nach der Schule mal bei ihr vorbei und schaue selbst, wie es ihr geht."


show lilly basic_smileclosed onlayer master
with charachange

"Noch eine gehobene Augenbraue."


li "Nein, was für ein Gentleman du bist, Hisao."


hi "Nicht der Rede wert, wirklich. Ich sehe schließlich nur nach einer kranken Freundin."


show lilly basic_planned onlayer master
with charachange

li "Ah, also nur Freunde? Wie schade."


"Ich werde rot, und bin froh, dass Lilly es nicht sehen kann."


show lilly basic_giggle onlayer master
with charachange

"Aber irgendwie merkt sie trotzdem, dass ihr Kommentar mich aus dem Konzept gebracht hat. Sie lacht."


li "Tut mir leid, Hisao. Ich nehme dich schon wieder auf den Arm."


show lilly basic_smile onlayer master
with charachange

li "Sag Emi bitte, dass ich ihr Gute Besserung wünsche, in Ordnung?"


"Ein Blick auf meine Uhr verrät mir, dass ich fast keine Zeit mehr habe, mein Buch zu finden."


hi "Natürlich."


hi "Also… Ich muss noch ein Buch finden, bevor die Mittagspause vorbei ist, also sollte ich mich besser beeilen."


hi "Wir sehen uns später."


"Das hätte ich vielleicht glücklicher formulieren können."


"Aber Lilly geht nicht auf meinen Fauxpas ein."


show lilly basic_weaksmile onlayer master
with charachange

stop music fadeout 3.0

li "Bis zum nächsten Mal, Hisao."


scene bg school_hallway2 onlayer master
with shorttimeskip

"Ich finde das Buch, das ich gesucht hatte, nicht mehr und leihe mir stattdessen ein anderes aus."


"Mein Magen knurrt ein wenig, um mich zu erinnern, dass ich etwas hätte essen sollen."


"Na ja."


"Ich hole mir nachher was, bevor ich Emi besuche."



label de_E13:

scene bg school_hallway2 onlayer master
with None

scene bg school_scienceroom onlayer master
with shorttimeskip

play music music_normal fadein 3.0

"Es kommt mir vor, als hätte die Zeit beschlossen, langsamer zu laufen – nur um mich zu ärgern."


"Der Unterricht scheint mir ewig lang zu sein."


"Ich vermute, dass das etwas damit zu tun hat, dass ich mir solche Sorgen um Emi mache."


play sound sfx_normalbell

"Zum Glück läutet endlich die Glocke, und ich stürze aus der Klasse – was sicherlich für einige hochgezogene Augenbrauen sorgt."


scene bg school_hallway3 onlayer master
with locationchange

"Ich habe mir den ganzen Tag Mühe gegeben, meine Anspannung zu verbergen."


"Auch wenn Doc denkt, dass Emi okay ist, will ich es mit eigenen Augen sehen."


stop music fadeout 14.0

scene bg school_girlsdormhall onlayer master
with locationskip

"Es dauert nicht lange, das Mädchenwohnheim zu erreichen, und ich gehe zu Emis Zimmer."


"Als ich vor ihrer Tür stehe, halte ich inne. Was, wenn sie schläft?"


"Ich will sie nicht aufwecken, gerade wenn sie noch krank ist."


"Allerdings… Wenn sie den ganzen Tag schläft, bringt das ihren ganzen Schlafrhythmus durcheinander."


"Aber Ruhe ist wichtig, wenn man krank ist, oder?"


"Ich kann mich nicht entscheiden, was ich tun soll, also stehe ich vor der Tür herum und sehe aus wie ein Idiot."


"Dann höre ich Emis Stimme durch die Tür."


emi "Nett, dass du dir Sorgen machst, aber mir geht es wirklich gut."


"Redet sie mit mir?"


emi "Wir sehen uns ja dann morgen im Training!"


"Wohl eher nicht."


"Jedenfalls schläft sie offensichtlich nicht, also kann ich beruhigt klopfen."


"Was soll also dieses verkrampfte Gefühl in meinem Magen? Das letzte Mal war ich doch auch nicht nervös, als ich hier war, also warum heute?"


"Na ja, ich hatte immer noch keine wirkliche Gelegenheit, herauszufinden, warum mir Emis Gesundheit plötzlich so am Herzen liegt."


"Ich habe damit ja nicht so viel Erfahrung, aber das scheint mir doch etwas über normale, freundschaftliche Gefühle hinauszugehen."


"Aber könnte ich diesen Schritt gehen? Würde ich es wagen, das was ich jetzt habe aufs Spiel zu setzen?"


"Ich meine… Es ist doch genug, mit ihr befreundet zu sein, oder nicht?"


"Auf jeden Fall sollte ich einfach die Tür öffnen und schauen, wie es ihr geht. Deswegen bin ich schließlich hier… Oder?"


stop music fadeout 1.5

"Und wenn sie noch nicht angezogen ist?"


play ambient sfx_heartslow
with Fade (0.05, 0.0, 0.3, color="#ffc0cb")

"Das Bild schießt mir durch den Kopf, und mein Herz setzt buchstäblich einen Schlag aus."


stop ambient fadeout 3.0

"Ich sollte solche Gedanken wahrscheinlich nie wieder denken, wenn ich einen weiteren Herzanfall vermeiden will."


"Mir fällt plötzlich auf, dass ich immer noch wie ein Idiot im Gang stehe."


play sound sfx_doorknock2

"Emi scheint immer noch mitten im Gespräch zu sein, aber ich klopfe trotzdem. Hoffentlich stört sie die Unterbrechung nicht."


emi "Du machst dir zu viele Ge- Herein! Die Tür ist offen."


"Das ist sie wirklich. Ich öffne die Tür und betrete das Zimmer, und an dieser Stelle machen meine Gedanken eine abrupte Vollbremsung."


play music music_serene fadein 4.0

scene ev emi_sleepy_face onlayer master:
    subpixel True
    center
    zoom 1.05
    ease 15.0 zoom 1.0
with whiteout

"Emi sitzt auf ihrem Bett, die Haare wirr, weil sie den ganzen Tag geschlafen hat. Ich glaube, das ist das erste Mal, dass ich sie ohne die gewohnten Perlen in ihrem Haar sehe."


"Ihr T-Shirt und die Sporthosen, die sie offenbar hastig angezogen hat, bevor ich hereingekommen bin, sind ganz zerknittert. Anscheinend hat sie sie nicht sehr ordentlich aufbewahrt."


scene ev emi_sleepy_legs onlayer master at Fullpan(8.0)
with flash

"Ihre Beine liegen unbedeckt auf dem Bettlaken."


"Ich habe Emi noch nie ohne ihre Prothesen gesehen. Aber hier ist sie, und ihre schlanken Beine enden knapp unterhalb der Knie."


"Aber so seltsam der Anblick auch ist, wird mein Blick doch eher von dem angezogen, was sich nördlich der Taille befindet."


scene ev emi_sleepy onlayer master:
    subpixel True
    center
    zoom 1.05
    ease 15.0 zoom 1.0
with flash

"Wie es scheint, hat Emi ihr Telefonat beendet und beobachtet nun genau meine Reaktion mit ihrem geöffneten Auge, während sie sich den Schlaf aus dem anderen reibt."


"Sie wirkt überhaupt nicht verlegen und gähnt ungeniert. Ich bin überrascht, wie weit sich so ein kleiner Mund öffnen kann."



"Als sie mich betrachtet, spielt einen kurzen Moment lang ein fast schon flirtendes Grinsen um ihre Mundwinkel."


"Ich kann nichts tun, außer zwischen Furcht, Verwirrung und einer gehörigen Portion Lust zu schwanken."


"Emi schiebt sich hastig die Haare aus den Augen und stellt ihre gewohnte Frisur wieder her, bevor sie sich mir zuwendet."


scene bg school_dormemi onlayer master
show emi sad_grin_gym onlayer master at center
with locationchange

emi "Du wirkst etwas überrascht, Hisao."


"Sie lacht mich an, und ich grinse zurück und kratze mich verlegen am Hinterkopf."


hi "Tut mir leid, ich habe…"


"Nur noch nie jemanden gesehen, der so zerzaust und trotzdem so attraktiv ist."


"Dich nur noch nie ohne deine Beine gesehen."


"Dich noch nie so…"


hi "Äh, tut mir leid."


show emi basic_closedgrin_gym onlayer master
with charachange

"Emi kichert wieder und setzt sich ein wenig aufrechter hin."


"Ich verliere mich beinahe in den Bewegungen ihres T-Shirts."


show emi basic_grin_gym onlayer master
with charachange

emi "Ich habe mich gefragt, wie du reagieren würdest."


show emi basic_closedhappy_gym onlayer master
with charachange

emi "Doc hat mich angerufen und mir erzählt, dass du vorbeikommen würdest."


show emi basic_grin_gym onlayer master
with charachange

emi "Und da ich weiß, dass du mich noch nie ohne… Na ja, du weißt schon."


show emi sad_grin_gym onlayer master
with charachange

emi "Ohne Beine gesehen hast."


"Ich antworte wie beiläufig überrascht."


hi "Ach, du hast sie nicht an? Hatte ich gar nicht bemerkt."


"Das ist fast die Wahrheit. Beinahe hätte ich es nicht bemerkt."


"Ich versuche möglichst nicht zu mitfühlend zu klingen. Irgendwie habe ich das Gefühl, dass Emi dann beleidigt wäre."



stop music fadeout 0.5
play sound sfx_pillow
show emi basic_annoyed_gym onlayer master
with vpunch

"Stattdessen streckt sie mir die Zunge heraus und wirft mir ein Kissen an den Kopf."


emi "Esel."


"Ich fange das Kissen geschickt auf und ziele genau, bevor ich es zurückwerfe."


play music music_running

show emi basic_annoyed_gym onlayer master:
    center
    parallel:
        ease 0.5 xpos 0.7
    parallel:
        "emi basic_closedhappy_gym" with Dissolve(0.5, alpha=True)

"Emi lacht und rollt sich zur Seite, um meinem Wurf auszuweichen. Dabei lenkt mich ihr verrutschendes T-Shirt so sehr ab, dass ihr nächster Wurf mich genau zwischen die Augen trifft."


play sound sfx_pillow

hi "Uff!" with hpunch


"Ich werfe natürlich zurück."


"Und nachdem ich nun zweimal zurückgeworfen habe, musste ja früher oder später ein Krieg ausbrechen."


"Und da Emi anscheinend viel besser zielen kann als ich, na ja…"


"Es war nur eine Frage der Zeit, bevor ich außer einem Frontalangriff keine Chance mehr sehe."


show bg school_dormemi onlayer master:
    center
    ease 0.5 bgleft

show emi basic_closedhappy_gym onlayer master:
    ease 0.5 center

with None

show emi basic_closedhappy_gym_close onlayer master:
    ease 0.5 center

with characlose

hi "Hab ich dich!"


show emi basic_hes_gym_close onlayer master
with charachange

emi "Eeh!"


window hide None

play sound sfx_pillow

show comic vfx1 onlayer master
show emi basic_closedsweat_gym_close onlayer master
with vpunch

with Pause(0.5)

play sound sfx_pillow

show comic vfx2 onlayer master
with hpunch

with Pause(0.5)

play sound sfx_pillow

show comic vfx3 onlayer master
with vpunch

with Pause(0.5)

show comic vfx3 onlayer master:
    truecenter
    easeout 0.5 yanchor 0.3 alpha 0.0
with Pause(0.5)







stop music fadeout 3.0

scene black onlayer master
with dissolve

window show

"Und nach dem Frontalangriff… Na ja, da musste ich ihr natürlich das Kissen entringen."


"Und bei so einem Kampf sind wir dann natürlich in dieser Position herausgekommen."


window hide

play music music_twinkle fadein 2.0

scene ev emi_bed_full onlayer master:
    xalign 0.5 yalign 1.0 subpixel True
    easein 15.0 yalign 0.0

with Dissolve(1.0)

with Pause(3.0)

window show

"Und so starre ich nun von meiner Position über ihr auf sie hinab."


"Sie grinst, und ihre Augen funkeln belustigt."


"Sie ist bei unserer Rauferei etwas ins Schwitzen gekommen. Ihre Brustkorb hebt und senkt sich, als sie nach Luft schnappt."


"Der kleine Teil meines Gehirns, der gerade nicht vollkommen von ihrem Anblick und ihrem Geruch gefesselt ist, stellt fest, dass sie immer noch krank sein muss. Normalerweise hätte sie mehr Ausdauer."


"Wir bleiben eine Weile in dieser Position."


"Ich weiß nicht genau wie lange, weil alles um mich herum plötzlich so undeutlich wird. Jedenfalls alles außer ihr."


"Unsere Augen treffen sich und tief in ihrem Inneren erkenne ich… Was? Angst? Verlangen?"


"Hoffnung?"


hi "Emi…?"


stop music fadeout 0.5

show ev emi_bed_unsure onlayer master at center
with vpunch

"Plötzlich wird sie von einem Hustenanfall durchgeschüttelt, und ich falle fast zu Boden in meiner Eile, von ihr herunterzukommen und mich zu entschuldigen."


play music music_emi fadein 3.0

hi "Tut mir leid, ich hätte nicht…"


show ev emi_bed_happy onlayer master
with charachange

emi "Schon gut, schon gut."


"Sie klopft mir beruhigend auf die Schulter."


show ev emi_bed_normal onlayer master
with charachange

emi "Also… Was führt dich hierher?"


"Sie atmet immer noch schwer, und das bringt ihre Stimme leicht zum Zittern."


hi "Na ja, bevor ich so grob mit Kissen attackiert wurde, wollte ich schauen, wie es dir geht."


window hide None

play sound sfx_pillow

show comic vfx4 onlayer master
show ev emi_bed_frown onlayer master
with vpunch

with Pause(0.5)

show comic vfx4 onlayer master:
    truecenter
    easeout 0.5 yanchor 0.3 alpha 0.0
with Pause(0.5)

window show

"Das bringt mir einen weiteren Schubser ein, und ich falle beinahe vom Bett."


show ev emi_bed_normal onlayer master
hide comic onlayer master
with charachange

"Emis Augen leuchten wieder, und ich frage mich, wie mir bisher entgehen konnte, wie attraktiv sie sind."


show ev emi_bed_smile onlayer master
with charachange

emi "Verzehrt von Sorge, nicht wahr?"


"Ihr Ton ist spöttisch, hochmütig. Sie will mich ärgern."


"Sie hält sich dramatisch ihren Arm vor die Stirn, aber darunter ist ihr Grinsen immer noch klar erkennbar."


show ev emi_bed_unsure onlayer master
with charachange

emi "Du konntest den Gedanken nicht ertragen, dass ich hier todkrank liege."


"Während wir uns beide von unserer kurzen Rauferei erholen, fängt Emi schon wieder an, mich aufzuziehen."


hi "Na ja, ich würde nicht sagen, dass ich mich vor Sorge verzehrt habe, aber als du Memme heute Morgen einfach nicht aufgetaucht bist…"


show ev emi_bed_frown onlayer master
with charachange

"Emi schmollt, verschränkt die Arme vor ihrer Brust und streckt die Unterlippe vor."


emi "Nicht meine Schuld."


emi "Doc hat mich nicht gelassen."


hi "Klar hat er das nicht. Das glaube ich dir sofort."


"Emi streckt mir wieder die Zunge heraus."


emi "Du bist so ein Idiot, Hisao."


hi "Also, wie war dein Tag, hm? Hast du es genossen, mal auf der faulen Haut zu liegen?"


show ev emi_bed_normal onlayer master
with charachange

emi "Nicht wirklich. Das Telefon hat mich ziemlich früh geweckt."


hi "Das Telefon?"


emi "Ja, der Teamkapitän hat angerufen, um zu fragen, wie es mir geht."


emi "Und um mir zu sagen, dass ich heute nicht zum Training kommen muss."


"Gut, zumindest war sie nicht den ganzen Tag allein. Jemand hat nach ihr gesehen."


"Obwohl ich mich des Gedankens nicht erwehren kann, dass ich das hätte sein sollen."


hi "Oh, das ist gut."


hi "Er passt wirklich gut auf dich auf, hm?"


show ev emi_bed_smile onlayer master
with charachange

"Emi zuckt mit den Schultern."


emi "Das ist sein Job."


emi "Wenn man Teamkapitän ist, muss man wissen, wo die anderen Teammitglieder sind, wenn sie nicht in der Schule sind."


emi "Trotzdem war es nett, dass er angerufen hat, oder?"


hi "Ja, das war es."


"Emi gähnt und rutscht in eine etwas bequemere Position."


show ev emi_bed_normal onlayer master
with charachange

emi "Also, wie war dein Tag?"


hi "Ziemlich ereignislos."


hi "Ich bin heute Morgen allein gelaufen, und habe dann mit Doc darüber gesprochen, wie es dir geht…"


stop music fadeout 2.0

scene bg school_dormemi_ni onlayer master
with shorttimeskip

"Ich erzähle von meinem Tag; nichts davon ist wirklich interessant."


"Dann werde ich von einem Arm abgelenkt, der plötzlich auf meiner Hüfte liegt."


"Sieht so aus, als wäre Emi eingeschlafen, während ich geredet habe, also ziehe ich die Decke über uns."


play music music_comfort fadein 9.0

scene ev emi_sleep_unsure onlayer master
with locationchange

"Sie ist auf ihre Seite gerollt, und nun liegt eines ihrer Beine quer über meinen Beinen, sodass ich effektiv gefangen bin."


hi "Hey."


"Es wäre eine Schande, sie aufzuwecken, aber ich muss noch einige Dinge erledigen."


play sound sfx_rustling

"Ich schüttele sie sanft, aber ihre einzige Reaktion ist ein leises Seufzen, und ihr Arm greift noch etwas fester zu."


"Mein Widerstand bricht relativ schnell zusammen."


"Das Gefühl ihres gleichmäßig atmenden Körpers ist gleichzeitig beruhigend und unglaublich erregend."


"Mein Atem kann sich nicht entscheiden, ob er sich beruhigen oder schneller werden soll."


"Die Entspannung siegt, und ich lege stattdessen auch meinen Arm um Emi."


scene ev emi_sleep_normal onlayer master
with dissolve

hi "Ich glaube, ich bin verliebt."


"Die Worte rutschen mir einfach so heraus und hängen ungehört im Raum."


"Zumindest hoffe ich, dass sie ungehört geblieben sind."


scene ev emi_sleep_weep onlayer master
with dissolve

"Emi wimmert schwach in ihrem Traum, und ihr Griff verkrampft sich plötzlich."


"Zum ersten Mal, seit ich sie kenne, sehe ich Tränen über Emis Gesicht laufen."


"Mein Herz fühlt sich an, als würde es jeden Moment brechen."


"Ich halte sie instinktiv fester und streiche über ihre Haare, in der Hoffnung, dass das beruhigend wirkt."


"Tröstende Worte – bedeutungslos in dieser Situation – schießen mir durch den Kopf."


"Vielleicht sollte ich sie aufwecken. Soll man Leute aufwecken, die einen Alptraum haben?"


"Ich kann mich beim besten Willen nicht erinnern."


"Die Entscheidung wird mir abgenommen, als Emi plötzlich mit einem Schrei aufschreckt."


scene ev emi_sleep_cry onlayer master
with dissolve

emi "Papa!"


"Das ist… mehr, als ich ohne ihr Wissen hören will. Ich setze mich schnell auf und schüttele sie sanft an der Schulter."


scene bg school_dormemi_ni onlayer master
with locationchange

hi "Hey, alles okay?"


"Dumme Frage."


show emi basic_shock_gym_close_ni onlayer master at tworight
with charaenter

emi "Hä? Was?"


show emi basic_hes_gym_close_ni onlayer master
with charachange

emi "Hisao?"


"Sie schüttelt den Kopf, als ob sie die Erinnerung verreiben will und wischt sich schnell die Tränen aus den Augen."


hi "Du hattest einen Alptraum. Glaube ich."


show emi sad_shy_gym_close_ni onlayer master
with charachange

"Emi schaudert und schaut mich ein wenig unsicher an, als ob sie sich nicht sicher wäre, ob sie wirklich wach ist."


emi "J-Ja, scheint so."


hi "Willst du drüber reden?"


emi "Hm?"


"In ihrem Kopf scheint eine kurze Debatte abzulaufen, die in einem Schulterzucken endet."


show emi basic_hes_gym_close_ni onlayer master
with charachange

emi "Nö, ich kann mich kaum daran erinnern."


"Ich bin mir ziemlich sicher, dass sie mich anlügt, aber irgendwie glaube ich, ich sollte die Sache ruhen lassen."


show emi sad_shyblush_gym_close_ni onlayer master
with charachange

"Emi schaudert wieder und wendet sich mir zu. Sie sieht ein wenig verlegen aus."


emi "Tut mir leid, dass ich einfach so eingeschlafen bin."


"Ich halte meine Stimme so beruhigend wie möglich."


hi "Hey, keine Sorge. Du bist schließlich krank."


emi "Ja, wahrscheinlich hat mich nur die Medizin etwas schläfrig gemacht."


hi "Wahrscheinlich."


"Emi scheint mir niemand zu sein, der sonst einfach so einschlafen würde."


"Rin vielleicht, aber Emi ist dafür viel zu energiegeladen."


show emi basic_grin_gym_close_ni onlayer master
with charachange

"Emi lächelt über meine Antwort, und dann ist sie übergangslos wieder die alte."


show emi basic_closedgrin_gym_close_ni onlayer master
with charachange

emi "Na ja, dann bereite dich schon mal auf morgen früh vor, Hisao!"


show emi excited_proud_gym_close_ni onlayer master
with charachange

emi "Wir müssen uns morgen doppelt so sehr anstrengen, um den heutigen Tag wieder wettzumachen."


hi "Aber ich bin heute Morgen gelaufen!"


show emi basic_annoyed_gym_close_ni onlayer master
with charachange

emi "Das ist keine Entschuldigung!"


hi "Na gut, ich werde vorbereitet sein!"


show emi basic_grin_gym_close_ni onlayer master
with charachange

"Emi nickt zufrieden."


emi "Gut."


"Ich nehme das als Gelegenheit, mich zu verabschieden."


hi "Na ja, ich gehe dann besser. Besonders wenn ich bis morgen noch genug Schlaf kriegen will."


show emi basic_grin_gym_ni onlayer master
with vpunch

"Ich verlasse das Bett und gehe zur Tür."


show emi sad_shy_gym_ni onlayer master
with charachange

emi "Hey, Hisao…"


hi "Hmm?"


"Ich drehe mich auf dem Absatz um und schaue Emi an."


show emi basic_hes_gym_ni onlayer master
with charachange

"Sie öffnet ihren Mund, um etwas zu sagen, aber zum ersten Mal sehe ich sie zögern."


"Sie schließt ihren Mund und öffnet ihn wieder."


show emi sad_grin_gym_ni onlayer master
with charachange

emi "… Danke."


emi "Dass du vorbeigekommen bist, meine ich."


emi "Du bist der erste Besucher, den ich je hatte – außer Rin."


"Das überrascht mich. Ich hätte gedacht, dass Emi andauernd Besuch kriegen würde."


"Sie ist jedenfalls beliebt genug… dachte ich zumindest. Sie redet immer mit anderen Schülern in den Gängen."


show emi sad_shy_gym_ni onlayer master
with charachange

"Emi zögert wieder."


emi "Und danke, dass du geblieben bist, nachdem ich… Na ja…"


show emi sad_depressed_gym_ni onlayer master
with charachange

"Ein Schatten huscht über ihr Gesicht."


emi "Du weißt schon."


show emi sad_grin_gym_ni onlayer master
with charachange

emi "Es hat geholfen."


show emi basic_closedgrin_gym_ni onlayer master
with charachange

"Ihre Miene hellt sich wieder auf, und sie winkt mir fröhlich zu."


emi "Bis morgen dann!"


hi "Ja, bis morgen."


"Ich will gerade zur Tür hinaus, als mich irgendetwas dazu bringt, mich noch einmal umzudrehen."


hi "Hey, Emi."


show emi basic_grin_gym_ni onlayer master
with charachange

emi "Hmm?"


hi "Wann immer du reden möchtest, komm zu mir, okay?"


show emi sad_shy_gym_ni onlayer master
with charachange

"Emi scheint von dem Angebot überrascht zu sein."


show emi basic_closedgrin_gym_ni onlayer master
with charachange

"Ihr Grinsen wird noch breiter."


emi "Klare Sache, Hisao."


show emi basic_grin_gym_ni onlayer master
with charachange

emi "Man sieht sich dann morgen früh!"


scene bg school_girlsdormhall_ni onlayer master
with locationchange

"Ich verlasse Emis Zimmer; meine Gedanken sind in Aufruhr."


"War es in Ordnung zu gehen?"


"Ging es ihr wirklich gut?"


"Ich will mich umdrehen und zurückgehen, die Tür öffnen und ihr sagen…"


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

nvl clear

nvl show dissolve

n "\n\nIhr sagen, dass ich sie liebe, ihr sagen, dass sie wunderschön ist, ihr sagen, dass ich für sie da sein werde, wenn sie mich braucht."


n "Ich will bei ihr bleiben und sie festhalten, wenn sie wieder einschläft."


n "Wie viele Nächte ist sie so aufgewacht?"


n "Nur um zu merken, dass niemand da ist."


n "Ich will derjenige sein, der bei ihr ist, wenn das passiert."


n "Ich weiß, dass das ein dummer Gedanke ist."


n "Wir kennen uns nicht einmal so gut, oder?"


n "Der Gedanke ist zwar berauschend, aber er macht mir auch ein wenig Angst."


n "Angst, dass ich zu weit gehen könnte."


n "Und als ob ich nicht schon genug Sorgen hätte, scheint es, als wäre Emi schon an jemand anderem interessiert."


nvl clear

n "\n\n\n\n\n\nDieser Teamkapitän, der sich so um ihr Wohlergehen zu sorgen scheint."


n "Ja, ich habe die beiden nur ein paar Mal zusammen gesehen, aber das ändert nichts daran, dass sie besser zueinander zu passen scheinen."


n "Da kann man nichts machen."


n "Ich muss irgendwie auf andere Gedanken kommen."


$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl clear
nvl hide dissolve

window show

"Ich habe noch Hausaufgaben."


"Vielleicht lenkt mich das ein wenig ab."


stop music fadeout 2.0

$ suppress_window_after_timeskip = True

scene black onlayer master
with dissolve


label de_E14:

window hide None

scene black onlayer master
with dissolve

scene bg school_dormhisao onlayer master
with openeye

window show

"Nach einer schlaflosen Nacht bin ich heute Morgen ziemlich erschöpft."


play music music_drama fadein 8.0

"Die gestrigen Ereignisse haben mich die ganze Nacht wachgehalten."


"Die Erinnerung daran, wie Emi neben mir lag."


"Die Erinnerung an unsere Rauferei."


"Und am Schlimmsten: Die Erinnerung an ihren Alptraum."


"Ich konnte ihren Schmerz geradezu spüren."


"Ich frage mich immer wieder, wie es für sie sein muss, allein aufzuwachen."


scene bg school_dormbathroom onlayer master
show steam onlayer master
with locationskip

play ambient sfx_shower fadein 1.0

"Das heiße Wasser der Dusche versetzt mir einen Schock. Jetzt bin ich zwar wach, Sorgen mache ich mir aber immer noch."


$ renpy.music.set_volume(0.5, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

nvl show dissolve
nvl clear

n "\nWas wird heute passieren?"


n "Wird wieder alles so sein wie immer?"


n "Kapitel beendet, zurück zum Status Quo?"


n "Gestern war da etwas. Etwas, das uns fast die Grenzen einer normalen Freundschaft hätte überwinden lassen."


n "Wäre das so schlimm gewesen?"


n "Ich erinnere mich an Emis Gesichtsausdruck nach unserer Kissenschlacht. Es war fast, als wollte sie mich herausfordern, weiterzumachen."


n "Fast."


n "Aber sicher kann ich mir nicht sein."


n "Außerdem steht dieser Teamkapitän bei ihr sicher an erster Stelle."


n "Aber schon als ich den Gedanken fasse, erkennt mein Unterbewusstsein ihn als das, was er ist: Eine Ausrede. Ein Grund, warum es schiefgehen könnte."


n "Ein Grund, es nicht zu versuchen."


nvl clear

n "\n\n\n\nEs ist ja nicht so, als hätte ich die beiden jemals außerhalb des Trainings zusammen gesehen."


n "Und offensichtlich hat er sie noch nie besucht. Das hat Emi selbst gesagt. Wenn sie sich nahe stehen würden, würde er sie doch sicher mal besuchen."


n "Ich bin so ein Waschlappen."


n "Ich sollte es einfach versuchen, und auf die Konsequenzen pfeifen."


n "Ich denke, Emi würde es genauso machen. Verdammt, ich {b}weiß{/b}, dass sie es genauso machen würde."


n "Was auch ein Grund ist, warum ich überzeugt bin, dass sie kein Interesse an mir hat. Sie hat ebenfalls nichts gesagt."


n "Vielleicht wegen dieses Teamkapitäns. Vielleicht ist sie ja unglücklich in ihn verliebt."


nvl clear

n "\n\n\n\n\n\nAber wer könnte mir etwas über ihr Verhältnis sagen?"


n "Sicher nicht Emi. Sie würde wahrscheinlich nur lachen und fragen, warum ich das wissen will… und für diese Frage bin ich noch nicht bereit."


n "Rin… Rin würde mir wahrscheinlich nur irgendeine kryptische Antwort geben. Und bei meinem Glück würde sie dann einfach Emi fragen, die wiederum mich fragen würde, warum ich das wissen will, und das Problem hatten wir ja schon mal."


n "Ich frage mich…"


nvl clear

n "\n\n\n\n\nKönnte ich vielleicht Doc fragen? Er scheint sich ja sehr um Emi zu kümmern. Ich bin mir sicher, er wüsste, wenn da was im Busch wäre…"


n "Und er schuldet mir was, weil ich Emi nicht erzählt habe, dass er vergessen hat, mir von ihrer Krankheit zu erzählen, also wird er nichts sagen."


n "Aber was, wenn er mich fragt, warum ich das wissen will?"


n "Ich werde ihn schon abwimmeln können. Ich sage einfach, dass ich neugierig bin – einfach so. Das wird er mir doch glauben, oder?"


n "Natürlich!"


n "Damit wäre das geklärt."


n "Nach dem Training werde ich ihn fragen, während Emi vor seinem Büro wartet."


stop ambient fadeout 2.0

nvl clear
nvl hide dissolve

scene bg school_track onlayer master
with locationskip

nvl show dissolve

n "\n\n\n\nAls ich am Sportplatz ankomme, ist von Emi keine Spur zu sehen. Ist sie immer noch krank?"


n "Ich beschließe, ihr noch zehn Minuten zu geben."


n "Ich bin ein bisschen früh, und sie war gestern krank, also sollte es mich nicht wundern, wenn es noch einen Moment dauert, bis sie auftaucht."


n "Trotzdem will ich meine Zeit nicht einfach verschwenden. Ich beschäftige mich mit Aufwärmübungen und laufe ein wenig nervös auf und ab."


n "Was, wenn ich gestern zu weit gegangen bin?"


n "Was, wenn sie nicht kommt, weil sie sich schämt?"


n "Was, wenn…"


$ renpy.music.set_volume(1.0, 2.0, channel="music")
$ renpy.music.set_volume(1.0, 2.0, channel="ambient")

nvl clear

stop music fadeout 2.0

nvl hide dissolve

window show

show emi basic_closedgrin_gym onlayer master at center
with charaenter

emi "Du bist wieder früh dran, Hisao!"


show emi excited_proud_gym onlayer master
with charachange

emi "Ich bin beeindruckt!"


"Von einem Moment auf den anderen fühle ich, wie meine Anspannung nachlässt."


"Emi scheint genauso lebhaft und fröhlich zu sein wie immer – keine Anzeichen, dass sie gestern krank gewesen ist oder gar schlecht geschlafen hat."


"Trotzdem muss ich fragen."


hi "Gut geschlafen heute Nacht?"


play music music_serene

"Eine einfache Frage. Smalltalk."


"Die Art von Frage, die man Leuten stellt, die man zufällig beim Morgenkaffee in der Cafeteria trifft."


"Aber nicht für uns. Zumindest nicht für mich."


"Ich weiß nicht, ob Emi bewusst ist, dass ich wirklich besorgt bin, ob sie gut geschlafen hat, aber sie zögert mit der Antwort."


show emi basic_grin_gym onlayer master
with charachange

"Nachdem sie anscheinend einen Moment lang ernsthaft über die Frage nachgedacht hat, nickt sie."


show emi basic_closedhappy_gym onlayer master
with charachange

emi "Japp! Hab ich!"


"Meinetwegen?"


"Konnte ich wirklich helfen?"


"Oder sagst du das nur, damit ich aufhöre, solche Fragen zu stellen?"


hi "Gut zu hören."


show emi basic_closedgrin_gym onlayer master
with charachange

"Emi grinst und fängt an, sich aufzuwärmen."


show emi basic_grin_gym onlayer master
with charachange

emi "Also, bist du bereit?"


hi "Pah, ob ich bereit bin? Natürlich bin ich bereit! Ich bin bereit geboren worden!"


show emi basic_closedhappy_gym onlayer master
with charachange

"Emi lacht über meine Angeberei, und wir laufen los."


scene bg school_track_running onlayer master
with shorttimeskip

"Ich halte die ganze Zeit eine konstante Geschwindigkeit durch und atme ruhig."


scene bg school_track_on onlayer master
with Dissolve(2.0)

"Danach fühle ich mich zwar trotzdem wie erschlagen, aber zumindest schnappe ich nicht mehr nach Luft wie ein Fisch auf dem Trockenen."


show emi basic_happy_gym onlayer master:
    center
    xpos 0.6
    easein 0.5 center
with charaenter

"Emi strahlt mich nach dem Lauf richtig an."


emi "Gut gemacht, Hisao! Du wirst besser!"


show emi basic_closedgrin_gym onlayer master
with charachange

emi "Du bist bald schon halb so schnell wie ich!"


"Beim letzten Satz schenkt sie mir ein neckisches Grinsen, wie ich es inzwischen von ihr gewohnt bin."


hi "Oh, wie aufregend."


play ambient sfx_emisprinting

$ renpy.music.set_volume(0.3,1.0,channel="ambient")

hide emi onlayer master
with easeoutleft

"Emi fängt mit ihren Sprints an, während ich auf meiner Abkühlrunde bin."


"Sie strengt sich heute wirklich besonders an."


stop ambient fadeout 1.0

scene bg school_track onlayer master
with shorttimeskip

$ renpy.music.set_volume(1.0,0.0,channel="ambient")

"Als ich mit meiner Runde fertig bin, liegt sie erschöpft auf einer Bank auf der Tribüne."


hi "Meine Güte, ich hoffe, du hast dich heute nicht zu sehr angestrengt."


hi "Du hattest gerade eine Erkältung, falls du dich erinnerst."


show emi basic_annoyed_gym onlayer master at center
with charaenter

"Emi rümpft verärgert die Nase und setzt sich auf."


emi "Bah! Ich versuche nur, die verlorene Zeit wieder reinzuholen, das ist alles."


show emi excited_happy_gym onlayer master
with charachange

emi "Ich habe mir heute doppelt so viel Mühe gegeben."


show emi excited_laugh_gym onlayer master
with charachange

emi "Es geht nichts über ein gutes Training, um sich wieder auf Vordermann zu bringen."


show emi basic_closedgrin_gym onlayer master
with charachange

emi "Man kriegt auch den Kopf wieder klar."


hi "Ja?"


show emi excited_happy_gym onlayer master
with charachange

"Emi nickt lebhaft."


show emi excited_amused_gym onlayer master
with charachange

emi "Jepp! Es ist auch ein gutes Ventil für andere Dinge."


"Sie geht nicht näher auf ihre letzte Bemerkung ein, und ich frage auch nicht weiter."


"Ich kann mir den wahren Grund denken, warum sie sich heute so angestrengt hat."


"Es hatte nichts damit zu tun, dass sie krank war. Irgendetwas bedrückt sie."


"Vielleicht der Alptraum. Vielleicht etwas anderes."


"Aber ich habe kein Recht herumzuschnüffeln."


"Wenn sie es mir erzählen will, wird sie es mir erzählen."


hi "Das ist sicher sehr praktisch."


show emi basic_grin_gym onlayer master
with charachange

emi "Da kannst du Gift drauf nehmen."


"Die Ernsthaftigkeit in ihrer Stimme bestätigt meine Vermutungen."


"Das einzige Problem ist…"


"Obwohl ich weiß, dass sie es mir sagen würde, wenn sie wollte, möchte ich es doch wissen."


hi "Also bedrückt dich irgendwas?"


"Emi scheint von meiner Frage nicht überrascht zu sein."


show emi basic_closedgrin_gym onlayer master
with charachange

"Stattdessen zuckt sie mit den Schultern."


show emi sad_grin_gym onlayer master
with charachange

emi "Nö, nichts, worüber man sich Sorgen machen müsste."


"Es scheint, als würde sie sich selbst ebenso davon überzeugen wollen wie mich."


"Ich öffne den Mund, um zu fragen, ob Gestern für ihre Sorgen verantwortlich ist, aber ich überlege es mir anders."


"Das Risiko, dass sie die Frage falsch versteht, ist zu groß."


"Außerdem bin ich mir selbst nicht sicher, was ich von dem halten soll, was gestern passiert ist."


"Ich komme einfach nur bis zu dem Punkt, wo Emi neben mir eingeschlafen ist und wie sich das angefühlt hat, bevor mein Gehirn abschaltet."


"Auch jetzt, wo sie schweißgebadet vor mir steht und mich schief anlächelt, fällt mir das Denken schwer."


hi "Wenn du es sagst."


show emi basic_hes_gym onlayer master
with charachange

emi "Wir sollten uns beeilen, zu Doc zu kommen. Wir sind spät dran."


hi "Sind wir das nicht immer?"


show emi basic_grin_gym onlayer master
with charachange

"Emi lacht – ein trockenes Kichern, dass sich so gar nicht nach ihr anhört."


show emi sad_grin_gym onlayer master
with charachange

emi "Wie wahr."


"Einen Augenblick lang sieht sie alt aus, wie von alten Schmerzen gebeugt."


"Aber genau wie gestern kann ich beinahe sehen, wie sie ihre Last schultert und sich ein wenig gerader hinsetzt."


"Und dann ist sie wieder Emi."


show emi excited_proud_gym onlayer master
with charachange

emi "Komm schon, Hisao. Wer zuerst da ist!"


play ambient sfx_emisprinting

hide emi onlayer master
with easeoutleft

stop ambient fadeout 2.0

"Plötzlich grinst sie und sprintet los."


hi "Hey! Unfair!"


"Ich renne ihr hinterher. Ich weiß, dass ich sie nicht einholen kann, aber das ist mir egal."


"Auch wenn ich keine Chance habe, sie zu fangen, werde ich ihr trotzdem hinterherlaufen."


stop music fadeout 2.0

scene bg school_nursehall onlayer master
show emi basic_grin_gym onlayer master at center
with locationskip

"Emi wartet schon an der Tür auf mich, als ich ankomme."


show emi basic_closedhappy_gym onlayer master
with charachange

emi "Sieh da, wer endlich auch auftaucht!"


hi "Ja, ja."


hi "Genieß deinen Sieg solange du kannst."


show emi basic_closedgrin_gym onlayer master
with charachange

"Während Emi mich angrinst, streckt Doc seinen Kopf aus der Tür."


show nurse neutral onlayer master:
    center
    xpos 0.0 xanchor 0.5
    easein 0.5 xpos 0.1
with charaenter

nk "Ah, da seid ihr ja."


nk "Komm 'rein, Hisao."


play music music_nurse fadein 1.0

scene bg school_nurseoffice onlayer master
show nurse neutral onlayer master at center
with locationchange

"Das Programm ist inzwischen schon Routine: Er misst meinen Blutdruck und meinen Puls."


show nurse fabulous onlayer master
with charachange

nk "Etwas schnell heute, oder?"


hi "Ja, ich bin auf dem Weg hierher mit Emi um die Wette gelaufen."


show nurse grin onlayer master
with charachange

"Doc lacht."


nk "Das ist nie eine gute Idee!"


show nurse neutral_close onlayer master
with characlose

"Er beugt sich zu mir herunter und flüstert mir verschwörerisch zu."


show nurse fabulous_close onlayer master
with characlose

nk "Ich weiß nicht, ob du schon davon gehört hast… aber Emi ist der Star der Leichtathletikmannschaft."


show nurse fabulous onlayer master
with vpunch

"Ich weiche mit gespielter Überraschung zurück."


hi "Wirklich? Das hat sie nie erwähnt!"


show nurse grin onlayer master
with charachange

"Wir lachen zusammen."


show nurse neutral onlayer master
with charachange

nk "Ging es ihr heute besser?"


nk "Hat ihr die Erkältung noch zu schaffen gemacht?"


hi "Warum fragen Sie sie nicht selbst?"


show nurse concern onlayer master
with charachange

"Er rollt frustriert die Augen."


nk "Natürlich werde ich sie auch fragen, aber sie wird mir sagen, dass sie keine Probleme hatte, egal ob sie welche hatte oder nicht."


show nurse fabulous onlayer master
with charachange

nk "Deshalb frage ich dich, weil du ihr Freund bist und es mir wahrscheinlich sagen würdest, wenn sie Probleme gehabt hätte."


"Wenn er das so sagt, ergibt es schon Sinn."


hi "Es schien ihr heute ziemlich gut zu gehen, vielleicht etwas erschöpfter als sonst."


hi "Es ging ihr auch schon besser, als ich sie gestern besucht hatte, also bin ich nicht sonderlich überrascht."


show nurse neutral onlayer master
with charachange

"Doc nickt, aber mir fällt auf, dass er kurz innehält, als ich meinen gestrigen Besuch erwähne."


nk "Na ja, das ist ja gut zu hören."


nk "Ich dachte mir schon, dass es sich schnell wieder geben würde. Emi erholt sich immer schnell von Erkältungen und Ähnlichem."


hi "Hey, wo wir gerade von Emi sprechen…"


hi "Sind sie und der Teamkapitän…? Na ja, Sie wissen schon."


show nurse fabulous onlayer master
with charachange

"Er schaut mich misstrauisch an."


nk "Warum fragst du?"


hi "Na ja, es ist nur, dass sie sich anscheinend recht nahe stehen, und ich war einfach nur neugierig."


hi "Und sie direkt zu fragen wäre irgendwie peinlich."


"So weit, so gut. Nun noch die Tarnung komplett machen."


hi "Außerdem denke ich, sie würden ein gutes Paar abgeben."


show nurse grin onlayer master
with charachange

"Doc lacht."


nk "Na ja, ich glaube, du bist nicht der erste, der das denkt."


nk "Aber ich glaube mit einiger Sicherheit sagen zu können, dass die beiden niemals so etwas tun würden."


hi "Sicherheit?"


show nurse neutral onlayer master
with charachange

nk "Genau."


show nurse fabulous onlayer master
with charachange

nk "Nicht, dass ich dir sagen dürfte warum. Schweigepflicht und so."


hi "Ja genau, Sie finden es nur toll, mir ein Geheimnis vorenthalten zu können."


show nurse grin onlayer master
with charachange

nk "Das auch."


show nurse neutral onlayer master
with charachange

nk "Okay, und nun raus hier. Ich bin ein vielbeschäftigter Mann, wie du weißt."


stop music fadeout 2.0

scene bg school_nursehall onlayer master
show emi basic_grin_gym onlayer master at center
with locationchange

"Ich rolle nur meine Augen, als ich zur Tür hinaus gehe und Emi bedeute einzutreten."


show emi basic_grin_gym onlayer master:
    center
    easeout 0.5 xpos 0.4 alpha 0.0
with Pause(0.5)

hide emi onlayer master
with None

"Die ganze Zeit muss ich mich beherrschen, um nicht vor Freude loszutanzen."


window hide

play music music_running

centered "Die beiden würden niemals so etwas tun."


window show

"Das ist genau das, was ich hören wollte."


"Ich bin versucht, sie auf der Stelle zu fragen, aber ich denke, Doc hätte da sicher etwas dagegen."


"Außerdem weiß ich immer noch nicht genau, wie Emi über mich denkt."


"Ich meine, es ist offensichtlich, dass ich ein Freund für sie bin, aber mehr als das? Ich bin mir nicht sicher."


"Trotzdem fühle ich mich nun wesentlich besser. Ich muss nur noch einen guten Zeitpunkt finden, um Emi zu sagen, was ich fühle."


"Dieses Problem sollte mich wenigstens für den Rest des Tages beschäftigen."


stop music fadeout 6.0


label de_E15:

scene bg school_nursehall onlayer master
with None

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0

scene bg school_roof onlayer master
with shorttimeskip

"Das Dach ist komplett verlassen."


"Normalerweise ist Rin immer vor mir hier oben, aber sie ist seltsamerweise nicht da."


"Ich frage mich, ob sie Emi ausnahmsweise in die Cafeteria begleitet. Das scheint mir zwar ziemlich unwahrscheinlich zu sein, aber es ist die einzige Erklärung, die mir einfällt."


"Ein Teil von mir will Rin suchen gehen, aber ein weit größerer Teil von mir findet die Sonnenstrahlen auf meiner Haut viel zu angenehm, um sich aufzuraffen."


"Ich stochere gelangweilt in meinem Mittagessen herum, während ich auf Emi und Rin warte."


"Es dauert nicht lange, bis ich jemanden die Treppe hochkommen höre."


$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_door_creak

"Ich warte, bis die Tür sich öffnet, bevor ich anfange zu reden."


hi "Hat ja lange genug gedauert."


hi "Lasst ihr mich einfach hier warten, also ehrlich."


hi "Ihr Zwei seid…"


hi "Hä?"


"Das ist seltsam."


show emi basic_confused onlayer master at center
with charaenter

"Die einzige Person, die in der Tür steht ist Emi, die ein wenig verwirrt aussieht."


emi "Was meinst du mit „hä?”"


show emi basic_grin onlayer master
with charachange

emi "Ich bin's! Du weißt schon, Emi! Wir trainieren morgens zusammen."


"Sie grinst und ich spüre, wie mein Herz bei dem Anblick einen kleinen Sprung macht."


hi "Ja, das weiß ich. Ich bin nur verwirrt…"


hi "… Wo ist Rin?"


show emi sad_depressed onlayer master
with charachange

"Emis Grinsen weicht einem ziemlich schuldbewussten Gesichtsausdruck."


emi "Ach ja, das…"


emi "Ich… Irgendwie…"


show emi sad_shy onlayer master
with charachange

emi "habichsieangesteckt."


play music music_another fadein 0.5
$ renpy.music.set_volume(1.0, 0.0, channel="sound")

hi "Auweia."


hi "Sollte ich mir auch Sorgen machen?"


"Es wäre nur logisch. Schließlich hatten Emi und ich gestern engen Kontakt…"


"Also was haben sie und Rin getan, dass Rin sich angesteckt hat?"


"…"


"Ruhig Blut, alter Junge. Denk nicht mal dran."


"Rin hat wahrscheinlich einfach nur ein schlechteres Immunsystem als ich."


show emi basic_shock onlayer master
with charachange

"Emi scheint von meiner Frage schockiert zu sein, als hätte sie noch gar nicht daran gedacht."


emi "Ich hoffe nicht!"


show emi excited_sad onlayer master
with charachange

emi "Ich würde mir furchtbare Vorwürfe machen, wenn du meinetwegen krank werden würdest, Hisao!"


hi "Oh weh, ich glaube, ich fühle schon das Fieber…"


show emi sad_annoyed onlayer master
with charachange

"Emi sieht zu Tode erschrocken aus, aber dann setzt sie einen wütenden Gesichtsausdruck auf."


emi "Hisao!"


emi "Hör {b}sofort{/b} auf krank zu werden!"


show emi basic_annoyed onlayer master
with charachange

emi "Das lasse ich nicht zu!"


show emi basic_annoyed_close onlayer master
with vpunch

"Sie fasst mich impulsiv am Kragen."


emi "Hörst du mich, Hisaos Immunsystem?"


show emi sad_angry_close onlayer master
with charachange

emi "Bring deinen Arsch in Bewegung!"


"Ich salutiere vor ihr."


hi "Zu Befehl, gnädige Frau."


show emi basic_grin onlayer master
with charadistant

"Emi tritt einen Schritt zurück und nickt zufrieden."


show emi basic_closedgrin onlayer master
with charadistant

emi "Gut."


show emi basic_happy onlayer master
with charadistant

emi "Ich erlaube dir schließlich nicht, unser morgendliches Training zu verpassen."


hi "Aber du hast ein Training verpasst!"


show emi sad_annoyed onlayer master
with charachange

"Emi verschränkt ihre Arme vor der Brust und schaut mich herablassend an."


emi "Ja, aber das war etwas anderes. Das war ich und nicht du."


hi "Das ist überhaupt nichts anderes."


show emi basic_confused onlayer master
with charachange

"Emi starrt mich entgeistert an."


emi "Das ist ein Scherz, oder?"


show emi basic_annoyed onlayer master
with charachange

emi "Natürlich ist das etwas anderes!"


hi "Nein, ist es nicht! Du misst ganz offensichtlich mit zweierlei Maß!"


show emi sad_annoyed onlayer master
with charachange

emi "Ich weiß nicht, was das damit zu tun haben soll."


hi "Oh, na gut."


show emi basic_closedgrin onlayer master
with charachange

"Emi scheint sich über ihren Sieg zu freuen."


hi "Was ist überhaupt mit Rin? Ich hoffe, es geht ihr nicht allzu schlecht."


show emi basic_grin onlayer master
with charachange

"Emi schüttelt den Kopf."


emi "Nö! Sie ist bald wieder fit."


show emi excited_proud onlayer master
with charachange

emi "Ich habe ihr etwas Medizin vorbeigebracht, die sie wieder auf die Beine bringen sollte."


show emi basic_hes onlayer master
with charachange

emi "Obwohl… Ich hätte besser aufpassen sollen, dass sie nicht versucht, alles auf einmal zu nehmen…"


show emi basic_grin onlayer master
with charachange

emi "Das hat sie schon einmal gemacht, weißt du?"


"Irgendwie überrascht mich das gar nicht."


"Ich bezweifle, dass Rin auf Tageshöchstdosen oder so was achtet."


hi "Dann solltest du besser später nach ihr sehen. Nur um sicher zu gehen."


show emi sad_grin onlayer master
with charachange

"Emi zuckt mit den Schultern."


emi "Ich schaue nach dem Training bei ihr vorbei. Bis dahin wird sie durchhalten."


"Ich nicke. Damit ist dieses Thema wohl abgehakt."


"Das einzige Problem ist, dass ich nicht weiß, worüber man sonst noch sprechen könnte."


hi "Also…"


hi "Hast du demnächst noch irgendwelche Sportturniere?"


window hide

nvl clear
nvl show dissolve

n "\n\n\n\n\n\n\n\nDas ist eine sehr umständliche Methode, zu fragen, ob sie am Wochenende Zeit hat."


n "Wenn sie Zeit hat, kann ich mich vielleicht mit ihr verabreden."


n "Na ja, vorausgesetzt ich bringe die Worte heraus."


nvl clear
nvl hide dissolve

window show

show emi basic_grin onlayer master
with charachange

"Emi schüttelt den Kopf."


show emi basic_closedgrin onlayer master
with charachange

emi "Nö, die nächsten paar Wochen nicht, glaube ich. Die Saison geht dem Ende zu."


"Ach richtig. Ich bin ja genau mittendrin hier aufgetaucht nicht wahr?"


"Heißt das nicht, dass bald die Abschlussprüfungen sind? Ich sollte mich besser erkundigen."


hi "Was machst du denn so an Wochenenden, wenn kein Turnier ist?"


show emi excited_proud onlayer master
with charachange

"Eine Augenbraue hebt sich, und Emi schaut mich belustigt an."


emi "Du bist heute wahnsinnig neugierig, nicht wahr?"


"Ich zucke mit den Schultern und hoffe, dass es lässig aussieht."


hi "Es interessiert mich einfach."


hi "Ich weiß ja schließlich nicht wie es ist, ein Spitzensportler zu sein."


show emi basic_closedgrin onlayer master
with charachange

emi "Pah, Schmeichelei."


"Sie winkt gelangweilt ab."


show emi basic_grin onlayer master
with charachange

emi "Ich bin nicht wirklich so gut, weißt du?"


show emi basic_closedhappy onlayer master
with charachange

emi "Du hast mich nur an einem guten Tag gesehen, das ist alles."


hi "Lügnerin."


show emi sad_grin onlayer master
with charachange

stop music fadeout 6.0

emi "Hehe, ja."


emi "Aber Bescheidenheit ist die Zier eines guten Athleten."


show emi sad_depressed onlayer master
with charachange

emi "Zumindest hat mein Vater das immer gesagt."


"Sie zuckt mit den Schultern und versucht erfolglos, ihren dunklen Gesichtsausdruck zu überspielen."


hi "Hey, was ist los? Bedrückt dich was?"


"Emi fängt an, es abzustreiten, aber dann seufzt sie und gibt auf."


"Ich frage mich, ob sie noch zu erschöpft von ihrer Krankheit ist, um es wie sonst immer abzustreiten."


"Oder ob sie mir inzwischen einfach genug vertraut, um mit mir darüber zu reden."


show emi sad_shy onlayer master
with charachange

play music music_comfort fadein 9.0

emi "Na ja, erinnerst du dich an gestern Abend?"


"Und ob. Ich beschränke mich aber darauf zu nicken."


show emi sad_depressed onlayer master
with charachange

emi "Das ist nicht das erste Mal, dass mir das passiert ist."


emi "Ich kriege sie sogar ziemlich…"


"Sie unterbricht sich, als ob ihr plötzlich klar wird, was sie tut."


"Es ist fast, als würde sie eine ihrer Regeln brechen."


"Aber sie fängt wieder an und wählt ihre Worte sorgfältig."


emi "Na ja, nicht oft, aber…"


show emi sad_shy onlayer master
with charachange

emi "Manchmal."


emi "Es ist nur diese Woche ein paar Mal vorgekommen."


show emi sad_depressed onlayer master
with charachange

"Sie seufzt und sieht furchtbar frustriert aus."


show emi sad_shy_close onlayer master
with characlose

"Ich lehne mich zu ihr hinüber und nehme sie in den Arm. Anders als beim letzten Mal scheint sie das nicht zu erschrecken."


"Stattdessen scheint sie sich zu entspannen, als meine Arme sie umschließen."


"Wir bleiben eine Weile so."


hi "Hey, du weißt, dass es mir gestern Abend ernst war."


hi "Du kannst wirklich mit mir reden, wenn du Probleme mit so was hast. Es ist immer schwer, allein mit solchen Dingen fertig zu werden, weißt du?"


show emi sad_grin_close onlayer master
with charachange

"Emi lächelt und befreit sich aus meiner Umarmung, lehnt aber weiterhin an meiner Schulter."


emi "Danke, Hisao."


show emi basic_grin_close onlayer master
with charachange

emi "Es geht schon, denke ich."


"Ich sehe bereits, wie sie sich zusammenreißt und wieder alles in sich verschließt."


"Sieht aus, als wäre das Thema damit auch abgehakt."


hi "Also, hast du noch mal über diese Berufsumfrage nachgedacht?"


show emi basic_closedgrin_close onlayer master
with charachange

emi "Nein, nicht wirklich."


show emi basic_grin_close onlayer master
with charachange

emi "Weißt du, ich plane nicht sehr weit voraus."


emi "Aber ich denke, ich könnte wenigstens anfangen, mir ein paar Unis anzuschauen, hm?"


"Ich zucke mit den Schultern."


hi "Sicher, es sei denn, das mit den Piraten war dein Ernst."


hi "Als ich mich das letzte Mal erkundigt habe, war ein Uniabschluss keine Voraussetzung für eine Piratenkarriere."


hi "Aber vielleicht gibt es ja inzwischen irgendwo so was wie eine Piratenuniversität."


show emi basic_closedgrin_close onlayer master
with charachange

"Emi kichert und ist schon fast wieder die Alte, aber da ist noch etwas anderes…"


"Verschmitzt. So könnte man es vielleicht beschreiben."


"Emi schaut mich verschmitzt an, ihren Kopf immer noch an meine Schulter gelehnt."


show emi sad_grin_close onlayer master
with charachange

emi "Würdest du mit mir mitkommen, wenn ich ausreißen würde, um Pirat zu werden?"


hi "Natürlich würde ich das!"


hi "Wer würde sich die Gelegenheit entgehen lassen, mit dir zusammen Pirat zu sein? Der müsste ja völlig wahnsinnig sein!"


show emi basic_grin_close onlayer master
with charachange

emi "Na ja, wenn du es so sagst… Keine Ahnung."


show emi basic_closedgrin_close onlayer master
with charachange

"Sie kichert wieder."


"Mir fällt auf, dass mein Herzschlag sich beschleunigt hat. Das liegt wahrscheinlich an Emis Nähe."


"Wieder dieser Hauch von Erdbeeren."


"Ich muss einfach grinsen, als ich sie anschaue."


"Sie ist wieder glücklich."


show emi sad_shy_close onlayer master
with charachange

emi "Hey, Hisao."


hi "Hmm?"


show emi sad_grin_close onlayer master
with charachange

emi "Wenn du mich küssen willst, solltest du es bald tun. Ich glaube, die Mittagspause ist bald vorbei."


stop music fadeout 1.0

"Meine Gedanken machen eine Vollbremsung."


"Ich bin mir ziemlich sicher, dass meine Kinnlade herunterhängt."


"Alles, was ich herausbringe, ist ein gequältes „Hä?”"


show emi basic_closedgrin_close onlayer master
with charachange

"Das amüsiert Emi nur noch mehr."


show emi excited_proud_close onlayer master
with charachange

emi "Daran hast du doch gedacht, oder?"


"Sie setzt sich auf und bringt ihr Gesicht auf eine Höhe mit meinem."


show emi basic_grin_close onlayer master
with charachange

emi "Es würde mir wahrscheinlich gefallen, weißt du?"


show emi sad_grin_close onlayer master
with charachange

emi "Du bist ein wirklich…"


show emi sad_shy_close onlayer master
with charachange

emi "… Na ja."


"Sie sammelt sich kurz und sieht aus, als wolle sie gleich etwas sehr Wichtiges sagen."


show emi sad_grin_close onlayer master
with charachange

emi "Falls du es noch nicht gemerkt haben solltest: Ich glaube, ich habe mich ein bisschen in dich verliebt."


show emi basic_grin_close onlayer master
with charachange

emi "Da wirst du was unternehmen müssen."


"Diese Mal schließt ihr Grinsen bei mir einige wichtige Gedankenprozesse kurz."


"Irgendwann habe ich mich zu ihr umgedreht, und irgendwann hat sie ihre Arme um meinen Hals gelegt."


"Und irgendwann habe ich dann meine Arme um ihre Hüfte gelegt."


"Ich kann beim besten Willen nicht sagen, wann genau das passiert ist."


"Denn in diesem Moment gibt es in meinem Kopf nur diese Stimme, die schreit, dass ich sie endlich küssen soll."


"Ich schaue wieder in Emis Augen."


"Da ist es."


"Dieses Funkeln, das ich gestern auf dem Bett gesehen habe. Es ist wieder da."


"Plötzlich erkenne ich, dass sie Angst hat, ich könnte sie zurückweisen."


stop ambient fadeout 1.5

"Was für ein dämlicher Gedanke."


window hide

play music music_romance fadein 0.5

scene white onlayer master
show ev emi_firstkiss onlayer master:
    truecenter
    zoom 4.0 rotate 20 subpixel True
    0.7
    linear 0.3 zoom 1.1 rotate 0
    easein 12.0 zoom 1.0
with GenericWhiteout(0.5, 0.2, 2.0)

with Pause (5.0)

nvl clear
nvl show dissolve

n "\n\n\n\nIhre Lippen schmecken ein wenig nach Erdbeeren."


n "Sie lehnt sich vor, und ihre Arme schließen sich enger um meinen Kopf, damit ich nicht entkommen kann."


n "Nicht, dass ich das vorgehabt hätte."


n "Ich habe ein seltsames Gefühl in der Magengrube."


n "Die Welt fällt von mir ab."


n "Es gibt nur sie und mich und diese Bank."


n "Meine Arme schließen sich wie in Trance enger um sie, und ziehen sie näher an mich heran."


n "Ich atme ihren Duft ein; ich versuche verzweifelt, mir jedes Detail einzuprägen – wie sie schmeckt, wie sie riecht, wie sie sich anfühlt."


play sound sfx_warningbell
play ambient sfx_rooftop fadein 4.0

nvl clear
nvl hide dissolve

scene bg school_roof onlayer master
show bg school_roof_blurred as overlay onlayer master:
    center
    linear 6.0 alpha 0.0
show emi sad_shyblush_close onlayer master
with silentflash

window show

"Die Schulglocke bringt uns beide zurück in die Realität, und wir beenden unseren Kuss."


"Emis Wangen sind immer noch leicht gerötet, und sie scheint außer Atem zu sein. Zu ihrer Verteidigung – ich bin es auch."


"Wir stehen einen Moment lang da und versuchen zu begreifen, was wir gerade getan haben."


"Emi ist die erste, die das Schweigen bricht."


show emi sad_grin_close onlayer master
hide overlay onlayer master
with charachange

emi "Also…"


show emi basic_closedgrin_close onlayer master
with charachange

emi "… Hast du Lust, heute Abend nach dem Training mit mir zu essen?"


hi "So ein Zufall."


hi "Ich wollte dich gerade dasselbe fragen."


"Na ja, eigentlich hatte ich wohl mehr eine richtige Verabredung am Wochenende oder so was im Sinn. Aber es ging zumindest in die gleiche Richtung."


with vpunch

"Emi schubst mich spielerisch."


show emi basic_happy_close onlayer master
with charachange

emi "Ja, sicher."


show emi basic_closedhappy_close onlayer master
with charachange

emi "Du warst immer noch unter Schock, weil ich so unglaublich gut küssen kann."


"Wir gehen zusammen die Treppe hinunter zu unseren jeweiligen Klassenräumen."


stop ambient fadeout 2.0

scene bg school_hallway3 onlayer master
show emi sad_grin onlayer master at center
with locationskip

hi "Hey, du hast auch nicht gleich danach wieder angefangen zu reden."


show emi basic_closedgrin onlayer master
with charachange

emi "Das habe ich nicht."


show emi basic_closedhappy onlayer master
with charachange

emi "Wir sehen uns dann nach dem Training, Hisao."


show emi basic_closedgrin_close onlayer master
with charachange

show emi basic_closedgrin_close onlayer master:
    center
    easeout 0.5 xpos 0.6 alpha 0.0
with None

"Sie lehnt sich schnell zu mir herüber und gibt mir mitten auf dem Gang einen kurzen Kuss. Meine Gedanken gehen sofort wieder in den freien Fall über."


scene bg school_scienceroom onlayer master
with locationchange

"Als ich meinen Klassenraum betrete, begrüßt mich Misha kichernd."


show misha hips_grin onlayer master at center
with charaenter

mi "Aber, Hicchan, du kleiner Romantiker, du~!"


mi "Hast du ihr auf dem Dach deine Liebe gestanden? Hm? Hast du~?"


hi "Ähm, eigentlich war es anders herum, glaube ich."


show misha cross_laugh onlayer master
with charachange

"Das löst in Misha erneut einen Lachanfall aus."


show misha hips_grin onlayer master
with charachange

mi "Junge Liebe ist so unberechenbar, nicht wahr~?"


"Da das Misha ist, hätte ich eigentlich erwarten sollen, dass sie mich damit aufzieht."


hi "Ich glaube…"


show misha hips_grin onlayer master:
    center
    easeout 0.5 xpos 0.4 alpha 0.0
with None

"Bevor ich wirklich antworten kann, betritt Mutou den Raum, und Misha hüpft kichernd zu ihrem Platz."


"Ich habe den Verdacht, dass ich diese Art Gespräch heute noch öfter führen werde, vor allem weil Emi mich mitten auf dem Gang geküsst hat."


"Aber irgendwie ist mir das egal."


$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
stop music fadeout 5.0

"Zum ersten Mal seit ich hier angekommen bin, fühlt mein Herz sich leicht an."


window hide
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
