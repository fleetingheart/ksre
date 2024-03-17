label de_L9:

window hide None

scene black onlayer master
with dissolve

scene bg misc_sky onlayer master at Fullpan(10.0)
with locationchange

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_normal fadein 3.0

window show

"Ich stütze mein Kinn auf meiner Hand ab und starre geistesabwesend aus dem Fenster. Wieder einmal zieht sich eine von Mutous Unterrichtsstunden schier endlos in die Länge."


"Das Sommerwetter scheint in seiner himmelblauen Pracht fast schon verführerisch. Einzig eine gelegentlich vorbeiziehende Wolke durchbricht das strahlende Blau."


"Wahrscheinlich sehnt ein Teil vom mir sich danach, nach draußen zu fliehen."


mu "Nakai, kannst du das beantworten?"


"Aber dieser Teil von mir gehört nun der Vergangenheit an."


scene bg school_scienceroom onlayer master
show muto normal onlayer master at center
with locationchange

hi "In diesem Fall… Ich denke, das Suffix -an?"


show muto smile onlayer master
with charachange

mu "Richtig. Weiter im Text. Das Suffix für…"


"Während meine Aufmerksamkeit gegenüber Mutou abermals nachlässt, sehe ich Misha, die mir enthusiastisch ihren Daumen entgegenstreckt. Ich nicke ihr zu, um sie zu beruhigen."


scene bg school_scienceroom onlayer master
with shorttimeskip

"Es ist jetzt einige Tage her, dass Lilly nach Schottland aufgebrochen ist. Tage, die relativ friedlich vergangen sind."


"Anders als erwartet ging das Leben mehr oder weniger normal weiter. Ich muss zwar ab und zu an sie denken, aber zumindest bin ich durch meinen Tagesablauf bisher ausreichend abgelenkt."


"Als endlich Mittagspause ist, plaudere ich wie üblich mit Hanako."


show hanako basic_normal onlayer master
with charaenter

ha "Sind die Fortsetzungen genauso gut?"


hi "Nicht wirklich. Am besten bleibst du einfach bei den Originalen. Seine späteren Bücher werden ihnen nicht gerecht, außer vielleicht „Der Gottkaiser”."


show hanako basic_bashful onlayer master at center
with charachange

ha "Danke, ich war mir nicht ganz sicher, ob…"


show misha invis onlayer master at offscreenleft
show shizu invis onlayer master at offscreenleft
with None

show hanako defarms_shock onlayer master at right
show shizu behind_blank onlayer master at center
show misha hips_smile onlayer master at left
show bg school_scienceroom onlayer master at bgright
with dissolvecharamove

"Als Hanako zur Seite tritt, sehe ich Shizune in ihrer typisch sachlichen Art auf mich zukommen, flankiert von ihrem immer präsenten hellhaarigen Schatten."


"So sehr ich es auch versuche, mir gelingt es nicht, auch nur eine Spur ihrer Absichten aus ihren Gesichtern zu lesen. Shizunes Pokerface und Mishas schier unerschöpfliche Fröhlichkeit sind eine teuflische Kombination."


hi "Morgen, Shizune, Misha."


show hanako emb_timid onlayer master
with charachange

ha "Ähm… hi."


show shizu basic_normal onlayer master
with charachange

"Um den Gruß zu verdeutlichen, nicke ich Shizune zu. Sie grüßt uns kurz und knapp auf die gleiche Art zurück."


"Es ist schon eine ganze Weile her, seit ich wirklich mit einer von beiden geredet habe. Eine Weile lang dachte ich schon, dass sie mir ausweichen würden, aber dann dachte ich mir, dass Shizune dafür nicht wirklich der Typ ist."


show shizu adjust_happy onlayer master
with charachange

shi "…"


show misha sign_smile onlayer master
with charachange

mi "Morgen~! Shicchan sagt, dass Herr Mutou dich sehen will."


"Dank dieser Aussage verzieht sich mein Gesicht, als ob ich etwas Verdorbenes gegessen hätte, was Misha unendlich zu amüsieren schien."


show misha cross_laugh onlayer master
with charachange

mi "Wahahaha~! Jeder würde denken, dass du in der Patsche steckst, Hicchan!"


show shizu behind_smile onlayer master
with charachange

shi "…"


show misha perky_smile onlayer master
with charachange

mi "Es ist dir vielleicht nicht bewusst, aber in dieser Klasse bist du derjenige, der sich die geringsten Sorgen machen muss."


show hanako emb_smile onlayer master
with charachange

"Was für ein unerwartetes Vertrauensbekenntnis. Selbst Hanako nickt zögernd als Bestätigung."


hi "Danke, ich werd's mir merken. Aber da war etwas, was ich dich fragen wollte."


show shizu basic_normal onlayer master
with charachange

shi "…"


show misha hips_smile onlayer master
with charachange

mi "Und was wäre das, Hicchan?"


"Ich habe ein ganz mieses Gefühl bei der Sache, aber…"


hi "Gibt es einen Grund, warum du und Lilly nicht miteinander auskommt? Ein kleines bisschen Höflichkeit würde euch beiden doch sicher bei euren Pflichten helfen."


show shizu cross_angry onlayer master
with charachange

"Shizunes kalter Blick, nachdem Misha fröhlich übersetzt hat, lässt mich erstarren. Im Nachhinein betrachtet hätte ich das echt besser formulieren können…"


show hanako emb_sad onlayer master:
    xpos 1.05
with dissolvecharamove

"Ich bin mir sicher, dass ich aus den Augenwinkeln Hanako zurückweichen sehe. Nur ein bisschen."


show shizu basic_angry onlayer master
with charachange

"Glücklicherweise bemerkt Shizune das und zügelt sich, während sie sich eindringlich durch die Haare fährt, um etwas Dampf abzulassen. Wie auf Kommando beginnt Misha zu übersetzen, sobald sich Shizunes Arme in Bewegung setzen."


show shizu behind_frown onlayer master
with charachange

shi "…"


show misha hips_frown onlayer master
with charachange

mi "Ich würde ja sagen, dass dich solche Dinge nichts angehen, aber da du mit Lilly befreundet zu sein scheinst…"


show shizu adjust_frown onlayer master
with charachange

"Sie macht eine Pause, um ihre Brille zu richten und ihren Standpunkt auf bestmögliche Weise deutlich zu machen."


show shizu basic_angry onlayer master
with charachange

shi "…"


show misha sign_smile onlayer master
with charachange

mi "Meine Meinung dazu ist natürlich nicht unvoreingenommen, aber das gilt wohl auch für Lilly. Sagen wir einfach, dass wir uns früher besser verstanden haben als jetzt."


show shizu behind_frown onlayer master
show misha sign_confused onlayer master
with charachange

"Shizune stoppt Misha mit einer schnellen Geste und bespricht sich kurz mit ihr, bevor sie fortfahren. Die Tatsache, dass sie sich so einfach und doch geheim vor unseren Nasen unterhalten können, ist etwas verstörend."


show hanako basic_normal onlayer master
show shizu basic_normal2 onlayer master
show misha sign_sad onlayer master
with charachange

"Hanako scheint mein Interesse an diesem Verfahren mit kaum verborgener Neugier zu teilen. Als sie ihr undurchschaubares Gespräch beendet haben, sieht Misha etwas ernüchtert aus. Ihre Meinung zu dem Thema scheint nicht von Bedeutung zu sein."


show misha perky_confused onlayer master
with charachange

mi "Shicchan sagt, dass du Lilly fragen sollst. Sie will nicht diejenige sein, die dich in diese Sache hineinzieht."


"Was soll's. Ich werde sie wohl fragen müssen, wenn sie wieder da ist."
"Zumindest habe ich ein paar Informationen aus Shizune herausgekriegt. Dass die beiden sich einmal nähergestanden haben, heißt, dass sie sich nicht immer an die Kehle gesprungen sind – oder zumindest nicht so sehr."


hi "Ich verstehe. Trotzdem vielen Dank."


stop music fadeout 8.0

show shizu invis onlayer master at offscreenleft
show misha invis onlayer master at offscreenleft
show hanako basic_normal onlayer master at center
show bg school_scienceroom onlayer master at center
with dissolvecharamove

"Beide nicken, verabschieden sich und schreiten aus der Tür. Zweifelsohne machen sie sich direkt auf den Weg zum Schülerratsbüro."


hi "… Hätte vermutlich schlimmer ausgehen können."


show hanako cover_bashful onlayer master
with charachange

"Hanako atmet hörbar aus, erleichtert über das Ende dieser Konfrontation. Nicht, dass es mir anders ergeht."


show hanako basic_bashful onlayer master
with charachange

ha "Wir sehen uns dann später?"


hi "Ja, ich warte im Teeraum. Bis später."


hide hanako onlayer master
with charaexit

"Sie winkt und schließt sich dem Strom der Schüler an, die den Raum verlassen."


show muto normal onlayer master at center
with charaenter

mu "Nakai, hast du einen Moment Zeit?"


"Seine Stimme hat ihren üblichen, monotonen Klang. Anscheinend hat er beschlossen, dass ich daran erinnert werden muss, dass ich zu ihm kommen sollte."


hide muto onlayer master
with charaexit

"Als ich meine Sachen gepackt und seinen Tisch erreicht habe, ist der Klassenraum so gut wie leer."


hi "Äh… Sie wollten mich sprechen?"


play music music_happiness fadein 5.0

show muto normal onlayer master at center
with charaenter

"Er sieht mich an und gibt dann ein peinlich künstliches Lachen von sich."


show muto smile onlayer master
with charachange

mu "Kein Grund zur Sorge, du kriegst keinen Ärger. Ich wollte dich nur etwas fragen, was ich schon ein paar andere Schüler gefragt habe."


"Immerhin etwas. Einen Moment dachte ich, dass meine Maxime von gesenktem Kopf und erhobenem Stift versagt hätte."


hi "Worüber wollten Sie denn mit mir reden?"


show muto normal onlayer master
with charachange

mu "Also erst einmal: Wie kommst du mit dem Unterrichtsstoff zurecht? Gut oder eher schlecht?"


"Ich überlege, wie die Frage gemeint ist. Eine ganze Weile bin ich damit beschäftigt, mir eine Antwort zu überlegen, die nicht übertrieben demütig oder hochnäsig klingt."


hi "Ich denke, ich komme ganz gut mit. Die Themen sind nicht allzu schwierig, und ich schneide in den Tests besser ab, als ich dachte."


show muto smile onlayer master
with charachange

mu "Eine gute Antwort. Ich sehe das genauso."


"Innerlich seufze ich erleichtert darüber, dass meine Antwort zufriedenstellend ist. Zu sagen, dass es mich nicht stolz machen würde, wäre eine dreiste Lüge."


"In dem Strudel meiner Gedanken, nachdem ich erfahren hatte, dass ich auf die Yamaku wechseln würde, erschienen mir meine Noten völlig unwichtig."


"Völlig im Unklaren darüber, was für ein Wissensstand von mir erwartet werden würde, war ich enorm erleichtert, als ich herausfand, dass ich dem Unterricht folgen konnte."


show muto normal onlayer master
with charachange

mu "Deine Umstände haben dir vermutlich einen Knüppel zwischen die Beine geworfen, aber hast du dir schon Gedanken über deine Zukunft gemacht?"


hi "Meine Zukunft?"


mu "Was willst du später mal machen? Hast du dir schon überlegt, wo du dich in zehn oder zwanzig Jahren siehst?"


mu "Es würde mich nicht wundern, wenn du dir das schon auf deiner vorherigen Schule überlegt hättest, aber ich habe keine Aufzeichnungen darüber."


"Ich denke, das letzte Jahr der Oberstufe ist die Zeit, in der Schüler sich mit so etwas befassen müssen. Um ehrlich zu sein, habe ich mir – im Gegensatz zu meiner aktuellen Situation – kaum Gedanken darüber gemacht."


"Meine Gedanken erahnend äußert sich Mutou."


mu "Es ist in Ordnung, wenn du dir noch keine Gedanken gemacht hast. Ich wäre nicht überrascht, wenn sich ein Großteil der Klasse noch keine Gedanken darüber gemacht hätte. Vielleicht willst du eines deiner Talente verfolgen?"


"Er versucht ziemlich offensichtlich, eine Antwort aus mir herauszukriegen, aber etwas an seiner Formulierung macht mich stutzig."


"Er schien nicht vorzuhaben, alle so auszufragen, also muss er irgendeine Art von Auswahlkriterium haben. Vermutlich unsere Noten."


hi "Irgendwas in den Naturwissenschaften wäre wohl der Weg des geringsten Widerstandes."


"Er beginnt zu strahlen, ohne Zweifel erfreut darüber, dass ein Musterschüler sein Fach als berufliche Laufbahn auswählt."


show muto smile onlayer master
with charachange

mu "Gut. Eine grobe Idee zu haben, ist der erste Schritt. Ich würde dir jedoch raten, noch einmal darüber nachzudenken."


hi "Das werde ich. Zum Glück beruhigt sich langsam alles. Das sollte helfen."


mu "Schön zu hören. Oh, außerdem habe ich bemerkt, dass Ikezawas Anwesenheit und Noten sich verbessert haben, seit du dich mit ihr angefreundet hast. Vielen Dank dafür."


hi "Ich bin überrascht, dass Sie bemerkt haben, dass wir uns kennen."


"Sein Lachen ist genauso unbeholfen wie sein Lächeln."


"Dieser Mann hat wirklich keine Ahnung, wie man sich unter Menschen richtig verhält. Jede Regung seines Gesichtes wirkt wie vorsichtig eingeübt, jedoch mit völlig falscher Choreographie."


show muto normal onlayer master
with charachange

mu "Man könnte sagen, dass es Teil der Aufgaben eines Lehrer ist, zu wissen, wer sich untereinander kennt."


"Als er bemerkt, dass er zu weit vom Thema abschweift, hustet er lautstark in seine Hand."


mu "Du hast sicher noch etwas vor, also will ich dich nicht aufhalten. Bitte denk darüber nach, in welche Richtung du gehen willst. Du hast nicht mehr viel Zeit, bis du mit der Oberschule fertig bist."


hi "Werde ich. Danke."


stop music fadeout 4.0

scene bg school_hallway3 onlayer master
with locationchange

"Das kurze Gespräch ist zu Ende, und ich verabschiede mich, während Herr Mutou sich wieder dem Durchwühlen seiner Lehrmaterialien zuwendet."


"In Zeiten wie diesen bin ich unglaublich neidisch auf Lilly. Seine eigene Zukunft so klar vor Augen zu haben und trotzdem in so jungen Jahren schon darauf hinzuarbeiten…"


"So wie meine Gedanken im Hier und Jetzt festgefahren sind, kann ich mir das überhaupt nicht vorstellen."


scene black onlayer master
with dissolve



label de_L10:

scene bg school_lobby onlayer master
with locationchange

"Auf dem Weg zur Cafeteria bereue ich stillschweigend, dass meine tägliche Routine aus dem Fenster geworfen wurde."


"Es fing wie ein ganz normaler Tag an. Ich war als einer der Ersten in der Klasse, da ich ganz gut darin geworden bin, meine Pillen zu nehmen, ohne mich zu verschlucken."


"Aber als die Schüler eintrudelten, fehlte eine von ihnen. Hanako."


play ambient sfx_crowd_indoors fadein 0.5
scene bg school_cafeteria onlayer master at right
show crowd onlayer master at left
with locationchange

"Als ich die Cafeteria betrete, lasse ich meinen Blick auf der Suche nach einem geeigneten Sitzplatz durch den Raum schweifen – ein Versuch, der durch die herumlaufenden und sich unterhaltenden Schüler erschwert wird."


play sound sfx_impact2
with vpunch
$ renpy.music.set_volume(0.5, 0.3, channel="ambient")

hi "Argh!"


"Eine Hand schlägt mir mehrmals kräftig auf den Rücken und bringt mich völlig aus der Fassung."


$ renpy.music.set_volume(0.0, 0.0, channel="ambient")
scene black onlayer master
with shuteyefast

"Mir ist ziemlich egal, wer der Übeltäter ist, da ich mich aus Reflex auf meinen Brustkorb konzentriere."


play sound sfx_heartfast
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.2)

"Meine Hand greift instinktiv an meine Brust, während ich in meinem Kopf die Schritte durchgehe, die mir fast schon in Fleisch und Blut übergegangen sind."


play sound sfx_heartfast
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.2)

"Gleichmäßig atmen… einatmen… und ausatmen…"


play sound sfx_heartslow
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.7)

"Mit Erleichterung merke ich, dass sich mein Brustkorb langsam entkrampft. Als ich wieder aufsehe, ist mein Gesicht schweißgebadet."


$ renpy.music.set_volume(1.0, 5.0, channel="ambient")

scene bg school_cafeteria onlayer master at right
show crowd onlayer master at right
show kenji happy_close onlayer master at center
with openeye

ke "Hey Kumpel… Alles klar bei dir?"


hi "VERDAMMT! Tu das {b}nie{/b} wieder, du Vollidiot!"


show kenji tsun onlayer master
with charadistant

"Er schreckt zurück, ein Ausdruck von Unbehagen auf seinem Gesicht. Ich hätte ihn vermutlich nicht so anfahren sollen – schließlich konnte er es nicht wissen."


"Ich seufze und richte mich mit etwas Mühe wieder auf."


hi "'Tschuldige. Ich habe nur ein paar… Probleme mit meinem Brustkorb. Schwere Schläge sind da nicht gerade fördernd."


"Es ist seltsam, ihn so besorgt zu sehen – und die Tatsache, dass ich nichts dagegen tun kann, ärgert mich."


hi "Lass uns was essen."


show kenji neutral onlayer master
with charachange

ke "Okay. Es tut gut, zur Abwechslung mal Gesellschaft zu haben."


hide kenji onlayer master
with charaexit

show bg school_cafeteria onlayer master at left
show crowd onlayer master at left
with charamove

"Wir stellen uns an. Eine gute Sache ist, dass ich mich mittlerweile vernünftig mit Kenji unterhalten kann, ohne dass er mir anti-feministische Vorträge hält."


hi "Einen freien Tisch zu finden, scheint schwierig zu werden."


show kenji neutral onlayer master at center
with charaenter

ke "Es gibt ein paar Leute, bei denen ich kein Problem hätte, mich dazuzusetzen. Allerdings ist keiner davon wie du."


$ renpy.music.set_volume(0.0, 0.5, channel="ambient")

"Ein Schauer läuft mir den Rücken hinunter."


hi "Erläutere das. Sofort."


play music music_kenji fadein 2.0

show kenji tsun onlayer master
with charachange

ke "Sie hören nicht zu. Ihr Geist ist verschlossen. Es sind die Medien, Kumpel, die gottverdammten gehirnwaschenden, faschistischen Feministenmedien."


"Er holt tief Luft, und ich genieße die Sekunde der Stille."


$ renpy.music.set_volume(1.0, 10.0, channel="ambient")

ke "Verdammt, sie kontrollieren alles. Alles außer dir und mir."


"Ich entspanne mich etwas, während wir unser Essen und Trinken holen."


show kenji happy onlayer master
with charachange

ke "Also, was hast du für mich?"


hi "Was?"


show kenji neutral onlayer master
with charachange

ke "Komm schon, du hängst seit Ewigkeiten mit Satou und diesem anderen Mädel rum. Die Gerüchteküche brodelt."


hi "Leute belauschen ist keine gute Angewohnheit."


show kenji happy onlayer master
with charachange

ke "Lass mich raten – du machst das nie? Nicht mal, wenn dir langweilig ist? Niemals nie?"


hi "Also… Ich… Äh…"


hi "Gut. Punkt für dich."


hide kenji onlayer master
with charaexit

"Wir halten an, um Suppe in unsere Schüsseln zu bekommen und stellen sie auf unsere Tabletts. Das Gebräu, das in den Schüsseln landet, sieht ziemlich fragwürdig aus, aber es riecht zumindest einigermaßen gut."


stop ambient fadeout 1.0

show bg school_cafeteria onlayer master at center
show crowd onlayer master at Alphaout(1.0), center
show kenji invis onlayer master at center
with charamove

show kenji neutral onlayer master:
    ypos 1.14
hide crowd onlayer master
with dissolvecharamove

"Als wir uns an einen wundersamerweise freien Tisch setzen, versuche ich an etwas zu denken, das ihn auch interessieren würde. Hoffentlich fällt mir etwas Brauchbares ein."


hi "Ich hab eine Antwort auf die Frage, die du mir vor ein paar Wochen gestellt hast. Über Lillys nicht-japanische Familienhälfte."


show kenji happy onlayer master
with charachange

ke "Guter Junge. Es ist Russland, richtig? Auf jeden Fall Russland."


hi "Schottland."


show kenji tsun onlayer master
with charachange

"Er ist sichtlich entsetzt."


ke "… Schottland?"


hi "Ja, ich hab genauso reagiert. Sie spricht fließend Englisch und so."


show kenji rage onlayer master
with charachange

ke "… Verdammt! Weißt du, was das heißt? Was für grausame Nachrichten das für mich sind?"


label de_choiceL10_1:
menu:
    with menueffect
    "Ich glaube, er hyperventiliert. Kurz das Bewusstsein zu verlieren, würde seinen Nerven vermutlich guttun."
    "Sein Spiel mitspielen.":




        return m1
    "Sein durchgeknalltes Gefasel ignorieren.":


        return m2

label de_L10a:

hi "Ich habe keine Ahnung, was es heißt. Erleuchte mich."


ke "Kumpel, ich habe gerade 1.000 Yen verloren! Verdammt, das ist der schlimmste Tag meines Lebens."


label de_L10b:

"Ich fange an zu essen, in der Hoffnung, dass er mein Schweigen richtig deutet."


ke "Kumpel, ich habe grade 1.000 Yen verloren! Verdammt, das ist der schlimmste Tag meines Lebens."


"Leider kein Glück."


label de_L10c:

hi "Das ist nicht dein Ernst. Du hast um ihre Nationalität gewettet?"


show kenji tsun onlayer master
with charachange

ke "Einer der Typen in meiner Klasse hat mich damit genervt. Ich hab meine Weisheit mit ihm geteilt, und er hatte den Nerv zu behaupten, dass ich falsch läge."


hi "Und was dachte er?"


ke "Eh, Deutschland oder so. Ist nicht wichtig. Was wichtig ist, sind meine 1.000 Yen."


show kenji rage onlayer master
with charachange

ke "Verdammt, ihretwegen ist der Tag im Eimer. Was für eine Schlampe."


show kenji tsun onlayer master
with charachange

"Er sieht fertig mit den Nerven aus, als er mehrere Klumpen sojagetränkten Reis in sich hineinstopft. Nach nur ein paar Ladungen fängt er an, mit seinen Stäbchen auf mich zu zeigen und auf die Luft vor sich einzustechen."


ke "Also… mm… mm… könntest… mm…"


hi "Hat dir deine Mutter nicht beigebracht, nicht mit vollem Mund zu reden?"


"Er guckt mich grimmig an, bevor er den Rest seines Essens herunterschlingt und mit Saft hinunterspült – auf ziemlich unappetitliche Weise."


"Ich erinnere mich an mein eigenes Essen und beginne, dieses so schnell wie möglich in mich hineinzuschlingen. Je eher ich anfange, desto schneller ist diese Erfahrung vorbei."


show kenji neutral onlayer master
with charachange

ke "Also, wie gesagt."


show kenji tsun onlayer master
with charachange

ke "Wieso würde jemand da leben wollen? Ich meine, was gibt's da? Gras und Hügel. Mehr nicht. Viel Gras und viele Hügel."


ke "Und Männer in Röcken."


"Ich bin mir nicht sicher, was schlimmer ist – das Essen oder seine Weltansicht. Mein Gesicht verzieht sich durch die kombinierte Wirkung von beidem. Nicht, dass er es bemerken würde, oder dass es ihn interessiert."


