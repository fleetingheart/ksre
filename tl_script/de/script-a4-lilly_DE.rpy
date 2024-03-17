label de_L21:

window hide None

scene bg school_scienceroom onlayer master
with locationchange

nvl clear
nvl show dissolve

$ renpy.music.set_volume(0.5, 1.0, channel="music")
play music music_normal fadein 1.0

n "\n\n\nNach der ganzen Aufregung mit unserer Fahrt nach Hokkaido ist es richtig seltsam, so schnell wieder zur Tagesordnung überzugehen. Man könnte denken, es wäre ein ganz normaler Tag wie jeder andere."


n "\nNa ja, das würde ich jedenfalls gerne denken."


n "\nUm die Wahrheit zu sagen, hat sich die Atmosphäre in der Klasse… Nein, in der ganzen Schule verändert."


n "Schon seit einiger Zeit war in der Klasse eine gewisse Unruhe spürbar, aber nun, wo die Prüfungen vor der Tür stehen, versucht jeder hektisch, noch möglichst viel zu lernen. Das sieht man nicht oft."


n "Noch ein Tag bis die Prüfungen losgehen. Es war eigentlich unverantwortlich, dass wir unsere Zeit mit einer Reise verschwendet haben, anstatt zu lernen. Dabei sind wir doch solche Musterschüler."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

show misha invis_close onlayer master:
    xanchor 0.5 xpos -0.1
with None

show misha perky_confused_close onlayer master:
    xpos 0.1
show bg school_scienceroom onlayer master at bgright
with dissolvecharamove

window show

"Wenn ich so durch den Klassenraum schaue, ist sogar bei der immer fröhlichen und energiegeladenen Misha irgendwie die Luft raus. Sie sitzt an ihrem Tisch und kaut nervös auf ihrem Füller herum, während Mutou vorne seinen Vortrag hält."


"Moment… Wenn ich genauer hinschaue, glaube ich, dass sie ihn aufisst."


show misha invis_close onlayer master:
    xpos -0.1
show bg school_scienceroom onlayer master at center
with dissolvecharamove

hide misha onlayer master
with None

"Ich reiße meinen Blick von dem traurigen Bild los und wende meine Aufmerksamkeit jemand anderem zu."


show hanako invis onlayer master:
    xanchor 0.5 xpos 1.1
with None

show hanako defarms_strain onlayer master:
    xpos 0.94
show bg school_scienceroom onlayer master at bgleft
with dissolvecharamove

"Hanako macht hektisch Notizen in ihrem Heft, ihr Gesicht nur wenige Zentimeter von dem Blatt entfernt, und versucht anscheinend, jedes Wort, das aus Mutous Mund kommt, auf Papier zu bannen."


show shizu invis onlayer master:
    xanchor 0.5 xpos 0.0
show misha invis_close onlayer master:
    xanchor 0.5 xpos -0.1
with None

show shizu basic_normal onlayer master:
    xanchor 0.5 xpos 0.3
show misha perky_confused_close onlayer master:
    xpos 0.1
show hanako invis onlayer master:
    xpos 1.1
show bg school_scienceroom onlayer master at bgright
with dissolvecharamove

hide hanako onlayer master
with None

"Shizune… Na ja, sie ist eben Shizune. Sie ist die Ruhe selbst, macht sorgfältig Notizen und fokussiert ihre Aufmerksamkeit voll und ganz auf die Tafel."


"Ehrlich gesagt sollte ich das auch tun, aber ich habe das Gefühl, dass ich das momentane Thema bereits recht gut verstanden habe."


"Ich frage mich, wie es Lilly geht. Sie ist zwar gut in der Schule, aber im Gegensatz zu mir hat sie noch so viel anderes um die Ohren."
"Ihre Pflichten als Klassensprecherin, sich um Hanako kümmern, ihre anderen Freunde, ihre zusätzlichen Englischkurse… Sie mutet sich schon einiges zu."


scene bg school_scienceroom onlayer master
with shorttimeskip

play sound sfx_normalbell

"Die Mittagsglocke läutet, und die gesamte Klasse – inklusive Mutou – stößt einen Seufzer der Erleichterung aus."
"Ich habe das Gefühl, dass ihm die lockere Atmosphäre seines normalen Unterrichts lieber ist als die Prüfungsvorbereitungen, mit denen wir uns jetzt abplagen müssen."


mi "Hicchan~…"


show misha invis_close onlayer master:
    xanchor 0.5 xpos 0.1
with None

show misha perky_sad_close onlayer master at twoleft
show bg school_scienceroom onlayer master at bgright
with dissolvecharamove

mi "Hilf mir~…"


"Ich schließe meine Augenlider halb, um klarzustellen, dass ich genau das Gegenteil vorhabe."


mi "Hilf mir, hilf mir, hilf mir~…"


hi "Probleme?"


show misha perky_confused_close onlayer master
with charachange

mi "Bei Shicchan ist alles in Ordnung, aber ich glaube, ich werde sterben. Werde ich sterben, Hicchan? Wirst du zulassen, dass diese ganze Arbeit mich umbringt?"


"Wie armselig. Sie ist weder die intelligenteste Schülerin in der Klasse noch die fleißigste. Da ist es kaum verwunderlich, dass sie mit dem Stoff nicht zurechtkommt."


hi "Tut mir Leid, Misha, aber ich habe selbst genug zu tun. Ich dachte, du und Shizune würdet über das lange Wochenende zusammen lernen?"


show misha sign_sad_close onlayer master
with charachange

mi "Lernen ist zu langweilig, um die Ferien dafür zu verschwenden, Hicchan! Zusammen shoppen zu gehen hat viel mehr Spaß gemacht, nicht wahr, Shicchan?"


show shizu behind_blank behind misha at tworight onlayer master
with charaenter

"Erst jetzt fällt mir auf, dass Shizune uns beobachtet, und dass Mishas Arme sich wohl schon die ganze Zeit bewegt haben. Ich muss wirklich weggetreten gewesen sein, dass ich das nicht bemerkt habe."


hi "Warum wollen Mädchen eigentlich immer Shoppen gehen? Sogar Lilly und Hanako haben mich schon ein paar Mal mitgeschleppt."


show misha hips_grin_close onlayer master
with charachange

mi "Aber du bist trotzdem mitgegangen? Es ist so selten, einen Jungen zu sehen, der gerne shoppen geht~…"


hi "Na ja, ich war wohl eher der Packesel. Ich teile euren Enthusiasmus nicht wirklich."


hi "Zurück zu den Prüfungen. Du hast doch noch gelernt, nachdem du vom Shopping zurück warst, nicht wahr, Shizune?"


show shizu basic_normal2 onlayer master
with charachange

shi "…"


show misha sign_smile_close onlayer master
with charachange

mi "Natürlich, Hicchan. Es wäre doch dumm, so kurz vor den Prüfungen nicht…"


show misha perky_sad_close onlayer master
with charachange

mi "U~rgh."


"Als Misha ihre Eselei bemerkt, macht sie ein Geräusch, das sich wie eine verendende Kuh anhört, und lässt sich schlaff auf ihren Tisch fallen. Sogar ihre beste Freundin lässt sie im Stich."


show shizu basic_angry onlayer master
with charachange

"Nach Shizunes frustriertem Gesichtsausdruck zu urteilen, hat sie ihr vermutlich gesagt, dass sie auch lernen soll."


hi "Keine Sorge, du kannst immer noch ein paar Punkte erreichen, wenn du jetzt anfängst zu lernen."


hi "Vielleicht."


"Misha scheint darüber nicht lachen zu können. Es ist, als hätte man ihren Ballon der ewigen Fröhlichkeit auf grausame Weise zum Platzen gebracht."


show shizu behind_blank onlayer master
with charachange

shi "…"


show shizu behind_blank_close onlayer master
with characlose

with Pause(0.3)

show shizu adjust_frown_close onlayer master
show misha perky_confused_close onlayer master
with vpunch

"Shizunes Gesten bleiben unbemerkt, was Misha einen schnellen Stoß an der Schulter einbringt. Es dauert nur einen Moment, und Misha ist wieder ganz die alte."


show misha hips_smile_close onlayer master
with charachange

mi "Oh. Äh, und was hast du am Wochenende so gemacht, Hicchan?"


hi "Ich habe nur mit Lilly und Hanako einen Kurzurlaub auf Hokkaido gemacht. Es war ganz nett."


show misha perky_smile_close onlayer master
show shizu behind_blank_close onlayer master
with charachange

"Ich sehe, wie beide mich stirnrunzelnd anschauen. Ich bin mir sicher, dass sie gerade sehr schmutzige Gedanken haben. Dass sie damit Recht haben, macht die Situation nur noch peinlicher."


hi "Wir haben nur gelernt und uns die Gegend angeschaut; nichts weiter."


show misha cross_smile_close onlayer master
with charachange

mi "Hmm~…"


"Mir wird bewusst, dass so eine glatte Lüge vielleicht nicht die beste Idee war, wenn ich bedenke, welche Verbindungen Shizune hat und wie rücksichtslos sie Leute ins Verhör nimmt, die sie im Verdacht hat zu lügen."


"Ich habe keine Ahnung, wie sie es aufnehmen wird, aber sie wird es früher oder später sowieso herausfinden. Es geht sie sowieso nichts an, mit wem ich ausgehe."


hi "Und ja, Lilly und ich sind nun zusammen."


show misha hips_grin_close onlayer master
show shizu basic_normal2_close onlayer master
with charachange

"Während Misha die Neuigkeit mit einem enthusiastischen Lächeln aufnimmt, schaut mich Shizune nur leicht überrascht an, versteckt das aber schnell hinter einem neutralen Gesichtsausdruck."


show shizu behind_blank_close onlayer master
with charachange

shi "…"


show misha sign_smile_close onlayer master
with charachange

mi "Mit wem du ausgehst ist deine Sache. Ich wünsche euch beiden alles Gute."


"Mishas Blick sagt mir, dass ich mehr von Shizune nicht erwarten kann. Mehr will ich ja auch eigentlich gar nicht."


show shizu basic_normal2_close onlayer master
with charachange

"Shizune beginnt noch, etwas anderes zu gestikulieren, unterbricht sich aber und schüttelt ihren Kopf, um Misha vom Übersetzen abzuhalten."


hide shizu onlayer master
with charaexit

hide misha onlayer master
with charaexit

"Normalerweise wäre das seltsam genug, aber das aufgesetzt lässige Winken, mit dem Shizune sich von mir verabschiedet, verwirrt mich noch mehr."
"Es ist normalerweise nicht Shizunes Art, Zurückhaltung zu üben oder ohne nachzudenken zu kommunizieren."


"Achselzuckend wende ich mich Hanakos Tisch zu, aber ihr Stuhl ist leer. Eben war sie definitiv noch da – sieht so aus, als wollte sie nicht warten."


"Dann gehe ich eben allein etwas zu Essen holen."


stop music fadeout 2.0

scene bg school_hallway2 onlayer master
with shorttimeskip

"Ich gehe den Gang entlang zu dem unbenutzten Klassenraum, der für uns drei schon fast ein zweites Zuhause geworden ist, und schaue betrübt auf das in Plastik verpackte Salatbrötchen und das Saft-Trinkpäckchen in meiner Hand."


"Das Essen in der Cafeteria ist wirklich unappetitlich. Vielleicht sollte ich es als Strafe für meine jüngsten Ausschweifungen ansehen."


"Als ich die Tür öffne, ist da eine Person weniger als ich erwartet hatte."


scene ev lilly_tearoom onlayer master
with whiteout

play music music_lilly fadein 3.0

"Es ist seltsam. Obwohl ich Lilly nun schon so lange kenne, muss ich an das erste Mal denken, als ich diese Tür geöffnet habe und sie dort im Sonnenlicht sitzen sah."


show ev lilly_tearoom_open onlayer master
with charachange

"Genau wie damals öffnet sie langsam ihre bewegungslosen Augen und spricht mich ruhig an."


li "Guten Morgen, Hisao."


hi "Ich glaube, es ist schon Nachmittag."


hi "War Hanako schon hier? Sie ist aus der Klasse verschwunden, ohne dass ich es bemerkt habe."


scene bg school_miyagi onlayer master
show lilly basic_listen_close onlayer master:
    center
    ypos 1.1
with locationchange

"Lilly greift sich gedankenverloren an die Wange, während ich Platz nehme. Meine Tasche stelle ich wie immer an das nächsten Tischbein und meine wenig ansehnliche Mahlzeit vor mir auf den Tisch."


show lilly basic_reminisce_close onlayer master
with charachange

li "Sie war hier… aber nur kurz. Sie sagte, sie müsse noch für die Prüfungen lernen, und ist in die Bibliothek gegangen."


"Wir können das beide nicht so richtig glauben."


hi "Na ja, zumindest sind ihre Absichten löblich."


show lilly basic_concerned_close onlayer master
with charachange

li "Es ist lieb von ihr, aber sie muss sich nicht so viel Mühe geben, uns alleinzulassen. Ich denke, ich werde mal mit ihr darüber reden."


hi "Das ist wohl das Beste."


show lilly basic_weaksmile_close onlayer master
with charachange

"Eine Weile essen wir still unsere Mahlzeiten; Lilly knabbert elegant an ihren Sandwiches und nippt an ihrem Tee, während ich mein zu trocken geratenes Brötchen esse."


"Die Atmosphäre ist etwas angespannt. Jetzt, wo der Smalltalk beendet ist, wissen wir beide nicht wirklich, worüber wir reden sollen."


"Schließlich sind wir beide mit dem Essen fertig, ohne ein Gesprächsthema gefunden zu haben. Am Ende ist es Lillys sanfte Stimme, die das Schweigen bricht."


show lilly basic_reminisce_close onlayer master
with charachange

li "Es ist viel passiert… nicht wahr?"


hi "Mhm."


"Wieder Stille. Allerdings denken wir beide an dasselbe Thema, und ich glaube, ich bin mir über meine diesbezüglichen Gefühle im Klaren."


hi "Ich weiß, es ging alles ziemlich schnell, aber… ich bereue nichts, was in Hokkaido passiert ist. Gar nichts."


show lilly basic_oops_close onlayer master
with charachange

li "Hisao…?"


"Leicht angespannt nehme ich ihre Hände in meine – teils um sie zu spüren, teils um meine Nerven zu beruhigen."


hi "Ich stehe zu dem, was ich dort gesagt habe, Lilly. Ich liebe dich, und ich werde bei dir bleiben. Ich hoffe, du denkst genauso."


show lilly basic_weaksmile_close onlayer master
with charachange

"Sie denkt eine lange Zeit still nach; es fühlt sich wie eine Ewigkeit an."


show lilly invis_close onlayer master at center
with dissolvecharamove

"Ihre Trance endet, als sie eine ihrer Hände auf meine legt, sich aus ihrem Stuhl erhebt und nach vorne lehnt."


"Ihr Gesicht wirkt leicht nachdenklich, aber nach einem kurzen Zögern treffen ihre Lippen die meinen für einen kurzen Augenblick."


show lilly behind_cheerful_close onlayer master:
    ypos 1.1
with dissolvecharamove

"Ich fühle mich, als hätte mein Gehirn für einen Moment ausgesetzt. Ich nehme kaum wahr, dass Lilly sich wieder auf ihren Stuhl setzt und mich mit leicht geröteten Wangen anlächelt."


show lilly basic_smileclosed_close onlayer master
with charachange

li "Das zu hören, macht mich sehr glücklich, Hisao. Es wäre mir eine Freude, bei dir zu bleiben."


hi "Vielleicht wäre es gut, die Sache etwas langsamer anzugehen als bisher. Wir haben ja immer noch Schule und die Prüfungen."


show lilly basic_giggle_close onlayer master
with charachange

"Sie kichert schelmisch, was irgendwie ansteckend ist."


show lilly basic_smileclosed_close onlayer master
with charachange

li "Das wäre vielleicht wirklich besser."


show lilly basic_smile_close onlayer master
with charachange

li "Was denkst du, wie du in den Prüfungen abschneiden wirst? Wie du schon sagtest, es ist nur noch ein Tag."


hi "Ich hätte wahrscheinlich mehr lernen sollen, aber ich denke, ich werde zurechtkommen."


hi "Allerdings musste ich Misha und Shizune abwimmeln. Sind in eurer Klasse auch alle so besorgt wegen der Prüfungen?"


show lilly basic_weaksmile_close onlayer master
with charachange

"Sie seufzt verärgert – anscheinend ist es wirklich so. Ich bin dankbar, dass wir endlich ein Gesprächsthema gefunden haben."


li "Ich denke schon. Mich haben schon zwei Klassenkameraden um Hilfe gebeten, und es werden sicher noch mehr werden."


hi "Vielleicht solltest du es einfach als deine erste Bewährungsprobe als Lehrerin ansehen?"


show lilly basic_smile_close onlayer master
with charachange

li "Das wäre sicher das Beste."


show lilly basic_smileclosed_close onlayer master
with charachange

li "Bei dem Thema… Wie sieht es denn mit deinem Englisch aus? Soweit ich mich erinnere, war das nicht gerade dein stärkstes Fach, und die paar Sätze, die du gelernt hast, um mit meiner Mutter zu sprechen, werden dir wohl kaum helfen."


"Verdammt, sie hat den Nagel auf den Kopf getroffen."


hi "Treffer versenkt. Wenn es dir nichts ausmacht, könntest du mir dabei ein wenig helfen? Bitte?"


show lilly basic_planned_close onlayer master
with charachange

li "Es wäre mir ein Vergnügen, dir zu helfen, Hisao. Aber als Gegenleistung…"


"Sie sieht mich mit gesenktem Blick an, und ihre verspielte Seite kommt zum Vorschein."


hi "Kein Problem. Aber Hilfe beim Lernen könntest du vielleicht doch besser gebrauchen."


show lilly behind_cheerful_close onlayer master
with charachange

"Sie strahlt mich an und freut sich so sehr über ihren kleinen Sieg, dass ich beinahe rot werde. Ich habe das Gefühl, sie weiß genau, wie sie mich um den Finger wickeln kann, also sollte ich vielleicht besser aufpassen."


"Hier und jetzt ist eine Lerngruppe aber wohl ein guter Weg, uns gegenseitig in unseren schwächeren Fächern zu helfen."


play sound sfx_warningbell

"Die Schulglocke läutet und erinnert uns daran, dass die Zeit für uns nicht still steht."


hi "Huch, die Mittagspause ist schon vorbei. Man vergisst hier so leicht die Zeit."


show lilly basic_weaksmile_close onlayer master
with charachange

li "Dieser Raum ist so weit von den anderen Klubs und Aktivitäten entfernt, dass man kaum etwas davon hören kann. Wahrscheinlich liegt es daran."


show lilly basic_weaksmile_close onlayer master at center
with charamove

"Ein Ort fern von allem anderen, allein mit nur einem Menschen, den sie liebt. Während Lilly aufsteht und ihre Tasche und ihren Stock einsammelt, muss ich an unsere Zeit in Hokkaido zurückdenken."


show lilly basic_satisfied_close onlayer master
with charachange

li "Ach ja, bevor ich gehe… Akira und ich haben morgen Abend eine Heimkehrparty in meinem Zimmer. Hast du Zeit zu kommen?"


"Ihre Stimme holt mich zurück in die Gegenwart."


hi "Mein Kalender ist leer, also sollte ich mir die Zeit fürs Lernen entsprechend einteilen können."


show lilly basic_smileclosed_close onlayer master
with charachange

li "Schön, das zu hören, Hisao."


hi "Weißt du, ich bin wirklich froh, dass du aus Schottland zurück bist. Sobald die Prüfungen vorbei sind, sollten wir etwas mehr Zeit für uns haben."


show lilly basic_smile_close onlayer master
with charachange

li "Mhm. Die Ferien fangen ja auch bald an."


hi "Wir können die Ferien dann auch gleich mit Tanabata beginnen, wie wir es uns am Schulfest versprochen haben."


show lilly basic_arablush_close onlayer master
with charachange

"Sie bringt ihre Hand an ihre Wange und lacht etwas nervös, als sie sich daran erinnert. Gut, dass ich noch daran gedacht habe."


"Ihre Reaktion ist ein wenig seltsam, aber es ist nicht so, als hätte ich sie noch nie verlegen gesehen."


show lilly basic_weaksmile_close onlayer master
with charachange

li "Ich… sollte besser gehen. Bis dann, Hisao."


hi "Bis später."


hide lilly onlayer master
with charaexit

stop music fadeout 6.0

"Ob es nun Gewohnheit ist oder der Wille, ein wenig Normalität aufrechtzuerhalten, hebe ich zum Abschied wie immer meine Hand. Zumindest bin ich mir nun bewusst, dass ich das tue."


"Ich glaube, ich sehe nun mehr Zusammenhänge als vorher – sowohl was Lilly angeht als auch meine eigene Zukunft."


"Die Ketten meiner Vergangenheit fallen endlich von mir ab."


scene black onlayer master
with dissolve



label de_L22:

$ renpy.music.set_volume(0.8, 0.0, channel="music")
play music music_ease fadein 4.0

scene bg school_girlsdormhall onlayer master
with locationchange

"Inzwischen kenne ich mich einigermaßen im Mädchenwohnheim aus. Als ich durch die Flure gehe, höre ich von weiter vorne leises Lachen."


show bg school_girlsdormhall onlayer master at bgleft
with charamove

"Es dauert nicht lange bis ich merke, dass es aus Lillys Zimmer kommt, aber die tiefe weibliche Stimme gehört unverkennbar nicht ihr, sondern ihrer Schwester."


play sound sfx_doorknock2

"Ich klopfe wie üblich drei mal leicht gegen die Tür und habe meine Hand kaum zurückgezogen, als sie auch schon aufschwingt."


show akira invis onlayer master:
    xanchor 0.5 xpos 1.0
with None

show akira basic_smile onlayer master:
    xpos 0.9
with dissolvecharamove

aki "Hey, Hisao."


hi "Hey. Hallo Lilly, Hanako."


scene ev lilly_bedroom onlayer master:
    truecenter
    zoom 1.0 subpixel True
    acdc_warp 8.0 zoom 1.03
with locationchange

"Hanako schaut zögernd zu mir auf, die Hände in ihrem übergroßen pinken Nachthemd vergraben. Neben ihr dreht Lilly ihren Kopf in meine Richtung und lächelt."


"Es wäre eine glatte Lüge, wenn ich sagen würde, dass mir ihr Anblick in diesem Pyjama nicht gefällt."


"Ich sehe, wie Akira mich von der Seite her angrinst, worauf ich mit einem scharfen Blick antworte."


scene bg school_dormlilly onlayer master at bgleft
with locationchange

"Sie nimmt es zur Kenntnis, zuckt mit den Schultern und geht zurück zu dem niedrigen Tisch in der Mitte des Raumes. Als ich es ihr gleichtue, nickt Lilly mir zur Begrüßung zu und schenkt mir eine Tasse Tee ein."


show hanagown distant onlayer master:
    twoleft
    ypos 1.14
show akira basic_smile onlayer master:
    tworight
    ypos 1.14
with charaenter

hi "Schön, dich wiederzusehen, Hanako. Du warst ja in letzter Zeit viel beschäftigt."


"Lilly schaut sehr konzentriert drein, als die hellbraune Flüssigkeit – wie immer vorsichtig mit ihren Fingern abgemessen – aus der Teekanne in die Tasse fließt."


li "Es scheint, als hätte Hanako angefangen, einer Klassenkameradin mit der Schülerzeitung zu helfen. Naomi, nicht wahr?"


show hanagown normal onlayer master
with charachange

"Hanako nickt zustimmend."


"Sogar nach etwa zwei Monaten in der Klasse fällt es mir immer noch schwer, mir die Namen aller meiner Mitschüler zu merken, mit denen ich kaum rede."


"Ich muss eine Weile nachdenken, bis ich den Namen mit einem Gesicht verbinden kann, aber schließlich erinnere ich mich an das Mädchen, das neben Hanako in der letzten Reihe sitzt."


"Naomi Inoue. Sie sieht recht normal aus, abgesehen von ihrem blond gebleichten Haar."


"Sie hat eine sehr fröhliche und direkte Persönlichkeit. Wahrscheinlich hat sie die Gelegenheit gesehen, Hanako für ihren Klub zu gewinnen, als sie nach einem gefragt hat."


"Jedenfalls ist es schön, dass Hanako ihren Freundeskreis erweitert. Als ich sie kennengelernt habe, war allein die Vorstellung, dass sie ohne Lilly einem Klub beitreten würde, einfach nur lächerlich."


hi "Das erklärt, warum du so beschäftigt warst. Macht's Spaß?"


show hanagown smile onlayer master
with charachange

ha "Mhm. Es ist… wirklich interessant."


"Wie immer ist Hanako nicht gerade gesprächig. Manche Dinge ändern sich nie, und Hanakos Persönlichkeit ist wohl eins davon. Sie wird wohl immer davor zurückscheuen, sich anderen zu sehr zu öffnen."


show hanagown smile onlayer master:
    center
    ypos 1.14
show akira basic_smile onlayer master:
    right
    ypos 1.14
show bg school_dormlilly onlayer master at center
with charamove

show lilly invis onlayer master at left
with None

show lilly basic_smileclosed_paj onlayer master:
    ypos 1.17
with dissolvecharamove

"Vor mir erklingt das Geräusch von Porzellan auf dem Tisch, als Lilly vorsichtig die Tasse vor mir abstellt. Ich danke ihr und trinke einen langen Schluck."
"Hanako und Lilly widmen sich ihren eigenen Tassen, und Akira trinkt aus einer Tasse mit anscheinend sehr starkem schwarzem Kaffee."


show akira basic_laugh onlayer master
with charachange

aki "Du bist ein richtiger Glückspilz, Hisao."


hi "Hm?"


"Ihr Grinsen ist immer noch erkennbar, obwohl sie die Teetasse an ihre Lippen gepresst hat. Ich kann mir eine Grimasse nicht verkneifen."


show akira basic_ending onlayer master
with charachange

aki "Du siehst meine Schwester in ihrem Schlafanzug. Eine Menge Jungs würden jetzt gerne mit dir tauschen."


"Ich habe bereits viel mehr von ihr gesehen – nicht, dass ich das hier zugeben würde."


show lilly basic_emb_paj onlayer master
with charachange

li "Akira!"


show akira basic_smile onlayer master
with charachange

aki "Hey, ich zieh ihn doch nur ein bisschen auf."


"Sie lehnt sich so weit es geht zu mir hinüber und flüstert mit einem durchtriebenen Grinsen auf dem Gesicht."


show akira basic_kill onlayer master
with charachange

aki "Und Hanako auch. Du Lustmolch."


hi "Hey, das war ihre Idee."


show hanagown distant_blush onlayer master
with charachange

ha "Äh, ich… äh…"


"Wir schauen beide zu ihr hinüber. Ihr Gesicht ist direkt auf den Boden gerichtet, und ihre Hände liegen unruhig im Schoß ihres Nachthemds."


show hanagown smile onlayer master
with charachange

ha "Wenn… es Hisao ist… macht es mir nichts aus…"


"Ah, das könnte ein Problem sein. Ich weiß, dass Hanako viel zu unschuldig ist, um in diese Aussage zu viel hineinzulesen, aber der Blick, den Akira mir zuwirft, ist geradezu stürmisch."


show lilly basic_concerned_paj onlayer master
show hanagown normal onlayer master
with charachange

li "Ähm… Akira… bitte…"


"Es scheint, als ob Lilly Akiras plötzlichen Stimmungsumschwung ebenso gespürt hat wie ich, sogar ohne ihr Gesicht sehen zu können."


show akira basic_boo onlayer master
with charachange

"Akira wendet langsam ihren Blick von mir ab, wie ein Kampfhund, den man im letzten Moment an die Leine genommen hat. Ich atme erleichtert auf."


"Ich kann mir keinen günstigeren Zeitpunkt vorstellen, um das Thema zu wechseln."


hi "Ich hoffe, es stört dich nicht, wenn ich frage, Akira, aber was machst du eigentlich beruflich? Ich habe dich noch nie ohne diesen Anzug gesehen."


show akira basic_laugh onlayer master
with charachange

aki "Machst dir Gedanken, was du nach der Schule machen sollst, was?"


show akira basic_smile onlayer master
with charachange

aki "Ich bin Anwältin. Hauptsächlich arbeite ich in der Rechtsabteilung der japanischen Zweigstelle unseres Familienunternehmens."


aki "Das ist wohl die langweiligste Antwort überhaupt. Recht ist für die meisten ein sehr trockenes Thema."


hi "Ziemlich."


show akira basic_lost onlayer master
with charachange

aki "Hey, du sollst mir da nicht zustimmen."


show lilly basic_giggle_paj onlayer master
show hanagown normal onlayer master
show akira basic_smile onlayer master
with charachange

"Lilly kichert belustigt, während sie immer noch ihre Tasse und Untertasse hält; Hanako stimmt schnell mit ein."


"Diese freundliche Atmosphäre unter uns hatte ich vermisst, während Lilly und Akira fort waren. Hanakos Probleme hatten daran zwar sicher einen großen Anteil, aber ich denke, allein dass Lilly nicht da war, hat unsere Laune schon gedrückt."


show lilly basic_smileclosed_paj onlayer master
with charachange

li "Es ist schön, wieder da zu sein. Ich habe dich vermisst, Hisao, und dich auch Hanako."


hi "Wir dich auch. Ich nehme an, deine Klassenkameraden waren auch froh, dich wiederzusehen."


show lilly basic_ara_paj onlayer master
with charachange

li "In gewisser Hinsicht, ja."


show akira basic_laugh onlayer master
with charachange

"Akiras amüsiertes Prusten zeigt, dass ihr Lillys Haltung zu solchen Redewendungen durchaus bewusst ist. So lange wie die beiden schon zusammen sind, ist das wohl auch nicht ungewöhnlich."


show hanagown normal onlayer master
with charachange

ha "Hattet ihr Spaß in Schottland?"


$ renpy.music.set_volume(0.1, 2.0, channel="music")

"Einen Moment lang wundere ich mich, warum sie fragt – es ist ja schon eine Weile her, dass sie zurück sind – aber dann erinnere ich mich an alles, was passiert ist."
"Wir hatten vor lauter Prüfungen und der Fahrt nach Hokkaido noch gar keine Zeit, darüber zu reden."


show lilly basic_reminisce_paj onlayer master
show akira basic_annoyed onlayer master
with charachange

"Lilly sieht einen Moment lang etwas abwesend aus, und dass Akiras erste Reaktion ist, zu ihrer Schwester zu schauen, entgeht mir auch nicht. Aber sie fasst sich schnell wieder."


$ renpy.music.set_volume(0.8, 0.4, channel="music")

show akira basic_smile onlayer master
show lilly basic_weaksmile_paj onlayer master
with charachange

li "Es war… nett. Ich… Wir… hatten unsere Familie schon sehr lange nicht mehr getroffen, also war es ein wundervolles Wiedersehen."


show akira basic_boo onlayer master
with charachange

aki "Ja, das stimmt wohl. Ihr Haus am Strand war aber das Beste daran."


"Ihr abweisender Tonfall weckt in mir den Eindruck, dass Akira ihre Familie nicht so sehr mag wie Lilly es tut."


show lilly basic_giggle_paj onlayer master
with charachange

li "Das mochtest du nur, weil du endlich genug Zeit zum Herumspielen hattest."


show akira basic_ending onlayer master
with charachange

aki "Nur weil ich die bessere Schwimmerin bin…"


show lilly basic_smileclosed_paj onlayer master
with charachange

li "Ich gehöre eben nicht zum athletischen Teil unserer Familie – das ist alles."


show akira basic_laugh onlayer master
with charachange

aki "Nun, du kannst dich damit trösten, dass du wenigstens die Gene für die Körpergröße geerbt hast."


show akira basic_boo onlayer master
with charachange

aki "Und die für die Oberweite…"


show lilly basic_weaksmile_paj onlayer master
with charachange

li "Das ist nicht wirklich etwas, worüber man vor anderen reden sollte…"


"Obwohl Lilly so tut, als würde sie Akira schelten, hat sie ein unübersehbares, freches Grinsen im Gesicht."


show hanagown distant_blush onlayer master
with charachange

"Ihrem gleichgültigen Gesichtsausdruck nach zu urteilen, macht das Akira nicht wirklich etwas aus. Mir geht es genauso, aber neben mir läuft Hanako knallrot an."


"Abgesehen von den Mätzchen der beiden Schwestern… Ihre Eltern scheinen wirklich auf großem Fuß zu leben."


"Es scheint ein ganz anderes Leben zu sein, als das, das Lilly und Akira bisher gelebt haben. Das muss wohl praktische Gründe gehabt haben."


"Aber dass die beiden aus so einer wohlhabenden und einflussreichen Familie kommen, passt gut zu Lillys vornehmer Art. Es ist ein kleines Wunder, dass nichts davon auf Akira abgefärbt zu haben scheint."


"Sie sind so verschieden wie Geschwister nur sein können. Die einzige Gemeinsamkeit scheint ihr Selbstvertrauen zu sein. Das ist zwar bewundernswert, kann aber auch ziemlich anstrengend sein."


stop music fadeout 2.0

scene bg school_dormlilly onlayer master
show lilly basic_smileclosed_paj onlayer master:
    twoleft
    ypos 1.17
show akira basic_smile onlayer master:
    tworight
    ypos 1.14
with shorttimeskip

"Der Abend nimmt seinen Lauf. Irgendwann verlässt uns Hanako und geht zum Schlafen in ihr Zimmer."


"Eine Weile hört man nur ab und zu das leise Klirren von Lillys Teeservice, während sie langsam trinkt."
"Die Stille ist sehr angespannt, während Lilly und ich darauf warten, dass Akira das Thema anspricht, das ihr schon die ganze Zeit auf dem Herzen liegen muss."


show akira basic_boo onlayer master
with charachange

aki "Also…"


$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_dreamy fadein 4.0

show lilly basic_weaksmile_paj onlayer master
with charachange

"Lilly stellt pflichtbewusst ihre Tasse ab und richtet ihre ungeteilte Aufmerksamkeit auf Akira."


"So wie Lilly und ich an der einen Seite des flachen Tisches sitzen und Akira auf der anderen, komme ich mir beinahe so vor, als würde ein Richter ein Urteil über uns sprechen."


show akira basic_smile onlayer master
with charachange

aki "Ich habe gehört, ihr Zwei seid nun zusammen?"


"Ich schaue seitwärts zu Lilly, um zu erfahren, ob Akira das von ihr erfahren hat. Sie nickt Akira leicht zu, und ich tue es ihr gleich."


"Da es die passende Gelegenheit zu sein scheint und Akira noch am ehesten eine Elternfigur für Lilly ist, verbeuge ich mich – die Hände vor mir auf dem Boden und den Kopf fast genauso tief."


hi "Ich werde mich gut um deine Schwester kümmern, Akira. Das verspreche ich dir."


show lilly basic_smile_paj onlayer master
with charachange

li "Siehst du? Er ist ein reizender junger Gentleman."


"Sie muss bemerkt haben, dass der Ursprung meiner Stimme niedriger ist als sonst."


"Ich richte mich langsam wieder auf, und meine Augen suchen zögernd nach Akira."


"Um die Wahrheit zu sagen, bezweifle ich, dass meine Richterin irgendwelche Einwände haben wird. Sie ist definitiv der Typ, der kein Geheimnis daraus machen würde, wenn er mit jemandem ein Problem hat, und das ist etwas, was ich sehr respektiere."


show akira basic_laugh onlayer master
with charachange

aki "Der altmodische Typ, was? Na ja, ich hab mir schon immer gedacht, dass du auf solche Typen stehst."


show akira basic_smile onlayer master
with charachange

aki "Ich habe kein Problem damit, und ich wünsche euch Zweien alles Gute. Auch wenn ich was dagegen hätte, könnte ich nicht wirklich viel machen."


"Ich nicke ihr dankbar zu, und Lilly seufzt erleichtert – wahrscheinlich eher aus Prinzip als dass sie wirklich befürchtet hätte, Akira könnte Probleme mit unserer Beziehung haben."


show akira basic_evil onlayer master
with charachange

aki "Aber… ich frage mich, wie der Rest der Familie es aufnehmen wird – besonders der Teil hier an der Schule. Hast du es ihr gesagt?"


show lilly basic_listen_paj onlayer master
with charachange

"Lillys Lächeln wird zur Grimasse, als Akira sie fast schon bösartig angrinst. Wer dir am nächsten steht, weiß, wie er am besten Salz in die Wunde streuen kann."


show lilly basic_weaksmile_paj onlayer master
with charachange

li "Man könnte sagen, sie hat es „zur Kenntnis genommen”, oder was meinst du, Hisao?"


hi "Ja, das könnte man sagen. Zumindest ist sie vernünftig."


show akira basic_boo onlayer master
with charachange

aki "Gut zu hören. Dieses Mädchen kann ganz schön anstrengend sein."


show akira basic_smile onlayer master
with charachange

aki "Wir haben uns ein paar Mails geschrieben, nachdem ich aus Schottland zurück war, und sie hat mich direkt zur Schnecke gemacht, weil ich mich erst mal mit meinem Freund getroffen habe, nachdem ich Hideaki so lange allein gelassen hatte."
aki "Sie mag den kleinen Kerl wirklich gern."


"Ich erinnere mich an Shizunes seltsame Reaktion, als ich ihr von unserer Beziehung erzählt habe, aber ich erwähne es nicht. Es lag wahrscheinlich nur an ihrer gegenseitigen Antipathie. Akiras Kommentar bestätigt das nur noch."


show akira basic_boo onlayer master
with charachange

aki "Na dann ist das ja geklärt. Muss morgen früh zur Arbeit, also verzieh ich mich dann besser mal."


show akira basic_smile onlayer master at tworight
with charamove

"Sie erhebt sich mit einem Grunzen vom Tisch, wobei sie sich mit ihrer Hand auf dem Knie abstützt. Ich bemerke, wie Akiras Augen ein paar Sekunden lang auf Lilly verweilen, bevor sie sich umdreht und verabschiedet."


hide akira onlayer master
with charaexit

"Auf dem Weg zur Tür bleibt sie stehen und blickt gedankenverloren auf, bevor sie sich noch einmal umdreht."



show akira invis onlayer master:
    xanchor 0.5 xpos 1.0
with None

show akira basic_lost onlayer master:
    xpos 0.9
with dissolvecharamove

aki "Ach ja, fast hätte ich's vergessen."


show akira basic_ending onlayer master
with charachange

aki "Immer schön verhüten!"


"Ich verschlucke mich an dem Tee in meinem Mund. Im Gegensatz zu mir lässt Lilly sich nichts anmerken. Beeindruckend."


show lilly basic_smile_paj onlayer master
with charachange

li "Keine Sorge, wir denken daran."


show akira basic_smile onlayer master
with charachange

aki "Braves Mädchen. Tschö!"


show akira invis onlayer master:
    xanchor 0.5 xpos 1.0
with dissolvecharamove

hide akira onlayer master
with None

"Und damit dreht sie sich um und marschiert mit einer Hand winkend durch die Tür, verschwindet im dunklen Flur und schließt die Tür hinter sich."


show lilly basic_smile_paj onlayer master:
    center
    ypos 1.17
show bg school_dormlilly onlayer master at bgright
with charamove

"Akira ist wirklich anstrengend. Total erschöpft lasse ich mich vorwärts auf den Tisch plumpsen. Ich bewundere, wie Lilly diesem anzugtragenden Teufel standhalten kann."


hi "Sie ist wirklich unglaublich direkt. Ich denke nicht, dass ich je mit der Energie deiner Schwester mithalten kann."


show lilly basic_smileclosed_paj_close onlayer master:
    center
    ypos 1.1
with characlose

"Als ich dann spüre, wie Lillys weiche Hand sich auf meine legt, rolle ich meinen Kopf zur Seite, um sie sanft lächeln zu sehen. Für eine lange Zeit sitzen wird einfach still nebeneinander."


"In Anbetracht ihrer unüblichen Körpergröße ist sie in etwa so groß wie ich – wenn nicht vielleicht sogar ein paar Zentimeter größer. Aus dieser Perspektive wirkt sie sogar noch größer."


"Das Gefühl ihrer blassen, weichen Hand auf meiner ist angenehm – genauso wie der Anblick dieses dünnen, seidenen Pyjamas, der ihre Kurven und Schlüsselbeine betont."


show lilly basic_smile_paj_close onlayer master
with charachange

li "Dafür, dass du das sagst, schlägst du dich aber recht gut."


hi "Schätze schon. Weißt du, ihr Zwei seid euch viel ähnlicher, als ich es bei unserer ersten Begegnung noch gedacht hatte."


show lilly basic_cheerful_paj_close onlayer master
with charachange

li "Dann ist es doch gut, dass ich dich davon abgehalten habe, dich an sie ranzumachen, nicht wahr?"


"Auch wenn sie Scherze darüber macht, die Einschätzung meiner Unfähigkeit, mit Akira mitzuhalten – körperlich oder mental – war ziemlich ernst gemeint."


"Lillys gelassene und damenhafte, fast mütterliche Natur, ist vielleicht das, was mir in meinen ersten Wochen an der Yamaku am meisten geholfen hat."


"Da fällt mir ein…"


hi "Warte… seit wann verhüten wir?"


show lilly basic_pout_paj_close onlayer master
with charachange

"Als ich einen neugierigen Blick zu meiner Seite werfe, sehe ich, wie Lilly ihre Wangen aufpustet und mich beleidigt anschaut."


li "Anders als du habe ich daran gedacht. Das Päckchen liegt in der Schublade neben der Spüle."


"Also… bin ich nicht der Einzige von uns, der Pillen nimmt. Im Nachhinein fühle mich recht rücksichtslos, dass ich gar nicht daran gedacht und alles Lilly überlassen habe."


"Als ich zur besagten Schublade hinübersehe, bemerke ich erneut die kniehohen Bücherstapel um uns herum, die auch schon bei meinem letzten Besuch da waren."
"Größtenteils sind sie an der Wand gestapelt, um für etwas mehr Platz am Tisch zu sorgen."


hi "Warum beschaffst du dir nicht ein Bücherregal für deine Bücher? Dass sie einfach gestapelt herumliegen, sieht seltsam aus – besonders weil der Rest deines Zimmers so sauber und ordentlich ist."


show lilly basic_smileclosed_paj_close onlayer master
with charachange

li "So sind sie leichter zu finden; ich weiß genau, in welchem Stapel welches Buch liegt."


hi "Würdest du das nicht auch wissen, nachdem du jeden Stapel in ein anderes Regal gestellt hast?"


show lilly basic_weaksmile_paj_close onlayer master
with charachange

li "Das mag sein, aber…"


"Am Ende ist sie also auch nicht gegen Faulheitsanfälle gefeilt."


hi "Du hast so viele. Es ist schade, dass wir sie nicht teilen können, obwohl wir beide so viel lesen."


show lilly basic_giggle_paj_close onlayer master
with charachange

"Sie kichert kurz."


hi "Da fällt mir ein – warum bestellst du deine Bücher über Yuuko? Ich kann mir vorstellen, dass es zahlreiche Seiten gibt, bei denen man Braille-Bücher bestellen kann. Besonders englisches Braille. Es gibt auch viele Vorleseprogramme."


show lilly basic_displeased_paj_close onlayer master
with charachange

"Sie wendet ihr Gesicht leicht von mir ab, was mich irgendwie überrascht."


li "Ich bin einfach… nicht so gut mit Computern. Ich komme mit Schreibmaschinen und Brailleschreibmaschinen zurecht… aber das war es auch schon."


"Ihr Ton bringt mich fast zum Schmunzeln. Sie ist ein stolzes Mädchen, darum muss es schwierig für sie sein, so etwas zuzugeben."


"Also gehört Lilly eher zu den unmodernen Menschen. Bei ihrer altmodischen Persönlichkeit ist das auch nicht gerade eine Riesenüberraschung."


hi "Ich würde mir keine Sorgen darum machen. Viele Leute können damit nicht richtig umgehen, also ist es nicht allzu ungewöhnlich."


show lilly basic_concerned_paj_close onlayer master
with charachange

li "„Allzu” ungewöhnlich…"


"Jetzt ist sie sogar noch deprimierter. Es fühlt sich an, als würde ich das Messer drehen, anstatt ihre Wunden zu heilen."


show lilly basic_weaksmile_paj_close onlayer master
with charachange

"Etwas unbeholfen rutsche ich näher an sie heran und lege vorsichtig eine Hand um ihre Hüfte, um sie zu umarmen. Ich habe mich noch immer nicht wirklich an diese Art der körperlichen Zuneigung gewöhnt, aber Lilly scheint es zu mögen."


scene ev lilly_kissing onlayer master
with whiteout

"Als sie sich zu mir wendet, lächelt sie und küsst mich zur Belohnung. Sie zieht mich näher an sich heran und streift meine Unterlippe mit ihrer, bevor sie sie wieder für einen Kuss vereinigt."


"Auf diese Weise sind all meine Sinne von ihr erfüllt."
"Der kaum wahrnehmbare Duft ihre Haares, der Geschmack ihrer Zunge, als sie meine flüchtig berührt, die Zartheit ihrer Lippen, das Bild von ihr, das meinen Verstand ausfüllt, die vollkommene Stille abgesehen von ihrem Atem…"


"Wir mögen uns zuvor schon geküsst haben, doch selbst wenn dies bloß ein schlichter Kuss der Zuneigung ist, ist es trotzdem eine neue und angenehme Erfahrung."


scene bg school_dormlilly onlayer master at bgright
show lilly basic_cheerfulblush_paj_close onlayer master:
    center
    ypos 1.1
with locationchange

"Ihrem knallroten Gesicht nach zu urteilen, nachdem sie sich von mir gelöst hat, ist es offensichtlich, dass sie das Gleiche empfindet. Auch wenn wir vollkommen ungestört sind, ist es mir immer noch etwas peinlich, sich dem anderen so sehr zu öffnen."


show lilly basic_smileclosed_paj_close onlayer master
with charachange

li "Ich denke, es wäre das Beste, wenn wir alles Tag für Tag angehen. Kleine Schritte, richtig?"


hi "Ja. Nur kleine Schritte."


"Wir haben noch reichlich Zeit, um zusammen zu sein – selbst wenn das Schuljahr vorbei ist. Ich denke, solange wir zusammenbleiben, wird alles gut gehen; schließlich wird keiner von uns allzu bald irgendwo hingehen."


"Im Augenblick bin ich einfach nur dankbar für diesen kurzen Moment, den wir zusammen verbringen können."


stop music fadeout 2.0

scene black onlayer master
with dissolve




label de_L23:

scene bg school_nursehall onlayer master
with locationchange

"Es müssen schon mindestens ein Dutzend Minuten vergangen sein, seit ich regungslos vor der Tür von Docs Büro stehe."


"Nicht, dass ich diesen kleinen, beigen Raum zuvor noch nie betreten oder dass ich kindische Angst vor Arztbesuchen hätte."


"Vielleicht liegt es daran, dass das Krankenzimmer einem Beichtstuhl gleicht – ein Zugeständnis, dass mein Körper fehlerhaft ist. Das Wissen, dass das zwischen mir und Doc absolut vertraulich ist, lindert dieses Gefühl kaum."


"Als ich mich dann daran erinnere, dass bald die Glocke zur Mittagspause läuten wird, seufze ich und öffne die Tür. Zumindest wird es nicht lange dauern."


play music music_nurse fadein 0.5

scene bg school_nurseoffice onlayer master
show nurse neutral onlayer master at center
with locationchange

nk "Na sieh an, wenn das nicht Nakai ist. Schön, dich zu sehen."


show nurse grin onlayer master
with charachange

nk "Oder vielleicht auch schlecht – kommt drauf an, warum du hier bist."


"Amüsiert über seinem eigenen Witz lacht er kurz. Ich finde diesen Humor flach und irgendwie unpassend, aber dass er solch eine Situation so locker nehmen kann, ist vielleicht ganz beruhigend – oder zumindest ablenkend."


show nurse neutral onlayer master
with charachange

"Nachdem seine kurze Unterhaltungseinlage vorüber ist, klatscht er die Hände zusammen und wendet sich den wichtigen Dingen zu. Er bietet mir einen Stuhl an, auf den ich mich dann auch setze."


"Ich wünschte, die Klassenzimmer hätten so gemütliche Stühle."
"Als ich kurz meinen Blick durch den Raum schweifen lasse, merke ich, wie mein Geist – abgelenkt von all den kleinen Veränderungen seit meinem letzten Besuch – langsam woandershin wandert."


show nurse fabulous onlayer master
with charachange

nk "Also dann, was führt dich her? Ich hab dich kaum gesehen, daher denke ich, dass es um deine Gesundheit bisher ganz gut steht?"


hi "Na ja, größtenteils."


show nurse neutral onlayer master
with charachange

nk "Verstehe."


"Sein Lächeln verfliegt, als ich nicht weiterrede."
"Ich fühle mich deswegen etwas schuldig. Es sind diese Momente, in denen mir bewusst wird, dass ich nicht wirklich „normal” bin, wegen derer ich Doc so ungern besuche. Es ist, als würde ich zugeben, dass ich anders bin."


stop music fadeout 5.0

hi "Als ich über das lange Wochenende auf einem Ausflug war, hatte ich ein paar Problem mit meinem Herzen."


"Er brummt ernst und nickt. Ich soll wohl fortfahren."


hi "Ich glaube, es war… Genau, es war, als ich eine ziemlich weite Strecke gelaufen bin. Ich denke, der richtige Fachbegriff dafür ist Herzflimmern."


hi "Plötzlich waren meine Knie schwach, und es fühlte sich fast an, als hätte ich eine kleine Herzattacke, aber nach ungefähr einer halben Minute war es vorüber. Aber auch danach fühlte ich mich noch ziemlich ausgelaugt und unwohl."


show nurse concern onlayer master
with charachange

nk "Mhm. Nicht gut. Überhaupt nicht gut."


nk "Wie viele Tage ist das genau her? Hast du irgendetwas unübliches getan, außer dich vor dem Anfall zu überanstrengen? Hast du ordnungsgemäß deine Medikamente genommen?"


"Doc verwandelt sich vom peinlichen Scherzbold in einen ernsten Gesundheitsprofessor, der Fragen herunterrattert, sich Notizen macht und Akten auf seinem Computer aufruft."


"Ich erzähle ihm von den Pillen, die ich an jenem Morgen vergessen hatte, und von dem vorangegangen Abend. Das zu tun war dumm, aber jetzt kann ich auch nichts mehr daran ändern, außer ehrlich zu antworten und in den sauren Apfel zu beißen."


"Seine Ernsthaftigkeit wird zu einem Stirnrunzeln und die Unterhaltung wird zu einer sofortigen Untersuchung."


hide nurse onlayer master
with shorttimeskip

"Nachdem ich mein Hemd fertig zugeknöpft habe, weist mich Doc erneut mit einer Geste an, mich vor ihn zu setzen."


show nurse concern onlayer master at center
with charaenter

nk "War es das erste Herzproblem, das du seit deiner Ankunft an der Yamaku hattest?"


hi "Ich hatte vorher schon ein paar Mal kurz Schmerzen in der Brust, aber die waren kein Vergleich zu dem Anfall vom Wochenende."


"Er lehnt sich in seinem Stuhl zurück und ähnelt kurz einem Poirot im weißen Mantel, während er über dem mysteriösen Fall des Herzflatterns brütet."


"Als er gedankenversunken seine Lippen hin und her bewegt und damit seinen nicht vorhandenen Schnurrbart zum Tanzen bringt, kommt er schließlich zu einem Ergebnis."


show nurse fabulous onlayer master
with charachange

play music music_nurse fadein 1.0

nk "Na ja, du hast's überlebt. Das ist immer 'was Gutes."


"Ich schaue überrascht zu ihm auf und bemerke, dass er sein „Erwischt!”-Gesicht aufgesetzt hat."


"Eigentlich ist es irgendwie beruhigend. Ich denke nicht, dass er Witze reißen würde, wenn es wirklich etwas Ernstes wäre. Darum bleibe ich still und akzeptiere meine verdiente Strafe."


show nurse neutral onlayer master
with charachange

nk "Ich werde mit deinem Arzt reden müssen, aber ihm Moment vermute ich, dass es schlicht und einfach an der körperlichen Überanstrengung lag."


nk "Hast du das regelmäßige leichte Fitnesstraining beibehalten, wie es angeordnet hatte?"


hi "Ich sehe zu, dass ich jeden Tag eine angemessene Strecke laufe. Meistens reicht es, um etwas ins Schwitzen zu kommen. Andererseits bin ich nicht so fit wie früher."


nk "Dann sollte es ausreichen. Hauptsache du vergisst nicht, dich regelmäßig körperlich leicht zu ertüchtigen – keine Kraftakte oder Sprints oder dergleichen."


hi "Verstanden. Seit ich das Krankenhaus verlassen habe, habe ich mich viel mehr aufs Lernen konzentriert – teilweise um mich davon abzulenken, dass ich körperlich nicht mehr so einsatzfähig bin."


show nurse grin onlayer master
with charachange

nk "Gut zu hören, dass du die Lage meisterst. Eine plötzliche Umstellung des Lebensstils ist fast immer schwierig, darum freut es mich, dass du anscheinend alles geregelt kriegst. Zumindest fast alles."


show nurse neutral onlayer master
with charachange

nk "Nichtsdestotrotz will ich eine Weile ein Auge auf dich werfen, nur zur Beobachtung. Nur zum sicherzustellen, dass es nicht bergab geht, wenn du verstehst."


"Das ist etwas, das ich nicht wirklich hören wollte. Seit ich an die Yamaku gekommen bin, wollte ich einfach nur ein so normales Leben wie möglich leben."


"„Beobachtung” war eines der Worte, die ich während meines Krankenhausaufenthaltes zu hassen gelernt habe."
"Für lange Zeit kam es mir vor, als hätte ich einfach geradewegs aus dem Krankenhaus hinausspazieren können, wenn nicht diese „Beobachtung” gewesen wäre, die die Ärzte so innig wollten."


hi "Sicher. Soll ich öfter vorbeikommen?"


"Er überprüft den Kalender neben seinem Computer, was ihm anscheinend ein heftiges Stirnrunzeln beschert. Danach dreht er sich wieder zu mir."


show nurse concern onlayer master
with charachange

nk "In Anbetracht des Timings sind die Sommerferien etwas lästig…"


nk "Ich werde mich mit deinem Arzt absprechen und versuchen, die Situation besser in den Griff zu bekommen. Ich muss sehen, wie er das angehen will, aber ich denke, du solltest die Dinge fürs Erste ruhig und vorsichtig angehen."


nk "Was du beschrieben hast, klang nicht wirklich nach einem wiederkehrenden Vorfall, aber es wird nicht schaden, eine Weile auf die Bremse zu treten – nur um sicher zu sein."


hi "Was soll ich dann den Rest des Tages tun?"


"Er sieht über meine Schulter hinweg auf die Uhr, die über der Tür hängt. Ich hätte sie nie bemerkt, wenn ich nicht seinem Blick gefolgt wäre."


show nurse fabulous onlayer master
with charachange

nk "Die Schule ist fast vorbei, also kannst du auch genauso gut früher Schluss machen."


"Er blinzelt mir durchtrieben zu, damit ich auch wirklich begreife, dass er mir hier einen Gefallen tut."


hi "Na ja, ärztliche Anweisung. Danke."


show nurse grin onlayer master
with charachange

nk "Dafür bin ich schließlich da."


show nurse neutral onlayer master
with charachange

nk "Ich weiß, dass es dir vielleicht nicht gefällt, aber du kannst deinen Zustand nicht ignorieren. Zöger nicht, mich zu besuchen, falls du weitere Probleme bekommen solltest oder wenn du einfach nur etwas fragen möchtest. Bis dann."


hide nurse onlayer master
with charaexit

"Er dreht sich um und wendet sich wieder dem Computer vor ihm zu, auf dem er dann auch eifrig zu tippen beginnt. Ich schätze, ich lese einfach etwas, bevor ich am Tor auf Lilly warte. Immerhin habe ich nichts anderes zu tun."


stop music fadeout 3.0

"Sogar als ich gehe, hallen seine Worte in meinem Kopf wider. Mein Zustand ist nicht so einschränkend wie der vieler anderer hier auf der Yamaku, und ich will auch nicht, dass Lilly sich deswegen so viele Gedanken macht."


"Wenn ich mein Leben einfach normal leben und kurze, heftige Schläge vermeide, sollte es gut gehen. Ich werde nicht zulassen, dass mein Zustand mich beherrscht."


scene bg school_gate_ss onlayer master
show lilly cane_smileclosed_ss onlayer master at center
with shorttimeskip

play music music_tranquil fadein 3.0

play sound sfx_normalbell

"Lilly kommt in Sichtweite, nachdem die Glocken das Ende des Schultages verkündet haben. Sie verabschiedet sich von einigen Klassenkameraden, die in die andere Richtung gehen, bevor sie ihren wöchentlichen Weg zum Mini-Markt antritt."


hi "N'Abend, Lilly."


show lilly cane_smile_ss onlayer master
with charachange

"Das sofortige warme Lächeln und entspannte Auftreten nachdem sie mich gehört hat, sind eine unerwartet willkommene Begrüßung."


li "Hallo, Hisao. Dir auch einen guten Abend."


show lilly cane_smileclosed_close_ss onlayer master
with characlose

"Sie zögert für eine Sekunde, doch dann hebt sie schließlich ihr Kinn etwas an und schließt ihre Augen. Mit einer leichten Beklommenheit berühren meine Lippen ihre, ehe wir beide uns auf den Weg machen – Hand in Hand."


"Die Tatsache, dass wir beide fast gleichgroß sind, ist ab und zu ganz praktisch. Keiner von uns braucht seinen Kopf zu neigen, um den anderen zu erreichen."


scene bg school_road_ss onlayer master
with locationchange

"Es dauert nicht lange, bis wir den Lärm der anderen Schüler weit hinter uns gelassen haben und Lillys klackernder Blindenstock in ihrer freien Hand das einzig hörbare Geräusch ist."


"Stille – wohltuende Stille – ist alles, was uns begrüßt, als wir langsam im Licht der untergehenden Sonne gehen."


hi "Ich glaube, mir gefällt dieses Dorf langsam wirklich. Diese riesige grüne, hügelige Weite; überall Bäume; diese etwas rustikalen kleinen Häuser…"


show lilly cane_smile_close_ss onlayer master at center
with charaenter

li "Also gefällt dir mittlerweile auch die Ruhe hier?"


hi "Ich denke schon. Ich komme aus einer Großstadt in der Nähe von Tokyo, daher war die Ruhe dieses Dorfes bei meiner Ankunft wirklich sehr ungewohnt für mich."


hi "Nach einer Weile wurde es allerdings wirklich angenehm. Ich glaube, ich ziehe es nun der Hektik meiner Heimatstadt vor."


show lilly cane_smileclosed_close_ss onlayer master
with charachange

li "Mir gefiel die Ruhe eines so ländlichen Dorfes zwar schon, bevor ich hier ankam, aber ich schätze, dass ich den Vorteil hatte, in einer ruhigen Gegend aufzuwachsen."


show lilly cane_weaksmile_close_ss onlayer master
with charachange

li "Hanako sagte auch, dass sie die Umgebung sehr schön findet."


"Lilly mag solche Dinge leicht aussprechen, aber jedes Mal, wenn sie erzählt, wie andere die Sehenswürdigkeiten um sie herum als schön oder hübsch beschreiben, bringt mich das ins Grübeln."


"Ich bemerke, wie ihr Blick immer erwartungsvoller wird. Vielleicht wartet sie auf eine Frage. Sie hatte immer schon ein gutes Gespür dafür, wann jemand nicht sagt, was ihm auf dem Herzen liegt. Darum kann ich es genauso gut aussprechen."


hi "Ich hab mich irgendwie gefragt… Äh, wie soll ich sagen."


hi "Bedauerst du es je… dass du nicht selbst sehen kannst, wie alles aussieht? Das ist mir nur so durch den Kopf gegangen."


show lilly cane_listen_close_ss onlayer master
with charachange

"Sie denkt eine Zeit lang sorgfältig darüber nach."


show lilly cane_smileclosed_close_ss onlayer master
with charachange

li "Bedauerst du es je, dass du die Leute auf der anderen Seite eines Raumes nicht Flüstern hören kannst?"


show lilly cane_smile_close_ss onlayer master
with charachange

li "Ich kann zwar nur für mich selbst sprechen, aber ich habe mein gesamtes Leben ohne Augenlicht verbracht. Genau wie ich etwas nicht kann, was du kannst, kannst du etwas nicht, was ich kann."


show lilly cane_weaksmile_close_ss onlayer master
with charachange

li "Die Tatsache, dass die Welt für Sehende gemacht ist, kann manchmal ärgerlich sein, aber es gibt viele, viele Menschen, die wegen dieser Welt noch viel mehr leiden als ich."


hi "Das ergibt Sinn, aber trotzdem – es fühlt sich irgendwie mies an, dir etwas zu beschreiben, das du nicht selbst erfahren kannst."


show lilly cane_surprised_close_ss onlayer master
with charachange

"Sie neigt fragend ihren Kopf, als würde das, was ich gerade gesagt habe, kaum Sinn ergeben."


li "Aber ich kann es doch erfahren."


show lilly cane_smile_close_ss onlayer master
with charachange

li "Du hast selbst gesagt, dass du diese Gegend wegen ihrer Umgebung magst. Ich mag sie aus genau dem gleichen Grund."


show lilly cane_smileclosed_close_ss onlayer master
with charachange

li "Dank der Tatsache, dass dieses kleine, ländliche Dorf von Wäldern umgeben ist, bietet es fern vom Lärm der Schule und der Hektik – ganz zu schweigen von den Gerüchen – der Stadt etwas Frieden und Stille."


"Ich schätze, es wäre auch so ähnlich wie dort, wo sie mit Akira zusammen gewohnt hat."


"Ihre Perspektive ist ziemlich vernünftig, und ich bin nicht überrascht, dass sie ihr Leiden viel besser im Griff hat als ich meins."


"Da sie aus einer Gegend kommt, die ähnlich ruhig ist wie die Umgebung der Yamaku, konnte sie sich hier schneller einleben. Genauso hat die Tatsache, dass sie schon blind geboren wurde, ihre Einstellung dazu beeinflusst – wie sie selbst zugibt."


"Ich sollte aufhören, von mir selbst so genervt zu sein, doch ich werde dieses Gefühl einfach nicht los, dass ich mich in Anbetracht der Umstände, mit denen die Meisten auf der Yamaku zu kämpfen hatten, viel zu sehr auf Lilly verlassen habe."


hi "Das ergibt wirklich Sinn. Du bist wie immer ziemlich gut im Erklären."


hi "Da fällt mir ein – wo ist eigentlich Hanako? Beim Mittagessen war sie noch bei uns."


show lilly cane_weaksmile_close_ss onlayer master
with charachange

li "Sie scheint mit Lernen beschäftigt zu sein. Die Prüfungen sind noch lange nicht vorbei, und sie meinte, dass sie dieses Jahr besser abschneiden will als letztes."


hi "Auch wenn ich ihre Arbeitsmoral bewundere – sie lässt uns neuerdings viel Zeit zu zweit."


show lilly cane_reminisce_close_ss onlayer master
with charachange

li "Sie ist diese Art von Mensch, denke ich. Die Art, die andere wann immer möglich über sich selbst stellt. Sie ist ein süßes Mädchen, obwohl sie in der Vergangenheit so verletzt wurde."


show lilly cane_weaksmile_close_ss onlayer master
with charachange

li "Ich weiß nicht… Es kommt mir so vor, als würde sie sich erst jetzt, wo sie mir so fern wie noch nie ist, wirklich selbst finden."


show lilly cane_smile_close_ss onlayer master
with charachange

li "Schließlich ist es dir und nicht mir zu verdanken, dass sie angefangen hat, mehr Selbstbewusstsein zu bekommen."


"Ich ziehe meine Hand von ihrer zurück und lege sie sanft auf ihren Kopf."


hi "Das Wichtigste ist, dass du für sie da warst. Ich kann mir nicht einmal ausmalen, wie sie wäre, wenn sie dich nicht gehabt hätte. So viel ist mir klar geworden, als du in Schottland warst."


hi "Wir sind alle immer noch Freunde, also müssen wir nur auf sie vertrauen. Ich denke, sie wird ein guter Mensch – und das, weil du für sie da warst, als sie es am meisten gebraucht hat… genauso wie du für mich da warst."


show lilly cane_weaksmile_close_ss onlayer master
with charachange

li "Ich komme mir ein bisschen kindisch vor, wenn du so weise klingst."


hi "Na ja, ich geb mein Bestes."


hi "Hast du am Wochenende vielleicht schon etwas vor?"


show lilly cane_surprised_close_ss onlayer master
with charachange

li "Ich glaube nicht. Wieso?"


hi "Wie wäre es dann mit einem Date am Sonntag? Es wäre eine Abwechslung von den Prüfungsvorbereitungen."


show lilly cane_smileclosed_close_ss onlayer master
with charachange

"Sie beruhigt mein schnell schlagendes Herz, indem sie einfach lächelt und nickt."


li "Das wäre entzückend."


hi "Wo würdest du gerne hingehen?"


show lilly cane_displeased_close_ss onlayer master
with charachange

"Auf ihrem Gesicht macht sich Missbilligung breit."


li "Das darfst du nicht, Hisao. Das ist geschummelt."


hi "Was meinst du?"


li "Ein Gentleman sollte nie eine Lady fragen, wohin er sie ausführen soll."


hi "Ah… Oh."


show lilly cane_smile_close_ss onlayer master
with charachange

"Ihr rasch zurückkehrendes Lächeln versichert mir, dass das nicht so ernst gemeint war."


show lilly cane_smileclosed_close_ss onlayer master
with charachange

li "Mach dir darüber keine Sorgen. Ich werde mir etwas einfallen lassen."


hi "Dann überlasse ich es dir. Allerdings verspreche ich, dass ich beim nächsten Date entscheide."


stop music fadeout 4.0

"Da unsere Pläne für das Wochenende nun gemacht sind, laufen wir schweigend den Rest des Hügels hinab."


"Mir wird klar, dass dieses Schweigen nicht von langer Dauer sein wird, als ich eine vertraute Gestalt erblicke, die mit erhobener Hand auf uns wartet."


show lilly cane_smileclosed_close_ss onlayer master at twoleft
show bg school_road_ss onlayer master at bgleft
with charamove

show akira basic_smile_ss onlayer master at tworight
with charaenter

aki "Yo."


scene bg suburb_konbiniint onlayer master
with shorttimeskip

play music music_daily fadein 0.5

"Verkäuferin" "Danke, und beehren Sie uns bald wieder!"


scene bg suburb_konbiniext_ss onlayer master
with locationchange

"Der Temperaturwechsel, als ich die Türschwelle des Mini-Markts überschreite, jagt mir einen Schauer über den Rücken. Es fühlt sich an, als würde der Sommer langsam nachlassen."


show lilly cane_weaksmile_ss onlayer master at center
with charaenter

"Als ich zu meiner Seite schaue, scheint es Lilly genauso zu gehen, aber im Gegensatz zu mir kann sie es nicht verstecken. Am Anfang hatte ich nicht bemerkt, wie empfindlich sie körperlich ist – sogar verglichen mit Hanako."


"Wenn ich sie beschreiben müsste, würde ich sagen, dass sie mich an eine Porzellanpuppe erinnert."


show akira basic_ending_ss behind lilly at center onlayer master
with charaenter

show lilly cane_surprised_ss onlayer master
with vpunch

show lilly cane_reminisce_ss onlayer master at twoleft
show akira basic_ending_ss onlayer master at tworight
show bg suburb_konbiniext_ss onlayer master at bgleft
with dissolvecharamove

"Akira taucht hinter ihr auf und klopft ihr zweimal grob auf die Schulter, was Lilly ziemlich verwirrt. Für einen Augenblick sieht sie aus, als wäre sie auf meinen Status als Einzelkind genauso neidisch wie ich auf ihre enge Beziehung."


show lilly cane_listen_ss onlayer master
show akira basic_boo_ss onlayer master
with charachange

"Während ich mich mit meinen Tüten arrangiere, reden sie für einige Augenblicke unter sich. Ihre Stimmen sind zu leise, als dass ich sie hören könnte, doch schließlich beenden sie ihr Gespräch, und wir machen uns auf den Rückweg zur Schule."


scene bg school_road_ss onlayer master
show akira basic_smile_ss onlayer master at tworight
with locationskip

aki "Ah, es fühlt sich gut an, mal aus diesem verdammten Büro rauszukommen. Ihr Kids wisst nicht, wie gut ihr es hier habt."


show lilly cane_displeased_ss onlayer master at twoleft
with charaenter

li "Kids…"


show akira basic_laugh_ss onlayer master
with charachange

aki "Tz. Dann halt „ihr Zwei”. Kinder werden heutzutage zu schnell groß."


show lilly cane_pout_ss onlayer master
with charachange

li "Du bist nicht alt genug, um das zu sagen."


show akira basic_lost_ss onlayer master
with charachange

aki "Ich weiß nicht. In Hidaekis Nähe zu sein, sorgt dafür, dass ich mich verdammt alt fühle; er ist so vorlaut, dass er mich an dich erinnert, als du noch jünger warst."


show lilly cane_weaksmile_ss onlayer master
with charachange

li "Er ist ein netter Junge. Es wäre eine Schande, wenn Shizune zu viel Einfluss auf ihn bekommt."


show akira basic_laugh_ss onlayer master
with charachange

"Akira schnauft amüsiert wegen der Antipathie ihrer Schwester. Sie scheint es nicht für würdig zu erachten, daraus ein großes Thema zu machen, und behandelt es eher wie eine Kinderzankerei."


show akira basic_smile_ss onlayer master
with charachange

"Sie schaut zu mir herüber, als würde sie sich gerade erst wieder daran erinnern, dass ich da bin. Dann grinst sie und greift in ihre Gesäßtasche."


hi "Was ist denn?"


show akira basic_ending_ss onlayer master
with charachange

aki "Nur 'ne Sekunde, lass es mich eben rausholen…"


"Nach einigen Schwierigkeiten schafft sie es, ihr schwarzes Lederportemonnaie aus ihrer Gesäßtasche zu holen, und nimmt zügig etwas heraus, das wie ein gefaltetes viereckiges Blatt Papier aussieht."


"Während Lilly sich des Ganzen nicht bewusst ist, entfaltet Akira den Fetzen und reicht ihn mir."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

show stallphoto_insert onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Ein altes Foto von… sieht aus wie jüngere Versionen von Lilly und Shizune, die einen Nudelstand betreiben. Im Hintergrund ist noch ein anderes Mädchen. Sie kommt mir irgendwie bekannt vor, aber ich komme nicht darauf woher."


show lilly cane_smile_ss onlayer master
with None

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show stallphoto_insert onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide stallphoto_insert onlayer master
with None

li "Was ist das, Akira?"


show akira basic_boo_ss onlayer master
with charachange

aki "Ich denke, das weißt du."


show lilly cane_listen_ss onlayer master
with charachange

"Lilly grübelt darüber einige Augenblicke, bis sie darauf kommt."


show lilly cane_surprised_ss onlayer master
with charachange

li "Akira… das war wirklich nicht…"


show akira basic_smile_ss onlayer master
with charachange

aki "Das geht schon in Ordnung, meinst du nicht? Außerdem ist es so ziemlich das einzige Foto, das ich von euch beiden aus eurer Yamakuzeit habe, auf dem ihr euch nicht an die Gurgel geht."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

show stallphoto_insert onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Ich sehe erneuert auf das Foto in meiner Hand hinab."


"Es wirkt seltsam, Lilly und Shizune so fleißig ohne jegliches Anzeichen von Feindseligkeit zusammen arbeiten zu sehen."
"Wenn das Foto während des Yamaku-Festivals geschossen wurde, bedeutet das, dass es vor ein oder zwei Jahren gemacht worden ist."


"Mit anderen Worten, in der Zeit, als beide noch zusammen im Schülerrat waren."


hi "Wer ist das Mädchen hinter ihnen? Sie kommt mir irgendwie bekannt vor."


aki "Hah, ich wusste, du würdest sie nicht erkennen. Das ist Misha bevor sie ihr Haar pink gefärbt hat."


hi "{b}Das{/b} ist Misha? Niemals…"


"Es fühlt sich extrem komisch an, Misha ohne ihren so unverwechselbaren Haarstil zu sehen. Akiras Ton nach zu urteilen, scheint sie Mishas Vorstellung von Mode nicht wohlwollend gegenüberzustehen."


"Ich schätze, diese Tatsache trägt nur zur Kuriosität der Situation auf dem Bild bei. Kaum zu glauben, dass sie früher so gut miteinander ausgekommen sind… Ich wünschte, ich könnte etwas tun, um ihre Freundschaft zu kitten."


li "Du bist so still, Hisao."


hi "Es kam mir nur etwas seltsam vor, euch alle so freundlich zusammen zu sehen."


"Lilly will etwas sagen, hält sich jedoch zurück. Letzten Endes geht mich das nichts an; es ist zwischen Shizune und Lilly – und niemand anderem."


li "Dinge ändern sich. Leider."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

stop music fadeout 6.0

show akira basic_resigned_ss onlayer master
show lilly cane_reminisce_ss onlayer master
with None

show stallphoto_insert onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide stallphoto_insert onlayer master
with None

"Ich reiche das Foto zurück zu Akira. Sie seufzt, als sie es zusammenfaltet und in ihr Portemonnaie schiebt. Ein kleine Erinnerung, still versteckt, um einige Zeit später wieder abgerufen zu werden."


aki "Ja, das tun sie."


"Ursprünglich dachte ich, dass Akiras Reaktion einfach eine Antwort auf die Situation zwischen Lilly und Shizune war, doch sie sieht entgegen meiner Erwartung seltsam bedrückt aus."


hi "Was ist los?"


show akira basic_boo_ss onlayer master
with charachange

aki "Ah, es ist nur, dass ich ziemlich bald nach Schottland fahren werde."


hi "Du reist schon wieder nach Schottland?"


show akira basic_lost_ss onlayer master
with charachange

"Für einen langen Moment sieht Akira überrascht aus. Ein Gesichtsausdruck, der ihr schlecht steht."


"Nach einem kurzen Blick zu Lilly wendet sie sich wieder mir zu, als hätte es ihn nie gegeben."


show akira basic_resigned_ss onlayer master
with charachange

aki "Ja. In ein paar Wochen mache ich mich auf nach Inverness, um im Unternehmenshauptquartier zu arbeiten. Ist ein ziemlich großer Sprung auf der Karriereleiter, und es ist eine Chance, die nicht so schnell wiederkommen wird."


"Also wird Akira Japan verlassen, und das wohl dauerhaft…"


"Ich werde das Gefühl nicht los, dass meine Hoffnung, unsere Tage glücklich vor uns hin zu leben und Spaß in dieser isolierten, kleinen Welt zu haben, sich langsam dem Ende nähert. Es ist beunruhigend."


"Leicht überrascht schaue ich zu Lilly. Sie hat mir nichts davon gesagt, obwohl sie sonst so mitteilsam ist."


"Sie läuft weiter, ihr Gesicht nach vorne gerichtet. Weder kann ich aus ihrem Gesichtsausdruck etwas ablesen noch kann ich erahnen, was ihr durch den Kopf geht. Das ist beunruhigend, wenn ich bedenke, wie leicht mir das normalerweise fällt."


"Es erinnert mich an die Zeit, als wir uns im Shanghai trafen – kurz vor dem, was man unser erstes Date nennen könnte. Zu jener Zeit war alles, was ich tun konnte, sie zu trösten, ohne die Ursache zu kennen. Und jetzt fühlt es sich genauso an."


scene bg school_dormext_full_ni onlayer master
show akira basic_resigned_ni onlayer master at tworight
show lilly cane_reminisce_ni onlayer master at twoleft
with shorttimeskip

"Als wir wieder einmal die Wohnheime der Schule erreichen, herrscht eine irgendwie peinlich Stille. Ich denke nicht, dass ich der Einzige bin, der das spürt."


hi "Ich seh dich dann morgen, Lilly. Bis dann, Akira."


show lilly cane_weaksmile_ni onlayer master
with charachange

li "Gute Nacht, Hisao."


show akira basic_smile_ni onlayer master
with charachange

aki "Ciao."


hide lilly onlayer master
hide akira onlayer master
with charaexit

"Daraufhin laufen sie zum Mädchenwohnheim."


"Als ich gerade die Tür zum Männerwohnheim öffnen will, halte ich inne und sehe noch einmal in ihre Richtung – wenige Augenblicke, bevor sie hinter der schweren, hölzernen Tür verschwinden."


"Das war… ein seltsamer Moment, als Akira sagte, sie würde abreisen. Obwohl das nicht das erste Mal war, dass meine Gedanken über mein neues Leben infrage gestellt wurden, ist das vielleicht das erste Mal, dass es so tiefgreifend war."


"Ich weiß immer noch nicht, was ich von Akiras Reaktion halten soll, und von Lillys noch weniger."


"Die Nachtkälte erinnert mich daran, dass ich zurück auf mein Zimmer sollte, bevor ich mir etwas einfange. Die Tüten, die meine Arme nach unten ziehen, scheinen ihr Gewicht verdoppelt zu haben."


"Nicht zuletzt habe ich mit ihr dieses Wochenende ein Date. Ich muss einfach aufhören, zu viel darüber nachzudenken, und die Dinge so nehmen, wie sie sind."


"Schließlich laufen die Prüfungen noch, und da das Trimester bald endet und die Sommerferien anfangen, wird es reichlich geben, um mich für eine Weile beschäftigt zu halten."


"Als ich gähnend eintrete, kreisen meine Gedanken um den Ort, den Lilly für unser Wochenend-Rendevouz aussuchen wird."


scene black onlayer master
with dissolve



label de_L24:

scene bg city_restaurant onlayer master at Fullpan(10.0)
with dissolve

play music music_jazz

"Ich habe zwar mit vielem gerechnet, als Lilly sagte, sie würde den Ort für unser Date aussuchen, aber ganz bestimmt nicht hiermit."


"Alle Männer und Frauen tragen nichts als ihre feinste Kleidung, genauso förmlich wie ihre Umgebung. Tiefrote Tapeten zierten die Wände, während die Straßenlichter weit unten flackern und glühen."


"In Kombination mit dem gedämpften Gemurmel leiser Gespräche und dem Klirren von Besteck und Weingläsern ist die Stimmung formal aber dennoch entspannt genug, dass ich mich nicht zu nervös fühle, obwohl das unser erstes Date ist."


"Nachdem wir zu unserem Tisch geführt wurden, verlässt uns unser Kellner nach einem wertschätzenden Nicken von Lilly mit einer kurzen Verbeugung, um andere zu bedienen."


"Auch ohne meine Hilfe hat es Lilly bisher geschafft, sich überraschend leicht umherzubewegen – trotz des unvertrauten Umfelds. Hier und da ein leichtes Streifen, und sie ist generell sehr geschickt darin, sich selbst nach Bedarf zu orientieren."


$ ksgallery_unlock("evul lilly_restaurant_listen")
scene ev lilly_restaurant_listen onlayer master at restaurant_out
with whiteout

"Meine Augen sehen in die von Lilly. Ich kann in ihrem Gesicht lesen, dass sie ihrer Umgebung genauso intensiv lauscht, wie ich sie beobachte."


"Aber ich muss zugeben – meine Augen bleiben jedes Mal an ihr hängen, wenn sie durch den Raum schweifen. Ihr rotes Cheongsam betont ihre Figur ausgesprochen gut und zeigt ihre Beine."
"Sogar ihr Haar ist hochgesteckt, und der Duft von Parfum ist gerade so wahrnehmbar."


"Auch wenn mein schwarzer Anzug nur ausgeliehen ist, habe ich immerhin einen angemessenen aussuchen können. Dafür, dass ich so selten einen trage, ist er überraschend bequem – und er passt ebenso gut zum Etablissement wie Lillys Kleid."


hi "Ich schätze, das ist dann wohl für uns beide eine neue Erfahrung."


$ ksgallery_unlock("evul lilly_restaurant_sheepish")
show ev lilly_restaurant_sheepish onlayer master at restaurant_out
with charachange

"Sie wird ein bisschen verlegen."


li "Ich bin zuvor noch nie in so einem Restaurant gewesen, also ja."


hi "Ein verdammt gutes erstes Date, das ist sicher. Wird ziemlich schwierig für mich, das zu übertreffen."


"Ein kleines Kichern. Unsere Nervosität schwindet weiter."


"Ihre Hand fährt die Mitte des Tisches entlang, bis sie die Speisekarte berührt, welche sie in beide Hände nimmt und vor ihr Gesicht führt."


li "Ähm, Hisao?"


"Als sie das beige, laminierte Papier gerade unter ihre Augen sinken lässt, erkenne ich einen weiteren verlegenen Blick."


"Ich bezweifle, dass es etwas bringen würde, den Kellner zu fragen, ob es die Speisekarte auch in Braille gibt."


hi "Ich kann sie dir vorlesen, kein Problem."


scene bg city_restaurant onlayer master at right
with locationchange

"Ich greife nach meiner und fliege schnell hinüber. Mein Grinsen verfinstert sich."


hi "Äh, vielleicht gibt es doch eins."


show lilly basic_weaksmile_che_close onlayer master:
    center
    ypos 1.1
with charaenter

li "Was stimmt denn nicht?"


hi "Hier sind eine Menge Gerichte drauf… und ich bin mir nicht ganz sicher, wie man manche davon ausspricht."


"Eine feines Gericht nach dem anderen ist aufgelistet. Das meiste mag Japanisch sein, doch einige sind auf Englisch oder Französisch geschrieben. Ich schätze, das war zu erwarten, aber ich habe keine Ahnung, was in manchen von ihnen drin ist."


"Oh, das hier erkenne ich. Nein, warte…"


hi "… Das kann man kochen?"


show lilly basic_giggle_che_close onlayer master
with charachange

"Ein kleines, belustigtes Kichern ist hinter der Speisekarte zu hören."


hi "Na ja, ich könnte sie alle vorlesen, aber ich glaube, das würde ein paar Stunden dauern."


show lilly basic_smile_che_close onlayer master
with charachange

li "Gibt es irgendetwas mit Fisch?"


hi "Mal sehen…"


"Nein. Nein. Nein. Nein. Sind die nicht giftig? Nein. Nein. Nein. So etwas isst man? Nein. Nein. Nein. Nein… Ah, na geht doch."


hi "Ein Thunfischsalat scheint eine gute Wahl zu sein. Vom Bild her sieht er auch so aus, als würde er ziemlich satt machen."


show lilly basic_smileclosed_che_close onlayer master
with charachange

li "Das scheint mir eine vernünftige und sichere Wahl."


hi "Lass uns dann zwei bestellen. Ich bin mir ziemlich sicher, dass ein paar dieser Gerichte von giftigen Tieren sind. Fürs erste hatte ich genügend Nahtod-Erfahrungen."


show lilly basic_weaksmile_che_close onlayer master
with charachange

"Lilly behält ihr Lächeln bei, doch man merkt das fehlende Lachen. Schwarzer Humor ist wohl nicht ihr Ding, und um ehrlich zu sein, finde ich es ebenfalls nicht außerordentlich witzig."


li "Hier schweben auf jeden Fall einige sehr interessante Gerüche herum. Und zu sehen gibt es auch einiges, nehme ich an."


hi "Ich bin noch nie in so einem Lokal wie diesem gewesen. Bei ein, zwei Gelegenheiten mal ein ausgefallenes japanisches Teehaus, aber nie etwas so Nobles und mit so einem europäischen Stil."


"Bevor wir weiterreden können, erscheint ein korpulenter Kellner in einer peinlich engen Weste an unserem Tisch, um unsere Bestellungen entgegenzunehmen."


hi "Provençal Tuna Salade Niçoise, bitte. Zweimal."


"Ich hoffe, ich habe die Aussprache nicht zu allzu sehr vermasselt. Selbst wenn ich es hätte, er lässt sich nichts anmerken."


show lilly behind_cheerful_che_close onlayer master
with charachange

li "Und dazu hätte ich noch gerne ein Glas Chardonnay, bitte. Hisao?"


hi "Oh, äh, das Gleiche."


"Als der Kellner nickt und geht, begreife ich plötzlich, was ich mit meiner gedankenlosen Nachahmung von Lillys Antwort eigentlich gesagt habe. Ich bereue es ziemlich schnell."


hi "Alkohol…"


show lilly basic_pout_che_close onlayer master
with charachange

li "Nur ein bisschen."


"Dieses Mädchen hat wirklich eine seltsame Veranlagung, süchtig nach etwas zu werden."


hi "Überraschend, dass sie nicht nach unseren Ausweisen gefragt haben."


hi "Andererseits sehen wir beide für unser Alter wohl recht erwachsen aus."


show lilly basic_smileclosed_che_close onlayer master
with charachange

li "Da muss ich mich auf deine Einschätzung verlassen. Aber ich muss dazu sagen, dass dies nicht für die Art von Lokal ist, wo man nach solchen Dingen fragt."


hi "Gutes Argument."


"Entspannt lassen wir uns etwas in unsere Sitze sinken und versuchen, die erdrückende Förmlichkeit der Umgebung zu verdrängen."


"Währenddessen erscheint der gleiche Kellner erneut an unserem Tisch – mit zwei leeren Gläsern und einer Flasche, deren Inhalt er dann auch gleich zügig und professionell einschenkt."


scene ev lilly_restaurant_wine onlayer master:
    zoom 1.05 xalign 0.0 yalign 0.5 subpixel True
    easeout 8.0 zoom 1.0
with flash

"Wir beide nicken höflich, als er geht. Lilly nimmt ihr Glas und schwenkt es behutsam. Die rote Flüssigkeit glitzert, als sie sich in dem Glas bewegt, und ich muss zugeben, dass ich es schon etwas weniger bereue, dass ich das Gleiche bestellt habe."


"Ich schätze, es muss Mühe machen, eine Flüssigkeit danach zu beurteilen, wie sich ihr Masseschwerpunkt verhält. Vielleicht ist es wie Origami für sie – sie nutzt jede Gelegenheit, um ihre Geschicklichkeit zu trainieren."


hi "Ich sollte nicht überrascht sein, dass du so ein Lokal kennst. Wer Geld hat, ist wohl mit solchen Orten vertraut."


"Das erinnert mich daran, wie vollkommen unterschiedlich unsere Erziehung war."
"Auf der Yamaku ist es leicht, die sozialen und wirtschaftlichen Ungleichheiten zwischen den Schülern zu vergessen, weil alle Schülern die gleiche Uniform tragen und in den gleichen Wohnheimen wohnen."


scene bg city_restaurant onlayer master at right
show lilly basic_smile_che_close onlayer master:
    center
    ypos 1.1
with flash

li "Na ja, Akira war diejenige, die mir davon erzählt hat. Anscheinend ist sie schon einmal hier gewesen."


"Also hatten sie das am Freitag miteinander besprochen."


hi "Und du beschwerst dich, dass ich schummle?"


show lilly basic_displeased_che_close onlayer master
with charachange

li "Das ist nicht Schummeln. Das nennt man einfach, seine Kontakte spielen lassen."


hi "Wenn du meinst. Trotzdem bekomme ich das Gefühl, dass du dich mit dieser Art von Restaurant besser auskennst als ich."


show lilly basic_reminisce_che_close onlayer master
with charachange

with Pause(0.5)

show lilly basic_smileclosed_che_close onlayer master
with charachange

"Sie hält mit einem wehmütigen Blick auf ihrem Gesicht inne, dann lächelt sie sanft. Diese Kompliment scheint sie aufzuheitern."


show lilly basic_planned_che_close onlayer master
with charachange

li "Du kannst dich dafür bei meiner alten Schule bedanken. Wenn ich nicht diesen Eindruck erwecken würde, wären sie sehr enttäuscht."


"Sie hat ihre frühere Schule zwar schon einmal erwähnt, aber nun bin ich irgendwie neugierig. Sie scheint viel über ihre Vergangenheit nachzudenken, darum sollte es kein Problem sein zu fragen."


hi "Wie war es dort?"


show lilly basic_smile_che_close onlayer master
with charachange

li "Es war eine sehr renommierte katholische Mädchenschule – deswegen haben meine Eltern sie für mich ausgesucht. Viele reiche Familien schickten ihre Töchter dorthin."


hi "Hört sich an, als wäre das Leben dort ziemlich streng gewesen."


show lilly basic_weaksmile_che_close onlayer master
with charachange

li "Ich würde nicht sagen, dass es eine schlechte Erfahrung war… aber du hast schon Recht – es war sehr strikt. Glücklicherweise habe ich es geschafft, mich dort ganz gut einzuleben und einige Freunde zu finden."


show lilly basic_reminisce_che_close onlayer master
with charachange

li "Unglücklicherweise kann man von meiner Schwester nicht das Gleiche behaupten. Sie fand die Atmosphäre und den religiösen Aspekt erdrückend, und hat sich so schnell sie konnte einen Job gesucht, um dort wegzukommen."


show lilly basic_weaksmile_che_close onlayer master
with charachange

"Sie gibt ein kleines, selbstironisches Kichern von sich."


li "Aber ich sollte mich nicht beschweren. Nicht viele haben auch nur die Chance, an so eine Schule zu gehen."


hi "Verübelst du es… deinen Eltern, dass sie dich dorthin geschickt haben und dann abgereist sind?"


"Sie schüttelt langsam den Kopf."


show lilly basic_reminisce_che_close onlayer master
with charachange

li "Mein Familie ist äußerst patriarchal. Mein Vater hat immer nur das Geschäftliche im Kopf und wusste überhaupt nicht, was er mit mir anfangen sollte."


show lilly basic_weaksmile_che_close onlayer master
with charachange

li "Am Ende hat er entschieden, dass meine Bildung höhere Priorität hat als die Nähe meiner Familie."


li "Er tat einfach, was er für richtig hielt."


"Dass sie so etwas so locker sagen kann… Was für ein unglaubliches Mädchen."
"Nichtsdestotrotz bin ich ein bisschen überrascht, dass sie nicht glaubt, dass ihre Blindheit dabei irgendeine Rolle gespielt hat… aber vielleicht bin ich nur zu hart ihrer Familie gegenüber."


hi "Du bist zu gutmütig, weiß du das?"


show lilly basic_surprised_che_close onlayer master
with charachange

li "Hmm?"


hi "Die Meisten würden ihre Eltern für so etwas hassen."


show lilly basic_weaksmile_che_close onlayer master
with charachange

li "Na ja, manche tun es…"


"Ohne meine hochgezogenen Augenbrauen wahrzunehmen, nimmt sie einen Schluck aus ihrem Glas."
"Da ihr ihre Vorliebe für Wein offenbar über den Geschmack von Alkohol hinweghilft, kriegt sie ihn problemlos hinunter. Von mir kann ich nicht das Gleiche behaupten."


show lilly basic_smile_che_close onlayer master
with charachange

li "Was ist mir dir? Wie war deine Schule?"


hi "Meine? Mal sehen…"


hi "Es war eine ziemlich normale öffentliche Schule, denke ich. Vielleicht etwas voller als der Durchschnitt."


hi "Ich schlug mich im Unterricht ganz gut und spielte im Fußballklub. Da ich ein Einzelkind bin und meine Eltern viel arbeiteten, verschwendete ich meine meiste Freizeit und das meiste von meinem Geld mit meinen drei Freunden in der Spielhalle."


hi "Aber egal wie viel ich spielte, ich schaffte es nie, Mai an diesen Automaten zu besiegen. Sogar Takumi und Shin verloren immer, wenn sie es versuchten."
hi "Ich war auch immer derjenige, der versuchte, ein verantwortungsbewusster Erwachsener zu sein, wenn Shin und Mai sich stritten. Mal wieder."


hi "Nur wir vier, wie wir ziellos unsere Kindheit genossen. Das waren wirklich alberne Zeiten."


"Ich ertappe mich dabei, wie ich abschweife. Die Tage meiner alten Schule verschwinden im Nachthimmel und den hellen Straßenlichtern außerhalb des Fensters."


"Auf Lillys Gesicht zeichnet sich eine seltsame Mischung aus Neugier und Mitleid ab. In Anbetracht ihrer strengen Schule vermute ich, dass das wohl ein interessanter Kontrast zu dem einzigen Leben ist, das sie kennt."


show lilly basic_satisfied_che_close onlayer master
with charachange

li "Es klingt, als hättest du auf deiner alten Schule eine Menge Spaß gehabt."


hi "Ich bin nicht wirklich sicher, wie viel davon Nostalgie ist, aber es sind ein paar schöne Erinnerungen."


hi "Aber das liegt in der Vergangenheit. Ich kann nicht mehr dorthin zurück, aber durch meinen Unfall habe ich ein neues Leben gefunden, das ich mir nie hätte vorstellen können."


hi "Der Frieden und die Gelassenheit an der Yamaku, eine neue Richtung für meine Zukunft in der Wissenschaft, die Freundschaft mit Shizune, Misha und Hanako. Und vor allem du."


scene ev lilly_touch_cheong onlayer master
with whiteout

"Sie schenkt mir ein großes, aufrichtiges Lächeln und bewegt ihre Hand in meine Richtung. Ihre Finger ertasten vorsichtig mein Gesicht und liebkosen sanft meine Wange."


scene bg city_restaurant onlayer master at right
show lilly basic_smileclosed_che_close onlayer master:
    center
    ypos 1.1
with whiteout

"Sie zieht ihre Hand nach einem stillen Augenblick widerwillig zurück, als wir bemerken, dass sich der Kellner mit unseren Salaten nähert."


"Lilly schafft es sehr gut, ihre Blindheit zu überspielen, nur ihr dankbares Nicken ist wegen seines Schweigens etwas falsch ausgerichtet."


"Sie scheint sich wirklich anzustrengen, um in der Öffentlichkeit so normal wie möglich zu wirken."
"Obwohl mir das schon seit langer Zeit klar ist, kann ich immer noch nicht richtig einschätzen, ob sie nicht anders behandelt werden will, ob es ihre Eitelkeit ist, oder eine Mischung aus beidem."


scene ev lilly_restaurant_eat onlayer master
with shorttimeskip

"Das servierte Gericht macht seinem Namen alle Ehre, und die Portion ist angenehm groß. Mit geschnittenen Eiern und Tomaten sieht es in der Tat sehr verlockend aus."


"Lilly nimmt ihr Messer in die eine Hand und die Gabel in die andere und macht sich genau wie ich über den Teller her. Sonst essen wir immer früher zu Abend, deshalb haben wir beide Hunger."


scene ev lilly_restaurant_chew onlayer master
with locationchange

"Ich spieße vorsichtig die Blätter und die fleischigen Würfel mit meiner Gabel auf, während Lilly sich still und bedächtig das Essen auf dem Teller zurechtschiebt."


"Ein gelegentliches Danebenpieksen, wenn sie versucht, einen Happen auf die Gabel zu nehmen, ist das Einzige, was ihre fehlende Sicht erahnen lässt."


scene bg city_restaurant onlayer master at right
with locationchange

"Nach kurzer Zeit bin ich mit meinem Salat fertig. Lilly nimmt ihre letzten paar Bissen, während ich sie dabei beobachte."


show lilly basic_smile_che_close onlayer master:
    center
    ypos 1.1
with charaenter

li "Fertig, Hisao?"


hi "Ja. Es war ziemlich lecker."


"Das ist nur allzu wahr. Ich hätte nie gedacht, dass ein simpler Salat so lecker und sättigend sein könnte, aber andererseits vermute ich, dass es deswegen so viel kostet, hier zu essen."


show lilly basic_smileclosed_che_close onlayer master
with charachange

"Zufrieden mit meiner Wertschätzung und offensichtlich der gleichen Meinung nickt Lilly leicht."


hi "Weißt du… Dafür, dass du teils ausländisch bist, exotisch und ziemlich hübsch aussiehst, bin ich überrascht, dass dir noch nie jemand seine Liebe gestanden hat."


show lilly basic_planned_che_close onlayer master
with charachange

li "Du {b}nimmst an{/b}, dass das niemand getan hat."


"Dieses schlichte Statement überrumpelt mich. Da ich ihr vor ein paar Sekunden noch selbst dieses Kompliment gemacht habe, sollte ich nicht überrascht sein. "


hi "Wirklich?"


show lilly basic_smile_che_close onlayer master
with charachange

li "Ich habe mehrere Liebesgeständnisse bekommen, sowohl an dieser als auch an meiner alten Schule."


show lilly basic_weaksmile_che_close onlayer master
with charachange

li "Pubertät ist eine lustige Zeit."


"Sie redet davon, als ob sie irgendwie darüberstehen würde…"


hi "Hm. Wie einfach du so etwas sagen kannst."


show lilly basic_surprised_che_close onlayer master
with charachange

with Pause(0.5)

show lilly basic_cheerful_che_close onlayer master
with charachange

"Lilly sieht einen Moment lang überrascht aus, bevor sich ein verspieltes Schmunzeln auf ihrem Gesicht breitmacht."


li "Ist das etwa… Eifersucht?"


hi "Was? Nein. Ist es nicht."


show lilly basic_giggle_che_close onlayer master
with charachange

li "Du bist ein schlechter Lügner, Hisao. Das solltest du berücksichtigen."


show lilly basic_smileclosed_che_close onlayer master
with charachange

li "Andererseits schätze ich, wie ehrlich du bist. Auch wenn du es manchmal gar nicht beabsichtigst."


li "Ich denke, deine Ehrlichkeit wird dir immer Gutes bringen, wenn du mit anderen zu tun hast."


"Ich räuspere mich mit vorgetäuschtem Missfallen über diese ganze Angelegenheit und versuche, die Unterhaltung woandershin zu lenken."


hi "Aber um die Wahrheit zu sagen, bevorzuge ich es, allein zu sein. Ich denke nicht, dass ich einen Freundeskreis wie deinen aufrechterhalten könnte."


show lilly basic_listen_che_close onlayer master
with charachange

"Sie denkt einen Moment lang darüber nach."


show lilly basic_smile_che_close onlayer master
with charachange

li "Ich denke, dass das ebenfalls nicht stimmt."


show lilly basic_smileclosed_che_close onlayer master
with charachange

li "Ich habe gesehen, wie vorsichtig und fürsorglich du bei Hanako bist, und du kommst fabelhaft mit anderen aus – sogar mit jenen, die du kaum kennst. Ich glaube, du hast ein gutes Händchen für soziale Situationen."


show lilly basic_cheerful_che_close onlayer master
with charachange

li "Aber bei dem Thema: Was ist mit deinen Liebesgeständnissen, Hisao? Ich bin mir sicher, dass jemand wie du mindestens eine Verehrerin gehabt haben muss."


"Als ich meinen Mund zum sprechen öffne, kann ich spüren, wie mein Gesicht etwas düster wird. Heimlich bin ich froh, dass sie meinen Ausdruck nicht sehen kann."


hi "Nur… eine. Ihr Name war Iwanako."


hi "Ich hatte meine Herzattacke, als sie mir ihre Liebe gestanden hat. Mitten im Wald, letzten Winter."


show lilly basic_oops_che_close onlayer master
with charachange

"Lilly ist sprachlos. Sie hat wohl nicht erwartet, dass das Gesprächsthema in solch eine Richtung geht."


"Mein Leiden hat ihr schon immer Sorgen bereitet. Das ist etwas, was ich versuche zu minimieren, trotz der gegenteiligen Bemühungen meines Körpers."


hi "Danach hat sie mich eine Weile lang besucht, als ich im Krankenhaus war. Wochenlang kam sie vorbei und unterhielt sich mit mir. Es war meistens nur Smalltalk oder Gerüchte aus der Schule, aber das war genug."


hi "Doch schließlich… kam sie nicht mehr."


hi "Sie war jeden Tag da. Dann jeden zweiten. Dann einmal die Woche. Und letztendlich hörte sie eines Tages ganz mit ihren Besuchen auf."


show lilly basic_sleepy_che_close onlayer master
with charachange

li "Hast du sie… je wieder gesehen?"



label de_choiceL24:
menu:
    with menueffect
    "Versunken in meiner eigenen Welt schüttle ich meinen Kopf, bis ich daran denke, dass diese Geste Lilly nichts bringt."
    "Den Brief erwähnen.":




        return m1
    "Das Thema wechseln.":

        return m2




label de_L24a:

"Der eine Brief, den mir Iwanako geschickt hat, fällt mir wieder an."


hi "Ich habe sie nie wieder gesehen, aber nachdem ich an die Yamaku geschickt wurde, hat sie mir einen Brief geschrieben."


"Lillys Gesicht zeigt einen Ausdruck, den ich gut kenne. Ich habe ihr Interesse erweckt. Ich wäre leicht beleidigt, dass sie so neugierig ist, aber sie war eben noch nie gut darin, ihre Reaktionen zu verstecken."


hi "Im Nachhinein hat er nicht viel ausgesagt: Wie es in meiner alten Klasse so läuft, wie es ihr ergeht und – fast als Nachsatz – dass es wahrscheinlich das Beste für uns beide wäre, wenn wir uns nicht wiedersehen."


hi "Nachdem ich ihn gelesen hatte, habe ich noch einmal über viele Dinge nachgedacht, von denen ich dachte, dass ich mit ihnen abgeschlossen hätte."
hi "Hauptsächlich hat mich dieser Brief daran erinnert, dass die Welt um mich herum sich immer noch dreht, und wie sehr ich von ihr isoliert wurde."


hi "Und… ich schätze, er hat mich auch an das erinnert, was ich verloren habe."


show lilly basic_emb_che_close onlayer master
with charachange





"Es ist ein seltsamer Anblick, Lilly so sprachlos zu sehen. Ihre ganze Fassade ist durch ihr vorheriges, vertieftes Interesse etwas zerbröckelt. So charismatisch sie auch ist, am Ende ist das kein Ersatz für Lebens- oder Beziehungserfahrung."


show lilly basic_reminisce_che_close onlayer master
with charachange

li "Vielleicht… ist es besser, dass sie ihn dir geschickt hat."


hi "Wie kommst du darauf?"


show lilly basic_weaksmile_che_close onlayer master
with charachange

li "Herauszufinden wie man am besten mit denen kommuniziert, die man lange nicht gesehen hat, kann schwierig sein. Umso mehr, wenn man eure verschiedenen Situationen betrachtet."


li "Anstatt den einfachsten Weg zu gehen, hat sie die Courage aufgebaut, um mir dir ein letztes Mal zu reden. Nicht nur um ihretwillen, sondern allem Anschein nach auch dir zuliebe."


hi "Vielleicht. Ich hasse sie nicht dafür. Nicht, dass ich das auch je hätte, aber… ich weiß nicht."


"Wahrscheinlich war das eher eine zu zurückhaltende Antwort, aber das ist nicht ohne Grund. Ich habe diese Situation zuvor noch nie aus Iwanakos Perspektive betrachtet."


label de_L24b:

"Iwanako will ich wirklich nicht mehr als nötig erwähnen. Dieses Date gehört schließlich allein mir und Lilly. In so einem Moment will ich nicht nicht an eine frühere Beziehung denken."


hi "Nein, das war das letzte Mal, dass ich sie gesehen habe. Wir haben danach auch nie wieder miteinander geredet."




label de_L24c:

"Sekunden vergehen schweigend, bis Lilly wieder zu sprechen beginnt."


show lilly basic_sad_che_close onlayer master
with charachange

li "Nach Yamaku zu ziehen muss hart für dich gewesen sein. Deine Freunde und sogar deine Freundin wurden dir genommen, obwohl du nichts getan hast."


hi "Das meiste davon hatte ich schon akzeptiert, während ich im Krankenhaus war. Wenn dich nichts weiter als vier weiße Wände und ein kleiner Fernseher umgeben, beginnt dein Kopf, sein eigenes Leben zu leben."



hi "Wie an meiner alten Schule, schätze ich. Ich versuche, nicht zu sehr an Geschehenes zu denken, und schaue nach vorne."


hi "In all diesen Erinnerungen zu schwelgen macht mir zu schaffen, und es ist Größtenteils dir zu verdanken, dass es sich anfühlt, als würden die Dinge endlich wieder ins Lot kommen."


show lilly basic_veryemb_che_close onlayer master
with charachange

li "Das… freut mich zu hören, Hisao."



"Mit einem nachdenklichen Gesichtsausdruck senkt sie leicht ihren Kopf. Ich schätze, ich bin zu weit gegangen und habe sie verlegen gemacht."


hi "Vermutlich hast du etwas Ähnliches durchgemacht, als du an der Yamaku eingeschult wurdest, oder nicht? An und für sich denke ich, dass das die große Mehrheit der Schüler hinter sich hat. "


hi "Du hast selbst gesagt, dass du an deiner alten Schule Freunde gefunden hast. Ich kann mir nicht vorstellen, dass dir viele gefolgt sind."


show lilly basic_displeased_che_close onlayer master
with charachange

"Lillys lächeln verfliegt und ihr Gesichtsausdruck verfinstert sich unerwarteterweise. Sogar ihre Hände legt sie in ihren Schoß."


"Nach einer langen Zeit fängt sie an zu sprechen."


show lilly basic_reminisce_che_close onlayer master
with charachange

li "Hisao… kannst du mir versprechen, niemandem zu erzählen, was ich dir gleich-"


hi "Ich verspreche es."


"Mein ernster Ton scheint sie leicht zu verblüffen, doch dann gibt sie nach und lächelt zaghaft, bevor sie fortfährt."


show lilly basic_weaksmile_che_close onlayer master
with charachange

li "Als ich nach Yamaku zog, bedauerte ich es, die Freunde zu verlieren, die ich auf meiner alten Schule hatte."


show lilly basic_reminisce_che_close onlayer master
with charachange

li "Doch da war eine Person, bei der ich es am meisten bedauerte. Er war der Grund, warum ich Englisch als meine zukünftige Karriere auswählte."


"„Er”? Wenn sie von einer Mädchenschule kam, kann das kein Schulkamerad gewesen sein…"


li "Ich lehnte alle Liebesgeständnisse, die ich damals bekam, seinetwegen ab. Jedes Mal, wenn ich meine Englischfähigkeiten verbesserte, war sein Lob meine schönste Belohnung."


show lilly basic_weaksmile_che_close onlayer master
with charachange

li "Lustig, nicht wahr? Ich hätte damit angeben können, wie viele Leute ein Auge auf mich geworfen haben… und ich war in jemanden verliebt, der gänzlich unerreichbar war – in meinen Klassenlehrer."


li "Es ist wirklich lächerlich…"


hi "Hast du…?"


"Sie schüttelt sofort den Kopf."


show lilly basic_displeased_che_close onlayer master
with charachange

li "Ich konnte nicht. Selbst damals wusste ich, dass es unmöglich war."


"Schweigen überkommt uns."


"Das scheint ihren leidenschaftlichen Fokus auf ihre Karriere als Englischlehrerin zu erklären, jedoch kann ich nur an ihr Geständnis mir gegenüber denken."


"Sie verlor ihn, ohne ihn je von ihren Gefühlen wissen zu lassen… Hatte sie Angst, dass das Gleiche noch einmal geschehen würde? Nur diesmal mit mir?"


"Ich weiß nicht recht, was ich davon halten soll. Von solchen Beziehungen habe ich schon einmal gehört; Tabus geboren aus Dingen wie Pubertät und Jugend. Jedoch ist es ermutigend, dass sie so ein gutes Urteilsvermögen hatte, nicht danach zu handeln."


show lilly basic_emb_che_close onlayer master
with charachange

li "Ich weiß, das muss komisch klingen, aber bitte… halt mich nicht für…"


hi "Warum sollte ich deswegen schlecht von dir denken?"


hi "Um ehrlich zu sein, ich glaube, er muss ein sehr netter Mensch gewesen sein, wenn du ihn so sehr mochtest. Nicht nur das – du hast dich sogar davon abgehalten, zu weit zu gehen."


with Pause(1.0)

show lilly basic_arablush_che_close onlayer master
with charachange

"Für einen Augenblick sieht sie etwas verloren aus. Allerdings dauert es keine Sekunde, bis sie unerwarteterweise zu lachen anfängt."
"Der Klang trifft mich unvorbereitet. Es ist weder ein Kichern noch ein zurückgehaltenes Schmunzeln, sondern ein ehrliches und aufrichtiges Lachen."


"Ich muss lächeln, und das nicht nur wegen ihrer Zurschaustellung von Erleichterung und Freude, sondern auch, weil sie mir so sehr vertraut, dass sie mir von ihren privatesten Geheimnissen erzählt."


scene ev lilly_touch_cheong onlayer master
with whiteout

"Bevor ich mich versehe, spüre ich, wie ihre Handfläche mein Gesicht berührt. Ihre Berührung ist sanft wie nie, und ihr Daumen streichelt meine Wange."


li "Du bist lieb, Hisao. Ich liebe dich wirklich."


"Ihr Gesicht so zu sehen, während ihre Hand sanft mein Gesicht liebkost… Ich denke, heute war ein wundervoller Abend."


hi "Schätze, wir beide haben ziemlich seltsame Vergangenheiten, was?"


li "Ich denke, nach den meisten Maßstäben ist unsere Gegenwart auch nicht gerade normal."


"Ich lächle und lasse meine Kopf hängen. Diese Frau kann mich locker in den Schatten stellen, dessen bin ich mir sicher."


scene bg city_restaurant onlayer master at right
with whiteout

"Ich schaue mich im Restaurant um, das noch immer von den Gesprächen der Gäste erfüllt ist."


hi "Dieses Lokal passt wahrscheinlich auch in die Kategorie „seltsam”."


show lilly basic_weaksmile_che_close onlayer master:
    center
    ypos 1.1
with charaenter

li "Es ist einen ein bisschen… erdrückend."


hi "Ja, das Wort passt."


"Mir fällt ein wuselnder Kellner auf. Ein kleiner, dürrer Kerl kaum älter als zwanzig. Er erinnert mich irgendwie an Kenji, allerdings ist der Kellner nicht wie er im Hochsommer für den Winter gekleidet."


show lilly basic_smileclosed_che_close onlayer master
with charachange

"Nach einer höflichen Verbeugung und dem Angebot, unsere Teller abzuräumen, fragt Lilly sanft und höflich nach der Rechnung."


"Mit meisterhafter Geschicklichkeit manövriert er mit unseren Tellern in den Händen zwischen den Tischen hindurch, um unsere Rechnung zu holen."


"In Windeseile kommt er wieder aus der Tür und reicht Lilly elegant die Rechnung."


show lilly basic_smile_che_close onlayer master
with charachange

"… die sie wiederum prompt mir überreicht, was den Kellner dazu bringt, eine Augenbraue hochzuziehen."


"Beim Lesen des kleinen gedruckten Zettels erkenne ich, dass die Kosten meine Erwartung beträchtlich übersteigen."


show lilly basic_surprised_che_close onlayer master
with charachange

li "Hisao?"


hi "Oh… äh…"


show lilly basic_smileclosed_che_close onlayer master
with charachange

"Zügig stammle ich die Summe, woraufhin Lilly lediglich nickt und nach ihrem Portemonnaie greift."


"Als sie dem Kellern ihre Karte übergibt, verschwindet er ein weiteres Mal."


hi "Das war… eine unverhältnismäßig große Menge Geld."


show lilly basic_emb_che_close onlayer master
with charachange

"Diese Feststellung scheint Lilly etwas unbehaglich zu machen."


show lilly basic_weaksmile_che_close onlayer master
with charachange

li "Meine Familie überlässt mir mehr als genug Geld für meine Bildung. Das Gleiche gilt für meine Schwester, auch wenn sie ungern daran erinnert wird."


show lilly behind_cheerful_che_close onlayer master
with charachange

li "Abgesehen davon mag ich es auch nicht, Geld aus dem Fenster zu werfen. Doch dieses eine Mal, denke ich, kann ich eine Ausnahme machen. Nur für dich."


hi "Du hast nicht nur unser Date ausgesucht, du hast sogar für uns beide bezahlt…"


"Ich reibe mir mit meinen Fingern die Nasenwurzel."


hi "Ich kann nicht fassen, wie hoch du die Latte für unser nächstes Date gesetzt hast."


show lilly basic_giggle_che_close onlayer master
with charachange

"Sie gibt ein kleines Kichern von sich."


show lilly basic_smileclosed_che_close onlayer master
with charachange

li "Ich freue mich schon darauf, Hisao."


"Wie durch Zauberei erscheint der Kellner neben uns und gibt Lilly ihre Karte zurück."
"Offenbar bemerkt er ihre Blindheit und platziert die Karte – vielleicht unnötigerweise – mit extra viel Druck auf ihrer Hand, um sicherzustellen, dass sie sie auch festhält."


"Als er geht, bemüht er sich als diplomatische Maßnahme, trotz meines verwunderten Gesichtsausdrucks ein neutrales Gesicht zu bewahren."


"Ich klatsche in die Hände und stehe von meinem Stuhl auf, um unseren Abend zum Abschluss zu bringen."


hi "Wollen wir uns dann auf den Weg machen, meine Dame?"


stop music fadeout 2.0

scene black onlayer master
with dissolve




label de_L25:

scene black onlayer master
with Dissolve(2.0)

scene bg school_dormhisao_ni onlayer master
with vpunch

hi "Uah!"


"Blitzartig schieße ich aus meinen Federn hoch und sitze kerzengerade auf dem Bett, als hätte gerade ein Stromstoß meinen ganzen Körper durchfahren."


"Die Nachtluft fühlt sich auf dem Schweiß meiner nackten Haut kalt an, und meine Atmung ist kurz und rau, fast an der Grenze zum Hyperventilieren."


"Mit rasenden Gedanken fasse ich mir mit der Hand an den Kopf und versuche, meinen in Panik geratenen Körper zu beruhigen."
"Ich brauche paar Sekunden, um zu bemerken, dass meine Hand heftig zittert – sogar als ich sie gegen mein Gesicht presse."


"Weitere Sekunden vergehen in vollkommener Stille. Meine verzweifelten Versuche, meinen Körper und Verstand zu bändigen, haben Gott sei Dank Erfolg."


"Ich sammle mich und fange an, meinen Zustand einzuschätzen. Es fühlt sich an, als wäre ich einen Marathon gelaufen. Jeder Muskel ist angespannt, und der Schweiß trieft nur so von mir."


"Vorsichtig lenke ich meine Aufmerksamkeit auf das Klopfen in meiner Brust und messe seinen Rhythmus in meinem Kopf. Tatsächlich funktioniert mein unzuverlässiges Herz ausnahmsweise einmal."


"Nur… Was zur Hölle war das?"


"Eine Herzattacke? Ein schlimmer Alptraum? Medikamentennebenwirkungen? Ich habe von Panikattacken schon gehört, und es scheint, als wäre das eine gewesen…"


"Ich kann gerade nicht einmal richtig darüber nachdenken. Nach dieser Erfahrung bin ich so vollkommen erschöpft und doch absolut wach."


"Ich schaue hinüber zur anderen Seite meines Bettes, wo das blasse Weiß des Gesichts des stillen Mädchens in der nächtlichen Dunkelheit des Raumes fast zu glühen scheint. Allein ihr Anblick ist genug, um mich deutlich zu beruhigen."


scene ev lilly_sleeping_smile onlayer master:
    truecenter
    zoom 1.0 subpixel True
    acdc_warp 20.0 zoom 1.05
with locationchange

"Sogar im Schlaf behält sie ihre Eleganz bei. Ihre perfekt abgestimmte Atmung und ihr sanftes Gesicht machen es unmöglich zu sagen, ob sie wach ist oder wirklich schläft."


"Ich gebe der Versuchung nach und fahre mit meinen Fingerspitzen vorsichtig über ihre Hand. Ihre Haut fühlt sich so weich wie immer an, und sogar in der Kälte der Nacht ist sie warm."


"In Momenten wie diesem, in denen wir still die Gegenwart des anderen genießen, fühle ich mich ihr am meisten verbunden."


"Meine Finger stoppen an ihrem Handgelenk, und ich lege meine Hand wieder neben mir auf das Bett."


"Ich bin mir nicht ganz sicher warum, aber als wir uns beide näherkamen, fühlte es sich an, als würde zwischen uns etwas wachsen. Ich bin mir nicht ganz sicher, was es ist oder ob es schon existierte, bevor wir uns ineinander verliebten."


"Alles entwickelt sich so schnell. Es stört mich ganz und gar nicht, aber es passt nicht wirklich zu Lilly."


scene bg school_dormhallway onlayer master
with shorttimeskip

play music music_dreamy fadein 2.0

"Zum Glück schwirren so früh am Morgen noch keine Schüler in den Gängen herum, sodass ich nicht ausgefragt werde, warum ich zwei Teller mit Frühstück zu meinem Zimmer trage, während ich eine offensichtlich hektisch angezogene Uniform anhabe."


"Damit will ich natürlich nicht sagen, dass solche Dinge nie passieren."
"Ein einzelner Sicherheitswärter, der zwischen den beiden direkt nebeneinanderliegenden Wohnheimen patrouilliert, kann kaum etwas gegen all die pubertären Hormone ausrichten."


"Da fällt mir ein – dass es Montag Morgen ist, ist vielleicht ganz gut. Ich weiß nicht genau wieso, aber Montage scheinen mich weniger zu stören als die meisten anderen."


"Es ist ein wenig kreative Hand- und Ellenbogenarbeit nötig, aber schließlich schaffe ich es, die Tür zu meinem Zimmer aufzukriegen."


scene bg school_dormhisao onlayer master
show lilly basic_sleepy_paj onlayer master at center
with locationchange

"Als ich eintrete, sehe ich Lilly, die gerade vom Bett aufsteht und müde ihre Augen reibt. Sie sieht schrecklich aus, genauso wie all die anderen Male, als ich sie direkt nach dem Aufstehen gesehen habe. Sie ist wirklich kein Morgenmensch."


hi "Entschuldige, ich wollte dich nicht wecken."


show lilly basic_displeased_paj onlayer master
with charachange

"Noch nicht ganz auf der Höhe schüttelt sie ihren Kopf. Im Morgenlicht bietet sie einen sehr angenehmen Anblick."


show lilly basic_weaksmile_paj onlayer master
with charachange

li "Schon okay, ich musste sowieso aufstehen. Wie spät ist es?"


"Ich stelle meinen Teller auf meinen Schreibtisch und drehe die Uhr, um nach der Zeit zu sehen."


hi "Immer noch früh. Keine Sorge, wir haben reichlich Zeit, bevor die Schule beginnt."


show lilly basic_smileclosed_paj onlayer master:
    ypos 1.2
with dissolvecharamove

"Sie setzt sich an die Bettkante und beginnt in der Luft zu schnüffeln. Als sie das tut, bewege ich ihren Teller schnell weg und stelle ihn neben meinen auf den Schreibtisch."


hi "Ja, ich hab uns etwas Frühstück geholt. Aber zuerst mal Duschen und Anziehen."


scene ev lilly_kissing onlayer master
with flash

"Mit leicht erhobenem Kinn steht sie für einen Moment lang still da. Mit Freuden nehme ich es hin, presse meine Lippen auf ihre und genieße das weiche Gefühl, bevor wir uns voneinander lösen."


scene bg school_dormhisao onlayer master
with locationchange

"Mit einem kleinen, süßen Lächeln – anscheinend recht zufrieden – macht sie sich langsam auf den Weg zur Dusche."


"Um mich etwas wacherzukriegen, strecke ich mich und schaue kurz auf die dampfenden Teller auf dem Schreibtisch. Reis, Fisch, Miso-Suppe und etwas Gemüse – ein Standardfrühstück für einen etwas ungewöhnlichen Tag."


"Ich greife nach den Fläschchen auf meinem Schreibtisch und nehme meine tägliche Dosis Pillen."


show pills onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Manchmal frage ich mich, wozu sie überhaupt gut sind, wenn ich an all den Ärger zurückdenke, den ich seit dem ersten Anfall hatte. Ich kann nicht einmal sagen, dass ihre Einnahme nicht schadet, wenn man die bisherigen Nebenwirkungen betrachtet."


"Na ja, was soll's. Die Ärzte meinen, ich muss sie nehmen, und es ist nur vernünftig, ihrem Urteilsvermögen mehr zu vertrauen als meinem."


show pills onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide pills onlayer master
with None

"Es dauert nicht lange, bis der Lärm aus der Dusche verklingt. Anscheinend reicht Lilly unter diesen Umständen eine kurze."


show lilly basic_smile_paj onlayer master:
    center
    xpos 0.55
    easein 0.5 xpos 0.5
with charaenter

"Als sie aus dem Badezimmer kommt, sieht sie erheblich wacher aus. Es war wohl eine Gelegenheit für sie, um sich zu sammeln."


show lilly basic_smile_paj_close onlayer master at center
with characlose

show lilly basic_smileclosed_paj_close onlayer master:
    ypos 1.1
with dissolvecharamove

"Ohne ein Wort nehme ich vorsichtig ihre Hand und führe sie an meinen Schreibtisch. Da ich in meinem Zimmer keinen Tisch habe wie sie, muss er reichen."


li "Danke, Hisao. Was hast du zum Frühstück gemacht?"


hi "Nur Reis und etwas Gemüse. Etwas Schnelles."


show lilly basic_ara_paj_close onlayer master
with charachange

"Bei dieser Enthüllung erhellt sich ihr Gesicht."


show lilly basic_satisfied_paj_close onlayer master
with charachange

li "Das klingt nach einem guten Frühstück. Isst du das jeden Morgen?"


"Jetzt ist sie einfach nur höflich. In Anbetracht ihrer Vergangenheit glaube ich kaum, dass dieses Essen ihren hohen Standards gerecht wird."


hi "Frühstück ist die wichtigste Mahlzeit des Tages. Nur weil wir Schüler sind, heißt das nicht, dass wir das auf die leichte Schulter nehmen können."


"Jedenfalls ist das meine Sichtweise. Nach dem, was ich von anderen gehört habe, könnte ich damit in der Minderheit sein."


show lilly basic_smileclosed_paj_close onlayer master
with charachange

"Ich setze mich auf die Kante meines Bettes und beginne zusammen mit Lilly zu essen. Ihre Essstäbchen ertasten vorsichtig das Gemüse, genau wie ich es bei unserem Date schon bemerkt hatte."


show lilly basic_smile_paj_close onlayer master
with charachange

li "Das ist ziemlich lecker, Hisao. Ich wusste ja gar nicht, dass du so gut kochen kannst."


"Diesmal ist sie sehr viel aufrichtiger, so viel kann ich sagen. Allerdings ist Kochen überhaupt nichts Besonderes; nach etwas Übung ist es ziemlich einfach, ein simples Gericht zuzubereiten."


hi "Das meiste davon ist der modernen Technologie zu verdanken; trotzdem sollte ich es mittlerweile können, nachdem ich jahrelang für mich selbst gekocht habe."


hi "Auf Dauer hing es mir zum Hals raus, immer Fertignudeln zu machen oder Pizza zu bestellen, wenn meine Eltern arbeiten waren, also habe ich mir selbst beigebracht, wie man ein paar Gerichte zaubert. Allerdings bin ich noch am Rumprobieren."


show lilly basic_cheerful_paj_close onlayer master
with charachange

li "Du wirst eines Tages eine gute Ehefrau abgeben, Hisao."


"Ich nehme ein Reiskorn und platziere es auf meinem Daumen, bevor ich vorsichtig Ziele und es schwungvoll wegschieße."


show lilly basic_surprised_paj_close onlayer master
with vpunch

"Lilly erschrickt ein wenig, als es ihre Wange trifft. Volltreffer."


show lilly basic_pout_paj_close onlayer master
with charachange

"Ich muss ein wenig schmunzeln, als sie die Augenbrauen zusammenzieht und versucht ernst und böse dreinzuschauen."


show lilly basic_sleepy_paj_close onlayer master
with charachange

li "Oh, stimmt ja…"


hi "Was ist denn?"


show lilly basic_concerned_paj_close onlayer master
with charachange

$ renpy.music.set_volume(0.5, 1.0, channel="music")

li "Hattest du heute Nacht Probleme beim Schlafen? Du hast etwas unruhig gewirkt."


"Also war sie vorhin doch wach, oder zumindest teilweise. Ob es nun mein Herz war oder ein Alptraum, verursacht durch die Nebenwirkungen meiner Medikamente – das Letzte, was ich will, ist, dass sie sich noch mehr Sorgen um mich macht."


"Sogar vor meiner Beziehung mit Lilly spürte ich, wie mein Körper mich bei allem zurückhielt. Mein Körper ist allein meine Bürde, darum werde ich weiterhin so normal wie möglich sein, solange ich bei ihr bin."


hi "Nein, nicht wirklich."


show lilly basic_reminisce_paj_close onlayer master
with charachange

li "Ach so… Dann ist ja gut."


$ renpy.music.set_volume(1.0, 4.0, channel="music")

"Gott sei Dank scheint sie mich beim Wort zu nehmen."


show lilly basic_weaksmile_paj_close onlayer master
with charachange

li "Da fällt mir ein – es gibt noch etwas anderes, das ich dich fragen wollte."


hi "Ja?"


show lilly basic_smileclosed_paj_close onlayer master
with charachange

li "Wie soll ich sagen…"


show lilly basic_smile_paj_close onlayer master
with charachange

li "Wenn man träumt… sieht man dann Menschen und Gegenstände?"


hi "Ja, natürlich. Ich… oh."


"Ich fühle mich mehr als nur ein bisschen verlegen wegen dieses Ausrutschers, so unbeabsichtigt er auch gewesen sein mag. Lilly scheint es aber nicht zu stören."


show lilly basic_smileclosed_paj_close onlayer master
with charachange

li "Aber man schmeckt, fühlt oder riecht nichts?"


"Ich will antworten, gerate aber ins Stocken. Je mehr ich darüber nachdenke, desto mehr begreife ich, dass ihre Hypothese korrekt ist."


hi "Das… stimmt wohl, denke ich. So hab ich's noch nie betrachtet. Willst du damit sagen, dass es bei dir anders ist?"


show lilly basic_smile_paj_close onlayer master
with charachange

li "Meistens höre ich in meinen Träumen nur, aber ja – manchmal rieche oder spüre ich auch etwas."


show lilly basic_planned_paj_close onlayer master
with charachange

li "Ich frage nur, weil Akira das sehr seltsam fand, als ich es erzählt habe. Wenn du es auch nicht tust, dann liegt das vielleicht an meiner Blindheit."


hi "Das würde Sinn ergeben. Du verlässt dich auf deine anderen Sinne mehr als ich, vielleicht beeinflusst das dann auch deine Träume."


"Die Wunder des menschlichen Körpers, schätze ich."


"Den Rest der Zeit, bevor die Schule beginnt, sitzen wir still da und essen das herzhafte Frühstück, während wir dabei etwas Smalltalk führen."


stop music fadeout 2.0

scene bg school_dormext_full onlayer master
with shorttimeskip

"Wir werfen einen kurzen Blick aus der Tür, um sicherzugehen, dass niemand den Eingang des Jungenwohnheims im Auge hat. Sobald die Luft rein ist, gehen wir nach draußen."


play music music_soothing fadein 4.0

hi "Ah, das Wetter ist heute schön."


"Ich strecke mich, als die helle Morgensonne auf uns herabscheint."


"Mittlerweile sieht man, wie ein paar Schüler das Gleiche tun, als sie entweder von den Wohnheimen oder vom Haupttor zum Hauptgebäude strömen."


show lilly cane_smile_close onlayer master at center
with charaenter

li "Es ist schön warm."


"Wir halten uns an den Händen, und Lilly tastet mit ihrem Stock den Weg vor sich ab, während wir uns unter die schwatzenden Schüler um uns herum mischen und uns auch auf den Weg zum Schulgebäude machen."


show lilly cane_smileclosed_close onlayer master
with charachange

li "Heute ist der letzte Tag der Prüfungen, nicht wahr?"


hi "Genau. Wie laufen sie bei dir?"


show lilly cane_concerned_close onlayer master
with charachange

li "Den Umständen entsprechend ganz gut. Allerdings scheinst du im Stress zu sein."


hi "Ist es so offensichtlich?"


hi "Ich glaube aber nicht, dass es nur an den Prüfungen liegt. Vieles ist in sehr kurzer Zeit passiert, und ich bin nicht so gut in den Geisteswissenschaften."


show lilly cane_smileclosed_close onlayer master
with charachange

li "Aber in den Naturwissenschaften bist du doch gut, oder nicht?"


hi "Na ja, für mich wäre es schwierig, in Naturwissenschaften nicht gut zu sein. Wo wir gerade beim Thema sind – hast du nicht mal gesagt, dass du in Naturwissenschaften und Mathe nicht so gut bist?"


show lilly cane_oops_close onlayer master
with charachange

"Plötzlich sieht sie sehr verlegen aus. Meine Bemerkung hat wohl ins Schwarze getroffen. Lillys Stolz kann wirklich ein zweischneidiges Schwert sein."


show lilly cane_smile_close onlayer master
with charachange

li "Nun, das mal beiseite… Hast du je darüber nachgedacht, was du aus dieser Fähigkeit machen könntest? Es wäre eine Schande, so etwas zu verschwenden."


hi "Ein bisschen, hauptsächlich auf Mutous Drängen hin."


hi "Jedenfalls werde ich wahrscheinlich irgendeine Wissenschaftskarriere einschlagen."


show lilly cane_smileclosed_close onlayer master
with charachange

li "Das freut mich zu hören, Hisao."


scene bg school_gardens onlayer master at bgleft
with locationchange

stop music fadeout 0.3
with vpunch

"Als wir durch die Gärten gehen, klopft mir plötzlich jemand ungefragt auf den Rücken."


"Der in Grün gekleidete Täter baut sich vor mir auf und schenkt Lilly neben mir offenbar keine Beachtung."


play music music_kenji fadein 0.5

show kenji neutral onlayer master:
    center
    xpos 0.55
    easein 0.5 center
with charaenter

ke "Hey Mann, was geht? Hab dich 'ne Weile nicht gesehen."


hi "Hey. Ich war in letzter Zeit nur mit Prüfungen und so beschäftigt."


show kenji tsun onlayer master at center
with charachange

ke "Ach was, Prüfungen… Ein wahrer Mann der Renaissance braucht nicht zu lernen, um bei so was überragend zu sein."


"Kenji macht auf mich den Eindruck, als gehöre er zu den Leuten, die auch mit furchtbarer Anwesenheitsquote und dürftiger Arbeitsmoral gut in der Schule sind. Daher habe ich kaum Grund, seine Fähigkeiten anzuzweifeln."


"Um ehrlich zu sein, ich bin etwas neidisch auf ihn; zwischen dem Lernen für die Prüfungen und meiner Zeit mit Lilly hatte ich praktisch kaum Zeit für mich selbst. Vielleicht ist es ein bisschen so, wie sich Yuuko fühlen muss."


show kenji tsun onlayer master at tworight
show bg school_gardens onlayer master at center
with charamove

show lilly cane_smile_close onlayer master at twoleft
with charaenter

li "Guten Morgen, Setou. Schön zu hören, dass es dir gutgeht."


"Es wirkt etwas seltsam, Lilly so förmlich sprechen zu hören. Über die Monate hat sie mich immer lockerer angesprochen, allerdings habe ich von Zeit zu Zeit auch gesehen, wie sie mit ihren Klassenkameraden förmlicher spricht."


"Manche Menschen ändern sich nie, schätze ich. Ich will damit nicht sagen, dass ihr ruhiges und höfliches Verhalten etwas Schlechtes ist; schließlich ist es einer der Gründe, aus denen ich überhaupt gerne in ihrer Nähe bin."


"Kenji scheint einen Moment zu brauchen, um zu erkennen, wer neben mir steht. Und wahrscheinlich hat er auch nicht bemerkt, dass wir uns an den Händen halten. Bringt seine Brille überhaupt etwas?"


show kenji neutral onlayer master at tworight
with charachange

ke "Oh, hey Lilly. Dir auch viel Glück bei den Prüfungen."


show kenji tsun onlayer master at tworight
with charachange

ke "Ich seh dich dann nach der Schule, Mann."


"Die leichte Bestimmtheit seiner Stimme lässt mich denken, dass diese Worte eher ein Befehl als ein lässiger Abschied sein sollten. Ich schätze, nachher muss ich die Dinge wieder ins Lot bringen."


hi "Klar. Mach's gut."




show kenji invis onlayer master:
    xpos 0.6
with dissolvecharamove

hide kenji onlayer master
with None

"Kenji nickt kurz. Er zieht an uns vorbei, aber er ist zu beschäftigt damit, böse in Lillys Richtung zu starren, um ihren Blindenstock zu bemerken."


show lilly cane_surprised_close onlayer master at twoleft
with charachange

"Bevor ich auch nur reagieren und die Situation retten kann, stolpert Kenji und versucht reflexartig, sich an etwas festzuhalten. Unglücklicherweise ist Lillys Arm das Erste, was er zu greifen bekommt."


show lilly cane_surprised_close onlayer master:
    easeout 0.3 ypos 1.2 alpha 0.0
with Pause(0.5)

play sound sfx_pillow
hide lilly onlayer master
with vpunch

$ doublespeak(ke,li,"Whoa!", "Ah!")


"Beide stürzen zu Boden und liegen mit ausgestreckten Gliedmaßen auf einem Haufen, während ich recht hilflos daneben stehe."


hi "Ah, verdammt. Seid ihr Zwei okay?"


show kenji invis onlayer master:
    center
    ypos 1.2
with None

show kenji neutral onlayer master:
    ypos 1.0
with dissolvecharamove

"Kenji kommt schnell wieder auf seine Füße und ist anscheinend unbeeindruckt von dem Unfall."


ke "Kein Problem, Mann, kein Problem. Das ist nichts, mein Körper kann viel schlimmere Misshandlungen ertragen."


"Lilly liegt mit dem Gesicht nach unten auf dem Rasen. Sie sieht nicht verletzt aus, eher erschrocken. Ich nähere mich, um ihr meine Hilfe anzubieten."


hi "Bist du in Ordnung, Lilly?"


show kenji happy onlayer master
with charachange

ke "Hey, Satou?"


"Kenji bietet ihr eine Hand an und berührt ihre vorsichtig, um sie wissen zu lassen, was er vorhat."


"Manchmal sagt er echt abscheuliche Dinge, aber ich denke, im Herzen könnte er doch ein aufrichtig guter Mensch sein. Ich kann mir denken, dass ihm das hier ziemlich leidtut."


stop music fadeout 2.0

"Aber zu meiner und seiner Überraschung schlägt Lilly ohne Vorwarnung ihre Faust auf den Boden."


play sound sfx_impact
with vpunch

li "Verdammt!"


show kenji tsun onlayer master
with charachange

"Kenji erstarrt und ist von ihrem Ausbruch völlig überrumpelt. Ich bin genauso schockiert; sie hat sich noch nie zuvor so verhalten, nicht einmal bei Shizune."


ke "Äh…"


show lilly invis_close onlayer master:
    twoleft
    ypos 1.2
with None
show lilly cane_mad_close onlayer master at twoleft

with dissolvecharamove

"Sie rappelt sich langsam auf und erinnert sich anscheinend erst jetzt, dass Menschen um sie herum stehen. Ihr Gesicht dabei lässt mich etwas zurückweichen."


show lilly back_listen_close onlayer master
show lillyprop back_cane_close onlayer master at twoleft
with charachange

"Ich erhasche nur einen kurzen Blick, bevor sie sich abwendet, aber es ist ein Anblick, den ich nicht so schnell vergessen werde."


"Sie hat oft ihre Verärgerung zur Schau gestellt, wenn sie sich mit Shizune in den Haaren hatte, doch dieser aufblitzende Zorn war etwas anderes. Es ist unmöglich, dass das nur an diesem unbedeutenden Zwischenfall lag."


hide lilly onlayer master
hide lillyprop onlayer master
with charaexit

"Sie hält einen Moment inne, dann seufzt sie und läuft weiter geradeaus. Ich weiß nicht recht, was ich davon halten soll."


hi "Wir… äh… reden dann später, Alter. Bis dann."


ke "Jepp, bis dann."


hide kenji onlayer master
with charaexit

"Kenji kratzt sich am Hinterkopf und versucht, die passenden Worte zu finden. Dann zuckt er mit den Schultern und zieht davon, wobei er einen großen Bogen um uns macht."


show bg school_gardens onlayer master at right
with charamove

show lilly back_listen onlayer master at center
show lillyprop back_cane onlayer master at center
with charaenter

"Rasch habe ich Lilly eingeholt. Sie dreht ihren Kopf etwas, um meine Gegenwart anzuerkennen, mehr aber auch nicht."


"Ich sollte sie wahrscheinlich dafür tadeln, so ausfallend zu werden. Aber ich will auch keinen Streit mit ihr anfangen. Sie ist offensichtlich immer noch genervt."


"Im Endeffekt halte ich einfach den Rand und warte, bis sie sich etwas beruhigt."


scene bg school_hallway3 onlayer master
with shorttimeskip

"So laufen wir schweigend nebeneinander her und erreichen schließlich das obere Ende der Treppen im dritten Stock – und damit auch die Stelle, an der wir uns jeden Tag trennen müssen."


show lilly cane_listen_close onlayer master at center
with charaenter

"Ich drehe mich zu Lilly, bevor sie geht. Obwohl ich die angenehmen stillen Momente mag, die wir sonst teilen, war dies alles andere als das. Ich will mich nicht so verabschieden."


hi "Du scheinst… in letzter Zeit ruhiger als sonst zu sein. Stimmt irgendwas nicht?"


show lilly cane_displeased_close onlayer master
with charachange

"Sie schüttelt fast automatisch ihren Kopf, als wollte sie um jeden Preis verhindern, dass ich mir um sie Sorgen mache."


li "Die Prüfungen machen mir nur zu schaffen. Es geht schon."


"Ich denke nicht, dass das der Grund ist. Fast spreche ich es aus, entscheide mich aber doch noch dagegen. Es bringt nichts, es ihr aus der Nase ziehen zu wollen, wenn sie es mir nicht erzählen will – besonders nicht, wenn sie so eine miese Laune hat."


hi "Wenn du dir sicher bist… Ich sehe dich dann später."


hide lilly onlayer master
with charaexit

"Als ich mich umdrehe und den Gang zu meinem Klassenzimmer entlanglaufe, erklingt Lillys sanfte Stimme hinter mir."


show lilly cane_concerned onlayer master
with charaenter

li "Hisao, ähm…"


hi "Ja?"


li "…"


li "Es tut mir leid."


hide lilly onlayer master
with charaexit



"Daraufhin macht sich Lilly auf den Weg zu ihrem eigenen Klassenzimmer, wobei sie ihre Hand an dem Metallhandlauf entlangfahren lässt."


"Ich stehe still da und sehe ihr nach, bis sie in ihrem Klassenzimmer und damit aus meinem Sichtfeld verschwindet. Mit einem gewissen Maß an Widerwillen gehe ich dann zu meiner eigenen Klasse."


scene bg school_scienceroom onlayer master at left
with locationchange

play music music_normal fadein 4.0

"Wie üblich bin ich früh dran. Mutou geht die Ordner und Blätter auf seinem Schreibtisch durch, als er sich auf den Tag vorbereitet. Eine Handvoll Schüler sind schon da und plaudern."


"Meine Bedenken wegen Lilly sind zwar noch nicht verflogen – noch lange nicht – aber dass sie meine Prüfungsleistungen erwähnt hat, erinnert mich daran, dass ich meinen eigenen Lebensweg vor mir habe."


"Ich habe viel darüber nachgedacht und bin zu dem Schluss gekommen, dass ich wirklich einer Wissenschaftskarriere nachgehen will – und das nicht nur als Weg des geringsten Widerstandes."


"Aber bis jetzt hatte ich kaum eine Ahnung, in welches Gebiet ich gehen will. „Wissenschaft” hat ziemlich viele Tätigkeitsfelder."


"Etwas, das Lilly neulich erwähnt hat, hat mich darauf gebracht. Etwas, worüber ich zuvor nur sehr träge nachgedacht habe, weil ich nie wirklich in Betracht gezogen hatte, diesen speziellen Weg zu gehen."


show bg school_scienceroom onlayer master at right
with charamove

"Ich gehe zu Mutous Schreibtisch. Mutou ist immer noch zu sehr auf seine Tagesvorbereitungen konzentriert, um mein Näherkommen zu bemerken. Es ist wie jeden Tag."


hi "Guten Morgen."


show muto normal onlayer master at center
with charaenter

"Er schaut mit einem leicht überraschten Gesichtsausdruck auf, der schnell von seinem typischen, linkischen Lächeln ersetzt wird."


show muto smile onlayer master
with charachange

mu "Guten Morgen, Nakai. Kann ich dir helfen?"


hi "Dürfte ich Sie etwas fragen?"


"Er sieht hinab auf den unordentlichen Bücherstapel auf seinem Schreibtisch, bevor er die Papiere in seinen Händen hinlegt und etwas umständlich aufsteht, um sich angemessen mit mir zu unterhalten."


mu "Dafür bin ich doch schließlich da. Nur zu."


hi "Ich hab mich nur gefragt… Was motiviert jemanden dazu, Lehrer zu werden?"


"Er denkt über diese Frage ein paar Augenblicke nach, bevor er antwortet. Offenbar hat er keine Antwort parat."


show muto normal onlayer master
with charachange

mu "Wenn du das zehn verschiedene Lehrer fragst, bekommst du bestimmt zehn verschiedene Antworten darauf."


mu "Ich kann zwar nur von mir selbst sprechen, aber ich denke, ich unterrichte, weil… hmm…"


"Er versinkt wieder in Gedanken und wägt vorsichtig ab, wie er mir seine Vorstellung erläutern will."


show muto smile onlayer master
with charachange

mu "Stell es dir so vor: Als du ein Kind warst, hast du wahrscheinlich mit Stöcken und Kieselsteinen im fließendem Wasser gespielt – in Regenrinnen oder Pfützen, richtig?"


hi "Ja. Ich glaube, eine Menge Leute machen das, wenn sie jung sind."


show muto normal onlayer master
with charachange

mu "Nun, manche nicht nur, wenn sie jung sind, allerdings nimmt es eine andere Form an. Was ich damit aber sagen will ist, dass wenn jemand das tut, dann ist er neugierig darüber, wie das Wasser fließen oder sich verändern wird."


mu "Jeder, sogar in diesem jungen Alter, besitzt eine starke Neugier, wie die Welt um einen herum funktioniert, auch wenn es nur die kleinsten Dinge sind."


mu "Ich spüre immer noch diese Neugier auf das Universum."
mu "Einfach nur über neue Entdeckungen oder klassische Experimente zu lesen, führt mir immer wieder vor Augen, wie erstaunlich und wundervoll doch alles ist. Von den entferntesten Sternen bis zur kleinsten Pfütze."


show muto smile onlayer master
with charachange

mu "Ich hoffe nur, dass ich anderen wenigstens ein kleines Stück meiner Neugier abgeben kann. Wenn ich das tun kann, auch wenn es nur für einen Menschen ist, denke ich, dass ich als Lehrer sehr zufrieden sein kann."


"Er kratzt sich am Kopf, während er mental noch einmal durchgeht, was er gerade gesagt hat."


"Ich glaube, ich verstehe ihn jetzt besser. Auch wenn er in der Nähe anderer unbeholfen ist, so hat er doch ein aufrichtiges Bedürfnis, bei ihnen zu sein und ihnen ein Stück seiner Selbst anzubieten, das ihm so wichtig ist."


"Was Lilly mir gestern gesagt hat, klingt in meinen Ohren. „Du kommst fabelhaft mit anderen aus”, was? Sie hat immer gesagt, dass ich ungewöhnlich neugierig bin…"


show muto normal onlayer master
with charachange

mu "Entschuldige, falls ich etwas abgeschweift bin. Hat das deine Frage beantwortet?"


hi "Hat es, vielen Dank."


hi "Eigentlich hatte ich noch eine weitere Frage."


mu "Oh? Und die wäre?"


hi "Ähm… Haben Sie irgendwelche Universitätsbroschüren oder Studienführer? Es wird langsam Zeit, dass ich einige Bewerbungen rausschicke."


"Er nickt und beugt sich nach unten, um in seinem Schreibtisch nachzusehen. Als er das tut, bemerke ich, dass sein Lächeln gerade bemerkenswert authentisch ist. Ich glaube nicht, dass ich ihn je so natürlich in der Nähe anderer gesehen habe."


"Vielleicht ist dies nicht Mutou der Lehrer, sondern eher Mutou der Mensch."


show muto smile onlayer master
with charachange

mu "Hier. Falls du mehr brauchst, kannst du mich jederzeit fragen."


"Er reicht mir ein halbes Dutzend Broschüren und Hefte in verschiedenen Farben und Größen, die ich begierig annehme."


"Ja, es wird diese Information sein, aus der ich meine eigene Zukunft schmieden werde. Ich glaube jetzt, nach all dieser Zeit und all diesen Herausforderungen, kann ich endlich mein zukünftiges Leben vor mir sehen."


"Mein Körper mag eine Sache sein, aber mein Verstand ist immer noch gesund."


hi "Ich danke Ihnen."


stop music fadeout 2.0

scene black onlayer master
with dissolve

$ suppress_window_after_timeskip = True



label de_L26:

window hide None

scene black onlayer master
with dissolve

nvl clear
nvl show dissolve

n "\n\n„Das ist seltsam.”"


play music music_pearly fadein 5.0

$ ksgallery_unlock("evul hisao_teacup")
show ev hisao_teacup onlayer master:
    truecenter
    alpha 0.0 subpixel True
    linear 30.0 alpha 0.5
with None

n "\n\nDieser eine Gedanke schoss mir unzählige Male durch den Kopf, seit mein Leben hier begann."


n "Es scheint ein einfacher Weg zu sein, um einer problematischen Frage auszuweichen. Als würde man mit diesen drei Worten etwas verscheuchen oder zumindest nicht mehr so oft daran denken müssen."


n "Mein Leben vor meiner Herzattacke ist jedes Mal verschwommener, wenn ich versuche, mich daran zu erinnern, und mein Verstand kämpft, um mit all den plötzlichen Geschehnissen seither mitzuhalten."


n "Ich hörte irgendwo, dass es sich so anfühlt, wenn man in einem Land gestrandet ist, in dem man die nur die Grundlagen der örtlichen Sprache beherrscht."


n "Tatsächlich scheint es, wenn ich darüber nachdenke, wie eine wunderbare Analogie für das, was mir passiert ist."


nvl clear

n "\n\nJedoch soll man in solchen Situationen auch in kürzester Zeit extrem viel von dieser Sprache lernen, da man gezwungen ist, sie zu lernen, um zu überleben. Mit anderen Worten, entweder man lernt zu schwimmen oder man geht unter."


n "\nIch frage mich, ob ich es nach all dieser Zeit wirklich geschafft habe zu schwimmen."


n "Die Prüfungen stressen mich sehr, auch wenn sie jetzt endlich zu einem Ende kommen, aber ich bin in Mutous Gunst geblieben, und ich habe nun eine Art Ziel für meine Zukunft."


n "Aber ich benutze immer noch diese dumme, bedeutungslose Phrase."


n "\n\n„Das ist seltsam.”"


nvl clear

n "\n\nEs ist wirklich erstaunlich, wie schnell man es akzeptiert, von Leuten mit manchmal unglaublich kuriosen Behinderungen und Leiden umgeben zu sein."


n "So sehr, dass ich mich wirklich frage, warum ich mich so sehr wie ein Außenseiter fühle."


n "\nUnd das liegt bestimmt nicht an Mangel an sozialen Kontakten oder Freunden. Die meisten meiner Klassenkameraden kann ich mittlerweile mit ihrem Vornamen ansprechen, und ich kenne vereinzelt Leute auf der ganzen Schule."
n "\nOb ihnen ein Arm oder ein Bein fehlt – die Schüler hier sind genau wie alle anderen in ihrem Alter."


n "Dank des ausgeklügelten Schulaufbaus finde ich mich ohne Probleme in den Gängen zurecht, in denen ich mich einst noch verlaufen habe – und das mit einer Leichtigkeit, die ich nie für möglich gehalten hätte. Ich kann mich sogar problemlos mit meinen Lehrern unterhalten."


nvl clear
nvl hide dissolve

scene ev hisao_teacup onlayer master:
    truecenter
    zoom 1.0 subpixel True alpha 1.0
    acdc_warp 20.0 zoom 0.8
with locationchange

window show

"Gemächlich rühre ich meinen Tee um, wobei die Reflektion meines Gesichts in der sich bewegenden Flüssigkeit verzerrt wird. "


"Das ist seltsam… Früher habe ich das Teetrinken gehasst."


hi "Vielleicht mache ich mir zu viele Gedanken."


play sound sfx_teacup

"Es ertönt das vertraute Geräusch von klirrendem Porzellan einer Teetasse, die auf einer Untertasse abgestellt wird."


li "Bereitet dir etwas Sorgen?"


hi "Keine Sorge, es ist nichts."


scene bg school_dormlilly onlayer master
show hanagown normal onlayer master:
    tworight
    ypos 1.15
show lilly basic_smileclosed_paj onlayer master:
    twoleft
    ypos 1.2
with whiteout

"Ich tue es den Mädchen gleich und nehme einen langen Schluck von meinem Tee."


"Sich einfach nur die Zeit damit vertreiben, in Lillys Zimmer mit ihr und Hanako Tee zu trinken… Es fühlt sich vertraut an, fast nostalgisch."


hi "Also, wie läuft's mit deiner Arbeit für die Schülerzeitung, Hanako?"


show lilly basic_satisfied_paj onlayer master
with charachange

li "Das möchte ich auch wissen. Es klingt, als wäre es ziemlich interessant."


show hanagown distant onlayer master
with charachange

"Hanako senkt wegen der auf sie gerichteten Aufmerksamkeit ihren Blick, auch wenn ihr Lächeln preisgibt, dass sie in Wahrheit gerne das Zentrum unserer beider Aufmerksamkeit ist."


ha "Es… läuft gut. Ich denke, ich werde langsam besser darin."


ha "Naomi und ein paar ihrer Freunde machen die meiste Arbeit… Storys beschaffen und so."


show hanagown smile onlayer master
with charachange

ha "Ich kümmere mich nur um die Computerangelegenheiten. Zum Beispiel die Storys zusammenführen und sie ausdrucken. Es… es macht Spaß, da ich sitzen und mich konzentrieren kann."


"Es sieht aus, als ob Hanako nicht solche Probleme mit moderner Technik hat wie Lilly."
"In einem Raum zu sitzen und die Zeitungsartikel anderer Leute zu formatieren, ist sicher nicht die kontaktfreudigste Tätigkeit, aber es ist ermutigend zu hören, dass sie ihren Freundeskreis erweitert."


"Kleine Schritte, schätze ich. Es wäre wahrscheinlich übertrieben zu erwarten, dass sie so ein Gesellschaftslöwe wie Lilly wird."


show lilly basic_oops_paj onlayer master
with charachange

li "Was hältst du von Naomi? Ich habe gehört, dass sie manchmal ziemlichen Ärger machen kann."


"Und Lilly verfällt wieder in ihren Muttermodus. Sie ziehen zu lassen, ist etwas, was sie noch lernen muss."


show hanagown worry onlayer master
with charachange

"Hanako kratzt sich an der Wange und überlegt sich eine Antwort."


show hanagown smile onlayer master
with charachange

ha "Naomi ist… nett. Sie ist manchmal etwas laut und etwas anstrengend… aber sie ist echt hilfsbereit. Ihre Freunde sind auch nett."


show lilly basic_cheerful_paj onlayer master
with charachange

li "Das zu hören, ist wundervoll, Hanako. Ich freue mich, dass du etwas gefunden hast, das dir so viel Spaß macht."


"Lillys Lächeln ist warm und aufrichtig, doch ich kann auch einen Hauch von Wehmut darin erkennen. Hanako scheint das vollkommen zu entgehen, aber ich glaube keine Sekunde, dass ich mir das nur einbilde."


"Das liegt vermutlich daran, dass ich langsam anfange, allem um mich herum mehr Aufmerksamkeit zu schenken."
"Mit den scheinbar immer schneller aufeinander folgenden Geschehnissen kommt es mir so vor, als würde ich etwas verpassen, wenn ich nicht so wachsam wie möglich bin."


"In letzter Zeit war ich ziemlich im Stress."
"Kein Wunder bei den Prüfungen, meinem neuen Liebesleben, dem Ausloten von verschiedenen Optionen für Universitäten… und natürlich meinem Herzen, das mir immer dann einen Knüppel zwischen die Beine wirft, wenn ich es nicht erwarte."


"Dadurch weiß ich die seltenen, ruhigen Momente wie diesen zu schätzen."


"Ich schätze deswegen hat Lilly ihre wöchentlichen Spaziergänge zum Mini-Markt und ihre Teepartys mit Hanako zu würdigen gelernt hat, obwohl sie gerne von anderen umgeben ist."
"Sie gaben ihr in ihrem chaotischen und vielbeschäftigten Leben einen Moment der Ruhe."


hi "Gott sei Dank sind die Prüfungen vorbei, was?"


show lilly basic_giggle_paj onlayer master
with charachange

"Mein Kommentar entlockt den Mädchen ein aufrichtiges Schmunzeln. Es scheint, als wären seit dem Ende der Prüfung letzte Woche alle viel fröhlicher."



hi "Und was machst du über die Sommerferien, Hanako? Immerhin…"


"Fix zähle ich in meinem Kopf die Tage. Heute ist Montag, und die Schule endet am Samstag…"


hi "… sind es nur noch fünf Tage."


show hanagown normal onlayer master
with charachange

ha "Ich dachte daran zu… verreisen. Nur etwas… herumkommen."


show hanagown smile onlayer master
with charachange

ha "Es gibt viele Orte, die ich sehen will, und… ich denke, ich habe genug Geld, um den Bus und die Zugfahrten zu bezahlen. Naomi und eins der anderen Mädchen von der Schülerzeitung meinten, dass sie vielleicht auch mitkommen."


"Ihr Blick deutet darauf hin, dass sie ziemlich viel darüber nachgedacht hat. Ich bin irgendwie überrascht, dass sie so etwas in Erwägung zieht."


"Anscheinend hat sie wirklich vor, selbständiger zu werden."


show lilly basic_smile_paj onlayer master
with charachange

li "Gibt es irgendeinen besonderen Ort, zu dem du fahren willst?"


show hanagown distant_blush onlayer master
with charachange

ha "Ich dachte mir, dass… Kyoto ganz nett wäre. A-Aber ich glaube, ich werde versuchen, mehrere Orte zu besuchen."


show lilly basic_cheerful_paj onlayer master
with charachange

"Zufrieden mit Hanakos Plänen nickt Lilly anerkennend."


"Meine Augen sind zwar auf Lilly gerichtet, aber ich vermeide es, ihr die gleiche Frage zu stellen. Sie ist der Frage über ihre Zukunftspläne schon lange ausgewichen, aber ich finde keine gute Gelegenheit, um das Thema mit ihr allein anzusprechen."


"Jedes Mal, wenn unsere Unterhaltung in diese Richtung geht, kommt es mir vor, als wäre sie sich selbst unsicher oder als würde sie der Frage ausweichen. Es ist beunruhigend."


hi "Ruf auf jeden Fall mal an, wenn du unterwegs bist. Meine Nummer habe ich dir gegeben, oder?"


show hanagown smile onlayer master
with charachange

"Hanako nickt mit einem glücklichen Lächeln auf ihrem Gesicht."


"Es ist seltsam zu sehen, wie Menschen glücklich werden, wenn sie ein Ziel haben, auf das sie hinarbeiten können. Yuuko scheint zu strahlen, wann immer ihre Universitätsplanungen erwähnt werden, und mit Hanako ist es genau das Gleiche."


"Also warum empfinde ich diese Unsicherheit? Und warum Lilly auch?"


"Beziehungen können manchmal äußerst Mühsam sein."


show hanagown worry onlayer master
with charachange

ha "Oh… äh… Wi-wie spät ist es?"


hi "Hmm? Oh…"


"Ich brauche eine Sekunde, um mich daran zu erinnern, dass Lillys Uhr weder Zeiger noch ein Display hat. So oft wie ich schon in ihrem Zimmer gewesen bin, sollte ich das langsam wirklich wissen."



"Nichtsdestotrotz nehme ich meine Armbanduhr aus meiner Tasche und schaue schnell nach. Warum sie gefragt hat, wird mir schnell klar."


hi "Es ist ungefähr zwanzig nach zehn. Fast Ausgangssperre."


show hanagown normal onlayer master:
    ypos 1.0
with dissolvecharamove

"Hanako steht auf, klopft sich ab und richtet danach ihr Nachthemd."


show hanagown smile onlayer master
with charachange

ha "Ich… gehe dann besser mal. Gute Nacht Lilly, Hisao."


stop music fadeout 5.0

show lilly basic_smileclosed_paj onlayer master
with charachange

li "Schlaf gut, Hanako."


hi "Bis morgen."


hide hanagown onlayer master
with dissolve

"Daraufhin läuft sie zur Tür und verlässt leise das Zimmer."


show lilly basic_smileclosed_paj onlayer master:
    xpos 0.5
show bg school_dormlilly onlayer master at bgright
with charamove

"…"


"Stille."


"In letzter Zeit scheint das zwischen Lilly und mir immer öfter vorzukommen. Nach ein paar Sekunden finde ich endlich etwas, worüber wir reden können."


play music music_another fadein 4.0

hi "Ah ja, ich habe am Freitag mit Mutou gesprochen, und mir endlich ein paar Bewerbungstipps für Universitäten angesehen."


show lilly basic_smile_paj onlayer master
with charachange

li "Das sind gute Neuigkeiten. Wenn du dich für Universitäten bewerben willst, nehme ich an, dass du eine Vorstellung davon hast, was du in Zukunft machen willst?"


hi "Ich denke, ich habe mich dazu entschlossen, Naturwissenschaftslehrer zu werden. Es wird eine Weile dauern, durch die Universität zu kommen und mich dafür zu qualifizieren, aber ich denke, das wird es wert sein."


show lilly basic_satisfied_paj onlayer master
with charachange

"Lillys Gesicht erhellt sich bei diesen Neuigkeiten erheblich. Ich vermute, da sie selbst Lehrerin werden will, ist sie erfreut darüber, dass ich eine ähnliche Laufbahn einschlage."


li "Also hast du dich für eine Karriere als Lehrer entschieden…"


show lilly basic_smile_paj onlayer master
with charachange

li "Ich denke, dass diese Laufbahn hervorragend zu dir passt, Hisao."


"Ich lächle und nicke. Ich weiß zwar, dass sie es nicht sehen kann, aber dieses Mal bin mir sicher, dass sie es spürt."


show lilly basic_planned_paj onlayer master
with charachange

li "Ich nehme an, dass Mutou sich auch darüber gefreut hat?"


hi "So kann man es auch sagen."


hi "Hey, Lilly?"


show lilly basic_smile_paj onlayer master
with charachange

li "Ja?"


hi "Ich weiß, du willst Lehrerin werden, aber…"


"Für einen Augenblick frage ich mich, ob ich ihr wirklich die Frage stellen sollte, die mir auf dem Herzen liegt, aber da es für diese Bedenken nun eh schon zu spät ist, ziehe ich es durch."


show lilly basic_smileclosed_paj onlayer master
with charachange

li "Du denkst doch wohl nicht immer noch, dass ich wegen Fragen über meine Blindheit beleidigt sein könnte."


"Ihr Grinsen verrät mir, dass ihr vorwurfsvoller Ton nicht ernst gemeint ist. Anscheinend amüsiert es sie immer noch, dass mir das Thema so unangenehm ist. Manche Dinge ändern sich nie."


hi "Da hast du wohl Recht."


hi "Ich hab mich nur gefragt, ob blind zu sein nicht ein Hindernis wäre – wo du doch Lehrerin werden willst und so…"


show lilly basic_surprised_paj onlayer master
with charachange

"Sie sieht leicht überrascht aus und denkt eine Weile über diese Frage nach. Ich weigere mich zu glauben, dass sie noch nie über diesen Aspekt nachgedacht hat."


show lilly basic_emb_paj onlayer master
with charachange

li "Ich frage mich… Hisao, könntest du für einen Moment deine Augen schließen?"


hi "O… kay?"


"Ihr hebe eine Augenbraue und tue, worum sie mich bittet."


$ renpy.music.set_volume(0.5, 2.0, channel="music")

scene black onlayer master
with shuteye

"Ich habe keine Ahnung, was sie vorhat, und meine Fragen werden nur noch mehr, als ich heimlich ein Auge öffne."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

show bg school_dormlilly onlayer master at bgright
show lilly basic_smileclosed_paj_close onlayer master at center
with openeye

"Sie holt die schwarze Schleife, die sie üblicherweise in ihren Haaren trägt, aus dem Schrank neben ihrem Bett und kommt wieder zu mir, während sie mit ihrer Hand darüber fährt, um übriggebliebene Haare aus dem Stoff zu entfernen."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene black onlayer master
with softwipedown

"Plötzlich werden mir ihre Absichten klar, als ich spüre, wie der schwarze Streifen in Berührung mit meinem Gesicht kommt und um meinen Kopf und meine Augen gewickelt wird."


hi "Äh… wofür genau brauchst du die denn?"


li "Ein kleiner Test, Hisao. Da du ja neugierig zu sein scheinst, werde ich dich die Dinge eine Zeit lang aus meiner Perspektive sehen lassen."


"Aha, darum geht es also."


"Um ehrlich zu sein, klingt das eigentlich irgendwie nach Spaß. Kindisch und eher albern für alle, die zusehen würden, aber ein bisschen alberner Spaß hat noch niemandem geschadet."


"Ich stehe mit Schwung auf und halte meine Hände schnell voraus, um etwaige Hindernisse zu ertasten."


hi "Okay, was jetzt?"


li "Berühr mich."


hi "Wenn du das sagst. Also dann…"


"Langsam bewege ich mich vorwärts in Richtung Lillys Stimme."


"Meine Schrittgeschwindigkeit kann nicht einmal mehr ein Schlurfen genannt werden."
"Die gesamte Situation ist befremdlich genug, dass ich nicht riskieren will, versehentlich über etwas zu stolpern – wie zum Beispiel ihren Tisch oder die willkürlichen Bücherstapel."


play sound sfx_rustling

"Etwas Weiches und dennoch Festes streift mein linkes Bein. Bei genauerer Überlegung muss es Lillys Bett sein."


"Ich laufe weiter und bin dabei dankbar, dass Lillys Zimmer so sauber und aufgeräumt ist. Sogar ihre Bücherstapel sind in der Regel nah an der Wand und damit so gut wie ungefährlich."


play sound sfx_pillow

"Die harte Wand, die meine ausgestreckten Hände begrüßt, lässt mich frustriert meine Augenbrauen zusammenkneifen."


hi "Hey Lilly, wo bist du?"


li "Was machst du dort drüben? Ich bin hier."


"Lillys Stimme kommt von der anderen Seite des Zimmers, weit entfernt von dem Punkt, an dem sie vorher war – sogar meine untrainierten Ohren hören das. Wenn sie versucht zu verhindern, dass ich sie erreiche, ist das dann nur ein Spiel für sie?"


"… Natürlich ist es das. Verglichen mit einem Leben, in dem das Konzept des Sehens etwas Abstraktes ist, sind ein paar Minuten mit einer Augenbinde gar nichts."


"Ich schätze, sie hat ihren Standpunkt klargemacht. Sie ist sehr wohl in der Lage, sich in ihrem Zimmer umherzubewegen, und außerdem habe ich gesehen, wie unabhängig sie ist – sogar verglichen mit vielen anderen an der Yamaku."


"Na ja, auch wenn es nur ein Spiel ist, kann ich genauso gut aufs Ganze gehen."


"Mit viel höherem Tempo als vorher bewege ich mich zum Ursprung ihrer Stimme, während ich dabei geschickt den Tisch in der Mitte des Raumes umgehe."


hi "Jetzt hab ich dich!"


"Sie gibt ein schelmisches Kichern von sich. Gerade lang genug, dass ich mitkriege, dass sie direkt an mir vorbeiläuft."


play sound sfx_impact2
with vpunch

"Rasch drehe ich mich in die neue Richt- Der Tisch war eben noch nicht hier!"


hi "Au… Au… Au…"


$ renpy.music.set_volume(1.0, 1.0, channel="music")

show bg school_dormlilly onlayer master
with softwipeup

"Langsam richte ich mich neben dem Tisch auf und hebe die Augenbinde an, während ich meinen schmerzenden Kopf reibe."


play sound sfx_impact
with vpunch

"Ich verpasse dem Tisch, der genau vor der Stelle steht, an der ich hingefallen bin, einen wütenden Tritt. Vollkommen sinnlos, aber das Ding hat es verdient."


show lilly basic_oops_paj_close onlayer master at center
with charaenter

li "Hisao?"


"Lilly steht immer noch direkt neben mir und ist sich offenbar nicht im Klaren, was gerade passiert ist."


hi "Sorry. Ich bin irgendwie hingefallen."


show lilly basic_concerned_paj_close onlayer master
with charachange

li "Bist du verletzt?"


hi "Mein Kopf tut weh, aber ich denke, ich bin okay. Ich glaube, der Tisch hat sich bewegt, um mich zum Stolpern zu bringen."


show lilly basic_giggle_paj_close onlayer master:
    ypos 1.1
with dissolvecharamove

"Sie kichert, während sie zu mir kommt und sich neben mich setzt. Dabei legt sie ihre Hand auf meine."


show lilly basic_weaksmile_paj_close onlayer master
with charachange

li "Ich vermute, dann hören wir jetzt damit auf?"


hi "Ich denke ja."


hi "Aber ich denke auch, dass ich verstehe, was du mir damit zeigen wolltest. Auch wenn ich es lieber ohne diese Kopfschmerzen gehabt hätte."


show lilly basic_surprised_paj_close onlayer master
with charachange

"Plötzlich schaut Lilly verwirrt drein."


li "Was zeigen?"


"Und nun tue ich es ihr gleich."


hi "Das war nur zum Spaß?"


show lilly basic_reminisce_paj_close onlayer master
with charachange

li "Ich dachte, das würde dich das Thema etwas lockerer sehen lassen. Schließlich scheinst du immer drumherumzureden."


show lilly basic_smileclosed_paj_close onlayer master
with charachange

li "Wenn es ums Unterrichten geht, ist Sehen nicht so wichtig. Es gibt viele Kurse, die von vollkommen blinden Lehrern gelehrt werden, und mehr als genug Ressourcen, um mir das Fach anzueignen."


show lilly basic_smile_paj_close onlayer master
with charachange

li "Es ist wirklich so simpel."


"Ich lasse meine Schultern hängen und schnaufe belustigt."


hi "Ja, ich verstehe. Ich schätze, wir beide müssen dann einfach nur hart arbeiten, um unsere Ziele zu erreichen."


stop music fadeout 4.0

show lilly basic_cheerful_paj_close onlayer master
with charachange

li "Hmm…"


hi "Was denn?"


"Mit einem kleinen Zögern schiebt Lilly ihr Kinn nach vorne und schließt ihre Augen. Eine unverkennbare Geste."


scene ev lilly_kissing onlayer master
with whiteout

play music music_one fadein 1.0

"Ich nehme mit Freuden an, und unsere Lippen berühren sich. Währenddessen spüre ich, wie ihre Hand unter meinem Hemd meine Brust hinauffährt. Das Gefühl ihrer Hand auf meiner nackten Haut ist genug, um mein Herz plötzlich rasen zu lassen."


"Ist sie wieder in Stimmung?"


"Nun, ich würde mich deswegen wohl kaum beschweren. Ihr gefällt es wirklich, und glücklicherweise ist meine Libido trotz all meiner Medikamente noch intakt."


"Ich vertiefe meinen Kuss und halte fest ihre Hand, als ich spüre, wie sie die Konturen meiner Brust entlangfährt."


scene bg school_dormlilly onlayer master
show lilly basic_smileclosed_paj_close onlayer master:
    center
    ypos 1.1
with whiteout

"Schließlich lösen wir uns voneinander, und der Raum ist nur von dem Geräusch unserer Atmung erfüllt."


show lilly basic_surprised_paj_close onlayer master
with charachange

li "Hey, Hisao?"


hi "Ja?"


show lilly basic_emb_paj_close onlayer master
with charachange

li "Ich nehme nicht an… dass du die Augenbinde noch einmal aufsetzen würdest?"


"Ihr zögernder Vorschlag überrascht mich."


"Vermutlich will sie mich Sex ebenfalls durch ihre Augen sehen lassen. Oder sie will einfach herausfinden, wie ich mich während des Aktes verhalte, wenn ich durch die Augenbinde behindert bin."


$ renpy.music.set_volume(0.5, 0.0, channel="music")


scene black onlayer master
with softwipedown

"Mit einem gewissen Maß an Unwohlsein gemischt mit Neugier tue ich, was sie sagt, und lege die Augenbinde wieder an. Noch einmal wird die Welt schwarz."


"Reflexartige verkrampfe ich, als ich spüre, wie Lillys Hand sanft die Seite meines Gesichts streichelt, da ich ihre Berührung nicht vorhersehen konnte."


"Ich muss mich wirklich mehr an solchen Körperkontakt gewöhnen. Sogar nach all den Wochen, die wir schon zusammen sind, ist es für mich immer noch nicht so selbstverständlich wie für sie."


"… Stille?"


hi "Hey, Lilly…"


li "Shh."


"Gehorsam leiste ich ihren Anweisungen Folge, höre leise zu und versuche zu erkennen, was um mich herum passiert."


"Verglichen mit eben, wo ich Lilly noch hinterhergejagt bin, brauche ich mich nicht mehr vorsichtig um die Hindernisse des Zimmers herumzubewegen. Ich kann mir Zeit lassen; mich viel mehr auf mein Gehör konzentrieren."


"Es dauert eine Weile, aber schließlich kann ich in dem sonst todstillen Raum das leise Geräusch ihrer Atmung hören."


"Ein… aus… ein… aus…"


"Als ich sie mit meiner eigenen Atmung vergleiche, bemerke ich, dass sie definitiv tiefer ist als sonst – besonders für sie."


"Ein weiteres Geräusch dringt in meine Ohren. Eins, das ich nicht sofort einordnen kann. Ich denke nicht, dass ich es schon einmal gehört habe, aber…"


"Mein Herz setzt einen Schlag aus, als mir der Ursprung klar wird. Reflexartig streckt sich meine Hand danach aus. Ihr Gesicht fühlt sich weicher als sonst an, und ihr Kopf dreht sich ein kleines Bisschen zu den Fingern auf ihrer Wange."


li "Hisao…"


"Ich schlucke und versuche einen Moment lang, mich zu beruhigen. Ich brauche alle Konzentration, die ich in diesem Zustand aufbringen kann, um meine Umgebung vollständig aufzunehmen."


"Nach ein paar tiefen Atemzügen glaube ich, dass ich mich gefangen habe. Mit einer Berührung so leicht, dass sie nicht einmal eine Feder verrücken würde, beginne ich, mit meiner Hand ihren Körper hinabzufahren…"


"… und spüre dabei, wie ich dank ihres dünnen, seidenen Pyjamas, der perfekt an ihren Kurven liegt, wieder meinen Fokus verliere."


"Wenn sie in dieser Position ist, heißt das, dass sie mir zugewandt und gegen ihr Bett gelehnt dasitzt. Dann mal weiter."


"… Okay, das muss ihre Hüfte sein. Wenn ich mich nun langsam etwas abwärts bewege…"


label de_L26h:

"Lillys Atem stockt, als meine Hand ihre berührt, vorsichtig den Fingern zwischen ihre Beinen folgt und sie dann unter ihrer Unterwäsche verliert."


"Nur die leichteste Feuchtigkeit berührt meine Fingerspitzen, aber das reicht aus, um zu erahnen, was sie tut."


"Plötzlich füllt sich mein Kopf mit Vorstellungen davon, wie sie jetzt gerade vor mir aussehen muss. Ich hätte bisher niemals gedacht, dass sie so etwas tut, und dass ich sie dabei nicht sehen kann, vertieft die Stimmung nur noch."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

scene bg school_dormlilly onlayer master
with softwipeup

"Ich ziehe die Augenbinde ab und streiche ein paar Haare aus meinen Augen, die noch in der Schleife hängengeblieben waren."


"Eine Zeit lang bin ich nicht in der Lage zu denken; mein Kopf ist vollkommen leer. Alles, was ich tun kann, ist, mit meinen soeben befreiten Augen das anzustarren, was vor ihnen liegt."


scene evh lilly_masturbate onlayer master:
    truecenter
    subpixel True zoom 1.1
    acdc_warp 10.0 zoom 1.0
with flash

"Wie ich es mir gedacht hatte, sitzt Lilly vor mir."


"Mit einer Hand auf dem Boden, um sich aufrecht zu halten, und mit den Fingern der anderen – versteckt von ihrer dunkelblauen Unterwäsche – reibt sie sich sanft zwischen ihren Beinen. Ich glaube, das ist das Erotischste, was ich je gesehen habe."


"Noch einmal strecke ich meine Hand aus und streiche das Haar aus ihrem Gesicht. Dabei klappt ihr Kinn nach unten, als ihr von Lust durchströmter Körper einen weiteren Atemzug macht."


hi "Lilly…"

"Lilly sieht irgendwie niedlich aus, als sie daraufhin lächelt. Sie scheint immer in den unaufmerksamen Momenten ihre interessantesten Emotionen zu zeigen."


"Es dauert nicht lange, bis sie ihre Finger schneller bewegt als zuvor, wodurch ihre Erregung offenbar steigt. Der Duft ihres Schweißes in der Luft scheint das nur zu bekräftigen."


"Ich sitze vor ihr. Es ist nicht so, als wäre ich nicht selbst erregt – es braucht jede Faser meines Wesens, um sie selbst weitermachen zu lassen, anstatt mich auf sie zu werfen."


scene evh lilly_masturbate_come_face onlayer master
with flash

"Es ist seltsam… anfangs fand ich ihre getrübten, blauen Augen verwirrend, fast schon verstörend wegen ihres fehlenden Fokus. Das stört mich nun weitaus weniger als früher."


"Ich konzentriere mich wieder auf sie, als sie ein Wimmern von sich gibt. Ihr Atem wird viel schneller, und ihre Hüften schaukeln fast unmerklich."


scene evh lilly_masturbate_come onlayer master
with flash

"Erst als ihr der Atem stockt, begreife ich, wie nah Lilly der Grenze gekommen ist. Ihre Augen schließen sich fest, als jeder einzelne Muskel in ihrem Körper sich zu verkrampfen scheint und sie unverkennbar ihren Höhepunkt erreicht."


"Nur ein paar kurze Sekunden verkrampft sie sich, bevor ihr Körper sich entspannt und ein langes, erschöpftes Seufzen von ihren Lippen kommt."


scene bg school_dormlilly onlayer master
with locationchange

"Ich… habe einfach keine Ahnung, was ich sagen soll. Stille herrscht, als ich sie einfach ansehe. Sie sitzt erschöpft da; die Haare hängen ihr ins Gesicht."


show lilly basic_emb_paj_close onlayer master:
    center
    ypos 1.1
with charaenter

li "Hisao…"

"Als sie ihre Hand ausstreckt, um mein Gesicht zu streicheln, übernehmen meine Triebe die Kontrolle über meinen Körper. Ohne einen zweiten Gedanken klettere ich über sie."


"Das ist ein ungewohntes Gefühl. Ich fühle mich sonderbar mächtig, als ich ihr blasses Gesicht unter mir sehe – als würde ich mich seit dem so lange zurückliegenden Unfall zum ersten Mal wieder körperlich stark fühlen."


hi "Lilly… Ich will dich."


show lilly basic_weaksmile_paj_close onlayer master
with charachange

"Zu meiner Überraschung lächelt sie schwach, bevor sie nach oben greift, um die Seite meines Gesichts zu berühren. Es ist ein fast frecher Gesichtsausdruck – die Art, die sie nur zeigt, wenn sie mir etwas entlockt hat."


hi "Du… wolltest, dass ich das tue?"


show lilly basic_smileclosed_paj_close onlayer master
with charachange

"Sie behält ihr Lächeln bei und nickt schweigend. Ich schätze, es war ein effektiver Weg, um mich einmal die Initiative ergreifen zu lassen."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene black onlayer master
with softwipedown

"Und – wieder zu meiner Überraschung – zieht sie die immer noch um meinen Kopf gewickelte Schleife ruckartig hinunter. Wieder einmal bin ich von vollkommener Dunkelheit eingehüllt."


li "Ich hab dir… doch gesagt… dass du sie… anbehalten sollst… oder nicht?"


"Dieser stichelnde Beiklang in Lillys Stimme, betont durch ihre Atmung… Sie scheint niemals ihre Fähigkeit zu verlieren, die Kontrolle über die Lage zu übernehmen."


"Aber dieses Mal… Dieses eine Mal…"


li "Ah, Hisao!? Was ma…?"


"Ich schiebe meine Hände unter sie. Ich fühle weiche Seide und Haut in meinen Händen, als ich mit ein paar Schwierigkeiten sanft ihren Körper anhebe."


"Obwohl ich sie nicht als schwer bezeichnen würde… sorgt ihre Größe dafür, dass sie nicht gerade ein Federgewicht ist."


"Es braucht nur ein paar sorgfältig platzierte Schritte, bis ich die Kante ihres Bettes an meinen Beinen spüre. Dann lege ich Lilly genauso sanft auf ihr Laken, wie ich sie angehoben habe. "




hi "Dein Bett ist gemütlicher als der Boden, oder?"


li "Immer ein Gentleman, nicht wahr?"


"Rasch fahre ich mit meinen Händen Lillys lange, wohlgeformte Beine entlang, welche auch ohne den Luxus des Sehens ihren Reiz nicht verloren haben, und ziehe kurzerhand ihre Pyjama-Shorts und Unterwäsche aus."


"Ich habe keinen Ahnung, wo ich sie gerade hingeworfen habe…"


"Na ja, ist ja auch egal. Irgendwo werden sie schon sein."


"Ohne viel Getue winde ich mich aus meiner eigenen Hose heraus und lege mich zwischen ihre Beine. Oder zumindest glaube ich, dass es zwischen ihren Beinen ist."


"Mit einer Hand auf ihrem Bett, um mich festzuhalten, bewegt sich meine rechte zögernd abwärts."


"Äh, hoppla. Meine erste Berührung mit ihr ist meine Handfläche, die tollpatschig ihre Nasenspritze trifft."


"Sie kichert ein bisschen, bevor sie ihren Kopf zur Seite dreht. Ich nehme das als mein Stichwort und streichle sanft ihre Wange, während ich dabei mit meinem Daumen ihre Gesichtskonturen entlangfahre – so wie sie es so oft bei mir tut."


"Das wäre viel einfacher, wenn sie ihr Gesicht nicht gegen meine Hand pressen würde, doch das Gefühl, wie sie sich an sie anschmiegt, ist angenehm."


"Ich schlucke und versuche, mich aufrecht zu halten und meine andere Hand vom Bett zu nehmen, um mich in sie hineinzuführen."


"Sobald ich ihre Wärme um mich spüre, bemerke ich, wie erregt eigentlich ich bin."


"Mit meinen verbundenen Augen kann ich mich viel mehr auf meine anderen Sinne konzentrieren, einschließlich des Tastsinns. Die ganze Erfahrung fühlt sich lebhafter und intensiver als vorher an."


"Ich beginne langsam meine Hüften vor- und zurückzubewegen, während mein Herz wie wild vor Erregung schlägt."


"Ich spüre, wie Lilly ihre Augen fest schließt, wobei mich die Bewegung unter meinem Daumen an den sanften Griff erinnert, mit dem ich die Seite ihres Gesichts halte."


"Es ist schwierig, davon nicht total überwältigt zu sein. Es ist schwierig zu glauben, dass Sex immer so für sie ist – erlebt durch den jeden Sinn, außer dem, der mir am wichtigsten ist."


"Von ihrer Wange zu ihrem Hals beginne ich, mit meiner Hand langsam abwärts zu fahren und ihren Körper mit meinen Händen zu erspüren."


"Die Kontur ihres Schlüsselbeins… der leichte Tau auf ihrer Haut…"


"Mein Geruchssinn wird vom Duft ihres und meines Schweißes stimuliert. Sogar der Geruch ihres Zimmers, der deutlich anders ist als der meines eigenen Zimmers, trägt zu diesem Gefühl bei."


"Als ich meine Hand zu ihrer weichen Brust bewege, erfüllt ihr sanftes Wimmern meine Ohren – zusammen mit dem Geräusch unseres Aktes."


"Die Haut unter meiner Hand bewegt sich mit jedem Stoß vor und zurück. Mein Griff wird fester, als meine Lust auf Lillys fast nackten Körper vor mir wächst."


"Ich kann sogar ihren kleinen Nippel in meiner Handfläche spüren. Meine Hände fahren weiter hinab, und meine Finger zupfen an ihm durch die dünne Seide ihres Pyjamas."


"Ihre Wimmergeräusche werden zu Stöhnen, als sie die gleiche Lust durchfährt wie mich. Ich kann spüren, wie mein Herz in meiner Brust laut schlägt – und ihres unter meiner Hand."


"Ihre Hände umklammern mit überraschend festem Griff meine Handgelenke, als sich ihre Brust in überwältigender Lust anhebt."


label de_L26x:

scene black onlayer master
with dissolve

"Mehr… Ich will mehr…"


window hide

play sound sfx_heartslow
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.7)

window show

"Ich kann spüren, wie meine Brust enger wird, während ich mich heftig vor- und zurückbewege und wir beide unseren Trieben freien Lauf lassen."


$ renpy.music.set_volume(0.4, 0.5, channel="music")

window hide

play sound sfx_heartslow
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.7)

window show

"Nichts… Ungewöhnliches… Ich muss nur tiefere Atemzüge nehmen, um… ruhiger… zu werden."


$ renpy.music.set_volume(0.3, 0.5, channel="music")

window hide

play sound sfx_heartslow
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.7)

with Pause(0.7)

play sound sfx_heartfast
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.2)

window show

"Diese Gefühl ist völlig… normal…"


$ renpy.music.set_volume(0.2, 0.5, channel="music")

window hide

play sound sfx_heartfast
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

hi "Aah… aaaaaaaah…"


window hide

play sound sfx_heartfast
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

"Das ist… Ich kann nicht… Dieser Schmerz ist zu viel…!"


window hide

play sound sfx_heartstop
show heartattack alpha onlayer master
with Dissolve (0.1)

stop music fadeout 0.3

show heartattack residual onlayer master
with Dissolve (0.8)

window show

hi "AAAAARGH!"


with vpunch

"Ich stolpere mit unziemlicher Eile rückwärts von Lilly weg, stoße mit meiner Ferse tollpatschig gegen den Tisch und falle mit einem würdelosen Rums auf den Boden."


"Ich liege panisch atmend auf dem Rücken und reiße verzweifelt an der Binde vor meinen Augen. Ich muss sie abkriegen, ich muss sie abkriegen…"


scene white onlayer master
with softwipeup

scene bg misc_ceiling onlayer master
show heartattack residual onlayer master
with locationchange

"Für einen Moment wird alles schwarz. Als die Flut aus neugefundenem Licht meine Augen durchdringt, fängt meine Atmung, die gerade noch an der Grenze zur Hyperventilation war, langsam an, sich zu beruhigen."


window hide

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_tragic fadein 4.0

hide heartattack onlayer master
with Dissolve(3.0)

window show

"Sekunden vergehen, in denen ich so konzentriert wie unter diesen Umständen möglich versuche, den Rhythmus meines Herzschlags abzuschätzen."


"Mein Herz ist… normal. Es schlägt wieder normal."


"Mein Körper fühlt sich äußerst bizarr an, als ich benommen auf dem Boden liege und die Decke anstarre. Das Adrenalin von eben gerade strömt immer noch durch meine Adern, doch mein Verstand ist komplett erschöpft."


"Ich raffe mich auf, als ich höre, wie Lilly vom Bett aufsteht und in meine Richtung kommt."


show bg misc_ceiling_blur as bg2 onlayer master:
    center
    alpha 0.0
    linear 1.0 alpha 1.0
show lilly superclose_shock onlayer master:
    xalign 0.5 yanchor 0.5 ypos 0.15 alpha 0.0
    subpixel True rotate 180
    easein 1.0 alpha 1.0 ypos 0.3
with Pause(1.0)

li "Hisao? Bist du okay? Hisao!?"


hi "Mir geht's gut, Lilly. Es geht mir… gut."


show lilly superclose onlayer master:
    xalign 0.5 yanchor 0.5 ypos 0.3 alpha 1.0
    subpixel True rotate 180
with charachange

"Sie seufzt erleichtert, und ihr besorgter Gesichtsausdruck verfliegt."


"Ihre darauf folgende Miene ist das Letzte, was ich je von ihr sehen wollte. Eine Miene, die ich schon hasste, als ich vor all diesen Monaten meine Eltern zum ersten Mal im Krankenhaus sah."


"Mitleid. Lilly… bemitleidet mich."


scene black onlayer master
with shuteye

"Machtlos schließe ich meine Augen und wende mich ab. Ich glaube, mir wird gleich übel."


play sound sfx_rustling

"Ich kann hören, wie Lilly sich wegbewegt und sich fix um sich selbst kümmert; wie sie sich wieder anzieht, nachdem sie kurz nach ihrer Kleidung gesucht hat."


hi "Tut mir leid…"


scene bg school_dormlilly onlayer master
show lilly basic_concerned_paj onlayer master at center
with openeye

"Sie schüttelt langsam ihren Kopf, während sie den letzten Knopf ihres Hemdes zuknöpft. Ihr gütiges Lächeln sieht so zerbrechlich, so empfindlich aus, dass es meinem Herzen einen Stich versetzt."


show lilly basic_concerned_paj_close onlayer master
with characlose

show lilly basic_concerned_paj_close onlayer master:
    ypos 1.1
with charamove

"Als sie sich mir vorsichtig nähert, ertastet sie die Kante des tiefen Tisches, bevor sie sich neben mich setzt und ihre Arme um meine Brust legt."


li "Es tut mir leid, Hisao. Ich hätte dir meine Gelüste nicht so aufzwingen sollen."


hi "Du brauchst dich nicht zu entschuldigen. Normalerweise hätte ich keine Probleme; das hast du selbst schon gesehen."


hi "Ich schätze, ich hätte mich nicht so sehr anstrengen sollen."


"Meine Augenlider fühlen sich schwer an. So ruhig neben ihr zu sitzen, lässt das Adrenalin wahrscheinlich aus meinem Kreislauf verschwinden und meinen Verstand entspannen."


show lilly basic_oops_paj_close onlayer master
with charachange

li "Darum… hast du also nie die Führung übernommen…?"


hi "Ja. Schätze, es ist wohl gut, dass du das gerne machst, was?"


show lilly basic_weaksmile_paj_close onlayer master
with charachange

"Der Witz scheint sie etwas aufzumuntern, wodurch ich mich etwas weniger unwohl wegen meines unzuverlässigen Selbst fühle."


"Lillys Kopf legt sich auf meine Schulter, während ich damit ringe, meine Augen offen zu halten, was mir mit jedem Blinzeln schwerer fällt. Ich bin vollkommen ausgelaugt."


li "Es ist okay, Hisao. Es ist alles okay."


stop music fadeout 5.0

"Kaum hat sie das gesagt, entspringt ihren Lippen ein kleines, leises Lied. Gänzlich zu erschöpft, um zu denken, kann ich nur ihrem sanften Summen lauschen."


"Es ist ein sanftes, fast melancholisches Lied. Es klingt vertraut, doch je mehr ich versuche, mich daran zu erinnern, woher ich es kenne, desto weniger scheine ich mich konzentrieren zu können."


"Das Gefühl und der Duft ihres Kopfes, der sanft auf meiner Schulter ruht, und ihres warmen Körpers an meiner Seite sind wohltuend, und ihr leises Summen entspannt meinen Verstand genauso wie ihre Wärme meine Muskeln."


"Dieser einzelne, leise Moment… Nach all diesem Tumult lässt er mich begreifen, wie erschöpft ich eigentlich bin. Ich kann spüren, wie meine Augenlider langsam schwerer und schwerer werden."


"Selbst mit dem vorangegangenem Chaos wünschte ich mir, dass dieser Moment ewig anhalten würde."


"Lilly und ich zusammen, wie wir uns einen kleinen, unbedeutenden Moment teilen – so wie sonst auch immer."


"Aber wenn das der Fall ist… warum kommt es mir dann so vor… als wäre sie mir ferner als je zuvor?"


scene black onlayer master
with dissolve




label de_L27:

scene bg school_library onlayer master
with locationchange

play sound sfx_doorslam
play music music_happiness fadein 2.0

"Das laute Poltern der in den Rückgabekorb fallenden Bücher zerreißt den Mantel der Stille, der über der Schulbibliothek liegt."


"Ich habe mir angewöhnt, wenigstens einmal pro Woche in die Bibliothek zu gehen. Aber ich beschäftige mich nicht nur mit dem Lesen der Bücher, sondern ich diskutiere später auch mit Hanako und Lilly über sie."


show yuuko panic_up onlayer master at center
with charaenter

"Offensichtlich erschrocken dreht sich Yuuko in die Richtung des Lärms. Ich hätte gedacht, dass sie sich inzwischen daran gewöhnt hat, dass Leute Bücher fallen lassen. Immerhin arbeitet sie hier."


show yuuko neutral_down onlayer master
with charachange

yu "Oh, hallo Hisao. Wieder hier?"


"Ich brauche einen Augenblick, um ihr zu antworten. In meinem Kopf schwirrt immer noch die mir so vertraute Melodie von Lillys Lied, die mir seit mehreren Tagen nicht mehr aus dem Kopf gehen will."


hi "Hmm? Oh, ja. Ich bringe nur ein paar ausgeliehene Bücher zurück."


"Sie sieht nach unten. Vermutlich auf den Korb, in den die Bücher gefallen sind."


show yuuko closedhappy_down onlayer master
with charachange

yu "Du liest ziemlich viel, nicht wahr?"


hi "Es ist mittlerweile irgendwie zur Routine geworden. Vertreibt zumindest die Zeit."


show yuuko worried_up onlayer master
with charachange

yu "Ich wünschte, ich hätte Freizeit, die ich vertreiben könnte…"


"Von Smalltalk zu Depression in weniger als fünf Sekunden. Ich glaube, das ist ein neuer Rekord für sie. Sie wirkt heute allgemein etwas niedergeschlagen, sogar vergleichen mit sonst."


"Wenn man bedenkt, dass sie zwei Jobs braucht, nur um ihren Lebensunterhalt zu verdienen, kann ich mir vorstellen, dass das seinen Tribut an Freizeit fordert."


"Da fällt mir ein – die Bezahlung für ihren Job hier kann nicht allzu schlecht sein. Ich kann mir nicht vorstellen, dass das Personal an so einer prestigeträchtigen Schule am Hungertuch nagen müsste."


hi "Zwei Jobs zu haben, muss eine Menge Zeit verschlingen. Ich würde das wahrscheinlich niemals hinkriegen."


show yuuko neutral_up onlayer master
with charachange

yu "Du hast Glück, dass du ein Schüler bist. Glaubst du, dass du es auf die Universität schaffen wirst?"


"Wenn sie das fragt, dann schätze ich, dass man das von uns erwartet, wenn wir so eine Bildung bekommen. Privatschulen wie diese sind nicht gerade billig."


hi "Ich… denke ja. Ich habe das Geld, glaube ich."


hi "Meine Pläne setzen voraus, dass ich an eine gehe, und meine Noten sind gut genug. Die Frage ist eher, wie ich dafür bezahlen soll."


show yuuko worried_down onlayer master
with charachange

yu "Die Universität kostet so viel, dass ich zwei Jobs brauche, um mir auch nur die Gebühr leisten zu können… Die täglichen Ausgaben machen es noch viel schwieriger."


show yuuko neutral_down onlayer master
with charachange

yu "Aber wenn du so viel liest, heißt das doch, dass du dich in der Schule ganz gut machst, oder?"


"Interessante Schlussfolgerung. Wenn auch insgesamt nicht ganz falsch."


hi "Vermutlich. Ich fand keine der Prüfungen wirklich schwierig, abgesehen von einer oder zwei."


hi "Darf ich dich fragen, was du an der Universität studierst?"


show yuuko happy_up onlayer master
with charachange

"Bei dieser Frage erhellt sich Yuukos Gesicht schlagartig."


show yuuko closedhappy_up onlayer master
with charachange

yu "Anthropologie. Um genau zu sein, spezialisiere ich mich auf die Geschichte der Klassischen Ära der athenischen Zivilisation und Demokratie."


"Sie scheint wirklich Ahnung zu haben, wovon sie redet. So ein Enthusiasmus ist bewundernswert, und es ist schön, sie so begeistert von etwas zu sehen."


"Auch jemand wie Yuuko kann wohl glücklich sein, wenn sie einen sichtbaren Weg vor sich hat."


hi "Freut mich, das zu hören. Falls du—{w=0.6}{nw}"


stop music fadeout 0.5
play sound sfx_phone

show yuuko panic_up onlayer master
with vpunch

"Wir beide schrecken wegen der plötzliche Unterbrechung aus meiner Hosentasche auf."


scene bg school_hallway3 onlayer master
with locationchange

"Nachdem ich mich übermäßig entschuldigt habe, eile ich flugs in den Korridor, während ich auf dem Weg dorthin mein Handy aufklappe und auf das Display schaue."


"… Komisch. Eine Handynummer, die ich nicht kenne. Da ich die Leute, die meine Telefonnummer haben, an einer Hand abzählen kann, frage ich mich kurz, ob eine Werbefirma durch Zufall an meine Nummer gekommen ist."


scene bg school_hallway3_blurred onlayer master
show phone mobile onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)

hi "Hallo, Hisao Nakai hier."


mystery "Mann, geh das nächste Mal schneller ran. Jedenfalls – wer bin ich?"


play music music_comedy fadein 1.0

"Ich brauche nur eine Sekunde, um diese unverwechselbar tiefe und barsche Stimme wiederzuerkennen."


hi "Hey, Misha. Hätte nicht erwartet, dass du mich anrufst."


aki "Hä? Du denkst wirklich, ich klinge wie sie?"


hi "Überhaupt nicht, Akira. Allerdings kann ich mich nicht daran erinnern, dir meine Nummer gegeben zu haben, also wollte ich dich etwas auf den Arm nehmen."


aki "Oh, das? Ich hab sie mir von Lilly geben lassen. War kein Ding."


"Ohne jeden Zweifel strotzt sie bei diesem Statement vor Stolz."


"Allerdings sollte ich vermutlich nicht so überrascht darüber sein, dass Lilly ihr meine Nummer gegeben hat, wenn sie sich so nahestehen."


hi "Und? Was gibt's?"


aki "Hast du gerade Zeit?"


hi "Ich… glaube? Wieso?"


aki "Könntest du mich in dem Park im Dorf treffen? Ich will mit dir nur über ein paar Sachen reden."


hi "Ist das eine Einladung für ein Date?"


aki "Was? Natürlich nicht…"


stop music fadeout 5.0

"Auf einmal klingt sie sehr geknickt und ihr bisher stichelnder Charakter ist sofort verpufft. Das passt nicht zu ihr."


hi "Jedenfalls hätte ich nichts dagegen. Wann willst du dich treffen?"


aki "Na ja… so um… jetzt."


hi "Warte, genau jetzt? Aber es ist…"


"Die Totenstille von der anderen Seite der Leitung sagt mir, dass sie kurzerhand aufgelegt hat."


show phone mobile onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

scene bg school_hallway3 onlayer master
show phone mobile onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with locationchange
with Pause (0.5)

hide phone onlayer master
with None

"Für eine lange Zeit stehe ich lediglich da und starre auf die „ANRUF BEENDET”-Nachricht auf dem Display, während ich die Unterhaltung in meinem Kopf noch einmal wiederhole."


hi "Was zum Teufel, Akira?"


scene bg suburb_park_ss onlayer master
with shorttimeskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 2.0

"Ich lasse meinen Blick nach rechts und links schweifen, überquere die Straße und gehe in den Park."


"Ich habe gelernt, bei solchen Spaziergängen meinen Rhythmus zu halten – hauptsächlich weil Lillys langsameres Tempo bei unseren Ausflügen ins Dorf dafür sorgt, dass ich mich bewusst bremsen muss."


"Abgesehen davon hoffe ich, dass Akira nicht von mir erwartet hat, dass ich unverzüglich erscheine."


$ ksgallery_unlock("evul akira_park")
scene ev akira_park onlayer master:
    subpixel True xalign 1.0 yalign 0.0 zoom 1.0
    acdc_warp 15.0 zoom 0.8
with whiteout

play music music_night

"Es dauert nur ein paar Sekunden, bis ich sie entdecke, wie sie mit einer Dose Bier in der Hand auf einer Bank wartet."


"Dem Blick, den sie mir zuwirft, als ich auf sie zugehe, mangelt es an jeglicher Regung, die man als Anerkennung für mein Erscheinen hätte interpretieren können."


hi "Was soll dieser Blick? Ich hätte nicht kommen müssen, weißt du."


aki "Ich wusste, dass du kommen würdest. Immerhin bist du so Einer."


scene bg suburb_park_ss onlayer master
with locationchange

play sound sfx_can_clatter

"Ich hebe eine Augenbraue, während sie aufsteht und sich der Dose entledigt, die sie beim Warten auf mich geleert hat. Ein metallisches Klappern folgt. Akira nimmt wieder auf der alten Holzbank platz, und ich tue es ihr gleich."


play sound sfx_can

"Sie greift neben sich und nimmt eine weitere Bierdose. Bevor sie weiterspricht, öffnet sie sie und nimmt einen großen Schluck. Sie scheint dieses Zeug wirklich zu mögen."


hi "Ich schätze, ich brauche nicht zu fragen, worum es hier geht? Oder eher, um wen?"


show akira basic_resigned_close_ss onlayer master at tworight
with charaenter

aki "Ich hab von Lilly gehört, dass du nach unserer Familie gefragt hast."


"Sie tauschen mehr aus als nur Telefonnummern, so viel ist sicher. Ich würde mir gerade wahrscheinlich große Sorgen machen, wenn es ihrer Stimme nicht vollkommen an Böswilligkeit fehlen würde. Vielmehr klingt ihre Stimme fast wehmütig."


hi "Hauptsächlich pure Neugier."


hi "… Ich muss zugeben, ich hätte niemals gedacht, dass ihr beide Halbschottinnen seid."


show akira basic_ending_close_ss onlayer master
with charachange

"Sie schmunzelt amüsiert."


show akira basic_smile_close_ss onlayer master
with charachange

aki "Das hab ich schon oft gehört, glaub mir."


show akira basic_distant_close_ss onlayer master
with charachange

"Das kleine Lächeln verschwindet von ihrem Gesicht und ihre Augen schauen nachdenklich geradeaus."


"Abgesehen von den gelegentlichem Wortwechsel des alten Paares, welches langsam den sich schlängelnden Weg entlanggeht, und den vereinzelten, in die Jahre gekommenen Autos, ist es angenehm ruhig."


show akira basic_lost_close_ss onlayer master
with charachange

aki "Sie hat dir aber nicht alles erzählt, oder?"


hi "Sie hat sich sehr kurz gefasst. Deine Eltern leben in Schottland, sie hat sie nicht getroffen, seit sie zwölf war, und sie will sie wiedersehen."


show akira basic_annoyed_close_ss onlayer master
with charachange

aki "Es hat mich immer überrascht, wie ergeben sie unseren Eltern gegenüber ist, nach allem, was sie für uns getan haben."


"So wie sie es sagt, klingt es fast verächtlich. Sie seufzt leise, als wollte sie damit diese Gefühle verdrängen."


show akira basic_resigned_close_ss onlayer master
with charachange

aki "Warum glaubst du, sind sie gegangen, Hisao?"


hi "Was ich denke, warum sie gegangen sind?"


hi "Lilly zufolge war es wegen der Arbeit. Ein ziemlich gut bezahlter Job war wohl auch im Spiel, wenn man den Lebensstil eurer Eltern betrachtet."


hi "Also ging Lilly an eine Privatschule, und darum hat sie auch diese Grazie und diese Oberklasse-Aura um sich."


aki "Ja. Da das Geschäft in Inverness boomte, beschloss unser Vater, direkt in die Stadt zu ziehen, in der auch der Hauptsitz liegt."


show akira basic_smile_close_ss onlayer master
with charachange

aki "Das ist genau die Schlussfolgerung, von der ich dachte, dass du zu ihr kommen wirst. Du bist zu gutgläubig."


hi "Du glaubst nicht, dass sie wegen ihrer Karriere gegangen sind?"


show akira basic_resigned_close_ss onlayer master
with charachange

aki "Ich sitze hier und lästere darüber mit dir. Was denkst du denn?"


show akira basic_lost_close_ss onlayer master
with charachange

aki "Yamaku Akademie. Mir kam diese Schule schon immer irgendwie gruselig vor; als ob sie ein isolierter Zufluchtsort für jene ist, die die „normale Gesellschaft” weder sehen noch hören will."


show akira basic_annoyed_close_ss onlayer master
with charachange

aki "Wahrscheinlich bereuen sie einfach die Tatsache, dass Lilly nicht alt genug war, um sie noch vor ihrer Abreise da reinzustecken."


"Eine lange Stille folgt ihrer abrupten und sehr brutalen Kritik über ihre eigenen Eltern und die Yamaku."


"Lillys Blindheit ist schwerlich etwas, das man in einer Oberklasse-Familie, die versucht, ihr Gesicht zu wahren, einfach ignorieren kann. Noch viel weniger, wenn ein lukratives Angebot auf sie wartet."


"Schließlich schnaubt Akira verächtlich, und ihre Gefühle brechen aus ihr hervor."


aki "Umziehen, um mit seiner Beförderung unsere finanzielle Zukunft zu sichern. Selbst damals konnte ich es kaum fassen."


"Da ich nicht nur gekommen sein will, damit sie Dampf an mir ablässt, versuche ich behutsam, die Unterhaltung zu lenken."


hi "Dann bist du also mit Lilly in Japan geblieben?"


show akira basic_resigned_close_ss onlayer master
with charachange

aki "Entweder das, oder sie hätte mit unseren kränklichen Großeltern zusammenleben müssen."


hi "Was ist mit Shizunes Familie? Wenn ihr Cousinen seid, dann…"


show akira basic_annoyed_close_ss onlayer master
with charachange

aki "Unsere Väter hassen einander. Ich hätte Vater ja gesagt, dass er bleiben soll, wo der Pfeffer wächst, und wäre trotzdem bei ihnen eingezogen, aber Lilly hätte das nicht gewollt."


show akira basic_resigned_close_ss onlayer master
with charachange

aki "Damals hatte ich auch schon ein Jobangebot, also taten wir unser Bestes, um das Haus unserer Eltern in gutem Zustand zu halten, und versuchten weiterzuleben, als wären sie nie gegangen."


hi "Also habt ihr einfach zu zweit dort gewohnt?"


show akira basic_lost_close_ss onlayer master
with charachange

aki "So ziemlich. Lilly hatte Schule, und ich hatte meinen Job, also hatten wir nicht gerade Langeweile."


aki "Aber es kommt mir vor, als hätte ich sie enttäuscht. Während ich am Arbeiten war, hat sie sich um ihre Schule, ihre Hausaufgaben und um die Hausarbeit gekümmert. Ich hab versucht, für sie da zu sein, aber letzten Endes hab ich es vermasselt."


show akira basic_annoyed_close_ss onlayer master
with charachange

aki "… Von einer Neunzehnjährigen zu erwarten, eine Mutter für ein blindes Kind zu sein. Das ist lächerlich."


"Also… lebten Lilly und Akira allein, nachdem ihre Eltern umgezogen waren, und Lilly hat sich größtenteils um sich selbst gekümmert. Das erklärt wohl ihre offensichtliche Unabhängigkeit – verglichen mit vielen anderen auf der Yamaku."


"Ich mag die meiste Zeit allein gewesen sein, weil meine Eltern beide arbeiteten, aber das… ist einfach etwas gänzlich anderes."


show akira basic_resigned_close_ss onlayer master
with charachange

aki "Tut mir leid, dass du dir mein Gejammer anhören musst, Hisao."


hi "Braucht es nicht, aber… darf ich fragen, warum du mir all das erzählst?"


show akira basic_smile_close_ss onlayer master
with charachange

aki "Hmph. Du warst schon immer neugierig."


show akira basic_distant_close_ss onlayer master
with charachange

aki "Also Kontext, schätze ich."


aki "Das Leben ist kein Ponyhof, Hisao. Manche Menschen müssen das auf die harte Tour lernen."


"Sie nimmt einen langen Schluck aus der Dose in ihrer Hand. Ihre Miene wirkt langsam eher deprimiert als distanziert."


stop music fadeout 2.0

show akira basic_resigned_close_ss onlayer master
with charachange

aki "Vor ein paar Tagen hab ich mit meinem Freund Schluss gemacht. Nachdem ich wegfahre, werden wir uns nicht wiedersehen können."


aki "Aber so ist das Leben. Man kann nicht einfach sein Leben planen und erwarten, dass es für immer so bleibt. Manchmal passieren Dinge, die man nehmen muss, wie sie kommen – auch wenn es bedeutet, dass man sich oder andere verletzt."


"Sie nimmt einen langen Atemzug, bevor sie zum hellen, orangenen Himmel hinaufsieht."


show akira basic_distant_close_ss onlayer master
with charachange

aki "Verdammt… Wenn ich rauchen würde, könnte ich genau jetzt einen schönen, langen Zug nehmen und dabei ziemlich cool aussehen."


"Ich will antworten, um ihr irgendwie zu helfen, aber ich fühle mich absolut nutzlos. Noch nie bin ich in so einer Situation gewesen, und ich habe einfach nicht die Erfahrung, um etwas Bedeutungsvolles zu sagen, das sie trösten würde."


"Akira sieht herüber und bemerkt es offenbar – sehr zu meiner Beschämung."


show akira basic_lost_close_ss onlayer master
with charachange

aki "Ich muss gerade ziemlich erbärmlich aussehen, dass ich mich bei jemanden ausjammere, den ich kaum kenne."


hi "Nicht wirklich – und ich bin geradezu ein Experte im erbärmlich Aussehen."


show akira basic_ending_close_ss onlayer master
with charachange

"Sie kichert, was mich diesen Spruch wie einen persönlichen Sieg sehen lässt."


show akira basic_smile_close_ss onlayer master
with charachange

aki "Du bist ein guter Junge, Hisao. Als ich sagte, dass ich es akzeptiere, dass du mit meiner Schwester zusammen bist, habe ich nicht gescherzt oder es nur nett gemeint."


show akira basic_smile_ss onlayer master:
    tworight
    ypos 1.1
    ease 0.5 ypos 1.0
with charadistant

play sound sfx_can_clatter

"Sie erhebt sich mit einem kaum zu ihrem Alter passendem Grummeln von der Bank und schmeißt die leere Dose nach einem letzten Schluck in den Abfalleimer."


show akira basic_boo_ss onlayer master at tworight
with charachange

aki "Es ist nur schade, dass das in dieser Welt nicht wirklich viel bringt."


show akira basic_resigned_ss onlayer master
with charachange

aki "Als ich sagte, dass ich nach Schottland abreise, tat ich es, weil sich sich eine gute Stelle im Hauptsitz des Unternehmens auftat."


aki "Aber als wir bei ihnen waren, sagten unsere Leute mir, dass sie auch Lilly aufgefordert haben, nach Inverness zu ziehen."


play music music_sadness fadein 0.5

"Niemals…"


"Ihre Ausflüchte, als ich sie nach ihrer Zukunft gefragt habe… Die Unbeholfenheit, die zwischen uns immer weiter zunahm… Dieser untypische Wutausbruch…"


"Alles passt auf einmal zusammen."


"Die gleiche Familie, über die sie auf Hanakos Geburtstagsparty in Erinnerungen schwelgte, die gleiche Familie, die sie und Akira sich selbst überlassen hat…"


"Jetzt komme ich mir bescheuert vor, dass ich Lilly nie richtig danach gefragt habe, was sie geplagt hat. Ich habe nicht einmal in Erwägung gezogen, dass während ihrer Reise zu ihrer Familie in Inverness etwas passiert sein könnte."


"Und nun… wächst ein Gefühl der Besorgnis in meiner Brust. Wenn ihre Familie sie dazu aufgefordert hat, zu ihnen nach Schottland zu ziehen, auf die andere Seite der Erde…"


hi "Hat sie… angenommen?"


show akira basic_lost_ss onlayer master
with charachange

aki "Lilly hat mir nicht gesagt, ob sie annehmen will oder nicht. Und dir anscheinend auch nicht."


aki "Deswegen wollte ich hier mit dir reden, Hisao."


hi "Kontext, was…"


"Ich lehne mich zurück. Die Sorgen und der Frust stehen mir ohne Zweifel ins Gesicht geschrieben."


show akira basic_resigned_ss onlayer master
with charachange

aki "Lilly ist ein starker Mensch, Hisao, aber sie ist nicht unfehlbar."


aki "Ich schätze, es ist wohl mein Job als ältere Schwester, mich um sie zu sorgen, aber ich denke, dass du es verdient hast, das zu erfahren."


hi "Ich verstehe."


show akira basic_lost_ss onlayer master
with charachange

aki "Alles klar? Du klingst deprimiert."


hi "Nein, ich… denke nur nach."


show akira basic_ending_ss onlayer master
with charachange

aki "Das ist gut. Nachdenken ist gut. Überstürztes Handeln wird dich nicht weit bringen."


show akira basic_boo_ss onlayer master
with charachange

"Mit einer kaum merklichen Handbewegung schaut sie auf ihre Uhr."


show akira basic_lost_ss onlayer master
with charachange

aki "Ich muss los. Kommst du klar?"


hi "Passt schon, keine Sorge. Ich werde mit Lilly darüber reden und ein paar Dinge klarstellen müssen."


show akira basic_smile_ss onlayer master
with charachange

"Sie lächelt mir zu, was aber ein wenig gekünstelt aussieht."


"Was uns beide bedrückt, ist die Tatsache, dass Lilly vor der größten Entscheidung ihres Lebens steht und versucht, die ganze Last allein zu Schultern."


"Und ein Teil dieser Last ist unsere Beziehung."


stop music fadeout 5.0
hide akira onlayer master
with charaexit

"Als ich wieder aufsehe, zieht Akira bereits mit einer erhobenen Hand davon."


"Zum ersten Mal seit langer Zeit habe ich endlich eine Antwort auf etwas. Vielleicht nicht einmal das. Aber zumindest habe ich nun die richtige Frage."


"„Wirst du bleiben… oder gehen?”"


stop ambient fadeout 2.0

scene black onlayer master
with dissolve




label de_L28:

scene bg suburb_roadcenter_rn onlayer master
show rain normal onlayer master
with locationchange

play ambient sfx_rain fadein 4.0

hi "Lilly, beeil dich!"


show lilly basic_concerned_cas_close_rn behind rain onlayer master at center
with charaenter

li "Ich laufe, so schnell ich kann!"


"Durch das ohrenbetäubende Prasseln des Regens kann ich Lillys Stimme kaum hören. Auch wenn ich sie ungern umherschleife, verlangt die Lage danach."


"Ich drehe mich wieder nach vorn, lege meine freie Hand auf meinen Kopf und versuche vergeblich, zumindest meine Haare trocken zu halten."
"Meine Sicht scheint sich auf Graustufen reduziert zu haben. Das ist ein ziemlich mieses Wetter für den Sommer, und wohl das letzte, das ich mir für ein Date gewünscht hätte."


"Eine Schande. Ich habe vorher sogar die Wettervorhersage überprüft – eine Seltenheit für mich – und sie haben gesagt, dass es Sonntag Nachmittag schön sein wird."


"Beim Blick auf Lilly sehe ich, dass ihre Schultern mittlerweile komplett nass sind. Ihre rechte Hand klammert sich fest an meine, und ihre linke hält den zusammengeschobenen Blindenstock."


"Dieser furchtbare Regenguss kam plötzlich, als wir genau zwischen unserem Ziel und der Schule waren. Darum haben wir uns dazu entschieden, den Rest der Strecke einfach zu rennen, anstatt die ganze Tour umsonst gemacht zu haben."


"Da sie es nicht gewohnt ist, so schnell zu rennen, nutzt Lilly all ihre Konzentration, um nicht zu stolpern."


show lilly basic_oops_cas_close_rn onlayer master
with charachange

li "Hisao, weißt du eigentlich, wo du hinwillst?"


"Sogar sie muss schreien, um über das Geräusch des Windes und des Regens hinweg gehört zu werden."


hi "Das Sha—"


"Der Rest meiner Stimme wird vollkommen von einer noch heftigeren Sturmböe verschluckt."


show lilly basic_sad_cas_close_rn onlayer master
with charachange

li "Das was?"


hi "Das Shanghai!"


show lilly basic_concerned_cas_close_rn onlayer master
with charachange

li "Wie weit ist es noch?"


hi "Es sollte nicht mehr weit sein!"


show bg suburb_shanghaiext_rn onlayer master
show lilly basic_concerned_cas_close_rn onlayer master
with shorttimeskip

"Es dauert nicht lange, bis ich ihr noch einmal etwas zurufe."


hi "Sieht aus, als wären wir gerettet – es ist direkt vor uns!"


"Genau vor der vertrauen Ladenfront komme ich zum Halt und warte darauf, dass Lilly zu Atem kommt, bevor wir hineingehen. Dabei schenkt uns die draußen hängende, verlässliche Laterne ihr Licht."


hi "Ladies first."


play sound sfx_storebell

show lilly basic_smileclosed_cas_close_rn onlayer master at center
with charachange

with Pause(0.5)

hide lilly onlayer master
with charaexit

"Die kleine Glocke im Inneren ertönt, als ich ihr die Tür offenhalte. Ein Lächeln und ein höflicher Knicks belohnen mich, bevor sie hineingeht."


$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
play music music_dreamy fadein 3.0

scene bg suburb_shanghaiint onlayer master
show lilly basic_smileclosed_cas onlayer master at center
with locationchange

"Ich folge ihr und trete meine Füße ab. Nur ein kurzer Blick reicht aus, um zu bemerken, dass es sehr leer ist. Das Shanghai scheint nicht wirklich viel Besuch zu bekommen, und heute ist es auch nicht anders. Nur ein paar Tische sind besetzt."


"Gerufen von dem Klingeln der Glocke erscheint eine sehr vertraute Person, um uns zu begrüßen."


show bg suburb_shanghaiint onlayer master at bgleft
show lilly basic_smileclosed_cas onlayer master at twoleft
with charamove

show yuukoshang happy_up onlayer master at tworight
with charaenter

yu "Willkommen im Shanghai!"


"Yuuko sieht heute aufgeweckt aus. Ihre Stimmung vorherzusagen ist ziemlich schwierig, aber es ist eine schöne Abwechslung."


show lilly basic_smile_cas onlayer master
with charachange

li "Hallo Yuuko."


hi "Hey."


show yuukoshang closedhappy_down onlayer master
with charachange

yu "Gute Tag ihr Zwei."


show yuukoshang neutral_down onlayer master:
    ypos 1.25
with Dissolvemove(0.2)

with Pause(0.2)

show yuukoshang neutral_down onlayer master at tworight
with charamove

"Sie verbeugt sich tief und ist etwas bestürzt, als sie sich wieder aufrichtet und einen genaueren Blick auf uns wirft."


show yuukoshang worried_down onlayer master
with charachange

yu "Was ist mit euch passiert? Ihr beide seht…"


"Ihre Augen wandern zum Fenster der Tür hinter uns."


show yuukoshang panic_up onlayer master
with charachange

yu "Oh. Oh je."


hi "Wenigstens sind wir jetzt drin. Ich denke, das ist das Wichtigste."


show lilly basic_weaksmile_cas onlayer master
with charachange

li "Es ist warm und gemütlich. Du hast Glück, dass du heute drinnen arbeitest."


show yuukoshang smile_down onlayer master
with charachange

yu "Es war angenehm ruhig. Ich mag solche Tage."


show yuukoshang worried_down onlayer master
with charachange

yu "Oh wartet, ähm, entschuldigt… Möchtet ihr etwas bestellen?"


show lilly basic_smile_cas onlayer master
with charachange

li "Französischen Vanilletee bitte."


hi "Ich nehme das Gleiche."


show yuukoshang closedhappy_up onlayer master
with charachange

yu "Okay. Kommt sofort."


hide yuukoshang onlayer master
with charaexit

"Sofort jagt sie mit einem entschlossenem Blick davon und versucht wohl mit aller Kraft, unsere Bestellung nicht zu vergessen. Zumindest engagiert sie sich für ihre Jobs, das muss man ihr lassen."


show bg suburb_shanghaiint onlayer master at center
show lilly basic_smileclosed_cas_close onlayer master at center
with dissolvecharamove

show lilly basic_smileclosed_cas_close onlayer master:
    ypos 1.1
with charamove

"Ich führe Lilly zu einem leeren Platz und wir setzen uns hin. Ich lasse mich erschöpft in meinen Stuhl plumpsen, während Lilly sich elegant auf ihren setzt und ihren Blindenstock neben sich legt."


"Für eine Weile sehe ich untätig dem draußen fallenden Regen zu. Vereinzelt rennen Leute die Straße entlang und versuchen dabei, so trocken wie möglich zu bleiben, wobei sie oft einen klatschnassen Regenschirm fest umklammern."


"Lilly sitzt genauso still da wie ich. Weil sie allen Geschehnissen aufmerksam lauscht, sind ihre Augen geschlossen."


"Es ist eine angenehme, entspannende Stille, die zwischen uns herrscht; genau die, die wir so oft in den letzten Monaten geteilt haben."


stop music fadeout 5.0

"Für Lilly zumindest."


"Unaufhörlich wiederholen sich die Worte ihrer Schwester in meinem Kopf, und ich versuche, darin eine Erklärung für Lillys Verhalten seit ihrer Rückkehr aus Schottland zu finden."


"Egal wie sehr ich es versuche, ich werde aus Lilly nicht schlau. Es ist, als würde jeder Versuch, ihre Gefühle und ihre potentielle Entscheidung vorherzusagen, es nur noch schwieriger machen, zu einer klaren Schlussfolgerung zu kommen."


"Es lässt mich daran zweifeln, ob ich sie je wirklich verstanden habe. Letztendlich werde ich sie fragen müssen, auch wenn ich es viel lieber vermeiden würde."


show lilly basic_smile_cas_close onlayer master
with charachange

li "Du bist heute etwas still, Hisao."


hi "Echt?"


show lilly basic_ara_cas_close onlayer master
with charachange

li "Du warst so begeistert davon, mich auf ein Date auszuführen. Ich hatte angenommen, dass du etwas Spezielles vorhast."


hi "Nein, nicht wirklich. Ich wollte nur etwas Zeit mit dir verbringen."


show lilly basic_weaksmile_cas_close onlayer master
with charachange

li "Ach so…"


hi "Na gut. Es gibt da eine Sache."


show lilly basic_cheerful_cas_close onlayer master
with charachange

"Ein kleines Grinsen findet seinen Weg auf Lillys Gesicht. Sie weiß ganz genau, dass sie mich geschlagen hat. Das macht das, was ich sagen will, nur noch peinlicher."


hi "Es ist nur… Akira und ich haben uns unterhalten."


show lilly basic_surprised_cas_close onlayer master
with charachange

li "Oh?"


hi "Was soll dieser Ton?"


show lilly basic_weaksmile_cas_close onlayer master
with charachange

li "Ihr Zwei scheint euch ja recht gut zu verstehen."


hi "Na ja, sie ist cool, und ich denke, dass man sich ganz gut mit ihr unterhalten kann. Es wäre schön, wenn irgendeiner der Lehrer auch nur annähernd so wie sie wäre."


show lilly basic_sleepy_cas_close onlayer master
with charachange

li "„Cool…”"


"Für einen Augenblick versuche ich, ihren Tonfall einzuordnen, und als es mir gelingt, verziehen sich meine Mundwinkel zu einem Lächeln."


hi "Du bist eifersüchtig, stimmt's?"


show lilly basic_pout_cas_close onlayer master
with charachange

li "Bin ich nicht!"


"Nachdem sie mich bei unserem ersten Date auch mit diesem Thema aufgezogen hat, fühle ich mich nicht allzu schlecht, wenn ich mich diesmal etwas über sie amüsiere."


"Aber als wir dann wieder ruhig werden, war es dann doch nur eine kleine Ablenkung von dem echten Grund, weswegen ich Lilly hergebracht habe."


hi "Keine Sorge, es war größtenteils nur alltägliches Zeug. Aber abgesehen davon hat Akira etwas erwähnt, worüber ich mit dir reden wollte."


hi "Sie sagte, als ihr vor einer Weile deine Familie in Inverness besuchen wart…"


show lilly basic_reminisce_cas_close onlayer master
with charachange

li "Akira hat dir von der Aufforderung meiner Familie erzählt, nicht wahr?"


play music music_drama fadein 2.0

"Sekunden vergehen, während ich versuche, Lillys Gesicht zu lesen. Ihr steht eine seltsame Mischung aus Gefühlen ins Gesicht geschrieben. Sie wirkt genervt, aber irgendwie auch verwirrt."


show bg suburb_shanghaiint onlayer master at bgleft
show lilly basic_reminisce_cas_close onlayer master:
    twoleft
    ypos 1.1
with charamove

show yuukoshang neutral_up onlayer master at tworight
with charaenter

yu "Ähm… bitteschön…"


"Yuuko platziert zögerlich unsere Getränke auf den Tisch, wobei ihre Präsenz seltsam klein wirkt."


hide yuukoshang onlayer master
with charaexit

show bg suburb_shanghaiint onlayer master at center
show lilly basic_reminisce_cas_close onlayer master:
    center
    ypos 1.1
with charamove

"Als sie nach einer schnellen, höflichen Verbeugung zurück zum Tresen geht, realisiere ich, dass die Atmosphäre zwischen mir und Lilly gespannt ist und unsere Gesichter irgendwie nachdenklich."


show lilly basic_displeased_cas_close onlayer master
with charachange

li "Obwohl sie sagt, dass ich mein eigenes Leben leben sollte, mischt sie sich zu den schlechtesten Zeitpunkten trotzdem ein…"


hi "Ich denke nicht, dass du Akira dafür die Schuld geben solltest. Sie gibt nur auf dich Acht, und ich kann ihre Bedenken darüber gut nachvollziehen."


show lilly basic_weaksmile_cas_close onlayer master
with charachange

"Lillys Ärger weicht einem peinlichen und überwiegend erfolglosen Versuch, ihre Gefühle zu verschleiern. Sie kann wirklich nicht gut damit umgehen, wenn sie über persönliche Angelegenheiten ausgefragt wird."


li "Ich weiß, aber… ich wollte einfach etwas mehr Zeit. Ich wusste, dass du es schließlich irgendwann herausgefunden hättest, aber…"


hi "Du hast es absichtlich vor mir geheimgehalten? Wie lange hattest du vor, das zu tun?"


show lilly basic_displeased_cas_close onlayer master
with charachange

li "Wie schon gesagt, ich wollte einfach mehr Zeit, um gründlich darüber nachzudenken. Ich wollte mir meiner Entscheidung sicher sein, bevor ich es dir erzähle."


hi "Und wofür hast du dich am Ende entschieden?"


"Ich weiß, was ich von ihr hören will, aber ich habe ein schreckliches Gefühl im Bauch."


show lilly basic_sleepy_cas_close onlayer master
with charachange

li "Meine Familie möchte innig, dass ich wieder zu ihnen zurückkehre, und Akira wird auch dorthin reisen. Ich könnte nach wie vor Lehrerin werden – hier und dort."


hi "Also… gehst du."


hi "Wie lange weißt du das schon? Ich weiß bereits, dass du gefragt wurdest, als du vor etwa einem Monat zum ersten Mal nach Schottland gereist bist."


show lilly basic_concerned_cas_close onlayer master
with charachange

li "Schon… etwas länger."


"Mein Frust droht überzukochen. Die Tatsache, dass sie das getan hat, trifft mich mehr als es sollte."


"Nicht nur, dass sie weggeht, sondern auch dass sie ihre Pläne bewusst vor mir geheimgehalten hat. Und das, nachdem sie so lange jemand zu sein schien, auf den ich mich bedingungslos verlassen konnte…"


"Es fühlt sich an, als würde ich den Boden unter meinen Füßen schneller verlieren, als ich mich darauf einstellen kann. Vielleicht ist das eher bloße Unsicherheit als Frust."


hi "Lilly…"


show lilly basic_sad_cas_close onlayer master
with charachange

li "Es tut mir leid, nur ich… wollte das genauestens überdenken. Ich wollte dich nicht ausnutzen, bitte…"


hi "Ich weiß, Lilly. Ich weiß. Nur kommt das wirklich plötzlich."


hi "Das heißt dann wohl, sobald du weg bist, ist es mit uns aus?"


"Seit ich sie kenne, habe ich sie nur sehr selten sprachlos gesehen. Dies ist einer dieser Momente."


"Sie sieht nicht überrascht aus. Ohne Zweifel weil sie sich dessen bewusst war, seit sie ihre Entscheidung getroffen hat, aber sie scheint sich nicht sicher zu sein, wie sie mit dieser Situation umgehen soll, nun da sie vor ihr liegt."


show lilly basic_oops_cas_close onlayer master
with charachange

li "W-Wir könnten eine Fernbeziehung versuchen. Immerhin werden sie heutzutage immer geläufiger…"


"Auch wenn sie es sagt, verrät ihre Stimmlage, dass sie nicht wirklich glaubt, was sie von sich gibt."


$ renpy.music.set_volume(0.5, 1.0, channel="music")
$ renpy.music.set_volume(0.05, 1.0, channel="ambient")

window hide
nvl clear
nvl show dissolve

n "\n\n\nLilly ist viel zu altmodisch, um eine Beziehung ohne jeglichen Körperkontakt auszuhalten – sogar ich bin das, in gewisser Weise. Alles, was wir für den jeweils anderen sein würden, wäre eine Stimme von der anderen Seite der Welt."


n "Letzten Endes ist es vergeblich, alles vernünftig betrachten zu wollen. Alle Versuche, die Zukunft mit der Vergangenheit in Einklang zu bringen, werden immer schwieriger, je mehr ich mich konzentriere."


n "Die stillen Momente, als wir einfach Seite an Seite umherliefen, die kostbare Zeit mit Hanako und Akira, die lockeren Unterhaltungen während unserer Mittagspausen, die Male, in denen wir uns geliebt haben, die Geständnisse unserer Gefühle…"


n "\n\n\nAlles zwecklos. Alles nur ein flüchtiger Moment in unserem jungen Leben."


$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show

hi "Wir sind nur zwei Kinder, die Erwachsene spielen, stimmt's?"


show lilly basic_sad_cas_close onlayer master
with charachange

"Eine lange, lange Stille liegt in der Luft zwischen uns. Der Lärm der anderen trinkenden und sich unterhaltenden Gäste macht die Situation nur noch seltsamer und unwirklicher."


"Lilly Gesicht bleibt gesenkt, während ihr deprimierter Gesichtsausdruck es verfinstert."


stop music fadeout 4.0

show lilly basic_concerned_cas_close onlayer master
with charachange

li "Es tut mir leid, Hisao."


"Eine schlichte Entschuldigung, und mehr nicht. Sie hat keine ausführlichere Antwort oder Erläuterung."


"Mit einem langem Seufzen nehme ich den Rest meiner Gedanken zusammen und stelle ihr die letzte Frage."


hi "Wann fährst du?"


show lilly basic_sad_cas_close onlayer master
with charachange

li "Ich fliege mit Akira, also in etwas weniger als einer Woche."


hi "Zum Anfang der Sommerferien?"


show lilly basic_sleepy_cas_close onlayer master
with charachange

li "Kurz danach, ja."


"Ihre Stimme ist ungewöhnlich langsam und stabil. Wahrscheinlich will sie die Emotionen in ihrer Stimme unterdrücken; dafür steht ihr das Bedauern umso deutlicher ins Gesicht geschrieben."


"Letzten Endes kann ich nicht einmal mein Versprechen halten, mit ihr zu Tanabata zu gehen, bevor sie abreist."


stop ambient fadeout 14.0
$ ksgallery_unlock("evul hisao_teacup")
show ev hisao_teacup onlayer master:
    truecenter
    zoom 0.85 subpixel True
    acdc_warp 15.0 zoom 0.8
with locationchange

"Ich schaue nach unten und sehe, wie mein Gesicht von der mittlerweile lauwarmen Tasse des vernachlässigten Tees vor mir reflektiert wird."


"Ich dachte wirklich, dass ich diesen Gesichtsausdruck hinter mir gelassen habe."


"Für eine Weile schaue ich lediglich hinab auf diese ruhige Oberfläche und versuche, meine Emotionen einzuordnen. Ich muss mir klar werden, welchen Weg ich ab jetzt einschlage – sei es genau jetzt oder in der Zukunft-"


"Aber – genau wie zuvor – ist die Anstrengung vergebens."


hide ev onlayer master
show lilly basic_reminisce_cas_close onlayer master
with locationchange

"Ich schaue kurz nach oben und sehe, wie Lilly klaglos langsam an ihrem kühlen Tee nippt. Ihr Gesicht ist angespannt und ihre Schultern hängen herab. Sie scheint auch tief in Gedanken versunken zu sein."
"Eine seltsam kalte Atmosphäre breitet sich zwischen uns aus, als wir beide in Gedanken versinken."


"Selbst als sich Lillys Tasse langsam leert, bleibt meine unberührt."


"Eine lange Zeit ist vergangen, bis ich bemerke, wie der Regen draußen nachlässt und die paar anderen Gäste des Shanghais gegangen sind."


scene bg school_dormhallway onlayer master
with shorttimeskip

stop ambient
play music music_moonlight fadein 0.5

"Die Kälte des sich schnell verdunkelnden Abends dringt durch die Flure des Wohnheimes. Während ich mich den Flur entlangschleppe, sehe ich vor mir eine unwillkommene Bewegung."


show kenji happy onlayer master:
    center
    xpos 0.4
    easein 0.5 xpos 0.5
with charaenter

"Ganz gewiss verkündigt das Öffnen der Tür, die meiner Gegenüberliegt, die Ankunft eines bebrillten Kenji."


ke "Hey Mann, was is…"


show kenji tsun onlayer master at center
with charachange

ke "Whoa Alter, du siehst furchtbar aus, glaube ich. Alles klar?"


"Er hat wirklich eine Gabe dafür, jede Situation zu verbessern."


hi "Ich… will nicht wirklich drüber reden. Es ist spät."


show kenji neutral onlayer master
with charachange

ke "Okay. Geht klar."


ke "Falls du je darüber reden willst, ich bin, du weiß schon, da."


"Ich sehe ihn eine Weile an, bevor ich meine ernste Fassade aufgebe und mich verlegen am Nacken kratze. Jetzt ist mir meine reservierte Antwort peinlich."


hi "Danke, Kenji."


show kenji happy onlayer master
with charachange

ke "Hey, ist okay. Dafür sind Freunde doch da, oder?"


hi "Ja, da hast du Recht. Ähm, bis dann."


scene bg school_dormhisao_ni onlayer master
with locationchange

"Ich öffne die Tür zu meinem eigenen Zimmer und schließe sie hinter mir, als er sich kurzerhand verabschiedet."


play sound sfx_doorslam

"Das laute Zuknallen der Tür besiegelt das Ende des Lebens, das ich seit meiner Ankunft an der Yamaku gelebt habe."


"Ich stehe lediglich in meinem dunklen Zimmer und versuche vergeblich zu ergründen, was ich von jetzt an tun soll."


"Was soll ich nur tun…?"


$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
stop music fadeout 2.0

scene black onlayer master
with dissolve



label de_L29:

scene bg school_scienceroom onlayer master
with locationchange

"Als der Unterricht endet, lasse ich meinen Kopf einfach auf meiner Hand ruhen und starre zum Zeitvertreib aus dem Fenster."


$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_normal fadein 2.0

window hide
nvl clear
nvl show dissolve

n "\n\nEs ist ein paar Tage her, seit mir Lilly von ihren Plänen erzählt hat. Seitdem bin ich nicht mehr zu unserem täglichen Mittagessenstreffen gegangen. Nicht, dass es noch etwas bringen würde."


n "Hanako ist nur noch mit dem Schülerzeitungsklub beschäftigt, seit sie ihm beigetreten ist. Sie hat sogar angefangen, sich ab und zu im Unterricht mit Naomi zu unterhalten."


n "Sogar Lilly hat sich, weil die Sommerferien anstehen, wegen ihrer Klassensprecherpflichten die Füße wundgelaufen. Wahrscheinlich auch einfach, weil sie dadurch einer peinlichen Begegnung mit mir aus dem Weg gehen will."


n "Und jetzt sind sie so gut wie da. Mit dem heutigen Erklingen der Glocke werden die Sommerferien beginnen."


n "\n\n\nIch schätze, dass ich am Ende meine Eltern besuchen und in meinem alten Zuhause herumlungern werde, jetzt wo meine bisherigen Pläne gänzlich schiefgegangen sind."


nvl clear

n "\n\nWährenddessen werden Akira und Lilly auf dem Weg nach Schottland sein, um den Rest ihres Lebens dort zu verbringen."


n "Egal wie sehr ich mir vorstelle, dass mein Leben wieder so wird, wie es einmal war, sobald die Sommerferien beginnen – es klappt einfach nicht. "


n "Alle schreiten in ihrem Leben voran. Lilly vereinigt sich wieder mit ihrer Familie, Akira steigt im Unternehmen ihres Vaters auf, Hanako findet neue Freunde und Hobbys, und sogar Yuuko kommt mit ihren Universitätsbestrebungen voran."


n "Am Ende schreite sogar ich voran. Mit meinen bisherigen Noten scheint einer Wissenschaftslehrer-Karriere trotz eines so holprigen Starts nichts im Wege zu stehen."


n "\n\nVermutlich sollte ich zumindest darüber glücklich sein, aber es scheint kaum zu helfen."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

window show

mi "Hicchan~!"

"Umgehend schrecke ich aus meinen Gedanken auf, wende mein Gesicht zu der quirligen Stimme neben mir und setze den fröhlichsten Gesichtsaufdruck auf, zu dem ich in der Lage bin."


show misha hips_smile onlayer master at twoleft
show shizu behind_smile onlayer master at tworight
with charaenter

"Wie erwartet flankiert Shizune sie. Ich habe die schleichende Vermutung, dass sie etwas von mir wollen."


hi "Hey Misha, Shizune. Was gibt's?"


show misha hips_grin onlayer master
with charachange

mi "Na ja~…"


show misha perky_smile onlayer master
with charachange

mi "Shicchan und ich dachten uns~…"


show misha sign_smile onlayer master
with charachange

mi "Da wir nur zwei arme, kleine Mädchen sind, die Hilfe mit all der Arbeit brauchen, die wir kurz vor Anfang der Sommerferien bekommen haben~…"


hi "Klar, ich kann helfen."


show misha perky_sad onlayer master
with charachange

mi "Aber Hicchan, wir brauchen wirkli-"


stop music fadeout 0.2

show misha perky_confused onlayer master
with charachange

mi "Was?"


"Ich glaube, ich habe Misha kaputtgemacht."


show shizu behind_blank onlayer master
with charachange

"Sogar Shizune hebt eine Augenbraue, als sie sieht, wie ihre Komplizin schaudernd still wird."


show misha hips_grin onlayer master
with charachange

mi "Also hilfst du uns, Hicchan?"


hi "Hab ich doch gerade gesagt, oder nicht?"


"Als hätte ich etwas anderes zu tun. Ihnen zu helfen, wird mich vielleicht auf andere Gedanken bringen."


"Misha scheint von meiner Antwort aufrichtig verzückt, doch Shizunes Gesicht ist betrübt und schwer zu lesen."
"Ich bemerke, wie ich zügig meine Augen von ihren abwende, als würde sie mich fast bemitleidend ansehen. Das ist sicher nur meine Einbildung."


scene bg school_council onlayer master
with shorttimeskip

play music music_daily fadein 0.5

"Das ist kaum das erste Mal, dass ich im Schülerratsraum bin. Tatsächlich war ich sogar oft hier – entweder um Lilly mit ihrer Klassensprecher-Arbeit zu helfen, oder um das eine oder andere mit dem Schülerrat selbst zu besprechen."


"Nun ist es allerdings… ein recht anderer Ort."


show sc_comp onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Papiere und Ordner sind über jeden Tisch im Raum verteilt. Nur ein einzelner kleiner schwarzer Laptop auf einem Tisch sticht aus der Unordnung hervor."


"Er sieht uralt aus, und ich schätze, dass er seine Aufgabe, Informationen zu archivieren, Jahre über Jahre tapfer ausgeführt hat."


show sc_comp onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide sc_comp onlayer master
with None

hi "Also, was steht an? Sieht aus, als gäbe es eine Menge zu tun."


show misha hips_smile onlayer master at twoleft
show shizu behind_frown onlayer master at tworight
with charaenter

shi "…"


"Shizune setzt eine entschlossene Miene auf, als sie gebärdet. Ein besorgniserregender Anblick."


show misha hips_grin onlayer master
with charachange

mi "Alles, Hicchan!"


"Meine Besorgnis war wohl berechtigt."


hi "Alles… sagst du?"


show shizu basic_normal onlayer master
with charachange

shi "…"


show misha sign_smile onlayer master
with charachange

mi "Was noch auf den Tischen liegt, muss gemacht werden."


show misha perky_smile onlayer master
with charachange

mi "Es muss alles digital übertragen werden. Dafür ist der Laptop da."


hi "Und ich schätze, dass das an mir hängenbleibt?"


show shizu behind_smile onlayer master
with charachange

shi "…"


show misha hips_smile onlayer master
with charachange

mi "Shicchan sagt, sie hat dich vor ein paar Tagen mit den Computern in der Bibliothek gesehen, und dass du total gut mit ihnen umgehen konntest~."


"Gut mit Computern? Ich kann zwar Tippen ohne hinzusehen, aber es klingt immer noch nach einer Überschätzung meiner Fähigkeiten."


hi "Ich hab nur Hausaufgaben abgetippt…"


hi "Warte – Shizune hat mir dabei zugesehen?"


show shizu adjust_smug onlayer master
with charachange

shi "…"


show misha sign_smile onlayer master
with charachange

mi "Man muss seine Verbündeten kennen, bevor man seine Feinde kennen kann, was denkst du denn~."


show misha cross_grin onlayer master
with charachange

mi "Wow, ziemlich weise…"


"Ausnahmsweise ist es mal nicht sehr schwer herauszufinden, wer was gesagt hat."


"Nichtsdestotrotz bringt es wohl nichts, sich darüber zu streiten. An einem Computer zu sitzen und etwas zu tippen, ist wohl kaum so lästig wie die Aufgaben, mit denen Shizune und Misha sonst aufwarten."


show shizu basic_normal onlayer master
with charachange

shi "…"


show misha perky_smile onlayer master
with charachange

mi "Außerdem wird es dir helfen, deinen Kopf freizukriegen~."


hi "Meinen Kopf freikriegen? Wovon meinen Kopf freikriegen?"


show misha perky_confused onlayer master
with charachange

"Misha schaut verblüfft drein, als sie es für Shizune übersetzt, aber Shizune antwortet nur mit einer kurzen Geste und lässt dann ihren Blick durch das Fenster schweifen."


show shizu behind_blank onlayer master
with charachange

shi "…"


show misha sign_smile onlayer master
with charachange

show shizu basic_normal2 onlayer master
with charachange

"Misha setzt umgehend wieder ein Lächeln auf, als sie zurückübersetzt. Sie war wohl verwirrt, aber Shizune ist schwieriger zu interpretieren."


show misha cross_smile onlayer master
with charachange

mi "Ich dachte mir nur, dass du du vielleicht an etwas anderes als die Prüfungen denken willst, versteht sich~."


hi "So oder so, wir sollten lieber gleich als später anfangen. Da bin ich eurer Meinung."


show misha hips_smile onlayer master
with charachange

mi "Das ist die richtige Einstellung, Hicchan~!"



























scene bg school_council onlayer master
with shorttimeskip

"Und somit ist die fünfte Tabelle erstellt und gespeichert. Zeit für die…"


"Nach ein bisschen Herumwuseln haben wir es geschafft, alles etwas zu sortieren."


"Shizune hat die losen Blätter eingesammelt und sie – glücklicherweise – neben mir zu einem ordentlichen Stapel sortiert."
"Währenddessen hat sich Misha um das Handschriftliche gekümmert, wobei ihr mädchenhafter, pinker Stift Blatt für Blatt seine unverkennbare Signatur hinterlassen hat."


"Als ich erst einmal den Rhythmus gefunden hatte, war es gar nicht mehr so schlimm. Shizune und Misha scheinen auch mit Elan dabei zu sein. Wortlos kommunizieren sie, während sie sich mit Eifer ihrer Arbeit widmen."


"Regelmäßig werfe ich einen Blick auf das Blatt neben dem Laptop, während ich pflichtbewusst die darauf enthaltenen Daten eingebe."
"Anscheinend ist es eine Liste von Schülernamen und passenden Adressen. Ich widme dem, was ich tippe, nicht viel Aufmerksamkeit, bis ich ungefähr in der Mitte der Seite ankomme."


"Hakamichi… Klasse 3-3 hm… Ihre Familie wohnt in Saitama."


"Meine Neugier wird abrupt unterbrochen, als jemand dreimal leicht an die Tür klopft."


show misha perky_smile onlayer master:
    twoleft
    xpos 0.4
    easein 0.5 twoleft
with charaenter

"Rasch eilt Misha hinüber, um nachzusehen, wer es ist. Auf dem Weg dorthin tippt sie Shizune auf die Schulter, um ihre Freundin wissen zu lassen, was gerade passiert."


show misha hips_grin onlayer master at twoleft
with charachange

mi "Ah, du bist hier~."


hi "Hmm? Wer ist es denn?"


"Nach einer kurzen Pause, um Shizunes und all die anderen Daten in die Datei zu schreiben, schaue ich zur Tür."


stop music fadeout 0.5

show lilly invis onlayer master:
    left
    xpos -0.2
with None

show bg school_council onlayer master at bgright
show misha hips_grin onlayer master at center
show lilly basic_weaksmile_cas onlayer master at left
with dissolvecharamove

"… Lilly?"


"Nachdem sie Misha zur Begrüßung flüchtig zunickt, richtet sie auf ihre typische Art ihren Kopf auf."


show lilly basic_surprised_cas onlayer master
with charachange

li "Ist das Hisao?"


"Sie ist mittlerweile verflixt gut darin, meine Stimme an den kürzesten Sätzen zu erkennen."


hi "Ja, ich bin's. Ähm… Hi."


show lilly basic_reminisce_cas onlayer master
with charachange

"Als sie sich verbeugt, herrscht eine leicht peinliche Atmosphäre. Keiner von uns weiß, wie wir uns in Gegenwart des anderen verhalten sollen. Immerhin reist sie schon in ein paar Stunden ab."


"Gott sei Dank ist das etwas, das weder die unaufmerksame Misha noch die fleißige Shizune bemerken."


hi "Also… hast du auch etwas zu erledigen?"


show lilly basic_sleepy_cas onlayer master
with charachange

li "Unglücklicherweise. Ich bin gekommen so schnell ich konnte, aber meine Klasse hielt für mich eine Überraschungsabschiedsparty, und ich musste mich umziehen."


"Ich werfe einen Blick auf die Uhr des Laptops. Es ist so ungefähr das Ende der Mittagspause, also vermute ich, dass Lilly es auch geschafft hat, sich aus der letzten Unterrichtsstunde herauszuwinden."


show lilly basic_weaksmile_cas onlayer master
with charachange

li "Ich nehme an, dass Shizune auch hier ist?"


play music music_shizune fadein 3.0

show shizu behind_blank onlayer master at right
with charaenter

shi "…"


show misha cross_smile onlayer master
with charachange

mi "Na klar!"


show shizu adjust_smug onlayer master at right
with charachange

shi "…"


show misha sign_smile onlayer master
with charachange

mi "Und ich bin auch die ganze Mittagspause hier gewesen!"


"Dieser letzte Kommentar war wirklich nicht nötig. Shizune lockt Lilly in einen weiteren Streit, ich kann es spüren."


show lilly basic_displeased_cas onlayer master
with charachange

li "Tut mir leid, dass ich nicht so fleißig sein kann wie du, Shizune. Ich bemühe mich darum, mehr Lakaien einzustellen, die in Zukunft meine Arbeit erledigen – das versichere ich dir."


"Und Lilly hat den Köder geschluckt und eskaliert."


show shizu basic_frown onlayer master
with charachange

shi "…"


show misha hips_frown onlayer master
with charachange

mi "Aber bist du nicht diejenige, die die Arbeit auf ihre Klassenkameraden abwälzt~?"


show lilly basic_listen_cas onlayer master
with charachange

li "Der Unterschied ist, dass sie von sich aus helfen wollen – anders als dein tyrannischer Griff um deine eigene Klasse."


show shizu behind_frown onlayer master
with charachange

shi "…"


show misha cross_smile onlayer master
with charachange

mi "Tyrannei funktioniert~! Auch wenn wir die Dinge anders angehen, kriegen wird trotzdem die gleichen Resultate, oder~?"


show lilly basic_displeased_cas onlayer master
with charachange

li "Das ist eine Schule, kein Polizeistaat. Ich kann mich leider nicht erinnern, wann du zum Klassenmonarch gewählt worden bist."


show shizu cross_angry onlayer master
with charachange

shi "…"


show misha cross_frown onlayer master
with charachange

mi "Macht muss man ergreifen~! Sie ist wertlos, wenn sie einem in die Hand gegeben wurde~! Aber ich schätze, das würdest du wohl nicht wirklich verstehen, richtig~?"


show shizu adjust_angry onlayer master
with charachange

shi "…"


show misha hips_smile onlayer master
with charachange

mi "Du wirst mich auch daran erinnern müssen, wann Monarchen auf ihre Positionen gewählt wurden."


"Offensichtlich ist Lilly empört. Shizunes Zwei-Treffer-Kombination zwingt sie in die Defensive."


show lilly basic_displeased_cas onlayer master
with charachange

li "Und doch schaffst du es mit all deiner vielgepriesenen Macht nicht, auch nur eine Person zum Helfen zu bewegen, ohne sie dazu zu zwingen."


show shizu behind_frustrated onlayer master
with charachange

shi "…"


show misha sign_smile onlayer master
with charachange

mi "Aber Hisao hat sich freiwillig gemeldet~! Anstatt sich bedeutungslosen Teekränzchen zu widmen, arbeitet er lieber hart, stimmt's~?"


show lilly basic_listen_cas onlayer master
with charachange

li "Ist das so, Hisao?"


"Ah, das ist übel. Jetzt stecke ich wirklich in der Zwickmühle."


"So sehr es mir auch wehtun mag, die Wahrheit hat zumindest eine Chance, diesen Streit hier und jetzt zu beenden."


hi "Schon okay, Lilly, sie haben mich nicht bedrängt oder so."


show lilly basic_displeased_cas onlayer master
with charachange

"Lilly schneidet eine missbilligende Grimasse, und ich kann ihren brausenden Unmut mir gegenüber spüren."


"Wenn sie will, kann sie ziemlich furchteinflößend sein – auch wenn das glücklicherweise seltener vorkommt."


show shizu cross_angry onlayer master
with charachange

shi "…"


show misha hips_frown onlayer master
with charachange

mi "Hicchan, du lässt es klingen, als wäre das eine Regelmäßigkeit~…"


hi "Ist es das nicht?"


hi "Am Ende ist es doch egal, solange alles rechtzeitig erledigt wird. Lasst uns einfach damit fertig werden, damit wir nach Hause gehen können."


hide shizu onlayer master
with charaexit

hide lilly onlayer master
with charaexit

hide misha onlayer master
with charaexit

"Shizune schnaubt verächtlich und wendet sich wieder dem Markieren des vor ihr liegenden Blattes zu, während Lilly seufzt und sich mit einer Hand an den an der Wand aufgereihten Aktenschränken durch den Raum navigiert."


"Das wäre das erste Mal, dass ich es geschafft hätte, eine dieser Situationen erfolgreich zu entschärfen, aber der widerwillige Waffenstillstand, basierend auf gegenseitiger Angst und Respekt, ist eher wie ein Kalter Krieg als ein wahrer Frieden."


"Aber das kann ich nicht nur mir anrechnen; Lillys Abreise hat Shizune sicherlich auch ein wenig beeinflusst, dass sie so einfach aufgibt."


show bg school_council onlayer master at center
with charamove

show lilly basic_listen_cas onlayer master at center
with charaenter

"Augenblicke bevor ich wieder zurück an meine Arbeit gehe, bemerke ich, wie Lilly nach oben greift, um an etwas oberhalb des Aktenschranks heranzukommen. Ich biete fast meine Hilfe an, aber sie ist groß genug, um es selbst sicher herunterzunehmen."


show lilly basic_displeased_cas onlayer master:
    ypos 1.15
with dissolvecharamove

"Sobald sie das seltsam geformte Gerät auf den Schreibtisch neben mich stellt und die alte, grüne Abdeckung entfernt, begreife ich erst, was es ist… mehr oder weniger…"


show brailler onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Auf den ersten Blick scheint es eine alte, metallisch-blaue Schreibmaschine zu sein, aber ich brauche nicht lange, um zu erkennen, dass sie alles andere als gewöhnlich ist."


"Sie hat viel weniger Tasten als erwartet, und die, die sie hat, haben keine Buchstaben aufgedruckt. Nur die Schatten, geworfen von den kleinen Braille-Punkten auf ihnen, lassen den Zweck dieses Dings erahnen."


hi "Eine Blindenschreibmaschine?"


show lilly basic_smile_cas onlayer master
with None 

show brailler onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide brailler onlayer master
with None

li "Oh, das? Nun, du liegst gar nicht so daneben."


li "Normalerweise nennt man es eine Punktschriftmaschine, aber im Grunde ist es eine Schreibmaschine für Blinde, ja. Sie presst Braille anstatt Text auf die Seite; deswegen hat sie auch weniger Tasten."


hi "Wow… echt cool."


show lilly basic_cheerful_cas onlayer master
with charachange

"Als Antwort auf meine Neugier darüber schenkt sie mir ein fröhliches Grinsen. Ich muss zugeben, dass mich so etwas Neuartiges reizt."


hide lilly onlayer master
with charaexit

"Ohne Weiteres wenden wir uns wieder unseren zugeteilten Aufgaben zu. Das laute Klicken der Mechanik in Lillys Punktschriftmaschine und das Getippe auf der alten Tastatur des Laptops erfüllen schnell den Raum."


"Es ist wirklich eine schöne Atmosphäre. Jeder weiß, was er zu tun hat, und Lilly und ich können nebeneinander sitzen und gelegentlich Worte austauschen, während wir alles abarbeiten."


"Nostalgisch. So fühlt es sich an."


"Es ist angenehm, aber ein wenig von dem Wissen befleckt, dass unsere gemeinsame Zeit sich dem Ende nähert."


show lilly basic_smile_cas onlayer master:
    center
    ypos 1.15
with charaenter

li "Misha, könntest du mir kurz helfen?"


show bg school_council onlayer master at bgleft
show lilly basic_smile_cas onlayer master:
    twoleft
    ypos 1.15
with charamove

show misha hips_smile onlayer master at tworight
with charaenter

"Um anständig mit ihr reden zu können, eilt Misha vom Aktenschrank, den sie gerade noch durchsucht hat, zu ihr – ungeachtet Lillys mangelnder Sicht. Einen Moment lang finde ich es seltsam, doch dann wird mir klar, dass ich genau dasselbe tue."


mi "Was gibt's?"


show lilly basic_weaksmile_cas onlayer master
with charachange

li "Könntest du Shizune fragen, wo die Anwesenheitslisten für die Klasse 3-2 sind? Ich glaube, sie wurden woanders hingeräumt."


show misha hips_grin onlayer master
with charachange

mi "Okie dokie!"

hide misha onlayer master
with charaexit

stop music fadeout 8.0

"Daraufhin wuselt sie hinüber zu Shizune, die am Tisch hinter uns arbeitet."


"Lillys Vertrautheit mit dem Schülerratsraum und ihre Arbeitseffizienz erinnern mich daran, dass sie, Misha und Shizune früher einmal im Schülerrat zusammengearbeitet haben."


"Vielleicht ist das ein passendes Ende für ihren Aufenthalt an der Yamaku; einfach Dinge wie früher abarbeiten, umgeben von denen, die sie liebt – oder zumindest mochte."


"Ich sehe auf und werde von dem Anblick überrumpelt. Nicht Misha, sondern Shizune wühlt durch eine Schublade."


show shizu behind_blank onlayer master at tworight
with charaenter

"Tatsächlich zupft sie eine Aktenmappe heraus, die abgesehen von den kaum sichtbaren Hügelchen auf dem Deckblatt komplett leer ist, und hält sie Lilly entgegen."


"Lillys Hand huscht darüber, um zu überprüfen, was es ist. Ihre Finger ertasten die Braillepunkte und bestätigen, dass es das ist, wonach sie gefragt hat."


show lilly basic_smile_cas onlayer master
with charachange

li "Ich danke dir, Misha."


"Keine Antwort."


show shizu behind_smile onlayer master
with charachange

"Keine Antwort, nur… ein seltsames Grinsen… nein… Lächeln… auf Shizunes Gesicht."


show ev lilly_sheets onlayer master:
    truecenter
    zoom 1.05 subpixel True
    easein 10.0 zoom 1.0
with whiteout

"Ein paar Sekunden vergehen, bis es bei Lilly merkt, dass nicht Misha, sondern Shizune hinter ihr steht. Ihr kurzer, überraschter Blick wird zu einem leicht verlegenem Lächeln."


"Für einen Moment ist der Raum fast komplett Still."


"Aber dann schreitet Shizune zurück zu ihrem Arbeitsplatz, und Lilly beginnt wieder zu tippen."


"Es hat insgesamt nur ein paar Sekunden gedauert, aber es fühlt sich an, als wären Jahre der Kommunikation in diesem stillen Austausch nachgeholt worden."


scene bg school_council_ss onlayer master at right
with shorttimeskip

play music music_tranquil fadein 3.0

hi "So, fertig."


"Ich lasse meinen Kopf nach hinten fallen und reibe meine Augen, um die Müdigkeit loszuwerden. Auf diesen kleinen und eher minderwertigen Bildschirm zu starren, hat seinen Tribut gefordert."


show lilly basic_smile_cas_ss onlayer master:
    center
    ypos 1.15
with charaenter

li "Exzellentes Timing; das Einzige, was ich noch tun muss, ist die hier wegzuheften, dann habe ich meine Arbeit auch erledigt."


hi "Gut. Währenddessen kann ich ja die Punktschreibmaschine einpacken und wegräumen."


show lilly basic_smileclosed_cas_ss onlayer master
with charachange

li "Danke, Hisao."


hi "Misha, braucht ihr noch lange?"


"Ich sehe mich nach den beiden um, während ich die Abdeckung auf die Punktschreibmaschine setze, nur um sie an der Tür warten zu sehen. Ich schätze, sie warten auf uns."


scene bg school_council_ss onlayer master at left
show misha hips_smile_ss onlayer master at center
show shizu behind_blank_ss onlayer master at right
show lilly basic_smileclosed_cas_ss onlayer master at left
with shorttimeskip

"Ohne weitere Zeit zu verschwenden, sortieren und packen wir alles Übriggebliebene ein und gesellen uns hinzu."


hi "Danke, dass ihr beide gewartet habt."


show misha hips_grin_ss onlayer master
with charachange

mi "Wir konnten nicht einfach ohne dich gehen, Hicchan. Du warst eine große Hilfe!"


show shizu behind_smile_ss onlayer master
with charachange

"Shizune nickt zustimmend, sichtlich zufrieden mit meinen Bemühungen."


hi "Ich schätze… das war dann wohl die letzte Klassensprecherarbeit."


show lilly basic_smile_cas_ss onlayer master
with charachange

li "Das stimmt."


show misha perky_sad_ss onlayer master
with charachange

mi "Ich werde dich vermissen, Lilly. Es hat mir Spaß gemacht, mit dir zu arbeiten."


show lilly basic_weaksmile_cas_ss onlayer master
with charachange

li "Danke, Misha. Es war auch schön, mit dir zu arbeiten… und mit Shizune."


show shizu basic_normal_ss onlayer master
with charachange

"Shizune denkt einen Moment lang nach, bevor sie ihre Antwort formuliert. Nicht, dass sie oft ohne nachzudenken kommunizieren würde, im Gegenteil, aber diesmal überlegt sie sogar noch länger."


show shizu adjust_smug_ss onlayer master
with charachange

shi "…"


show misha perky_confused_ss onlayer master
with charachange

"Misha schaut etwas überrascht drein, bevor sie die Botschaft übermittelt."


show misha hips_smile_ss onlayer master
with charachange

mi "Shizune sagt… du sollst deine Arbeit dort drüben gefälligst besser machen als hier."


show lilly basic_giggle_cas_ss onlayer master
with charachange

"Ohne es ihr auch nur ein bisschen übelzunehmen, kichert Lilly in ihre Hand."


show lilly basic_smileclosed_cas_ss onlayer master
with charachange

li "Wenn das der Fall ist, dann sag Shizune bitte, dass sie denen, die noch hierbleiben, in Zukunft etwas mehr Verständnis entgegenbringen soll."


"Wetteifernd bis zum Ende. Vielleicht sind Shizune und Lilly letztendlich doch nicht so verschieden."


show shizu behind_smile_ss onlayer master
with charachange

shi "…"


show misha hips_grin_ss onlayer master
with charachange

mi "Shicchan sagt, dass sie sicherheitshalber überprüfen wird, ob du deinen Teil des Versprechens einhältst."


show lilly basic_cheerful_cas_ss onlayer master
with charachange

li "Dann soll sie das tun."


show lilly basic_smile_cas_ss onlayer master
with charachange

li "Ich mache mich dann besser auf den Weg. Lebwohl, Shizune. Lebwohl, Misha."


show lilly basic_smileclosed_cas_close_ss onlayer master
with characlose

li "Hisao?"


"Lilly verhakt ihren Arm mit meinem, da sie keinen Blindenstock braucht, solange ich da bin, um sie zu führen. Mit einem letzten Nicken zu den beiden schreiten wir aus der Tür und machen uns auf den Weg zum Schulgelände."


"Als ich mich umdrehe, um ihnen zum Abschied zu winken, bemerke ich, dass Shizunes Blick auf Lilly ruht. Sie mögen sich zwar auf die Nerven gehen, aber Familienbande reißen nicht so leicht."


scene bg school_courtyard_ss onlayer master
with locationskip

hi "Hast du all deine Papiere bereit?"


show lilly basic_smileclosed_cas_ss onlayer master at center
with charaenter

li "Ja, alle wurden ausgefüllt und eingereicht."


hi "Wie immer alles im Griff, nicht wahr?"


show lilly basic_weaksmile_cas_ss onlayer master
with charachange

stop music fadeout 4.0

"Auf dieses Kompliment hin lächelt sie mir warm zu, aber es fühlt sich an, als wäre ihr Glück nur eine Fassade über der Tatsache, dass sie sich vollkommen bewusst ist, wie viel sie zurücklässt."


"Es erinnert mich daran, wie sie war, als ich ihr zum ersten Mal begegnet bin; immerzu am Lächeln, immer ein wenig reserviert, immer diese kleine Distanz zwischen ihr und allem anderen."


"Sogar jetzt behält sie dieses Auftreten bei vielen anderen bei. Besonders bei denen, die ihr nicht nahestehen. Ich hatte gehofft, dass unsere Zeit zusammen das geändert hat."


scene bg school_gardens_ss onlayer master
with locationchange

"Unser Lauftempo verringert sich, bis wir beide in dem gänzliche leeren Schulgarten zum Stillstand kommen."


show lilly basic_weaksmile_cas_ss onlayer master at center
with charaenter

li "Hisao? Stimmt etwas…"


play music music_comfort

show lilly basic_surprised_cas_close_ss onlayer master
with vpunch

"Lillys Worte werden abgewürgt, als ich mich zu ihr drehe, sie in den Arm nehme und fest an mich ziehe. Normalerweise neige ich nicht zu solch impulsiven Handlungen, aber ich will sie einfach nah bei mir haben – auch wenn es das letzte Mal ist."


"All die anderen Schüler haben sich in die Wohnheime zurückgezogen oder sind nach Hause gefahren. Nur die in der Brise rauschenden Blätter sind zu hören."


show ev lilly_touch_cas onlayer master
with charachange

"Als ich zurückweiche, kann ich sehen, dass ihr sonst so sorgfältig gepflegtes Lächeln verschwunden ist."


"Ihr Hand zögert, als ob sie nicht wüsste, ob sie auf meinem Gesicht bleiben will oder nicht."


"Sie gibt sich tapfer, aber ihr leichtes Zittern verrät sie. Lilly mag sich selbst gut im Griff haben, aber sogar sie kann gerade nicht gelassen bleiben."


"Das ist die Frau, in die ich mich verliebt habe, aber auch die, die in allzu kurzer Zeit das Land für immer verlassen wird."


li "Es tut mir leid, Hisao."


hi "Schon okay. Immerhin musst du dein eigenes Leben leben."


scene bg school_girlsdormhall onlayer master
with shorttimeskip

"Hand in Hand laufen wir zusammen durch den Flur der Mädchenwohnheime. Unsere Emotionen sind mittlerweile größtenteils bezwungen. Nichtsdestotrotz umklammern sich unsere Hände viel fester als zuvor."


"Leise, gedämpfte Stimmen sind aus Lillys Zimmer zu hören, deren Ursprung auch nicht schwer zu erraten ist."


scene bg school_dormlilly onlayer master

show hanako invis onlayer master at tworight
show lilly invis onlayer master at twoleft
with locationchange

show lilly basic_weaksmile_cas onlayer master at twoleft
show hanako emb_downsad onlayer master:
    xpos 0.4 xanchor 0.5
with dissolvecharamove

show lilly basic_surprised_cas onlayer master
with vpunch

"In dem Augenblick, in dem sie die Tür öffnet, stürmt zu Lillys offensichtlicher Überraschung Hanako hindurch und wickelt ihre Arme um sie. "


ha "Lilly! Lilly!"

show lilly basic_oops_cas onlayer master
with charachange

li "Ha-Hanako…?"

show hanako emb_downtimid onlayer master
with charachange

ha "Ich werde dich vermissen… Lilly…"


show lilly basic_weaksmile_cas onlayer master
with charachange

"Wie erwartet ist sie den Tränen nahe. Lilly erwidert das, indem sie sanft Hanakos Haar streichelt, sich dann von ihr löst und ihr ein warmes, ermutigendes Lächeln schenkt."


show akira invis onlayer master:
    right
    ypos 1.15
with None

show akira basic_lost onlayer master at right
with dissolvecharamove

"An Hanako vorbei kann man sehen, wie Akira von der Kante von Lillys Bett aufsteht und sich am Kopf kratz."


show akira basic_smile onlayer master
with charachange

"Ihre Augen springen von Lilly zu Hanako und dann zu mir. Ein gekünsteltes Lächeln ruht auf ihrem Gesicht. Ich versuche, einen aufrichtigeren, fröhlicheren Blick zu erwidern, aber das Resultat ist wahrscheinlich dasselbe."


show akira basic_boo onlayer master
with charachange

aki "Also, alles bereit? Konntest du es dir verkneifen, Shizune umzubringen?"


show lilly basic_giggle_cas onlayer master
with charachange

"Diese Bemerkung entlockt ihrer Schwester ein erfreutes Kichern."


li "Ja, ich habe alles dabei, und ja, konnte ich. Hast du alles eingepackt, was du brauchst?"


show akira basic_smile onlayer master
with charachange

aki "Hab die beiden Taschen dabei, aber es liegt noch einiges Zeug im Haus der Hakamichis. Das kann ich einpacken, während wir dort auf den Flug morgen Abend warten."


"Akira verpasst den beiden großen schwarzen Reisetaschen auf dem Boden einen herzhaften Klaps. Wahrscheinlich ist sie gekommen, um beim Packen zu helfen und sicherzustellen, dass von Lillys Seite alles geklärt ist, bevor sie abfahren."


show hanako cover_worry onlayer master at center
with dissolvecharamove

ha "Lilly… wirst du dort drüben… zurechtkommen?"


show lilly basic_smileclosed_cas onlayer master
with charachange

li "Es wird alles gut gehen, das versichere ich dir. Akira wird auch auf mich aufpassen, und du weißt, dass sie zuverlässig ist."


show hanako basic_worry onlayer master
with charachange

ha "Aber…"


show lilly basic_smile_cas onlayer master
with charachange

li "Keine Sorge, Hanako. Schließlich habe ich deine Telefonnummer, also können wir in Verbindung bleiben. Mit Akiras Hilfe könnte ich dir auch ein paar Sachen über das Internet schicken."


show akira basic_boo onlayer master
with charachange

aki "Hey, benutz mich nicht, nur weil du nicht lernen willst, wie man einen Computer bedient."


show lilly basic_giggle_cas onlayer master
show hanako basic_smile onlayer master
with charachange

"Hanako und Lilly kichern kurz, wodurch die Stimmung ein bisschen aufgelockert wird."


show lilly basic_smileclosed_cas onlayer master
with charachange

li "Allerdings gilt dasselbe für dich, Hisao. Ich verspreche dir, dass ich mich bei dir melden werde, sobald ich in Schottland bin."


hi "Ich weiß. Ich freue mich darauf."


"Ihr Angebot mag lieb sein, aber wir beide wissen, dass es gleichbedeutend mit Schluss machen ist. Keiner von uns bildet sich irgendwie ein, dass eine Fernbeziehung funktionieren würde."


"Ohne dass jemand das Signal dazu gibt, begeben wir Vier uns schweigend auf den langen Weg zum Schultor."


scene bg school_gate_ni onlayer master at bgleft
with shorttimeskip

"Die zahlreichen, auf dem Gelände verteilten Lampen werfen in der ansonsten dichten Dunkelheit nicht mehr als ein paar vereinzelte Lichtkegel auf den Boden."


"Ein direkt vor der Schule auf der Straße geparktes Auto kommt in Sichtweite. Sein glänzend schwarzes Exterieur reflektiert die schwach leuchtenden Lampen der Yamaku. Ich spreche Akira an, um die schwere Stimmung etwas zu heben."


hi "Dein Auto? Was für eins ist es?"


show akira basic_smile_ni onlayer master at center
with charaenter

aki "Du hast nicht viel Ahnung von Autos, oder? Es ist ein Lancer Evo. Robust und schnell."


"Na ja, es ist nicht so, als würde sie mit ihrem Kommentar über mein Wissen danebenliegen. Ich habe mich nie wirklich dafür interessiert."


show akira basic_resigned_ni onlayer master
with charachange

"Sie seufzt leise."


show akira basic_lost_ni onlayer master
with charachange

aki "Sie ist ein gutes Auto gewesen. Morgen muss ich mich von ihr trennen, genauso wie von dem Sommerhaus. Ihr wart die Letzten, die es besucht haben, bevor es den Eigentümer gewechselt hat."


"Ich gebe meinen fehlgeschlagenen Smalltalkversuch auf und werfe einen Blick auf Hanako und Lilly, die uns folgen."


show akira basic_lost_ni onlayer master at tworight
show bg school_gate_ni onlayer master at center
with charamove

show hanako emb_downtimid_ni onlayer master:
    xpos 0.4 xanchor 0.5
show lilly basic_weaksmile_cas_ni onlayer master at twoleft
with charaenter

"Eigentlich sollte Hanako Lilly führen, aber es ist eher andersherum, da sie sich fest an Lillys Arm klammert."


"Ein deprimierender Anblick."


show akira basic_resigned_ni onlayer master
with charachange

aki "So… Ich schätze, das war's dann."


show lilly basic_reminisce_cas_ni onlayer master
with charachange

li "Allerdings."


"Auch wenn jetzt der Zeitpunkt gekommen ist, an dem jeder sein Lebewohl sagen sollte, will niemand wirklich den ersten Schritt machen. Als würden sich die Chancen verbessern, dass sie hier bleiben, je länger niemand etwas sagt."


show hanako emb_downsad_ni onlayer master
with charachange

ha "Lilly… musst du wirklich gehen?"


show lilly basic_concerned_cas_ni onlayer master
with charachange

li "Es tut mir leid, Hanako. Aber ich werde dich nicht für immer verlassen; ich kann dich immer noch anrufen. Hisao wird auch noch hier sein."


"Ich nicke, doch Hanako klammert sich nur noch fester an Lillys Arm."


"Nachdem man so viel Zeit ohne jemanden verbracht hat, den man eine Familie nennen konnte, muss Lebewohl zu dieser Person zu sagen qualvoll sein. Diese Person, die so nah an eine Mutter heranreichte, wie es je jemand in ihrem Leben konnte. "


show lilly basic_sad_cas_ni onlayer master
with charachange

"Lilly lässt einen langen, traurigen Atemzug entweichen. Alles, was ich und AKira wirklich tun können, ist still am Rande zu stehen, da die einzige Person, die das lösen kann, Lilly selbst wäre."


"Schließlich zieht Lilly ihren Arm aus Hanakos griff und hält sie sanft an beiden Schultern. Bisher wohl die entschlossenste Art von Lilly, Hanako anzusprechen."


show lilly basic_reminisce_cas_ni onlayer master
with charachange

li "Hanako, erinnerst du dich an unsere erste Begegnung?"


show lilly basic_weaksmile_cas_ni onlayer master
with charachange

li "Als du zum ersten Mal in mein Zimmer gekommen bist, nachdem du gehört hast, wie ich einen Freund tröstete, hast du die ganze Nacht lang nicht ein einziges Wort gesagt."
li "Sogar als ich dir Tee eingeschenkt und mit geredet habe, hast du still dagesessen und hast einfach nur zugehört, was ich dir erzählt habe."


li "Es brauchte viele solcher stillen Treffen, bis du begonnen hast, dich mir zu öffnen. Aber als es soweit war, war das für mich einer der glücklichsten Momente überhaupt."


show lilly basic_sleepy_cas_ni onlayer master
with charachange

li "Ich bin nicht deine Freundin geworden, weil ich dich bemitleidet habe, Hanako. Ich bin deine Freundin geworden, weil ich wusste, dass du dich nicht nur vor mir, sondern vor allen versteckst."


li "Deine Ambitionen, deine Persönlichkeit, deine Interessen, deine Geschmäcker… Ich kannte nichts davon, und sonst kannte sie auch niemand."


show lilly basic_weaksmile_cas_ni onlayer master
with charachange

li "Aber als du dich mir gezeigt hast, fing ich an zu begreifen, was für ein Mensch du bist, und ich war mir sicher, dass unser Treffen ein ganz besonderer Moment war."


show hanako emb_blushtimid_ni onlayer master
with charachange

ha "Aber ich…"


"Lilly unterbricht sie, indem sie ihre Hand auf Hanakos Kopf legt, ihr den Pony zur Seite streicht und sanft ihre Lippen auf Hanakos Stirn presst."


show lilly basic_smile_cas_ni onlayer master
with charachange

"Als sie ihren Kopf zurücknimmt, steht Hanako sprachlos und mit feuchten Augen da. Lilly hingegen mit einem strahlenden und breiten Lächeln."


li "Ich glaube, dass du ein sehr schöner Mensch bist, Hanako, und ich bin mir sicher, dass du eine starke und unabhängige Frau werden wirst."


li "Du bist mir eine sehr liebe Freundin, und jemand, den ich sehr liebe. Genau wie Hisao werde ich dich nicht vergessen, solange ich lebe."


show lilly basic_smileclosed_cas_ni onlayer master
with charachange

li "Ich mag zwar gehen, aber du hast hier dein eigenes Leben zu führen. Genau wie ich es tue, hast du deine eigenen Freunde und Hobbys, und deine Pläne für nach dem Schulabschluss. Ich will, dass du sie verfolgst, auch wenn ich nicht mehr da bin."


show lilly basic_smile_cas_ni onlayer master
with charachange

li "Deswegen denke ich, dass du es schaffen wirst. Weil du du bist, mit deinem eigenen Leben. Du selbst hast es mir bewiesen."


show hanako emb_downtimid_ni onlayer master
with charachange

"Hanako senkt verlegen ihren Kopf, aber nickt gleichzeitig."


ha "Ich… ich verstehe."


ha "Ich weiß, dass ich Lebewohl sagen muss… Ich weiß, dass ich meinen eigenen Weg gehen muss…"


show hanako emb_smile_ni onlayer master
with charachange

ha "Aber… ich danke dir, Lilly. Für alles."


show lilly basic_reminisce_cas_ni onlayer master
with charachange

li "Danke, Hanako. Wirst du zurechtkommen?"


"Ein paar stille Sekunden vergehen, bis die Antwort kommt."


show hanako cover_smile_ni onlayer master
with charachange

ha "Werde ich."


show lilly basic_smile_cas_ni onlayer master
with charachange

"Lilly lächelt, ohne Zweifel wenigstens teilweise aus Erleichterung."


show lilly basic_smileclosed_cas_ni onlayer master
with charachange

li "Dann macht mich das sehr glücklich. Lebwohl."


show hanako basic_bashful_ni onlayer master
with charachange

ha "Lebwohl… Lilly."


show lilly basic_weaksmile_cas_ni onlayer master
with charachange

li "Dir auch alles Gute, Hisao."


hi "Lebwohl. Ich werde dich vermissen."


show lilly basic_weaksmile_cas_close_ni onlayer master
with characlose

"Sie hält einen Moment inne, bevor sie auf mich zukommt. Ihre rechte, vor ihr ausgestreckte Hand legt sie auf meine Schulter."


"Ihre linke Hand bewegt sich langsam und anmutig auf mein Gesicht zu und berührt meine Wange."


show lilly basic_smile_cas_close_ni onlayer master
with charachange

"Für eine Weile hält sie einfach mein Gesicht und bewegt ganz leicht ihre Finger, um sich seine Konturen einzuprägen. Normalerweise wäre ihre Hand dabei warm, aber die Nachtluft hat ihrer Haut eine gewisse Kälte gegeben."


"Ich bin mir nicht sicher, wie lange wir so bleiben. Ihre trüben Augen sind ein wenig unter meine eigenen gerichtet, während ihr Gesicht ein wehmütiges Lächeln zeigt. Schließlich nehme ich ihre kalte Hand in meine eigene."


"Das zu tun, fällt mir schwer, aber mit einem kleinen Seufzen entferne ich sanft ihre Hand von meiner Wange."


hi "Ich hoffe, du hast ein langes und glückliches Leben, Lilly – wo auch immer du hingehen magst."


show lilly basic_weaksmile_cas_close_ni onlayer master
with charachange

li "Danke. Das werde ich ganz sicher."


"Sie nimmt einen langen, zitternden Atemzug, bevor sie sich leicht in Akiras Richtung dreht."


show lilly back_sad_cas_close_ni onlayer master at twoleft
with charachange

li "Akira…"


show akira basic_lost_ni onlayer master
with charachange

aki "Okay."


show hanako basic_bashful_ni onlayer master at left
show lilly back_sad_cas_ni onlayer master at center
show bg school_gate_ni onlayer master at right
with dissolvecharamove

"Mit einem Nicken nimmt sie Lilly bei der Hand und führt sie zum Auto, das vor den Toren geparkt ist. Die beiden laufen langsam und wohlüberlegt, als ob ihre Bewegungen im Voraus geplant gewesen wären."


"Es ist seltsam, so etwas zu fühlen – jetzt wenn jemand die Yamaku verlässt. Dieses unbehagliche Gefühl erinnert mich an das erste Mal, das ich durch diese schwarzen, schmiedeeisernen Tore gegangen bin. Sie sahen immer viel zu pompös aus."


"Als sie gehen, wissen wir alle ganz genau, dass sich unsere Leben unumkehrbar verändern. Ich habe mir schon immer gesagt, dass ich das Leben einfach so nehmen muss, wie es kommt, aber alles ändert sich so schnell, so plötzlich."


"Letzten Endes ist Lilly ein unersetzlicher Teil meines und Hanakos Lebens."


"Das Geräusch, als Akira die Beifahrertür für Lilly öffnet, bringt mich aus meinen Gedanken. Während Lilly einsteigt, winkt sie uns zu."


show akira basic_smile_ni onlayer master
with charachange

aki "Bis dann, Leute! Passt auf euch auf!"


show lilly basic_weaksmile_cas_ni onlayer master
with charachange

li "Lebwohl Hanako, Lebwohl Hisao!"


show hanako cover_smile_ni onlayer master
with charachange

"Hanakos Hand schießt plötzlich in die Höhe und ihr Gesicht erhellt sich, als sie sich noch einmal enthusiastisch verabschiedet."


ha "Lebwohl, Lilly! Alles Gute!"


hi "Bis dann, Akira, und Lebwohl Lilly!"


hide lilly onlayer master
hide akira onlayer master
with charaexit

"Die Tür schließt sich, während wir alle unsere besten Lebewohl-Gesichter aufsetzen. Akira steigt selbst in das Auto ein und startet es kurzerhand."


"Durch die getönten Scheiben kann man gerade so Lillys winkende Hand erkennen. Unsere Hände sind hoch erhoben und winken ebenfalls."


"Genau wie jedes andere Mal, als ich solche Dinge getan habe, kann ich nicht genau ergründen, warum ich – oder Hanako – ihr zuwinke, obwohl sie es niemals sehen kann. Aber das ist unwichtig."


"Sogar nachdem das schwarze, glänzende Auto den Hügel hinabgefahren und in der dunklen Nacht verschwunden ist, winken wir ihnen immer noch zum Abschied zu."


stop music fadeout 5.0

"Und dann… sind sie weg."


show bg school_gate_ni onlayer master at center
show hanako basic_normal_ni onlayer master at center
with dissolvecharamove

"Eine merkwürdige Stille überkommt uns, als wir unsere Hände wieder senken."


"Ich weiß nicht recht, was oder wie ich mich fühlen soll. Letztendlich stehen wir lediglich da und starren still dorthin, wo eben gerade das Auto aus unserem Blickfeld verschwunden ist."


ha "Lebwohl… Lilly."


show hanako basic_normal_close_ni onlayer master
with characlose

"Das Einzige, was ich als Antwort auf ihr leises, schwermütiges Lebewohl tun kann, ist, eine Hand auf ihre Schulter zu legen."


show hanako basic_distant_close_ni onlayer master
with charachange

"Sie sieht mich ein paar Augenblicke lang an, bevor sie wieder den Hügel hinabsieht – sicher mit dem Wissen, dass ich immer noch für sie da bin."


"Was wir von jetzt an tun werden, scheint nicht allzu ungewiss. Wir alle habe nun unsere Ambitionen, genau wie Lilly gesagt hat."


"Doch auch so fühlt es sich an, als würde in unser beider Leben nun ein gewisser Teil fehlen. Ein Teil, der nie ersetzt werden kann."



window hide Dissolve(1.0)
$ suppress_window_before_timeskip = True

scene black onlayer master
with Dissolve(2.0)



label de_L30:



scene bg school_hallway2 onlayer master
with locationchange

play music music_daily fadein 1.0

"Das Zuschnappen meines Handys ist sogar im Flur vor der Bibliothek über die Stimmen und den Lärm hinweg hörbar."


"Es ist der erste Tag der Sommerferien. Die Ferien schienen ständig so fern zu sein, und jetzt sind sie nicht nur da, man merkt es auch sehr deutlich, weil fast keine Schüler mehr an der Schule sind."


"Die meisten Schüler sind mittlerweile nach Hause gefahren, um die Ferien bei ihren Verwandten zu verbringen. Die paar, die übrig sind, bleiben größtenteils unter sich und unterhalten sich meistens über das, was sie in den kommenden Wochen vorhaben."


"Ich komme mir wie ein Außenseiter vor, weil ich es ausnutze, dass die Schulbücherei über die ersten Ferientage geöffnet hat."


"Angeblich ist sie nur geöffnet, damit die Schüler alle Bücher zurückgeben können, die sie ausgeliehen haben, und damit diejenigen, die von ihren Eltern abgeholt werden, sich etwas die Zeit vertreiben können."


"Dank des langen Telefonanrufs meiner Eltern, der mich gerade so unsanft aus meinem Schlaf auf einem Sitzsack in der Bibliothek geweckt hat, gehöre ich nun zu der letzteren Kategorie."


"Als ich mein Handy diesmal zurück in meine Hosentasche gleiten lasse, vergesse ich nicht, es auf lautlos zu schalten, und gehe zurück in den ruhigen und gänzlich friedlichen Raum."


scene bg school_library_ss onlayer master
with locationchange

"Ein nostalgischer Anblick."
"Genau wie an dem Tag, als mich Lilly zum ersten Mal zur Bibliothek geführt hat, badet der Raum im orangenen Licht des Sonnenuntergangs, während Hanako still auf einem Sitzsack liest und Yuuko herumwuselt – gerade noch hinter ihrem Tresen sichtbar."


"Besonders Hanako ist seit den gestrigen Geschehnissen viel stiller als sonst, aber ich kann es ihr nicht wirklich übel nehmen."


"Immerhin war nicht nur ich es, der sich auf diesen Menschen gestützt hat."


"Leise laufe ich zurück zu dem Sitzsack neben ihr, wo ich bis eben gesessen hatte. Dabei bin ich doppelt vorsichtig, keinen unnötigen Lärm zu machen."


scene ev hana_library onlayer master
with locationchange

show ev hana_library_read onlayer master
with charachange

"Das sanfte Geräusch der entweichenden Luft, als der Sack mein Gewicht federt, lässt Hanakos Augen zu mir huschen, aber nur für eine Sekunde."


"Ich bekomme das Gefühl, dass Hanako nur teilweise aus Trauer um Lillys Abreise so ruhig gewesen ist."


"Eher wirkt sie nachdenklicher und bedächtiger als ich es erwartet hatte; vielleicht will sie lieber herausfinden, wie sie mit Lillys Weggang umgehen soll, als nur deprimiert darüber zu sein. Es macht mich ein bisschen stolz auf sie."


hi "Hey, Hanako?"


show ev hana_library onlayer master
with charachange

ha "J-Ja?"


hi "Ziehst du deine Idee mit der Reise immer noch durch?"


"Sie nickt entschlossen."


ha "Ich fahre in ein oder zwei Tagen los. Naomi hat sich auch entschieden mitzukommen."


hi "Wow, das ging schnell. Wo wollt ihr Zwei als Erstes hin?"


ha "Ich denke, wir werden erst mal nach Norden fahren… und dann eine Kurve nach Süden machen."


hi "Also… wird Hokkaido euer erstes Ziel sein?"


"Sie nickt erneut, aber zögerlicher als zuvor. Die Bedeutung dieses Ortes ist uns beiden bewusst."


hi "Wisst ihr, wie ihr die Reise- und Unterkunftskosten auftreiben werdet?"


ha "Ja, ich habe alles geplant. Ich denke, es sollte gut gehen. Naomi sagt auch, dass von ihrer Seite alles vorbereitet ist."


hi "Du weißt, dass du einfach anrufen kannst, falls du etwas brauchst, oder? Meine Nummer hab ich dir schon gegeben. Du kannst mich jederzeit erreichen."


show ev hana_library_smile onlayer master
with charachange

"Sie schenkt mir ein kleines Lächeln, welches sich allein schon wie ein kleiner persönlicher Sieg anfühlt."


ha "Ich weiß."


ha "D-Danke… Hisao."


"Vielleicht hatte Lilly Recht. Obwohl ich Hanako jede Hilfe anbiete, die mir möglich ist, glaube ich zu wissen, dass sie sie nicht braucht."


"Sie ist wirklich gewachsen."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\nHanakos Pläne für ihre Ferien stehen im starken Kontrast zu meinem simplen geplanten Aufenthalt bei meinen Eltern."


n "Ferien haben mich aber noch nie so begeistert wie andere, also ist das vielleicht nur eine Rückkehr zum Status quo."


n "\nVor meiner Herzattacke hatte ich immerzu so ziellos vor mich hingelebt, dass sich die Ferien kaum von meinem alltäglichen Leben unterschieden."


n "Nach der Schule spazierte ich etwas durch die Stadt und hing oft mit ein paar Freunden ab, bevor ich dann zum Abendessen nach Hause ging, um meist mit einem, selten mit beiden meiner Eltern zu essen."


n "Ihre Arbeitszeiten ließen ihnen nicht viel Zeit, um zu Hause zu sein, und direkt von der Schule nach Hause zu gehen, hätte nur Langeweile zur Folge gehabt. Ich war durch und durch ein Stadtkind."


nvl clear

n "\n\nAber seit ich an der Yamaku bin, fühle ich mich, als hätte ich mich als Mensch grundlegend verändert. Das Telefongespräch mit meinen Eltern hat jedenfalls jegliche Zweifel darüber ausgelöscht."


n "Während ich früher eine relativ durchschnittliche Unabhängigkeit für einen Teenager hatte – was nicht sehr viel war – waren meine Eltern mehr als erfreut, von meiner neugefundenen Fähigkeit zu hören: Ich kann auf mich selbst aufpassen."


n "Wäsche waschen, für mich selbst kochen, saubermachen – all das zusätzlich zu den anderen allgemeinen Hausarbeiten, die das allein Wohnen mit sich bringt… Nur kleine, niedere Dinge, die ich mir aneignen musste. Doch das ging relativ leicht."


n "\nWenn ich darüber nachdenke, habe ich mich immer auf sie verlassen, obwohl sie die ganze Zeit nicht zu Hause waren. Zu sagen, dass ich mich nie auf jemanden verlassen habe, nachdem ich in das Wohnheim gezogen bin, wäre aber auch nicht die Wahrheit."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve
window show

yu "Ähm… entschuldigt…"


stop music fadeout 3.0

scene bg school_library_ss onlayer master
show yuuko worried_down_ss onlayer master at center
with locationchange

"Wir beide sehen zu der unbeholfen zappelnden Gestalt vor uns auf. Manche Dinge ändern sich nie."


show yuuko worried_up_ss onlayer master
with charachange

yu "Ich muss bald schließen, also ähm…"


"Oh, richtig. Ich hatte vergessen, dass die Bibliothek in den Ferien früher schließt."


"Hanako und ich stehen auf, klopfen uns ab und legen die Bücher zurück auf das Regel hinter uns. Dass sich unsere Lesevorlieben recht häufig überschneiden, ist manchmal nützlich."


"Mit einer Verbeugung entschuldigt sich Hanako bei Yuuko, dass sie so lange gebraucht hat. Danach verabschiedet sie sich."


show bg school_library_ss onlayer master at bgleft
show yuuko worried_down_ss onlayer master at twoleft
with dissolvecharamove

show hanako basic_normal_ss onlayer master at tworight
with charaenter

ha "Bis morgen, Hisao."


hi "Bye."


hide hanako onlayer master
with charaexit

"Und damit geht sie durch die großen, hölzernen, alternden Türen am Eingang zur Bibliothek."


play music music_happiness fadein 3.0

show bg school_library_ss onlayer master at center
show yuuko neutral_down_ss onlayer master at center
with dissolvecharamove

yu "Sie ist ein ruhiges Mädchen, nicht wahr?"


"Vermutlich sollte ich überrascht darüber sein, dass eine Angestellte persönliche Meinungen von sich gibt, aber nachdem ich Yuuko nun eine Weile kenne, war das fast schon zu erwarten."
"Unser Verhältnis ist eben persönlicher als das zwischen einer Autoritätsperson und einem Schüler."


hi "Ja, ich denke, so ist sie einfach."


hi "Allerdings hat sie mittlerweile viel mehr Selbstvertrauen aufgebaut."


show yuuko smile_down_ss onlayer master
with charachange

yu "Ich kenne sie nicht so gut wie du, aber ich bin der gleichen Meinung. Es ist schön zu sehen, dass sie sich mit den Leuten hier unterhält; das hat sie früher nie getan."


hi "Hey, Yuuko… Du weißt von Lillys Abreise, oder?"


show yuuko worried_down_ss onlayer master
with charachange

yu "Sie hat es mir selbst vor ein paar Tagen gesagt. Es muss hart für sie sein, alle so zurückzulassen."


"Nachdem sie das sagt, sieht sie schnell wieder zurück zu mir. Wahrscheinlich erinnert sie sich daran, dass ich einmal wegen eines Beziehungstipps für Lilly und mich zu ihr gekommen bin."


show yuuko worried_up_ss onlayer master
with charachange

yu "Kommst du damit zurecht?"


"Das ist… eine schwierige Frage. Allerdings ist es etwas, worüber ich jetzt wegen dringenderer Angelegenheiten lieber nicht nachdenken würde."


hi "Irgendetwas scheint an der ganzen Sache faul zu sein, meinst du nicht?"


"Yuuko scheint eine Weile darüber nachzudenken und zeigt dabei eine Vielzahl an kreativen Gesichtsausdrücken."


show yuuko worried_down_ss onlayer master
with charachange

yu "Ich glaube nicht, dass du sie gut genug kennst, um so ein Urteil zu fällen."



yu "Tut mir leid, dass ich dir keine größere Hilfe sein kann."


hi "Nee, ist schon okay. Ich hab nur laut gedacht."


"Ich seufze laut und kratze mich frustriert am Kopf."


hi "Es passiert einfach so vieles auf einmal, worüber ich keine Kontrolle habe… Es kommt mir vor, als würde ich überschwemmt werden."


show yuuko neutral_down_ss onlayer master
with charachange

yu "Ich denke, dass jeder solche Zeiten durchmacht."


yu "Wichtig ist, dass man sich darauf konzentriert, was man tun kann, anstatt auf das, was man nicht tun kann. Zumindest sehe ich das so."


show yuuko smile_down_ss onlayer master
with charachange

yu "Wenn ich nicht so denken würde, würde ich mein Leben wohl nicht auf die Reihe kriegen."


"Sie sagt es mit einem Lächeln und einer fröhlichen Stimme, aber ihre Worte sind weit von einem Witz entfernt. Zwei Jobs zu jonglieren, nur um hoffentlich nicht nur genug Geld zum Leben zu haben, sondern auch für die Universität, muss anstrengend sein."


"Vielleicht fühlt sich das besonders bedeutungsvoll an, weil es von ihr kommt, und nicht von irgendjemand anderem."


hi "Ich schätze, da hast du Recht."


hi "Wieder einmal danke für deinen Rat, Yuuko."


show yuuko smile_down_ss onlayer master:
    ease 0.5 ypos 1.2
with None

show yuuko closedhappy_down_ss onlayer master:
    ease 0.5 ypos 1.2
with charachange

with Pause(0.2)

show yuuko closedhappy_down_ss onlayer master:
    ease 0.5 ypos 1.0
    linear 0.5 alpha 0.0 
with charamove

"Sie verbeugt sich tief und lächelt noch einmal, bevor sie sich zurück zu dem Tresen begibt, an dem sie so viel ihrer Zeit verbringt."


stop music fadeout 2.0

scene bg school_dormhisao_ni onlayer master
with shorttimeskip

"Die kleinen Flügel des Papp-Kranichs in meinen Fingern sind im trüben Licht meines Zimmers gerade so zu erkennen. Nur ein kleines bisschen Mondlicht schafft es durch die Vorhänge."


show origami_hand onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with None

show origami_hand onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
show bg school_dormhisao_blurred_ni onlayer master
with Dissolve (1.0)

play music music_twinkle fadein 10.0

"Für eine lange Zeit liege ich still in meinem dunklen Bett und betrachte untätig den kleinen Origamivogel."


"Es kommt mir so vor, als wäre eine Menge passiert, seit Lilly ihn gefaltet hat, aber zur gleichen Zeit kommt es mir auch so vor, als hätte sich nur sehr wenig verändert."


"Verglichen mit allen anderen bin ich wieder am Anfang. Ich mag ein neues Ziel für meine Zukunft gefunden haben, aber das ist etwas, was mir jetzt gerade auch nicht weiterhilft."


"Hanako hat sich verändert, so viel weiß ich. Wenn man ihre frühere Situation bedenkt, habe ich das Gefühl, als hätte ich keine Ausrede dafür, mich so zu fühlen."


"Aber Lilly…"


"Ich drehe den Vogel in meinen Fingern und betrachte ihn aus einem anderen Winkel."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\nAls ich sie zum ersten Mal traf, schien sie reserviert und vielleicht etwas distanziert. Ihre Handlungen waren immer sorgfältig, bedächtig und präzise, und ihre sorgsam aufrechterhaltene Gelassenheit gab ihr immer den Anschein von unfehlbarer Selbstsicherheit und Ruhe."


n "Im Laufe der Zeit wurde sie umgänglicher. Nur ein wenig, aber es war genug. Es fühlte sich gut an zu sehen, wie sie ihre Hemmungen in meiner Nähe fallen ließ und sich mir von sich aus öffnete. Auch wenn es nur ein bisschen war, fühlte es sich an, als würde ich sehen, wie ihr wahres Ich langsam lebhafter und offensichtlicher wurde."


n "\nAllerdings kommen mir langsam Zweifel."


n "Vielleicht war das zu erwarten, nachdem wir im Grunde Schluss gemacht haben – sie kommen mir aber nicht neu oder komisch vor, sondern eher wie ein altes Buch, dass ich gefunden und abgestaubt habe."


n "Kurz nachdem ich Lilly traf, begriff ich, dass sie in mir sah, was sie in Hanako gesehen hat: Jemanden, der Hilfe und Fürsorge brauchte. Am Anfang dachte ich lediglich, dass wir gute Freunde werden und einander durch unsere begrenzte Schulzeit helfen."


nvl clear

n "\n\nDoch dann begann ich, unsere gemeinsamen Momente mehr und mehr schätzen – von unseren stillen Spaziergängen bis zu unseren Gesprächen beim Mittagessen. Ihre guten Seiten wurden sogar noch offensichtlicher, und noch liebenswürdiger."


n "Ihre Abwesenheit während ihrer Reise nach Schottland, um ihre weit entfernte Familie und kranke Tante zu besuchen, ließen mich nur noch mehr begreifen, wie gerne ich in ihrer Nähe war. Und ich dachte, dass sie ähnlich fühlen würde."


n "\n\nFür sie war das jedoch nicht alles in unserer Beziehung."


n "\nSelbst nachdem sie nach Japan zurückgekehrt war, bedeutete es nur, dass sie erneut ihre Familie verlor, nachdem sie sie gerade für so kurze Zeit wiedergetroffen hatte."


n "Sie hat ihr Leben so lange ohne die Nähe ihrer Familie gelebt, ganz zu schweigen von Akiras langen Arbeitszeiten. Sie hatte kaum eine Wahl, sie konnte nur so werden."


nvl clear

n "\n\nIch hielt ihre Unabhängigkeit für einen guten und bewundernswerten Charakterzug. Sie stand im starken Kontrast zu meinem Vertrauen auf meine Eltern vor meiner Herzattacke, so widerwillig ich es auch zugegeben haben mag."


n "Allerdings bedeutete es auch, dass sie niemals einen Menschen zu nah an sich heranlassen würde."


n "Allem Anschein nach hat sie ihre Familie wegen ihrer Blindheit verloren, ging ihretwegen an eine andere Schule als jeder, den sie sonst kannte, und arbeitet umso härter, um sicherzustellen, dass sie keine Last für ihre Schwester und diejenigen um sich herum sein würde."


n "\nUnd jetzt fährt Akira nach Inverness – genau wie die Familie, die sie verloren geglaubt hatte."


n "Sie erzählte mir nie von ihren Plänen, so sehr sie auch mit sich gekämpft hat."


n "Lilly wollte niemandem zur Last fallen. Mich eingeschlossen."


n "\n… Ich bin ein Idiot."


nvl clear

n "\nIch habe es nie hinterfragt. Ich habe nie versucht, für sie da zu sein, oder zu fragen, ob sie mich braucht."


n "Ich habe mein Leben einfach aufgestellt und erwartet, dass es für immer so bleibt – wir Zwei in einer schönen, langen Beziehung, wie wir zusammen in unsere Zukunft schreiten."


n "\nEin wenig Frust und Zorn auf mich selbst machen sich in meiner Brust bemerkbar."


n "\nIch habe einfach alles geschehen lassen und nie auch nur versucht, Lilly zu helfen."


n "\nDass sie einfach da war, war genug. Ich dachte, ich könnte ewig so weitermachen, solange sie da war."


n "Aber das hätte nie ausreichen können. Es war eine kindische Abhängigkeit von jemanden, ohne jeglichen Versuch, ihre Lage zu verstehen oder zu helfen."


n "Deswegen habe ich Lilly verloren. Ich habe diesen einen Menschen verloren, den ich am meisten liebte, weil ich nicht für sie da war, als sie mich gebraucht hat."


stop music fadeout 5.0

nvl clear
nvl hide dissolve

show origami_hand onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

show origami_hand onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
show bg school_dormhisao_ni onlayer master
with Dissolve (1.0)

hide origami_hand onlayer master
with None

window show

"Als sich in mir eine zunehmende Wut anbahnt, rolle ich mich zur Seite, um den Kranich zurück auf den Tisch neben meine Uhr zu stellen – an den Ort, an dem er seit dem Tag gelebt hat, an dem sie ihn für mich gefaltet hat."


"Seit diesem Tag, an dem sie selbst gesagt, dass ich meine Last nicht allein tragen muss."


"Die unausstehlichen, hellroten Ziffern auf meinem Wecker scheinen durch die Dunkelheit des Raumes in meine müden Augen."


"Zehn Uhr. Abend. Bald ist Ausgangssperre."


hi "Ich frage mich…"


"Akira erwähnte, dass sie heute Abend abreisen würden."


"Ich habe keine Ahnung, wann ihr Flug ist… aber das bedeutet, dass es eine Chance gibt – so klein sie auch sein mag – dass sie vielleicht noch nicht abgereist sind."


"Adrenalin fängt an, sich seinen Weg durch meinen Körper zu bahnen, als ich mich auf mein Bett setze und meine Augen sich plötzlich in Anbetracht der Möglichkeiten vor Aufregung weiten."


"Es gibt keine Garantie dafür, dass sie nicht schon weg sind – wahrscheinlich sind sie es sogar – aber es gibt auch die Möglichkeit, dass sie es nicht sind."


"Nur dieses eine Mal, so wie ich es schon vorher hätte tun sollen…"


play sound sfx_switch

show bg school_dormhisao onlayer master
with Dissolve(0.2)

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_friendship fadein 9.0

"Ich stehe auf und eile zu meinem Schrank, schmeiße so schnell ich kann ein paar Klamotten heraus und schlüpfe schnell in sie hinein."


"Jede Sekunde, die vergeht, ist eine, die ich nicht wiederbekomme. Eine Sekunde, die den Unterschied ausmachen kann zwischen sie einholen und sie für immer verlieren."


"Selbst wenn ich scheitere, muss ich es versuchen. Ich kann nicht zulassen, dass sie alles zurücklässt, ohne auch nur zu versuchen, sie aufzuhalten. Ohne – nur dieses eine Mal – für sie da zu sein."


"Nachdem ich die letzten meiner Klamotten angezogen habe, greife ich hastig das Handy auf dem Schreibtisch. Gott sei Dank ist die Nummer des örtlichen Taxiunternehmens noch in meinem Anrufverlauf."


show bg school_dormhisao_blurred onlayer master
show phone mobile onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)

"Eine barsche, lustlose Stimme verkündet den Namen des Unternehmens, während ich im Zimmer auf- und abgehe. Ich muss muss mir etwas Mühe geben, um langsam und deutlich zu sprechen."


scene bg school_dormext_full_ni onlayer master
with locationskip

"Die kühle Nachtluft weht mir entgegen, als ich die Tür des Wohnheims öffne, aber nichtsdestotrotz behalte ich mein flottes Tempo bei. Halb joggend und halb rennend begebe ich mich hinaus zum Schultor."


"Es mag noch nicht ganz Ausgangssperre sein, aber es ist gefährlich nah dran."
"Wenn ich auf einen Wächter treffe, hätte er ohne Zweifel ein paar Fragen an mich, aber es sieht aus, als hätte ich es vor ihrem Dienstbeginn hinausgeschafft – oder sie warten um die Ecke."


scene bg school_gardens_ni onlayer master
with locationchange

"Mein Tempo beschleunigt sich, während ich die Schulgärten durchquere. Ihr nächtlicher Zauber ist gänzlich verloren, als ich anfange, zum Schultor zu rennen."


scene bg school_courtyard_ni onlayer master
with locationchange

"Die trüben Lampen im Schulhof bieten gerade genug Licht, um mir den Weg zu erleuchten, damit ich nicht hinfalle. Die Gebäude selbst sehen irgendwie rustikal, fast antik aus, wenn ich sie in diesem Licht anschaue."


"Als ich zurückblicke, wirkt es seltsam, dass sie mir einst so dunkel und bedrohlich erschienen. Jetzt sehen sie bloß aus wie irgendwie unzeitgemäße Schulgebäude, genau wie alle anderen abgesehen von ihrem Alter."


scene bg school_gate_ni onlayer master
with locationchange

"Nachdem ich die Tore hinter mir gelassen habe, komme ich direkt vor dem Taxi zum Halt. Es parkt genau da, wo Akiras Auto gestanden hat, und sein knallbuntes und hell erleuchtetes Schild sieht in der ruhigen Landkulisse deplatziert aus."


"Ungeduldig quetsche ich mich durch die Tür und gebe dem Fahrer die Adresse, wo die beiden sich hoffentlich aufhalten sollten."


scene bg shizu_houseext_ni onlayer master
with shorttimeskip

"Als das Taxi nach seiner Fahrt mit unerträglich legerem Tempo an die Seite fährt, ist es bereits tief in der Nacht."


"Das Haus ist wahrlich riesig. Seine schiere Größe übertrifft meine Erwartungen, und das dramatisch. Weil ich das Schlimmste befürchte, bitte ich den Fahrer zu warten – nur für den Fall, dass meine Mühen umsonst waren."


"Ein kurzer Druck auf die extravagante Gegensprechanlage am Tor erzeugt eine kurze elektronische Melodie in der ansonsten stillen Straße. Es dauert nicht lange, bis eine etwas tiefe, unwirsche Stimme aus ihr zu hören ist."


mystery "Dies ist das Hakamichi-Anwesen. Bitte nennen Sie Ihren Namen und warum Sie uns so spät noch stören."


"Obwohl ich wegen der vertretbaren Genervtheit in seiner Stimme innerlich zusammenzucke, spreche ich mein Anliegen aus."


hi "Ich bin Hisao Nakai. Ich hatte gehofft, Akira und Lilly zu treffen, falls sie noch hier sind."


"Überraschenderweise gelingt es mir, einiges an Energie in meine Stimme zu legen – genug, um die andere Seite der Sprechanlage verstummen zu lassen."


show bg shizu_houseext_lights onlayer master
with Dissolve(0.2)

"Ein paar Sekunden vergehen, doch kurz bevor ich den Knopf noch einmal drücke und frage, was los ist, schaltet sich ein Licht außerhalb der Fronttür ein."


"Ich kneife meine Augen zusammen, um zu erkennen, wer herauskommt, aber als er an einem großen, geparkten Auto vorbeikommt, aus dessen Kofferraum Angelruten herausragen, wird seine Identität eindeutig."


"Sein Gesicht ist wie immer gelassen und emotionslos, als er zum Tor schlendert. Trotz seines Auftretens ist er immer noch kindisch. Nachdem er hinter dem Zaun ein paar Knöpfe gedrückt hat, öffnet sich das Tor langsam."


show hideaki surprise_ni onlayer master at center
with charaenter

hh "Hisao? Was machst du denn hier?"


"Ich glaube, so viel Emotion habe ich noch nie in seiner Stimme gehört. Nicht, dass das schwierig wäre."


hi "Akira sagte mir, dass sie und Lilly hier übernachten würden, bevor sie ihren Flug nehmen."


hi "Ich muss mit Lilly reden, nur ein letztes Mal. Sind sie noch hier?"


show hideaki sad_ni onlayer master
with charachange

"Der Blick auf seinem Gesicht sagt alles."


"Ich bin gescheitert. Ich war zu spät. Das einzige Mal, dass ich wirklich schnell handeln musste, und…"


show hideaki serious_up_ni onlayer master
with charachange

hh "Eigentlich… ist es möglich."


hi "Was? Wie spät ist es?"


show hideaki confused_ni onlayer master
with charachange

"Er ist etwas von meinem Eifer verdutzt, aber inzwischen ist mir das egal."


show hideaki normal_ni onlayer master
with charachange

hh "Sie sind vor Kurzem erst losgefahren; eigentlich sogar nur ein paar Minuten, bevor du angekommen bist. Wenn du direkt zum Flughafen fährst, könntest du sie vielleicht… Hisao?"


"Ich schieße zurück zu dem wartendem Taxi und greife dabei nach dem letzten Geld, das noch in meiner Hosentasche ist."


hi "Danke, Hideaki!"


"Ich setze mich ins Auto und rufe dem Taxifahrer direkt mein neues Ziel zu."


scene bg city_street4_ni onlayer master
show crowd_ni onlayer master
with shorttimeskip

play ambient sfx_crowd_outdoors fadein 2.0

"Mein Herz klopft wie wild, als ich die Straße entlanghetze und sich mein Körper durch die dichte Masse von Fußgängern windet."


"Weil die Straße vollkommen von Taxis und anderen Autos blockiert ist, die Passagiere ein- und aussteigen lassen, mussten wir letztendlich fast einen Block entfernt anhalten."


"Aber das ist jetzt Vergangenheit. Ich muss Lilly erreichen."


"Einen Schritt nach dem anderen führen mich meine Füße vorwärts, als hätten meine Beine ein Eigenleben entwickelt. Alles, was mein Verstand tun kann, ist, sich auf das zu konzentrieren, was vor mir liegt."


"Nur ein flüchtiges Aufblitzen ihrer langen Haare. Dieses lange, blonde Haar, das sie gleiche Farbe hatte, wie das Getreide, das sich so weit das Auge sehen konnte erstreckte."


"Letzten Endes habe ich mich auf Lilly verlassen, genau wie Hanako auch. Selbst nachdem wir zusammenkamen, fühlte es sich trotzdem nicht so an, als hätte sie sich je wirklich auf mich verlassen wollen."


"Abgesehen von einem Moment. Dieser eine Moment, wo wir in diesem hellgelben Feld fest aneinander festhielten."


"Zu jener Zeit muss sie gefürchtet haben, dass sie mich genau wie jeden anderen verliert. Darum… nur dieses eine Mal…"


"Die Nachtluft wickelt sich um mich und zieht das letzte bisschen Wärme aus meinem Körper – so sehr, dass es sich eher wie tiefer Winter als eine Sommernacht anfühlt."


"Meine Finger, meine Hände, meine Füße… Alles fühlt sich zunehmend kälter an."


"Das Geräusch der vorbeiziehenden Menschenmenge wird zu einem bloßen Hintergrundrauschen, während meine auf den Bordstein stapfenden Schuhe laut durch die Straßen schallen."
"Mit jedem Schritt nähere ich mich dem Menschen, den ich einholen muss."


"Meine Brust zieht sich wegen der Nachtkälte zusammen und zwingt mich, einen Arm über sie zu legen, damit ich versuchen kann, mein Herz zu beruhigen."


window hide

scene bg hosp_ext_ni onlayer master
show crowd_ni onlayer master
with locationchange

play sound sfx_heartslow
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.7)

window show

"Als der Flughafen jedoch in Sichtweite kommt, begreife ich, dass ich dieses Gefühl schon einmal gespürt habe."


"Nicht jetzt… Zu jedem anderen Zeitpunkt, aber nicht jetzt."


"Ich schlucke und mache trotzdem unermüdlich weiter. Ich verlange meinem Körper alles ab – bis zum Letzten."


"Schweiß trieft von mir, während ich vorwärts rase. Meine Schulter trifft jemandes Seite, und mein Kopf wird plötzlich von Emotionen und Erinnerungen überschwemmt."


"Ohne eine Entschuldigung renne ich weiter. Ich darf jetzt nicht stehenbleiben. Wenn ich jetzt anhalte, bin ich mir nicht sicher, ob ich wieder loslaufen könnte, und selbst wenn ich es könnte, wäre alles umsonst, wenn es nicht rechtzeitig schaffe."


with vpunch

"Ich pralle gegen eine weitere Person, und dann noch eine. Mir ist egal, ob ich herumgestoßen werde."


"Meine Füße sind taub. Meine Arme verlieren all ihr Gefühl. Meine Brust zwingt mich dazu, mich unbeholfen zu krümmen, als sie sich noch weiter zusammenzieht."


window hide

play sound sfx_heartslow
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.2)

window show

"Dieser Nachtmittag im Schnee… Dieser Augenblick, als mein Leben sich unumkehrbar veränderte… Bilder von Iwanako, der ersten Liebe, die ich aufgrund dieser Krankheit verlor, und diesem verdammten Brief blitzen wieder und wieder in meinem Kopf auf."


"Ich kann es nicht wieder geschehen lassen. Mir ist mittlerweile egal, was mit mir passiert, ich muss sie nur ein letztes Mal sehen."


"… Da!"


scene ev lilly_airport onlayer master
with flash

"Eine kleiner Fleck aus Gelb und Weiß kommt weiter hinten auf der Straße in Sichtweite. Ihre Gestalt wird von den strahlenden Lichtern des Flughafeneingangs umrahmt."


hi "Lilly! Lilly!"

hi "Lilly! Bleib stehen, bitte! Lilly!"


"Komm schon Lilly, ich weiß, dass dein Gehör weit bes…"


scene bg hosp_ext_ni onlayer master:
    xalign 0.5 yalign 0.52 rotate 0 zoom 1.0
    linear 0.1 rotate -6 zoom 1.2
show crowd_ni onlayer master:
    xalign 0.5 yalign 0.52 rotate 0 zoom 1.0
    linear 0.1 rotate -6 zoom 1.2
with vpunch

play sound sfx_impact

hi "Agh!"


"Meine Welt gerät ins Schleudern, und ich lande auf dem Boden. Mein Körper liegt zusammengesunken da, nachdem ich gegen jemanden gestoßen und gestolpert bin."


window hide

play sound sfx_heartslow
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.2)

window show

"Bevor ich den Schaden abschätzen kann, entflammt ein unglaublicher Schmerz in meinem Körper. All meine Gedanken sind wie weggeblasen, als ich mich zusammenrolle und panisch an meine Brust greife."


mystery "Hey, bist du okay? Das war ein wirklich schlimmer Sturz."


"Dieser Schmerz… Ich halte es nicht…"


hi "Argh… aaaaarrgh!"


window hide

play sound sfx_heartslow
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.2)

window show

"Jeder heftige Schlag könnte mich erledigen. Jeder Überanstrengung. Ich dachte, ich könnte dieses eine Mal meine Grenzen überwinden…"


mystery "Etwas stimmt nicht mit ihm!"


window hide

play sound sfx_heartslow
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.8)

window show

mystery "Was hast du denn? Bist du…"


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

window show

"Die Stimmen jener, die sich um mich versammeln, werden nach und nach von einem lauten Piepen in meinen Ohren ersetzt."
"Mittlerweile kann ich meinen Kopf nicht mehr bewegen, also drehen sich meine Augen nach oben, um den stummen Bewegungen ihrer Lippen zu folgen."


window hide

play sound sfx_heartfast
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.8)

with Pause(0.15)

play sound sfx_heartslow
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.8)

play sound sfx_heartfast
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.8)

with Pause(0.05)

play sound sfx_heartstop
show heartattack alpha onlayer master
with Dissolve (0.1)

stop ambient fadeout 0.3

show heartattack residual onlayer master
with Dissolve (0.8)

window show

"Als ich mir an die Brust greife, fällt mir auf, dass ich meine Finger nicht mehr spüren kann und meine Füße auch nicht. Es fühlt sich an, als würde mein gesamter Körper sich abschalten und dabei bei meinen Extremitäten anfangen."


scene ev lilly_airport_end onlayer master:
    truecenter
    zoom 1.2 rotate -8 subpixel True
    easein 12.0 zoom 1.0 rotate 0
with slowfade

"Mit einer letzten Anstrengung drehe ich meinen Kopf die Straße hinab, in Richtung des Flughafeneingangs, dessen Lichter auf mich scheinen."


"Lilly ist dort, hinter dieser Menschenmenge. Ihr Kopf ist geneigt, aber nur ein wenig."


show passoutOP1 onlayer master
with None

"Ich merke, wie meine Sicht sich trübt, als ich versuche, ihr zuzurufen, aber trotz meiner größten Anstrengungen bringe ich keinen Ton hervor. Langsam aber sicher beginnt sich die Szene vor mir schwarz zu färben."


"… So endet es also."


"Ich bin gescheitert. Ich war so nah, so verdammt nah dran, doch im allerletzten Moment nahm mir meine Krankheit meine Chance auf ein neues Leben und zerrte mich zurück."


"Nun werde ich sterben, nur Meter vor dem Flughafen mit allen Gliedmaßen von mir gestreckt und einer Gruppe von schwafelnden Menschen um mich herum, während Lilly mit nur ein wenig Vorsprung nach Schottland abreist."


hi "Li… lly…"

stop music fadeout 4.0

"Dieses letzte Wort lässt meine letzte Energie erlöschen. Die Welt fällt in eine tiefe, unabwendbare Schwärze, als sich jeder Muskel in meinem Körper ausschaltet."


"Es tut mir leid, Lilly."


"Ich war zu spät."


scene black onlayer master
with dissolve



label de_L31:

scene white onlayer master
with dissolve

"…"

"……"

"………"

"Was… geht hier vor…?"


"Als ich langsam meine Augen öffne, brennt sich ein helles, weißes Licht in meine Netzhäute."


"Minutenlang liege ich bloß still da und starre gedankenlos nach oben, während sich meine verstreuten Gedanken in meinem langsam wachwerdenden Verstand zusammenfügen."


show bg hosp_ceiling onlayer master:
    alpha 0.0
    linear 5.0 alpha 1.0
with None

"Langsam aber sicher beginnt das Weiß klarer zu werden, und eine nackte Fläche zeichnet sich vor meinen Augen ab."


"Erst als die Lampenbefestigung erkennbar wird, wird mir klar, dass dies die Decke über mir ist."


scene bg hosp_room2 onlayer master
with locationchange

"Als ich mich langsam aufraffe, absorbiere ich still mit all meinen Sinnen die Details des Raumes, in dem ich mich befinde."


"Der Geruch und Geschmack von starker Bleiche hängt in der Luft und verleiht den Eindruck eines Ortes, der etwas zu sauber ist, um natürlich zu sein."


"Unaufdringlich blasse, pfirsichfarbene Wände, alle perfekt gestrichen, ohne einen Riss, Fleck oder Makel. Ein einzelnes gerahmtes Bild hängt perfekt ausgerichtet an der Wand. Wie die Wände ist es so langweilig und unaufdringlich, wie es nur sein kann."


"Meine Aufmerksamkeit richtet sich auf die lichtdurchlässigen Vorhänge, die vor meinen Augen umherwehen, und meine Augen folgen ihnen zu dem offenen Fenster, welches sie bedecken."


"Als ich meinen rechten Arm bewege, um mich selbst etwas aufzusetzen und nach draußen zu sehen, spüre ich, wie sich der Katheter unangenehm in meinen Arm bohrt."
"Jetzt bemerke ich auch erst die Kanülenschläuche, die sich um meine Wangen und in meine Nase hineinwinden. "


"Nach etwas Zappelei gebe ich mich einfach mit einem etwas niedrigeren Blickwinkel durch das Fenster zufrieden."


scene ev lilly_hospitalwindow onlayer master
with whiteout

"Hinter den dichten Blättern mehrerer großer Bäume kann ich unten die Vegetation sehen, die sich nach hinten in ein Feld streckt. Eine gewöhnliche Insel aus Grün in den Randgebieten der Stadt."


"Der Sonne draußen nach zu urteilen, ist es Mittag. Welcher Tag heute ist, weiß ich aber nicht."


"… Also bin ich mal wieder in einem Krankenhaus."


"Ich lasse einen langen, erschöpften Atemzug entweichen, während ich versuche, meine verstreuten Gedanken zu sammeln. Mein Kopf rast scheinbar gleichzeitig in ein Dutzend Richtungen, wobei mich genauso viele Emotionen durchströmen."


scene bg hosp_room2 onlayer master
with locationchange

"Nachdem ich mich langsam zurücklege, beschließe ich, am Anfang zu beginnen – warum ich hier bin."


"Ich gehe in Gedanken zurück, kann mich aber nicht genau erinnern, was passiert ist. Die Geschehnisse von letzter Nacht… oder welche Nacht auch immer es war… sind eher eine Reihe von Schnappschüssen als eine zusammenhängende Erinnerung."


scene bg school_dormhisao_ni_fb onlayer master
show origami_fb onlayer master at center
show noiseoverlay onlayer master
with flash

"Ich lag auf dem Bett und sah mir den Origami-Vogel an."


scene bg shizu_houseext_lights_fb onlayer master
show hideaki serious_up_fb onlayer master at center
show noiseoverlay onlayer master
with flash

"Ich sprach mit Hideaki außerhalb des Hakamichi-Anwesens."


scene bg hosp_ext_fb onlayer master
show crowd_still1_fb onlayer master at center
show noiseoverlay onlayer master
with flash

"Ich lief die Straße hinab, wich Fußgängern aus und stieß gegen immer mehr von ihnen."


scene bg hosp_ext_fb onlayer master:
    xalign 0.5 yalign 0.52 rotate -6 zoom 1.2
show crowd_still2_fb onlayer master:
    xalign 0.5 yalign 0.52 rotate -6 zoom 1.2
show noiseoverlay onlayer master
with flash

"Ich stürzte."


scene ev lilly_airport_end_fb onlayer master
show noiseoverlay onlayer master
with flash

"Ich sah hinauf zu dem grellen Flughafeneingang und sah dann Lillys Rücken, während ich am Boden lag."


"…"

scene bg hosp_room2 onlayer master
with fade

"Die Stille in dem Einzelzimmer fühlt sich plötzlich erdrückend an."


play music music_rain fadein 2.0

window hide
nvl clear
nvl show dissolve

n "\nDas war's also. Ich hatte meine Chance, meinen Fehler wieder gutzumachen, und ich habe es vermasselt."


n "Ob es meine Schuld war, weil ich meine Medikamente vernachlässigt habe und mich nicht in Form bringen wollte, oder die meines Körpers, weil er zu schnell schlappgemacht hat, ist jetzt egal."


n "Alles, was zählt, ist, dass ich – wieder einmal – allein bin."


n "Das pastellblaue Kissen gibt ohne viel Widerstand nach, als ich mich wieder aufs Bett fallen lasse, das mit seinen steifen Bezügen und den steifen Bettlaken wenig Komfort bietet."


n "Verglichen mit der Dunkelheit der gestrigen Ereignisse ist das helle Licht des Raumes um mich herum beeindruckend. Jedoch betont es nur, wie jenseitig sich solche Räume anfühlen."


n "Arrhythmie."


n "Ein seltsames Wort. Ein ganz und gar fremdartiges. Eines, mit dem man nicht im gleichen Raum sein will."


n "Eine seltene Krankheit. Sie bewirkt, dass das Herz sich unstet verhält und gelegentlich viel zu schnell schlägt. Sie kann tödlich sein."


nvl clear

n "\n„Es war ein Wunder, dass du so lange Leben konntest, ohne dass irgendetwas passiert ist”, sagten sie."


n "Und dann passierte es. Meine Krankheit nahm mir alles weg; meine alte Schule war fortan bedeutungslos. Mein Zuhause wurde zu einem weit entfernten Ort. Sowohl meine Freunde als auch meine erste Liebe hörten nach kurzer Zeit einfach auf, mich zu besuchen."


n "Ich wurde zynisch und verbittert. Distanziert und kleinlaut. Zu meiner Verteidigung: Kein Mensch könnte das verhindern, wenn ihm so etwas widerfährt, aber trotzdem hatte ich mich definitiv verändert, als ich das Krankenhaus verließ."


n "Dinge änderten sich. Ich fand in Hanako, Shizune und Misha neue Freunde. Ich fand eine neue Art von „Zuhause” in meinem Wohnheim, neues Interesse an Wissenschaft und der Welt um mich herum, und ich fand neue Lebensziele, wie ich sie noch nie gehabt hatte."


n "Aber ich entdeckte auch andere Dinge."


n "Das Gefühl der Isolation an der Yamaku und in der Umgebung war nicht gänzlich unwillkommen. Die Ruhe schenkte mir einen Seelenfrieden, den ich vielleicht nirgendwo sonst gefunden hätte, aber es gab der Gegend auch ein Gefühl, als würde man vor anderen versteckt werden."


nvl clear

n "\n\nMenschen auf der Straße warfen mir manchmal verlegene Blicke zu, oder drehten ihren Kopf schnell in die andere Richtung, als sie ihr Starren bemerkten. Auch wenn meine Krankheit nicht sichtbar war – meine Uniform war es."


n "Und auch wenn sie es nicht wäre, war ich immer noch anders. Ich nahm täglich siebzehn Tabletten – morgens, mittags und abends. Meine Narbe, auch wenn sie unter Kleidung versteckt war, war immer noch ein permanenter Zeuge meines Zustandes. Und am allerwichtigsten: Es gab die sehr reale Möglichkeit des Todes."


n "Ein schlimmer Sturz. Ein unbedachter harter Schlag auf den Rücken. Ein schlichter, zu gut gemeinter Sprint. Alles hätte meinem Herzen den Rest geben können, und trotz aller Vorsicht taumelte ich mehrere Male am Rand des Abgrunds."


n "\nAber das war in Ordnung. Ich hätte mit alledem Leben können."


n "Weil ich eine letzte Sache gefunden – oder eher wiedergefunden – hatte, nachdem ich an die Yamaku kam."


n "\nWas mir dann wieder einmal vor der Nase weggeschnappt wurde."


nvl clear

n "\nErst jetzt bemerke ich, wie zerbrechlich mein neu gefundenes Glück doch war. Alles hing von ihr ab, der Stütze meines Lebens, seit ich das erste Mal Yamaku als mürrischer, verwirrter und zielloser Transferschüler betrat."


n "Lilly Satou war diese Eine, auf die ich mich vor allen anderen verlassen konnte, und die die Liebe erwiderte, die ich für sie empfand. Doch ich enttäuschte sie, und bemerkte es erst, als es längst zu spät war."


n "Ich dachte, dass ich einfach ein neues Leben beginnen und immer so weitermachen könnte, aber die echte Welt läuft anders. Ich begriff endlich die Bedeutung dieser Worte, nur um festzustellen, dass es zu spät war."


n "\n…"

n "\nDie Räumlichkeiten, in denen ich mich gerade befinde, sind mir nur allzu vertraut. Es ist, als wäre Yamaku lediglich ein Traum gewesen, und ich erhole mich immer noch von meiner ersten großen Herzattacke."


n "Vielleicht fühle ich mich deswegen so müde. Es kommt mir fast vor, als hätte ich die letzten paar Monate meines Lebens in ein paar Minuten durchlebt."


nvl hide dissolve
nvl clear

scene black onlayer master
with shuteye

window show

"Meine Augenlider sind so schwer, dass ich meine Augen nicht offenhalten kann."


window hide
with Pause(1.0)
with shorttimeskip
with Pause(1.0)
window show

"Unverständliches Gemurmel vor meinem Bett rüttelt mich aus meinem Schlaf."


"Mit immer noch geschlossenen Augen kann ich mich konzentrieren, um jemanden herauszuhören. Vermutlich eine Schwester, die sich von einem Arzt verabschiedet."


scene bg hosp_room2 onlayer master
with openeye

"Als ich meine Augen öffne, sehe ich aus dem Augenwinkel, wie sich die Tür schließt."


"Der Arzt steht am Bett, liest ein paar Notizen auf dem Klemmbrett in seinen Händen und betrachtet sorgsam die Seiten."


"Nachdem er seine offenbar sehr wichtigen Dokumente überprüft hat, sieht er auf und bemerkt meinen Blick."
"Jetzt bemerke ich erst, dass an seinem Gesichtsausdruck und seinem allgemeinen Gemüt etwas komisch ist, aber ich kann nicht genau sagen was."


"Arzt" "Ah, Sie sind ja wach… Herr Nakai."


"Sein kurzer Blick auf mein Bettende, um meine Identität zu bestätigen, zeigt, dass auf seinen Dokumenten offenbar nicht mein Name stand."


"Arzt" "Ich muss zugeben, dass das etwas bedauernswert ist. Ihre Eltern haben sie gerade vorhin besucht, als Sie am Schlafen waren. Wenn Sie wollen, könnte ich sie benachrichtigen, dass Sie jetzt wach sind."


hi "Ähm… danke. Das wäre schön."


"Bevor ich mir wirklich darüber im Klaren bin, was ich gesagt habe, gebe ich eine etwas benebelte Antwort von mir. Wahrscheinlich die, die er erwartet hatte."


"Arzt" "Kein Problem."


"Arzt" "Falls Sie irgendwelche Fragen haben, will ich sie Ihnen gerne beantworten. Es sei denn, Sie wollen sich lieber ausruhen; die Betäubungsmittel werden Sie wohl leider noch eine Weile beeinflussen."


"Die Betäubungsmittel… natürlich. Darum habe ich mich wohl so seltsam gefühlt, als ich das erste Mal aufgewacht bin."


"Ich schüttle langsam meinen Kopf, um nicht die Schläuche abzuschütteln oder mir mehr Schmerzen als nötig anzutun. Der Arzt legt daraufhin höflich sein Klemmbrett ab."


hi "Ich schätze… die wichtigste Frage ist… Was genau ist passiert?"


"Arzt" "Um es direkt zu sagen, Sie hatten leider eine erneute Herzattacke. Wobei sie nicht so schwer wie Ihre erste war. Sie hatten großes Glück, dass es so nah bei einem Krankenhaus geschah."


"Arzt" "Nachdem Sie stabilisiert wurden, wurden sie in den Operationssaal gebracht. Darauf folgte eine minimalinvasive Operation, um einen temporären Schrittmacher einzusetzen."


"Arzt" "Der Vorfall geschah vor zwei Tagen, wobei direkt nach ihrer Ankunft die Notfall-Behandlung eingeleitet wurde. Seitdem haben wir Sie unter strenger Beobachtung gehalten, während Sie schliefen."


hi "Werde ich durchkommen? Gibt es irgendwelche Folgeschäden?"


"Arzt" "Verglichen mit der Prozedur nach Ihrer ersten Herzattacke war diese relativ harmlos."


"Arzt" "Obwohl Sie sich in ein paar Tagen einer weiteren Operation unterziehen müssen, um den Schrittmacher zu entfernen, sollte es keine gesundheitlichen Folgeerscheinungen geben."


"Er spricht weiter, wobei das Thema zu einer Wiederholung der Fakten über Arrhythmie und meine Medikation wechselt, die ich bereits größtenteils schon kenne. Ich beginne zu nicken und täusche Interesse vor, während mein Kopf woanders hinwandert."


"Ich fange an, darüber nachzudenken, wie perfekt dieses unaufdringliche Gemälde über seiner Schulter an der Wand hängt, und wie sauber und steril die Umgebung ist – sogar der Arzt selbst."


"Arzt" "Falls Sie mein Gebrabbel langweilt, Herr Nakai, so können Sie es gerne sagen. Gott weiß, wie sehr ich manchmal abschweife."


"Er lacht kurz über seinen selbstironischen Witz, während ich eine verlegene Grimasse schneide, weil ich ertappt wurde."


"Das Lachen des Doktors klingt allerdings irgendwie anders als das von Doc an der Yamaku. Während ich mich frage, wieso, verstehe ich, warum der Mann vor mir einen etwas „komischen” Eindruck macht."


"Seit Lächeln ist gepflegt und steril. Er bringt seinen kleinen Witz perfekt rüber, mit einem gewöhnlichen, harmlosen Lachen."


"Anstatt mit dem Mann zu reden, dessen Name auf dem Schild an seinem Arztkittel steht, ist es, als würde ich mit einem Schauspieler interagieren, der sein vorher einstudiertes Skript abliest, und bei dem jede Handlung vorher choreographiert wurde."


"Jedoch muss er als Arzt vermutlich so sein."


"Er muss sein gepflegtes und steriles Lächeln beibehalten, wenn er mit dem Mädchen plaudert, bei dem sich der Krebs langsam im Körper ausbreitet."
"Er braucht es, wenn er die Frau beruhigt, die gewiss bei einer Geburt sterben wird, und bei jedem anderen sterbenskranken Patienten."


"Dieses kleine bisschen Distanz. Dieses kleine bisschen Reserviertheit."


"Ich frage mich, ob ich zu streng gewesen bin – besonders wenn man bedenkt, dass es bei Weitem keine Neigung ist, die nur Leute in seinem Beruf haben."


"Immerhin hat diejenige, die ich liebte, zwischen sich und anderen die gleiche Distanz gehalten."


"Als ich wieder zum Arzt sehe, bemerke ich, dass ich eine Zeit lang gedankenversunken meinen Kopf geneigt hatte."


"Arzt" "Ich kann nachvollziehen, dass Sie immer noch erschöpft sind. Sie haben eine Menge durchgemacht, und wie ich schon erwähnt habe, werden die Betäubungsmittel Sie immer noch beeinflussen."


"Arzt" "Falls Sie nichts dagegen haben, werde ich Sie nun etwas ruhen lassen und Ihren Eltern für Sie sagen, dass Sie aufgewacht sind."


hi "Ich denke… das wäre gut. Vielen Dank."


stop music fadeout 6.0

"Er nickt flüchtig, bevor er sein Klemmbrett aufhebt, sich seinen Weg zu der großen weißen Tür in der Ecke des Raumes bahnt und sie mit einem dumpfen Knall hinter sich schließt."


"Am Ende bin ich wieder allein."


"Lilly ist weg. Akira ist weg. Hanako müsste am Herumreisen sein, und sogar meine Eltern haben das Krankenhaus schon verlassen."


"Vier blasse, pfirsichfarbene Wände, eine weiße Decke, und ein einzelnes offenes Fenster, um auf die Welt da draußen hinauszublicken."


"Es ist schwierig, an die Zukunft zu denken, wenn die Vergangenheit einen umgibt – klaustrophobisch in ihrem sauberen, sterilen, steifen, nach Bleiche riechendem Griff."


"Ich weiß nicht, was ich tun oder in welche Richtung ich blicken soll. Darum verschlafe ich einfach die Zeit, als wäre all dies nur ein weiterer Traum – genauso wie Yamaku es gewesen ist."


with dissolve



label de_L32:

scene white onlayer master
with dissolve

"Weiß."


"Ein steriles, reines Weiß für einen sterilen, reinen Raum."


$ renpy.music.set_volume(0.05, 0.0, channel="music")
play music music_musicbox fadein 10.0

show bg hosp_ceiling onlayer master:
    alpha 0.0
    linear 5.0 alpha 1.0
with None

"Meine Augen öffnen sich, und ich starre eine Zeit lang lediglich an die Decke. Sie ist ungefähr genauso interessant wie der Fernseher, der in seiner Metallhalterung an der Decke vor dem Bett hängt."


"Tatsächlich war der Fernseher nur in Benutzung, als meiner Eltern hier waren. Sie haben ihn leise angelassen, während sie darauf gewartet haben, dass ich aufwache. Es war ungefähr genauso banal wie das erste Mal, als ich im Krankenhaus gelandet war."


"Vor ein paar Stunden bot mir eine Schwester an, die Lautsprecher des EKGs auszuschalten. Ich lehnte ab, einfach weil das Geräusch für mich mittlerweile vollkommen normal ist."


"Irgendwie ist es fast beruhigend. Die metronomartige Regelmäßigkeit gibt mir zumindest ein bisschen das Gefühl, dass die Zeit voranschreitet – sogar an einem Ort wie diesen."


"Doch nachdem ich beim Aufwachen eine Weile seinem Piepen zugehört habe, bemerke ich, dass in dem Raum noch ein anderes Geräusch ist."


$ renpy.music.set_volume(0.1, 5.0, channel="music")

"Als ich all meine Konzentration auf mein Gehör lenke – eine bei bei diesem ablenkungsarmen Raum eher leichte Aufgabe – kann ich eine leise, blecherne Melodie hören."


"Leicht und ruhig. Die Musik klingt fast fragil, als würde sie von dem EKG-Piepen übertönt werden."


scene bg hosp_room2 onlayer master
with locationchange

"Als ich meinen Kopf leicht zur Seite neige, um die Quelle der Melodie auszumachen, ohne dabei die an mir befestigten Sensoren und Röhrchen abzureißen, bemerke ich eine kleine hölzerne Box, die auf dem Nachttisch neben meinem Bett steht."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

show musicbox open onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Mein Mund öffnet sich kaum merklich, während ich still der winzigen gelben Metallrolle im Inneren beim Rotieren zusehe. Die kleinen Einbuchtungen auf ihrer Oberfläche scheinen zu erscheinen und zu verschwinden, als hätten sie kein Ende."


"Diese Spieluhr… Die habe ich doch Li-"


show musicbox open onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide musicbox onlayer master
with None

"Das Quietschen der Tür reißt mich aus meiner Träumerei. Mein Kopf und mein Herz stehen still, als meine Augen sich auf den Ursprung des Geräusches richten."


"Langer, brauner Rock… pfirsichfarbener, schulterfreier Pullover… blasse, fast prozellanartige Haut… blaue, trübe Augen und langes, gelbes Haar…"


show lilly basic_reminisce_cas onlayer master at center
with charaenter

"Ich kann lediglich zusehen, als Lilly langsam den Raum betritt und ihre Finger zur Orientierung an der Wand entlanggleiten lässt. Mein Verstand kommt abrupt zum Stillstand."


hi "L… Lilly…?"

show lilly basic_oops_cas onlayer master
with charachange

"Sie bleibt umgehend stehen, und ihr ganzer Körper verkrampft sich."


li "Hisao? Warst du das?"


"Ihre Stimme ist leise und nachdenklich, genau wie ihr Gesichtsausdruck."


hi "Ich dachte, du wärst…"


show lilly basic_sad_cas onlayer master
with charachange

"Lilly macht einen zögerlichen Schritt vorwärts, dann einen weiteren – als ob sie sich selbst zurückhalten würde."


show lilly basic_sad_cas_close onlayer master
with characlose

"Aber es gelingt ihr nicht, und als ihr letzter Widerstand zerbröckelt, stürmt sie schließlich zu meinem Bett."


$ ksgallery_unlock("unlock_ev lilly_hospitalclosed")
scene ev lilly_hospitalclosed onlayer master at l_hosp_out
with whiteout

"Als sie sich an mich klammert und Tränen über ihre Wangen fließen, bin ich leicht verwirrt. Immerhin dachte ich noch vor wenigen Minuten, dass sie auf der anderen Seite der Welt sei."
"Nach einem Moment des Zögerns lege ich meine rechte Hand auf ihre weiche Schulter."


li "Hisao! Hisao!"

"Lillys Körper zittert, während ihre Tränen die dunkelblaue Bettwäsche benetzen und ihre Emotionen durch ihre sorgfältig aufrechterhaltene Fassade brechen."


"Jetzt, wo ihr Gesicht näher ist und ihre blasse Haut vom Sonnenlicht, das durch das Fenster fällt, beleuchtet wird, bemerke ich, dass ihre Wangen röter sind, als sie sein sollten."


hi "Schon okay, Lilly. Ich bin okay. Du brauchst nicht zu…"


$ ksgallery_unlock("unlock_ev lilly_hospital")
show ev lilly_hospital onlayer master at l_hosp_out
with charachange

"Sie richtet sich rasch auf und unterdrückt entschlossen ihre Tränen, wobei in ihren feuchten Augen Traurigkeit und Sturheit zurückbleiben. Ihre stolze Natur, mit der ich schon immer zu kämpfen hatte, überrascht mich wieder einmal."


li "Sag mir nicht, dass ich mir keine Sorgen um dich machen soll, Hisao!"


li "Lass mich weinen… Nur dieses eine Mal…"


"Ich bin sprachlos. Sie wartet auf eine Antwort, doch ihre Fassung zerbricht schon nach wenigen Sekunden wieder."


show ev lilly_hospitalclosed onlayer master at l_hosp_out
with charachange

"Ich schlucke schwer und versuche, meine eigenen Emotionen zu bändigen, während sie in mein Bett schluchzt. Eine seltsame Mischung aus Erleichterung und Schwermut quillt in mir auf."


"Lilly ist… hier. Sie ist wirklich hier. Wenn ich ihre Haut nicht unter meiner Hand spüren könnte, würde ich kaum meinen Augen trauen."
"Meine Mühen waren nicht umsonst; der Versuch meines Körpers, alles von mir zu nehmen, was mir wichtig ist, wurde wieder einmal vereitelt."


"Doch nun… bin ich nicht so glücklich darüber, wie ich dachte."


"Sie hier zu sehen, wie sie meinetwegen weint… Das ist das Einzige, was ich vermeiden wollte, seit ich mich in sie verliebt habe. Nein, sogar seit ich das Krankenhaus verlassen habe."


hi "Es tut mir leid, Lilly. Es ist meine Schuld, dass ich hier bin. Ich hätte mir nicht so viel abverlangen dürfen."


"Ich schnaube selbstverachtend."


hi "Nach all den Monaten, in denen ich so vorsichtig war, damit sich niemand um mich sorgen muss, hab ich so etwas angerichtet. Ich schätze, ich bin ziemlich bescheuert."


scene bg hosp_room2 onlayer master
show lilly basic_weaksmile_cas_close onlayer master at center
with whiteout

"Mit ein paar Schniefern und einem langen Atemzug schafft es Lilly, sich zusammenzureißen und sich etwas zu beruhigen."


"Trotz ihrer roten Wangen, feuchten Augen und den immer noch sichtbaren Bahnen, die ihre Tränen hinterlassen haben, trägt sie grazil dieses schwache Lächeln, das so typisch für sie ist."


li "Du brauchst dir nicht die Schuld zu geben. Ich habe gehört, dass es passiert ist, als du mir auf der Straße hinterhergerannt bist, oder?"


hi "Trotzdem…"


"Sie wischt sich ihre Augen mit ihrem Handrücken ab und kehrt immer mehr zu ihrem alten Ich zurück, als der Ansturm der Emotionen abklingt."


show lilly basic_reminisce_cas_close onlayer master
with charachange

li "Warum bist du mir nachgelaufen, Hisao?"


show lilly basic_concerned_cas_close onlayer master
with charachange

"Ich will gerade antworten, doch dann verzieht sich ihr Gesicht."


li "Selbst nachdem ich Lebewohl gesagt, und die Yamaku verlassen habe…"


"Sie nimmt sich einen Moment, um sich aufzurichten, wobei ihre Emotionen beinahe wieder hervorbrechen."


hi "Ich wollte nur sagen, dass es mir leidtut."


show lilly basic_surprised_cas_close onlayer master
with charachange

li "Leidtut?"


hi "Für all die Male, an denen ich nicht da war, als du mich gebraucht hast."


hi "Bis jetzt dachte ich, dass es genug wäre, wenn du nur da bist. Ich brauchte dich nur an meiner Seite, um jeden Tag besser zu machen."


hi "Auch wenn mein Körper so ein Wrack ist, will ich dir helfen, Lilly; da sein, wenn du jemanden brauchst."


show lilly basic_weaksmile_cas_close onlayer master
with charachange

li "Aber du warst immer da, Hisao…"


hi "Warum wolltest du nach Schottland gehen, Lilly?"


show lilly basic_sleepy_cas_close onlayer master
with charachange

li "Warum…? Das habe ich dir doch schon gesagt: Weil Akira es tut, und weil mich meine Familie zu sich gerufen hat."


hi "Warum hast du nicht gesagt, dass du gehen willst?"


show lilly basic_oops_cas_close onlayer master
with charachange

li "Ich…"


hi "Ich bin nicht oft stur, aber diesmal muss ich es wohl sein. Ich will, dass du hierbleibst, Lilly."


hi "Ich will, dass du bleibst, wo alle wohnen, die du kennst und wo all deine Träume und Ambitionen entstanden sind. Wenn du bleibst, werde ich niemals von deiner Seite weichen. Ich werde dich nicht noch jemanden verlieren lassen."


hi "Als ich meine Herzattacke hatte, wurde ich von allem und jedem weggerissen, den ich kannte. Du hast mir ein neues Leben gezeigt, nachdem ich an die Yamaku kam. Ich habe meine Vergangenheit verloren, aber du hast mir eine Zukunft gezeigt."


hi "Es ist wahr, dass ich nicht immer für dich dagewesen bin. Ich bin unverlässlich, habe manchmal gelogen, und ich dachte, ich würde dich verstehen, obwohl ich mich nicht einmal selbst verstanden hatte."


hi "Wie dem auch sei – ich will dir auch eine Zukunft geben. Ich will für dich da sein, um deine Last und dein Glück mit dir zu teilen, genau wie ich es dir damals in Hokkaido versprochen habe."


hi "Ich will, dass du mir vertraust. Ich weiß, dass ich Probleme hatte, auf dich zu vertrauen, nachdem ich nach meiner Herzattacke so viele Freunde verloren hatte, aber so weiß ich, dass es furchtbar sein kann, anderen nicht vertrauen zu können."


hi "Darum kann ich nicht mitansehen, wie du das alles einfach so wegwirfst. Ich will niemals, dass du das Gleiche durchmachst wie ich. Ich würde alles tun, um das zu verhindern."


show lilly basic_weaksmile_cas_close onlayer master
with charachange

li "Wenn du willst, kannst du ziemlich standhaft sein, nicht wahr?"


hi "Wie gesagt, kommt nicht oft vor."


"Mein schwaches Lächeln verfliegt jedoch, als die Kanüle sich etwas in meinen Arm bohrt. Eine rigorose Erinnerung daran, wie meine Krankheit mich zurückhält."


show lilly basic_concerned_cas_close onlayer master
with charachange

"Lillys Gesicht verzieht sich, als ich einen kleinen Schmerzlaut von mir gebe. Seufzend wünsche ich mir, ich hätte ihn besser unterdrückt."


hi "Die ganze Zeit, nachdem ich das Krankenhaus verlassen hatte, wollte ich niemandem Sorgen bereiten, aber ich kann nicht einmal verhindern, dass die, die ich am meisten liebe, meinetwegen weint."


hi "Selbst wenn ich endlich in der Lage bin, meine Gefühle in Worte zu fassen, komme ich mir mit so einem Körper ziemlich nutzlos vor."


hi "Jedes Mal, wenn ich etwas ergreifen wollte, wurde es einfach weggeschnappt, und sogar jetzt war es nur Glück, dass alles gut ausgegangen ist."


hi "Ich schätze, das ist noch etwas, wofür ich mich entschuldigen sollte. Ich bereite dir nichts als Sorgen. Sogar jetzt besteht kaum eine Chance, dass ich ein auch nur annähernd erfülltes Leben leben kann."


"Das Gefühl von Lillys warmer, weicher Hand, die sich über meine linke Wange bewegt, lässt mich meinen Kopf heben. Sie lächelt sanft, als sie mich berührt."


show lilly basic_smileclosed_cas_close onlayer master
with charachange

li "Ich denke, so etwas zu sagen, passt zu dir. Du warst schon immer so ehrlich und unsicher."


show lilly basic_smile_cas_close onlayer master
with charachange

li "Du warst auch zurückhaltend und freundlich, hattest überaus viel Geduld mit Hanako und warst doch neugierig auf alles und jeden."


show lilly basic_weaksmile_cas_close onlayer master
with charachange

li "Als ich sagte, dass ich dich vermisst habe, als ich bei meiner Familie war, habe ich weder gelogen noch übertrieben. Ich musste immerzu an dich denken, und das half mir durch diese Zeit."


show lilly basic_reminisce_cas_close onlayer master
with charachange

li "Darum war ich so verwirrt, als mich meine Familie zu sich rief. Ich wusste nicht, was ich machen sollte. Selbst nachdem ich dachte, ich hätte meine Entscheidung getroffen, hast du dein Bestes gegeben, um mich zum Zweifeln zu bringen."


show lilly basic_weaksmile_cas_close onlayer master
with charachange

li "Ich habe dir meine Liebe nicht aus Mitleid oder in dem Glauben gestanden, dass du anders wärst als du bist. Ich tat es, weil ich dich niemals verlieren will und du immer ein Teil meines Lebens bleiben sollst – was auch passieren mag."


show lilly basic_smileclosed_cas_close onlayer master
with charachange

li "Du bist ein wunderschöner Mensch, Hisao. Dein Herz ändert nichts daran. Also bitte, entschuldige dich nicht mehr dafür, wer du bist."


"Für eine lange Zeit herrscht Stille im Raum."


"Ich bin mir nicht wirklich sicher, was dieses neu geborene Gefühl in meinem Inneren ist, aber diese Frage wird unwichtig, als ich wortlos in Lillys lächelndes Gesicht blicke – warm und sanft, so wie es schon immer gewesen ist."


"Erst als ihr Daumen über meine Wange fährt und einen einzelnen Tropfen Nass wegwischt, begreife ich, dass das alles ist, was ich je wollte."


"Es fühlt sich an, als wäre es das erste Mal, dass ich Lilly ein ehrliches, großes Lächeln schenke. Als Lilly das mit ihrer Handfläche spürt, erwidert sie die Geste."


"Mehr Zeit vergeht, bis einer von uns beiden ein Wort sagt. Keiner von uns muss dem anderen noch seine Gefühle mitteilen."


hi "Ich weiß, ich kann dir nicht versprechen, dass ich immer da sein werde, oder dass wir für immer zusammen sein werden."


"Mit ein paar Schwierigkeiten hebe ich langsam meine Hand und lege sie auf ihre blasse Schulter."


hi "Aber… ich denke, ich kann dich wenigstens nächstes Jahr zu Tanabata ausführen, um dieses Jahr wiedergutzumachen."


show lilly basic_emb_cas_close onlayer master
with charachange

"Lilly blickt überrascht drein, allerdings kann ich es ihr nicht verübeln."


li "Du hast… daran gedacht?"


hi "Ich habe ein ziemlich gutes Gedächtnis. Manchmal."


show lilly basic_giggle_cas_close onlayer master
with charachange

"Sie hebt leicht ihren Kopf und nimmt ihre Hand von meiner Wange, während sie ein leises, amüsiertes Kichern von sich gibt. Ich lächle gedankenverloren, weil es so aufrichtig und mädchenhaft klingt."


show lilly basic_cheerful_cas onlayer master
with charadistant

"Während sie ihr warmes Lächeln beibehält, sammelt sie sich und stellt sich gerade hin, wobei ihre Hand auf meiner Brust ruht."


"Es kommt mir so vor, als würde ich sie zum ersten Mal sehen. Die Sonne leuchtet hinter ihr genauso durch das Fenster wie damals, als ich zum ersten Mal in den Raum spazierte, in dem sie gerade Tee trank."


show lilly basic_smile_cas onlayer master
with charachange

li "Na gut. Wollen wir uns dann versprechen, dass wir nächstes Jahr zusammen zu Tanabata gehen?"


"Auch wenn sie mich dabei nicht sehen kann, nicke ich zustimmend."


hi "Ich verspreche es."


show lilly basic_smileclosed_cas onlayer master
with charachange

li "Ich verspreche es."


window hide

stop music fadeout 4.0




label de_L33:

window hide None

play ambient sfx_parkambience fadein 6.0

scene bg lilly_hilltop onlayer master
with Dissolve(3.0)

play music music_lilly fadein 5.0

window show

"Akira, Lilly und ich sitzen still auf der grasbedeckten Böschung hoch über dem Dorf, während die Brise sanft durch den wolkenlosen Himmel weht."


"Wir sind zwar nur ein paar Minuten Fußweg vom Dorf entfernt, auf einem Hügel direkt außerhalb, aber die Aussicht ist gänzlich unerwartet."


show lilly basic_smileclosed_cas_close onlayer master:
    left
    ypos 1.1
with charaenter

"Lilly sitzt mit geschlossenen Augen neben mir, während die sanfte Brise durch ihr Haar weht."


li "Das ist eine schöne Gegend."


hi "Ja. Ich wusste gar nicht, dass es in der Nähe der Yamaku so einen Ort gibt."


show akira basic_ending_close onlayer master:
    right
    ypos 1.1
with charaenter

aki "Und natürlich war ich diejenige, die ihn finden musste."


"Akiras Grinsen ist aufrichtig, aber ihr Ton unterscheidet sich leicht von ihrer üblichen sorglosen Natur."


show akira basic_smile_close onlayer master
with charachange

aki "Aber es ist schön, dass du aus dem Krankenhaus raus bist, Hisao."


hi "Niemanden freut das mehr als mich. Ich kann Krankenhäuser nicht ab."


aki "Also geht ihr Zwei morgen wieder zur Schule?"


$ doublespeak(hi, li, "Jupp.", "Jupp.")


show akira basic_ending_close onlayer master
with charachange

"Akira kichert amüsiert, bevor sie wieder zurück auf das unter uns liegende Dorf sieht. Die Bäume zwischen den Gebäuden wiegen sich im Wind."


hi "Schade, dass wir in den Sommerferien nicht nach Hokkaido fahren oder zu Tanabata gehen konnten."


show lilly basic_weaksmile_cas_close onlayer master
with charachange

li "Ich würde mir keine Sorgen deswegen machen. Es gibt immer ein nächstes Mal."


show akira basic_smile_close onlayer master
with charachange

aki "Vor den nächsten Sommerferien macht ihr doch euren Abschluss, oder?"


hi "Ja. Aber denk daran, dass wir danach auch noch an die Uni gehen."


aki "Geht ihr an die gleiche?"


show lilly basic_smile_cas_close onlayer master
with charachange

li "Wahrscheinlich. Unsere Noten sind gut genug, um die Eintrittsbedingungen zu erfüllen."


hi "Du hörst dich da so sicher an…"


show lilly basic_cheerful_cas_close onlayer master
with charachange

li "Keine Sorge, in den meisten Fächern bist du besser als ich."


hi "Das werden wir wohl zu gegebener Zeit herausfinden."


show akira basic_laugh_close onlayer master
with charachange

aki "So ist es richtig. Genießt einfach eure Zeit an der Yamaku solange ihr noch da seid."


show lilly basic_weaksmile_cas_close onlayer master
with charachange

"Lilly seufzt traurig."


show lilly basic_reminisce_cas_close onlayer master
with charachange

li "Musst du wirklich zurück nach Schottland?"


show akira basic_resigned_close onlayer master
with charachange

aki "Ja. Die Leute wollen mir so schon die Hölle heiß machen."


hi "Du solltest gar nicht so lange bleiben?"


show akira basic_ending_close onlayer master
with charachange

"Sie zeigt ihr typisches Grinsen."


aki "Meinem Freund einen Reisepass zu beschaffen, hat etwas Zeit gebraucht."


hi "Du nimmst ihn mit?"


show akira basic_smile_close onlayer master
with charachange

aki "Erst mal nur eine Weile. Er ist ein ziemlich pragmatischer Kerl, darum denke ich, dass er sich gut zurechtfinden wird."


show akira basic_lost_close onlayer master
with charachange

"Akira schnaubt amüsiert."


aki "Wenn sich unser Vater durchgesetzt hätte, wäre ich schon vor langer Zeit weg gewesen."


show akira basic_laugh_close onlayer master
with charachange

aki "Aber ich konnte mir doch nicht die Chance entgehen lassen, ein bisschen länger mit meiner kleinen Lieblingsschwester zusammen zu sein."


show lilly basic_smileclosed_cas_close onlayer master
with charachange

"Sie lehnt sich nach rechts und gibt Lilly eine feste, verspielte Umarmung, wodurch sie beträchtlich aufgemuntert wird."


li "Allerdings ist es schön, ein letztes Mal mit dir zusammen zu sein."


hi "Das finde ich auch, wenn du mich fragst."


show akira basic_smile_close onlayer master
with charachange

aki "Heh, danke ihr Zwei. Ich werde versuchen, ab und zu wiederzukommen, keine Sorge."


show lilly basic_reminisce_cas_close onlayer master
with charachange

li "Eine Schande, dass das Geschäft einen so beschäftigt hält."


show akira basic_lost_close onlayer master
with charachange

aki "Der Laden läuft leider nicht von allein, und ich glaube, dort drüben wird es genauso sein."


show akira basic_smile_close onlayer master
with charachange

aki "In Anbetracht dessen… mache ich mich besser auf den Weg."


hi "Viel Spaß da drüben, Akira."


show akira basic_laugh_close onlayer master
with charachange

aki "Haha, werde ich haben."


show akira basic_smile_close onlayer master at right
with dissolvecharamove

"Mit einem leichten Grummeln richtet sie sich mit ihren Händen vom Boden auf und klopft sich den Staub ab."


show akira basic_lost_close onlayer master at right
with charachange

aki "Na dann, ich mach mich lieber auf den Weg. Der Flieger wartet schließlich nicht auf mich."


"Eine gewisse, unübliche Wehmut liegt in ihrer Stimme, und ihre Augen sind fest auf ihre Schwester gerichtet."


show lilly basic_weaksmile_cas_close onlayer master
with charachange

li "Ich komme zurecht, Akira."


show akira basic_resigned_close onlayer master
with charachange

aki "Ja, ich weiß."


show lilly basic_smileclosed_cas_close onlayer master
with charachange

li "Komm schon, so schlimm ist es nicht. Du wirst uns bald wiedersehen können."


"Es ist seltsam, dass diesmal Lilly eine zweifelnde Akira beschwichtigt. Sie hat sich wirklich verändert."


show lilly basic_smile_cas_close onlayer master
with charachange

li "Bis dann, Akira."


hi "Mach's gut."


show akira basic_smile_close onlayer master
with charachange

"Für eine Sekunde sieht die schwarz gekleidete Gestalt auf uns beide herab und lächelt breit. Vielleicht breiter als ich es je bei ihr gesehen habe."


show akira basic_boo onlayer master at tworight
with charadistant

"Sie lässt einen langen, etwas zitternden Atemzug entweichen, um sich zu sammeln, bevor sie geht, doch schließlich schlüpft ihre Hand in ihre Hosentasche, und sie dreht sich auf den Fersen um."


"Und dann zieht sie davon, während sie dabei eine Hand in die Höhe hält."


show akira basic_ending onlayer master
with charachange

aki "Ich seh euch später, ihr Zwei!"


hide akira onlayer master
with charaexit

"Ein Jazz-Song ohne Takt, Melodie oder Ziel bis zum bitteren Ende."


show bg lilly_hilltop onlayer master at bgright
show lilly basic_smileclosed_cas_close onlayer master at center
with dissolvecharamove

"Wir sitzen einige Augenblicke still da, dann stehen Lilly und ich auch auf und klopfen uns den Staub ab."


"Mit einem breiten Lächeln wende ich mich zu ihr und halte ihr meine Hand entgegen."


hi "Wollen wir dann los?"


"Mit einem leichten Nicken und einem Lächeln so schön und warm wie immer nimmt sie meine Hand in ihre."


show lilly basic_cheerful_cas_close onlayer master
with charachange

li "Das sollten wir, Hisao."


scene unlock_ev lilly_goodend onlayer master
show evbg lilly_goodend onlayer master:
    truecenter
    zoom 3.0 subpixel True
    1.0
    linear 0.5 zoom 0.9
    easein 12.0 zoom 0.8
show evfg lilly_goodend onlayer master:
    truecenter
    zoom 6.0 subpixel True
    1.0
    linear 0.5 zoom 1.2
    easein 12.0 zoom 0.8
with whiteout

"Als wir uns auf den Weg zur Schule machen, graviert sich dieses wundervolle Lächeln in meinem Gedächtnis. Dieses wundervolle Lächeln, das wir beide teilen."


"Unsere Vergangenheiten mögen von Zeit zu Zeit von Trauer überschattet werden, aber sie sind auch ein unabänderlicher Teil unseres Lebens und unserer Persönlichkeiten."
"Selbst wenn ich eine Kleinigkeit ändern könnte, würde ich es nicht tun, weil meine Vergangenheit das ist, was mich hierher geführt hat."


"Darum werden wir zusammen voranschreiten – mit allem, was uns passiert ist, und allem, was noch auf uns zukommen wird…"


"Vorwärts… in Richtung Zukunft. Unserer Zukunft."


window hide Dissolve(1.0)

stop ambient fadeout 2.0
stop music fadeout 2.0

scene black onlayer master
with Dissolve(1.0)

with Pause(1.0)

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