hi "Ist doch gar nicht so schlimm. Wieso interessierst du dich überhaupt so für sie? Sie ist doch nur deine Klassensprecherin."


show kenji neutral onlayer master
with charachange

"Es folgt ein unheimliches Kichern. Wäre es jemand anderes als Kenji, würde ich mich verdammt unwohl fühlen."


ke "Endlich habe ich die Schwachstelle in der Rüstung der Feministenlegion gefunden. Es hat eine Weile gedauert, aber ich bin mir sicher, dass wir so das gesamte System vernichten können."


show kenji happy onlayer master
with charachange

ke "Das wird dich so was von umhauen. Bist du bereit?"


stop music fadeout 2.0

"Als ich meinen Reis aufgegessen habe, blende ich sein Gebrabbel für einen Moment aus und wage mich an die nicht so lecker aussehende Suppe. Ich merke schon beim ersten Löffel, dass sie kalt ist."


hi "So bereit wie noch nie."


show kenji happy onlayer master
with charachange

ke "Ich habe bestätigt, dass Lilly in der Mafia ist."


play music music_kenji

hi "Was du nicht sagst."


show kenji neutral onlayer master
with charachange

ke "Also gut, hör mir eine Weile zu, und ich beschreibe dir die Szene."


"Ich wünschte, ich hätte die Wahl zu gehen."


ke "Also, Lilly geht nach der Schule die Straße runter."


hi "Du stalkst sie aber nicht, oder?"


show kenji tsun onlayer master
with charachange

ke "Nein! Verdammt, Kumpel, ich hab 'nen Selbsterhaltungstrieb."


"Aber keine Würde, Moralvorstellungen oder soziale Standards…"


show kenji neutral onlayer master
with charachange

ke "Wie auch immer, wie ich gesagt hab. Dieses Auto fährt an sie heran, und wer steigt aus? Ein Mann in Nadelstreifenanzug. Er hilft ihr hinein und fährt einfach weiter. Alter, ich sag dir. Sie steht unter ihrem Schutz. Unter. Ihrem. Schutz."


"Ein Mann in einem… oh. Ich kann sehen, wo das hinführt. Mit viel Mühe unterdrücke ich mein verzweifeltes Seufzen."


hi "Lass mich raten: Der Mann war durchschnittlich groß, von relativ schmaler Statur, hatte blondes Haar, sah ausländisch aus und lächelte viel?"


show kenji rage onlayer master
with charachange

"Er ist absolut überrascht. Ich nutze den Moment der Stille und zwinge einen Mundvoll kalter Suppe in mich hinein."


show kenji tsun onlayer master
with charachange

ke "Anscheinend bist du aufmerksamer als ich dachte."


show kenji neutral onlayer master
with charachange

ke "Ja, meine Wahl war gut."


"Er lacht in sich hinein und nickt so übertrieben dramatisch, dass es komisch aussieht. Die Tatsache, dass ich nicht sagen kann, ob es mit Absicht ist oder nicht, lässt mich meine Stirn runzeln."


show kenji happy onlayer master
with charachange

ke "Das hat weitreichende Folgen, weißt du. Wenn sie wirklich eine Verbindung zu denen hat und wir es geschickt anstellen, könnte diese Information unsere größte Waffe im Kampf gegen den Schülerrat sein."


show kenji happy onlayer master:
    2.0
    "kenji neutral" with Dissolve(0.5, alpha=True)
    3.0
    "kenji happy" with Dissolve(0.5, alpha=True)
    1.0
    "kenji neutral" with Dissolve(0.5, alpha=True)
    4.0
    "kenji tsun" with Dissolve(0.5, alpha=True)
    repeat

"Sobald er mit seinen Reden über Verschwörungstheorien anfängt, wirkt mein Saft auf einmal um einiges wichtiger."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl clear

window hide
nvl show dissolve

n "\n\n\n\nWährend ich halbherzig seinen Hetzpredigten zuhöre, wandern meine Gedanken zu Lilly und ihrer Abneigung gegen Shizune."


n "Mein Verständnis der Vergangenheit der beiden nimmt immer mehr Gestalt an, aber ich bin mir nicht sicher, ob ich auf diesem Weg von ihrer Vergangenheit erfahren sollte. Selbst wenn ich herausfinden sollte, was zwischen den beiden vorgefallen ist, wäre meine Einmischung wohl unerwünscht."


n "… Verdammt, dass Lilly nicht hier ist, lässt mich abschweifen. Ohne ihre Gesellschaft bin ich merklich gelangweilter und melancholischer. Genauso ist es mit Hanako. Alles, was wir während der Pausen noch machen, ist essen und Schach spielen."


n "Wenn ich so darüber nachdenke, sollte ich nach der Schule bei Hanako vorbeischauen. Da sie mittlerweile viel öfter zum Unterricht erscheint, heute aber schon den ganzen Tag nicht da war, hat sie sich vielleicht etwas eingefangen."


stop music fadeout 2.0
$ renpy.music.set_volume(1.0, 6.0, channel="music")

nvl clear

nvl hide dissolve

scene bg school_scienceroom onlayer master
with shorttimeskip

play sound sfx_normalbell

window show

mu "Oh, Nakai?"


show muto normal onlayer master at center
with charaenter

"Ich stoppe auf dem Weg aus dem Klassenraum und drehe mich zu Mutou. Er hält mir ein paar Arbeitsblätter entgegen, die wir im Laufe des Tages abgearbeitet haben."


show muto smile onlayer master
with charachange

mu "Könntest du die zu Ikezawa bringen? Normalerweise würde ich ja eines der Mädchen fragen, aber ich denke, du schaust sowieso bei ihr vorbei."


"Einen Moment überlege ich, ob es mehr als nur eine Vermutung seinerseits sein könnte, aber ich verwerfe die Idee schnell wieder. Ich kann mir nicht vorstellen, dass er so manipulativ ist – es passt einfach nicht zu ihm."


hi "Klar, kein Problem."


scene bg school_girlsdormhall onlayer master
with locationskip

play music music_night fadein 1.0

"Auf dem Weg durch das Mädchenwohnheim geistern mehrere Ideen durch meinen Kopf, warum Hanako abwesend sein könnte. Die offensichtlichste Antwort ist eine Erkältung."


"Aber sie könnte genauso gut gesund sein. Es ist fast eine Woche her, dass Lilly weg ist, und ich vermute, dass sie sich deshalb unsicherer fühlt, als sie es sich anmerken lässt."


show bg school_girlsdormhall onlayer master at right
with charamove

"Schließlich erreiche ich Hanakos Zimmer. Nur eine einfache, braune Tür trennt uns. Dass ihr Zimmer direkt neben Lillys liegt, ist ziemlich praktisch, und hat vermutlich sehr zum Treffen der beiden beigetragen."


$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_doorknock2

"Als ich klopfe, verzieht sich mein Gesicht leicht bei dem Gedanken, dass sie krank sein könnte."


"… Stille. Ich lausche, ob irgendetwas von innen zu hören ist, aber da ist rein gar nichts."


$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_doorknock2

"Ich klopfe erneut, dieses Mal etwas lauter."


"Immer noch keine Antwort. Wie seltsam."


$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_dooropen

show bg school_girlsdormhall onlayer master at center
with charamove

"Hinter mir öffnet sich eine Tür. Ein sommersprossiges und leicht dürres Mädchen kommt heraus und scheint von meiner Anwesenheit etwas überrascht."


label de_choiceL10_2:
menu:
    with menueffect
    "Mädchen" "Äh… Hi."
    "Nach Hanako fragen.":



        return m1
    "Es allein regeln.":

        return m2

label de_L10d:

"Eigentlich ist das eine ziemlich günstige Gelegenheit."


hi "Hi. Entschuldige, aber weißt du, ob Hanako in ihrem Zimmer ist? Sie scheint nicht zu reagieren."


"Mädchen" "Ikezawa ist Ikezawa. Dass sie nicht reagiert, ist völlig normal. Die große Ausländerin ist ja der einzige Mensch, mit dem sie redet."


"Sie zuckt mit den Schultern und verschwindet den Gang hinunter. Anscheinend ist sie mit wichtigeren Dingen beschäftigt als mit Hanako oder mir."


"Ihre abweisende Art verärgert mich."


"Hanako muss den Ruf einer Einsiedlerin haben; ein Ruf, der wohl nicht völlig unverdient ist – zumindest in der Zeit, bevor wir uns kannten."


label de_L10e:

hi "Hi. Sorry, beachte mich nicht weiter."


"Ich denke, Hanakos Situation sollte so weit wie möglich privat bleiben. Ich weiß nicht, was ihr widerfahren ist, aber mein Bauch sagt mir, dass was immer sie sich zugezogen hat, keine körperliche Krankheit ist."


"Sie braucht keine um sie kreisenden Gerüchte. So weh mir dieser Gedanke auch tut – es wäre ihr vermutlich lieber, ihren Status als seltsames, ignoriertes Mitglied der Klasse zu behalten, als dass man hinter ihren Rücken über sie redet."


"Mädchen" "Wie du meinst."


"Und damit verschwindet sie den Gang hinunter, ohne mich eines weiteren Blickes zu würdigen. Wie unhöflich."


label de_L10f:

show bg school_girlsdormhall onlayer master at right
with charamove

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_doorknock2

"Ich kratze mich am Hinterkopf und starte einen letzten Versuch, doch noch eine Antwort von Hanako zu bekommen. Ich klopfe ein letztes Mal an die Tür."


hi "Hanako, ich bin's nur. Ich soll für Mutou ein paar Zettel abliefern."


"Für eine Weile scheint der Versuch genauso erfolglos wie die vorigen. Gerade als ich die Zettel unter ihrer Tür durchschieben will, höre ich, wie die Türklinke sich bewegt."


play sound sfx_dooropen
with Pause(1.5)

show hanagown distant onlayer master:
    xpos 1.0 xanchor 0.75
with charamoveinright

"Als die Tür sich einen Spalt öffnet, versuche ich so schnell wie möglich zu erkennen, wie es Hanako geht – eine Aufgabe, die durch ihr übergroßes Nachthemd, das den Großteil ihres Körpers verhüllt, nicht gerade erleichtert wird."


"Auf dem ersten Blick sieht sie nicht wirklich krank aus. Aber um ehrlich zu sein, wäre mir das im Vergleich zu ihrem jetzigen Gesichtsausdruck um einiges lieber."


hi "Hi, Hanako. Mutou wollte, dass ich dir die hier gebe, weil du heute nicht im Unterricht warst."


"Ich halte ihr die losen Zettel entgegen, die sie zögernd in ihre Hände nimmt. Ihre Bewegungen sind seltsam gedankenverloren, als wäre sie eher eine Art mechanische Puppe als ein Lebewesen."


hi "Alles… okay? Wenn es dir nicht gut geht, kann ich Doc holen."


"Es ist schon fast erbärmlich, wie ich in einen typischen „Gute Besserung” Monolog herunterrassele – aber mir fällt nichts anderes ein, was ich für sie tun kann."


show hanagown normal onlayer master:
    xanchor 0.7
with dissolvecharamove

"Bei dem Gedanken scheint sie sich etwas zusammenzunehmen… aber nur ein bisschen."


show hanagown distant_blush onlayer master
with charachange

ha "Es geht mir gut."


hi "Okay."


stop music fadeout 6.0

with Pause(2.0)

hide hanagown onlayer master
with charamoveoutright

play sound sfx_doorclose

"Es folgt eine peinliche Stille, die schließlich dadurch gebrochen wird, dass sie zum Abschied nickt und ihre Tür schließt. Diese ganze Erfahrung fühlt sich surreal an."


"Mehr als etwas beunruhigt gehe ich zurück auf mein Zimmer und hoffe darauf, dass es ihr morgen besser gehen wird – auch wenn ich nicht genau weiß, was mit ihr los ist."


scene black onlayer master
with dissolve



label de_L11:

show bg school_girlsdormhall onlayer master at right
with locationchange

"Wieder einmal befinde ich mich vor Hanakos Tür, nachdem sie ein weiteres Mal unerklärlicherweise vom Unterricht ferngeblieben ist."


play sound sfx_doorknock2

"…"


play sound sfx_doorknock2

"…"


"Nichts. Da das bereits der zweite Tag in Folge ist, an dem sie sich so verhält, fange ich an, mir Sorgen um sie zu machen."


"Ich nehme all meine Willenskraft zusammen und beschließe, es ein letztes Mal zu versuchen."


hi "Hanako, wenn du nichts sagst, gehe ich Doc holen."


ha "… Geh weg."


play music music_hanako fadein 10.0

"W… Was? Es ist schwierig zu sagen, ob Depression, Zorn oder beides in ihrer Stimme liegt. Wie in aller Welt kann ich ihr helfen, wenn sie gar keine Hilfe will?"


"Die Botschaft ist glasklar. Nur kann ich einfach nicht zulassen, dass sie tagelang in ihrem Zimmer hockt."


"Während ich gedankenverloren meine Schläfen reibe, ziehe ich mich in mein eigenes Zimmer zurück, um über meine weitere Vorgehensweise nachzudenken. Vernunft ist hier von Nöten, da eine Überreaktion die Dinge nur verschlimmern könnte."


scene bg school_dormhisao onlayer master
with shorttimeskip

"Ich durchwühle Schublade für Schublade meinen Schreibtisch und suche nach dem verdammten Blatt Papier."


"Bevor sie abgereist ist, hat mir Lilly die Nummer aufgeschrieben, über die ich sie anrufen kann, während sie in Schottland ist. Doch gerade wo ich sie brauche, ist dieses verdammte Ding…"


"Ah. Hier."


"Wenn ich es mir genau überlege, hätte ich sie wohl einfach direkt in meinem Handy speichern sollen. Ohne länger zu zögern, tippe ich die Nummer ein und drücke auf „anrufen”."


show phone mobile onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)

"Die Tatsache, dass überhaupt ein Rufzeichen ertönt, zeigt, dass ich zumindest die Vorwahl für Schottland richtig habe. Ich habe noch nie einen internationalen Anruf getätigt, von daher ist das etwas erleichternd."


"Schließlich geht jemand ran. Eine weibliche Stimme, die ich nicht erkenne, ist am anderen Ende der Leitung. Wahrscheinlich ist es Lillys Mutter."


$ renpy.music.set_volume(0.5, 0.2, channel="music")


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


$ renpy.music.set_volume(1.0, 5.0, channel="music")

li "Hallo, hier ist Lilly."


hi "Du klingst furchtbar."


"Sie macht ein Geräusch irgendwo zwischen einem sterbenden Tier und einem Gähnen."


"Eine Sache, die ich noch vor dem Anruf überprüft habe, war die Zeitzone. Dort drüben ist es inzwischen ziemlich später Morgen, daher hat sie nicht wirklich eine Entschuldigung."


hi "Geht's dir nicht gut?"


li "Nur müde. Wie spät ist es bei euch?"


hi "Später Nachmittag. Der Unterricht für heute ist gerade vorbei."


hi "Du bist wirklich kein Morgenmensch, stimmt's?"


li "Du brauchst dich gar nicht darüber lustig zu machen…"


"Ich muss mich zusammenreißen, um bei ihrem wehleidigen Stöhnen nicht loszulachen. Armes Mädchen."


hi "Abgesehen von den Morgenstunden – wie geht's dir dort drüben so?"


li "Bisher ganz gut. Nachdem ich sie so lange nicht gesehen habe, ist es schön, einfach mal wieder mit meinen Eltern zusammen zu essen."


li "Aber der Pool und die schiere Größe des Hauses könnten auch dazu beigetragen haben."


"Es klingt, als ob ihre Familie ziemlich luxuriös lebt. Auch wenn sie nicht in Japan leben, müssen sie für so einen Lebensstil wohl sehr reich sein."


li "Ist bei dir und Hanako alles in Ordnung?"


stop music fadeout 0.3

"Verdammt. Ich hätte nicht gedacht, dass wir so schnell zu diesem Punkt kommen würde."


"Ich überlege einen Moment, wie ich die Lage beschreiben kann, ohne ihr unnötig Sorgen zu bereiten, aber sie bemerkt es, ohne dass ich ein Wort sagen muss."


play music music_moonlight fadein 2.0

li "Hanako geht es nicht gut, nicht wahr?"


hi "Woher weißt du das?"


li "Weil heute ihr Geburtstag ist. Ich hatte gehofft, dass es ihr zumindest ein bisschen besser gehen könnte, nachdem sie dich kennengelernt hat, aber…"


li "Wie geht es ihr gerade?"


hi "Gestern hat sie den Unterricht verpasst, und als ich sie besucht habe, wirkte sie etwas neben der Spur. Heute war sie wieder nicht da und hat mir nur gesagt, dass ich weggehen soll."


hi "Ich weiß wirklich nicht, was ich davon halten soll. Ist das früher schon einmal passiert? Hat es irgendwas mit ihren Narben zu tun?"


li "Bedauerlicherweise ja. In etwa dasselbe passierte letztes Jahr, als ihr Geburtstag anstand."


li "Soweit ich sagen kann, ist es, weil ihre Eltern bei dem Unfall gestorben sind, durch den sie ihre Narben hat, und Hanako gibt sich die Schuld an ihrem Tod."


"Ihre Erklärung klingt einleuchtend. Wenn sie diese Schuldgefühle immer an ihrem Geburtstag bekommt, dann bereut sie vielleicht, überhaupt geboren worden zu sein."


"Aber dass Lilly diesbezüglich fast genauso im Dunklen tappt wie ich, ist eine Überraschung."


hi "Also wohnt sie deshalb im Wohnheim der Schule. Hat sie dir noch mehr über den Unfall erzählt?"


li "So nahe wir uns auch gekommen sind… Sie hat mir nur sehr wenig über die Geschehnisse erzählt. Was ich darüber weiß, sind größtenteils Vermutungen."


"Sie klingt deprimiert, fast niedergeschlagen. Angesichts des Traumas, das Hanako durchgemacht haben muss, kann ich es Lilly nicht wirklich übel nehmen, dass sie es nicht weiß. Nichtsdestotrotz scheint sie es als persönliches Versagen zu sehen."


hi "Mach dir keine Vorwürfe, Lilly. Bei allem, was sie erlebt hat…"


li "Ich weiß. Danke, Hisao. Es tut mir leid, dass ich dir nicht weiterhelfen kann."


hi "Schon okay, ich werde weiter darüber nachdenken. Danke, und hab eine schöne Zeit in Schottland."


li "Ähm, ich…"


hi "Hm?"


li "Ach, nichts. Danke, dass du dich um Hanako kümmerst."


hi "… Okay. Tschüss."


li "Auf Wiederhören."


stop music fadeout 4.0

"Daraufhin wird die Leitung still."


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

"Inmitten der scheinbar nur zunehmenden Anzahl an Fragen, die ich nicht beantworten kann, ist Lillys unbeendeter Satz die brennendste."


"Oh. Oh nein."


"Ich bin ein Idiot. Sie muss gedacht haben, dass ich angerufen habe, um mit ihr zu reden. Aber ich habe nur um Hilfe mit Hanako gebeten."


"Noch beschämender als dieser Gedanke ist die Tatsache, dass sie mit dieser Einschätzung im Großen und Ganzen Recht hat."


"Na ja… Das Wichtigste zuerst. Fürs Erste muss ich die Angelegenheit mit Hanako in Ordnung bringen und sicherstellen, dass sie wirklich anständig isst."


show bg school_girlsdormhall onlayer master
with shorttimeskip

"Die gelegentlich an mir vorbeilaufenden Schüler werfen verstohlene Blicke auf den Essensteller, den ich zum Mädchenwohnheim bringe."


"Es ist nur ein Mikrowellen-Fertiggericht aus dem Mini-Markt – kaum eine Mahlzeit, auf die man stolz sein kann – aber zumindest sollte es sie sattmachen."


show bg school_girlsdormhall onlayer master at right
with charamove

"Schließlich komme ich vor ihrer Zimmertür an, nachdem ich ein paar Mädchen verscheuchen musste, die scherzhaft versucht haben, das Essen zu klauen, das ich so mühevoll beschaffen musste."


"Das Klopfen lasse ich gleich, da es sich als völlig sinnlose Maßnahme herausgestellt hat. Und mit vollen Händen ist es sowieso schwierig."


hi "Hanako, ich bin's, Hisao."


hi "Ich weiß, dass du mich hörst. Ich hab dir etwas zum Essen mitgebracht."


"Stille. Wie erwartet."


hi "Ich lasse es neben deiner Tür. Bitte iss wenigsten was, okay?"


"So. Ich habe meinen Teil getan. Nun ist sie an der Reihe."


show bg school_girlsdormhall onlayer master at center
with charamove

"Nachdem ich den Teller abgestellt habe, laufe ich zurück zu meinem Zimmer, um mein eigenes Abendessen zu essen."


with shorttimeskip

"Als ich zu Hanakos Zimmer zurückkehre, ist gut eine Stunde vergangen."


"Glücklicherweise ist neben ihrer Tür nichts mehr zu sehen. Etwas glücklicher und in der Gewissheit, dass sie etwas isst, laufe ich zurück."


"Wenn sie darauf besteht, das allein zu bewältigen, dann ist es immerhin etwas, ihr helfen zu können – auch wenn es nur auf diese kleine Weise ist."


scene black onlayer master
with dissolve



label de_L12:

scene bg school_library_ss onlayer master
with locationchange

play music music_pearly

"Nach der Schule sitze ich in der Bibliothek und lese. Seite für Seite durchblättere ich mein Buch, ohne wirklich die geschriebenen Wörter zu registrieren."


"Den Kopf auf meine Hand gestützt, bemerke ich das leicht raue Gefühl an meiner Wange. Ich muss mir wohl bald einen Rasierer besorgen."


"Ich gebe das Lesen auf und lasse meinen Kopf einfach auf das Buch vor mir fallen."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

nvl clear
nvl show dissolve

n "\n\n\nDie Dinge haben sich erheblich beruhigt, seit Hanako wieder angefangen hat, den Unterricht zu besuchen."


n "Am ersten Tag, an dem sie wiederkam, haben wir nichts gesagt oder getan, was nicht Teil der täglichen Routine war. Und dabei blieb es auch. Niemand von uns wollte ihren Unfall zur Sprache bringen, also gab es schlichtweg keinen Grund, das Thema anzusprechen."


n "So vergingen einige Tage, an denen sich der Alltag genau wie zuvor fortsetzte."


n "Es ist nur natürlich, dass mein Kopf zu anderen Orten, und noch viel wichtiger, zu anderen Menschen wandert. Das Loch, dass Lilly in Hanakos und meinem Alltag hinterlassen hat, ist nun seit einer Weile so spürbar wie nie zuvor."


n "Wenn ich es in all der Zeit wenigstens geschafft hätte, meine Gefühle für sie zu entschlüsseln… Aber leider hatte ich kein solches Glück."


n "Ebenfalls hilft es nicht, dass viele dieser Versuche zu dem schwierigen Thema Iwanako geführt haben. Jedes Mal, wenn meine Gedanken in diese Richtung abschweifen, versuche ich reflexartig, an etwas anderes zu denken."


$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl clear

nvl hide dissolve

window show

hi "Warum musste das gerade jetzt passieren…"


yu "Ähm…"


show yuuko worried_up_ss onlayer master
with charaenter

"Ich drehe mich um und sehe zum Ursprung der zaghaften Stimme hinter mir auf."


hi "Ah, sorry. Ich wollte niemanden stören."


show yuuko worried_down_ss onlayer master
with charachange

yu "Das… ist es nicht."


hi "Ah…"


"Ich lasse meinen Blick durch den orangegefärbten Raum schweifen und bemerke schnell, wie albern meine Entschuldigung geklungen haben muss. In der Zeit, die ich hier mit Nachdenken und Faulenzen verbracht habe, sind restlos alle gegangen."


hi "Schließt du die Bibliothek?"


show yuuko neurotic_down_ss onlayer master
with charachange

yu "Wenn du nicht gehen willst, kann ich sie noch etwas länger offen lassen. Es ist überhaupt kein Problem."


hi "Keine Sorge, ich sollte sowieso los. Danke."


show yuuko worried_down_ss onlayer master
with charachange

"Als ich aufstehe und langsam loslaufe, spüre ich, wie sich Yuukos Augen in meinen Rücken bohren."


hi "Stimmt etwas nicht?"


show yuuko worried_up_ss onlayer master
with charachange

yu "Du siehst deprimiert aus. Bist du okay?"


"Als sie das sagt, spielt Yuuko nervös mit ihren Fingern. Sie ist sich wohl unsicher, ob sie damit eine Grenze überschreitet. Ich kann nicht wirklich sagen, ob sie sich mehr Sorgen um meine Laune macht oder Angst davor hat, mich zu belästigen."


"Normalerweise würde ich es einfach abtun und ihr versichern, dass es mir gutgeht, doch meine nachdenkliche Stimmung gewinnt die Oberhand. Obwohl sie zum Personal gehört, wirkt sie nicht wirklich wie eine Autoritätsperson wie die anderen."


hi "Es ist nur… Ich glaube, das beste Wort dafür wäre Beziehungsprobleme."


show yuuko worried_down_ss onlayer master
with charachange

yu "Oh. Mit… solchen Dingen kenne ich mich nicht so gut aus. Meine einzige Beziehung endete etwas abrupt."


show yuuko smile_down_ss onlayer master
with charachange

yu "Aber falls du darüber reden willst… Ich meine… könnte ich dir… zuhören. Denke ich."



"Jetzt fühle ich mich irgendwie schlecht, dass ich das erwähnt habe. Allerdings ist sie nicht so alt, darum hat sie zumindest eine gute Chance, einen neuen Partner zu finden."


hi "Wir haben gerade nicht wirklich Probleme. Wir haben als Freunde viele Tage zusammen verbracht. Ausgehen und solche Sachen… so was in der Art."


hi "Doch ich fange an, mehr für sie tun zu wollen; mehr über sie lernen und mehr mit ihr zusammen sein zu wollen. Ich weiß aber nicht, ob es wirklich Liebe ist oder nicht, und mir gefällt eigentlich, wo unsere Freundschaft gerade steht."


show yuuko panic_up_ss onlayer master
with charachange

yu "Du solltest dich davon nicht aufhalten lassen!"


show yuuko worried_down_ss onlayer master
with charachange

yu "Ah… entschuldige."


show yuuko worried_up_ss onlayer master
with charachange

yu "Wie soll ich sagen… ähm…"


show yuuko neutral_down_ss onlayer master
with charachange

yu "Ich finde es gut, dass ihr eine tiefe Freundschaft habt. Aber irgendwann wird die Schulzeit vorbei sein. Hättest du kein Problem damit, nach deinem Abschluss nicht zu wissen, ob aus euch mehr hätte werden können?"


hi "Ich schätze, das ist der Knackpunkt des Problems. Ich habe echt keine Ahnung, was die Antwort auf diese Frage ist."


show yuuko worried_down_ss onlayer master
with charachange

yu "Nun, da kann ich dir nicht wirklich weiterhelfen. Seine wahren Gefühle muss jeder selbst herausfinden. Doch ich denke, wenn du sie liebst, dann solltest du auf jeden Fall etwas sagen."


show yuuko smile_down_ss onlayer master
with charachange

yu "Ich habe viel darüber nachgedacht, und bin zu dem Schluss gekommen, dass es so immer noch besser war, als es nie versucht zu haben – auch wenn meine Beziehung nicht geklappt hat."


"Ich hätte nie gedacht, dass Yuuko so weise klingen kann. Es ergibt Sinn, dass sie mit mehr Lebenserfahrung als ich auch mehr Ahnung davon hat."


"Auch wenn meine Fragen nicht wirklich beantwortet wurden, konnte ich es mir dank ihr von der Seele reden. Ich habe keine Zweifel, dass ich es ihr gestehen sollte, wenn ich Lilly wirklich mag."


"Ich gebe ein leicht frustriertes Seufzen von mir."


hi "Ich wünschte, so viel zu lesen, würde in solchen Situationen etwas helfen…"


show yuuko closedhappy_up_ss onlayer master
with charachange

"Sie kichert mädchenhaft und bestärkt damit meinen Eindruck, dass sie anders als das sonstige Personal hier ist."


stop music fadeout 9.0

nvl clear

window hide
nvl show dissolve

n "\n\n\n\n\n\nLetztendlich kommt alles darauf an, was passiert, nachdem die Schulzeit vorbei ist."


n "Wenn man bedenkt, was vor meinem Wechsel zur Yamaku passiert ist, kommt es mir vor, als müsste ich mit einer Läufermannschaft mithalten, obwohl ich zehn Meter hinter ihnen gestartet bin."


n "Es ist nur ein weiterer Grund, meine Vergangenheit hinter mir zu lassen. Das Letzte, was ich jetzt gebrauchen kann, ist, mich darin zu verlieren und dabei noch Heimweh zu bekommen."


nvl clear
nvl hide dissolve

scene bg school_dormhisao_ss onlayer master
with locationskip
window show

"Wieder einmal rufe ich Lilly an. Meine Telefonrechnung wird sicher schrecklich aussehen – schließlich ist das ein internationaler Anruf."


"Doch das ist es wert. Ich will nicht nur ihren Eindruck von meinem letzten Anruf ausbessern, sondern wirklich wieder mit ihr reden."


scene bg school_dormhisao_blurred_ss onlayer master
show phone mobile onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)

"Als der Hörer endlich abgenommen wird, erkenne ich mühelos die Stimme am anderen Ende."


"Frau Satou" "{image=vfx/garbage.png} {image=vfx/garbage.png} Satou {image=vfx/garbage.png}?"



hi "<Hallo Frau Satou. Könnte ich… äh… mit…>"


"Verdammt. Ich habe vergessen, wie der Satz weitergeht. Nicht wirklich ermutigend, so eine kleine Menge an Wörtern zu vergessen – auch wenn ich nicht lange damit verbracht habe, sie auswendig zu lernen."


hi "Könnte ich bitte mit Lilly sprechen?"


"Frau Satou" "Hallo Hisao. Bringst du dir selbst Englisch bei?"


hi "Nur ein bisschen. Ich glaube, Sprachen liegen mir allgemein nicht so sehr."


"Frau Satou" "Oh, sag doch so etwas nicht. Deine Betonung war gut! Ich gehe Lilly für dich holen, warte einen Augenblick."


"Gehorsam warte ich, während sie Lilly suchen geht und das andere Ende der Leitung still wird."


"Schließlich geht eine viel wacher klingende Lilly als letztes Mal ran. Mittlerweile ist es dort drüben Nachmittag."


play music music_comfort fadein 12.0

li "Hisao, bist du dran?"


hi "Ja, ich bin da. Hi."


li "Guten Tag. Entschuldige, dass ich so lange gebraucht habe. Ich war draußen im Garten."


hi "Gärtnern?"


li "Unglücklicherweise habe ich herausgefunden, dass ich kein Talent dafür habe, darum rieche ich lediglich an den Blumen. Ich denke, meine Finger finden das auch besser."


li "Ich nehme an, Hanako hat sich etwas erholt?"


hi "So ziemlich. Ich habe nur sichergestellt, dass sie isst. Aufgerappelt hat sie sich letztendlich selbst. Danke für deine Hilfe neulich."


li "Ich denke nicht, dass ich eine große Hilfe war. Die Hauptsache ist doch, dass es ihr besser geht."


hi "Richtig. Wie lebt's sich bei dir so? Es klingt, als würdest du in nichts geringerem als einer Villa wohnen."


li "Eine Villa würde ich es nicht nennen…"


"„Aber es ist ziemlich groß” will sie offensichtlich sagen, doch ihre Bescheidenheit zügelt sie. Ich bin ein bisschen neidisch, aber es sind ihre Ferien."


li "Aber es ist ein schönes Haus zum Wohnen. In der Nähe gibt es auch einen Strand, der es Akira besonders angetan hat."


hi "Sie ist eine Schwimmerin?"


li "Sie schleppt mich immer dorthin, um Wettschwimmen zu veranstalten. Die sie auch gewinnt. Jedes Mal."


"Lilly wirkt auf mich alles andere als athletisch, daher scheint es nur logisch zu sein, dass sie kein Ass im Schwimmen ist."


"Ich habe noch nie gesehen, dass sie sich schneller bewegt als bei unseren Spaziergängen von der Schule in das Dorf und zurück, und das ist verständlicherweise ziemlich gemütlich. Irgendwie kann ich sie mir nur schwer beim Schwimmen vorstellen."


hi "Die Strände dort müssen schön aussehen. Zumindest sind sie wohl nicht so überfüllt wie die Strände hier."


li "Durchaus. Akira sagt, die Umgebung hier sieht schöner aus, weil sie weit abseits der Stadt liegt."


"Ich begreife erst, was ich gesagt habe, nachdem die Worte meinen Mund verlassen haben, doch es stört sie ganz und gar nicht."
"Wenn sie nicht da ist, ist es immer noch leicht zu vergessen, dass sie nicht sehen kann – egal wie lange wir schon Freunde sind."


li "Abgesehen davon macht der lokale Akzent die Kommunikation etwas schwierig. Es ist eine permanente Erinnerung daran, dass das hier nicht zu Hause ist."


"Es ist verständlich, dass sie die Residenz ihrer Eltern nicht als ihr Zuhause ansieht, aber dabei fällt mir auf, dass ich mir nicht sicher bin, ob das auch für mich gilt."


"Unser Abschluss ist noch zu weit entfernt, um sich darüber Gedanken zu machen, und ich habe schon so viel Zeit in diesem kleinen Zimmer verbracht, dass ich das Wohnheim überraschend schnell als mein neues Zuhause akzeptiert habe."


hi "Ich schätze, das macht die Verständigung schwieriger. Reichen deine Englischkenntnisse aus?"


li "Glücklicherweise. Ich spreche zwar flüssig Englisch, aber in einer Position zu sein, in der ich es oft benutzen muss, hilft mir, meinen japanischen Akzent loszuwerden. Daher ist es eine gute Übung gewesen."


li "Ich höre, du versuchst dir selbst Englisch beizubringen?"


hi "Eher nur ein paar Zeilen auswendig lernen, wobei ich daran schon gescheitert bin. Ich bin echt nicht dafür gemacht, eine andere Sprache zu lernen."


"Die Zugabe meiner Niederlage bewirkt ein belustigtes Kichern."


li "Ich glaube, es gibt Dinge im Leben, die man sich aussucht, und Dinge, die für einen ausgesucht werden."


li "Du kannst dich zumindest damit trösten, dass du in Naturwissenschaften und Mathe besser bist als ich."


hi "Alles, was mir das gebracht hat, ist, mich zu Mutous Musterschüler zu machen…"


li "Mach dir keine Sorgen deswegen. Das sind nützliche Fähigkeiten für viele Berufe, oder?"


hi "Das erzählt er mir auch. Sein Gesicht hat sich richtig erhellt, als ich ihm erzählt habe, dass ich wahrscheinlich eine Karriere in einem der beiden Felder einschlagen werde."


"Wir beide lachen herzlich über die Ereignisse, die dem jeweils anderen am anderen Ende der Welt widerfahren sind. Es ist schön, und es erinnert mich an unsere kleinen Smalltalks, die ich seit ihrer Abreise vermisst habe."


"Als wir beide darauf warten, dass der andere etwas sagt, entschließe ich mich dazu, meine Gefühle voranzutreiben. Ich kann spüren, wie sich mein Hals etwas zuschnürt."


hi "Wir… ähm…. Ich… vermisse dich."


"Die Stille am anderen Ende der Leitung verrät mir, dass sie den Worten gebührend Gewicht gibt. Doch je länger sie dauert, umso ängstlicher werde ich."


"Gott sei Dank endet die Stille genauso schnell, wie sie gekommen ist."


li "Ich vermisse dich auch, Hisao."


li "Bis bald."


hi "Bis bald, Lilly."


stop music fadeout 6.0

"Wiedereinmal wird der Hörer schlicht und einfach aufgelegt, ohne weiteres Getue."


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

"Diese helle, zögernde und fast schon schüchterne Stimme. Ihr warmer und sanfter Klang… Ich würde mich bloß selbst belügen, wenn ich behaupten würde, dass ich dieses Gefühl nicht einordnen kann."


"Mit Gedanken an Lilly in meinem Kopf fange ich an, mich auf ihre Rückkehr zu freuen. Heute ist ein absoluter Traumtag gewesen."


scene black onlayer master
with dissolve



label de_L13:

scene bg school_scienceroom onlayer master
with locationchange

"Ich sitze in einer weiteren von Mutous langwierigen Vorlesungen, während mein Kopf weit weg von dem Gekritzel auf der dreckigen Tafel wandert."


play music music_tranquil fadein 4.0

nvl clear

window hide
nvl show dissolve

n "\nSeit ich Lilly angerufen habe, ist mein Verstand in zwei Richtungen geteilt. Beide führen im Groben zu derselben Schlussfolgerung: Ich fühle mich seltsam losgelöst von meinem alten Leben."


n "Es ist nur eineinhalb Monate her, dass ich hier angekommen bin. Dennoch ist diese Schule schon mein zweites Zuhause geworden. Ich habe neue Freunde gefunden und Kontakte geknüpft, mich in den Alltag und die Kultur dieser Schule eingelebt, und mich an die Eigenheiten meiner Klassenkameraden gewöhnt."


n "Dass ich mich an eine Schule gewöhnt habe, an der Behinderungen die Norm sind, wundert mich manchmal immer noch, wenn ich darüber nachdenke. Eine Schule, bevölkert mit Brandopfern, Amputierten, Blinden, Tauben und allen möglichen sonstigen Arten von behinderten Schülern."


n "Wenn mir jemand die Schule vor meiner Ankunft beschrieben hätte, hätte ich es als eine übertriebene Einbildung abgetan. Selbst bei meiner Anreise fühlte ich mich wie ein Entdecker, der zum ersten Mal auf dieses seltsame neue Land stößt."


n "Es ist beeindruckend, wie schnell man sich an die Umgebung gewöhnt, in der man gezwungen ist zu leben. Wirklich. Und nun habe ich sogar jemanden gefunden, der mich vollkommen eingenommen hat. Was für ein seltsames Leben."


nvl clear
nvl hide dissolve
window show

"Bevor mein Verstand jedoch noch weiter abschweifen kann, entdecke ich eine Seite mit liniertem Papier, die unter mein Gesicht geschoben wurde. Das grelle, helle Pink lässt keinen Zweifel, dass es von Misha verfasst wurde."


window hide

show misha hips_grin_close onlayer master at offscreenleft
with None

show misha hips_grin_close onlayer master:
    xpos 0.1 xanchor 0.5
show bg school_scienceroom onlayer master at left
with charamove

$ written_note(u"Schau nicht so gelangweilt, Hicchan! Schule ist fast vorbei! Drei-Tage-Wochenende!", text_args={"color":"#FF2AAA"})


window show

"Oh, richtig, wir kriegen Samstag und Montag frei. Über weniger Schule kann ich mich wohl nicht beschweren."


"Ich öffne meinen Stift und kritzle auf das Blatt, bevor ich es ihr heimlich zurückgebe. Ich schiele ab und zu nach vorne, aber Mutou schreibt nur weiter mystische Gleichungen und Formeln an die Tafel."


window hide
$ written_note(u"Ich schätze, du hast etwas geplant?")


show misha perky_smile_close onlayer master
with charachange

window show

"Misha nimmt das Papier zurück kauert sich auf eine selbst für sie komische Weise darüber, während ihre Zunge aus ihrem Mundwinkel hervortritt. Hat sie meinen Gesichtsausdruck als deprimiert interpretiert und versucht mich nun aufzumuntern?"


window hide

show misha sign_smile_close onlayer master
with charachange
$ written_note(u"Schülerratsarbeit mit Shicchan natürlich.", text_args={"color":"#FF2AAA"})


$ written_note(u"Ihr seid mir deswegen aber nicht immer noch böse, oder?")


show misha hips_frown_close onlayer master
with charachange
$ written_note(u"Aber Hicchan hätte uns armen, einsamen Mädels helfen können.", text_args={"color":"#FF2AAA"})


$ written_note(u"Ich würde euch heute zur Hand gehen, wenn ich nicht selbst beschäftigt wäre.")


show misha hips_grin_close onlayer master
with charachange

$ written_note(u"Ooh, böser böser Hicchan!", text_args={"color":"#FF2AAA"})


$ written_note(u"Ich gehe lediglich mit Hanako Lilly abholen. Ich weiß nicht, was dir durch den Kopf schwirrt.")


show misha perky_smile_close onlayer master
with charachange

$ written_note(u"Also kommt Lilly zurück?", text_args={"color":"#FF2AAA"})


$ written_note(u"Ja, sie kommt mit dem Abendflug zusammen mit ihrer Schwester, also wird sie nächste Woche wieder in der Schule sein.")


show misha hips_grin_close onlayer master
with charachange

window show

"Als sie den Zettel an sich nimmt und anfängt zu schreiben, sehe ich auf und bemerke etwas sehr Unangenehmes."


stop music fadeout 2.0

show muto irritated behind misha onlayer master at Alphain(1.0), Slide(0.8, 0.5, 0.6, 0.5, 1.0)
with Pause(0.5)

"Während ich hektisch versuche, still Mishas Aufmerksamkeit zu bekommen, schreitet Mutou siegessicher durch die Lücke zwischen den Tischen der ersten Reihe, während er seinen Blick auf sie fokussiert hat."


show misha perky_confused_close onlayer master
with charachange

"Plötzlich hört sie auf zu schreiben, als seine lange Gestalt einen unmöglich langen Schatten über die Seite wirft."


show misha sign_confused_close onlayer master
with charachange

mi "Ah… Ich…"


"Schweigend nimmt er ihr das Stück Papier ab und beginnt zu lesen."


"Schweißperlen. Ich schaue mich kurz im Klassenzimmer um und bemerke die vollkommene Stille. Natürlich – das ist wohl das Einzige, das während des Unterrichts wirklich ihre Aufmerksamkeit erlangt."


play sound sfx_impact
show misha perky_sad_close onlayer master
with vpunch

"Nachdem er die Seite ein paar Sekunden untersucht hat, rollt er das Papier zu einem kleinen Rohr und haut Misha damit leicht auf den Kopf."


show muto normal onlayer master
with charachange

mu "Noch eine halbe Stunde bis du dich zum Schülerrat verkrümeln kannst. Ich denke, du kannst es bis dahin aushalten."


play music music_ease

"Mishas Gesicht verzieht sich, als die gesamte Klasse in Gelächter ausbricht. Er mag vielleicht unbeholfen sein, aber er weiß ganz genau, wie er mit ihr umgehen muss."


"Wahrscheinlich würde sie mir leidtun, wenn ich nicht damit zu tun hätte, mein eigenes Lachen zu ersticken."


scene bg hosp_ext onlayer master at right
show hanako basic_distant_cas onlayer master at center
with shorttimeskip

play ambient sfx_rooftop fadein 2.0

ha "Hisao, ist es dieses?"


hi "Nein, ich glaube, das ist eine ausländische Airline."


"Und so setzt das dritte Flugzeug, auf dem sie nicht sind, zur Landung an."


"Die letzte halbe Stunde haben wir uns mit sinnlosem Geschwätz die Zeit vertrieben. Lillys und Akiras Flug hat sich verspätet – und wenn es so weitergeht, wird es dunkel sein, bis ihr Flugzeug ankommt."


show hanako def_worry_cas onlayer master at twoleft
with shorttimeskip

ha "Ist es dieses?"


hi "Nein, die Farben stimmen nicht."


show hanako basic_distant_cas onlayer master
with charachange

show hanako basic_normal_cas onlayer master
with charachange

"Hanakos Augen springen von links nach rechts und folgen den hinein- und herausströmenden Menschen hinter dem großen Glas vor uns."
"Glücklicherweise beachtet sie kaum jemand, da deren Aufmerksamkeit offenbar auf wichtigere Dinge gerichtet ist."


show hanako emb_timid_cas onlayer master at tworight
with shorttimeskip

ha "Vielleicht ist es dieses?"


hi "Nein, ich glaube, das… Moment mal – ich glaube, das könnte es sein."


show hanako cover_distant_cas onlayer master at center
with shorttimeskip

"Die Anzeigetafel schaltet ihren Flugstatus auf „gelandet” um; trotzdem müssen wir noch einige Zeit warten."


"Ein lautes Gähnen überkommt mich, sodass ich es nicht rechtzeitig schaffe, es zurückzuhalten."
"Mein Schlafrhythmus ist – mal wieder – vollkommen aus den Fugen geraten; wahrscheinlich wegen des Mix aus Sorge um Hanako und den Nebenwirkungen meiner Medikamente."


show hanako emb_smile_cas onlayer master
with charachange

ha "Hisao, dort drüben…"


"Ich sehe zu Hanako und folge dann ihrem Blick zur Flughafentür."


aki "Hmm? Oh, Lilly, sie sind da!"


li "Wirklich?"


show akira basic_smile onlayer master:
    xanchor 0.5 xpos -0.3
show lilly basic_cheerful onlayer master at offscreenleft
with None

show akira basic_smile onlayer master at left
show lilly basic_cheerful_cas onlayer master:
    xanchor 0.5 xpos 0.4
show hanako emb_smile_cas onlayer master at tworight
show bg hosp_ext onlayer master at center
with charamove

"Wir begrüßen uns gegenseitig, wobei wir uns rasch an die Seite stellen, um die nachfolgenden Passagiere nicht zu blockieren."


ha "Lilly!"


show hanako emb_downsmile_cas onlayer master at center
with dissolvecharamove

"Hanako springt nach vorn, um Lilly zu umarmen. Das breite Lächeln auf ihrem Gesicht reicht aus, um ihre Freude über Lillys Rückkehr erkennen zu lassen. Lilly lächelt einfach zurück und begrüßt sie mit einer sanften Stimme."


show lilly basic_smileclosed_cas onlayer master
with charachange

li "Es ist wundervoll, dich wiederzusehen, Hanako."


show akira basic_smile onlayer master at twoleft
show lilly basic_smileclosed_cas onlayer master:
    xpos 0.6
show hanako emb_downsmile_cas onlayer master at tworight
show bg hosp_ext onlayer master:
    xpos 0.55
with charamove

"Während die zwei sich gegenseitig umarmen – wohlverdient nach allem, was nach ihrer Abreise passiert ist – wende ich mich Akira zu."


show akira basic_ending onlayer master
with charachange

aki "Yo."


hi "Ihr seid ziemlich spät dran."


show akira basic_annoyed onlayer master
with charachange

aki "Ja, es gab einen wirklich heftigen Sturm über dem Flughafen. Selbst auf dem kurzen Weg vom Bus zum Flugzeug sind wir klatschnass geworden."


hi "Dann schätze ich, dass dir das Wetter hier besser gefallen wird. Willkommen zurück, Lilly."


stop music fadeout 4.0

show hanako basic_smile_cas onlayer master:
    xpos 0.8
show akira basic_smile onlayer master
show lilly basic_weaksmile_cas onlayer master
with dissolvecharamove

"Hanako löst sich von Lilly, als ich spreche. Für eine lange Zeit sagt keiner von uns ein Wort."


"Entgegen meiner eigentlichen Vorstellung, wie ihre Rückkehr ablaufen würde, herrscht eine peinliche, fast erdrückende Atmosphäre. Wir beide versuchen, die Gefühle des jeweils anderen zu erraten, wobei wir uns nicht sicher sind, was wir sagen sollten."


"Verdammt. Genau das hatte ich befürchtet, als ich daran gedacht habe, die Dinge zwischen uns voranzutreiben."
"Lilly fährt mit ihrer Hand durch ihr blondes Haar und wickelt verlegen eine ihrer Ponysträhnen um ihre Finger. Eindeutig versucht sie herauszufinden, wie sie am besten reagieren soll."


"Glücklicherweise gibt Lilly schließlich ein kleines Seufzen von sich und bricht das Schweigen."


show lilly basic_smile_cas onlayer master
with charachange

play music music_lilly fadein 6.0

li "Danke, Hisao. Es ist schön, wieder da zu sein."


show hanako basic_worry_cas onlayer master
with charachange

ha "Geht es euch gut? Ihr seht müde aus."


"Obwohl sie offensichtlich nicht so auf der Höhe ist, winkt sie zügig ab, um jegliche Bedenken zu zerstreuen, die Hanako ihretwegen haben könnte."


show lilly basic_weaksmile_cas onlayer master
with charachange

li "Mir geht es gut. Wirklich. Es ist nur etwas Jetlag."


show akira basic_laugh onlayer master
with charachange

aki "Schwach."


hi "Hast du keinen?"


show akira basic_ending onlayer master
with charachange

"Sie zeigt lediglich ein breites Grinsen und streckt ihre bescheidene Brust heraus."


aki "Mir geht's total gut!"


show lilly basic_sleepy_cas onlayer master
with charachange

li "Das ist nicht fair…"


show akira basic_smile onlayer master
show hanako basic_normal_cas onlayer master
with charachange

aki "Haha, ach na ja. Sollte nicht zulange dauern, bis du es los bist."


show lilly basic_smile_cas onlayer master
with charachange

li "Ah! Stimmt ja – Hisao?"


hi "Ja?"


show lilly basic_smileclosed_cas onlayer master
with charachange

li "Haben wir nicht bald ein paar Tage schulfrei?"


hi "Ich hätte es vergessen, wenn Misha mich heute morgen nicht daran erinnert hätte. Wir haben ab morgen ein Drei-Tage-Wochenende."


show akira basic_laugh onlayer master
with charachange

"Mit einem Grinsen stößt Akira scherzhaft ihren Ellenbogen in Lillys Seite."


show akira basic_smile onlayer master
with charachange

aki "Hab dir doch gesagt, dass du es nicht verpassen würdest."


hi "Hast du etwas geplant?"


show lilly basic_smile_cas onlayer master
with charachange

li "Wenn ihr Zwei noch nichts vorhabt…"


hi "Ich hab nichts vor, also würde mich über etwas zu tun freuen. Hanako?"


show hanako basic_smile_cas onlayer master
with charachange

ha "Nein, nichts."


show lilly basic_cheerful_cas onlayer master
with charachange

li "Das ist gut. Ich dachte mir, wir könnten über dieses Wochenende zu dem Sommerhaus meiner Familie fahren. Allerdings haben wir es in letzter Zeit kaum benutzt, darum müssten wir es etwas auf Vordermann bringen, während wir da sind."


hi "Oh? Wo steht es?"


show akira basic_ending onlayer master
with charachange

aki "Im Norden, auf Hokkaido. Die Gegend ist praktisch verlassen, daher sollte es für euch eine angenehme, ruhige Auszeit sein."


hi "Kommst du nicht mit?"


show akira basic_smile onlayer master
with charachange

aki "Nee. Ich hab selber einen kleinen Urlaub mit meinem Freund geplant."


"Ich sehe sie mit zusammengekniffen Augen an. Was sie wohl im Schilde führt?"


hi "Es klingt, als würden wir nur das Sommerhaus für dich aufräumen."


show lilly basic_displeased_cas onlayer master
with charachange

li "Das… ist vielleicht eine berechtigte Schlussfolgerung…"


"Als wir uns beide auf Akira einschießen, weicht sie unseren Blicken aus. Sieht aus, als lägen wir richtig."


show akira basic_boo onlayer master
with charachange

aki "Das ist nur ein glücklicher Zufall. Ehrlich. Ich und der Kerl haben es das letzte Mal in ziemlich gutem Zustand hinterlassen. Versprochen."


show akira basic_smile onlayer master
with charachange

aki "Also dann, ich mach 'nen Abflug."


show lilly basic_reminisce_cas onlayer master
with charachange

li "Schon? Akira…"


"Sie dreht sich rasch um und zieht mit erhobener Hand von dannen."


show akira basic_laugh onlayer master
with charachange

aki "Ich seh euch in ein paar Tagen, Leute."


show akira basic_laugh onlayer master at Alphaout(1.0), offscreenleft
with charamove

hide akira onlayer master
with None

show lilly basic_reminisce_cas onlayer master:
    xpos 0.4
show hanako basic_smile_cas onlayer master:
    xpos 0.6
show bg hosp_ext onlayer master at bgleft
with charamove

"Lilly und ich können wegen ihres hastigen Rückzugs nur seufzen."


show hanako cover_bashful_cas onlayer master
with charachange

ha "Es klingt, als wäre es ein schöner Ort für einen Urlaub."


show lilly basic_smileclosed_cas onlayer master
with charachange

"Lilly nickt enthusiastisch, während sie ihre Tragetasche in die Hand nimmt. Als wir uns dann auf den Weg zum Taxistand machen, legt sie die andere Hand auf Hanakos Schulter, um geführt zu werden."


"Nach dem Tumult der letzten paar Tage wäre es ein Traum, ein Wochenende mit ihr und Lilly allein auf dem Land zu verbringen."


"Je mehr ich darüber nachdenke, desto sicherer bin ich mir. Das wird der richtige Ort und der Zeitpunkt sein, um ihr mein Gefühle zu gestehen."


stop music fadeout 2.0
stop ambient fadeout 2.0

scene black onlayer master
with dissolve



label de_L14:

scene bg city_station onlayer master
with locationchange

play music music_daily fadein 7.0

"Mein Körper fröstelt in der morgendlichen Kühle. Wir stehen auf dem Bahnsteig, und ich versuche verzweifelt, die Kälte zu lindern, indem ich in meine gewölbten Hände hauche."


"Lillys Kleidung sieht für die Temperaturen um uns eher unpassend aus. Ich kann nur hoffen, dass man dadurch auf das Wetter schließen kann, das sie an unserem Ziel erwartet."


show lilly basic_sleepy_cas onlayer master at twoleft
show hanako basic_distant_cas onlayer master at tworight
with charaenter

hi "Verdammt, Lilly, warum mussten wir so früh hier sein?"


show lilly basic_displeased_cas onlayer master
with charachange

li "Leider ist der Zug-Fahrplan ungünstig für uns. Der nächste Zug nach Hokkaido kommt erst um zwei Uhr nachmittags."


hi "Klasse. Einfach klasse."


"Ich halte einen Moment inne, um mir den Schlaf aus den Augen zu reiben. Lilly nutzt diese Gelegenheit."


show lilly basic_weaksmile_cas onlayer master
with charachange

li "Kopf hoch, Hisao. Sobald wir da sind, wird es viel wärmer werden."


hi "Warum fahren wir nicht einfach mit dem Hochgeschwindigkeitszug? Ein normaler Zug wird Stunden brauchen, um uns dorthin zu bringen, also könnten wir genauso gut mit dem Shinkansen so weit wie möglich nach Norden fahren und dann umsteigen."


show lilly basic_smile_cas onlayer master
with charachange

li "Ältere Züge haben einen gewissen Charme an sich, findest du nicht auch?"


hi "Ich würde zustimmen, wenn ich nicht in der Morgenkälte erfrieren würde, weil wir beschlossen haben, mit eben so einem zu fahren."


show hanako emb_timid_cas onlayer master
with charachange

ha "Es… tut mir leid, Hisao."


hi "Es tut dir leid? Was denn?"


show hanako emb_downtimid_cas onlayer master
with charachange

ha "Ich war… diejenige, die vorgeschlagen hat, einen normalen Zug zu nehmen."


"Na toll, jetzt fühle ich mich auch noch, als hätte ich einen Welpen getreten. Alles, was ich tun kann, ist seufzen und mein Gesicht mit meiner Hand zu bedecken."


hi "Schon okay, ich bin nur mürrisch."


show lilly basic_ara_cas onlayer master
with charachange

li "Na na, Hanako, du musst nicht die ganze Schuld auf dich nehmen. Auch ohne deinen Vorschlag hätte ich für diesen Zug gestimmt."


show hanako emb_smile_cas onlayer master
with charachange

hide hanako onlayer master
hide lilly onlayer master
with charaexit

"Dankbar wegen Lillys schnellem Einschreiten lasse ich einen kurzen Blick über den Bahnhof schweifen."


"Abgesehen von uns ist er wie ausgestorben, sodass sich der Morgentau auf den leeren Bänken sammelt. Ich schätze, niemand sonst war masochistisch genug, dem sehr frühen Morgen zu trotzen."


"Wenn es aber jemand täte, würde er die gewaltigen Taschen, die Lilly und Hanako mitgenommen haben, mehr als nur bemerken."


hi "Was habt ihr überhaupt in diese Dinger eingepackt?"


show lilly basic_listen_cas onlayer master at center
with charaenter

li "In die Taschen? Hmm…"


"Sie hält einen Moment inne und neigt gedankenversunken ihren Kopf."


show lilly basic_smileclosed_cas onlayer master
with charachange

li "Wechselwäsche, Regenmantel, Unterwäsche, Schlafanzug, ein paar Bücher… Ich glaube, das müsste alles sein."


hi "Du lässt es klingen, als wäre ich unvorbereitet."


show lilly basic_surprised_cas onlayer master
with charachange

li "Hast du weniger mitgenommen?"


hi "Unterwäsche und ein Kartenspiel. Das war's."


"Und meine Tabletten, aber egal."


li "Kein Pyjama?"


hi "Verdammt. Ich wusste, dass ich etwas vergessen habe."


"Als ich mir frustriert die Haare raufe, seufzt Lilly."


show lilly basic_weaksmile_cas onlayer master
with charachange

li "Es sollte dort Kleidung geben, die du benutzen kannst. Immerhin fährt Akira ab und zu dorthin, und ich glaube, etwas Kleidung meiner Eltern ist noch im Schrank."


show lilly basic_smile_cas onlayer master
with charachange

li "Ich denke nicht, dass es im Fall der Fälle ein Problem wäre, wenn du dir einen Pyjama ausleihen würdest."


hi "Danke. Aber trotzdem hab ich nichts dagegen, einfach in meinen normalen Klamotten zu schlafen."


show lilly basic_surprised_cas onlayer master
with charachange

li "Zwei Tage lang?"


hi "Da ist was dran."


"Nicht wirklich. Auch wenn zwei Tage grenzwertig sind, liegt es mehr daran, dass es in der Anwesenheit von zwei Mädchen inakzeptabel wäre, auch nur ein bisschen wie ein Schmutzfink auszusehen."


hide lilly onlayer master
with charaexit

"Während wir uns auf der Bahnhofsplattform entspannt unterhalten, ertönt eine Ankündigung aus den Lautsprechern, die laut die Ankunft unseres Zuges verkündet."


"Als ich an Lilly und Hanako vorbeischaue, ist der Zug jedoch noch außer Sichtweite. Ein kurzer Blick auf meine Uhr genügt, um zu sehen, dass es unserer ist."


hi "Der Zug um fünf Uhr dreißig war unserer, oder?"


show lilly basic_smileclosed_cas onlayer master at twoleft
show hanako basic_distant_cas onlayer master at tworight
with charaenter

li "Korrekt."


hi "Wollt ihr beide, dass ich eure Taschen trage? Meine ist nicht wirklich schwer."


show lilly basic_ara_cas onlayer master
with charachange

li "Na so was, du bist ja ein richtiger Gentleman, Hisao."


hi "Jetzt gib dich nicht so widerwillig."


"Als ich mich nach unten beuge, um Lillys große Tasche aufzuheben, sehe ich, wie Hanako ihre eigene aufhebt."


hi "Schaffst du das?"


show hanako basic_normal_cas onlayer master
with charachange

"Ein stilles Nicken ist die einzige Antwort. Ich bekomme langsam das Gefühl, als könnte ich am Ende des Ausflugs Hanakos ausgesprochene Sätze an einer Hand abzählen."


stop music fadeout 5.0
play ambient sfx_trainint fadein 5.0

$ ksgallery_unlock("ev lilly_trainride")
scene train_scenery onlayer master
show train_scenery_fg onlayer master
show evfg lilly_trainride onlayer master at train_shake
with shorttimeskip

"Ich versuche, die am Fenster vorbeiziehende Morgenlandschaft und das gelegentlichen Geklapper des Zuges zu ignorieren, während ich meine Aufmerksamkeit auf die in die Jahre kommenden Spielkarten in meiner Hand konzentriere."


hi "Ich erhöhe um fünf."


ha "Ähm… Ich…"


"Sie verzieht ihr Gesicht und lehnt sich verschwörerisch zu Lilly, woraufhin die beiden sich flüsternd austauschen. Wenn man bedenkt, wie oft das bis jetzt passiert ist, fange ich an, Hanakos Verständnis für das Pokerspielen anzuzweifeln."


"Lilly scheint es aber nicht beim Lesen zu stören. Ihre Hände huschen über jede Seite, was nur durch die gelegentlich notwendigen Korrekturen wegen des Geholpers und Schaukelns des Zuges unterbrochen wird."


"Meine Sammlung von Schachfiguren, die wir als Chips verwenden, wächst sowieso stetig. Darum stört es mich nicht wirklich."


"Ich sehe mich um. Unser Waggon ist fast so leer wie der Bahnhof, wo wir auf den Zug selbst gewartet haben. Nur ein Handvoll Menschen sind zu sehen, die größtenteils wie Touristen oder Pärchen im Urlaub aussehen."


"Während die beiden ihre nicht-wirklich-geheime Strategieplanung fortsetzen, schaut ein kleiner Junge über den Sitz und starrt mich an. In der Hoffnung, dass er nicht anfängt, Hanako anzustarren, winke ich und lächle ihm kurzum zu."


"Glücklicherweise rutscht er in seinen Sitz zurück, nachdem er mich zu langweilig findet, um seine Aufmerksamkeit an mich zu verschwenden."


ha "Ich gehe mit und erhöhe… um weitere fünf."


hi "Verdammt, du hast mich. Ich steige aus."


"Ich habe geblufft, und sie hat mich ertappt. Mit hängendem Kopf schiebe ich einen großen Teil meiner Gewinne hinüber."


$ ksgallery_unlock("ev lilly_trainride_smiles")
show evfg lilly_trainride_smiles onlayer master at train_shake
with charachange

"Hanako sieht vollkommen begeistert aus, und selbst wenn Lilly sich weiterhin auf ihr Lesematerial konzentriert, kann ich das Schmunzeln auf ihrem Gesicht sehen. Sie sind beide äußerst erfreut."


"Für einen Moment versuche ich zu ergründen, was Lilly gerade liest, doch das Cover ist so verblichen, dass ich nur erkennen kann, dass es lateinische Schrift ist. Schade, dass ich das Braille über dem aufgedruckten Titel nicht lesen kann."


hi "Was liest du da, Lilly? Vom Titel her sieht es nach Englisch aus."


li "Das ist richtig. Das ist „Zehn Kleine Negerlein” – eine alte britische Geschichte. Ich könnte dir etwas vorlesen, wenn du willst."


"Sie bietet es mir mit einem Grinsen an, offensichtlich war das als Scherz gemeint."


hi "Ich denke, ich passe. Danke."


stop ambient fadeout 2.0

scene bg hok_houseext onlayer master at Fullpan(10.0, dir="left")
with shorttimeskip

play music music_tranquil fadein 3.0
play ambient sfx_parkambience fadein 4.0

"Nach einer scheinbar endlosen Reise stehen wir letztendlich vor der ersehnten Türschwelle des Satou Sommerhauses. Selbst nach der Zugfahrt schien der Fußweg dorthin ewig zu dauern."


"Aber trotz meiner Nörgeleien hätte ich nie gedacht, dass uns am Ende dieser langen, verlassenen Straße dieser Anblick bevorsteht."


"Es sieht eher wie ein Landhaus aus als das gewöhnliche Haus, das ich mir vorgestellt hatte. Es ist klein und umringt von Bäumen und Büschen."


"Ein weite Fläche von Kornfeldern ist zu sehen, als wir darauf zulaufen. Der Zaun besteht nur aus klapprigen alten Holzbrettern."


"Es macht einem klar, wie weit wir eigentlich von großen Städten entfernt sind. Es ist das genaue Gegenteil der Umgebung, in der ich aufgewachsen bin."


"Das Einzige, was mich nicht überrascht, ist der westliche Stil."


show bg hok_houseext onlayer master at left
with None

hi "Wow, es ist erstaunlich…"


show lilly basic_smileclosed_cas onlayer master at twoleft
show hanako basic_bashful_cas onlayer master at tworight
with charaenter

ha "Mhm, es ist wundervoll."


show lilly basic_smile_cas onlayer master
with charachange

li "Das ist schön zu hören. Obwohl Akira sagte, dass sie das Haus in vernünftigem Zustand gehalten hat, war ich in Sorge, dass wir vielleicht verschiedene Ansichten von „vernünftig” haben."


hi "Es sieht aus, als wäre kilometerweit keine Menschenseele außer uns. Ich dachte, Akira wäre der Typ, der sich eher in Städten aufhält."


show lilly basic_listen_cas onlayer master
with charachange

"Lilly legt gedankenversunken die Stirn in Falten. Scheinbar erinnert sie sich an fast vergessenes Wissen."


show lilly basic_weaksmile_cas onlayer master
with charachange

li "Hmm, mein Gedächtnis sagt mir, dass es nicht weit voraus ein kleines Dorf gibt. Ansonsten ist es aber größtenteils nur altes Farmland."


show lilly basic_smile_cas onlayer master
with charachange

li "Akira und ich wohnten eine Weile im Haus unserer Eltern in der nächsten Stadt, aber nachdem sie aber weggezogen sind, haben wir uns entschieden, in ein kleineres, pflegeleichteres Haus zu ziehen."


hi "Heutzutage ein Haus wie dieses in Japan zu finden… Es ist irgendwie anachronistisch."


show lilly basic_smileclosed_cas onlayer master
with charachange

li "Nun, dieses Dorf hat ziemlich viel Geschichte."


"Ich schaue ein letztes Mal die Straße hinunter, bevor ich auf die anstehende Aufgabe zurückkomme."


hi "Wollen wir dann reingehen? Ich bin am verdursten."


show hanako basic_normal_cas onlayer master
with charachange

ha "Es war ein weiter Fußweg hierher."


show lilly basic_smile_cas onlayer master
with charachange

"Lilly nickt enthusiastisch, woraufhin wir unsere Taschen ins Haus schleppen."


stop ambient fadeout 1.0
$ renpy.music.set_volume(0.7, 1.0, channel="music")

scene bg hok_lounge onlayer master
with locationchange

"Sobald wir das Haus betreten, fangen Hanako und ich an, uns umzusehen. Wir nehmen jedes Detail von dem Ort auf, an dem wir die nächsten paar Tage verbringen werden."


"All die Artefakte des Leben eines Anderen liegen wie von der Zeit eingefroren im Haus herum – zum Beispiel die Fernsehzeitung, die neben dem Tresen auf dem Boden liegt, und die Pfannen in der angrenzenden Küche, die immer noch auf dem Herd stehen."


"Es ist wirklich ein seltsames Gefühl – als ob wir für einen kurzen Moment in Akiras Leben treten, bevor wir in ein paar Tagen genauso abreisen, wie wir gekommen sind."
"Natürlich ist die banalere Realität, dass sie hinter sich einfach nicht so richtig aufgeräumt hat."


hi "Wo sollen wir unsere Taschen hinstellen?"


show lilly basic_smileclosed_cas onlayer master at twoleft
show hanako basic_normal_cas onlayer master at tworight
with charaenter

li "Ich zeige Hanako unser Schlafzimmer. Du kannst deine hier hinstellen, wenn du willst."


hi "Du meinst, ich schlafe nicht mit euch Zweien in einem Zimmer?"


show hanako emb_blushing_cas onlayer master
show lilly basic_emb_cas onlayer master
with charachange

"Hanako läuft knallrot an, während Lilly eine Hand an die Wange legt."


show lilly basic_ara_cas onlayer master
show hanako emb_emb_cas onlayer master
with charachange

li "Meine Güte, wie kühn."


"Ihr Zwei…"


hi "Warte mal, wenn ich meine Tasche hierlassen soll – wo schlafe ich dann?"


show lilly basic_weaksmile_cas onlayer master
with charachange

li "Na ja, da wir kein Gästezimmer haben…"


hi "Der Futon, oder?"


show lilly basic_concerned_cas onlayer master
with charachange

li "Tut mir leid, Hisao."


"Ich seufze und gebe so meinem Missfallen über meinen letzten Platz auf der Schlafplatz-Rangliste Ausdruck."


hi "Ich schätze, ich habe keine Wahl."


hide lilly onlayer master
hide hanako onlayer master
with charaexit

"Lilly geht, um Hanako ihr Schlafzimmer zu zeigen, daher stelle ich meine Tasche auf den Boden und mache eine kleine Tour durch das Haus."


scene bg hok_kitchen onlayer master
with locationchange

"Die Küche ist recht bescheiden, genauso wie das Wohnzimmer. Das rustikale Ambiente der hölzernen Möbel macht mir klar, wie weit wir eigentlich von der Zivilisation entfernt sind."


scene bg hok_lounge onlayer master
with locationchange

"Als ich wieder ins Wohnzimmer gehe, beschließe ich, den Fernseher auszuprobieren, bis die beiden zurück sind. Mit einem Tastendruck auf der Fernbedienung erwacht er zum Leben. Anscheinend ist er auf den Nachrichtenkanal eingestellt."


"Nachdem ich mich mehr fallen lasse, als dass ich mich hinsetze, lehne ich mich zurück und schaue."


stop music fadeout 5.0
$ renpy.music.set_volume(1.0, 8.0, channel="music")

"Und schaue."


"Und schaue…"


window hide

scene black onlayer master
with shuteye

with Pause(4.0)

window show

ha "Hisao…"


play ambient sfx_cicadas fadein 5.0

scene bg hok_lounge_ni onlayer master
show lilly basic_smileclosed_cas onlayer master at twoleft
show hanako basic_normal_cas onlayer master at tworight
with openeye

"Schnell blinzelnd wache ich auf. Lilly und Hanako sind wiedergekommen – ohne ihre Taschen."


"Dem Hokkaido-Nachthimmel außerhalb der Fenster nach zu urteilen, bin ich wohl eingeschlafen. Ein Blick auf die Uhr an der Wand verrät mir, dass es bereits zehn ist."


show lilly basic_weaksmile_cas onlayer master
with charachange

li "Wie es aussieht, hast du den Fernseher ja schon gefunden."


hi "Ja. Hier ist es echt gemütlich."


show lilly basic_smile_cas onlayer master
with charachange

li "Freut mich, dass es dir gefällt."


show lilly basic_giggle_cas onlayer master
with charachange

li "Du hast schon tief und fest geschlafen, als wir vom Auspacken unserer Sachen zurückgekommen sind, darum haben wir es nicht übers Herz gebracht, dich sofort zu wecken."


"Ihrem Kichern nach zu urteilen, muss ich mich lustig anhören, wenn ich schlafe. Prompt beschließe ich, nicht nachzufragen."


show hanako emb_smile_cas onlayer master
with charachange

ha "Abendessen steht für dich in der Küche…"


show hanako emb_downtimid_cas onlayer master
with charachange

"Hanako gähnt herzhaft und erinnert sich gerade noch daran, ihren Mund zu bedecken."


show lilly basic_weaksmile_cas onlayer master
with charachange

li "Oh je, bist du müde?"


show hanako emb_timid_cas onlayer master
with charachange

ha "Ah, mhm. Ich habe letzte Nacht nicht viel geschlafen."


hi "Ich bin auch ziemlich müde. Es war ein langer Fußweg hierher, und es wird langsam spät."


show lilly basic_smileclosed_cas onlayer master
with charachange

li "Wenn das so ist, dann sollten wir für heute wohl Schluss machen. Gute Nacht, Hisao."


show hanako basic_smile_cas onlayer master
with charachange

ha "Gute Nacht."


hi "Nacht."


hide hanako onlayer master
hide lilly onlayer master
with charaexit

"Daraufhin drehen sie sich leise um und gehen zurück zu ihrem Schlafzimmer."


"Während ich meine Augen reibe, seufze ich. Ob ich wieder einschlafen kann, nachdem ich gerade erst aufgeweckt wurde?"


"Ich denke, ich werde etwas essen und leise etwas weiter Fernsehen gucken, bevor ich ins Bett gehe."


stop ambient fadeout 2.0

scene black onlayer master
with dissolve



label de_L15:

scene black onlayer master
with dissolve

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 6.0

ha "Schläft er immer noch?"


li "Ich glaube schon."


"Tue ich nicht. Aber ich bin irgendwie unglaublich müde."


ha "Der Morgen ist fast vorbei…"


"Das weiß ich."


li "Wahrscheinlich ist er aufgeblieben, um fernzusehen. Ich konnte es von unserem Schlafzimmer aus hören."


"Nur weil ich nicht einschlafen konnte."


ha "Sollten wir ihn aufwecken?"


"Tu das nicht, Hanako. Bitte."


li "Nein, wir sollten ihn schlafen lassen. Ich bezweifle, dass er früh aufgeweckt werden will, wenn er nachts kaum Schlaf bekommen hat."


"Ich danke dir, Lilly."


li "Außerdem klingt er so friedlich. Es wäre eine Schande, ihn jetzt zu wecken."


"Verzieh keine Miene, Hisao. Allerdings ist es schön, dass sie sich so sorgt."


ha "Ähm…"


li "Hanako, könntest du zum Kühlschrank gehen und herausfischen, was wir brauchen, um Mittagessen zu machen?"


ha "In Ordnung. Nur das Gemüse und den Reis?"


li "Mhm, das sollte genug sein. Wir brauchen nur etwas Einfaches, weil wir später im Dorf essen können."


"Hanakos Schritte sind auf dem Teppichboden zu hören und bewegen sich weg vom Wohnzimmer. Während sie das tun, kann ich Lillys Hand sanft auf meiner Brust spüren."


"Nicht zu reagieren, kostet mich übermenschliche Anstrengung, aber irgendwie glaube ich, dass sie trotzdem weiß, dass ich wach bin."


"Eine lange Stille vergeht."


"Der einzige Gedanke in meinem Kopf gilt der sanften, ausgestreckten Hand auf meiner Brust. Nach einer unbestimmbar langen Zeit zieht Lilly ihre Hand zurück."


li "Guten Morgen, Hisao."


$ renpy.music.set_volume(1.0, 3.0, channel="ambient")
play music music_dreamy fadein 8.0

scene bg hok_lounge onlayer master
show lilly basic_smileclosed_cas onlayer master at center
with openeye

"Ich gestehe meine Niederlage viel zu leicht ein, raffe mich auf und reibe meine Augen."


hi "Woher wusstest du?"


show lilly basic_weaksmile_cas onlayer master
with charachange

li "Deine Atmung hat sich verändert."


"Obwohl das Sinn ergibt, kann sie nicht so lange gebraucht haben, um das herauszufinden. So wie ich ihr Gehör kenne, wusste sie es wahrscheinlich schon, bevor sie ihre Hand auf mich gelegt hat."


show lilly basic_displeased_cas onlayer master
with charachange

li "Wenn du länger schlafen willst, solltest du wirklich früher zu Bett gehen. Ich hab den Fernseher noch bis tief in die Nacht gehört."


hi "Das tut mir leid. Meine Medikamente haben schon seit einer Weile meinen Schlafrhythmus durcheinandergebracht. Auch wenn ich müde bin, habe ich Probleme, wirklich einzuschlafen."


show lilly basic_oops_cas onlayer master
with charachange

li "Tut… mir leid, dass ich das erwähnt habe, Hisao."


label de_choiceL15:
menu:
    with menueffect
    "Ich seufze. Das ist genau das, was ich von anderen nicht hören will."
    "Es ansprechen.":




        return m1
    "Vom Thema ablenken.":

        return m2


label de_L15a:

hi "Komm schon, du sorgst dich manchmal mehr um mich als ich selbst. Das heißt nur, dass ich etwas länger schlafen muss. Das ist alles."


show lilly basic_reminisce_cas onlayer master
with charachange

li "Aber trotzdem…"


hi "Ich würde sagen, dass ich absolut okay aussehe, aber ich schätze, das würde dir nicht viel sagen."


show lilly basic_displeased_cas onlayer master
with charachange

"Sie seufzt fassungslos, bevor sie amüsiert kichert und nachgibt."


show lilly basic_weaksmile_cas onlayer master
with charachange

li "Wenn du es sagst. Bitte pass auf dich auf, Hisao."


hi "Nun geh schon, Hanako könnte etwas Hilfe gebrauchen."


hide lilly onlayer master
with dissolve

"Sie will protestieren, nimmt es aber widerwillig hin und verschwindet in die Küche. Auf dem Weg dorthin fährt sie mit ihrer Hand an den glatten, weißen Wänden entlang."



label de_L15b:

hi "Hanako könnte… wahrscheinlich etwas Hilfe gebrauchen."


show lilly basic_displeased_cas onlayer master
with charachange

hide lilly onlayer master
with dissolve

"Lilly scheint für einen Augenblick protestieren zu wollen, nimmt es aber schließlich hin und nickt, bevor sie in die Küche geht."


label de_L15c:

"Für eine Weile bleibe ich sitzen und schaue fern, um etwas wacher zu werden – doch es ist umsonst. Ich habe nichts Besseres zu tun, daher folge ich Lilly in die Küche."


stop ambient fadeout 5.0

scene bg hok_kitchen onlayer master
with locationchange

"Als ich um die Ecke komme, sehe ich Hanako und Lilly, die beide mit den Rücken zu mir still das Essen auf dem granitfarbenen Tresen schneiden."


"Einen Moment lang beobachte ich fasziniert, wie Lilly ihr Messer vorsichtig mit dem Finger zum Salat führt. Sie setzt jeden Schnitt langsam aber mit Präzision."


"Sie wirkt etwas langsam, doch wenn man bedenkt, dass sie nicht sieht, was sie tut, ist es ein kleines Wunder, dass sie überhaupt kochen kann – noch dazu für sich und Hanako."


hi "Hi Hanako, Lilly. Braucht ihr Hilfe?"


show lilly back_surprise_cas onlayer master at twoleft
show hanako basic_normal_cas onlayer master at tworight
with charaenter

stop music fadeout 0.3
$ doublespeak(li, ha, "Ist das Hisa— ah!",  "Oh, Morgen Hisao.")


show lilly basic_oops_cas onlayer master
with charachange

"Lilly zuckt überrascht zurück, bevor sie sich umdreht. Ihr Aufschrei ruft Hanako und mich augenblicklich an ihre Seite."


hi "Was ist… ah."


"Ein kleiner roter Tropfen fällt von ihrer blassen Fingerspitze herab. Das Messer hat gerade so tief geschnitten, dass es zu bluten anfängt."


"Mit den Fernsehgeräuschen, die meine Schritte übertönt haben, hat sie mich sicher nicht kommen hören. Um zu kompensieren, dass sie sich beim Kochen über den Tastsinn orientieren muss, muss sie besonders aufpassen."


show hanako defarms_shock_cas onlayer master
with charachange

play music music_dreamy fadein 8.0

ha "Lilly!"


show lilly basic_weaksmile_cas onlayer master
with charachange

li "Keine Sorge, Hanako. Es ist nur eine kleine Wunde."


hi "Du solltest trotzdem ein Pflaster draufmachen – zumindest bis es aufhört zu bluten. Erste-Hilfe-Zeug ist im Badezimmer, oder?"


show lilly basic_sleepy_cas onlayer master
with charachange

li "Ich denke, ja. Kommst du hier allein zurecht, Hanako?"


show hanako cover_worry_cas onlayer master
with charachange

"Dass sie kaum auf sich selbst acht gibt, lässt mich meine Stirn runzeln. Hanako hingegen nickt kurz – fast automatisch."


show hanako basic_worry_cas onlayer master
with charachange

ha "Schon okay, ich kann weiter Mittagessen machen."


scene bg hok_bath onlayer master
with locationskip

"Eine peinliche Stille herrscht, während ich die Flasche mit dem Desinfektionsmittel und die Schachtel Pflaster auf die Abstellfläche des Waschbeckens stelle und Lilly mir ihren zu behandelnden Finger entgegenstreckt."


"Der Deckel der Flasche löst sich fast ohne Widerstand. Als ich dann den kleinen Watteball in die Flüssigkeit tauche, färbt er sich zu einem blassen Grün."


hi "Okay, halt still. Das wird wahrscheinlich ein bisschen wehtun."


show lilly basic_weaksmile_cas_close onlayer master at center
with charaenter

"Sie nickt leicht, während ich ihre Hand greife, um sie zu stützen. Mit aller Zärtlichkeit, die ich aufbringen kann, führe ich den feuchten Bausch zu der kleinen roten Linie."


show lilly basic_oops_cas_close onlayer master
with charachange

li "Ah!"


hi "Was? Ich hab's kaum berührt."


show lilly basic_reminisce_cas_close onlayer master
with charachange

li "Entschuldige…"


"Wegen ihrer Reaktion und um meine eigenen Nerven etwas zu beruhigen, seufze ich. Ihre Schmerztoleranz ist erschreckend gering."


hi "Ich würde dir ja sagen, dass du es nehmen sollst wie ein Mann, aber das geht nicht wirklich."


show lilly basic_weaksmile_cas_close onlayer master
with charachange

"Als sie ein leises Kichern von sich gibt, nutze ich ihre momentanen Ablenkung aus und drücke die Watte ein paar Mal sanft gegen ihren Finger. Glücklicherweise ist es damit auch schon getan."


"Wir beruhigen uns beide etwas, als ich das Pflaster um ihre Fingerspitze wickle und die Wunde bedecke. Dabei passe ich auf, dass es nicht an ihrem Fingernagel kleben bleibt."


hi "So, fertig. Du kannst dich jetzt bewegen."


"Sie zieht ihre Hand von meiner zurück und umschließt sie mit ihrer anderen."


show lilly basic_smileclosed_cas_close onlayer master
with charachange

li "Ich danke dir."


hi "Ist kein Problem. Nachdem du dich meinetwegen verletzt hast, ist es das Mindeste, was ich tun kann."


show lilly basic_emb_cas_close onlayer master
with charachange

"Bei dieser Entschuldigung senkt sie leicht ihren Kopf und reibt gedankenverloren ihre Hand. Anscheinend ist sie etwas verlegen."


show lilly basic_weaksmile_cas_close onlayer master
with charachange

li "Das macht mir wirklich nichts aus."


stop music fadeout 5.0

"Ihre Antwort scheint nicht viel Sinn zu ergeben, da das Geschehene ziemlich klar meine Schuld ist."


"Trotz der Tatsache, dass sie ihr feines Lächeln beibehält, kann ich sie nur verwundert ansehen. Sie wird wohl ungern an die Einschränkungen erinnert, die mit ihrem fehlenden Sehvermögen einhergehen."


"Das ist etwas, das ich ihr unmöglich vorwerfen kann. Ich bin zuvor den gleichen Gefühlen zum Opfer gefallen, obwohl mein Zustand im meinem Leben nicht annähernd so allgegenwärtig ist."


"Zusammen begeben wir uns zurück in die Küche, aus der uns inzwischen zahlreiche Kochgerüche entgegenkommen."


scene bg hok_lounge onlayer master
with shorttimeskip

play music music_another fadein 8.0

"Dampf steigt langsam von dem gekochten Reis und dem Curry auf, während ich die Essensteller auf den Tisch stelle und Hanako das Besteck verteilt."


"Messer auf der einen Seite, Gabel auf der anderen. Westlich. Wie perfekt passend für jemanden wie Lilly."


"Während wir Platz nehmen und dabei vorsichtig auf die dunkelrote, bis unter unsere Knie hängende Tischdecke achten, taucht Lilly aus der Küche auf."


"In ihrer Hand sind drei Gläser und… eine Weinflasche?"


"Als ich mich an unser voriges Treffen mit diesem Teufelselixier erinnere, verberge ich mein Gesicht mit meiner Hand."


hi "Alkohol? Ernsthaft?"


show lilly basic_cheerful_cas onlayer master at center
with charaenter

"Als sie den Tisch erreicht, hält sie inne, ihre Lippen zu einem spielerischem Grinsen geformt."


show lilly basic_giggle_cas onlayer master
with charachange

li "Akira hat uns ausdrücklich die Erlaubnis gegeben, eine Flasche aus ihrer Sammlung zu nehmen."


"Nicht nur, dass sie Minderjährigen Alkohol gibt, sie lässt sie sogar von ihrem eigenen Vorrat klauen? Das perfekte Vorbild eines verantwortungsvollen Erwachsenen ist Akira nicht."


"Wichtiger noch ist jedoch, dass dies kaum ein Essen ist, zu dem Alkohol passt. Ich fange an zu glauben, dass Lilly der Typ ist, der schnell nach etwas süchtig wird."


hi "Das ist nicht wirklich das Problem. Ich habe nicht wirklich etwas dagegen, aber hattest du damit letztes Mal nicht schlechte Erfahrungen?"


show lilly basic_smileclosed_cas onlayer master
with charachange

li "Beim letzten Mal lag es wahrscheinlich daran, dass ich zu viel getrunken habe. Daher sollte ein einziges Glas sich nicht als Problem erweisen."


show lilly basic_smile_cas onlayer master
with charachange

li "Sieh es als eine lehrreiche Erfahrung."


hi "Mir fallen nicht viele lehrreiche Erfahrungen ein, bei denen mir so sauübel geworden ist, aber ich glaube dir mal."


show lilly basic_smileclosed_cas onlayer master
with charachange

"Sie tunkt ihren unverletzten Finger bis zum Boden hinein, um die Flüssigkeitshöhe zu erfühlen, wodurch der Pegel steigt."


"Ihr weißer Finger scheint fast zu glühen, als das Sonnenlicht ihn trifft, sein zarter Umriss durch das Glas unscharf und gebrochen."


"Ihre Finger sind definitiv länger als meine. Ich finde, sie passen eher zu einer Pianistin als zu einer Lehrerin. Sie wäre wahrscheinlich gut geworden, wenn sie gelernt hätte zu spielen."


hide lilly onlayer master
with charaexit

"Schnell widmen wir uns unserem Essen; die Messer und Gabeln klirren gegen die Teller."


"Niemand von uns ist beim Essen besonders gesprächig. Lilly ist für so etwas insgesamt zu zurückhaltend, Hanako ist wahrscheinlich zu schüchtern, um eine Unterhaltung anzufangen, und ich bin zu beschäftigt damit, das Essen zu genießen."


"Zusammen an einem Tisch zu essen ist so etwas Unspektakuläres. Es scheint so absolut normal, aber es lässt mich begreifen, wie lange es her ist, seit ich das letzte Mal so etwas getan habe."


"Nur wir drei, zusammen an einem Tisch beim Essen, als wären wir eine deformierte Familie. Vielleicht war dieser Ausflug, der uns so weit von allem anderen weggebracht hat, es doch wert."


with shorttimeskip

"Es dauert ziemlich lange, aber schließlich beenden wir alle unsere überraschend sättigende Mahlzeit. Der Wein hat – glücklicherweise – wenig Effekt, da wir jeder nur ein oder zwei Gläser hatten."


"Ich lasse mich im Stuhl zusammensinken und reibe mir zufrieden meinen Bauch."


hi "Ich bin voll."


show lilly basic_smileclosed_cas onlayer master at twoleft
show hanako basic_smile_cas onlayer master at tworight
with charaenter

"Lilly tupft sich den Mund mit einer Serviette ab. Zweimal – nur zweimal – und mit gleichmäßigen Zeitabständen dazwischen. Es ist manchmal schwierig zu sagen, ob ihr Verhalten gut antrainierte Routine oder gut einstudiertes Schauspiel ist."


show lilly basic_satisfied_cas onlayer master
with charachange

li "Ich denke, ich bin es auch. Hat es dir geschmeckt, Hanako?"


show hanako cover_bashful_cas onlayer master
with charachange

ha "Mhm, es war lecker."


show lilly basic_smileclosed_cas onlayer master
with charachange

li "Nun da wir alle satt sind – wollen wir dann los?"


hi "Los? Wohin?"


show lilly basic_weaksmile_cas onlayer master
with charachange

li "Ah, du hast die Diskussion zwischen Hanako und mir vorhin ja gar nicht mitbekommen."


"Ich bekommen den Eindruck, dass sie mich wegen meines Verschlafens etwas sticheln will."


show hanako basic_bashful_cas onlayer master
with charachange

ha "Wir gehen in das nahegelegene Dorf."


"Ich schätze, ich hätte damit rechnen sollen, dass zwei Mädchen einen Urlaub als Ausrede zum shoppen gehen nehmen würden – egal wo auf dem Planeten sie sein mögen."


"Allerdings würde ich auch gerne mehr von der Gegend hier sehen, daher kann das nur eine gute Sache sein."


hi "Klingt gut. Wie weit ist es denn bis dorthin?"


show lilly basic_smile_cas onlayer master
with charachange

li "Es sollten ungefähr zwei bis drei Kilometer sein."


stop music fadeout 4.0

hi "„Nahegelegen”, was? Klasse."


"Einfach klasse."


scene bg hok_road onlayer master at bgright
with shorttimeskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 6.0
play music music_soothing fadein 0.5

"Während wir den von Bäumen und Büschen gesäumten Pfad hinaufwandern, betrachte ich Lilly und Hanako, die gerade vor mir laufen."


"Die seichte Brise übertönt beinahe das Geräusch von Lillys Blindenstock, der sanft auf den Boden klopft. Ich bemerke, dass Lillys das Pflaster mittlerweile entfernt hat; die Blutung am ihrem Finger hat aufgehört."


"Ein tiefer, lungenfüllender Atemzug der frischen Landluft lässt mich wünschen, dass die Luft zu Hause auch nur annähernd so sauber gewesen wäre."


"Es kann nicht einmal ein Kilometer gewesen sein, trotzdem komme ich schon ins Schwitzen."


hi "Hey Lilly, wie gut kennst du diese Dorf eigentlich?"


show lilly back_smileclosed_cas onlayer master at center
show lillyprop back_cane onlayer master
with charaenter

li "Da ich einige meiner Ferien hier verbracht habe, bis ich an die Yamaku gekommen bin, würde ich sagen, dass ich es recht gut kenne. Wir sind damals jedes Wochenende hingefahren."


"Wie ich mir wünsche, dass Akira jetzt hier wäre, um uns zu fahren."


"Rasch nutze ich den Moment, um meine Hände ein paar mal aneinander zu reiben, um damit das seltsam kalte Gefühl aus ihnen zu vertreiben."


hi "Hat es dir hier gefallen?"


show lilly cane_weaksmile_cas onlayer master
hide lillyprop onlayer master
with charachange

li "Ich würde sagen, dass es im Winter schön war, aber wie du merkst, wird es im Sommer etwas zu heiß. Zumindest ist es schön ruhig."


li "Das richtige Haus meiner Familie ist ziemlich weit im Süden. Als sie Japan verließen, haben meine Eltern es Akira und mir gegeben. Nachdem ich an die Yamaku gezogen bin, lebt dort nur noch Akira."


hi "Na ja, ruhig passt allerdings zu diesem Ort."


"Auch wenn ich es eher einsam nennen würde."


"Abgesehen von dem angekündigten Dorf ist kilometerweit keine Seele weit und breit. Da mein Zuhause mitten in der Großstadt liegt, ist es auf jeden Fall… anders."


"Ich denke, wenn ich nicht die letzten Wochen an der Yamaku verbracht hätte, wäre eine Umgebung wie diese eine zu große Veränderung gewesen, um mich daran zu gewöhnen."


"Nachdem ich mich aber an die Abgelegenheit der Schule gewöhnt habe, ist der Gedanke, an solch einem Ort zu leben, fast einladend geworden – irgendwo fern von der Hektik der Großstadtzentren."


show lilly cane_smile_cas onlayer master
with charachange

li "Also Hisao, bist du schon einmal in Hokkaido gewesen?"


hi "Nee. Ich hab im Süden gelebt, und wir hatten nie irgendwelche Wandertage oder Klassenfahrten so weit in den Norden."


show lilly cane_cheerful_cas onlayer master
with charachange

li "Nun, dann ist das für dich ja eine neue Erfahrung."


hi "Ja, ist es. Ich bin überrascht, wie angenehm es hier ist."


hi "Was ist mit dir, Hanako?"


show lilly cane_cheerful_cas onlayer master at twoleft
show bg hok_road onlayer master at center
with charamove

show hanako emb_smile_cas onlayer master at tworight
with charaenter

"Sie schüttelt ihren Kopf."


show hanako basic_bashful_cas onlayer master
with charachange

ha "Es ist auch mein erstes Mal."


"Während wir weiterlaufen, beginne ich, Nadelstiche in meinen Beinen zu spüren. Es ist etwas verstörend, da es dafür eigentlich keinen Grund gibt."


stop ambient fadeout 9.0
stop music fadeout 4.0

hi "Könntet ihr Zwei einen Moment warten? Ich muss nur eben…"


show lilly cane_surprised_cas onlayer master
with charachange

li "Stimmt etwas nicht?"


hi "Nein, ich hab nur so ein Stechen in…"


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
with Dissolve (0.8)

with Pause(0.05)

play sound sfx_heartstop
show heartattack alpha onlayer master
with Dissolve (0.1)

show heartattack residual onlayer master
with Dissolve (0.8)

play music music_tragic fadein 0.5

window show

"Meine Stimmbänder verkrampfen plötzlich, als meine Brust sich augenblicklich zusammenzieht. Schnell lege ich meinen Arm auf mein Herz und versuche, die Schmerzwelle zu unterdrücken, die durch meinen Körper jagt."


show lilly cane_reminisce_cas onlayer master
show hanako defarms_strain_cas onlayer master
with charachange

li "Hisao?"


"Lillys Gesicht ist nur wenig beunruhigt, da sie nicht weiß, vor welchem Anblick Hanako zurückschreckt."


hi "Mit geht's gut, mir… geht's gut. Bin nur… erschöpft…"


"Ich nehme den Arm von meiner Brust und zwinge mich dazu weiterzulaufen. Es ist nur ein kleines Herzflimmern, daher wird es genauso wie die anderen vorübergehen."


play sound sfx_heartslow

show heartattack alpha onlayer master
with Dissolve (0.1)

show heartattack residual onlayer master
with Dissolve (0.8)

"Es dauert nur ein paar Schritte, bis mein Körper wieder gewaltsam gegen mich rebelliert. Meine Beine geben plötzlich unter mir nach, und all die Spannung in meinen Knien scheint zu schwinden."


scene bg hok_road onlayer master:
    xalign 0.5 yalign 0.52 rotate 0 zoom 1.0
    linear 0.1 rotate -6 zoom 1.2
show lilly cane_reminisce_cas onlayer master:
    xanchor 0.5 xpos 0.3 yalign 0.52 rotate 0 zoom 1.0
    linear 0.1 xpos 0.25 rotate -6 zoom 1.2
show hanako defarms_strain_cas onlayer master:
    xanchor 0.5 xpos 0.7 yalign 0.52 rotate 0 zoom 1.0
    linear 0.1 xpos 0.75 rotate -6 zoom 1.2
show heartattack residual onlayer master
play sound sfx_pillow
with vpunch

"Bevor ich reagieren kann, knicken sie nutzlos unter meinem Gewicht ein und lassen mir gerade genug Zeit, dass ich mich wappnen und auf allen Vieren landen kann."


hi "Ah, mist…"


show hanako defarms_shock_cas onlayer master
with charachange

ha "Hisa… AAAAH!"


"Als ich zu ihr aufsehe, realisiere ich, dass mein Gesicht immer noch schmerzverzogen ist. Das macht ihre Sorge wohl nur noch schlimmer."


show lilly cane_oops_cas onlayer master
with charachange

li "Hisao!? Hanako, sag mir, was los ist!"


li "Hanako, sag's mir!"


show hanako def_strain_cas_close onlayer master
with characlose

"Hanako kommt schnell an meine Seite, während Lilly fast in Panik ausbricht, da sie nicht wissen kann, wie schlimm mein Zustand eigentlich ist. Während sie dort wie versteinert steht, senke ich mein Gesicht und nehme einen tiefen Atemzug."


scene black onlayer master
show heartattack alpha onlayer master
with shuteyefast

"Ich komme zu einer Erkenntnis, die mich unendlich wütend über meine eigene Dummheit macht."
"Bei all der Aufregung über mein neues Umfeld habe ich es vollkommen vernachlässigt, meine Medikamente zu nehmen – gestern Abend und sogar heute Morgen."


stop music fadeout 9.0

hide heartattack onlayer master
with Dissolve(3.0)

"Nach einem weiteren Atemzug beginnt der heftige Schmerz in meiner Brust so plötzlich abzuklingen, wie er gekommen ist."


"Gott sei Dank. Gott sei Dank. Gott sei Dank. Gott sei Dank. Gott sei Dank."


play ambient sfx_parkambience fadein 6.0

scene bg hok_road onlayer master
show lilly cane_oops_cas onlayer master at twoleft
show hanako def_strain_cas_close onlayer master at tworight
with openeye

"Mir wird bewusst, dass mir der Schweiß vom Gesicht tropft, und dass zwei verängstige Mädchen vor mir stehen."


show lilly cane_reminisce_cas onlayer master
with charachange

li "Hisao!"


hi "Ich bin okay, Lilly. Ich bin… okay."


show hanako defarms_strain_cas_close onlayer master
play sound sfx_impact
with vpunch

"Bei dem Versuch, mich aufzuraffen, kneife ich meine Augenbrauen zusammen. Als ich dabei etwas ins Wanken gerate, bringt Hanako ihre Arme in Bereitschaft, um mich aufzufangen, aber ich finde mein Gleichgewicht selbst wieder."


"Ich sehe Lilly und Hanako an, denen die Sorge ins Gesicht geschrieben steht. Ich fühle mich schrecklich. Absolut schrecklich."


show lilly cane_sad_cas onlayer master
with charachange

li "Ich denke, wir sollten zurückgehen."


hi "Ich…"


"Als ich die Vergeblichkeit des Protestierens begreife, schaue ich frustriert weg."


hi "Okay…"


stop ambient fadeout 2.0

$ suppress_window_after_timeskip = True

scene black onlayer master
with dissolve



label de_L16:

window hide None

scene black onlayer master
with dissolve

scene bg hok_lounge_ss onlayer master
with openeye

window show

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_cicadas fadein 2.0

"Angeschlagen und gänzlich meiner Energie beraubt öffne ich meine Augen."


"Für eine Weile liege ich lediglich leblos da und starre an die Decke, während ich die Ereignisse dieses Morgens durchgehe und versuche, meine Gedanken zu sortierten."


"Wir machten uns auf den Weg zu dem Dorf. Mein Herz gab fast den Geist auf. Wir kamen zurück. Ich nahm meine Tabletten. Ich schlief."


"Ich kann mich nur wie im Zeitraffer an jedes einzelne Ereignis erinnern, doch die Abfolge ist glasklar. Das Erinnerung an die Gesichter der Mädchen, als ich versucht habe aufzustehen, ist eine unschöne und versetzt mir einen heftigen Stich."


"Wenn ich mich lange genug auf die Decke konzentriere, kann ich mir die Muster der Decke im Krankenhaus vorstellen. Diese Tatsache allein ist genug, um mich dazu zu bewegen, mich aufzusetzen und mich zusammenzureißen."


"Ich fahre mir mit der Hand durch meine zerzausten Haare und lasse meinen Blick durch das Zimmer schweifen. Lilly und Hanako sind nirgends zu sehen, und der Fernseher ist ausgeschaltet."


"Die Uhr darüber sagt, dass es ziemlich spät am Nachmittag ist. Der merklich gerötete Himmel außerhalb der Fenster bestätigt dies umso mehr."


"Ich drehe mich um und erhebe mich von dem Futon, wobei ich mit meinen Armen das Gleichgewicht halte. Ich schätze, ich sollte besser nach den Mädchen sehen, um zu schauen, ob sie… in Ordnung sind…"


"Als ich aus dem Fenster sehe, erkenne ich schwach etwas in der Ferne."


"Wenn ich meine Augen anstrenge, kann ich gerade so die Form einer menschlichen Gestalt erkennen. Ihre langen blonden Haare, die in der leichten Brise wehen, lassen sie fast mit dem hellen Gelb des Kornfeldes verschmelzen."


"Ohne lange nachzudenken, verlasse ich das Zimmer und folge dieser einsamen Erscheinung."


stop ambient fadeout 2.0
play music music_innocence fadein 14.0

scene bg hok_wheat_ss onlayer master at Fullpan(8.0)
with Fade(0.5, 0.2, 3.0, color="#fff")

"Die Helligkeit der untergehenden Sonne überflutet meine frisch aufgewachten Augen. Es zwingt mich wegzusehen, bis sie sich daran gewöhnt haben."


"Die langen, gelben Getreidehalme streifen gegen meine Beine, als ich durch sie hindurchwate. Das dicht bewachsene Feld macht das Vorankommen schwierig."


"Trotzdem bleiben meine Augen nach vorn gerichtet – immer auf diese alleinstehende Gestalt. Binnen Minuten stehe ich wenige Meter hinter ihrem mir zugewandten Rücken."


hi "Lilly?"


scene bg hok_wheat_ss onlayer master at right
show lilly back_pout_cas_ss onlayer master at center
with charaenter

"Sie nickt lediglich."


hi "Wo ist Hanako?"


show lilly back_listen_cas_ss onlayer master
with charachange

li "Sie ist im Bett. Sie ist schlafen gegangen, nachdem ich sie beruhigt hatte."


"Sie sagt es nüchtern und mit so wenig Worten wie möglich, als ob alles Weitere streng vertraulich wäre."


"Etwas ist anders an ihr. Ihre normalerweise selbstsichere Gestalt wirkt seltsam fragil. Ihr Körper bietet der Brise, die ihren Rock flattern lässt, keinen Widerstand."


"Das Schweigen zwischen uns ist ohrenbetäubend. In der Stille ist nur das Rascheln der von Seite zu Seite schwankenden Getreidehalme zu hören."


"Als wir beide allein im Feld stehen, weiß ich, was ich fragen muss."


hi "Was ist los, Lilly? Du benimmst dich anders als sonst."


show lilly back_sad_cas_ss onlayer master
with charachange

li "Erinnerst du dich, als ich über meine Familie geredet habe, Hisao?"


hi "Deine Familie…"


"Ich schaue nachdenklich nach unten und durchsuche meine verstreuten Erinnerungen. Mir wird schnell klar, von welchem Ereignis sie redet."


hi "Nach Hanakos Geburtstagsparty?"


"Sie nickt schlicht und einfach."


show lilly back_pout_cas_ss onlayer master
with charachange

li "Es… war schön, damals. Du und ich, wie wir mit Hanako gefeiert haben. Einfach ein paar Geschenke austauschen, uns unterhalten, zusammen Spaß haben. Es war fast, als wären wir eine Familie. Eine kleine, unförmige Familie."


show lilly back_sad_cas_ss onlayer master
with charachange

li "Ich dachte, dass es für immer einfach so weitergehen könnte. Nur wir drei, glücklich zusammen."


"Sie nimmt einen langen Atemzug, welcher ein kleines Zittern enthält, das über die Brise gerade noch hörbar ist."


show lilly back_pout_cas_ss onlayer master
with charachange

li "Auch wenn meine Familie so weit weg war… Solange wir zusammen waren, war das alles, was ich gebraucht habe. Ich will dich nicht verlieren, Hisao."


li "Ich habe bis heute nicht einmal gemerkt, wie viel Angst ich davor habe, jemand anderen zu verlieren. Bis…"


hi "Es tut mir leid, Lilly. Ich weiß, mein Körper ist schwach, und trotzdem mache ich die allerdümmsten Fehler."


stop music fadeout 4.0

show lilly back_sad_cas_ss onlayer master
with charachange

li "Entschuldige dich nicht… bitte entschuldige dich nicht…"


hi "Lilly…?"


show lilly basic_concerned_cas_ss onlayer master
with charachange

"Sie dreht sich zu mir um. Ihre blassen Wangen sind tränenüberströmt."


show lilly basic_concerned_cas_close_ss onlayer master
with characlose

"Einen unbeholfenen Schritt nach dem anderen stolpert sie auf mich zu, während sie ihre Arme suchend nach mir ausstreckt."


play music music_romance fadein 2.0

window hide

scene unlock_ev lilly_wheat_close onlayer master
show ev lilly_wheat_large onlayer master:
    yalign 0.5 xalign 0.0 subpixel True
    easein 20.0 xalign 1.0
show ovl lilly_wheat_foreground onlayer master:
    yalign 0.5 xalign 0.0 subpixel True
    easein 20.0 xalign 1.0
with GenericWhiteout(1.0, 0.0, 4.0)

window show

"Weder rast noch klopft mein Herz, als ich zu Lilly laufe, sie sanft ergreife und sie fest in meine Armen halte, während sie sich schluchzend an mich klammert."


"Wie sie so zitternd vor mir steht und ihr Gesicht in meiner Schulter vergräbt, sind ihre nächsten Worte die Letzten, die ich erwartet hätte."


li "Ich liebe dich, Hisao. Ich liebe dich, ich liebe dich, ich liebe dich, ich liebe dich, ich liebe dich!"


li "Geh nicht weg, ich flehe dich an. Geh niemals weg. Niemals. Ich liebe dich, also bitte…!"


"Darum also… hat sie sich so verhalten. Ihre liebevolle Stimme, als ich sie angerufen habe, ihre gedankenlose Sorge über den kleinsten Schmerz, den ich spüren könnte…"


"Nachdem sie ohne ihre Familie in Japan zurückgelassen wurde und nur Akira, Hanako und mich bei sich hatte, hatte sie Angst davor, einen weiteren ihr nahestehenden Menschen zu verlieren. Sie hat sich aufrichtig um mich Sorgen gemacht."


"Es ist ein seltsames Gefühl. Eine Mischung aus Überraschung und Reue und der tiefsten Dankbarkeit, die ich wohl je gefühlt habe. Die einzige Reaktion, die ich durch meine in Konflikt stehenden Gefühle aufbringen kann, ist ein ruhiges Seufzen."


hi "Du Idiot."


li "Hi… sao?"


"Für einen flüchtigen Moment spüre ich, wie ihr Körper zur Ruhe kommt. Die einzige Bewegung, die zu spüren ist, ist die ruhige Nachmittagsbrise."


hi "Ich hab's dir schon mal gesagt, oder nicht? Es ist nur normal, dass man sich um die Menschen Sorgen macht, die einem nahestehen."


hi "Ich bin immer noch hier, und ich werde immer hier sein – denn ich will dich jeden Tag mehr sehen. Um deine Freude zu teilen, um dich zu unterstützen, wenn du traurig bist…"


hi "Doch vor allem werde ich hier sein, weil ich dein Lächeln sehen will. Dein echtes Lächeln."


"Eine einzelne Windböe raschelt durch die langen Getreidehalme. Eine Sekunde lang ist alles still."


hi "Lächle, wenn du lächeln willst. Weine, wenn du weinen willst. Ich liebe dich, Lilly. Also brauchst du dich nicht mehr zurückzuhalten."


"Daraufhin umklammern ihre Arme meinen Rücken so fest wie sie nur kann und vergräbt ihr Gesicht neben meinem."


scene ev lilly_wheat_small onlayer master:
    xalign 0.5 yalign 0.5 zoom 1.1 subpixel True
    ease 16.0 zoom 1.0
with whiteout

"Ihre Tränen fallen meinen Rücken hinab, und sie weint sich hemmungslos aus, während ihr letzter Widerstand dahinschmilzt."


li "Hisao! Hisao! Hisao!"

"Ich schließe meine Augen, lege meinen Kopf auf ihre Schulter und halte ihre zitternde Gestalt fest in meinen Armen."


hi "Es ist okay, Lilly. Ich werde niemals weggehen."


hi "Ich verspreche es."


stop music fadeout 6.0



label de_L17:

scene bg hok_lounge_ss onlayer master
with locationskip

"Wir laufen langsam zurück zum Haus und halten einander fest, als wir uns drinnen hinsetzen. Lilly lehnt ihren Kopf auf meine Schulter, während ich meinem Arm um ihre Hüfte lege."


"Keiner von uns will die Stille brechen."


"Mit ihren geschlossenen Augen ist es schwierig zu sagen, ob sie eingeschlafen ist. Nicht, dass mich das stört – die Wärme ihres Körpers, der an meinem lehnt, die Zartheit ihrer Hand, die sanft von meiner gehalten wird…"


"Für eine lange, lange Zeit sitzen wir so zusammen und teilen unsere Wärme und Gefühle, während langsam die Nacht anbricht."


"Lillys sanfte, weiche Stimme beendet die Stille."


show lilly basic_smileclosed_cas_close_ss onlayer master at center
with charaenter

play music music_twinkle fadein 6.0

li "Danke, Hisao."


hi "Danke?"


show lilly basic_smile_cas_close_ss onlayer master
with charachange

li "Dass du meine Gefühle erwiderst."


hi "Dachtest du, ich würde es nicht?"


show lilly basic_weaksmile_cas_close_ss onlayer master
with charachange

li "Die Möglichkeit bestand."


"Ich nehme nachdenklich einen tiefen Atemzug. Das war allein mein Fehler."


hi "Eigentlich ist es lustig. Ich hatte daran gedacht, dir bald meine eigenen Gefühle zu gestehen."


hi "Ich schätze, wenn man es so sieht, hast du mir die Mühe erspart."


show lilly basic_giggle_cas_close_ss onlayer master
with charachange

"Sie hebt etwas ihren Kopf und kichert leise und amüsiert. Es ist so aufrichtig und so mädchenhaft süß, dass ich selbst lächeln muss, aber sie nimmt sich schnell wieder zusammen. Ihr Haar fällt immer noch über meine Schulter."


hi "Fühlst du dich besser?"


show lilly basic_smileclosed_cas_close_ss onlayer master
with charachange

"Sie nickt leicht."


show lilly basic_smile_cas_close_ss onlayer master
with charachange

li "Du bist rücksichtsvoll, Hisao. Darum mag ich dich."


hi "Tut mir leid, dass ich so bin. So sehr ich dir meinetwegen auch keine Sorgen bereiten wollte, konnte ich nichts tun, um es zu verhindern."


show lilly basic_concerned_cas_close_ss onlayer master
with charachange

li "Entschuldige dich nicht dafür. Bitte nicht."


hi "Lilly?"


show lilly basic_reminisce_cas_close_ss onlayer master
with charachange

li "Habe ich mich je für meine Blindheit entschuldigt? Ein einziges Mal? Du kannst nichts dafür, wie du geboren wurdest, Hisao. Es hat keinen Sinn, sich für das zu entschuldigen, was man ist."


"Sie sagt es mit verblüffender Überzeugung. Am Ende war es wahrscheinlich diese Einstellung, die sie dazu angespornt hat, sich in so kurzer Zeit mit mir anzufreunden – zusammen mit ihren mütterlichen Instinkten."


"Sie wirkte von Anfang an schnell vertrauensvoll, doch ich habe nie hinterfragt warum. Nun scheint es offensichtlich, dass sie es getan hat, um mir durch den Tiefpunkt meines Lebens zu helfen."


"Ich will gerade antworten, doch ich komme nicht dazu, weil ich ihre Finger sanft durch mein Haar gleiten spüre."
"Ich spüre, wie ihre sanfte und zarte Berührung abwärts wandert, um die Konturen meines Gesichtes abzutasten. Danach ruht ihre Hand schließlich auf meiner Wange."


show lilly basic_weaksmile_cas_close_ss onlayer master
with charachange

li "Du bist ein wundervoller Mensch, Hisao. Bitte, entschuldige dich niemals dafür."


"Für einen Augenblick bin ich vollkommen sprachlos. Ich beuge langsam meinen Kopf nach unten, um einen liebevollen Kuss auf ihr helles, voluminöses Haar zu setzen."


hi "Wir sind wirklich ein paar alte Narren, nicht wahr?"


show lilly basic_cheerful_cas_close_ss onlayer master
with charachange

li "… Sind wir."


"Nach einer langen Stille spricht sie erneuert."


show lilly basic_smile_cas_close_ss onlayer master
with charachange

li "Hisao?"


hi "Ja?"


show lilly basic_smileclosed_cas_close_ss onlayer master
with charachange

li "Ich…"


stop music fadeout 4.0

show lilly basic_weaksmile_cas_close_ss onlayer master
with charachange

li "Ich hätte nichts dagegen, wenn du…"


"Ich spüre, wie sich ihre Hand unter meiner anspannt und leicht zittert. Mein Mund öffnet sich, doch so sehr ich es auch versuche, ich finde auf ihren Vorschlag keine Antwort."


hi "Lilly…"


"Bevor ich ein weiteres Wort sagen kann, zieht sie ihre Hand unter meiner weg und hält ein weiteres Mal sanft die Seite meines Gesichts."


show lilly basic_pout_cas_close_ss onlayer master
with charachange

li "Bitte."


"Ich schenke ihr ein friedliches Lächeln und halte ihre Hand an meine Wange, während ich ein einziges Mal nicke."


hi "Okay."


play music music_heart fadein 0.5

show lilly basic_smileclosed_cas_close_ss onlayer master
with charachange

"Als ich in ihre Augen sehe, lehnt sie sich zu mir. Mit ihrer Hand führt sie mein Gesicht an ihre Lippen."


"Kaum eine Sekunde später löst sie sich und lächelt zaghaft."


show lilly basic_smile_cas_close_ss onlayer master
with charachange

li "Ich liebe dich, Hisao."


show lilly basic_smileclosed_cas_close_ss onlayer master
with charachange

"Wir küssen uns erneut. Diesmal treffen sich unsere Lippen."


"Während der vorige ein Kuss aus Liebe war, ist dieser einer der Lust. Unsere Zungen treffen sich, und unsere Atmung ist schwer. Nach wertvollen Sekunden trennen wir uns. Unsere Gesichter sind nun voll und ganz errötet."


"Gleichzeitig legen wir unsere Finger auf unsere Lippen und erinnern uns an das flüchtige Gefühl, das schnell von unseren Trieben und unserer Verlegenheit begraben wird."


show lilly basic_pout_cas_close_ss onlayer master
with charachange

"Jedoch ist Lilly die Erste, die unruhig hin und her rutscht."


hi "Was ist denn?"


show lilly basic_weaksmile_cas_close_ss onlayer master
with charachange

li "Wollen wir… es uns bequemer machen?"


hi "Hmm? Ah, o-okay…"


"Jetzt, wo sie es erwähnt – dieser Futon wäre ein bisschen zu schmal, um viel darauf tun zu können. Wenn man die Gedanken bedenkt, die uns beiden durch den Kopf schießen, ist es ein Wunder, dass einer von uns noch eine gewisse Weitsicht hat."


show lilly invis onlayer master:
    ypos 1.2
with dissolvecharamove

hide lilly onlayer master
with vpunch

"Ich nehme ihre Hände und führe sie seitwärts, während ich mich bewege. Der kurze und unbeholfene Tanz endet damit, dass wir uns beide zögernd auf dem Boden gegenüber sitzen."


"Als ich meine Hände ausstrecke, um ihr Oberteil auszuziehen, hält sie inne, bevor sie es mir gleichtut."


show lilly basic_concerned_cas_close_ss onlayer master:
    center
    ypos 1.17
with charaenter

li "Du zitterst…"


"Ich schaue auf meine Hände."


"Tatsächlich beben sie etwas. Ob es von der Nervosität oder der Aufregung kommt, weiß ich nicht genau."


hi "Äh… ich schätze, das tue ich."


show lilly basic_weaksmile_cas_close_ss onlayer master
with charachange

li "Dann bist du also genauso nervös wie ich?"


"Ich ziehe meine Hände zurück, seufze und beruhige mich. Wir haben reichlich Zeit, also gibt es keinen Grund, das zu überstürzen."


hi "Sorry. Es ist mein erstes Mal, darum bin ich ein bisschen…"


show lilly basic_cheerfulblush_cas_close_ss onlayer master
with charachange

"Sie kichert zittrig, womit meine bisherigen Vermutungen so gut wie bestätigt sind."


show lilly basic_smile_cas_close_ss onlayer master
with charachange

li "Für mich ist es genauso. Ich bin glücklich… dass wir das miteinander teilen können."


"Ich erwidere ihr Lächeln mit einem doppelt so großen. Dabei lehne ich mich nach vorne und nehme ihren Körper in meine Arme, während sie es mir gleichtut."


hi "Ich liebe dich, Lilly."


show lilly basic_smileclosed_cas_close_ss onlayer master
with charachange

li "Das hast du bereits gesagt."


"Ich kann nur grinsen. Sogar in solch einer Situation hat sie immer noch ihre scharfe Zunge."


hide lilly onlayer master
with charaexit

"Nachdem wir uns aus unserer Umarmung lösen, beschließen wir, uns unsere eigene Kleidung auszuziehen. Obwohl es auf dieser Weise einfacher ist, bezweifle ich nicht, dass es nur ein Versuch ist, um uns von unserer Nervosität abzulenken."


"Mit leicht steifen Händen beginne ich, den ersten Knopf meines Hemdes zu öffnen."


"Sobald wir unsere letzten Kleidungsstücke losgeworden sind, die sich nun willkürlich hinter uns stapeln, raubt der vor mir liegende Anblick mir den Atem."


label de_L17h:

show lilly behind_reminisce_nak_ss onlayer master
with charaenter

"Ihre langen, wohlgeformten Beine, ihre runden Hüften und ihre Brüste – plump aber anmutig… Ihr leicht errötetes Gesicht, zierlich und zurückhaltend, umrahmt von ihren Haaren."


"Ihre Hände, fest hinter ihrem Rücken gehalten, betonen ihre Brust nur noch mehr. Ihr großer und blasser Körper ist schön, wenn er nackt ist."


"Dieses Mädchen vor mir, zurückhaltend und doch verspielt, scharfsinnig und doch freundlich, ist das Mädchen, in das ich mich verliebt habe."


"Ich lehne mich nach vorne und nehme ihre Schultern in meine Hände."


show lilly behind_listen_nak_close_ss onlayer master
with charachange

"Als ich das tue, legt sie ihre Hände auf meine Brust. Mit leicht ungleichmäßigem Atem lehnen wir uns für einen tiefen Kuss nach vorne."


"Ich spüre, wie eine ihrer Hände langsam zu meiner Schulter hinaufwandert. Das, und wie sie ihren Kopf ganz zaghaft vorwärts bewegt. Da ich ihr Vorhaben erahnen kann, lasse ich mich rückwärts auf den Boden sinken."


hi "Ah…"


scene evhunlock lilly_handjob_chest_normal_small onlayer master
show evh lilly_handjob_chest_normal onlayer master:
    xalign 0.7 yalign 1.0 subpixel True
    ease 8.0 xalign 0.4 yalign 0.2
with whiteout

"Sie legt sich neben mich, während eine Hand mein Haar streichelt und die andere sich über meine Brust bewegt. Das Gefühl ihrer Brust an meiner ist genug, um mich zu erregen."


"Das muss ihre Art sein, wie sie aufnimmt, was ich bereits von ihr gesehen habe; trotz ihres fehlenden Sehvermögens prägt sie sich jedes Detail meines nackten Körpers ein."


"Als ihr Mittelfinger auf die leichte Vertiefung meiner Brustnarbe stößt – ein Überbleibsel meiner Operation von vor so vielen Monaten – tastet sie sie langsam mit ihrer Hand der Länge nach ab."


show evhunlock lilly_handjob_chest_frown_small onlayer master
show evh lilly_handjob_chest_frown onlayer master:
    xalign 0.4 yalign 0.2
with charachange

li "Das ist…"


hi "Die Narbe… von meiner Operation. Sie mussten das tun, um an meinem Herzen operieren zu können."


"Für einen Moment fehlen ihr die Worte. Der Gedanke an solch eine ausgedehnten Narbe fügt ihr nur noch eine weitere Sorge hinzu. Ihr Blick wandelt sich von Neugier zu Besorgnis."


li "Sollten wir… so etwas wirklich tun…?"


"Diese Worte beunruhigen mich mehr als sie sollten. Lillys Gesichtsausdruck bricht mein Herz mehr als es ihre Worte je tun könnten. Dennoch weiß ich nicht einmal die Antwort auf ihre Frage."


"Ich kann nicht zulassen, dass mich dieser Zustand für immer beherrscht. Es mag vielleicht medizinisch nicht ratsam sein, aber ich lehne es gänzlich ab, mein Leben in solch einem Gefängnis zu verbringen."


hi "Es ist okay, Lilly. Ich werde es schon überstehen."


show evh lilly_handjob_chest_normal onlayer master
with charachange

"Ihr beunruhigter Gesichtsausdruck hält noch etwas länger an, doch schließlich nimmt sie es hin. Dann bewegt sich ihre Hand weiter meine Brust hinab und dann zu meinem Schenkel."


show evh lilly_handjob_chest_normal onlayer master:
    zoom 1.0 xalign 0.4 yalign 0.2
    ease 4.0 zoom 0.667 xalign 0.5 yalign 0.5
with None

show evh lilly_handjob_stroke_normopen onlayer master:
    zoom 1.0 xalign 0.4 yalign 0.2
    ease 4.0 zoom 0.667 xalign 0.5 yalign 0.5
with charachange

"Mit einem leicht überraschten Blick fährt sie mit ihrer Hand weiter langsam hinunter. Ihr Atem stockt, als sie die Seite meiner Schamhaare streift."


"Zögernd bewegt sie ihre Hand zur Seite und berührt vorsichtig den ehrlichsten Teil meines Körpers."


show evh lilly_handjob_stroke_normshut_small onlayer master:
    truecenter 
    zoom 1.0
with charachange

li "Da… Das ist…"


hi "J-Ja."


"Unsere Nervosität erreicht den Höhepunkt, als der Akt beginnt. Ihr Hand beginnt sanft auf und ab zu tasten, als würde er bei der leichtesten Berührung zerbrechen."


"Ich bin mir nicht sicher, ob ich mich selbst oder sie beruhigen will, aber ich benutze meine freie Hand und halte damit die Seite ihres Gesichts."
"Es ist angenehm, wie sich ihre Haare und ihre weiche Haut anfühlen, und es scheint ihre Stimmung etwas zu heben."


"Die bloße Tatsache, dass ich von ihr berührt werde, ist überraschend erotisch. Ich spüre, wie mein Körper sich entspannt, als ich mich der Lust hingebe."


"Lange Minuten vergehen fast in vollkommener Stille. Unsere schwere Atmung ist das Einzige, was im Haus gehört werden kann. Lillys Finger hören auf, liebevoll mein Haar zu streicheln, und sie setzt ein weiteres Mal zum Sprechen an."


show evh lilly_handjob_stroke_flustopen_small onlayer master
with charachange

li "Hisao…"


"Ich warte eine Sekunde auf den Rest des Satzes, doch es folgt nichts. Sie versucht vermutlich, die Führung zu übernehmen, ist aber immer noch unglaublich nervös."


"Ich kann nur lächeln, als ich ihr ein paar Mal das Haar aus dem Gesicht streiche, um sie zu beruhigen. So nervös sie auch sein mag, ich bin froh, dass Lilly die Führung übernimmt. Ich wäre in dieser Situation wahrscheinlich genauso ängstlich wie sie."


show evh lilly_handjob_stroke_normopen_small onlayer master
with charachange

hi "Okay."


"Sie hält einen Moment inne, bevor sie leicht nickt, sich aufsetzt, und ihre Beine über meine legt. Wieder einmal wird mir von dem erhabenen Anblick ihres Körpers der Atem geraubt."


show evh lilly_cowgirl_smile_small onlayer master
with whiteout

"Ich kann nur wie erstarrt zusehen, als sie sich zögernd auf mich herablässt und ihre geröteten Lippen auf mir ruhen lässt. Langsam beginnt sie, ihre Hüfte abwärts zu bewegen, während ihre Zartheit mein Bewusstsein einhüllt."


show evh lilly_cowgirl_weaksmile_small onlayer master
with charachange

"Sie nimmt einen tiefen Atemzug, um sich zu sammeln."
"Ihr Gesicht bleibt dabei gelassen. Anstatt ihrer Augen nehmen ihre Hände meinen Körper auf; die intime Situation macht es ihr schwer, ihre mangelnde Sicht auf die übliche Weise zu kompensieren."


"Nach und nach lässt sie sich auf mich sinken, indem sie sich mit ihren Händen und Knien abstützt. Ihr gesamter Körper verkrampft sich, als ich eindringe. Ihr Gesicht ist offensichtlich von Schmerz verzerrt."


"Trotzdem kann ich nicht anders, als das weiche, warme Gefühl zu genießen, das mein Bewusstsein überkommt. Die Welle aus Lust überschwemmt all meine Sinne."


"Die letzten Zentimeter verschwinden in ihrem Inneren, während sie ihre Nägel leicht in meine Brust gräbt, um nicht vor Schmerz aufzuschreien. Ein gequältes Stöhnen entweicht ihren Lippen. Es ist zu viel für sie, um es komplett zu unterdrücken."


"Als ich meinen Mund öffnen will, um sie zu trösten, entdecke ich gerade so erkennbare rote Tropfen zwischen ihren Beinen."


hi "Lilly, wenn es zu viel ist…"


scene evh lilly_cowgirl_strain_small onlayer master
with charachange

"Sie presst ihre Lippen fest zusammen und schüttelt aus Trotz heftig ihren Kopf. Nach ein paar Sekunden entspannt sich ihr Körper etwas, auch wenn sie noch weit davon entfernt ist, locker zu sein."


li "E… es ist okay… Ich bin okay."


scene evh lilly_cowgirl_frown_small onlayer master
with charachange

"Sie schluckt schwer und versucht, sich zusammenzunehmen."


"Während sie sich langsam hebt und wieder absinken lässt, entspannt sie sich ein bisschen mehr, da die Gefühle der Lust die des Schmerzes übertrumpfen."


scene evh lilly_cowgirl_strain_small onlayer master
with charachange

"Ihre Atmung beginnt, sich meinem ungleichmäßigen Rhythmus anzupassen. Ihr Körper bewegt sich fast herausfordernd langsam. Sie sieht aus, als würde sie langsam den Akt genießen, und meine Gefühle erreichen sie endlich."


"Ich bin mir nicht sicher, ob sie ihretwillen oder meinetwillen dieses Tempo hält, aber so oder so… denke ich, dass ich mit diesem Tempo… meinen Körper unter Kontrolle halten kann. Irgendwie ist es lustig, dass ich mich sogar jetzt auf sie verlasse."


"Dass wir so verbunden sind, unsere Gefühle so ähnlich… Es macht mich glücklich. Dass wir unser erstes Mal so miteinander teilen… ist ein fast… überwältigendes… Gefühl…"


hi "Ich liebe dich… Lilly…"


scene evh lilly_cowgirl_cry_small onlayer master
with charachange

li "Hisao… Hisao…!"

"Ich kann spüren, wie sich ihr Körper anspannt und ihre Atmung und ihre Bewegungen allmählich immer weniger kontrolliert sind."
"Ich freue mich, dass sie sich so gut fühlt, doch als meine Gedanken zunehmend konzentrierter werden, spüre ich, dass ich mich schnell meinem Limit nähere."


scene white onlayer master
with Dissolve(3.0)

"Die Kontrolle über meinen Körper wird mir augenblicklich entrissen, als ich heftig mit meinen Zähnen knirsche, und mit einem lauten Stöhnen den Höhepunkt erreiche."
"Ihr Körper fällt im gleichen Moment nach vorne, und ihre Brüste berühren meinen Oberkörper."


"Für einen kurzen Moment verweilen wir in dieser allumfassenden Ekstase. Mein Verstand ist von diesem Gefühl für ein paar kostbare Sekunden eingenommen."


scene evh lilly_cowgirl_weaksmile_small onlayer master
with charachange

"Es endet allzu bald, als unsere Körper vor Erschöpfung zusammensacken und sich Lilly gerade noch so auf mir halten kann."


"Leblos schaffe ich es, meinem Arm um ihren schlaffen, schwitzenden Körper zu legen. Für einige Minuten liegen wir einfach da und genießen still die Berührung des jeweils anderen, während wir uns von der Erfahrung erholen."


"Keiner von uns war auf so einen Augenblick vorbereitet – dessen bin ich mir sicher."


"Vollkommen ausgelaugt und viel zu müde für eine Unterhaltung, schaue ich in ihr erschöpftes Gesicht. Es sieht aus, als hätte sie die Überanstrengung – körperlich und mental – fast zum Zusammenbruch gebracht."


hi "Ich liebe dich, Lilly."


scene evh lilly_cowgirl_smile_small onlayer master
with charachange

"Sie nickt schwach und streichelt mein Haar mit ihrer linken Hand. Wenn wir für eine Ewigkeit so zusammenbleiben könnten, wäre das ein unvergleichliches Paradies."


stop music fadeout 2.0

scene black onlayer master
with dissolve



label de_L18:

scene bg hok_lounge_rn onlayer master
with locationchange

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_rain fadein 1.0

"Nachdem ich von einem Geräusch geweckt worden bin, öffne ich etwas widerwillig meine Augen."


"Als ich meinen Kopf nach links drehe, sehe ich, wie der Regen von draußen gegen die Fenster prasselt. Windstoß um Windstoß prasseln die Tropfen gegen das Glas, als würden sie mit aller Kraft versuchen, die Hitze der vergangenen Tage auszugleichen."


"Ich setze mich auf dem Futon auf und fasse mir an den Nacken, um den Schmerz zu lindern, den ich wegen meiner unbeholfenen Schlafposition habe."


"Allem Anschein nach sollte ich mich wegen des Wetterumschwungs beklagen, da es unser letzter Tag hier ist, aber die gestrigen Ereignisse gehen mir einfach nicht aus dem Kopf."


"Das Gefühl von Lillys weinendem Körper in meinen Händen. Die Welle aus Lust und Hormonen, die durch uns floss, als wir die Nacht zusammen verbracht haben. Der Versuch, das alles rational zu verarbeiten, scheint aussichtslos."


"Bei dem Versuch, mich abzulenken, beuge ich mich ächzend nach vorne, um meine Tasche zu greifen, ohne aufstehen zu müssen."
"Ich hole ein Fläschchen nach dem anderen heraus, nehme die Tagesdosis an Tabletten aus ihren Behältern und werfe sie mir ohne weiteres Trara ein."


$ renpy.music.set_volume(0.1, 1.0, channel="ambient")

window hide
nvl show dissolve

nvl clear

n "\n\n\n\nIch habe mich überraschend schnell daran gewöhnt, Pillen ohne Wasser zu schlucken – und genauso habe ich mich wohl auch daran gewöhnt, an eine Schule für behinderte Schüler zu gehen."


n "Wenn ich an die Yamaku denke, werde ich umso dankbarer, von dort mal wegzukommen – auch wenn es nur für eine sehr kurze Zeit ist."


n "Ich schätze die Gelegenheit, mit Lilly und Hanako allein Zeit verbringen zu können – fern von dem betriebsamen Schulalltag, sogar in Anbetracht der kürzlichen Komplikationen."


n "Ich hätte nie gedacht, dass ich das mal sagen würde, aber die Vorstellung, fern von der Stadt in einer schönen, ruhigen Gegend zu leben, ist eine einladende. Ein Gedanke, der mir vor kaum einem Jahr noch völlig lächerlich vorgekommen wäre."


$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

nvl clear
nvl hide dissolve

window show

"Ein leuchtendes Pink – ohne Zweifel Hanako in ihrem Morgenmantel – schaut um die Ecke."
"Mir wird bewusst, dass ich ziemlich wild aussehen muss, da ich gerade erst aufgewacht bin. Ich werfe mir die übrigen Tabletten in den Mund und fahre mir mit einer Hand durch meine Haare."


show hanagown smile_rn onlayer master at center
with charaenter

ha "Guten Morgen, Hisao."


hi "Ah, gu- ack!"


$ renpy.music.set_volume(0.0, 0.2, channel="ambient")

with vpunch

"Ich antworte ihr und vergesse dabei vollkommen, dass ich gerade dabei war, ein besonders große Tablette zu schlucken. Hustend und nach Atem ringend verschlucke ich mich heftig an ihr."


show hanagown worry_rn onlayer master
with charachange

ha "Ah, Hisao!"


$ renpy.music.set_volume(0.2, 10.0, channel="ambient")

"Nachdem ich laut huste und mir ein paar Mal auf die Brust klopfe, um sie herunterzuwürgen, schaffe ich es, mich wieder einzukriegen."


hi "Mir geht's gut. Sorry, ich hab vergessen, dass ich am Schlucken war."


play music music_happiness fadein 5.0

show hanagown distant_rn onlayer master
with charachange

ha "Entschuldige, ich wollte nicht…"


"Ich halte meine Hand hoch, um ihr zu signalisieren, dass sie aufhören soll."


hi "Ich habe mich verschluckt. Es war mein Fehler. Morgen, Hanako."


"Sie hält einen Moment inne, bevor sie sich zur Antwort leicht verbeugt."


show hanagown distant_rn onlayer master at tworight
show bg hok_lounge_rn onlayer master at bgright
with charamove

show lilly basic_sleepy_paj_rn onlayer master at twoleft
with charaenter

"Hinter Hanako läuft – nein, torkelt – Lillys vertraute Gestalt ins Zimmer, ebenfalls im Pyjama. Mit ihren Augen voller Schlaf und ihrem ungepflegten Haar ist sie ein wunderbarer Anblick."


hi "Hi, Lilly."


show lilly basic_weaksmile_paj_rn onlayer master at twoleft
with charaenter

li "Guten Morgen… Hisao."


"Für eine Weile hängt eine Stille in der Luft, da niemand von uns weiß, was er tun soll."


"In Anbetracht dessen, was gestern passiert ist, haben wir beide mehr als genügend Gründe, um diese Situation peinlich zu finden. Wie sollen wir auf ein Aufeinandertreffen nach… so etwas… reagieren?"


"Die beste Vorgehensweise wäre wohl, mit Lilly allein zu reden und die Dinge und Ordnung zu bringen."


hi "Ähm, ich… mache dann mal das Frühstück."


"Offenbar merkt Lilly, was ich vorhabe."


show lilly basic_smileclosed_paj_rn onlayer master
with charachange

li "Ich helfe. Hanako, könntest du den Tisch decken?"


"Sie nickt. Danach verschwindet ihr Kopf in einem Geschirrschrank, als sie sich zügig ihrer zugeteilten Aufgabe widmet."


$ renpy.music.set_volume(0.1, 0.5, channel="ambient")

scene bg hok_kitchen_rn onlayer master
with locationchange

"Ich reibe mir noch etwas Schlaf aus den Augen und schlendere zum Kühlschrank, um etwas Milch herauszunehmen. Währenddessen nimmt Lilly neben mir zahlreiche farbenfrohe Boxen aus den unteren Schränken."


"Während wir eine eher fade aussehende Mahlzeit zubereiten, flüstere ich etwas leiser als sonst. So wie ich Lillys Gehör kenne, wird sie keine Probleme damit haben, mich zu verstehen."


hi "Geht es dir gut, Lilly? Nach letzter Nacht…"


show lilly basic_reminisce_paj_rn onlayer master at center
with charaenter

"Mit einem müden Gesichtsausdruck nickt sie zaghaft."


"Auch wenn ihre Erschöpfung sicherlich einen Teil dazu beiträgt, scheint sie sich aufrichtig unsicher darüber zu sein, was zwischen uns passiert ist, und wie sie damit umgehen soll."
"Wenn man bedenkt, dass ich das Gleiche empfinde, kann ich es ihr nicht wirklich verübeln."


show lilly basic_sad_paj_rn onlayer master
with charachange

li "Es tut mir leid, Hisao. Ich konnte gestern nicht klar denken. Ich habe keine Sekunde an dich oder Hanako gedacht, und bin sogar so weit gegangen, dass…"


"Sie steigert sich hinein. Als sich ihre Hände anspannen und ihre Stimme spitzer wird, gebe ich ihr einen sanften Stoß, um die Situation etwas aufzulockern."


hi "Du musst dich nicht entschuldigen. Ich habe doch gesagt, dass ich dich auch mag."


show lilly basic_oops_paj_rn onlayer master
with charachange

li "Aber ich…"


"Als sie droht, aus der Fassung zu geraten, wird es offensichtlich, dass es keine Alternative gibt."


show lilly basic_sad_paj_close_rn onlayer master
with characlose

"Ich drehe mich zu Lilly und umarme ihren hochgewachsenen Körper. Sie leistet überhaupt keinen Widerstand und beruhigt sich glücklicherweise wieder ein bisschen."


show lilly basic_sad_paj_close_rn onlayer master at twoleft
show bg hok_kitchen_rn onlayer master at bgleft
with charamove

show hanagown normal_rn onlayer master at tworight
with charaenter

"Obwohl meine beruhigende Umarmung nur ein paar Sekunden dauert, bemerke ich Hanako, die uns wortlos zusieht. Der Teller in ihrer Hand schwebt Zentimeter über dem Tisch, da sie bei unserem Anblick mitten in der Bewegung erstarrt ist."


stop music fadeout 2.0

scene bg hok_lounge_rn onlayer master
show hanagown distant_rn onlayer master:
    tworight
    ypos 1.15
show lilly basic_sleepy_paj_rn onlayer master:
    twoleft
    ypos 1.17
with shorttimeskip

$ renpy.music.set_volume(0.2, 0.5, channel="ambient")

"Das Geklapper der Tischutensilien und der Teller ist das einzige Geräusch, das während unseres stillen Essens zu hören ist. Vorhin waren wir uns vielleicht nur unseretwegen unsicher, doch nun hat sich die ganze Situation geändert."


"Nach Wochen seliger Freundschaft, an denen wir uns die Tage mit gemeinsamen Essen und fast bedeutungslosem Geschwätz vertrieben haben, hat sich die Beziehung zwischen mir und Lilly – nein, zwischen uns allen – unumkehrbar verändert."


"Ich halte das nicht aus."


hi "Lilly…"


stop ambient fadeout 25.0

show lilly basic_listen_paj_rn onlayer master
with charachange

"Sie nickt ernst und legt ihren Löffel behutsam auf den Teller vor sich. Keiner von uns weiß genau, wie wir einander sehen – geschweige denn, wie Hanako uns sieht."


show lilly basic_weaksmile_paj_rn onlayer master
with charachange

li "Das mag vielleicht etwas plötzlich sein, aber… ich habe Hisao meine Liebe gestanden."


show hanagown distant_blush_rn onlayer master
with charachange

"Für einen Moment sieht Hanako fast verwirrt aus; genau die Reaktion, die ich von ihr erwartet hatte. Schließlich nickt sie – den Löffel immer noch in ihrem Mund."


show hanagown normal_blush_rn onlayer master
with charachange

ha "Und was ist mir dir?"


hi "Ich fühle genauso."


show hanagown smile_rn onlayer master
with charachange

"Sie schenkt uns ein Lächeln. So groß und so ehrlich, dass ich erröte. Ich glaube, ich habe sie noch nie so strahlen sehen."


play music music_serene fadein 6.0

ha "Dann bin ich glücklich. Ich bin wirklich, wirklich glücklich."


show lilly basic_sleepy_paj_rn onlayer master
with charachange

li "Es tut mir leid, dass ich dir vorher nichts davon erzählt habe. Die Dinge sind…"


"Hanako schüttelt energisch ihren Kopf und vergisst in ihrer Eile anscheinend, dass Lilly es gar nicht bemerken kann."


show hanagown distant_blush_rn onlayer master
with charachange

"Sie beginnt mit ihren Händen zu spielen und sieht dabei etwas nervöser aus als zuvor."


ha "Um ehrlich zu sein, ich habe vor einer Weile schon gedacht, dass ihr euch mögen könntet. Zuerst wusste ich nicht wirklich, was ich davon halten sollte… aber ich…"


show hanagown smile_rn onlayer master
with charachange

ha "Dann habe ich mir gedacht, wenn meine Freunde glücklich sind, dann bin ich es auch."


ha "Ich war wirklich glücklich, einen weiteren Freund zu haben, als wir Hisao kennengelernt haben. Dass du durch ihn nun auch Liebe gefunden hast, ist doch sogar noch besser… oder?"


"Ein Gefühl der Erleichterung, dass sie unsere Beziehung so einfach akzeptiert, überkommt mich wie eine Flutwelle. Ihrem Gesichtsausdruck nach zu urteilen, geht es Lilly genauso."


show lilly basic_weaksmile_paj_rn onlayer master
with charachange

li "Danke, Hanako. Ich schätze es wirklich, dass du so verständnisvoll bist."


show hanagown distant_rn onlayer master
with charachange

"Lillys Stimme klingt immer noch leicht entschuldigend, oder zumindest unsicher. Hanako bemerkt das ebenfalls. Sie scheint einen Moment lang zu überlegen, dann wendet sie sich mir zu."


show hanagown smile_rn onlayer master
with charachange

ha "Hisao, hättest du etwas dagegen, wenn Lilly und ich ein bisschen nach draußen gehen?"


hi "Ah, nein, nur zu…"


show lilly basic_surprised_paj_rn onlayer master
with charachange

li "Hanako?"


show hanagown smile_rn onlayer master at tworight
with charamove

show lilly basic_surprised_paj_rn onlayer master at twoleft
with charamove

hide lilly onlayer master
hide hanagown onlayer master
with charaexit

stop ambient
$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

"Hanako steht von ihrem Stuhl auf, nimmt Lilly bei der Hand und zerrt sie vor Aufregung fast vom Tisch weg."
"Da Lilly sich normalerweise eher ruhig und gelassen bewegt, ist Hanakos Hektik für sie so ungewohnt, dass sie ein paar Mal fast das Gleichgewicht verliert."


"Es ist ein ziemlich amüsanter Anblick, der mich sprachlos zurücklässt, während sie durch die Tür verschwinden."
"Erst jetzt merke ich, dass der Regen aufgehört und einem weitaus lebhafteren und helleren Himmel gewichen ist, um das trübe Grau des Morgens wiedergutzumachen."


"Für Hanako muss das eine ziemlich große Offenbarung sein. Lilly und ich sind wirklich die einzigen Menschen, mit denen sie etwas zu tun hat. Fast, als wären wir ihre Eltern."


"Ich schätze, das könnte vielleicht die beste Art sein, unsere Beziehung zu beschreiben. Ein Vater, eine Mutter und eine Tochter – alle fröhlich in unserer kleinen Schein-Familie, als könnte es für immer so weitergehen."


"Es ist vielleicht eine seltsame Dynamik – und dazu eine, die gewiss nicht lange anhalten kann… Aber vielleicht, nur für diesen kleinen Moment, ist es okay."


"Als ich vom Tisch aufstehe, um Lilly und Hanako zu den Feldern draußen zu folgen, nicke ich mir selbst bestätigend zu."


"Dieser kleine Moment des Glücks, ganz egal wie kurz, wird überdauern. Für mich, für uns alle… für immer."


stop music fadeout 2.0

label de_L19:

scene bg hok_bath onlayer master
show steam onlayer master
with shorttimeskip

"Bis zum Hals im heißen Wasser liegend stoße ich ein langgezogenes Seufzen aus. Zu spüren, wie sich jeder Muskel in meinem Körper entspannt, ist pure Euphorie."


"Ich habe keine Ahnung, wie lange es her ist, dass ich ein richtiges heißes Bad genommen habe, aber im Augenblick ist es mir auch ganz egal."


play music music_dreamy fadein 2.0

nvl clear
window hide

nvl show dissolve

n "Vielleicht messe ich der Tatsache, dass ich ausnahmsweise mal ein echtes Bad nehmen kann, mehr Wert bei als ich sollte; die Gelegenheit, einfach mal zur Ruhe zu kommen und mir selbst etwas Zeit zu gönnen, ist eine willkommene."


n "Hanako, Lilly und ich sind draußen herumgewandert und haben das überraschend weitläufige Umfeld des Hauses erkundet. Dann haben wir den Großteil des Nachmittags mit Ausruhen, Fernsehgucken, Lesen und Kartenspielen verbracht."


n "Es mag nicht das aufregendste Finale für diesen Ausflug gewesen sein, aber diese ruhige Friedlichkeit sollte man auskosten. Auch nachdem wir zur Schule zurückgekehrt sind, werde ich mich wohl lange an dieses kleine Haus in Hokkaido erinnern."


n "Schade, dass wir nur noch ein paar Stunden hier verbringen können, bis wir den Zug nach Hause nehmen."


n "Ich kann einfach nur zufrieden gähnen, während ich den langsam von der stillen Wasseroberfläche aufsteigenden Dampf beobachte, bis meine Augen an der Decke haften bleiben."


n "Unsere Prüfungen stehen bevor. Ich habe kaum für alle gelernt."


n "Darüber hinaus weiß ich nicht einmal, was ich nach meinem Abschluss tun werde. Alle Prüfungen zu bestehen, ist schön und gut – aber zu welchem Zweck?"


n "Und ausgerechnet jetzt fange ich eine Beziehung an."


nvl clear
nvl hide dissolve
window show

hi "Was zum Teufel treibe ich nur?"


"…"


"… Ich schätze, so sollte ich nicht denken. Was geschehen ist, ist geschehen, und vielleicht könnte man das einfach als weiteren Aspekt meines neuen Lebens betrachten, an dem ich arbeite."


"Ich genieße es, mit Lilly zusammen zu sein, und im Leben geht es immerhin um mehr als nur Schule und eine Karriere."


"Während ich eifrig versuche, aus den bisherigen Geschehnissen schlau zu werden, klopft es ein paar Mal kurz an der Tür. Ich raffe mich auf, sitze aufrecht und überlege, wer es sein könnte."


"Drei, nicht mehr und nicht weniger. Leicht und doch fordernd, und so gleichmäßig, dass man mit ihnen ein Metronom eichen könnte. Ich wäre extrem überrascht, wenn es nicht Lilly wäre."


li "Darf ich… reinkommen?"


"Jepp, es ist Lilly."


hi "Ich komme sofort raus, ich bin immer noch in der Wanne."


li "… Ich weiß."


stop music fadeout 3.0

"Die Stimme, die von der anderen Seite der Tür kommt, lässt mich erstarren. Nach nochmaliger Überlegung lehne ich mich an die Seite der Wanne und lasse meine Arme über den Rand hängen."


"Obwohl ich mir Mühe gebe, es zu verhindern, kann ich nicht anders, als meine Gedanken abschweifen zu lassen."


hi "S-Sicher, komm rein."


show lilly basic_smileclosed_cas onlayer master at Alphain(1.0), Slide(0.4, 0.5, 0.5, 0.5, 1.0)
with Pause(1.0)

"Sie öffnet die Tür, läuft langsam in den Raum und schließt die Tür hinter sich. Im Gegensatz zu meinem rasenden Herz sieht sie seltsam gelassen aus."


hi "Ah… h-hi… Lilly."


play music music_one fadein 9.0

show lilly basic_smile_cas onlayer master at center
with charachange

li "Würde es dich stören, wenn ich mit dir zusammen baden würde?"


hi "Überhaupt nicht. Nur zu."


show lilly basic_listen_cas onlayer master at center
with charachange

"Mit einem kleinen Nicken beginnt sie, ihren Pullover auszuziehen, wodurch ihre Brust Stück für Stück sichtbar wird."


hi "Ich könnte das für dich tun, wenn du willst."


show lilly basic_emb_cas onlayer master at center
with charachange

li "Abgelehnt."


hi "Wieso?"


show lilly basic_pout_cas onlayer master at center
with charachange

li "…"


"Ihr Gesicht zeigt, dass ihr noch nicht allzu wohl bei dem Gedanken ist, mich an sie heranzulassen. Ich kann es ihr nicht wirklich verübeln."


hide lilly onlayer master
with charaexit

play sound sfx_rustling

"Sie zieht sich weiter aus. Ihr Hemd und Rock fallen auf den Boden, bis sie nur noch ihre weiße Unterwäsche anhat. Schließlich steht sie nackt in der Mitte des Raumes."


label de_L19h:

show lilly behind_sleepy_nak onlayer master at center
with charachange

"Verglichen mit dem letzten Mal ist es viel einfacher, ihrer gesamte Figur zu betrachten. Es ist ein wunderbarer Anblick."


li "Hisao?"


hi "Hmm?"


show lilly behind_pout_nak onlayer master at center
with charaenter

li "Du denkst gerade an etwas Perverses, stimmt's?"


hi "Was willst du von mir? Du ziehst dich direkt vor mir aus."


show lilly behind_weaksmile_nak onlayer master at center
with charachange

"Sie kneift nachdenklich ihre Augenbrauen zusammen."


li "Ich schätze, für dich wäre das etwas erotischer als für mich."


hi "Warum?"


hi "… Ah."


show lilly behind_giggle_nak onlayer master at center
with charachange

"Sie gibt ein kleines, fröhliches Kichern von sich, das ihre Nerven etwas zu beruhigen scheint."


show lilly behind_smile_nak onlayer master at center
with charachange

li "Wenn das zu viel für dich ist, Hisao, kann ich später wiederkommen."


hi "Nein, nein, das ist okay. Ich bin nur ein bisschen… na ja…"


hi "Du bist wirklich wunderschön, weißt du."


show lilly behind_emb_nak onlayer master at center
with charachange

"Mein ehrlicher Kommentar lässt Lilly knallrot anlaufen."


li "Hisao…"


"Ich grinse etwas. Sie ist süß, wenn sie überrumpelt wird."


show lilly behind_smileclosed_nak onlayer master at center
with charachange

li "Wie dem auch sei – darf ich reinkommen?"


hi "Ah, klar."


hide lilly onlayer master
with charaexit

"Ich lehne mich nach vorne, nehme ihre weichen Hände in meine und helfe ihr über die Badewannenschwelle."


"Sie ertastet den den Rand der Badewanne und lässt sich dann langsam ins Wasser sinken. Mein Atem stockt, als sie sich so hinsetzt, dass sie mit dem Rücken an meiner Brust lehnt. Ich hatte erwartet, dass sie sich ans andere Ende setzt."


scene evh lilly_bath_smile_small onlayer master
with whiteout

"Ich atme tief aus, um mich selbst zu beruhigen, lege meine Arme auf die Badewannenränder und versuche, meine Triebe im Zaum zu halten."


"Ich vermisse nicht einmal den Anblick ihrer… Vorzüge; das Gefühl ihres Körpers an meinem ist überraschend entspannend. Wenn Lilly so empfindlich gegenüber Berührungen ist, muss es für sie noch entspannender sein."


li "Du badest ziemlich heiß, kann das sein?"


hi "Ein bisschen. Willst du, dass ich etwas kaltes Wasser einlaufen lasse?"


"Sie schüttelt leicht ihren Kopf."


li "Nein, es ist gut so."


hi "Okay."


"Die Unterhaltung bricht abrupt ab. Es herrscht Stille."


show evh lilly_bath_emb_small onlayer master
with charachange

"Eine lange und sehr peinliche Stille."


li "Vielleicht war das ein bisschen zu…"


hi "Kein Sorge, es ist okay."


"Die Lage wird sogar noch peinlicher. Als wollte sie sich damit selbst ablenken, fährt Lilly mit ihrer freien Hand über ihre Beine, während sie die andere aus Sittsamkeit über ihre Brüste hält."


"Ich beobachte untätig die Wand vor mir und den aufsteigend Dampf. Ab und zu werfe ich einen flüchtigen Blick auf ihren Körper."


"Das Weiß ihrer Haut glitzert, während sie weiterhin mit ihrer Hand über ihre Beine fährt, was ihre Länge und Form nur noch offensichtlicher macht."


hi "Weißt du, verglichen mit Akira siehst du viel ausländischer aus."


li "Genetisch komme ich nach meiner Mutter. Akira eher nach meinem Vater."


hi "Das ergibt wohl Sinn. Wie in aller Welt sind sich überhaupt eine gebürtige Schottin und ein japanischer Geschäftsmann begegnet?"


li "Meine Mutter war Journalistin. Sie traf meinen Vater, als er bei einer Konferenz in Inverness war."


hi "Ah, ich verstehe. Dass du nach deiner schottischen Seite kommst, würde vermutlich auch deine Größe erklären."


"Ich sehe zurück zu ihr, und sie nickt. Dann seufze ich wegen der Lächerlichkeit der Situation."


hi "Das ist wirklich zu viel, stimmt's?"


show evh lilly_bath_smile_small onlayer master
with charachange

li "Trotzdem gefällt es dir doch, oder?"


hi "Auf gewisse Weise, ja. Ich schätze, am Ende ist alles gut ausgegangen."


hi "Alles hat sich beruhigt, Hanako hat unsere Beziehung gut aufgenommen, und morgen fahren wir zurück zur Schule."


li "In der Tat. Es ist schade, dass wir so bald wieder zurückfahren, aber wir werden immer noch unsere Erinnerungen an diesen Ort behalten."


hi "Erinnerungen, was? Das stimmt wohl. Wir müssen sehen, wie alles läuft, sobald wir zurück sind. Aber im Moment… bin ich einfach froh, dass du etwas für mich übrig hast."


hi "Ich habe mir deswegen wochenlang Gedanken gemacht, darum bin ich dankbar, dass alles so ausgegangen ist."


"Sie nickt und lehnt sich an mich."


"Ich bin mir nicht sicher, ob sie damit einverstanden ist, aber mein Verlangen beginnt zügig, meine Selbstbeherrschung zu übermannen."


hi "Hey, Lilly?"


li "Ja?"


hi "Wie fandest du es? Letzte Nacht, meine ich."


"Sie denkt einen Moment lang nach und sieht dann leicht nach unten. Ein zaghaftes Lächeln formt sich auf ihren Lippen, als sie errötet und ihr Körper sich weiter entspannt. Es ist mehr als genug, um meine Frage zu beantworten."


"Sogar als ich ihr als Antwort leicht zunicke, schwirren Gedanken an die letzte Nacht durch meinen Kopf. In Anbetracht der Situation kann mir das auch wohl niemand übel nehmen."


li "Hisao, dein Herz rast…"


"Sie unterbricht sich, als ich vorsichtig meine Hand auf ihren Schenkel lege. Ich habe mich bisher zwar zurückgehalten, aber die Erinnerung an unser erstes Mal ist genug, um mich klein beigeben zu lassen."


"Ohne ein Wort des Protests lehnt sie ihren Körper gegen meinen. Einen Einladung, die ich kaum ignorieren kann. Ich setze einen kleinen Kuss auf ihren Nacken, bevor ich langsam meine Hand über ihre geschmeidigen Beine gleiten lasse."


li "Hisao, bitte…"


"Sogar als sie das sagt, verziehen sich ihre Mundwinkel zu einem Lächeln, und ihre Stimme schwankt zwischen Scham und verlegenem Gekicher."


show evh lilly_bath_open_small onlayer master
with charachange

"Schließlich nimmt sie eine meine Hände in ihre und führt sie an ihre rechte Brust. Ich schätze die zögernde Führung, die sie bereit ist, mir zu geben."


show evh lilly_bath_grab_small onlayer master
with charachange

"Alle Anzeichen von Anspannung in ihrem Körper lassen nach. Ich genieße weiterhin das Gefühl ihrer weichen Haut, was dadurch verdoppelt wird, dass meine andere Hand zwischen ihre Beine wandert."


"Ich frage mich, ob sie meine Hände intensiver spürt, da durch ihr fehlendes Sehvermögen ihre anderen Sinne so verfeinert wurden."


"Immerhin scheint sie es in überraschendem Ausmaß zu genießen. Es gibt mir ein irgendwie seltsames Gefühl, aber ein angenehmes."


show evh lilly_bath_moan_small onlayer master
with charachange

"Es dauert nur ein paar Minuten, bis ihr Körper sich ein klein wenig zu winden beginnt und ihre Mühen, ihr Stöhnen zu ersticken, sichtbar werden, als sie ihre Lippen spitzt. Ihre scherzhaften, geflüsterten Proteste werden merklich leiser."


"Dies lässt mich bemerken, dass es auch mich zunehmend erregt, wie ihr Körper sich die ganze Zeit an meinem windet."


hi "Lilly…"


show evh lilly_bath_smile_small onlayer master
with charachange

"Ich ziehe meine Hand zurück, um ihren benebelten Sinnen Zeit zum reagieren zu geben. Nickend steht sie wackelig auf und bietet mir ihre Hand an, um mich aus der engen Badewanne zu führen."


scene evh lilly_afterbath_open_small onlayer master
with locationchange

"Wir beide steigen gleichzeitig aus dem Bad und halten uns dabei an den Händen."


"Schließlich setze ich mich neben die Badewanne."
"Wir beide zappeln noch etwas herum, bis wir es bequem haben. Mit einem kleinen, verzweifelt zurückgehaltenen Keuchen, um zu verhindern, dass sie von draußen gehört werden kann, lässt sie sich einmal mehr auf mich herab."


"Die Art, wie sie sich bewegt, macht es offensichtlich, dass sie immer noch kurz vor ihrem Höhepunkt sein muss."


"Sie fängt langsam an, ihre Hüften auf und ab zu bewegen. Ihre Zunge findet meine, als sie mein Gesicht nach oben hält. Ich merke, wie sehr es mich erregt hat, sie zu befriedigen."


scene evh lilly_afterbath_shut_small onlayer master
with locationchange

li "Hisao… Hisao…"


"Obwohl ihre getrübten Augen geschlossen sind, zeigt ihr fester werdender Griff an meinen Schultern, dass sie sich dem Ende ihres Durchhaltevermögens nähert."


"Als unsere Atmung heftiger und heftiger wird, spüre ich, wie auch ich mich schnell meinem Limit nähere."


"Eine Reihe von rauen Atemzügen ist die einzige Warnung vor ihrem finalen, ekstatischen Keuchen. Ihr gesamter Körper verkrampft sich, und ihre Fingernägel graben sich in meine Schultern."


"Meine Lenden stoßen gegen ihre, und wir beide verharren in dieser Position, als wir den Höhepunkt erreichen."


with Fade(0.5,1.0,4.0, color="#FFF")
stop music fadeout 8.0

"Nach ein paar kostbaren Sekunden ist alles vorbei. Lilly sackt auf mir zusammen, während ich versuche, wieder zu Sinnen zu kommen."


hi "Das war… gut…"


"Bevor sie antwortet, atmet sie kurz durch und richtet sich nickend auf."


li "Mhm…"


"Dann neigt sie ihren Kopf nach unten, um mir einen kleinen Kuss zu geben. Mit meiner Hand streiche ich daraufhin Strähnen ihres zerzausten Haares aus ihrem Gesicht, und wieder sitzen wir beide in seliger Stille da."


stop music fadeout 2.0

scene black onlayer master
with dissolve

label de_L20:

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_trainint fadein 5.0

scene ev lilly_trainride_ni onlayer master
show train_scenery_ni onlayer master
show train_scenery_fg_ni onlayer master
show lilly_trainride_ni norm onlayer master at train_shake
with locationchange

"Nach einem chaotisch-hektischem Aufbruch zum Bahnhof und dem Finden unserer Plätze in dem sonst verlassenen Wagon sind wir völlig erschöpft."
"Wenn man auf die Uhr sieht – beinahe Mitternacht – ist es kaum verwunderlich, dass so wenige diesen Zug nehmen."


"Hanako schläft tief und fest an Lillys Schulter, und ich kann mich gerade noch so wachhalten. Die Aufregung, die wir vor einer Weile hatten, hat es wahrscheinlich nicht besser gemacht."


"Wenn mein Hirn richtig funktionieren würden, wäre ich wahrscheinlich ziemlich deprimiert darüber, dass wir wieder zurück zur Schule müssen."


"Jedoch ist für den Augenblick der Anblick der vorbeiziehenden nächtlichen Landschaft überraschend schön."


"Mein lautes Gähnen wird fast völlig vom Geklapper des alten Wagons auf den Schienen übertönt."


hi "Müde…"


play music music_comfort fadein 2.0

show lilly_trainride_ni ara onlayer master at train_shake
with charachange

li "Und wessen Schuld ist das, Hisao?"


"Manchmal verwischt sie wirklich die Grenze zwischen beleidigend und belustigend. Allerdings schaffe ich es, mich zu einem schwachen Lächeln zu zwingen."


"Ich schaue aus dem Fenster. Mein Spiegelbild ist gerade so auf der klaren Fensterscheibe zu sehen. Ehrlich gesagt hat sie vollkommen Recht. Wäre dieses kleine Intermezzo vor ein paar Stunden nicht gewesen, hätten wir beide viel mehr Energie."


"Darüber hinaus mussten wir beide ein weiteres Bad nehmen, weswegen wir beinahe unseren Zug verpasst haben."


hi "Ja, ja, es war meine. Trotzdem ist es gefährlich, mit einem Kerl ins Bad zu steigen."


show lilly_trainride_ni smile onlayer master at train_shake
with charachange

li "Offensichtlich."


hi "Sorry. Ich schätze, ich hab da irgendwie die Situation ausgenutzt."


show lilly_trainride_ni weaksmile onlayer master at train_shake
with charachange

li "Na ja… ich hatte ja auch nicht wirklich etwas dagegen…"


"Als sie verstummt, sehe ich sie erneut an. Ich kneife meine Augen zusammen, als ich ihre leicht geröteten Wangen und ihr kleines Grinsen sehe. Ihre Gedanken sind offenbar woanders."


hi "Sag es."


li "Ich… wusste, dass es eventuell… passieren könnte."


hi "Wusste ich's doch. Du bist genauso versaut wie ich."


"Zügig hustet sie in ihre freie Hand, womit sie mir ihr Missfallen deutlich macht."


show lilly_trainride_ni pout onlayer master at train_shake
with charachange

li "Auf diese Weise klingt es ziemlich geschmacklos."


hi "Oh? Und was würdest du vorschlagen?"


li "Ich habe lediglich einen für Heranwachsende gesunden Sextrieb."


hi "Also in anderen Worten: versaut."


"Plötzlich murmelt Hanako leise, als sie auf Lillys Schoß ihre Stirn runzelt. Fast wirkt es, als wäre sie der Unterhaltung gefolgt."


show lilly_trainride_ni opensmile onlayer master at train_shake
with charachange

"Lillys missbilligender Blick schmilzt dahin, als sie sanft lächelt und Hanakos langes, dunkles Haar streichelt."


"Alles, was ich tun kann, ist zusehen. Zusehen und lächeln."


"Falls mich jemand fragen würde, wann ich mich in sie verliebt habe, könnte ich nicht antworten. Das Beste, was mir einfallen würde, ist: „Es ist einfach irgendwann passiert, aber ich habe es nicht bemerkt.”"


"Falls mich jedoch jemand fragen würde, warum ich sie liebe, fiele mir die Antwort viel leichter."


hi "Du liebst Hanako wirklich, nicht wahr?"


show lilly_trainride_ni smile onlayer master at train_shake
with charachange

"Sie nickt und schenkt mir ein warmes Lächeln."


label de_choiceL20:
menu:
    with menueffect
    li "Es ist schade, dass wir zurück zur Schule müssen. Während dieses Ausflugs hat sie sich so entspannt."
    "Über Hanako reden.":



        return m1
    "Über die Schule reden.":

        return m2


label de_L20a:


$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

hi "Ich würde mir keine Sorgen machen. Hanako hat dank dir an Selbstbewusstsein gewonnen. Zumindest in der Zeit, in der ich euch beide kenne."


show lilly_trainride_ni weaksmile onlayer master at train_shake
with charachange

"Sie seufzt selbstkritisch."


li "Ich denke, ich habe ihr lediglich Gesellschaft und Unterstützung geleistet. Seit sie dich kennengelernt hat, ist sie viel offener geworden – sogar mir gegenüber."


"Ich fange an zu glauben, dass sie mit ihrem Einfluss auf Hanako untertreibt. Besonders weil Hanako keine wirklichen Freunde hatte, bevor die Zwei sich kennengelernt haben."


"Die Freunde, die ich an meiner alten Schule hatte, erfüllten meine Erwartungen an sie – meistens haben wir uns nur über belanglose Dinge unterhalten. Doch bei Hanako und Lilly fühlt es sich wirklich so an, als wäre ihre Beziehung mehr als das."


"Ein Teil von mir beneidet sie, doch ein anderer kann die Tatsache nicht vergessen, dass dieses Schuljahr irgendwann enden wird."
"Ich habe wirklich keine Ahnung, was Hanako tun wird. Dieser Ausflug hat mir nur gezeigt, wir sehr wir alle voneinander abhängig sind."


"Jedenfalls müssen wir alle Entscheidungen treffen. Vielleicht ist das der Grund, warum ich dieses rastlose Gefühl nicht loswerde – ungeachtet dessen, dass unsere Rückkehr zur Schule auch eine Rückkehr zum normalen, alltäglichen Leben verkündet."


label de_L20b:


$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

hi "Stimmt. Bald fangen auch die Prüfungen an; das wird ein ganz schöner Stress. Glaubst du, dass du gut vorbereitet bist?"


show lilly_trainride_ni weaksmile onlayer master at train_shake
with charachange

li "Ich denke schon. Aber ich glaube nicht, dass die Zeit angenehm wird."


"Da muss ich ihr zustimmen."
"Die Prüfungen hatte ich in letzter Zeit aus meinem Kopf verdrängt, und auch wenn ich gute Noten in den meisten Tests bekommen haben mag, kann ich nicht davon ausgehen, dass ich sie genauso leicht bestehe, wenn ich so wenig gelernt habe."


"Lilly scheint fleißiger – oder zumindest gewissenhafter – zu sein als ich. Gleichwohl kämpft sie wohl damit, dass sie in manchen Fächern eher schlecht abschneidet, egal wie sehr sie es auch versucht."


hi "Wenigstens dauern sie nur eine Woche."


label de_L20c:


hi "Das Gute ist, nach den Prüfungen dauert es nicht mehr lange bis zu den Sommerferien. Wir könnten dann hierher zurückkommen, wenn du willst."


"Für einen Augenblick denkt sie über diesen Vorschlag nach, wobei ihr Gesicht irgendwie distanziert wirkt. Ich kann nur raten, dass sie über alles nachdenkt, was hier passiert ist."


show lilly_trainride_ni opensmile onlayer master at train_shake
with charachange

li "Das wäre… schön, denke ich."


"Zustimmend nicke ich und lächle ihr zu."


"Sommer – zusammen mit Lilly. Das scheint der perfekte Plan für die Ferien zu sein."


stop music fadeout 3.0
stop ambient fadeout 3.0

window hide
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
