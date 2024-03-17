label de_S17:

window hide None

scene bg school_hallway3 onlayer master
with locationchange

nvl clear
nvl show dissolve

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_normal fadein 3.0

n "\n\nDie nächsten Tage vergehen ereignislos und mit erstaunlicher Geschwindigkeit. Ich finde neue Motivation, die Zeichensprache zu lernen. Es scheint, als hätte ich ein Talent dafür, also kommt es gar nicht infrage, es halbherzig zu tun."


n "Die Sommerferien stehen bevor. Auch wenn ich dachte, dass die Arbeit im Schülerrat im gleichen Maß nachlassen würde, wie mein Unterricht träger wird, ist das nicht der Fall. Jeden Tag werde ich mit zunehmend sinnloser Arbeit überhäuft."


n "Egal wie sehr ich es auch will, ich finde zur Zeit nicht einmal eine freie Minute, um mit Shizune zu reden. Jedes Mal, wenn ich sie ansehe, ist ihr Gesicht zwischen irgendwelchen Nachweisbüchern oder in Papierstapeln vergraben, die wieder und wieder überprüft werden müssen."


n "\n\n Heute bin ich früh aufgestanden, um vor allen anderen zur Schule zu kommen, in der Hoffnung, Shizune zu erwischen. Sie hat die Angewohnheit, Morgens als erste zu kommen, um pünktlicher als alle anderen Schüler zu sein. Leider bin ich wohl noch früher da als sie."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

play sound sfx_doorclose

window show

"Das Zuschnappen der Tür zum Schülerratsraum zu meiner Rechten sagt mir, dass das nicht der Fall ist. Ich schätze, ich bin kurz nach ihr angekommen."


play sound sfx_dooropen

scene bg school_council onlayer master
with locationchange

"Ich betrete den Raum und tippe Shizune auf die Schulter, um ihre Aufmerksamkeit zu bekommen."






show shizu behind_smile onlayer master at center
with charaenter

"Vielleicht erwartet sie eine Unterhaltung, weswegen sie die Orangensaftpackung in ihrer Hand ablegt."


ssh "Guten Morgen."


his "Wo ist deine bessere Hälfte?"


show shizu adjust_frown onlayer master
with charachange

ssh "Wir sind eigenständige Individuen."


"Wenn ich darüber nachdenke, müssen sie das ziemlich oft hören. Wahrscheinlich kam die Antwort deshalb so wie aus der Pistole geschossen."


show shizu basic_normal onlayer master
with charachange

ssh "Du bist früh dran. Das ist gut, du kannst mir helfen, einige Handouts durchzusehen. Die werden nachher noch ausgeteilt."


his "Ich kam eigentlich früh hierher, damit ich dich sehen kann, ohne arbeiten zu müssen."


show shizu behind_smile onlayer master
with charachange

ssh "Misha zufolge ist es nichts Neues, dass du früh da bist."


his "Ist es für dich auch nicht."


show shizu adjust_happy onlayer master
with charachange

ssh "Soll das heißen, dass du ein Wettrennen willst?"


"Shizune rückt lässig ihre Brille zurecht – eine Geste, die verbergen soll, wie aufgeregt sie bei dem Gedanken ist, etwas so Belangloses zu einer ernsten Herausforderung machen zu können."
"Ich glaube, je kleiner die Angelegenheit ist, desto mehr reizt es sie."


his "Es ist kein Wettrennen. Willst du daraus einen Wettkampf machen? Ich nicht."


"Fast vergesse ich, den letzten und wichtigsten Teil hinzuzufügen."


show shizu behind_smile onlayer master
with charachange

ssh "Na gut, schon okay. Das Schuljahr hat noch zu viele Tage übrig, es würde mir so oder so zu langweilig werden."


"Daraufhin greift Shizune ihren Saft und trinkt ihn aus. Ich frage mich, ob sie versuchen wird, die leere Packung in hohem Bogen in den Müll zu werfen, doch sie lässt es."
"Sie scheint sogar verwirrt zu sein, weil ich so enttäuscht aussehe. Ich sollte lieber direkt zur Sache kommen."


his "Ich wollte einfach nur reden. Die Ferien stehen praktisch vor der Tür, weißt du."


his "Und wir sollten überhaupt mehr Zeit miteinander verbringen. Ich hatte gedacht, wir könnten das über den Sommer tun."


show shizu adjust_blush onlayer master
with charachange

"Shizunes Gesicht wird genauso rot wie meins wahrscheinlich schon ist, und sie rückt sich verlegen ihre Brille zurecht. Was für eine Allzweckgeste. Sie denkt sorgfältig über ihre nächsten Worte nach und tippt nachdenklich ihre Finger aneinander."


show shizu basic_normal onlayer master
with charachange

ssh "Du meinst, wie ein Date?"


his "Nur weil wir irgendwo hingehen, macht es das sofort zu einem Date?"


show shizu behind_blank onlayer master
with charachange

ssh "Ist es das nicht?"


show shizu adjust_frown onlayer master
with charachange

ssh "Ich will, dass es ein Date ist."


his "Dann ist es eins."


show shizu basic_happy onlayer master
with charachange

"Shizuna klatscht zustimmend einmal ihre Hände zusammen, bevor sie hinzufügt:"


show shizu behind_blank onlayer master
with charachange

ssh "Aber nicht heute."


show shizu basic_normal2 onlayer master
with charachange

ssh "Ich fahre für eine Woche weg, um meine Familie zu besuchen."


"Das ist eine seltsam formelle Weise, das zu sagen, und mein Interesse wird geweckt."
"Vielleicht ist ihre Familie von der prüden und traditionellen Art und lebt in einem altertümlichen Anwesen mit einem kleinen Fluss und einem Karpfenteich, wo alle immerzu Kimonos tragen."


"Es ist eine wilde Vermutung, aber manchmal macht es Spaß zu spekulieren. Ich frage mich, ob sich Shizune wie eine ruhige, erwachsene und gute Tochter wie Lilly verhält, wenn sie bei ihrer Familie ist."


"Ich kann es mir nicht vorstellen, aber wenn es auch nur eine Chance gibt, dass es so ist, dann muss ich es sehen."


his "Nur eine Woche? Dann kann es keine sehr weite Reise sein."


show shizu behind_frustrated onlayer master
with charachange

ssh "Natürlich nicht, sie sind schließlich noch in Japan."


his "Ach so…"


show shizu adjust_happy onlayer master
with charachange

ssh "Es ist nicht so, als ob du mit mir kommen könntest. Wolltest du darauf hinaus?"


his "Warum nicht?"


show shizu basic_normal2 onlayer master
with charachange

ssh "Es würde dir nicht gefallen."


his "Das weißt du nicht. Es könnte Spaß machen."


his "Ah, fast vergessen: Fährst du allein, oder kommt Misha mit dir? Kann deine Familie Zeichensprache?"


show shizu behind_blank onlayer master
with charachange

ssh "Misha kommt mit."


"Dass sie den zweiten Teil der Frage nicht beantwortet hat, sagt mir schon einiges."


"Ich frage mich, wie wohl ihre Kindheit war, wenn ihre Familie nicht mit ihr kommunizieren kann. Vermutlich hat sie alles auf den Block geschrieben, den sie mit sich herumträgt und manchmal noch aus dem Nichts holt."


"Für gewöhnlich ist das, wenn weder Misha noch ich in der Nähe sind. Dann sehe ich manchmal aus der Ferne, wenn sie ihn als letztes Mittel hervorholt und dabei die ganze Zeit ihr Gesicht verzieht."


his "Wenn Misha mitkommt, dann komme ich auch mit."


show shizu basic_normal onlayer master
with charachange

ssh "Magst du Misha?"


his "Es geht ums Prinzip."


"Ich finde Gefallen an der Vorstellung, dass Shizune tatsächlich eifersüchtig sein könnte, aber ich bezweifle es. Für gewöhnlich trägt sie ihre Emotionen auf dem Gesicht, und ich habe nichts gesehen, das meine Theorie unterstützen würde."


show shizu adjust_frown onlayer master
with charachange

ssh "Ich glaube, dir ist einfach nur langweilig."


show shizu behind_smile onlayer master
with charachange

ssh "Ist schon okay. In Ordnung, wir fahren alle zusammen. Darauf hatte ich sowieso von Anfang an gehofft."


show shizu adjust_smug onlayer master
with charachange

ssh "Du kannst den Schülerrat heute nicht schwänzen, um deine Koffer zu packen, nur weil du so kurzfristig mit uns mitkommst. Das ist keine Entschuldigung!"


his "Es geht schon, ich habe sowieso kaum etwas zu packen."


show shizu basic_normal onlayer master
with charachange

"Shizune hält inne und legt nachdenklich ihre Fingerspitzen zusammen."


show shizu behind_blank onlayer master
with charachange

ssh "Du musst sehr kurzfristig auf diese Schule gekommen sein."




label de_S17a:

"Es kann sein, dass sie sich an die Zeit erinnert, als sie und Misha unerwartet in mein Zimmer geplatzt sind und einen Blick auf all meine Medikamente erhascht haben. Das war ein peinlicher Moment, den ich gerne vergessen würde."


"Die Art und Weise, wie sie selbst jetzt noch diesem Thema ausweicht, macht mich nur noch unbehaglicher."




label de_S17x:
his "Ja, das stimmt. Es war eine sehr kurzfristige Entscheidung. Aber es lief besser, als ich erwartete hatte."


"Ich hoffe, Shizune geht darauf nicht näher ein, und zu meiner Erleichterung tut sie es auch nicht."


show shizu adjust_happy onlayer master
with charachange

ssh "Mein Zuhause ist in einem besonders schönen Teil von Saitama."


show shizu behind_smile onlayer master
with charachange

ssh "Wir fahren früh am Morgen, also sei fertig. Lass uns später weiter darüber reden, okay? Im Moment überprüfen sich diese Handouts nicht von allein, und du wirst mir dabei helfen."


stop music fadeout 3.0

hide shizu onlayer master
with charaexit

"Als Shizune sich in ihre Arbeit stürzt und mich dabei mitzerrt, wirkt es fast so, als ob sie sich auf die Fahrt freut."


scene black onlayer master
with dissolve



label de_S18:

scene bg school_dormhallway onlayer master
with locationchange

play music music_daily fadein 0.5

"Als Shizune und Misha früh am nächsten Morgen kommen, um mich abzuholen, tragen sie etwas anderes als die Schuluniformen, an deren Anblick ich mich schon gewöhnt habe."


show shizu behind_blank_cas onlayer master at center
with charaenter

"Es ist logisch, da wir Ferien haben, aber es ist trotzdem seltsam. Shizunes Kleid ist stilvoll und modisch, fast zu viel für einen ruhigen Ort wie Yamaku."
"Wenn ich daran zurückdenke, was sie an Tanabata anhatte, fange ich an, eine Vorliebe bei ihr zu erkennen."


"Ihre Kleidung ist durchweg sehr geschmackvoll, reif und sehr gut durchdacht. Deshalb frage ich mich, warum sie selbst so ein Kindskopf ist."


show bg school_dormhallway onlayer master at bgright
show shizu behind_blank_cas onlayer master at tworight
with charamove

show misha perky_smile_cas onlayer master at twoleft
with charaenter

"Na ja, wenigstens Mishas Kleidung spiegelt ihren Charakter wider."


show shizu adjust_frown_cas onlayer master
with charachange

ssh "Du nimmst ja so wenig mit."


hi "Sagte ich doch. Ich sagte, ich hätte nicht viel zu packen."


show shizu basic_frown_cas onlayer master
with charachange

"Shizune schmollt und stupst ihre eigene, ziemlich große Gepäcksammlung mit ihren Füßen, als wäre es ihr peinlich. Misha hat nur einen Koffer dabei, aber der ist fast größer als sie. Ihr scheint das auch etwas peinlich zu sein."


"Gott, der Koffer ist so groß wie ein Kleinwagen. Dazu ist die grüne Farbe auch noch beunruhigend. Es sieht aus wie etwas, womit man Leichen transportiert. So wie die beiden gerade aussehen, überkommt mich das Verlangen, sie zu ärgern."


hi "Ohh, das ist Pech für dich und Misha, nicht wahr? Diese riesigen Koffer tragen zu müssen. Ihr solltet nächstes Mal leichtes Gepäck mitnehmen – so wie ich. Alles passt in einen kleinen Koffer."


show misha hips_grin_cas onlayer master
with charachange

mi "Wie James Bond~!"


hi "Ja, genau wie James Bond."


show shizu adjust_frown_cas onlayer master
with charachange

shi "…"


"Konzentriert zupft Shizune sanft an ihrer Brille."


show shizu basic_normal_cas onlayer master
with charachange

ssh "Wir sollten das Gepäck gleichmäßig aufteilen."


show misha sign_smile_cas onlayer master
with charachange

mi "Wow~! Das ist eine tolle Idee, Shicchan~!"


hi "Was? Nein."


show shizu adjust_smug_cas onlayer master
with charachange

ssh "Es würde uns allen zugute kommen."


show misha cross_laugh_cas onlayer master
with charachange

mi "Jep~! Wahaha~!"


hi "Ich muss ablehnen."


show shizu cross_angry_cas onlayer master
with charachange

ssh "Du bist überstimmt!"


"Als sie es gebärdet, stürzt sie sich beinahe auf mich. Erschreckend."


hi "Schon gut. Ich habe kein Problem damit, etwas mehr zu tragen. Ich dachte einfach, es wäre lustig, euch beide auf den Arm zu nehmen."


hi "Aber falls ihr versucht hättet, mich alles tragen zu lassen, wäre ich mit diesem riesigen grünen Koffer den Berg wie mit einem Schlitten heruntergefahren."


show shizu adjust_smug_cas onlayer master
with charachange

shi "…"


"Das scheint Shizune zum Lachen zu bringen, und sie hält sich eine Hand vor den Mund, um es zurückzuhalten. Es ist, als ob sie es verbirgt."
"Ich frage mich, ob sie lachen kann. Wenn nicht, könnte das der Grund sein, warum sie das tut. Das macht mich irgendwie traurig."


stop music fadeout 3.0

scene bg city_station onlayer master
with locationskip

"Nachdem das geklärt ist, machen wir uns auf den Weg zum Bahnhof."
"Die weitere Fahrt ist sehr ereignislos. Shizune und Misha schaffen es, fast sofort einzuschlafen. Ich hingegen kriege das nicht hin. Das ist mir noch nie passiert. Vielleicht liegt es an meinen Medikamenten."


scene bg shizu_houseext onlayer master
with shorttimeskip

play music music_soothing fadein 0.5

"Als wir bei Shizunes Haus ankommen, ist es um einiges größer, als ich es mir vorgestellt hatte. Ich glaube riesig wäre keine Übertreibung."


hi "Du lebst in einer Villa?"


show shizu cross_angry_cas onlayer master at center
with charaenter

"Shizune stellt sich sofort auf Zehenspitzen, damit wir auf gleicher Augenhöhe sind und runzelt die Stirn, nachdem Misha ihr meinen Kommentar übersetzt hat. Es ist, als ob sie sagen würde: „Wie kannst du so etwas auch nur unterstellen?”"


show shizu basic_frown_cas onlayer master
with charachange

ssh "Das ist nur ein normales Haus. Nicht annähernd so pompös wie eine Villa."


"Dann denke ich, dass wir diese Begriffe ziemlich unterschiedlich definieren."


show bg shizu_houseext onlayer master at bgright
show shizu basic_frown_cas onlayer master at tworight
with charamove

show misha hips_grin_cas onlayer master at twoleft
with charaenter

mi "Wahaha~! Hicchan, bist du überrascht? Soll ich dir zeigen, wo dein Zimmer ist?"


show shizu behind_blank_cas onlayer master
with charachange

ssh "Ich glaube, wir haben ein Gästezimmer, aber ich bin mir nicht sicher, ob wir zwei haben. Ich sehe nach."


show misha sign_smile_cas onlayer master
with charachange

mi "Hm~, es ist aber kein Problem, Hicchan~! Shicchan und ich können uns ein Zimmer teilen, wenn wir müssen. Na ja~, außer es wird gerade für etwas anderes benutzt."


hide shizu onlayer master
with charaexit

hide misha onlayer master
with charaexit

stop music fadeout 5.0

"„Nicht sicher?” Ich fange an zu glauben, dass Shizune nicht viel Zeit zu Hause verbringt. Bevor ich auf ihre Kosten Witze machen kann, verschwindet Shizune gefolgt von Misha im Haus und lässt mich allein zurück."


"Ich will ihnen noch nicht hinein folgen. Ich lege meine Tasche vor der Haustür ab und nutze die Gelegenheit, um mich in einer kurzen Runde um das Haus auf dem Gelände umzusehen."


show hideaki bored onlayer master at center
with shorttimeskip

"Auch wenn es nur paar Minuten dauert, ist das erste, was ich bemerke, als ich zurückkomme, dass meine Tasche weg ist."
"Stattdessen steht da ein kleines Mädchen. Sie sieht aus wie Shizune, auch wenn Shizune keine roten Shorts und Strümpfe mit Monden und Sternen darauf tragen würde."


hi "Hi! Bist du Shizunes kleine Schwester oder so?"


show hideaki normal onlayer master
with charachange

hh "Nein, ich bin ihr kleiner Bruder. Mein Name ist Hideaki."


show hideaki thinking onlayer master
with charachange

hh "Freut mich, dich kennenzulernen."


play music music_happiness fadein 2.0

"Die Stimme, die darauf antwortet, ist direkt, monoton, und definitiv männlich. Es ist mir so peinlich, dass ich kurz davor bin, mich umzudrehen und zu gehen, aber ich kann mich nicht an den Rückweg zum Zug erinnern."


show hideaki serious onlayer master
with charachange

hh "Bist du die zweite Person, die meine Schwester mitgebracht hat?"


hi "„Mitgebracht hat”? Ich bin kein Gepäck."


hi "Wie auch immer, ich bin Hisao. Hast du meine Tasche genommen?"


show hideaki triangle onlayer master
with charachange

hh "Ja, es ist mein Recht, alles zu behalten, was ich auf meinem Grundstück finde."


hi "Nein, ist es nicht. So läuft das überhaupt nicht."


"Anscheinend glauben auch wohlerzogene kleine Kinder fest an die Regel „Wer's findet darf's behalten.” Auch wenn ich ihn als klein bezeichne – jetzt, wo ich darüber nachdenke, scheint er nicht viel jünger zu sein, höchstens zwei oder drei Jahre."


show hideaki normal onlayer master
with charachange

hh "Ich hab sie Shizune gegeben. Sie ist drinnen. Bist du im Schülerrat?"


hi "Ja, woher wusstest du das? Erwähnt sie das oft?"


"Fast hätte ich gefragt: „Spricht sie oft darüber?”. Das hätte schlecht ausgehen können."


show hideaki bored onlayer master
with charachange

hh "Ja, die ganze Zeit. Verstehst du dich mit ihr?"


hi "Mit ihr verstehen? Das ist eine komische Frage. Ich wäre nicht im Schülerrat, wenn ich mich nicht mit ihr verstehen würde. Was ist mit dir? Versteht ihr beide euch gut?"


"Auch wenn er eine monotone Stimme hat, sein Gesicht ist so ausdrucksstark wie Shizunes und offenbart, wie er sich wirklich fühlt. Es muss in der Familie liegen. Sieht aus, als wäre er über meine Frage nicht erfreut, aus welchem Grund auch immer."


show hideaki thinking onlayer master
with charachange

hh "Es tut mir leid. Ich habe nur gefragt, weil ihr euch so ähnlich seid."


"Ich weiß nicht warum, aber es fühlt sich an, als ob er mich ärgern will. Leider klappt es. Es gefällt mir nicht, mit Shizune verglichen zu werden."


hi "Du bist ihr viel ähnlicher, aber das ist zu erwarten. Ich hab dich sogar für ihre kleine Schwester gehalten. Wenn du nicht willst, dass Leute diesen Fehler machen, solltest du dich passender anziehen."


show hideaki confused onlayer master
with charachange

hh "Ich verstehe nicht ganz, meine Anziehsachen passen doch super zur Jahreszeit."


hi "Was ist mit den Strümpfen?"


show hideaki angry_up onlayer master
with charachange

hh "Sie sind cool."


show hideaki disapproves onlayer master
with charachange

hh "Du verhältst dich wie meine Schwester. Irgendwann werden die Leute anfangen, dich mit ihr zu verwechseln."


"Ich schätze, mein Kommentar hat ihn härter getroffen als ich dachte. Das würde diesen Konterversuch erklären."


hi "Ich hasse es, mit anderen Leuten verglichen zu werden."


show hideaki evil onlayer master
with charachange

hh "Shizune mag es ebenfalls nicht, wenn sie mit anderen verglichen wird."


"Ich dachte, dass Hideaki etwas reifer als Shizune wäre, aber sie haben den gleichen Wettbewerbsdrang und die Neigung, andere zu provozieren. Ich frage mich, ob er ihretwegen so ist, oder andersherum."


hi "Und du auch nicht, stimmt's? Okay, ich hab's verstanden. Ich sollte nicht so kleinlich sein."


show hideaki normal onlayer master
with charachange

stop music fadeout 4.0

"Besonders zu kleinen Kindern. Hideaki scheint das als Anerkennung einer Niederlage aufzufassen, was ich ihm nicht durchgehen lassen will. Dennoch muss ich es einfach ruhen lassen, solange ich die Chance dazu habe."


scene bg shizu_living onlayer master
with locationchange

"In dem Augenblick, in dem ich durch die Tür schreite, kann ich Mishas Gelächter durch den Flur hallen hören. Ich schließe daraus, dass sie gerade im Wohnzimmer ist. Hier sind mehr Leute, als ich erwartet hätte."


show lilly basic_displeased_cas onlayer master:
    center
    ypos 1.17 xpos 0.55
show akira basic_boo onlayer master:
    tworight
    ypos 1.15 xpos 0.72
show hideaki bored onlayer master:
    center
    xpos 0.92
    easein 1.0 ypos 1.1
show shizu behind_blank_cas onlayer master:
    twoleft
    ypos 1.11 xpos 0.27
show misha perky_smile_cas onlayer master:
    center
    ypos 1.1 xpos 0.08
with charaenter

play music music_another fadein 4.0

"Unter ihnen entdecke ich einen einzigartigen und vertrauten, blonden Pferdeschwanz. Ich bin eher verwirrt als überrascht, dass Lilly hier ist. Shizune wirkt genauso überrascht, und Lilly scheint ebenfalls nicht begeistert über die Begegnung zu sein."


"Neben Lilly sitzt eine große, androgyn aussehende Frau in einem stilvollen Anzug. Ich würde gerne davon ausgehen, dass es ihre ältere Schwester ist, aber ich will es nicht riskieren."


show lilly basic_listen_cas onlayer master
with charachange

li "Ich hatte nicht erwartet, dass ihr so früh ankommt."


"Zuerst dachte ich, dass sie mit mir redet. Doch es stellt sich heraus, dass es an Shizune gerichtet war."
"Ich glaube, dass Lilly meine Anwesenheit überhaupt nicht wahrnimmt. Ich bin mitten in ihr Gespräch gelaufen, aber es scheint so, als hätte sie mich noch nicht bemerkt, weil sie auf Shizune konzentriert ist."


show shizu basic_frown_cas onlayer master
with charachange

ssh "Ich hätte meinen ganzen Zeitplan deinetwegen neu ordnen sollen."


show misha sign_smile_cas onlayer master
with charachange

mi "Shicchan sagt: Ich hätte nur deinetwegen meinen Zeitplan neu anordnen sollen~!"


show lilly basic_displeased_cas onlayer master
with charachange

li "Das wäre schön gewesen, aber ich würde so etwas von dir nicht erwarten."


show misha hips_smile_cas onlayer master
with charachange

mi "Oh, hi Hicchan~! Da bist du ja endlich."


hi "Ja. Hallo, Lilly."


show lilly basic_surprised_cas onlayer master
with charachange

li "Oh, Hisao? Das ist eine ziemliche Überraschung. Akira, das ist Hisao, ein Schulkamerad. Hisao, das ist Akira, meine Schwester."


show akira basic_smile onlayer master
with charachange

aki "Yo."


"Sie hält ihre Hand in einer kurzen und sehr lässigen Begrüßungsgeste hoch. Also ist sie wirklich die große Schwester."


show akira basic_boo onlayer master
show lilly basic_weaksmile_cas onlayer master
with charachange

aki "Hoffentlich werfen wir eure Pläne nicht über'n Haufen. Da wir nur für einen weiteren Tag hierbleiben werden, dachten Lilly und ich, dass sie genauso gut mit mir kommen kann."


"Akira wendet sich zu mir, als ob sie sich zu einer Erklärung genötigt fühlt. Ich bin sehr dankbar dafür."


show akira basic_ending onlayer master
with charachange

aki "Ich vermute, dass sich meine Stellung hier am besten als Babysitter beschreiben lässt."


show hideaki disapproves onlayer master
with charachange

"Akira durchwuschelt Hidaekis Haare, während er seinem Hobby nachgeht – verärgert dreinschauen."


hh "Das ist erniedrigend."


show akira basic_smile onlayer master
with charachange

aki "Wirklich? Vielleicht ändere ich meinen Titel, wenn du ein paar Jahre mehr auf dem Buckel hast. Oder wenigstens ein paar Zentimeter."


"Sie stellen ein interessantes Paar dar, obwohl Akira mehr wie ein Rechtsanwalt als ein Babysitter aussieht. Ich bin mir aber immer noch nicht wirklich sicher, warum sie und Lilly hier sind."


"Bei einem Rundblick im Zimmer sehe ich hier und dort einige Tennisschläger, Golfschläger und sogar einen Stapel Angelruten samt Zubehör."


"Hinter jedem Stuhl, in jeder Ecke und unter jedem Tisch hier ist eine Art Outdoor-Hobbyutensil. Ich greife mir eine der Angelruten und spiele damit."


hi "Das ist ein schönes Haus."


hi "Shizune, es sieht so aus, als hätte dein Vater eine Menge Hobbys."


show misha sign_smile_cas onlayer master
with charachange

show misha perky_smile_cas onlayer master
with charachange

"Für einen Moment vergesse ich zu gebärden, doch Misha ist bereits dabei zu übersetzen, was ich gesagt habe. Ich bin immer noch ein wenig beeindruckt, wie automatisch das Übersetzen für Misha ist."


show hideaki normal onlayer master
with charachange

hh "Angelst du?"


hi "Nein, ich weiß nicht, wie das geht. Aber ich würde es gerne lernen. Ich hab gehört, dass es entspannend ist."


show shizu behind_blank_cas onlayer master
with charachange

ssh "Es gibt einen Fluss nicht weit von hier. Meine ganze Familie weiß, wie man angelt. Wenn du möchtest, könnten wir mal dort hinfahren."


show akira basic_laugh onlayer master
with charachange

aki "Du und Hidaeki, ihr angelt? Ich hatte nicht damit gerechnet, dass Leute in eurem Alter das können. Ich dachte immer, das wäre ein Hobby für alte Leute."


show akira basic_ending onlayer master
with charachange

aki "Weißte, Lilly kann super kochen. Wenn wir frischen Fisch hätten…"


"Es ist nicht schwer, Akiras Gedanken zu folgen."


show lilly basic_displeased_cas onlayer master
with charachange

li "Wenn ihr Fisch essen wollt, können wir zum Supermarkt gehen."


"Lillys Stimme klingt etwas autoritärer als sonst. Sie scheint den Enthusiasmus ihrer Schwester für diese Idee nicht wirklich zu teilen."


show shizu basic_happy_cas onlayer master
with charachange

shi "…"


show misha hips_grin_cas onlayer master
with charachange

mi "Es macht mehr Spaß angeln zu gehen; wir könnten sogar ein Spiel daraus machen, um zu sehen, wer den größten fängt. Das wäre spannend, oder? Ja~! Hicchan, was denkst du? Es klingt nach Spaß, nicht wahr?"


hi "Ja, das könnte es auf jeden Fall sein."


show akira basic_smile onlayer master
with charachange

aki "Klingt nach einem Plan. Ich weiß auch nicht, wie man angelt, daher wäre jetzt ein guter Zeitpunkt, es zu lernen."


show akira basic_boo onlayer master
with charachange

"Ihr Blick richtet sich auf Lilly, die nach wie vor unbeeindruckt bleibt. Das schmälert Akiras Lächeln etwas und ich frage mich, warum Lilly so dickköpfig deswegen ist."


show hideaki normal onlayer master
with charachange

hh "Ich glaube nicht, dass wir genug Angelausrüstungen für alle haben."


show shizu behind_smile_cas onlayer master
with charachange

ssh "Wir können uns abwechseln. Es wird ein Team-Match."


show hideaki confused onlayer master
with charachange

hh "Was sagt sie?"


hi "Wir können uns abwechseln. Sie will auch daraus einen Wettkampf machen."


show akira basic_laugh onlayer master
with charachange

aki "Komm schon, Lilly, wir können genauso gut das Beste daraus machen."


show akira basic_boo onlayer master
with charachange

aki "Also geht es bei dem Wettbewerb darum, zu sehen, wer den größten oder die meisten Fische fängt?"


show shizu adjust_smug_cas onlayer master
with charachange

ssh "Sieht so aus, als würde die ältere Schwester es besser verstehen, wie immer."


show shizu basic_normal_cas onlayer master
with charachange

shi "…"


show misha sign_smile_cas onlayer master
with charachange

mi "Shicchan sagt, dass sie vermutet, dass Lilly lieber zum Supermarkt gehen würde, richtig~? Es ist viel weniger Arbeit, natürlich würde sie das! Trotzdem würde Fischen gehen mehr Spaß machen und Geld sparen. Akira, du hast den Durchblick~!"


show akira basic_smile onlayer master
with charachange

"Akira lächelt freundlich, wenn auch etwas gekünstelt. Shizunes Lob war ja nicht ihr Ziel."


show lilly basic_sleepy_cas onlayer master
with charachange

li "…"


show lilly basic_weaksmile_cas onlayer master
with charachange

li "Ist der Fluss nicht ziemlich weit weg?"


show akira basic_ending onlayer master
with charachange

aki "Ich denke nicht, dass es so weit ist. Wenn es nötig ist, kann ich fahren. Solange ihr etwas fangt, habe ich kein Problem damit."


hi "Passen so viele Leute und diese Menge an Angelausrüstungen überhaupt in deinen Wagen?"


show akira basic_boo onlayer master
with charachange

"Sie spitzt ihre Lippen, während sie mit subtilen Fingerbewegungen die Anzahl der Passagiere und der benötigten Ausrüstungen abzählt. Wenn wir mich, Shizune, Misha, Lilly, Akira und Hideaki mitnehmen…"


show akira basic_lost onlayer master
with charachange

aki "Sechs Personen. Verdammt, in mein Auto passen nur fünf."


show akira basic_ending onlayer master
with charachange

aki "Hmm, wenn Hidaeki sich auf meinen Schoß setzt, könnten wir…"


show hideaki angry_up onlayer master
with charachange

hh "Ich werde mich nicht auf deinen Schoß setzen."


show akira basic_resigned onlayer master
with charachange

aki "Och."


show shizu adjust_happy_cas onlayer master
with charachange

shi "…"


show misha hips_smile_cas onlayer master
with charachange

mi "Shicchan sagt, dass das Auto ihres Vaters groß genug wäre."


show akira basic_lost onlayer master
with charachange

aki "Was, der Fuga? Wenn er nichts dagegen hat, dass wir ihn benutzen, haben wir wohl keine andere Wahl. Schade, dass ich meinen Wagen im Stich lassen muss… Ich habe ihn ja nicht mehr sehr lange."


"Trotz Lillys Sturheit und Hideakis Fragen, ob wir nicht lieber vorher etwas essen, bevor wir auf ein Fischgericht setzen, dass eventuell niemals zustande kommt, gibt es keine Möglichkeit, Akira und Shizune von ihrem Plan abzubringen."


stop music fadeout 5.0

scene ev shizune_car onlayer master
with shorttimeskip

play ambient sfx_businterior fadein 1.0

"Meine Erwartungen an eine einigermaßen entspannte Fahrt durch die Landschaft werden erfüllt. Akiras Fahrstil ist so sanft und friedlich wie die Umgebung, bis sogar Misha einschläft."


"Ich dachte, dass dieser Ausflug eher zu gemütlich für Shizunes Geschmack sein würde, doch sie scheint es aufrichtig zu genießen. Obwohl Hideaki unbeholfen zwischen ihr und der Tür gequetscht sitzt, sieht sie einfach nur aus dem Fenster und lächelt."


stop ambient fadeout 0.5

scene bg shizu_fishing onlayer master at left
with shorttimeskip

play ambient sfx_parkambience fadein 0.5

"Die Gegend um den Fluss ist ziemlich schön. Akira und Shizune machen sich so schnell auf zum Fluss, dass wir keine andere Wahl haben, als ihnen hinterherzuhetzen. Ansonsten würden sie uns zurücklassen."


show lilly basic_weaksmile_cas onlayer master at left
show hideaki bored onlayer master at center
show misha hips_grin_cas onlayer master at right
with charaenter

"Es ist offensichtlich, dass Hideaki und Lilly nur wegen ihrer Geschwister mitgekommen sind, wobei Lilly die Lustlosere der beiden ist."
"Misha jedoch scheint so fröhlich wie eh und je. Es sieht so aus, als ob Shizunes und Akiras Begeisterung auf sie abgefärbt hätte."


"Ich selbst würde lieber jetzt essen, aber der Gedanke an von Lilly zubereiteten, frischen Fisch ist verlockend."


"Der Fluss ist größer, als ich ihn mir vorgestellt hatte, wenn auch sehr malerisch und friedlich. Außer einem kleinen Pier, der scheinbar nur zum Angeln gebaut wurde, sieht dieser Ort unberührt von jeglicher Zivilisation aus."
"Es macht mir bewusst, wie viel Vegetation ich in letzter Zeit gesehen habe."


show shizu invis onlayer master at offscreenright
show akira invis onlayer master:
    center
    xpos 1.5
with None

show bg shizu_fishing onlayer master at right
show lilly invis onlayer master at Position(xpos=-0.6)
show hideaki invis onlayer master at offscreenleft
show misha perky_confused_cas onlayer master at left
show shizu basic_happy_cas onlayer master:
    center
    xpos 0.37
show akira basic_smile onlayer master:
    center
    xpos 0.8
with Dissolvemove(1.5)

"Shizune zerrt Misha weg, sodass sie Akira erklären können, wie man angelt. Lilly und Hideaki unterhalten sich miteinander, also beschließe ich, mich dem enthusiastischen Trio anzuschließen."


show akira basic_ending onlayer master
with charachange

aki "Hmm… Also welchen dieser Köder sollte ich dann benutzen? Kann ich diesen süßen, kleinen nehmen?"


show shizu basic_frown_cas onlayer master
show misha sign_smile_cas onlayer master
with charachange

mi "Wartet, wartet~! Das ist ein Wettkampf, also müssen wir zuerst Teams einteilen! Shicchan und ich sind natürlich in einem. Hicchan, du bist auch in unserem Team, oder? Wir können das Schülerrat-Team sein~!"


hi "Okay."


show akira basic_laugh onlayer master
with charachange

aki "Geht klar. Das macht mich, Hideaki und Lilly zum anderen Team. Lilly, wie sollen wir uns nennen?"


stop music fadeout 2.0

play sound sfx_flash

show bg shizu_fishing onlayer master at left
show lilly basic_sleepy_cas onlayer master at twoleft
show hideaki bored onlayer master at tworight
show misha invis onlayer master at Position(xpos=0.85)
show shizu invis onlayer master at offscreenright
show akira invis onlayer master:
    center
    xpos 1.5
with Dissolvemove(0.5)

$ doublespeak (li, hh, u"Ich wüsste nicht, warum das wichtig sein soll.", u"Ich glaube nicht, dass das wichtig ist.")


play sound sfx_flash

show bg shizu_fishing onlayer master at right
show lilly invis onlayer master at Position(xpos=-0.6)
show hideaki invis onlayer master at offscreenleft
show misha perky_confused_cas onlayer master at left
show shizu basic_angry_cas onlayer master:
    center
    xpos 0.37
show akira basic_ending onlayer master:
    center
    xpos 0.8
with Dissolvemove(0.5)

show akira basic_lost onlayer master
with charachange

aki "Dann wohl Team-Lustlos…"


play music music_comedy fadein 0.5

"Und mal wieder werden Akiras größte Bemühungen zurückgewiesen. Shizune und Misha wiederum mangelt es überhaupt nicht an Begeisterung."


show misha hips_smile_cas onlayer master
show shizu behind_frown_cas onlayer master
with charachange

ssh "Hisao! Du kannst als erster drankommen. Bitte gib dir Mühe und fang so viele oder so große Fische wie möglich."


hi "Warum gerade ich? Mir hat noch nicht einmal jemand beigebracht, wie man angelt."


show misha hips_grin_cas onlayer master
show shizu behind_blank_cas onlayer master
with charachange

mi "Das können wir jetzt tun~."


"Nach einer kurzen Einweisung versucht Shizune, uns sofort in eine Diskussion über die Strategie in einem Tag-Team Angelwettbewerb zu ziehen."


"Irgendwie passt „Wettbewerb” nicht zu wirklich zu einem Sport, bei dem man Stunden mit Sitzen verbringt und hofft, dass ein Fisch anbeißt."


show shizu adjust_happy_cas onlayer master
with charachange

ssh "Sieht so aus, als ob sich Hideaki mit der Ersatzrute begnügen muss. Du weißt, dass es nur ein Bambusstock mit einem Faden dran ist, oder? Das bedeutet, wenn wir die Reihenfolge beschließen, solltest du gegen ihn antreten."


hi "Was? Warum ich?"


show misha sign_smile_cas onlayer master
with charachange

mi "Du hast am wenigsten Erfahrung, Hicchan~."


hi "Ach ja? Wer ist dann der Beste hier? Shizune? Hideaki ist dein Bruder, er ist wahrscheinlich genauso gut. Wahrscheinlich angelt er die ganze Zeit, weil er näher an einem See lebt. Er könnte sogar besser sein."


show akira basic_annoyed onlayer master
with charachange

aki "Euch drei zu sehen bereitet mir Kopfschmerzen. Ihr wisst, dass ich nur zwei Drittel eurer Unterhaltung höre, oder? Worum geht's?"


hi "Auswahl der Reihenfolge."


"Akira macht ein beunruhigtes Gesicht. Sie wird ungeduldig, was irgendwie verständlich ist."


show shizu basic_sparkle_cas onlayer master
with charachange

ssh "Wenn du ungeduldig bist, macht es das nur noch aufregender. Jetzt will ich um höhere Einsätze spielen."


show akira basic_lost onlayer master
with charachange

aki "Was sagt sie?"


hi "Sie will um höhere Einsätze spielen."


show akira basic_laugh onlayer master
with charachange

aki "Ich wäre nicht zu voreilig; wir haben immerhin doppeltes Anfängerglück auf unserer Seite. Ihr könnt das nur schlagen, indem ihr einen ganzen Ozean fangt."


show shizu adjust_happy_cas onlayer master
with charachange

shi "…"


show misha hips_grin_cas onlayer master
with charachange

mi "Das ist Süßwasser, du Meeresbiologin~."


"Eine seltsame Beleidigung, ausgeteilt mit unerschrockener und unschuldiger guter Laune. Akira scheint es nicht zu stören. Sie lacht darüber, und Shizune scheint wieder wie ihr übliches neckisches Selbst. Ich bin froh, dass sie miteinander auskommen."


show akira basic_smile onlayer master
with charachange

aki "Also, fangen wir an, die Teams auszusuchen oder was? Ich werde langsam hungrig…"


show shizu basic_normal_cas onlayer master
with charachange

ssh "Hisao, Misha und ich sind ein Team, und Lilly, Hideaki und du seid das Andere, nicht wahr?"


show akira basic_ending onlayer master
with charachange

aki "Ich schätze, das ist die naheliegenste Aufteilung. Trotzdem – wäre es nicht etwas lustiger, wenn wir sie mischen würden? Hm?"


show misha perky_smile_cas onlayer master
with charachange

mi "Hmm~, du willst nicht mit deiner eigenen Schwester angeln?"


show akira basic_boo onlayer master
with charachange

aki "Na ja, keiner von uns weiß, wie man angelt. Uns beide in ein Team zu stecken wäre also irgendwie…"


"Nun, das klingt, als hätte ich gerade etwas Gefährliches gehört. Bevor Shizune mehr als nur einen ungläubigen Blick aufsetzen kann, versuche ich das Thema zu wechseln."


hi "Also… Ich nehme an, du und Shizune, ihr kennt euch?"


show akira basic_smile onlayer master
with charachange

aki "Sicher tun wir das. Schon sehr lange."


show shizu basic_normal2_cas onlayer master
with charachange

"Akira wirft Shizune ein wissendes Grinsen zu. Erst als Misha mit der Übersetzung des Gesagten fertig ist, zieht Shizune ein bekümmertes Gesicht."


"Akira ist gewiss anders als Lilly. Abgesehen von ihrem Aussehen ist sie viel ungezwungener und lockerer."
"Es ist überraschend, denn von Lillys Familie hätte ich erwartet, dass alle sehr anständig und förmlich sind. Aber ich denke, dass man mit ihr ganz ungezwungen reden kann."


show akira basic_laugh onlayer master
with charachange

aki "So gerne ich mich auch übers Fischfangen unterhalte, wir sollten vielleicht irgendwann mal damit anfangen."


show shizu behind_blank_cas onlayer master
with charachange

ssh "Würdest du vorschlagen, dass es wie beim Baseball eine Aufstellung geben sollte? Oder sollten alle gleichzeitig mitmachen? Oder ein Tag-Team-Kampf?"


show shizu basic_sparkle_cas onlayer master
with charachange

ssh "Kann jeder sitzen wo er will, oder müssen Teams auf einer Stelle bleiben? Bestimmen wir wo wir angeln? Welche Fischgrößen werden gezählt?"


show akira basic_lost onlayer master
with charachange

"Als sie sieht, wie Akira nach Mishas pflichtbewusster Übersetzung stöhnt, reibt sie leise lachend ihre Brillengläser."


show shizu adjust_happy_cas onlayer master
with charachange

stop music fadeout 4.0
ssh "Vergiss es. Lass uns einfach angeln."


show shizu behind_smile_cas onlayer master
with charachange

ssh "Es kann ein Einzelwettkampf sein."


stop ambient fadeout 2.0

scene ev shizu_fishing_ah onlayer master
with shorttimeskip

play music music_ease

"Bereit zum Fischen setze ich mich hin, auch wenn ich nicht wirklich zuversichtlich bin."
"Alle anderen sitzen bereits, außer Akira. Nachdem sie ihre Anzugjacke ausgezogen und ihre Ärmel hochgekrempelt hat, nimmt sie neben mir Platz und wirft ihre Schnur aus."


"Misha und Hideaki sitzen letztendlich am Ufer und angeln gemeinsam, da es auf dem Pier nicht genug Platz für alle gibt. Ehrlich gesagt, würde ich lieber neben Shizune sitzen, aber Akira scheint zugänglich genug."


aki "Vorsicht, du bist etwas zu nah. Verhedder nicht unsere Schnüre, 'kay?"


hi "Du hast also vorher noch nie geangelt?"


aki "Nein, aber ich habe ein wenig im Fernsehen darüber gesehen. Ich wollte schon immer einen von diesen großen Fischen mit dem Schwert als Gesicht fangen. Speerfische, glaube ich."


li "Wenn ich mich richtig erinnere, sind die aus dem Ozean. Es sind Salzwasserfische."


aki "Das weiß ich. Warum tun alle so, als wüsste ich den Unterschied zwischen Süß- und Salzwasser nicht?"


li "Egal ob Salzwasser oder nicht, wenn du nicht aufpasst, wirst du die Fische verscheuchen."


"Zwischen ihren Versuchen, Shizune zu ärgern und Lilly bei Laune zu halten, ist Akiras Stimme etwas laut, also könnte sie Recht haben. Bei mir scheint rein gar nichts anzubeißen, aber ich weiß nicht, in welchem Maße Akira dafür verantwortlich ist."


"Shizune tut ihr Bestes, um sich in der Sonne zu entspannen, und sieht dabei auch sehr überzeugend aus, aber ich kann sehen, dass sie ein wenig genervt davon ist, nicht zu wissen, worüber geredet wird."
"Es kann ein echtes Problem sein, Misha nicht in der Nähe zu haben."


ssh "Hisao, was sagt der Spielstand? Sind wir am gewinnen? Das hoffe ich doch, immerhin habe ich unseren Sieg in deine Hände gelegt."


"Ich habe es geschafft, mit kreativen und unbeholfenen Angelrutenbewegungen etwas einigermaßen zu gebärden. In gesprochener Sprache würde es wahrscheinlich an Kauderwelsch grenzen."


hi "Du bist doch genau da. Siehst du es nicht?"


ssh "Enttäuschend; du lässt dich ablenken. Du musst konzentriert bleiben."


hi "Hätte ich wissen müssen. Nun, es steht auf jeden Fall null zu null."


"Akira schmunzelt, obwohl es deutlich ist, dass ihr das regelrecht den Wind aus den Segeln genommen hat."


hi "Es sind nur Zahlen, weißt du. Oder zählt die Größe auch?"


ssh "Beides; Einstufung zählt."


hi "Wer wird sie denn bewerten? Bist du ein zertifizierter Fisch-Richter?"


"Shizune schüttelt den Kopf, um zu sagen, dass sie es nicht ist."


ssh "… Aber es scheint nicht allzu schwierig zu sein. Sag Misha, dass sie aufhören soll, so mit ihren Händen zu fuchteln. Es verscheucht die ganzen Fische. Und frag Hideaki, warum er noch nicht einmal seine Schnur ausgeworfen hat."


"Ich wende mich den beiden zu und rufe ihnen Shizunes Anliegen zu."


mi "Shicchan, ich glaube, er ist sauer, weil er die Ersatzrute bekommen hat~!"


"Da Misha gerade größtenteils unfähig ist, etwas zu gebärden, bekommt sie von Shizune nur einen verwirrten Blick. Nachdem ich übersetzt habe, seufzt sie nur."


aki "Hey, auch wenn es dir nicht gefällt, musst du es versuchen. Du weißt nie, ob du nicht vielleicht den ganz Großen fängst. Aber du wirst nichts fangen, bis du es versuchst!"


"Ich habe das Gefühl, dass die Hälfte ihrer Ermutigung daher kommt, dass wenn Hideaki „den ganz Großen” fängt, sie ihn mitessen will. Sechs Leute, die angeln, haben bessere Chancen etwas zu fangen als fünf."


"Da ich ständig umständlich mit der Angel hantieren muss, um mit Shizune zu kommunizieren – nicht zu vergessen, dass sie immer unruhiger wird – denke ich, es wäre eine gute Idee, ihr eine Gelegenheit zum Angeln zu geben."


hi "Hey Leute, können wir jetzt tauschen?"


aki "Klar. Lilly?"


li "Nein, nein, bitte nicht. Ich weiß nicht, wie man angelt."


"Angesichts der Tatsache, dass ich anscheinend Mishas Platz als Shizunes Übersetzer eingenommen habe, gebärde ich, was sie sagen."


ssh "Wie großzügig von dir, Lilly."


"Oh Mann, und los geht's. Aus Angst, einen weiteren Streit zu fördern, denke ich nicht einmal daran, das Gesagte zu übersetzen."


hi "Shizune sagt, du solltest es zumindest ausprobieren. Vielleicht macht es dir sogar Spaß."


li "Na schön. Akira, wie benutzt man das?"


aki "Es ist ganz einfach…"


"Ich frage mich, wie ethisch es ist, Shizunes Worte komplett zu verändern. Immerhin hat es sich gelohnt."


scene ev shizu_fishing_sl onlayer master
with shorttimeskip

li "… Ich denke, ich verstehe. Welche Köder glaubst du wären am besten geeignet? Ich würde etwas bevorzugen, das den Fisch nicht allzu sehr verletzt."


aki "Wenn du ihnen einen Haken durch den Mund rammst, glaube ich nicht, dass der Köder sehr viel mehr wehtun wird."


hi "Und ihn freilassen…? Nein, nein. Tu das nicht."


li "Aber wenn er nicht groß ist, ist es sinnlos, ihn zu töten…"


"Mit freien Händen ist es viel einfacher für mich, zu übersetzen, was die anderen sagen. Jetzt ist Shizune diejenige, die mit vollen Händen zu kämpfen hat, aber das scheint ihr nichts auszumachen."


ssh "Das ist so arrogant. Okay, ich werde von nun an auch nur die großen an Land ziehen."


aki "Was sagt sie?"


"Nachdem ich übersetze, seufzt Akira nur."


aki "Nein, dieses „nur” gefällt mir nicht. Ein Fisch ist ein Fisch, weißt du, und du musst nehmen, was du kriegen kannst."


"Leider kann Shizune sie nicht hören und Lilly scheint gerade nicht sehr aufmerksam zu sein."


"Lilly begreift das Angeln schnell; immerhin ist es eine sehr entspannte Beschäftigung. Nach kurzer Zeit fangen sie beide ihren ersten Fisch, und überraschenderweise ist Lilly genauso interessiert daran, welcher der größere ist wie Shizune."


stop music fadeout 3.0

"Während die Stunden vergehen, scheint es, als ob sie sogar langsam Spaß daran finden."


scene bg shizu_fishing_ss onlayer master
with shorttimeskip

play ambient sfx_parkambience fadein 4.0
play music music_tranquil fadein 3.0

"Am Ende des Tages haben wir mehrere ziemlich große Fische beisammen. Selbst Hideaki und Misha haben es geschafft, einen zu fangen."
"Keiner erwähnt, dass wir einen Wettkampf darum hatten, wer mehr fangen würde. Ich denke, es spielt für keinen mehr eine Rolle."


show akira basic_smile_ss onlayer master at center
with charaenter

"Shizune und Misha unterhalten sich etwas weiter weg miteinander. Lilly und Hideaki tun das Gleiche. Ich entschließe mich, diesen ruhigen Moment auszunutzen, um mit Akira zu reden."


hi "Lilly und Shizune haben sich heute gut vertragen. So wie sie in der Schule miteinander umgehen, hatte ich das nicht wirklich erwartet."


show akira basic_boo_ss onlayer master
with charachange

"Sie schnaubt amüsiert. Es sieht so aus, als ob sie ihre Fehden nicht so ernst nimmt wie ich."


aki "Sie haben ihre Gründe. Lilly und ich werden Morgen eine Zeit lang wegfahren, also dachten wir, wir schauen einfach mal vorbei."


show akira basic_ending_ss onlayer master
with charachange

aki "Letztendlich bin ich froh, dass wir gekommen sind."


"Nach einer kurzen Stille streckt sie sich lautstark und klatscht in die Hände, um die Aufmerksamkeit der anderen zu bekommen."


show akira basic_smile_ss onlayer master
with charachange

aki "Also gut, sieht aus, als hätten wir genug, um alle Mäuler zu stopfen. Wir sollten uns jetzt auf den Rückweg machen."


show bg shizu_fishing_ss onlayer master at bgright
show akira basic_smile_ss onlayer master at tworight
with charamove

show lilly basic_weaksmile_cas_ss onlayer master at twoleft
with charaenter

"Lilly nickt, doch dann zögert sie. Auch wenn ihr Gesicht noch etwas düster ist, scheint sie immer noch bessere Laune zu haben als heute morgen."
"Akira scheint wirklich zu wissen, wie man mit ihr umgeht, und hat ihre Abneigung gegenüber Shizune ziemlich gut im Griff."


show akira basic_ending_ss onlayer master
with charachange

aki "Der heutige Fang sieht lecker aus. Ich wünschte, ich hätte etwas Sojasoße, um einfach sofort losessen zu können."


show lilly basic_surprised_cas_ss onlayer master
with charachange

li "Ich dachte, du wolltest, dass ich sie koche…"


show akira basic_laugh_ss onlayer master
with charachange

aki "Du meinst, es wäre nicht okay, sie roh zu essen?"


"Obwohl Akira protestiert – oder ihre Schwester auf den Arm nimmt; ich kann das nicht unterscheiden – beschließen wir, die Fische zu kochen, bevor wir ihn essen."


stop ambient fadeout 2.0

scene bg shizu_houseext_lights onlayer master
with shorttimeskip

stop music fadeout 3.0

"Es ist schon ziemlich spät geworden, seit wir losgefahren sind, und als wir wieder bei Shizunes Haus ankommen, ist es bereits Zeit fürs Abendessen."


scene black onlayer master
with dissolve



label de_S19:

scene bg shizu_guesthisao onlayer master
with locationchange

play music music_pearly fadein 5.0

"Einige meiner Pillen haben sich über den gesamten Boden meiner Tasche verteilt, aber ich habe das erst einige Minuten bevor ich gestern ins Bett ging bemerkt. Ich habe einige ganze Weile damit verbracht, sie aus meinem Gepäck zusammenzukratzen."


"Da ich mich also erst sehr spät hingelegt habe und dann auch noch Probleme hatte einzuschlafen, wache ich ziemlich spät und mit einer Migräne auf."


scene bg shizu_living onlayer master
show hideaki normal_up onlayer master at center
with locationchange

"Als ich ins Wohnzimmer laufe, beendet Hideaki gerade sein Frühstück. Seine Gabel auf halbem Weg zu seinem Mund, scheint er sich nicht sicher zu sein, ob er weiteressen oder mich begrüßen soll. Vielleicht sollte ich das Zimmer wieder verlassen."


show hideaki triangle onlayer master
with charachange

hh "Guten Morgen."


hi "Morgen."


show hideaki thinking onlayer master
with charachange

hh "Was sollten wir deiner Meinung nach zum Frühstück machen?"


hi "„Wir?” Isst du nicht gerade schon Frühstück?"


show hideaki normal onlayer master
with charachange

hh "Doch. Alle anderen sind schon fertig."


"Trotzdem wiederholt er seine Frage noch einmal. Er versucht nur, nett zu sein. Er hat eine komische Art das zu zeigen, aber ich schätze es nichtsdestotrotz, und ich bin ziemlich hungrig."


"Um die Stille zu unterbrechen, versuche ich, ein Gespräch mit ihm anzufangen, während ich mein Frühstück hole."


hi "Dieser Angelausflug gestern hat Spaß gemacht. Kommen die Hakamichis und Satous öfter so zusammen?"


show hideaki bored onlayer master
with charachange

hh "Nicht wirklich."


hi "Verstehe."


"Nein, tue ich eigentlich nicht. Hideaki macht eine kurze Pause, bevor er sich herablässt, mich etwas mehr einzuweihen."


show hideaki thinking onlayer master
with charachange

hh "Familienprobleme. Unsere Väter sind Schwäger und können sich nicht leiden."


"Das zu hören gibt mir eine Menge zu denken. Ich glaube, ich verstehe nun besser, wie Shizune und Lilly miteinander umgehen. Gleichzeitig sollte ich in Zukunft noch vorsichtiger sein, um da nicht hineingezogen zu werden."


hi "Ah. Familienprobleme können lästig sein."


show hideaki normal onlayer master
with charachange

"Hideaki nickt einfach, als ich mich mit meinem Frühstück an den Tisch setze. Ich wünschte, es wäre ein wenig einfacher, sich mit ihm zu unterhalten."


"Während ich esse, bemerke ich, dass das Haus ungewöhnlich ruhig für einen Ort mit Misha in der Nähe scheint. Falls Shizune und Misha bereits gefrühstückt haben, kann es auch nicht daran liegen, dass sie noch schlafen. Ich frage Hideaki, wo sie sind."


show hideaki bored onlayer master
with charachange

hh "Sie machen einige Besorgungen für unseren Vater. Die örtlichen Geschäftsleute lieben Misha, deshalb hat er darauf bestanden."


hi "Na ja, sie hat eine nette und fröhliche Persönlichkeit. Ich kann verstehen, warum sie das würden. Vielleicht solltest du Unterricht bei ihr nehmen. Du könntest deine Geschäftsbeziehungen erweitern."


show hideaki confused onlayer master
with charachange

hh "Glaubst du wirklich?"


"Er klingt ernst. Ich weiß nicht, welche Art von Geschäftsbeziehung ein kleines Kind brauchen würde. Vielleicht will er den größten Benefiz-Kuchenbasar aller Zeiten veranstalten."


"Es ist eine Schande, dass ich bald wieder von hier wegfahren muss und nicht sehen kann, was er vorhat."


"Ich frage mich, was für ein Mensch Shizunes Vater ist – abgesehen von seinem Outdoor-Faible. Was ich bisher weiß ist, dass er seine Geschäftspartner und die Freunde seiner Tochter um Gefallen bittet."


"Ich nehme an, dass er entweder extrem schüchtern oder extrem faul ist. Vielleicht ist es unfreundlich, sich ein solches Vorurteil zu bilden, aber es würde einen großen Teil von Shizunes Persönlichkeit erklären."


show hideaki triangle onlayer master
with charachange

hh "Willst du irgendwo hingehen?"


hi "Nicht wirklich. Wieso? Willst du?"


show hideaki normal onlayer master
with charachange

hh "Ich dachte, es gäbe einen Ort, an den du hingehen wollen würdest. Willst du dir nicht die Gegend anschauen? Oder in einem bestimmten Restaurant etwas essen?"


hi "Ich weiß nicht. Ich bin noch nie hier gewesen."


show hideaki thinking onlayer master
with charachange

hh "Ach so."


"Ich wollte ihn gerade fragen, wie Shizune war, als sie jünger war. Aber er hat es geschafft, mich mit nur einer Frage davon abzulenken. Dies scheint für uns beide eine schwierige Unterhaltung zu sein."


hi "Du bist heute ziemlich erpicht darauf, es mir recht zu machen. Warum bist du so nett? Zeigst du mir gerade deine geheime nette Seite, jetzt wo deine Schwester nicht in der Nähe ist?"


show hideaki bored onlayer master
with charachange

hh "So was in der Art. Shizune wollte, dass ich dir heute Gesellschaft leiste."


"Ich will ihm keine Umstände bereiten, und er soll das wissen. Aber Hideaki ist genau so dickköpfig wie seine Schwester und hält das für seine Pflicht. Außerdem scheint er aufrichtig zu versuchen, nett zu sein."


"Schnell begreife ich, dass es Hideakis Vorstellung von Spaß ist, Angeln zu gehen, Kameras zu sammeln und esoterische Wortspiele zu machen."
"Angeln macht Spaß, aber ich würde es lieber tun als darüber zu diskutieren. Das gleiche gilt für Kameras; ich würde sie lieber benutzen, anstatt sie zu sammeln."


"Hideaki scheint das auch zu merken."


show hideaki normal_up onlayer master
with charachange

hh "Ist dir langweilig?"


hi "Nein, überhaupt nicht."


"Ich gähne die Worte fast, darum ignoriert Hideaki sie vollkommen."


show hideaki sad onlayer master
with charachange

hh "Dir ist langweilig. Shizune hat gesagt, dass ich unterhaltsam sein soll, und ich glaube, dass ich nicht weiß, wie das geht."


hi "Ich amüsiere mich."


show hideaki serious onlayer master
with charachange

hh "Du klingst nicht amüsiert."


hi "Bin ich aber!"


show hideaki normal onlayer master
with charachange

hh "Warum schreist du? Hoffentlich schreist nicht so viel in Shizunes Gegenwart."


"Es ist schwer zu sagen, ob das ein Scherz war. So oder so bin ich etwas überrascht. Ich versuche, es zu überspielen und das Thema zu wechseln."


hi "Sammelst du nur Kameras oder fotografierst du auch?"


show hideaki bored onlayer master
with charachange

hh "Nicht wirklich. Ansonsten würden hier im Haus mehr Fotos hängen. Was gibt es denn zu fotografieren?"


hi "Ich weiß nicht. Vögel? Architektur? Eines dieser Restaurants, über die du gesprochen hast? Ich dachte, diese Stadt hätte massenhaft cooles Zeug. Wie kannst du an einem Ort leben, wo so viel los ist und nichts unternehmen?"


show hideaki triangle onlayer master
with charachange

hh "Ich dachte, du wüsstest nicht, was man hier unternehmen kann? Auf einmal hast du viele Einfälle und betonst, wie interessant es hier ist. Du bist wie unser Tourismusamt. Willst du dir Vögel oder Gebäude ansehen gehen?"


hi "Okay, okay, kein Grund, so wütend zu werden."


show hideaki normal onlayer master
with charachange

hh "… Ich bin nicht wütend. Ich denke einfach, wenn du so einen starken Drang danach hast, dann sollten wir in einen Vergnügungspark gehen."


hi "Warum?"


show hideaki confused onlayer master
with charachange

hh "Damit du dich amüsieren kannst. Es macht garantiert Spaß."


"Wird er diesen gleichen ausdruckslosen, unamüsierten Gesichtsausdruck haben, während wir Achterbahnen und Freifalltürme fahren? Es würde auf jeden Fall das Spaßlevel verringern. Die Idee überzeugt mich nicht, dass es den Ausflug wert ist."


hi "Ich weiß nicht… Nach allem, was ich so gehört habe, steht man in Vergnügungsparks mehr in Warteschlangen als dass man wirklich etwas unternimmt. Und um die Warteschlangen zu vermeiden, müsste man früher losgehen."


show hideaki normal onlayer master
with charachange

hh "Warst du schon mal in einem?"


hi "Nein, aber so scheint es zu sein."


show hideaki bored onlayer master
with charachange

hh "… Gut. Was ist mit einem normalen Park? Es gibt einen in der Nähe, wo Shizune gerne hingeht. Vielleicht ist sie dort, und ich kann dich bei ihr abladen."


hi "Was meinst du mit „abladen”? Ich bin kein Gepäck."


show hideaki triangle onlayer master
with charachange

hh "Du willst nicht in einen Vergnügungspark. Ich weiß nicht, was ich tun soll."


"Es wirkt, als ob ich seine Gefühle verletzt habe, indem ich mich weigere, mit ihm zu gehen."
"Ich rechtfertige schon innerlich meine Entscheidung: Ich stehe nicht gerne in Schlangen. Es wäre zu sehr wie ein Date. Ich würde lieber mit Shizune gehen. Es wäre zu anstrengend."


hi "Es ist nichts Persönliches. Ich wollte nur irgendwie, dass mir stattdessen Shizune die Stadt zeigt."


stop music fadeout 2.0

"Und ich glaube nicht, dass es eine so gute Idee wäre, in meinem Zustand einen Vergnügungspark zu besuchen."


scene bg shizu_park onlayer master
with locationskip

play music music_soothing fadein 0.5

"Der Park ist nah genug, dass ihr Grundstück beinahe als eine Erweiterung davon bezeichnet werden könnte. Er und Shizunes Hinterhof sehen ungefähr gleich aus, außer dass der Park mehr Bänke und mehr Menschen hat."


"Das heißt, er ist ziemlich schön. Dort sind sogar Leute, die mit ihren Hunden Gassi gehen, und Kinder, die ihre Drachen steigen lassen, die man über den entfernten Bäumen gemächlich hin und her fliegen sehen kann."
"Ich könnte ewig hier sitzen bleiben und mich an so einem malerischen Ort entspannen."


show hideaki bored onlayer master at center
with charaenter

"Hideaki wiederum sieht extrem gelangweilt aus. Ich will ihn anstupsen, um zu sehen, ob er noch am Leben ist. Aber würde er überhaupt reagieren?"


hi "Ist dir langweilig?"


show hideaki normal onlayer master
with charachange

hh "Nein. Wirst du auch wie alle anderen joggen oder Frisbee mit Hunden spielen? Macht man so was in Parks?"


hi "Na ja, man geht in Parks, um zur Natur zurückzukommen und die Atmosphäre zu genießen. Deswegen joggt man im Park anstatt auf einem Bürgersteig oder so. Man kann überall joggen."


hi "Ich kann nicht fassen, dass ich diese Unterhaltung führe. Wie kannst du das nicht wissen? Diese Frage war einfach bizarr. Kennst du nicht die Redewendung „Kinder sollte man sehen, nicht hören?”"


show hideaki bored onlayer master
with charachange

hh "Doch."


show hideaki triangle onlayer master
with charachange

hh "Ich habe gelogen. Mir ist langweilig. Möchtest du ein Spiel spielen?"


"Ich seufze laut, in der Hoffnung, dass er versteht, dass ich das nicht will. Ihn kümmert es nicht. Es spielt sogar schon mit einem Spielkartendeck herum."


show hideaki serious onlayer master
with charachange

hh "Warum bist du sauer? Deswegen sind wir doch hier."


hi "Ich dachte, wir wären hier, um Shizune zu suchen."


show hideaki happy onlayer master
with charachange

hh "Genau. Deshalb sollten wir ein Spiel spielen. Es ist eine Falle für Shizune. Man kann alles einfangen, einschließlich Menschen."


show hideaki thinking onlayer master
with charachange

hh "Wenn wir gegeneinander im Geiste des Wettbewerbs und auf sportliche Weise konkurrieren, wird sie davon angezogen werden, um den Gewinner herauszufordern."
hh "Wie ein Hai. Dann werde ich sie wie ein Safarijäger besiegen. Danach werde ich ein Foto von der Preisverleihung schießen."


"Haie fordern keine Leute zu Glücksspielen heraus, als ob sie Hütchenspieler wären."


hi "Wo hast du plötzlich diese Kamera her? Trotzdem, nein. Ich spiele schon genug Spiele, wenn ich mit deiner Schwerster zusammen bin."


show hideaki normal onlayer master
with charachange

hh "Nein, komm schon. Es wird lustig. Wir können Schach spielen."


hi "Nein, bitte nicht. Außerdem, im Park Schach zu spielen ist etwas, das alte Leute machen – wie Angeln. Du wirst zu schnell alt werden, wenn du mit dem Alte-Männer-Zeug weitermachst."


show hideaki darkside onlayer master
with charachange

"Hideaki erstarrt, als ob ich plötzlich angefangen hätte, eine andere Sprache zu sprechen."
"Vielleicht habe ich ihn wieder beleidigt. Vielleicht ist er insgeheim 50 Jahre alt und hat sich nur unglaublich gut gehalten. Dass er Shizunes Bruder ist, könnte eine Tarnung sein."


show hideaki disapproves onlayer master
with charachange

hh "Wie wäre es mit Dame oder Go? Backgammon wäre auch in Ordnung, auch wenn ich es nicht mag. Wenn Brettspiele nicht so dein Ding sind, können wir Karten spielen. Alles außer Sevens – das ist was für Weicheier."


show hideaki evil onlayer master
with charachange

hh "Hast du Angst zu verlieren? Wenn du mich besiegst, kriegst du Süßigkeiten von mir."


hi "Hideaki, du bist genau wie Shizune. Ich fange an zu glauben, dass das alles nur ein Vorwand ist, um Spiele zu spielen."


show hideaki thinking onlayer master
with charachange

hh "Nein, das ist nicht wahr."


hi "Ist es doch! Ich wette, dieser Wettbewerbsdrang ist angeboren. Ich verkaufe dich an die Wissenschaft."


show hideaki normal onlayer master
with charachange

hh "Niemand kann einen Menschen besitzen."


hi "Wie wäre es, wenn ich dir stattdessen etwas Zeichensprache beibringe?"


hi "Als mich Shizune fragte, ob ich mitkommen will, haben wir uns ein wenig unterhalten, und es scheint, als ob du und dein Vater keine Zeichensprache benutzt."
hi "Ist nur geraten, aber falls es so ist, könnte ich dir ein wenig beibringen. Ich bin aber kein Meister darin."


hi "Ich denke, dass es sowieso gut für dich sein dürfte, deine Arme mehr zu bewegen."


"Er bewegt seine Arme fast gar nicht. Meistens hängen sie einfach nur schlaff an seinen Seiten. Wie entnervend."


"Es stört mich, dass Shizunes gesamte Familie anscheinend keine Zeichensprache kann."
"Ich frage mich, was sie getan hat, bevor sie Misha getroffen hat. Haben sie einfach Übersetzer für sie engagiert? Hat sie alles auf den Block geschrieben, den sie mit sich herumträgt?"


"Das Zweite ist am wahrscheinlichsten. Oder sie könnte es in ein Handy eintippen."
"Das würde erklären, warum sie den Block so ungern benutzt. So traurig es ist, ich kann irgendwie verstehen, warum Hideaki oder ihr Vater sich nicht die Mühe gemacht haben könnten, Gebärdensprache zu lernen."


"Es war damals wahrscheinlich ein zu großer Aufwand. Es ist sehr leicht, das zu glauben. Von dem, was ich bisher gesehen habe, halten sie es sich nicht gegenseitig vor oder sind davon zu stark betroffen."
"Es könnte auch sein, dass ich mir einfach zu viele Gedanken mache."


hi "Komm schon. Na ja, um ehrlich zu sein, bin ich selbst noch am Lernen. Ich habe all meine Bücher mitgebracht, damit ich dranbleiben kann, weißt du? Aber ich kann dir zumindest das Alphabet beibringen. Es ist ganz einfach. Das hier heißt „Drache”."


"Meine Worte kommen mir gerade selbst ziemlich abgedroschen vor. Sogar noch mehr als Hideaki mich ausdruckslos anstarrt, als wäre ihm das gesamte Konzept des Lernens fremd."


show hideaki bored onlayer master
with charachange

hh "Shizune mochte es auch, hier Drachen steigen zu lassen."


"Das ist sein Versuch, die Unterhaltung zu retten, und ich gehe gern darauf ein."


hi "Erst Angeln und jetzt auch noch Drachen? Gefallen all diese entspannenden Hobbys Shizune wirklich?"


show hideaki thinking onlayer master
with charachange

hh "Kampf-Drachen. Ach ja, wegen Shizune—{w=0.5}{nw}"


stop music fadeout 0.3

show misha cross_grin_cas behind hideaki onlayer master:
    center
    ypos 1.1 alpha 0.0
    linear 0.2 ypos 1.0 alpha 1.0
show hideaki ohshit onlayer master
with vpunch

"Hideaki erstarrt, als Misha hinter ihm auftaucht und ihre Hände über seine Augen legt."


play music music_comedy fadein 0.5
mi "Hallo hallo~! Wer bin ich~?"


"Dabei schien er gerade etwas lockerer zu werden."


hi "Hi, Misha. Ist Shizune bei dir?"


mi "Hicchan, nicht verraten! Nicht die Überraschung ruinieren, okay~?"


show hideaki thinking onlayer master
with charachange

hh "Misha."


show bg shizu_park onlayer master at bgright
show hideaki normal onlayer master at tworight
show misha perky_confused_cas onlayer master at twoleft
with dissolvecharamove

mi "Bingo~! Das ist richtig! Aber~ irgendwie war das zu einfach."


"Ich weiß nicht, was sie mit „irgendwie” meint."


show misha hips_frown_cas onlayer master
with charachange

mi "Zu viele Leute erraten, dass ich es bin! Ich will jemanden überraschen! Ich war mir sicher, dass sich Hideaki hereinlegen lässt. Warum hat es nicht geklappt, hm~?"


show hideaki bored onlayer master
with charachange

hh "Du bist die Einzige, die so etwas tut. Du und Entführer."


show misha cross_laugh_cas onlayer master
with charachange

mi "Wirklich? Wahaha~!"


show hideaki serious onlayer master
with charachange

hh "Warum lachst du?"


show shizu invis onlayer master:
    center
    xpos 0.1
with None

show bg shizu_park onlayer master at left
show misha cross_laugh_cas onlayer master at Position(xpos=0.4)
show hideaki serious onlayer master at Position(xpos=0.8)
show shizu basic_angry_cas onlayer master at Position(xpos=0.2)
with dissolvecharamove

ssh "Machst du Hisao Ärger? Ich dachte, du würdest ihn an einen etwas spannenderen Ort bringen als den Park. Das ist nicht einmal weit weg von zu Hause. Du bist so faul."


show misha hips_frown_cas onlayer master
with charachange

mi "Hideaki, machst du Hicchan Ärger? Du hättest ihn zu einem aufregenderen Ort bringen sollen! Der Park ist zu nah bei eurem Haus. Shicchan sagt, du bist faul~."


show hideaki bored onlayer master
with charachange

hh "Er wollte hierherkommen. Warum bist du so streitlustig?"


show shizu behind_frown_cas onlayer master
with charachange

ssh "Ich muss meinen kleinen Bruder doch im Zaum halten."


show hideaki triangle onlayer master
with charachange

hh "Was sagt sie?"


hi "Du musst im Zaum gehalten werden."


show hideaki serious onlayer master
with charachange

hh "Wirklich…"


"Sie gehen sich ziemlich schnell an die Gurgel. Ich habe gehört, dass Streitigkeiten unter Geschwistern nicht ungewöhnlich sind, und die Tatsache, dass sie sich überhaupt streiten, bedeutet, dass es irgendeine Ebene der Kommunikation geben muss."
"Ist also schön, dass sie miteinander auskommen."


scene bg shizu_houseext onlayer master
with locationskip

stop music fadeout 4.0

"Sie streiten auf dem ganzen Weg nach Hause. Misha übersetzt für Shizune und ich für Hideaki. So sieht es eher aus, als würden Misha und ich streiten – nur nicht so richtig. Niemand könnte Misha zuhören und das glauben."


"Zumindest war der Tag letzten Endes sehr unterhaltsam."


$ suppress_window_after_timeskip = True

scene black onlayer master
with dissolve



label de_S20:

window hide None

scene black onlayer master
with dissolve

show bg shizu_guesthisao onlayer master
with openeye

window show

"Obwohl ich erst seit zwei Tagen hier bin, kommt es mir viel länger vor. Beim Aufwachen fühle ich mich eher kaputt als erholt. Vielleicht weil ich ständig auf Achse war, seit ich ankommen bin."


"Was auch immer der Grund sein mag, es lässt mich jeden Tag ungewöhnlich spät aufstehen. Ich mag es auszuschlafen, aber es könnte lästig werden, falls es zur Gewohnheit werden sollte."


"Ich kann eine tiefe, männliche Stimme im Hintergrund rufen hören. Es muss Shizunes Vater sein. Wenn man die Größe dieses Hauses bedenkt vielleicht auch seine Gläubiger."
"Wahrscheinlich eher das Erstere, da das Geschrei nicht wütend scheint, sondern nur laut."


scene bg shizu_living onlayer master
show hideaki normal onlayer master:
    center
    xpos 0.5
show misha perky_smile_cas onlayer master:
    center
    xpos 0.3
show shizu basic_normal_cas onlayer master:
    center
    xpos 0.08
show jigoro smug onlayer master:
    center
    xpos 0.87
with charaenter

play music music_another fadein 0.5

"Shizune, Misha und Hideaki sitzen im Wohnzimmer und haben ein einseitiges Gespräch mit einem riesigen Bären von einem Mann, der abwechselnd Essen von dem Teller, der auf seinem Bein balanciert, in sich hineinschaufelt und ein Schwert herumschwingt."


"So wie sich Shizune und Hideaki verhalten, hätte ich erwartet, dass ihr Vater ein sehr zurückgehaltener, adretter, möglicherweise androgyner Mensch ist, darum bin ich ziemlich verwundert."
"Ich bin für eine Weile überrascht, bis er anfängt, mit mir zu reden."


show jigoro laugh onlayer master
with charachange

hx_ "Hallo! Du musst Shizunes anderer Gast sein. Hast du dich ordentlich ausgeschlafen? Die Gästezimmer sind etwas spartanisch eingerichtet. Wenn du irgendetwas brauchst, sag es mir einfach."


hi "Vielen Dank. Sie müssen Shizunes Vater sein. Freut mich, Sie kennenzulernen. Ich bin Shizunes Klassenkamerad, Hisao Nakai."


show jigoro neutral onlayer master
with charachange

hx_ "Die Freude ist ganz meinerseits. Ich wollte dich treffen, nachdem ich gehört hatte, dass ich einen zweiten Gast in meinem Haus haben würde."
hx_ "Unerwartet. Man hört so etwas und möchte natürlich sehen, wie dieser Mensch so ist. Möchtest du meine Visitenkarte?"


$ renpy.music.set_volume(0.5, 1.0, channel="music")

show jigorocard onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Er hält für eine Sekunde ein volles Etui hoch, und ich kann sehen, dass sein Name Jigoro ist und seine Bürozeiten von sechs bis acht sind. Da steht auch, dass er ein „Berater” ist."
"Er ist jedenfalls auf alles vorbereitet - trägt sein Kartenetui sogar im eigenen Haus mit sich."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

show jigorocard onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide jigorocard onlayer master
with None

show jigoro smug onlayer master
with charachange

hx "Du kommst gerade richtig, wir wollen gerade ein etwas verspätetes Mittagessen machen. Gut. Du suchst dir einen Platz aus, und ich bringe dir einen Teller. Hoffentlich hast du nichts gegen Bärenleber."


"Ich dachte, dass Bärenleber giftig wäre. Wie dem auch sei, der Gedanke, Bärenleber zu essen, spricht mich nicht an – abgesehen von der Möglichkeit, anderen davon zu erzählen. Ein Versuch würde nicht schaden. Doch Shizunes Vater lacht bloß."


show jigoro laugh onlayer master
with charachange

hx "Ich mache nur Spaß. Obwohl, vielleicht ist es doch keine so schlechte Idee, Bärenleber für euch Kinder zu kochen. Sie wird euch stark machen."


show jigoro neutral onlayer master
with charachange

hx "Es gibt übrigens Omelettes. Ich mache dir sofort eins. Ist es für dich ungewohnt, Mittags Omelettes zu essen?"


show hideaki triangle onlayer master
with charachange

hh "Sehr ungewohnt."


hi "Nein, überhaupt nicht."


hide jigoro onlayer master
with charaexit

"Jigoro verschwindet dorthin, wo die Küche sein muss. Ich bin überrascht, dass er selbst Essen kochen muss, obwohl er in einem solchen Haus wohnt. Vielleicht kocht er, weil es ihm Spaß macht."


show jigoro smug onlayer master:
    center
    xpos 0.87
with shorttimeskip

"Mein Essens ist nach sehr kurzer Zeit fertig. Es riecht wirklich gut."


hx "Bist du im Schülerrat? Wie Shizune? Ist der Schülerrat so beschäftigt, dass Shizune ihre Freunde überall mit hinschleifen muss?"


show shizu behind_blank_cas onlayer master at Position(xpos=0.12)
with charachange

ssh "Manchmal ist ein Urlaub einfach nur ein Urlaub."


hi "Mit dem Teil über den Schülerrat liegen Sie richtig. Jedoch glaube ich, dass wir nur zum Vergnügen hier sind."


show jigoro neutral onlayer master
with charachange

hx "Verstehe. Stimmt das? Als ich jung war, hatten unsere Schülerräte so viel Arbeit, dass sie es sich nicht leisten konnten, in den Urlaub zu fahren."
hx "Es muss schön sein, so viel Freizeit zu haben. Sollte euch genug Zeit geben, um über eure Zukunft nachzudenken."


"Mir gefällt dieser Gesprächsverlauf nicht, und ich beginne, einen Ausweg zu suchen."


hx "Hast du darüber nachgedacht? Darüber, was du einmal tun willst?"


hi "Nein, in letzter Zeit habe ich kaum darüber nachgedacht. Was tun Sie denn, falls ich fragen darf? Es muss etwas ziemlich Cooles sein, wenn Sie sich so ein Haus leisten können."


show jigoro angry onlayer master
with charachange

hx "Warum willst du das wissen? Kinder interessieren sich nicht für Geschäfte. Was haben deine Angelegenheiten mit meinen zu tun? Verdächtig. Bist du irgend so ein Steuereintreiber, Bursche?"


"Ich schätze, dass er ungern etwas gefragt wird."


show misha hips_grin_cas onlayer master
with charachange

mi "Hicchan ist kein Steuereintreiber, glaube ich~. Hicchan, was machen deine Eltern eigentlich? Du hast es uns nie erzählt~!"


hx "Du, sei still. Unterbrich mich nicht. Ich hasse es, unterbrochen zu werden. Unverschämt."


show misha perky_sad_cas onlayer master
with charachange

mi "Ähh~…"


show shizu basic_normal2_cas onlayer master at Position(xpos=0.08)
with charachange

"Shizune scheint nicht sehr glücklich über den Lauf der Dinge zu sein. Auch wenn Misha ihr gerade nicht gebärden kann, was passiert, kann sie die Stimmung leicht lesen. Ihr erboster Blick wir noch sengender, als Jigoro weitere Tiraden loslässt."


hx "Noch etwas. Meine Angelausrüstung. Ich kam nach Hause, und sie lag einfach auf einem großen Haufen in der Ecke. Die Ruten einfach willkürlich auf der Ausrüstung übereinander gestapelt."


show hideaki thinking onlayer master
with charachange

hh "Das war ich."


"Ich weiß nicht mehr, ob es wirklich er war. Falls er es nicht war, rechne ich es ihm hoch an, dass er für uns die Schuld auf sich nimmt. Es ist auch egal, denn Jigoro ignoriert ihn, ohne überhaupt zu reagieren."


show jigoro smug onlayer master
with charachange

hx "Na ja, wie auch immer. Ich bin froh, dass meine Angelausrüstung den Freunden meiner Tochter so viel Spaß bereitet hat. Habt mir nicht einmal gesagt, dass ihr sie benutzen würdet. Das sind teure, handgemachte Ruten. Nichts für Laien."


"Plötzlich bemerke ich die Eierschalen in meinem Omelette. Ist er einfach nur ein schlechter Koch? Isst er sie für das Kalzium? Wurden sie absichtlich hinzugefügt, um es mir noch unangenehmer zu machen?"


"Ich bin zwar verwirrt, aber nicht so entnervt, wie ich es normalerweise wäre. Immerhin ist mein Leben in letzter Zeit ziemlich seltsam gewesen, und ich stoße immer wieder auf alle möglichen komischen Menschen. Mich überrascht gar nichts mehr."


show jigoro angry onlayer master
with charachange

hx "Noch nicht einmal richtig gereinigt nach der Benutzung. Schrecklich."


hx "Wisst ihr überhaupt, wie man angelt? Unwahrscheinlich. Es gibt hier nicht genug Ruten für euch alle. Wie funktioniert das? Habt ihr alle geteilt? Einer befestigt den Köder am Haken und ein anderer wirft? Zwei Leute zum einholen? Unfähig."


hi "Nun, wir waren sechs Personen. Darum konnten wir es nicht alle gleichzeitig tun. Zuerst waren es nur ich, Akira, Hideaki und Misha."


hx "Hör auf zu reden. Das klingt unglaublich schmutzig. Ich habe genug von deinem Dreck. Wie vulgär. Sorg dafür, dass deine Aussagen das nächste Mal nicht so peinlich und achtlos formuliert sind."


hi "Was…?"


hx "„Was?” Du bist so respektlos. Unglaublich. Sind alle Delinquenten so? Selbst die Art, wie du dich kleidest, zeigt, wie respektlos du gegenüber Autorität bist. Pullunder. Erbärmlich…"


hi "Delinquent? Ich bin im Schülerrat."


"Der Kommentar über meinen Pullunder hat mich getroffen, besonders da er von einem Typen in so einem kitschigen Hemd kommt. Aber ich denke, dass ich nicht wirklich etwas sagen kann. Er hat ein Schwert. Vielleicht tötet er auch Bären."


stop music fadeout 0.3
play sound sfx_impact
with vpunch

"Misha stellt den Teller lautstark auf den Tisch."


show misha hips_smile_cas onlayer master
with charachange

mi "Das war köstlich~! Shicchan und ich sind jetzt fertig. Hicchan, du auch oder~? Wir sollten los!"


"Was für eine einfache und doch wirkungsvolle Strategie."


scene bg shizu_houseext onlayer master
with locationchange

"Ich habe kaum die Zeit, meinen Teller hinzustellen, bevor sie mich hochziehen und schließlich nach draußen zerren."


show shizu behind_frustrated_cas onlayer master at tworight
show misha perky_confused_cas onlayer master at twoleft
with charaenter

shi "…"


show misha sign_confused_cas onlayer master
with charachange

mi "Unglaublich~! Als würde ich wirklich einem Verhör zusehen~! Das ist keine Polizeishow! Gäste haben durchaus Verantwortlichkeiten, aber hat er noch nie etwas von Gastfreundschaft gehört? Also wirklich~!"


"Misha versucht so gut sie kann, Shizunes wütende und hektische Gesten zu übersetzen. Sie kriegt sogar den Gesichtsausdruck hin, nur ihre Stimme ist die gleiche wie immer. Es fehlt am nötigen Zorn, um alles zusammenzubringen."


show misha hips_smile_cas onlayer master
with charachange

mi "Wahaha~. Nimm es nicht zu ernst, Hicchan~! Shicchans Papa macht das mit jedem. Ich glaube, es ist wie ein Scherz~."


hi "Das war der aggressivste Witz überhaupt."


"Ich bin auch nicht davon überzeugt, dass es ein Witz war, wenn man den hastig inszenierten Rückzug bedenkt. Doch dies ist kein guter Moment, um zu diskutieren, ob Shizunes Vater ein Idiot ist."


play music music_shizune fadein 4.0

show misha sign_smile_cas onlayer master
with charachange

mi "Hicchan, lass uns shoppen gehen!"


show shizu adjust_happy_cas onlayer master
with charachange

ssh "Du warst noch nicht in der Stadt, oder? Es wird lustig. Du kannst dir die Sehenswürdigkeiten ansehen, einen Vergnügungspark besuchen, vielleicht auch in einem guten Restaurant essen."


hi "Wir hatten gerade Mittag."


"Auch wenn ich nicht viel gegessen habe."


show shizu behind_smile_cas onlayer master
with charachange

ssh "Schon okay, dann müssen wir einfach dafür sorgen, dass der Tag so gefüllt ist, dass es Zeit fürs Abendessen ist, wenn wir fertig sind."


show misha cross_grin_cas onlayer master
with charachange

mi "Das passt perfekt~! Komm schon, Hicchan~!"


show shizu behind_smile_cas_close onlayer master at closeright
show misha cross_smile_cas_close onlayer master at closeleft
with characlose

"Sofort umzingeln sie mich und verhaken ihre Arme mit meinen. Shizune einen und Misha den anderen."
"Zuerst stolpern wir fast über einander. Shizune geht in einem sehr raschen Tempo, und Misha hat eine ungewöhnlich hopsige Weise, sich zu bewegen."


scene bg shizu_park onlayer master
with locationchange

"Nach kurzer Zeit haben wir den Dreh raus, und ich merke, dass wir auf unserem Weg zur Stadt den Park durchqueren. Es scheint nicht wirklich effizient – wahrscheinlich ist das die landschaftlich reizvollere Route."


"Auf diese Art zu laufen erschwert unsere Kommunikation erheblich. Ich kann mit Shizune überhaupt nicht reden. Shizune und Misha können nur einhändige Gesten nutzen. Es fühlt sich gut an, darum kümmert es mich nicht allzu sehr."


"Als ich Misha gegenüber einen Scherz darüber mache, antwortet sie etwas verwundert."


show misha perky_confused_cas_close onlayer master at closeleft
with charaenter

mi "Wirklich, Hicchan~? Hm… Wenn du wirklich Shicchans Aufmerksamkeit willst, kannst du es mir sagen. Ich kann ihr dann für dich auf die Schulter tippen."


hi "Du könntest mich einfach loslassen und es mich selbst machen lassen. Wie willst du ihr von da aus auf die Schulter tippen?"


show misha hips_grin_cas_close onlayer master
with charachange

mi "Na so~!"


with vpunch

show shizu behind_frustrated_cas_close behind misha onlayer master at closeright
with charachange

"Plötzlich bleibt sie abrupt stehen und versucht hinter ihren Rücken und über meine Schulter zu fassen, um Shizunes Aufmerksamkeit zu bekommen. Es gelingt ihr. Aber auch nur, weil ich auch stehen geblieben bin. Andernfalls wären wir alle umgefallen."


show misha hips_laugh_cas_close onlayer master
with charachange

show shizu adjust_blush_cas_close onlayer master
with charachange

"Offensichtlich musste Shizune auch abrupt anhalten. Der Anblick veranlasst Misha zu ihrem typischen Lachen, was uns noch mehr ins Taumeln bringt."
"Je mehr Shizune versucht, mit ihrer freien Hand zu fuchteln, um sie aufzuhalten, desto mehr muss sie lachen."


"Es ist wirklich lustig zu sehen, wie sie sich so aufregt, und ich fange auch an zu lachen."


stop music fadeout 2.0

scene black onlayer master
with dissolve



label de_S21:

scene bg shizu_guesthisao onlayer master
with locationchange

play music music_dreamy fadein 2.0

"Ich habe mein Zeichensprache-Studium vernachlässigt, darum sollte ich wahrscheinlich einige Stunden nachholen – auch wenn ich denke, dass ich das meiste nur durch Immersion gelernt habe."
"Ich bin darauf ziemlich stolz und muss aufpassen, dass ich damit nicht angebe."


"Die meisten der Bücher, die ich mitgebracht habe, sind keine Handbücher über Gebärdensprache, sondern Studien über die verschiedenen Zeichen-„Dialekte”."
"Ich weiß, dass Shizune und Misha einige Geheimzeichen haben, deren Bedeutung nur die beiden kennen."


"Nachdem ich einige davon gesehen hatte, fiel mir dieses Buch aus der Schulbibliothek ins Auge."


"Vielleicht sollte ich einige Beispiele in meinen eigenen Gebärdenstil einbauen, nur um sie zu ärgern."
"Ich bin mir ziemlich sicher, dass sie ihre Codewörter öfter verwenden, seit ich angefangen habe, Zeichensprache zu lernen. Das wird ihnen eine Lehre sein."


"Nach einer kurzen Pause für eine Dusche, fahre ich wieder mit meinen Gebärdenübungen vor dem Gästezimmerspiegel fort."
"Gestern habe ich mir meine Finger ziemlich heftig aneinander gestoßen. Es tut immer noch weh, und ich will das nicht noch einmal wiederholen."


play sound sfx_doorknock2

show hideaki normal onlayer master at center
with charaenter

"Ich höre das Klopfen an der Tür hinter mir. Als mich umdrehe, sehe ich, wie Hideaki in der Tür steht und mich anstarrt. Wie höflich von ihm zu klopfen, doch normalerweise öffnet man die Tür nicht vorher."


show hideaki triangle onlayer master
with charachange

hh "Was tust du da?"


hi "Ich übe Zeichensprache. Wie lange stehst du schon da?"


show hideaki thinking onlayer master
with charachange

hh "Ich habe nichts gesehen."


"Darum geht's nicht. Ich weiß nicht einmal, was er damit meint. Es ist nicht so, als hätte ich etwas getan, wofür ich mich vor anderen schämen müsste."


"Allerdings muss Zeichensprache für die meisten Leute seltsam aussehen. Ich bin nur daran gewöhnt, weil ich so oft mit Shizune und Misha zusammen bin."


hi "Ich poliere meine Zeichensprache auf und lese auch etwas darüber. Zum Beispiel die Geschichte davon, auch wenn sie das im Zeichenspracheunterricht behandeln."


show hideaki normal onlayer master
with charachange

hh "Deine Schule unterrichtet Zeichensprache in einem Kurs?"


hi "Ja. Gleich am Anfang haben sie gesagt, dass das nicht gerade üblich ist. Ich schätze, wir sind sehr international oder so."


show hideaki serious onlayer master
with charachange

hh "Sieht lustig aus."


hi "Na ja, ich würde es nicht lustig nennen."


show hideaki bored onlayer master
with charachange

hh "Wenn es dir keinen Spaß macht, scheint es eine Menge Arbeit zu sein, nur um mit meiner Schwester zu reden."


hi "Warum sagen das alle immer?"


show hideaki happy onlayer master
with charachange

"Hideakis Mund zuckt, als ob er kurz davor war zu lachen, aber er hält sich zurück. Wo ich darüber nachdenke – er hat noch nicht ein Mal gelacht, seit ich ihn getroffen habe."
"Ich könnte es als ein Kompliment auffassen, dass er nicht über mich lacht. Aber ich bin gespannt, es zu sehen."


hi "Lach."


show hideaki thinking onlayer master
with charachange

stop music fadeout 4.0
hh "…"


show hideaki bored onlayer master
with charachange

hh "Warum?"


"Es war der schnellste und direkteste Weg, der mir zur Erfüllung meines Ziels einfiel."



show hideaki normal_up onlayer master
with charachange

hh "Kannst du mir Zeichensprache beibringen?"


"Er sagt es deutlich, doch nach seiner Körpersprache zu urteilen, ist er nervös. Er muss sich ziemlich Mühe geben, um das zu fragen. Ich schätze, Hideaki mag seine Schwester letztendlich doch."
"Ich hätte aber gedacht, dass Misha viel zugänglicher ist. Darum frage ich mich, warum er sie nicht gefragt hat."


"Innerlich schreie ich heimlich „Ja!”. Ich dachte mir schon, dass er Zeichensprache lernen wollte, und er hat es sogar selbst erwähnt, aber er ist dem Thema geschickt ausgewichen."
"Jetzt stellt sich heraus, dass ich Recht hatte. Ich weiß nicht wirklich, warum mich das so freut."


hi "Klar."


"Aber jetzt wo ich darüber nachdenke, bin ich kein Zeichensprachelehrer. Ich weiß nicht einmal, wo ich anfangen soll."
"Im Unterricht würde ich den Stoff schrittweise über eine Woche lernen. Erwartet Hideaki von mir, dass ich ihm irgendetwas Brauchbares in einem Ein-Tages-Crashkurs beibringe?"


show hideaki normal onlayer master
with shorttimeskip

play music music_normal fadein 3.0

"Mein Lehrer hat einige Tage damit verbracht, uns einfach nur die Geschichte der Zeichensprache beizubringen."
"Ich beschließe, auch damit anzufangen, um etwas Zeit zu bekommen, darüber nachzudenken, wie ich zu den komplizierteren Sachen übergehen kann. Schon nach fünf Minuten hebt Hideaki seine Hand."


show hideaki serious_up onlayer master
with charachange

hh "Ich verstehe nicht, was du da machst."


hi "Uh… Na ja, man kann nicht von jetzt auf gleich unterrichten, weißt du. Man muss es ruhig angehen lassen. Es ist wie beim Schwimmen – man springt nicht einfach in den See wie in irgendeinem Film."


show hideaki triangle onlayer master
with charachange

hh "Ich schwimme nicht."


"Es ist, als ob Wissenschaftler eine Methode entwickelt hätten, all die hyperaktiven, nervigen und kindischen Qualitäten eines kleinen Kindes herauszusaugen und sie dann in den Vater zu implantieren."
"Daraus ist dann ein wildgewordener Idiotenpapa entstanden, und Hideaki blieb übrig."


"Langsam fange ich an, mich klaustrophobisch zu fühlen – trotz der Tatsache, dass das Gästezimmer dreimal größer ist als mein Wohnheimzimmer und wir hier nur zu zweit sind."
"Es ist alles in meinem Kopf. Ich weiß das, und es ist mir egal. Trotzdem benutze ich es als Vorwand, um den Unterricht nach draußen zu verlegen."


scene bg shizu_garden onlayer master
with locationskip

"Hier draußen ist es viel einfacher, sich zu konzentrieren. Auch die wenigen wertvollen Sekunden, die es dauerte umzuziehen, erlaubten mir meine Gedanken zu sortieren."
"Diesmal gab es keine Fragen. Hideaki scheint nicht gleichzeitig reden und laufen zu können."


"Allerdings begreife ich allmählich, dass ich den Unterricht konstant am Laufen halten muss, wenn ich ihm irgendetwas beibringen will."
"Sobald eine Chance besteht, wird er eine Frage stellen. Die führt dann zu weiteren Fragen, und dann gibt es kein Ende mehr."


"Als er mich das zweite Mal fragt, warum eine bestimmte Geste das bedeutet, was sie bedeutet, und ich in meinem Gedächtnis nach der Etymologie einer Geste suchen muss, die ich selbst erst seit einem Monat kanne, suche ich nach einem Ausweg."


hi "Hideaki, lass uns eine Pause machen."


show hideaki bored onlayer master
with charachange

hh "Okay."


show hideaki serious onlayer master
with charachange

hh "Wie ist deine Schule so?"


"Dieses Kind ist wie ein kleiner Reporter, doch es passt zu jemanden in seinem Alter, so neugierig zu sein, und die Frage stört mich auch nicht."


hi "Wie sie ist? Ich hab nie wirklich darüber nachgedacht. Sie liegt oben auf diesem Berg, sodass es sich dort schon manchmal etwas einsam und isoliert anfühlt – auch wenn man gerade deswegen eine ziemlich gute Aussicht hat."


hi "Die Schüler sind interessant. Eigentlich habe ich mich am Anfang mies gefühlt. Du weißt, was für eine Art von Schule es ist, oder?"


show hideaki normal onlayer master
with charachange

hh "Ja."


hi "Ich fühlte mich mies, weil ich nicht dorthin wollte. Ich weiß gar nicht mal mehr genau, was ich zu jener Zeit dachte."
hi "Wahrscheinlich, dass eine Schule für Behinderte ein deprimierender Ort wäre. Sie sagten mir, dass ich dorthin gehen und vergessen werden soll."


hi "Aber dann lebten dort alle nur ihr eigenes Leben. Also fühlte ich mich noch mieser. Es war überhaupt nicht anders, darum kam ich mir vor wie ein Idiot."


hi "Shizune war die erste Person, die ich traf. Mit ihr habe ich die meisten Fächer. Mit Misha auch, weil sie immer zusammen sind. Ich vermute, die Schule ist entgegenkommend genug, um ihre Stunden so gut es geht zusammenzulegen."
hi "Dann ist da dieses Mädchen in meiner Klasse, das mir leid tut – Hanako."


hi "Sie hat diese Verbrennungen und scheint Komplexe deswegen zu haben. Aber ich denke, sie sieht recht hübsch aus. Sie ist ein süßes Mädchen. Und auch mit Lilly befreundet. Du kennst Lilly, richtig? Hat sie Hanako mal erwähnt?"


show hideaki thinking onlayer master
with charachange

hh "Ja, ab und zu."


hi "Ich versuche, mich zu erinnern, wer sonst noch interessant ist. Wir haben eine kleine Star-Läuferin, die auf Prothesen läuft."


hi "Und dann gibt es dieses eine Mädchen, Rin, das keine Arme hat, aber eine großartige Malerin ist. All ihre Kunst hat diese raue, lebendige Qualität. Warst du jemals in Yamaku? Du hast wahrscheinlich einiges von ihr herumhängen sehen."


hi "Manchmal ist sie ein wenig merkwürdig, aber ich habe gehört, dass künstlerische und schöpferische Typen immer so sind."
hi "Da fällt mir ein, der Kerl, der gegenüber von mir im Flur wohnt, ist auch ziemlich seltsam. Aber zumindest kann er interessant sein."


show hideaki normal onlayer master
with charachange

hh "Du bist auch interessant."


hi "Ist das schlecht? Und was soll dieser unterschwellige Ton? Was heißt das überhaupt? Sagst du, dass ich komisch bin, Hideaki?"


show hideaki triangle onlayer master
with charachange

hh "Du redest sehr viel."


"Mein erster Reflex ist, in die Defensive zu gehen, aber je mehr ich darüber nachdenke, desto mehr denke ich, dass er Recht hat."


hi "Das stimmt, ich rede sehr viel. Ich glaube nicht, dass ich früher so war."


hi "Ich denke… es liegt wahrscheinlich daran, dass ich so viel Zeit mit Shizune und Misha verbringe."
hi "Wenn ich mit ihnen rede, stecken mich ihre Zirkellogik und die Art, wie sie alles angehen, irgendwie an. Ich fühle mich, als würde ich entweder übertönt oder zurückgelassen."


show hideaki confused onlayer master
with charachange

hh "Meine Schwester kann dich übertönen?"


hi "Natürlich nicht wortwörtlich. Es ist schwer zu erklären. Sie haben mehr Energie als ich. Es ist wie eine Aggressivität. Ich fühle mich nicht so, als müsste mich dem gleichkommen, aber ich will es."
hi "Ich denke, dass deine Schwester diese Wirkung auf Menschen hat."


show hideaki thinking onlayer master
with charachange

hh "…"


hi "Schaust du zu deiner Schwester auf?"


show hideaki normal_up onlayer master
with charachange

"Er starrt mich ausdruckslos an, angespannt und verwirrt darüber, wie er auf diese Frage reagieren soll."


show hideaki angry_up onlayer master
with charachange

stop music fadeout 5.0

hh "Ich werde besser als Shizune sein."


hi "Besser worin?"


show hideaki angry onlayer master
with charachange

hh "In… allem."


hi "Und was könnte das sein?"


show hideaki triangle onlayer master
with charachange

hh "Ich kann Zaubertricks."


hi "Meinst du, wie Leuten zu sagen, dass du ihre Nase hast? Oder eher wie die Art von Magie, bei der du einen Hasen aus deinem Arsch ziehst?"


"Er sieht nicht erfreut aus. Eines Tages werde ich Hideaki lachen sehen. Wenn es sein muss, versuche ich es vielleicht einfach mit Kitzeln."


play sound sfx_doorslam

show hideaki surprise onlayer master
with vpunch

show hideaki thinking onlayer master at twoleft
show bg shizu_garden onlayer master at bgleft
with dissolvecharamove

show jigoro neutral onlayer master at tworight
with charaenter

"Die Hintertür fliegt auf, und Jigoro schreitet mit geradem Rücken und weiten, langsamen und majestätischen Schritten hindurch, als wäre er ein König oder ein gigantischer Idiot."


"Ich versuche, mich wegzudrehen – wenn ich ihn nicht sehen kann, kann er mich vielleicht auch nicht sehen. Unglücklicherweise geht der Plan nicht auf, und wie aus dem Nichts taucht er hinter meiner Schulter auf."


show jigoro laugh onlayer master
with charachange

play music music_happiness fadein 2.0

hx "Oho. Was ist hier los? Was fummelt ihr Zwei so mit euren Händen rum? Spielt ihr Fadenspiele wie Mädchen?"


hi "Ich bringe Hideaki etwas Zeichensprache bei. Was ist mit Ihnen, Herr Hakamichi?"


show jigoro angry onlayer master
with charachange

"Er kneift seine Augen argwöhnisch zusammen, als ob er Höflichkeit ihm gegenüber nicht gewöhnt wäre."


hx "Ich schreibe eine Autobiographie über mein Leben und meine Erinnerungen. Und mit „schreiben” meine ich, ich diktiere es meiner Biografin. Leider kommt sie zu spät. Unprofessionell."


show jigoro smug onlayer master
with charachange

hx "Vielleicht solltest du sie lesen, wenn sie später in diesem Jahr veröffentlicht wird. Ich kann dich auf die Warteliste schreiben."
hx "Vielleicht wird sie dir ein Gefühl für Gut und Böse geben, an welchem es dir zu mangeln scheint, und dich inspirieren, endlich nicht mehr so nutzlos zu sein."


"Es kann nicht nachhaltig für ihn sein, jeden so beiläufig zu beleidigen."
"Obwohl… Hideaki ist wahrscheinlich zu gleichgültig, um es überhaupt zu bemerken, Shizune ist taub, und bei Misha müssen die meisten Beleidigungen abprallen. Aber Akira hat sicherlich eine Meinung dazu."


"Ich versuche, nicht darüber nachzudenken. Wenn er mich damit zum ausflippen bringen will, muss ich ruhig bleiben, sonst gewinnt er. Er darf absolut, auf gar keinen Fall gewinnen. So muss sich Shizune fühlen."


hi "Wie alt sind Sie?"


show jigoro neutral onlayer master
with charachange

hx "Sechsundvierzig."


hi "Das scheint nicht alt genug, um das Schreiben einer Biographie zu rechtfertigen. Ich meine, das ist nicht einmal alt. Schreiben die meisten Leute ihre Memoiren nicht viel später?"


show jigoro angry onlayer master
with charachange

hx "Sei still, Junge. Ich gebe dir einen Tipp: Sprich nicht über Altersangelegenheiten mit Leuten, die älter sind als du. Du bist nicht einmal halb so alt wie ich, du hast kein Recht über Alter zu reden. Ich habe ein Geschwür, das älter ist als du."


"Er sollte sich untersuchen lassen. Aber vielleicht hat er nicht ganz Unrecht – er ist definitiv älter als ich."


show jigoro laugh onlayer master
with charachange

hx "… So oder so, wenn wir gleich alt wären, würde ich dir das nicht erklären müssen, Pullunderträger."


hi "Urgh."


show jigoro angry onlayer master
with charachange

hx "Warum machst du dieses Geräusch? Bist du wütend? Nun, offensichtlich. Gut. Dein Pullunder ist schrecklich, und ich will, dass du dich deswegen schlecht fühlst. Deine lodernden Augen sagen mir, dass es funktioniert."


hi "Ich mag meinen Pullunder."


show jigoro smug onlayer master
with charachange

hx "Bestimmt magst du es auch, Klebstoff zu schnüffeln. Das heißt noch lange nicht, dass es richtig ist."


hi "Ich schnüffele keinen Klebstoff. Wie kommen Sie darauf, dass ich so etwas tun würde?"


show hideaki normal onlayer master
with charachange

hh "Das ist Verleumdung."


"Ich frage mich, woher Hideaki weiß, was Verleumdung ist. Vielleicht ist Jigoro ein Anwalt."
"Irgendwie kann ich mir das vorstellen, auch wenn ich dachte, dass nur Fernsehanwälte so feindselig sind. Ich weiß nicht, ob ich die Gelegenheit ergreifen und ihn nach seinen Job fragen sollte."


hi "Er hat Recht. Es ist Verleumdung. Sind Sie ein Anwalt?"


show jigoro neutral onlayer master
with charachange

hx "Ich habe geraten. Eine Vermutung basierend auf der Tatsache, dass du dumm bist. Das ist genau wie deine Vermutung, dass ich Anwalt bin, obwohl ich dir keinen Grund gegeben habe, das zu glauben."
hx "Wenn du so sehr wissen willst, was ich mache, warum bestellst du dann nicht meine Autobiographie vor?"


show jigoro angry onlayer master
with charachange

hx "Jetzt beleidigst du mein Buch, und damit auch gleichzeitig mein gesamtes Leben. Was gibt dir das Recht, das zu tun? Arrogant."
hx "Ich frage mich, was ich tun kann, damit du meine Mühen verstehst. Vielleicht sollte ich dir eine überziehen. Mit meiner Autobiographie."


hx "Ich hoffe, du ziehst aus den Schlägen eine wertvolle Lektion. Zum Beispiel, dass man keine Vermutungen anstellen soll."


show hideaki bored onlayer master
with charachange

hh "Körperverletzung…"


"Aber er hat mir auch unterstellt, dass ich Klebstoff schnüffele. Ich ziehe in Erwägung, ihm dieses krasse Beispiel von Heuchlerei vorzuhalten, doch ich glaube nicht, dass es das wert wäre."
"Er würde sich wahrscheinlich mit „Sei still, Junge” herausreden."


show jigoro smug onlayer master
with charachange

hx "Zu meiner Zeit wurde Kinder gesehen, nicht gehört. Und ein Erwachsener zu sein bedeutete, durch harte Zeiten gegangen zu sein."
hx "Selbst mit einem kurzen Blick konnten die Leute den Charakter eines Mannes beurteilen. Kindheit gab es nur, um sich aufs Erwachsenenleben vorzubereiten."


hx "Kannst du nicht die Ansammlung meiner Erfahrungen auf einem Blick sehen, wenn du mich ansiehst?"


hi "Äh… vielleicht. Waren Sie ein Schwertkämpfer?"


"Er könnte genauso gut Hawaiianer sein. Und ein Werwolf."


hi "Moment, sagten Sie mir nicht eben, dass ich keine Vermutungen machen soll? Jetzt haben sich mich gerade darum gebeten."
hi "Und Sie sagen, dass es alle getan haben, als Sie so alt waren wie ich. Und das muss etwa in den 80ern gewesen sein. Das ist nicht einmal so lange her!"


"Ich bin bereit, ihm meine Meinung zu sagen."
"Er tut so, als musste er 25 Kilometer durch den Schnee stapfen, dann mit einer Dampflok, wo er selbst Kohle schaufeln musste, zu einem Berg fahren, und diesen dann noch gegen Oger kämpfend hochklettern, um zur Schule zu kommen."


"Aber jetzt, da ich endlich streiten will, ist Jigoro erfreut, ein gutes Thema zu haben, um weiterhin darüber schwafeln zu können, wie schwer es war, vor einer Generation aufzuwachsen."
"Nebenbei wirbelt er sein Schwert wie einen Schlagstock und pausiert ab und zu, um zu gähnen oder nach der Uhrzeit zu sehen."


"Die Verspätung seiner Biographin beschäftigt ihn immer noch. Das heißt, in der ganzen Zeit, in der er mich beleidigt hat, hat er das wahrscheinlich nur getan, um sich die Zeit zu vertreiben."
"Und was seine Beleidigung noch schlimmer macht: Seine Uhr ist wirklich ziemlich nett."


show jigoro angry onlayer master
with charachange

hx "… Als ich in deinem Alter war, hatten Kinder Verantwortung."
hx "Nicht wie heutzutage. Ekelerregend. Niemand denkt mehr an die Konsequenzen seiner Taten. Sie tun einfach, was sie wollen. Alle glauben, dass keiner sie zur Rechenschaft ziehen wird, weil sie jung sind."


"Es ist seltsam, diese Beschreibung könnte zu Shizune und Misha passen. Gerade gestern dachte ich so etwas ähnliches. Aber es passt nur ein wenig zu ihnen."


hx "Sieh dich an. Ein unmoralischer, perspektivloser, krimineller Klebstoffschnüffler, mit völligem Mangel an Etikette und absolut keinem Modegefühl. Du bist das Japan von Morgen. Schändlich. Ist das die Zukunft dieses einst großen Landes?"


hi "Ich kenne jemanden, mit dem Sie sich gut verstehen würden."


hx "Nicht unterbrechen! Wer? Einer deiner Freunde? Warum sollte ich mit so einem furchtbaren Teenager reden wollen? Hast du überhaupt zugehört? Warum bist du so ungezogen, Junge? Mit diesem Benehmen wirst du nicht viele Freunde finden."


hi "Ich wünschte, Sie würden aufhören, mir so viele Ratschläge zu geben."


"Oder zumindest wünschte ich, dass er mir Ratschläge gibt, bei denen er den Anstand hat, sie auch selbst zu befolgen."


show jigoro neutral onlayer master
with charachange

hx "Wo bist du gewesen?"


hi "Hä?"


show jigoro angry onlayer master
with charachange

stop music fadeout 3.0

hx "Nicht du, du Idiot."


show jigoro angry onlayer master at Position(xpos=0.85)
show hideaki normal onlayer master at Position(xpos=0.45)
show bg shizu_garden onlayer master at center
with dissolvecharamove

show shizu behind_blank_cas behind hideaki onlayer master:
    twoleft
    xpos 0.2
with charaenter

shi "…"


hi "Ups. Ich hab dich gar nicht bemerkt."


show shizu adjust_happy_cas onlayer master
with charachange

"Shizune lächelt und winkt kurz. Wegen ihres Erscheinens hat Jigoro aufgehört zu reden. Allein deswegen bin ich schon glücklich, sie zu sehen."


show shizu basic_normal2_cas onlayer master
with charachange

ssh "Misha und ich haben uns entschieden, in die Stadt zu gehen."
ssh "Hisao, ich habe bemerkt, dass du dir gestern einige Anziehsachen in einem Ladenfenster angesehen hast. Ich dachte, ich gehe zurück und kaufe einige davon für dich. Eigentlich sollte es eine Überraschung sein."


"Sie sieht verärgert darüber aus, dass ihre Überraschung ruiniert ist, obwohl sie sie selbst ruiniert hat."


show shizu behind_blank_cas onlayer master
with charachange

ssh "Bitte sehr!"


hi "Vielen Dank."


show shizu basic_normal_cas onlayer master
with charachange

ssh "Misha wollte sich ihre Haare schneiden lassen. Ich habe ihr gesagt, dass sie es nicht tun soll, aber sie meinte, dass es zu heiß für den Sommer wäre."


hi "Ach so? Ich weiß nicht, mir erscheint das sehr sinnvoll. Da drunter muss es wie in einem Ofen sein. Ich will es sehen. Wo ist Misha überhaupt?"


mi "Hier~! Hi Hicchan~! Hallo Herr Shicchans Vater~! Hi Hideaki~!"


show jigoro smug onlayer master
with charachange

hx "…"


play music music_running

show mishashort hips_grin_cas behind shizu onlayer master at offscreenleft
with charamoveinright

hide mishashort onlayer master
with None

show mishashort hips_grin_cas onlayer master at offscreenleft
with None

show shizu basic_normal_cas onlayer master:
    xpos 0.3
show jigoro smug onlayer master:
    xpos 0.95
show hideaki normal onlayer master:
    xpos 0.55
show mishashort hips_grin_cas onlayer master:
    center
    xpos 0.1
show bg shizu_garden onlayer master:
    xpos 0.55
with dissolvecharamove

"Misha läuft einmal in einem großen Kreis um uns herum, bevor sie neben Shizune stehen bleibt."


"Zum ersten Mal hat sie ihre Hände nicht auf meine Augen gelegt – obwohl ich nun sehe, dass sie auch mit Tüten beladen ist und es somit nicht einmal hätte tun können, wenn sie gewollt hätte."
"Auch wenn ich davon überzeugt bin, dass sie es zumindest versucht hat."


"Ihre liebevoll gestalteten Locken sind nun weg, zugunsten eines viel kürzeren und sportlicheren Looks."
"Misha sieht sogar noch glücklicher aus als sonst. Wahrscheinlich weil sie weiß, dass sie nicht mehr jeden Morgen zu Tagesanbruch ihre Haare machen muss."


show jigoro angry onlayer master
with charachange


hx "Was soll dieser Haarschnitt? Du siehst wie eine Praktikantin aus. Dein alter Haarschnitt sah lediglich so aus, als würdest du eine pinke Richterperücke tragen. Richter zu Praktikant ist ein gewaltiger Abstieg."


show shizu behind_frown_cas onlayer master
with charachange

ssh "Hisao, sagt er etwas Beleidigendes? Sag ihm, dass er meine Freunde nicht beleidigen soll!"


hi "Beleidigen Sie nicht meine Freunde."


hx "Wer von euch spricht gerade?"


hi "Wir beide. Ich stimme ihr zu."


show mishashort hips_smile_cas onlayer master
with charachange

mi "Hehehe~! Was denkst du, Hicchan?"


show shizu adjust_frown_cas onlayer master
with charachange

ssh "Du hättest es lassen sollen, wie es war."


show mishashort perky_sad_cas onlayer master
with charachange

mi "Ohh~… Hicchan, du siehst enttäuscht aus. Magst du es auch nicht?"


hi "Na ja, ich gebe zu, ich mochte deinen alten Haarschnitt lieber, aber dieser ist auch ganz nett. Er passt zu dir."


show mishashort hips_grin_cas onlayer master
with charachange

mi "Ohh, danke, Hicchan~!"


hx "Rührend. Wenn er dir so sehr gefällt, solltet ihr beide tauschen."


hi "Man kann einen Haarschnitt nicht tauschen."


hx "Wie schade. Sogar ihr alter Haarschnitt würde dir besser stehen als dein gegenwärtiger Taugenichts-Haarschnitt. Schrecklich. Was dich betrifft…"


show jigoro laugh onlayer master
with charachange

hx "Hmmm… Eigentlich ist er nicht ganz so geschmacklos wie dein alter Haarschnitt. Er gefällt mir."


show mishashort cross_laugh_cas onlayer master
with charachange

mi "Ahahahaha~! Wirklich? Vielen Dank, Herr Shizunes Papa~!"


show jigoro angry onlayer master
with charachange

hx "Ich heiße Herr Hakamichi. Sprich wie ein normaler Mensch."


show mishashort perky_smile_cas onlayer master
with charachange

mi "Hm~? Ich verstehe nicht~! Okay, okay, okay~! Ich werde Sie Herr Hakamichi nennen!"


hx "Argh, es ist, als würde man mit einer Querflöte reden. Verachtenswert. Wo ist meine Biografin? Hideaki!"


show jigoro invis onlayer master
show shizu basic_normal_cas onlayer master
show hideaki bored onlayer master
with charaexit

"Er beginnt, leise mit sich selbst zu reden, und geht. Ich schätze mal, ein launischer, alter Möchtegern wie Jigoro, würde zumindest zögern, Mädchen anzuschreien."
"Plötzlich macht er kehrt, unfähig dem Drang zu widerstehen, das letzte Wort zu haben."


show jigoro angry onlayer master
with charaenter

hx "Und noch etwas: Du solltest nicht so laut sein. Ich mag es nicht, angeschrien zu werden."


show mishashort hips_grin_cas onlayer master
with charachange

mi "Was? Schreien~? Ich schreie nicht~!"


"Ich kann mir keinen Unqualifizierteren vorstellen, wenn es darum geht, was auffällig ist oder jemand dafür zu schelten, wenn man Leute anschreit. Es ist wie eine Parade von Heuchelei, in der ein Höhepunkt nach dem anderen kommt."


"Dann passiert etwas Seltsames. Misha findet Jigoro offenbar lustig und lacht so gut wie jedes Mal, wenn er etwas sagt, was ihn sie nur noch schlimmer beschimpfen lässt. Ich glaube, das ist das, was man einen Teufelskreis nennt."


"Mishas Stimme ist erfüllt mit explosionsartigem Gelächter und scheint von überall her zu kommen. Die von Jigoro wiederum ist dröhnend und zielgerichtet wie eine Kanone. Auf jeden Fall sind sie beide unglaublich laut."


"Je mehr die beiden miteinander reden, desto mehr scheinen sie sich in ihrer Lautstärke gegenseitig zu übertrumpfen."


show mishashort perky_sad_cas onlayer master
with charachange

mi "Au~! Meine Ohren tun weh~!"


hx "WARUM SCHREIST DU?"


hide shizu onlayer master
with charaexit

show black onlayer master
with hands_in

"Shizunes Hände bedecken von hinten meine Augen. Ich bin das so sehr von Misha gewohnt, dass ich zum ersten Mal wirklich verwirrt deswegen bin, weil Misha vor mir steht."


show shizu adjust_happy_cas_close behind black at center onlayer master
show hideaki bored onlayer master at center
with None

hide black onlayer master
with hands_out

"Sie lässt los und presst einen Finger gegen ihre Lippen."


show shizu behind_smile_cas_close onlayer master
with charachange

ssh "Was für eine perfekte Ablenkung! Jetzt ist unsere Chance. Lass uns wegschleichen."


his "Warum müssen wir wegschleichen? Warum nicht einfach gehen?"


show shizu adjust_smug_cas_close onlayer master
with charachange

ssh "Es würde nicht so viel Spaß machen."


show shizu basic_happy_cas_close onlayer master
with charachange

ssh "Es ist beschlossen: Es ist eine Geheimmission. Entkommen ohne entdeckt zu werden. Hideaki zu retten gibt Bonuspunkte."


hide shizu onlayer master
with charaexit

stop music fadeout 3.0

"Und schon hat sie die Situation zu einem Spiel vereinfacht. Shizune entfernt sich leise vom Schauplatz und beginnt, sich ins Hausinnere hinauszutasten. Ich laufe ganz normal."





label de_S22:

scene bg shizu_living onlayer master
with locationskip

"Zuerst kann ich Shizune nicht finden, doch schließlich läuft sie in den Hauptteil des Hauses, während sie an einem Glas Eiswasser nippt und ihre Brille in ihrer freien Hand vor- und zurückbaumeln lässt. Als sie mich sieht, setzt sie sie zügig auf."


show shizu basic_normal2_cas onlayer master at center
with charaenter

play music music_ease fadein 4.0

ssh "Du hast Hideaki nicht gerettet. Das bedeutet, dass du keine Bonuspunkte kriegst. Wenn du auch für deinen Stil bewertet werden würdest, würde ich dir Punkte für eine laaaaaangweilige Flucht abziehen."


his "Es sah so aus, als wolltest du mit mir sprechen. Ich wusste nicht, dass ich dabei stilvoll vorgehen sollte. Weißt du, manche sagen, dass die stilvollsten Leute die sind, die nicht zu sehr versuchen, cool auszusehen."


show shizu cross_wut_cas onlayer master
with charachange

ssh "Du bist wirklich cool."


"Ich frage mich, wie ich ihren Sarkasmus so leicht erkennen kann, und wie schwer es gewesen sein muss, das Konzept des Sarkasmus zu lernen, ohne hören zu können. Ich kann's mir nicht vorstellen."


his "Scheint, als hättest du gute Laune."


"Auch wenn ich vermute, dass es keine wirklich gute Laune ist. Sie wirkt eher aufgeregt."


show shizu behind_frown_cas onlayer master
with charachange

ssh "Ich habe schlechte Laune."


show shizu basic_normal2_cas onlayer master at Position(ypos=1.1)
with dissolvecharamove

"Sie stellt ihr Getränk ab und setzt sich auf die Couch."


show shizu behind_frown_cas onlayer master
with charachange

ssh "Ich mochte ihre normale Frisur viel lieber. Es sah so hübsch aus. Es war kultiviert und sorgfältig. Jetzt sieht sie zu sportlich und jungenhaft aus."


his "Ich würde Misha nicht kultiviert und sorgfältig nennen. Das klingt eher nach dir. Du solltest es ausprobieren. Lass deine Haare wachsen und dreh sie zu Spiralen."


his "Hmm… das könnte dir sogar wirklich gut stehen."


show shizu adjust_frown_cas onlayer master
with charachange

"Shizune reibt grob den Rahmen ihrer Brille und sieht verärgert aus, wegen der Implikationen von dem, was ich ihr gerade gebärdet hatte."
"Das ist in Ordnung, denn genau so war es auch gemeint. Als ich mich hinsetze, kommt sie ein wenig näher zu mir."


show shizu basic_angry_cas onlayer master
with charachange

ssh "Bin ich dir zu jungenhaft?"


his "Nun, niemand würde dich als jungenhaft bezeichnen… was das Aussehen betrifft."


"Sie wirft mir einen erzürnten Blick zu. Ich muss mich anstrengen, um ernst zu bleiben."


his "Vielleicht solltet ihr beide trotzdem die Frisuren tauschen."


shi "…"


show shizu behind_frown_cas onlayer master
with charachange

ssh "Du klingst wie mein Vater."


show shizu adjust_smug_cas onlayer master at center
with Dissolvemove(0.2)

"Es stimmt. Sie kichert lautlos, als sie sieht, wie sehr mich das ärgert. Sie springt auf und wirbelt ein unsichtbares Schwert in ihrer linken Hand, während sie militärisch gerade steht und Grimassen schneidet. Eine erschreckend genaue Nachahmung."


show shizu basic_frown_cas onlayer master
with charachange

ssh "Wie auch immer, ich nehme keine Ratschläge von jemandem an, der einen blauen Pullover mit braunen Hosen trägt. Wo ist dein Sinn für Farbharmonie? Schrecklich."


show shizu adjust_smug_cas onlayer master
with charachange

ssh "… Aber meinen Haarschnitt verändern… Das könnte lustig sein. Oder nicht? Ich würde gerne sehen, wie alle darauf reagieren würden."


his "Du musst es wirklich mögen, mit Leuten zu spielen. Manchmal glaube ich, ein bisschen zu sehr."


show shizu adjust_frown_cas onlayer master
with charachange

"Keine Antwort. Die Art und Weise, wie sie an ihrer Brille fummelt und ihre Stirn runzelt, sagt mir, dass ihr keine gute einfällt."


show shizu behind_blank_cas onlayer master
with charachange

ssh "Es macht Spaß."


"Dann, mit mehr Selbstsicherheit, während sie sich mir nähert:"


show shizu basic_happy_cas onlayer master
with charachange

ssh "Es macht Spaß, immer mehr Menschen in mein Leben zu ziehen."


his "Oh, ich verstehe."


"Ich frage mich, ob ich auch zu denen gehöre. Ich will sie fragen, aber bin mir nicht einmal sicher wie."


show shizu adjust_happy_cas onlayer master
with charachange

"Um zu sagen, dass sie die Frage so oder so nicht beantworten würde, wedelt sie präventiv mit ihrem Finger."


stop music fadeout 0.5

show shizu adjust_blush_cas_close onlayer master
with vpunch

"Sie greift nach ihrem Glas, aber scheint nicht zu bemerken, wie weit sie sich schon die ganze Zeit langsam davon entfernt hat. Um zu verhindern, dass sie ungeschickt umfällt, versucht sie, sich an mir festzuhalten und zieht mich letztendlich auf sie."


scene ev shizu_couch onlayer master
with vpunch

play music music_serene fadein 9.0

"Als ich mich über sie lehne, kann ich den Wärme ihres Körpers spüren und bemerke, wie nahe wir uns sind. Ich kann das sanfte Atmen und das leise Rascheln ihrer Kleidung hören, als sie für einen Moment herumrutscht."


"Auf ihre Wangen wandert langsam eine sanfte Röte, doch ihre Augen sind auf meine fixiert, dunkel und ohne zu blinzeln."


"Es ist der gleiche Anblick wie beim ersten Mal, als ich sie sah. Durchdringend und emotionslos. Wie die Augen einer Katze, die nur darauf wartet, was als nächstes passiert. Es macht mich nervös, auf so eine Weise angesehen zu werden."


"Dies ist das erste Mal seit langer Zeit, dass ich ihr so nah bin, und die Stimmung ist nun anders. Die Situation ist gerade nicht die gleiche wie das zufällige Berühren ihrer Hand oder Mishas übliche Spielchen."


"Ihre Finger verflechten sich zaghaft, doch sie macht keine Anstalten, sich zu bewegen. Der Blick in ihren Augen ist nicht leer wie ich gedacht hatte. Er ist eher erwartungsvoll."
"Ich frage mich, ob ich vielleicht schon die ganze Zeit ihren Erwartungen gefolgt bin."


scene bg shizu_living onlayer master
with vpunch

show shizu behind_blank_cas_close onlayer master
with charaenter

"Ich spüre, wie sie mich behutsam aber fest an den Schultern greift und mich von sich schiebt."
"Ich rolle mich seitwärts auf die Couch und zwinge mich in eine Sitzposition weniger als ein paar Zentimeter von ihr entfernt. So wie ich mich fühle, könnten es genauso gut zehn Meter sein."


"Wenn ich darüber nachdenke, ist das vielleicht einer der größten Nachteile der Zeichensprache. Shizune sagte, dass man Zeit zum Überlegen hat, wenn man mit den Händen etwas gebärden muss."


"Andererseits bedeutet es auch, dass was normalerweise eine peinliche Stille wäre, zu einer unüberwindbaren Mauer wird."
"Wenn ich könnte, würde ich einfach irgendetwas plappern – irgendetwas, um die Anspannung, die ich gerade fühle, zu zerstreuen. Doch ich kann es nicht."


"Normalerweise bin ich der Meinung, dass es normal wäre, sich zu entschuldigen und vielleicht zu gehen. Aber jetzt frage ich mich, ob das hier auch gilt. Ich muss daran denken, wie so eine Aktion wirken würde: Als ob ich mich davonschleichen würde."


"Natürlich kann ich auch nicht so tun, als ob nichts passiert wäre. Das wäre eine Beleidigung für uns beide."
"So sehr ich es auch nicht will, ich entschuldige mich schnell. So schnell, dass ich vergesse, es zu gebärden. Dann gehe ich zurück in mein Zimmer."


window hide None

scene bg shizu_guesthisao_ss onlayer master
with locationskip

play sound sfx_pillow
with vpunch

$ renpy.music.set_volume(0.5, 1.0, channel="music")

show black onlayer master
with shuteye

window show

"Seufzend lasse ich mich rückwärts auf mein Bett fallen. Ich wünschte, ich könnte jetzt einfach einschlafen, aber ich bin hellwach."


play sound sfx_doorclose
$ renpy.music.set_volume(1.0, 3.0, channel="music")

with Pause(3.0)

show shizu basic_normal2_cas_close onlayer master
hide black onlayer master
with openeye

"Ich setze mich auf, als ich das Schließen der Tür höre und öffne meine Augen, um Shizune auf dem Stuhl vor mir sitzen zu sehen."


show shizu behind_blank_cas_close onlayer master
with charachange

shi "…"


"Sie stellt eine Frage, die wegen meiner Verwunderung komplett an mir vorbeigeht. Es ist kein Gefühl, das ich gut verbergen kann, und ich glaube nicht, dass es das ist, was sie beabsichtigt hatte."
"Was auch immer sie sagen wollte, sie lässt es sein und versucht für eine Weile nicht noch einmal, es zu gebärden."


show shizu adjust_happy_cas_close onlayer master
with charachange

ssh "Das ist das erste Mal, dass ich in deinem Zimmer bin."


"Sie tippt ihre Finger aneinander und versucht, sich bei dem Gedanken übertrieben verlegen und zurückhaltend aussehen zu lassen. Ich kann den Witz nicht würdigen. Allein die Tatsache, dass sie hier ist, lässt mich gerade nicht klar denken."


his "Sehr lustig. Das ist nicht mal mein Zimmer. Es ist dein Gästezimmer."




label de_S22a:

his "Außerdem sind du und Misha schon einmal in mein Zimmer geplatzt."


show shizu behind_blank_cas_close onlayer master
with charachange

"Es scheint, als würde sie erwarten, dass ich mehr sage."
"Ich erinnere mich an das panische Gefühl, als sie in mein Zimmer stürmten, und hatte Angst vor den Schlussfolgerungen, die sie ziehen könnten, wenn sie die Türme von Tabletten sehen. Auch wenn ich glaube, dass sich Shizune nicht daran erinnert."


show shizu basic_normal_cas_close onlayer master
with charachange

ssh "Es hat dich nervös gemacht."




label de_S22b:

ssh "Du sahst immer noch schockiert aus, als ich reinkam."



label de_S22c:

"Die Art und Weise, wie sie das sagt, versetzt mir einen Stich."


his "Eine Menge Dinge machen mich nervös."


his "Du bist eins davon."


show shizu behind_blank_cas_close onlayer master
with charachange

shi "…?"


his "Weil du übereifrig bist, immer andere Leute zum Mitmachen zu bewegen… egal was du tust. Sei es der Beitritt zum Schülerrat oder auch nur eine Pause zu machen. Ob sie es wollen oder nicht."


show shizu basic_angry_cas_close onlayer master
with charachange

shi "…"


show shizu adjust_happy_cas_close onlayer master
with charachange

shi "… … … …"


show shizu basic_normal2_cas_close onlayer master
with charachange

shi "… …"


"Sie gebärdet fast im Schneckentempo und stoppt zusätzlich noch ihre Hände mitten im Satz. Bevor ich auch nur anfangen kann, sie ansatzweise zu verstehen, zerfallen ihre Worte formlos. Ich versuche so zu tun, als ob dies nicht der Fall wäre."


"Es scheint zu funktionieren, aber sie sieht ein bisschen traurig aus, und ich bedauere, dass ich nichts zu sagen habe, was den seltsam wehmütigen und distanzierten Ausdruck auf ihrem Gesicht verschwinden lässt."
"Alles, was ich tun kann, ist darauf zu warten, dass sie sich selbst davon befreit."


show shizu behind_sad_cas_close onlayer master
with charachange

ssh "Du hast Recht. Ich will alle in mein Leben ziehen. Aber seit kurzem bin ich mir nicht mehr sicher, ob das das Richtige ist."


his "Es hat mich gefreut, wie du mich neulich Nachts zu deinem Lieblingsrestaurant mitgenommen hast."


show shizu basic_normal_cas_close onlayer master
with charachange

ssh "Es war nicht unbedingt mein Lieblingsrestaurant… Ich habe noch andere, die mir gefallen. Ich könnte sie sogar nach Noten einstufen."


his "Wirklich…"


show shizu adjust_frown_cas_close onlayer master
with charachange

ssh "Dieser Stuhl ist so hart. Ich will auf dem Bett sitzen."


"Während ich ihr mit einer Bewegung signalisiere, dass sie sich keinen Zwang antun soll, warte ich darauf, dass sie vom Stuhl aufsteht und sich zu mir setzt. Obwohl es nicht meine Absicht war, findet sie es amüsant."


show shizu behind_smile_cas_close onlayer master
with charachange

stop music fadeout 5.0

ssh "Schließ deine Augen."


his "Warum?"


show shizu adjust_smug_cas_close onlayer master
with charachange

ssh "Das ist eine Überraschung."


show black onlayer master
with shuteye

"Ich beschließe, sie bei Laune zu halten und mache sie zu."
"Ich kann spüren, wie sie sich über mich lehnt, und plötzlich berührt etwas Weiches und Feuchtes meine Lippen. Mein Körper verkrampft sich vor Überraschung. Glücklicherweise war das nicht die peinlichste Reaktion, die ich hätte haben können."


"Es war nur ein flüchtiger Kuss, doch gerade als ich dachte, es wäre vorbei, küsst sie mich noch einmal – dieses Mal viel intensiver."
"Ihre Hände wandern über meine Schultern zu meinem Hals und wieder zurück. Dann quer über meine Schultern und meine Arme hinab."


"Ich kann das Gewicht ihres Körpers auf meinen Beinen spüren, und die Erotik dieser Situation geht nicht an mir vorbei."
"An diesem Punkt versuche ich, meine Augen einen Spalt zu öffnen, doch als ob sie es erwartet hätte, legt sie ihre Finger auf meine Augenlider."


play sound sfx_rustling

"Sekunden später bindet etwas meine Hände an den Gelenken aneinander, und ich verfalle in Panik, weil ich nicht weiß,was ich davon halten soll."
"Mein erster Gedanke ist Shizune zu fragen, was sie sich dabei denkt. Auch wenn sie mich nicht hören kann, bin ich sicher, dass sie das Wesentliche verstehen wird."


"Widerwillig, meine Hände loszulassen, fährt sie mit ihren Fingern über sie. Von den Linien meiner Handflächen über meine Knöchel bis zu meinen Handgelenken."


scene evh shizune_hcg_tied_stare onlayer master:
    yalign 0.0 xalign 1.0 subpixel True
    easein 6.0 xalign 0.5 zoom 0.5
    truecenter
    zoom 1.0
    "evh shizune_hcg_tied_stare_small"
with whiteout

play music music_heart fadein 5.0

hi "Hey, was tust du da? Was soll das?"


"Natürlich hätte ich mit meinen Händen hinter dem Rücken genau so gut geknebelt sein können. Ein Teil von mir kann nicht anders als zu denken, dass das ihre Absicht war."


scene evh shizune_hcg_tied_smile_small onlayer master
with charachange

"Als ob sie meine Gedanken lesen würde, taucht ein verschmitzter Ausdruck auf ihrem Gesicht auf, aber die Röte bleibt. Eigentlich intensiviert sie sich noch, als sich unsere Augen treffen."


"Verlegen lehnt sie sich tiefer in unsere partielle Umarmung und versteckt ihr Gesicht zwischen meiner Schulter und meinem Hals."
"Ihr Haar ist weich und kitzelt mich. Mit dem Wissen, dass sie mich nicht hören wird; nicht beleidigt sein wird, lasse ich ein kleines Lachen heraus."


label de_S22h:

scene evh shizune_hcg_tied_blush_small onlayer master
with charachange

"Shizunes Hände bewegen sich abwärts zum Reißverschluß meiner Hose, bedeckt von ihrem Rock. Ihre Hände verschwinden aus meinem Blick, nur um bei der Berührung meiner Erektion zurückzuschnellen."
"Sie fällt fast vor Nervosität von mir herunter. Es ist, als hatte sie nicht erwartet, dass sie da ist."


"Die plötzliche Zurschaustellung von Naivität ist bis jetzt der stärkste Kontrast dazu, wie draufgängerisch sie bisher war."
"Ich finde es lustig. Auf einmal scheint sie wieder sehr unreif. Ein Oberschulmädchen, das die Rolle einer aggressiveren Frau spielt."


scene evh shizune_hcg_tied_blush onlayer master:
    yalign 0.0 xalign 0.8
show evh_hi shizune_hcg_tied_hisao2 onlayer master:
    yalign 0.0 xalign 0.8
with flash

"Sie stupst meinen Penis neugierig mit ihrem Zeigefinger an. Und während sie mit ihren restlichen Fingern den Schaft hinabfährt, wird ihr Gesicht immer roter. Ihre Bewegungen sind zart, neugierig und passen nicht zu ihrem verlegenem Blick."


show evh shizune_hcg_tied_stare onlayer master
hide evh_hi onlayer master
with charachange

"Es ist wahrscheinlich, dass Shizune genauso nervös ist wie ich, daher bin ich etwas erleichtert, als sie mit ihrem erkundenden Stupsen aufhört. Doch dann muss ich daran denken, was als nächstes passieren könnte."


"Sie könnte versuchen, die Knöpfe meines Hemdes zu öffnen. Wer weiß, was sie sagen würde, wenn sie die Narbe auf meiner Brust sieht."
"Ich bin mir dessen immer noch bewusst, und ich kann mir die Sorge auf ihrem Gesicht vorstellen, nachdem sie sie gesehen hat – und wie sie gedankenverloren ihre Fingerspitzen zusammenlegt."



"Glücklicherweise kann sie mir meinen Pullunder in dieser Position nur ausziehen, wenn sie ihn mir vom Leib reißt. Die Angst verschwindet aus meinen Gedanken. Jetzt verspüre ich nur eine unangenehme Mischung aus Vorfreude und Nervosität."


show evh shizune_hcg_tied_blush onlayer master
with charachange

"Eine neue Leichtigkeit auf meinen Knien bringt mich in die Realität zurück. Ich sehe, wie Shizune auf ihren Zehenspitzen steht, um ihre Unterwäsche ihre Schenkel herunterzuziehen."
"Als sie sieht, dass ich sie ihr dabei zusehe, versucht sie, meine Augen mit einer Hand zu bedecken."


"Ich frage mich, wann genau es anfing, dass ich von ihr angezogen wurde. Nicht nur körperlich, sondern vollkommen zu ihr hingezogen."
"Und ich frage mich warum. Sie ist hübsch, aber auch sehr kampflustig. Nicht nur das – sie scheint sich auch sehr wohl in ihrer Haut zu fühlen."


scene evh shizune_hcg_tied_blush_small onlayer master
with charachange

"So oder so, die Art, wie sie sich gerade verhält, passt nicht wirklich zu diesem Image. Ich bekomme langsam den Eindruck, dass sie meine Hände für mehr als nur die offensichtlichen Gründe verbunden hat."


"Trotzdem hat sie diese Aufdringlichkeit, die sie wie eine Visitenkarte in der Gegend verteilt."
"Ich weiß nicht, ob man diese Einstellung als gefährlich ansehen könnte oder nicht. Wenn ja, dann frage ich mich, was für eine Art von Mensch das aus mir macht."


hi "Es war wahrscheinlich in der ersten Woche, in der ich hier war. Wenn ich darüber nachdenke, hört sich eine Woche gar nicht so lange an, aber damals war es das."
hi "Auch wenn ich in dieser Woche dachte, dass meine Tage gezählt wären, schien die Zeit trotzdem sehr langsam zu vergehen."


"Selbst wenn sie mich nicht hören kann, fühle ich mich dabei wohl."


hi "Ich fing an zu begreifen, dass ich nicht viel hatte, worüber ich mich beschweren konnte. Aber da ist immer noch…"


hi "Ach, schon okay."


scene evh shizune_hcg_tied_stare_small onlayer master
with charachange

"Sie wirft mir einen Blick zu, als sie bemerkt, dass ich rede. Da sie nicht verstehen kann, was ich sage, wird sie zunehmend nervös, doch sie gebärdet keine Erwiderung."


scene evh shizune_hcg_tied_close_small onlayer master
show evh_hi shizune_hcg_tied_hisao2_small onlayer master
with charachange

"Shizune saugt scharf ihren Atem ein, als sie sich langsam auf meinen Penis herabsinken lässt und versucht, sich aufrecht zu halten, während sie auf mir wippt. "


"Der Rock ihres Kleides bedeckt unsere Intimbereiche und hält unsere Körperwärme wie unter einem Zelt gefangen. Unter ihm ist mir unerträglich heiß, und Shizunes Hand, die mich in sie führt, trägt auch noch dazu bei."


show evh shizune_hcg_tied_kinky3_small onlayer master
with flash

"In dem Augenblick, in dem ich in sie eindringe, zuckt sie zusammen und fällt fast auf mich. Das plötzliche Gefühl ist atemberaubend, und ich spüre Wellen der Lust, die mich von beiden Körperenden durchstrahlen."


"Es fühlt sich an, als ob mein ganzer unterer Körper in die Wärme und Feuchtigkeit von Shizunes Körper eingehüllt wäre. Als sie anfängt, sich zu bewegen, kann ich jedes Zucken und Zittern von ihr spüren."


show evh shizune_hcg_tied_kinky2_small onlayer master
with charachange

"Sie fängt an, ihre Hüften rhythmisch vor- und zurückzubewegen. Erst langsam, doch mit jeder Bewegung erhöht sich ihr Tempo, sodass sie sich fast von mir hebt und in der letzten Sekunde zurückfällt."


scene evh shizune_hcg_tied_kinky2 onlayer master:
    zoom 1.0 yalign 0.1 xalign 0.7
    acdc_warp 6.0 xalign 0.9
with flash

"So nahe wie ich ihr bin, kann ich ihre Schweißperlen und den Nebel auf ihrer Brille sehen, der entsteht, wenn sie ihre Nase herunterrutscht und zu nah an ihren Mund kommt, bevor sie sie wieder hochschiebt."


"Ihre Fingerspitzen drücken sich in meine Schultern, als sie sich an ihnen festhält und auch gleichzeitig von mir wegdrückt. Dann wandern sie meine Arme hinab und greifen nach meinen Handgelenken, als sie sich wieder herabsinken lässt."


scene evh shizune_hcg_tied_close_small onlayer master
with flash

"Sich so zu herumzumanövrieren ist bestenfalls schwierig. Shizune versucht, sich gegen mich zu stützen, während sie sich selbst mit ihren Füßen auf und ab bewegt."
"Ich versuche sie zu küssen, aber schaffe es gerade mal, dass unsere Köpfe zusammenstoßen – wenigstens nicht schmerzhaft."


"Ich frage mich, ob die Tür abgeschlossen ist oder nicht. Wenn sie sich jetzt öffnen würde, würde mir wahrscheinlich wortwörtlich das Herz stehenbleiben. Und dann ist da noch die Frage, wer die Tür öffnen würde."


"Das Gefühl von Gefahr macht Shizunes Bewegungen nur noch quälender für mich, und ich wünschte, sie würde schneller werden. Doch in dieser Position ist das vielleicht gar nicht möglich."


show evh shizune_hcg_tied_kinky1_small onlayer master
show evh_hi shizune_hcg_tied_hisao2_small onlayer master
with charachange

"Ich beginne damit, meine Hüften im gleichen Rhythmus wie sie zu bewegen und versuche so, tiefer in sie einzudringen."
"Es interessiert mich nicht, dass dadurch der Stuhl, auf dem wir sitzen, anfängt zu wackeln. Durch das Schlagen des Stuhls auf den Boden entsteht ein lautes Klopfen."


$ ksgallery_unlock("evhul shizune_hcg_tied_hisao2_small")
show evh shizune_hcg_tied_kinky3_small onlayer master
with charachange

shi "… Ngh…"


"Ihr Atmen wird lauter, und sogar etwas wie ein ersticktes Stöhnen entspringt ihrem Hals. Auch wenn es offensichtlich ist, dass sie es zurückhalten will, ist sie laut genug, dass jeder, der draußen vor Tür steht, sie hören könnte."


"Ich stoppe meine Stöße; zum Teil weil es schwieriger wird mitzuhalten, da sie sich immer mehr hineinsteigert und sich schneller bewegt, als ich unter ihr mithalten kann."


window hide

play sound sfx_heartslow
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.4)

window show

"Mein Herz rast so schnell, dass ich fast hören kann, wie das Blut in meinen Schläfen pocht."
"Und was noch beunruhigender ist: Ein dumpfes Klopfen in meiner Brust. Meine Gedanken schweifen von dem Druckgefühl zwischen meinen Schenkeln ab, wenn auch nur für einen Augenblick."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene white onlayer master
with whiteout

"Doch dieser Augenblick war genug. Zusammen mit dem Gefühl des von ihr Umschlungenseins und dem Aneinanderreiben unserer Haut, verkrampfe ich und feure in Shizune ab. Ein flüchtiges Gefühl von Kraft und Leichtigkeit."


label de_S22x:

$ renpy.music.set_volume(1.0, 2.0, channel="music")
$ renpy.music.play(music_heart, fadein=2.0, if_changed=True)

scene evh shizune_hcg_tied_close onlayer master:
    yalign 0.1 xalign 0.8
show evh_hi shizune_hcg_tied_hisao2 onlayer master:
    yalign 0.1 xalign 0.8
with Dissolve(2.0)

"Anschließend lausche ich dem Geräusch meines Herzens, wie es langsamer wird, bis es wieder seinen normalen Rhythmus erreicht. Shizunes Atem klingt, als würde er das gleiche tun."


hide evh_hi onlayer master
with charachange

"Ihre Brille liegt leicht schief, und es ist das erste Mal, dass sie nicht mit ihr herumspielt. Ich will sie für sie richten, aber als ich es versuche, werde ich daran erinnert, dass ich nicht kann. Shizune scheint es auch vergessen zu haben."


stop music fadeout 7.0

scene evh shizune_hcg_tied_close_small onlayer master:
    truecenter
    subpixel True zoom 1.2
    easein 10.0 zoom 1.0
with Dissolve(2.0)

"Anstatt aufzustehen presst sie sich gegen mich in den Stuhl, um ihre Reichweite zu verlängern. Es ist fast, als wäre das die einzige Position, die ihr einfällt, um meine Hände loszubinden."


"Allerdings steht sie nicht von mir auf. Ihre Finger berühren sanft die meinen, wobei sie gelegentlich mit den Fingerspitzen über meine Handfläche fährt. Es ist komisch, aber durch diesen schlichten Akt fühle ich mich ihr verbundener als zuvor."


"Shizune bleibt eine Weile so an mich gelehnt. Es ist etwas unbequem, aber es macht mich glücklich. Ich könnte stundenlang so bleiben."


scene black onlayer master
with dissolve

label de_S23:

scene bg shizu_guesthisao onlayer master
with locationchange

play music music_daily fadein 0.5

"Seitdem sind die Tage so schnell vergangen, dass sie sich wie Wasser anfühlten, das durch meine Finger rinnt."
"Jedes Mal, wenn ich versucht habe, mit Shizune zu reden, war sie shoppen oder mit Misha zusammen. Es kommt mir vor, als würde sie mir aus dem Weg gehen."


"Es überrascht mich nicht. Natürlich macht es mir Sorgen, aber ich finde, dass sie sich ziemlich normal verhält. Andererseits bin ich noch nie in so einer Situation gewesen."


scene bg shizu_living onlayer master at left
show mishashort perky_smile_cas onlayer master at center
with locationskip

"Immer wenn ich Shizune nicht finden kann, stoße ich auf Misha. Und dann bitte ich sie, mir beim Gebärden weiterzuhelfen. Allerdings windet sie sich am Schluss immer heraus."
"Nach dem heutigen Tag fahren wir zurück, darum bin ich entschlossen, sie diesmal nicht entwischen zu lassen."


"Sobald wir wieder zurück in der Schule sind, werden wir wegen des bald wieder beginnenden Schulbetriebs anfangen müssen, uns mehr um Schülerratsarbeiten zu kümmern."
"Bis dahin will ich meine Zeichensprache-Fähigkeiten so gut wie möglich aufpolieren, wenn auch nur für einen Tag."


hi "Komm schon, es sind doch nur paar Unterhaltungen in Zeichensprache! Du machst das die ganze Zeit. Sogar jetzt."


show mishashort cross_laugh_cas onlayer master
with charachange

mi "Wahaha~, wirklich, Hicchan? Das ist komisch!"


"Misha stoppt kurzzeitig ihr unbewusstes Gebärden, um mit ihren Händen eine abweisende Geste machen zu können, doch dann nimmt sie es rasch wieder auf und gebärdet alles, was wir beide sagen, ohne es wirklich an jemanden zu richten."


show mishashort sign_confused_cas onlayer master
with charachange

mi "Hicchan, du bist so hartnäckig. Dich so plötzlich wieder für Zeichensprache zu interessieren… Kann es sein, dass Hicchan das zum Beruf machen will? Das ist nicht fair, ich hatte die Idee als Erste~!"


show mishashort cross_frown_cas onlayer master
with charachange

mi "Du solltest vorsichtig sein, Hicchan. Zeiten ändern sich schnell~…"
mi "Bis ich mich dazu entschieden hatte, dass ich eine Zeichensprache-Übersetzerin werden will, hatten sie Handys rausgebracht, auf denen man ganze Absätze abtippen konnte. Unglaublich~! Auch wenn es für mich nicht wirklich gut ist!"


"Als ob sie weiß, dass eine weitere Verschiebung diesmal nichts bringen wird, wird Mishas Ton ziemlich schnell rechtfertigend."


show mishashort perky_sad_cas onlayer master
with charachange

mi "Tut mir leid, Hicchan, ich bin nur so~ müde~! Besonders in letzter Zeit. Auch wenn es Spaß macht, mit Shicchan unterwegs zu sein – sie hat viel mehr Energie als ich!"
mi "Darüber hinaus noch zu Unterrichten wäre zu~ anstrengend; so viel Ausdauer hab ich nicht! Sorry~!"


"Sie wirkt nicht sehr müde, da sie ihre Behauptung mit ihrer üblichen Fröhlichkeit und dem gewohnten Elan tönt. Ich weiß aber auch, dass es falsch von mir ist, sie so zu drangsalieren."


show mishashort sign_smile_cas onlayer master
with charachange

mi "Eigentlich~ hatten Shicchan und ich vor, heute shoppen zu gehen! Es ist unsere letzte Gelegenheit, noch ein paar Souvenirs mitzunehmen."


hi "Souvenirs, was? Ich hab fast vergessen, dass ich im Urlaub bin."


hi "Ich verstehe, was du meinst. Zu unterrichten scheint nicht so einfach zu sein. Hidaeki hat mich neulich gebeten, ihm etwas beizubringen, und ich wusste die ganze Zeit nicht, wie ich das angehen soll."


hi "Na ja, mal sehen, wie es für dich läuft, wenn du eine Zeichensprache-Lehrerin geworden bist. Dann darfst du auch nicht so schnell müde werden."


show mishashort perky_confused_cas onlayer master
with charachange

mi "Ja, richtig, richtig~! Ich hoffe nicht!"


show mishashort hips_smile_cas onlayer master
with charachange

mi "Hicchan, jetzt bin ich irgendwie besorgt. Aber~ – Souvenirs! Darum~ ein anderes Mal, Hicchan. Aha hahaha~. Sollen wir dir auch etwas mitbringen?"


"Nur weil ich es verstehe, heißt das nicht, dass ich nicht mehr will, dass sie mich unterrichtet. Aber ich schätze, ich kann sie fürs Erste wohl nicht weiter bedrängen. Sogar ich begreife, wie egoistisch das wäre. Ich gebe auf."


hi "Nein. Das braucht ihr nicht. Ich mein's ernst, überrascht mich nicht mit einem komischen Shirt oder so was, okay?"


show mishashort cross_grin_cas onlayer master
with charachange

mi "Heheheh~."


"Dieses Lachen gefällt mir gar nicht."


hide misha onlayer master
with charaexit

"Sie schlüpft in ihre Schuhe, schreit einen Abschiedsgruß in das sonst leere Haus und öffnet die Tür, um loszugehen, wodurch ein frischer Luftzug durch den Flur weht."
"Ein Büschel dunkler Haare auf der anderen Seite der Tür verrät mir, dass Shizune draußen auf sie wartet."


hi "Guten Morgen."


show mishashort invis onlayer master:
    center
    xpos 0.8
show shizu invis onlayer master:
    center
    xpos 1.0
with None

show bg shizu_living onlayer master at right
show shizu adjust_happy_cas onlayer master at tworight
show mishashort perky_smile_cas onlayer master at center
with Dissolvemove(2.0)

"Misha übersetzt für mich von der anderen Seite des Eingangs, und Shizune dreht sich um, um mir kurz zuzuwinken."


"Obwohl es kaum anders als ihre üblichen, flapsigen Begrüßungen ist, ist da ein unverkennbares Zögern. Es lässt mich mit einem vagen Gefühl der Leere und Distanziertheit zurück."


show shizu behind_blank_cas onlayer master
with charachange

shi "…"


show mishashort hips_grin_cas onlayer master
with charachange

mi "Hicchan, du bist früh wach~! Störe ich gerade?"


hi "Ich hab versucht, Misha dazu zu bringen, mir zu zeigen, wie man mit dir redet. Aber ich schätze, ich bin ungeduldig gewesen – es kann warten. Ihr Zwei hattet ja vor heute shoppen zu gehen."


"Weil Misha da ist, vergesse ich, die Worte zu gebärden, während ich sie sage. Leider steht Misha hinter Shizune, da diese sich in die Tür gestellt hat. Diese unglückliche Anordnung bedeutet, dass so gut wie alles an ihr vorbeigegangen ist."


show shizu basic_angry_cas onlayer master
with charachange

ssh "Ich verstehe dich überhaupt nicht."


"Es gibt Dinge, die ich sagen will, aber nicht so formulieren kann, dass sie es versteht. Und es gibt ganze Unterhaltungen, die sie führen könnte und die komplett an mir vorbeigehen würden."
"Jetzt will ich ihr sagen, dass es nicht mehr allzu lange so sein wird."


hide shizu onlayer master
hide mishashort onlayer master
with charaexit

"Stattdessen sage ich lediglich „schon okay” und wünsche ihnen viel Spaß, dann verabschiede ich sie."


"Es sieht aus, als wären heute alle außer Haus, also setze ich mich mit einem Buch auf den größten und gemütlichsten Sessel im Wohnzimmer."
"Kein Zeichensprache-Buch, sondern einer der Romane, die ich in meiner ersten Woche aus der Bibliothek ausgeliehen habe."


"Das ist so lange her. Ich sollte wirklich damit anfangen, mich durch diesen Bücherstapel durchzuarbeiten, oder sie zumindest zurückbringen."


stop music fadeout 2.0

show jigoro neutral onlayer master at center
with charaenter

"Nach sechzehn Seiten kommt Jigoro ins Zimmer, in der einen Hand einen Stapel Papier und in der anderen sein Schwert, das er wie einen Taktstock herumwirbelt."
"Zwischendurch schüttelt er etwas Wasser von seinem vorangegangenen Duschgang aus den Haaren."


show jigoro angry onlayer master
with charachange

show jigoro angry onlayer master at Position(ypos=1.15)
with charamove

"Da habe ich ihn wohl bei etwas erwischt, was er als „unfein” bezeichnen würde."
"Zuerst erstarrt er wie ein Reh im Scheinwerferlicht, dann sehe ich, wie eine mächtige wenn auch grundlose Wut in ihm aufglüht, und er setzt sich einen Meter entfernt von mir auf die Couch."


"Das ist gerade das dritte Mal, dass ich ihn getroffen habe, und mir wird schon aus Reflex übel. Ich schätze, man könnte das als eine Art Charisma bezeichnen."


"Ich habe nicht einmal etwas gesagt, und er wirkt schon unerfreut. Es ist wahrscheinlich eine schlechte Idee, ihn zu provozieren, und allein ihn anzusprechen könnte schon als Provokation gewertet werden."
"Aber ich muss die ganze Zeit an die alternativen Szenarien denken, die sich abspielen könnten."


"Sagen wir, ich halte die Klappe und gehe weg, eventuell zum Lesen in mein Zimmer oder nach draußen."
"Das würde definitiv als unverzeihliche Beleidigung rüberkommen. Wahrscheinlich würde er mich zurückrufen und zerstören. So oder so wäre es unhöflich von mir."


hi "Was lesen Sie da?"


show jigoro smug onlayer master
with charachange

play music music_another fadein 6.0

hx "Den Entwurf meiner Autobiographie. Es ist die Geschichte eines Mannes, der aufwacht, um einen ungeladenen Gast in seinem Wohnzimmer vorzufinden, der auf seinem Sessel sitzt und oberflächlichen literarischen Dreck liest."


"Ich habe gerade mal mit dem Buch angefangen. Nicht einmal eine Meinung konnte ich mir bilden. Ich kann bereits sehen, wie diese Unterhaltung ablaufen wird, also kann ich sie genauso gut in eine andere Richtung lenken."


hi "Wo ist Hideaki?"


show jigoro angry onlayer master
with charachange

hx "Du stellst sogar unverschämt fragen. Erbärmlich. Abgesehen davon, warum würdest du mir überhaupt so eine dumme Frage stellen? Woher soll ich das wissen? Bin ich der Wärter meines Sohnes?"


"„Nun, Sie sind sein Vater, und es scheint, als würde er hier leben, also…” Aber ich schätze, das kann ich nicht sagen – so verlockend es auch sein mag."


"Ich gebe auf. Ich habe schon versucht, mit ihm eine Unterhaltung zu führen, und es ging schief."
"Es ist, als würde man versuchen, mit einer Mauer zu reden, die einen darüber hinaus auch noch hasst. Das ist mein Stichwort zu gehen und in mein Portemonnaie zu sehen, ob ich noch genug Geld für einen Kinobesuch habe."


"Als ich gerade aufstehen will, überdenke ich das noch einmal. Ich bin das permanente Fliehen vor problematischen Situationen leid."


"Es wäre heuchlerisch von mir, auf Misha sauer zu werden, weil sie Dinge aufschiebt, wenn ich sogar vor meiner eigenen Freundin davonlaufe. Als Jigoro versucht mich aufzuhalten, bin ich fast froh darüber, auch wenn ich nicht länger vorhabe zu gehen."


show jigoro neutral onlayer master
with charachange

hx "Warte."


"Er sagt das mit immenser Autorität, aber darauf folgt nichts – als ob es nur ein besonders befehlender Nebengedanke wäre."
"Nur ein sehr mächtiger oder sehr arroganter Mensch kann jemanden auf diese Weise zum Warten auffordern. Ich bin irgendwie beeindruckt."


show jigoro smug onlayer master
with charachange

hx "Du bist mit Shizune im Schülerrat, nicht wahr? Was ist dort deine Aufgabe?"


hi "Ich denke nicht, dass wir da spezielle Rollen haben, abgesehen vom Präsidenten. Shizune versucht immer Leute zusammenzutrommeln, um hier und da auszuhelfen."
hi "Normalerweise können wir den einen oder anderen zum mitmachen bewegen, aber anderenfalls kümmern wir drei uns um alles, was so ansteht."


"Als ich sie noch nicht so lange kannte, dachte ich, dass Shizunes beunruhigendes, analytisches Starren von ihrer Taubheit kommen könnte, aber es sieht so aus, als ob sie diesen Charakterzug mit jedem in ihrer Familie teilt."


show jigoro neutral onlayer master
with charachange

hx "Und damit bist du einverstanden?"


hi "Warum sollte ich es nicht sein?"


show jigoro laugh onlayer master
with charachange

hx "Du, Shizune und das Mädchen mit den rosa Haaren? Ist das wirklich euer gesamter Schülerrat?"


show jigoro smug onlayer master
with charachange

hx "Mit so einem kleinen Schülerrat würden sie sich nicht einmal die Mühe machen, Wahlen abzuhalten."
hx "Ich rate einfach mal und sage, dass du dem Schülerrat nicht beigetreten bist, sondern dass Shizune dich eingezogen hat. Du sagtest, dass du nicht genau weißt, was dein Titel ist."


hx "Das ergibt Sinn. Ich nehme an, wenn du nicht einmal gewählt wurdest, kannst du es auch gar nicht wissen. Schließlich ist man nicht wirklich etwas, wenn man nicht gewählt wurde."


show jigoro laugh onlayer master
with charachange

hx "Niemand wird so einen Schülerrat respektieren. Eine nicht gewählte Gruppe aus drei Leuten, die versuchen, so etwas wie Teilzeitarbeiter zu erbetteln?"
hx "Es muss eine klägliche Schule sein, wenn drei Kinder bei einer Teeparty alle Probleme handhaben können."


hi "Was hat die Größe damit zu tun? Reicht es nicht, wenn der Schülerrat seine Aufgaben erledigt?"


hi "Und ein Spiel ist es auch nicht. Vielleicht sollten Sie wirklich mal für einen Tag zur Schule kommen. Wenn Sie an den richtigen Tagen kommen, können Sie eventuell sogar sehen, was Shizune alles erreichen kann."


show jigoro angry onlayer master
with charachange

hx "Glaubst du, dass ich so viel Freizeit habe, dass ich mir einen Ausflug in euer Hinterland leisten und meiner Tochter bei ihren Selbstverherrlichungskunststücken zusehen kann? Ich bin in meinem Leben noch nie so angewidert gewesen."


hi "Sie meinen, dass sie genauso gut auf einen Schülerrat verzichten könnten, aber die Tatsache bleibt, dass es einen gibt. Und Shizune wurde dafür gewählt – und für sie ist es keine bedeutungslose Position. Sie arbeitet sehr hart dafür."


show jigoro laugh onlayer master
with charachange

hx "Du klingst wie jemand, der für sie gestimmt hat."


hi "Nein, zu jener Zeit war ich noch nicht da."


show jigoro neutral onlayer master
with charachange

hx "Ha. Du hast nicht einmal für sie gestimmt. Na ja, abgesehen davon: Warum fragst du nicht Hideaki danach?"


show jigoro smug onlayer master
with charachange

hx "Shizune wollte seit der Mittelschule eine Oberschul-Schülerratspräsidentin werden. Sie hat ihn all ihre Übungsreden lesen lassen und damit seine Zeit verschwendet. Und wofür?"


"Die ganze Zeit über hat er nicht einmal von seinem Manuskript aufgesehen. Es wird zunehmend frustrierender."


hi "Weil es kein Spiel ist; wir leiten die Schule nicht, aber es ist auch nicht so, als würden wir nur herumalbern und es nicht ernst nehmen."


"Ich frage mich, ob es falsch ist, kein Purist zu sein."


show jigoro angry onlayer master
with charachange

hx "Ich bin in deiner Schule gewesen. Wirklich… die Schüler dort…"


"Mir fallen bereits Millionen Dinge ein, die er sagen könnte, und ich bin darauf vorbereitet, dass mir bei jedem davon mein Herz in die Hose rutschen könnte. Es ist lustig, denn wahrscheinlich sind es Dinge, die ich zuvor selbst gedacht habe."


hx "Sie haben nicht einmal Putzdienst."


"Das war alles andere als erwartet. Und Unrecht hat er auch."


hi "Haben sie. Ich muss es wissen, denn ich bin durch den Schülerrat davon befreit."


show jigoro neutral onlayer master
with charachange

"Das Konzept des Irrtums verwirrt Jigoro. Ich sollte die Gelegenheit ergreifen und in die Offensive gehen. Es ist wirklich ungewöhnlich, dass ich so über eine simple Unterhaltung denke."


hi "Es klingt, als wäre es ziemlich lange her, seit Sie das letzte Mal da waren."


hi "Wenn Sie gemächlich ihre Memoiren schreiben können, können sie auch ab und zu mit Shizune reden. Meinen Sie nicht, dass sie Dinge hat, auf die sie stolz ist?"


hi "So sind junge Leute. Wir haben Dinge, auf die wir stolz sein können. Wenn Sie eine Autobiographie schreiben, sollten sie das verstehen."


"So eine gute Gelegenheit, und ich hab sie vermasselt."
"Ich weiß nicht, was für eine Reaktion ich von ihm erwartet habe. Vielleicht Selbsteinsicht; doch Jigoro wird im Sekundentakt zusehends wütender. Dennoch wirkt er dabei irgendwie ruhiger – selbstsicherer und selbstbeherrschter."


show jigoro angry onlayer master
with charachange

hx "Was glaubst du wer du bist, dass du mein Leben als leicht bezeichnen kannst?"
hx "Du hast nicht einmal meine Biographie gelesen, dennoch willst du mir vorschreiben, wie ich alle meine Angelegenheiten zu regeln habe, einschließlich den Umgang mit meiner eigenen Tochter. Du könntest das niemals verstehen."


hx "Selbst wenn ich jetzt von dieser Couch aufstehen und dir mit einem Schlagring die Kurzfassung meiner Lebensgeschichte auf die Stirn stanzen würde… Selbst dann würdest du es nicht verstehen."


hx "Zwölf Jahre lang hat Shizune nicht ein Mal mit mir gesprochen, obwohl ich mehrere Privatlehrer und Übersetzer aller Art engagiert habe, um sie wieder normal zu bekommen. Es ist nicht so einfach wie du denkst."


show jigoro smug onlayer master
with charachange

hx "Wenn sie sich nicht mit mir abgeben will, dann sei es so. Ich vermute, das ist normal. Wann hast du das letzte Mal mit deinen Eltern gesprochen?"


"Das ist schon eine Weile her, und ich schäme mich dafür."
"Mehr weil er mich erwischt hat als weil es ganz einfach gewesen wäre, sie anzurufen oder ihnen eine E-Mail oder sogar einen Brief zu senden und ich es trotzdem nicht getan habe. Dieses Erkenntnis steigert die Scham nur noch mehr."


show jigoro laugh onlayer master
with charachange

hx "Dachte ich mir."


hi "Auch wenn ich meine Eltern besuchen wollte – ich könnte es nicht. Bei Ihnen ist das anders. Sie wohnen nicht allzu weit weg von ihr, es ist gerade mal eine Zugfahrt!"


show jigoro neutral onlayer master
with charachange

hx "Das reicht. Nein heißt nein. Du bist sehr hartnäckig. Wenn es wenigstens wegen etwas Wichtigem wäre. Ich sehe nicht, was du von meiner Tochter gelernt haben könntest, außer wie man unverschämte Antworten gibt. Ist es das?"


stop music fadeout 10.0

"Die Antwort ist ja. Bevor ich Shizune und Misha traf, war ich nicht so hartnäckig und streitlustig. Immerhin hatte ich einen kleinen Tod erlebt, bevor ich sie traf. Es ist mir ein Rätsel, warum ich am Anfang gegen einen Beitritt im Schülerrat war."



label de_S23a:

"Schon mich am ersten Tag vorzustellen hat mich viel Überwindung gekostet. Wahrscheinlich hätte ich allem und jedem nachgegeben. Es war wohl nur Zufall, dass der Schülerrat für mich so uninteressant war, dass ich mich gegen den Beitritt gewehrt habe."



label de_S23x:

"Ich habe damals andauernd versucht, ihren Rekrutierungsversuchen zu entkommen. Vielleicht hat mir das geholfen, meine Energie zurückzugewinnen. Eine schöner Gedanke."


"Ich stelle mir noch einmal die Frage, warum ich noch hier bin. Mit Jigoro zu streiten ist zwecklos, dennoch glaube ich, dass ich mich fast darauf gefreut habe."
"Und er hat Recht: Ich kann ihn nicht verstehen. Selbst wenn – es würde ihn nicht kümmern. Ich bin eine Laus, die auf einem Wal kriecht – vollkommen bedeutungslos."


"Er hat die Selbstsicherheit, die mir fehlt. Shizune hat sie, und vielleicht ist der Grund warum ich jetzt hier bin und beinahe ihren Vater anschreie, weil ihr Mut auf mich abgefärbt hat. Jedoch habe ich nicht die Energie, das aufrecht zu erhalten."


"Trotzdem hasse ich ihn. Ich weiß nicht, was ich tun kann."
"Vor ein paar Monaten noch hätte ich ihn wahrscheinlich eine reingehauen und den Dingen ihren Lauf gelassen. Aber jetzt kann ich das nicht mehr riskieren. Falls er zurückschlagen würde, würde er mich damit bestimmt umbringen."


"Schlussendlich kann ich nichts tun, außer Jigoro stumm anzustarren. Ich weiß, dass ich keine Antwort für ihn habe, dass ich ihn hasse und dass ich mich hilflos fühle. Seltsamerweise interpretiert er das als Trotz."


show jigoro angry onlayer master
with charachange

hx "Hmpf. Na schön. Viel Spaß damit."


show jigoro invis onlayer master at center
with dissolvecharamove

"Er benutzt sein Schwert als Stütze, um auf die Beine zu kommen, dreht sich um und schlendert lässig aus dem Zimmer."
"Ich will mein Buch nach ihm werfen, aber ich bin froh, dass ich endlich allein bin – auch wenn ich nicht länger in der Stimmung bin, etwas zu lesen."


scene black onlayer master
with dissolve

label de_S24:

scene bg city_station onlayer master
with locationchange

"Unsere Rückreise zur Schule verzögert sich wieder und wieder. Erst kommen Shizune und Misha so spät zurück, dass zurückzufahren keinen Sinn mehr macht und wir einen weiteren Tag bleiben."


"Am Morgen danach verpassen wir den Zug um eine Minute, und die nächsten zwei kommen erst gar nicht. Den vierten verpassen wir, weil ich zwischendurch etwas zu Trinken holen gegangen bin. Shizune ist nicht sehr erfreut darüber."


scene bg school_dormhisao onlayer master
with shorttimeskip

play music music_dreamy fadein 2.0

"Als ich endlich wieder zurück in meinem Zimmer bin, bin ich vollkommen erschöpft, obwohl ich während der Rückfahrt die meiste Zeit geschlafen habe."
"Ich kann nicht behaupten, dass es nur an dem heutigen Tag liegt; es scheint ein gängiges Reisesymptom zu sein. Das ist nicht zum ersten Mal passiert."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

scene black onlayer master
with shuteye

window show

"Wenn mir noch keiner zuvorgekommen ist, könnte ich eine wissenschaftliche Arbeit darüber schreiben und vielleicht in eine Medizin-Zeitschrift kommen."
"„Reise-Heimkehr-Syndrom”. Nicht sehr kreativ. Bevor mir ein besserer Name einfällt, schlafe ich ein."


window hide

play sound sfx_doorknock
with Pause(1.0)

scene bg school_dormhisao onlayer master
with openeye

$ renpy.music.set_volume(1.0, 1.0, channel="music")

window show

"Nach nur ein paar Stunden Schlaf weckt mich ein lautes Klopfen an der Tür bereits wieder."
"Da ich gerade mitten aus einem Traum gerissen wurde, bin ich ziemlich verärgert. Ich kann mich zwar nicht an ihn erinnern, aber ich bin mir sicher, dass es ein schöner war."


"Für einen kurzen Moment frage ich mich, wer es sein könnte, aber ich kriege nicht oft Besuch, darum wird es mit ziemlicher Sicherheit Kenji sein."
"Ich hoffe, er will mich einfach nur begrüßen und bettelt mich nicht wieder um Geld an. Wenn das der Fall wäre, wäre ich fast gerührt."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene black onlayer master
with shuteye

"Jedoch nicht gerührt genug, um den Drang zu widerstehen, mich umzudrehen und weiterzuschlafen."


stop music fadeout 5.0

window hide

with Pause(4.0)

scene bg school_dormhisao onlayer master
with openeye

window show

"Ein paar Stunden danach wache ich auf und entdecke sofort einen Umschlag auf dem Boden."


"Er muss mit der Post gekommen sein, während ich weg war. Das ist Shizunes und Mishas Abteilung, darum frage ich mich, ob sie vorbeigekommen sind, um ihn mir zu geben."
"Oder vielleicht ist jemand während ihrer Abwesenheit für sie eingesprungen und hat Kenji gesagt, dass er ihn weitergeben soll…"


show letter_insert onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_rain fadein 4.0

"Als ich ihn aufhebe, verschwinden augenblicklich alle Reste von Müdigkeit."


"Selbst wenn der Absender nicht darauf gestanden hätte, hätte ich durch den Umschlag selbst schon gewusst, von wem er ist – wegen der feinen Handschrift, mit der die Adresse geschrieben wurde."



"Er ist von Iwanako. Anfangs kann ich es nicht glauben, aber wenn sie mich finden wollte, wäre das sicher nicht allzu schwierig gewesen."


"Natürlich hätte ich nicht gedacht, dass sie es wollen würden. Wenn es hochkommt, war sie vielleicht fünf Sekunden lang meine Freundin. Danach haben wir kaum miteinander gesprochen."


show letter_insert onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide letter_insert onlayer master
with None

"Es wäre nur allzu einfach, diesen Brief irgendwo hinzulegen und ihn zu vergessen. Ein Teil von mir will das. Oder ihn ungelesen wegwerfen."
"Ich weiß nicht, warum ich diese Dinge tun will. Es wäre einfacher. Einfacher, als ihn zu lesen."


scene ev hisao_letter_open onlayer master
with locationchange

"Als ich den Umschlag mit der Spitze eines Kugelschreibers auftrenne, verblüfft mich die Länge des zum Vorschein kommenden Briefes."


$ renpy.music.set_volume(0.5, 1.0, channel="music")
window hide


$ written_note ("Lieber Hisao,\n\nWie geht es dir? Ich hoffe, dir geht es gut, und dir gefällt es an deiner neuen Schule. Alle hier vermissen dich. Fast unsere gesamte zweite Klasse ist nun zusammen in Klasse 3-1, also haben wir uns von Anfang an gut einfinden können. Ich bin sicher, du wärst auch in diese Klasse gekommen.")


$ written_note ("Im Moment sind alle Drittklässler schon sehr angespannt wegen der Abschlussprüfungen, obwohl es noch so lange hin ist. Die Lehrer liegen uns ständig damit in den Ohren – sogar der alte Herr Tachibana, der übrigens dieses Jahr unser Klassenlehrer ist. Hättest du das gedacht? Ich war mir sicher, dass er nach unserem zweiten Jahr in Pension gehen würde, aber er nervt immer noch alle wegen der Examen.\n")


$ written_note ("Ich glaube, das ist der Hauptgrund, warum alle Drittklässler so nervös sind. Ich muss zugeben, dass ich auch langsam mein Selbstvertrauen verliere, obwohl ich in Prüfungen bisher immer recht gut abgeschnitten habe.\n\n\n\n\n")


$ renpy.music.set_volume(1.0, 1.0, channel="music")

window show

"Dieser Smalltalk weckt Erinnerungen. Es ist fast, als wäre ich wieder im Krankenhaus. Hin und wieder kam Iwanako vorbei und erzählte mir das Wesentliche, was gerade in der Klasse vor sich ging."
"Sogar zu dieser Zeit hatte ich eine Ahnung, dass ich nie wieder zu ihr zurückkehren würde."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
$ written_note ("Es ist so seltsam, dass wir plötzlich die Ältesten sind, nicht wahr? Die Zeit ist so schnell vergangen. Ich frage mich, wo sie hin ist. Die neuen Erstklässler sehen so jung und irgendwie unschuldig aus. Ich frage mich immer wieder, ob ich in meinem ersten Jahr genauso war. Ich habe schon das ganze erste Trimester so ein nostalgisches Gefühl.\n\n\n")


$ written_note ("Es gibt noch andere Dinge, die ich dir sagen will. Ich schreibe dir, weil ich das Gefühl hatte, dass ich dir nach dem Vorfall im Winter noch vieles hätte sagen sollen. Ich bedaure wirklich, dass ich es dir nicht persönlich sagen konnte, und ich habe dafür keine Entschuldigung.\n\n\n\n\n")


$ written_note ("Die Wahrheit ist, immer wenn ich dich im Krankenhaus besucht habe, war ich sehr besorgt um dich. Ich rede nicht über deine Gesundheit. Du schienst dich immer mehr von mir zu entfernen und den Mut zu verlieren. Ich bin sicher, das ist ganz normal, nachdem so etwas passiert, aber irgendwie hatte ich das Gefühl, dass du damals irgendetwas aufgegeben hast. Glück, vielleicht?\n")


$ written_note ("Ich wollte irgendwie meine Gefühle zum Ausdruck bringen, aber ich habe einfach nicht die richtigen Worte gefunden. Ich konnte nichts sagen, um dich zu trösten. Es tut mir wirklich leid, dass ich dich nicht unterstützen konnte, als du mich am nötigsten gebraucht hast. Zumindest kann ich jetzt, nach so langer Zeit, ehrlicher sein.\n\n\n\n")


$ renpy.music.set_volume(1.0, 1.0, channel="music")

window show

"Was für ein passender Zeitpunkt, um ihre Aufrichtigkeit wiederzufinden. Na ja, auch wenn ich das denke, weiß ich, dass sie Recht hat. „Entfernen und den Mut verlieren” beschreibt es ganz gut. Und vielleicht hatte ich auch aufgegeben."


"Wenn ich an meine Zeit im Krankenhaus zurückdenke, spüre ich eine Last. Ich war so verbittert, als sie nicht mehr auftauchte. Ich war nicht überrascht, und ich hatte auch kein Recht dazu."
"Wie konnte sie nicht aufhören, mich zu besuchen, wenn es das einzige war, was ich von ihr erwartete?"


"Nach dem Vorfall hat sie mich gerade mal sechs Wochen lang besucht. Wenn ich mich von ihr entfernt habe, dann weil ich vom ersten Moment an gefühlt habe, wie sie sich von mir entfernt."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
$ written_note ("Wenn ich zu diesen stillen Tagen im Februar und März zurückkehren könnte, würde ich dir sagen, dass du dich nicht aufgeben sollst. Vielleicht hättest du dich nicht so weit von mir entfernt, wenn ich einfach nur etwas gesagt hätte. Ich hoffe, du hast es auch ohne mich geschafft, wieder auf die Beine zu kommen.\n\n\n\n")


$ written_note ("Jetzt, wo die Entfernung zwischen uns auch physisch ist, fühlt sich alles irgendwie endgültiger an. Ich frage mich, ob wir uns irgendwann einmal wiedersehen. Vielleicht wäre es besser, wenn nicht? Trotzdem, wenn du mir antworten willst, schreib mir bitte zurück. Ich würde wirklich gerne erfahren, wie es dir an deiner neuen Schule geht. Ich wünsche dir alles Gute.\n\nDeine Iwanako")


$ renpy.music.set_volume(1.0, 1.0, channel="music")

window show

"Es ist ein komisches Gefühl. Ich weiß, dass ich nie wieder etwas von ihr hören werde."


"Wenn sie wirklich in Kontakt bleiben wollte, hätte sie nicht ein Medium wie die Schneckenpost dafür ausgesucht."
"Wenn sie meine Adresse herausfinden konnte, dann wären meine E-Mail-Adresse oder Telefonnummer auch keine große Herausforderung gewesen, wenn sie sie gewollt hätte. Das ist lediglich ein Lebewohl."


stop music fadeout 4.0

"Ich atme aus und merke erst jetzt, dass ich mit angehaltenem Atem gelesen habe. Wer distanziert sich denn jetzt, Iwanako? Aber vielleicht ist es wirklich besser so."


"Dass sie einen Stift in die Hand nimmt und mir diesen Brief schreibt, kann nur heißen, dass sie Schuldgefühle hatte. Es erfüllt mich mit wehmütiger Zufriedenheit, dass unserer allmähliche, gegenseitige Entfremdung sie verletzt hat."


"Ich will ihr beinahe danken, und lasse es nur, weil ich weiß, dass sie nicht wollen würde, dass ich antworte."


play sound sfx_doorknock

scene bg school_dormhisao onlayer master
with locationchange

"Es klopft an meiner Tür, und trotzdem öffnet sie sich ungefähr eine Millisekunde später. Dummerweise habe ich vergessen sie abzuschließen."


ke "S'los, Mann? Warum is deine Tür offen?"


"Ich stürme schneller zur Tür, als wahrscheinlich aus medizinischer Sicht ungefährlich für mich wäre, um Kenji davon abzuhalten, die Berge an Tabletten zu sehen, die nur ein paar Meter von ihm entfernt liegen. Nur die Tür blockiert seine Sichtlinie."


"Darüber hinaus habe ich noch diesen Brief in der Hand. Falls er mich danach fragt, würde mir nichts Überzeugendes einfallen."


"Ungefähr einen halben Meter vor ihm fällt mir wieder ein, dass seine Sicht sowieso so schlecht ist, dass das wahrscheinlich nie Problem war. Er hat nicht einmal gesehen, wie ich praktisch kurz davor war, ihn zurück auf den Flur zu rammen."


scene bg school_dormhallway onlayer master
show kenji tsun_close onlayer master at center
with locationchange

play music music_kenji fadein 0.5

ke "Hey, was zur Hölle, Mann?"


hi "Wovon redest du? Dein Zimmer hat eine Milliarde Schlösser, trotzdem spazierst du einfach direkt durch anderer Leute Türen."


hi "Du hast nicht einmal eine Sekunde gewartet, bevor du versucht hast, die Tür aufzumachen. Es war quasi gleichzeitig. Schon beim Klopfen hast du die Tür aufgemacht."


show kenji happy_close onlayer master
with charachange

ke "Siehst du? Genau deswegen hab ich all diese Schlösser. Es ist eine kalte und harte Welt da draußen. Eine Welt voller ungebetener Gäste. Jetzt verstehst du es auch."


show kenji neutral_close onlayer master
with charachange

ke "Ich hab dir gerade eine wertvolle Lektion erteilt. Wissen ist Macht. Warum schreist du mich an? Ich bin ein Held."


show kenji tsun_close onlayer master
with charachange

ke "Sieh dich mal an… Du schließt nicht einmal deine Tür ab."
ke "Die durchschnittliche Frau hätte dich bereits eine Milliarde Mal umbringen und dich dann mit einem weiblichen Klon austauschen können, den man nicht vom Original unterscheiden könnte. Mir ist das fast schon passiert."


"Abgesehen von dem letzten, zu verwirrenden Teil ist es lustig, dass er so etwas sagt."
"Er war nicht in der Lage, mich davon abzuhalten ihn frontal zu rammen, doch eine Frau hätte mich anscheinend eine Milliarde Mal umbringen können. Wenn dieser Kerl ein Held ist, sind wir alle verloren."


show kenji happy_close onlayer master
with charachange

ke "Was hast du da?"


"Irgendwie kann er den Brief sehen, der immer noch in meiner Hand ist."
"So wie ich damit herumgewedelt habe, ist das auch kein Wunder. Ich falte ihn schnell zusammen, achte aber darauf, dass ich ihn nicht hinter meinem Rücken verstecke. Das wäre zu verdächtig."


"Es scheint, als wäre ich wegen Iwanakos Brief doch etwas nervöser, als ich gedacht habe."


hi "Ich hab einen Brief bekommen."


show kenji neutral_close onlayer master
with charachange

ke "Ah, ja, ich hab den dort hingelegt. Ich hab geschlafen, dann bin ich aufgewacht, weil ich Explosionen gehört hab."


ke "Ich hab mir meinen Helm aufgesetzt und dann draußen nachgesehen, was los war. Aber es war nur die Schülerrats-Frau, die an deine Tür gehämmert hat. Es war die ohne pinke Haare."


show kenji tsun_close onlayer master
with charachange

ke "Sie hat so laut geklopft; es war offensichtlich, dass sie mit mörderischem Zorn erfüllt war. Zorn auf dich."
ke "Dann hat sie mich irgendwie hinter sich bemerkt, und ich hab versucht zu fliehen, aber es war schon zu spät. Sie hat mich entdeckt und auf die Tür gedeutet."


"Ich war kurz davor ihm zu sagen, dass sie taub ist, entschließe mich aber, es nicht zu tun. Aus vielerlei Gründen."


ke "Ich hab's nicht wirklich kapiert, und sie wurde immer angepisster – wie ein alter Mann, der versucht, ein Smartphone zu benutzen."


show kenji happy_close onlayer master
with charachange

ke "Sie wollte mich umbringen. Umbringen und mit einer weiblichen Version meiner selbst ersetzen. Doch dann blendete sie das Sonnenlicht, das durch meine Brille reflektiert wurde, und rettete mein Leben."


show kenji neutral_close onlayer master
with charachange

ke "Es war wie, hör zu, ein Laserstrahl. Ich verstehe nicht, wie jemand mit Brille von jemandem mit Brille verletzt werden kann. Sie trägt auch eine, sie sollte immun gegen ihre Todesstrahlen sein, aber was auch immer."
ke "Sie gab mir diesen Umschlag mit deinem Namen drauf und ging einfach."


show kenji happy_close onlayer master
with charachange

ke "Mit Sicherheit hatte sie es auf dich abgesehen, darum log ich und sagte, dass du nicht da wärst."
ke "Das warst du doch, oder? Ich wollte dich schon die ganze Woche fragen, ob du mir mit meinen Hausaufgaben helfen kannst, aber ich bekam die ganze Zeit keine Antwort… Willkommen zurück, Mann!"


hi "Danke."


show kenji neutral_close onlayer master
with charachange

ke "Ja, also hat sie mir diesen Umschlag gegeben, und dein Name stand drauf. Ich wollte ihn nicht behalten, denn – was, wenn es eine Bombe wäre? Darum hab ich ihn einfach unter deiner Tür durchgeschoben, als sie weg war."


ke "Ich wollte es dir sagen, aber du warst zurück, bevor ich es konnte. Zumindest ist es keine Bombe."


hi "Na so was, danke. Ich werde dir nicht mit deinen Mathehausaufgaben helfen, denn – was, wenn dein Mathebuch eine Bombe ist?"


show kenji tsun_close onlayer master
with charachange

"Er sieht aus, als ob er am Boden zerstört wäre. Und auch, als ob er in Erwägung zieht, dass es wirklich eine Bombe sein könnte. Vermutlich ist es möglich, da niemand sein Mathebuch wirklich benutzt."


scene bg school_dormhisao onlayer master
with locationchange

"Ich werfe den Brief auf die Kommode hinter mir, drehe mich um und lasse dabei die Tür hinter mir zufallen."
"Sie stößt mit der Spitze von Kenjis Schuh zusammen, wodurch sie wieder aufschwingt. Kenji hüpft herum, so als ob ihm das mehr wehgetan hätte als das eigentlich möglich ist."


show kenji neutral onlayer master at center
with charaenter

"Bevor ich mich versehe, ist er bereits in meinem Zimmer. Ich schaffe es nicht, ihn davon abzuhalten, sich den Brief zu schnappen, wobei er seltsamerweise die Türme von Tablettenfläschchen drumherum ignoriert."


hi "Lies nicht einfach die Post anderer Leute!"


show kenji happy onlayer master
with charachange

ke "Komm schon, was ist es? Ein Liebesbrief von deiner Freundin? Hat sie irgendwelche Fotos mitgeschickt? Sexy Fotos?"


play sound sfx_dropstuff
stop music fadeout 4.0

"Während er sich gegen die Kommode lehnt und die Fläschchen, die dabei auf den Boden fallen, vollkommen ignoriert, liest Kenji still Iwanakos Brief."


"Es dauert eine gefühlte Ewigkeit, und so nah wie er den Brief an sein Gesicht hält, sieht es aus, als ob er ihn essen will."


show kenji tsun onlayer master
with charachange

ke "Wer ist „Iwanako”?"


hi "Meine Ex-Freundin."


play music music_night fadein 4.0

show kenji neutral onlayer master
with charachange

ke "Ex-Freundin, hm? Dann ist das wohl der Schluss-Mach-Brief. Ich dachte, die wären ein Mythos."


hi "Nein. Ich schätze, es ist einer. Aber im Grunde sind wir schon lange nicht mehr zusammen. Ich glaube, ich bin drüber hinweg."


"Kenji stimmt zu, sichtlich erleichtert, dass ich das nicht in eine peinliche Unterhaltung verwandle – auch wenn ich das fast will, da ich ihm gesagt habe, dass er ihn nicht lesen soll."


show kenji happy onlayer master
with charachange

ke "Ja, das ist eine gute Einstellung. Ist schon okay, ich hatte ebenfalls eine Trennung. Aber man darf sich davon nicht entmutigen lassen. Ich meine, sieh mich mal an."


hi "Ähhhhh…"


ke "Aber hey, sie hat dir einen Brief geschrieben. Vielleicht will sie wieder mit dir zusammenkommen, hm? Da steht es, antworte ihr. Das solltest du. Ist sie süß?"


"Für einen Kerl, der denkt, dass Feministinnen überall die Versklavung der Männer anstreben, interessiert er sich ziemlich für süße Mädchen. "


hi "Ich habe eine Freundin. Außerdem sieh mal den Zusammenhang – sie will nicht, dass ich ihr antworte. Nur weil es da steht, heißt das nicht, dass sie es will."


show kenji neutral onlayer master
with charachange

ke "Aber das hat sie geschrieben. Dieses Stein-Fisch-Kind Mädchen fährt immer noch total auf dich ab. Es steht sogar genau hier."


hi "Ich hab ihn gelesen – ich weiß, was da steht. Ich hab dir gesagt, dass du den Zusammenhang sehen musst. Sie sagte, dass ich mich von ihr entfernt habe, und alles in dem Brief zeigt, dass sie es akzeptiert hat."


hi "Ich denke, dass sie mir geschrieben hat, weil sie einfach freundschaftlich auseinandergehen will… schätze ich. Aber wir sind durch, sie will nicht wieder mit mir zusammenkommen oder was auch immer du denkst."


"Je mehr ich darüber nachdenke, desto mehr hört es sich danach an, als ob ich nur Ausreden für mich suche. Keine sehr gute Position."


"Ich bin mir sicher, dass sie nicht will, dass ich ihr antworte. Damit kann ich leben. Wenn ich ihr zurückschreibe und darauf eine deutlichere Antwort erhalten würde – oder gar keine – dann wäre ich nur am Boden zerstört."


"Vielleicht versuche ich, meine Entscheidung zu rechtfertigen, weil ich genau davor Angst habe. Es könnte sein, aber ich will nicht darüber nachdenken. Dieser Gedanke ist irgendwie abstoßend."


hi "Warum machst du überhaupt so eine große Sache draus?"


show kenji happy onlayer master
with charachange

ke "Weil du ihr zurückschreiben solltest. Sie will, dass du das tust. Ich will sehen, was sie antwortet."


show kenji neutral onlayer master
with charachange

ke "Verdammt, es muss nicht mal ein netter Brief sein. Das wäre auch cool, aber du könntest einen wütenden Brief schreiben und sie herausfordern. Das ist meine neue Angriffsstrategie – ich fordere Frauen einfach heraus. Du solltest es ausprobieren."


hi "Auch wenn sie mir einen Brief geschrieben hat, musst du verstehen, was das bedeutet. Jemandem heutzutage einen Brief zu schreiben ist etwas anderes. Man macht das nicht einfach so. Nicht in so einer Situation."


hi "Du kannst mit deinem Handy in einem Augenblick jemanden auf der anderen Seite der Welt anrufen und mit ihm reden, als ob er neben dir stehen würde. Oder ihm eine Mail schreiben, und er wird sofort benachrichtigt und kann dir antworten – einfach so."


hi "Ein Brief kann etwas Persönliches sein, aber sie wollte mich auf Distanz halten. Es ist ja nicht so, als ob ich vorbeischauen und sie besuchen könnte."


hi "Wenn ich ihre Nummer hätte, könnte ich sie anrufen; wenn ich ihre E-Mail-Adresse hätte, könnte ich ihr eine Mail schreiben. Falls sie wirklich etwas von mir hören wollte, hätte sie eins davon hinterlassen."


"Ich fühle mich albern, weil ich mir die ganze Zeit selbst einrede, dass Iwakanos Brief mir nichts ausgemacht hat, obwohl das offensichtlich Wunschdenken ist."


show kenji tsun onlayer master
with charachange

ke "Es könnte sein, dass sie es nur langsam angehen lässt. Vielleicht ist sie einfach nur zu schüchtern für einen Anruf. Ich weiß noch, wie meine Freundin mir immer SMS geschickt hat, weil sie so schüchtern war. Es war meganervig, Mann."


ke "Ich hab mich einen Dreck um Handys gekümmert, darum wollte ich keins. Und es hat sich rausgestellt, dass ich für jede einzelne bezahlen musste."
ke "Aber ich mag Handys nicht, darum konnte ich sie nicht mal zurückrufen und ihr sagen, dass sie das lassen soll."


show kenji neutral onlayer master
with charachange

ke "Doch ich hab es trotzdem getan. Ich hab sie herausgefordert. Sogar ein Handy hab ich benutzt. Es war buchstäblich {b}die{/b} Herausforderung."


hi "Schätze, das war es wohl."


"Auch wenn er Recht hat, bedeutet es, dass Iwanako immer noch ihre Distanz wahren will. Sie ist „nicht bereit”, locker mit mir zu reden."


"Wieso? Bin ich irgendein Freak? Ihre Taten ermutigen mich jedenfalls nicht. Vielleicht mache ich mir zu viele Gedanken deswegen, aber ich weiß es einfach nicht."


"Kenji fällt nichts dazu ein. Die darauf folgende Stille ist so unbehaglich und zähflüssig, dass ich anfange, die Sekunden zu zählen, bis Kenji sich eine Ausrede einfallen lässt und sich davonmacht."


show kenji tsun onlayer master
with charachange

ke "Sie fehlt mir…"


hi "Deine Ex?"


ke "Ja. Auch wenn sie durchgeknallt war, war es schön, mit ihr zusammen zu sein."


ke "Mein Rücken tut weh. Wenn sie immer noch bei mir wäre, könnte ich sie ihn massieren lassen."
ke "Wie man einen Ofen benutzt weiß ich auch nicht. Ich vermisse gebackenes Essen. Und manchmal haben wir auch im Flur Bowling gespielt. Auch das vermisse ich. Beim letzten Fest musste ich ganz alleine bowlen."


hi "Du spielst Bowling im Flur? Du wirst noch jemanden treffen."


ke "Das hat sie auch immer gesagt…"


"Kenji seufzt wehmütig. Wie schwer sich jemand beim Ausrutschen auf einem Bowling Pin verletzen kann, sieht er offensichtlich nicht ein."
"Seine Freundin scheinbar auch nicht, da sie ja auch mitgemacht hat. Was für eine seltsame Form der Liebe, aber es ist zumindest etwas, schätze ich."


hi "Vielleicht solltest du ihr einen Brief schreiben. Wenn sie dir zurückschreibt, könnt ihr heiraten."


stop music fadeout 0.3

show kenji rage onlayer master
with charachange

ke "Heiraten!? Nein. Nein nein nein. Nein."


hi "Okay, schön. Aber warum nicht? Es ist eindeutig, dass du sie magst, obwohl du Frauen hasst."


show kenji tsun onlayer master
with charachange

play music music_kenji fadein 2.0

ke "Feministinnen! Nicht Frauen, Feministinnen. Das ist ein Unterschied. Es gibt auch nicht-feministische Frauen. Verdammt, du bist so unglaublich diskriminierend. Korrelation impliziert keine Kausalität."
ke "Selbst wenn sie durchgeknallt und eine Frau ist, bedeutet das nicht, dass sie eine feministische, durchgeknallte Frau ist."


show kenji neutral onlayer master
with charachange

ke "So wie das Nichtexistieren von Beweisen kein Beweis für das Nichtexistieren ist. Wenn das stimmt, dann heißt das im Umkehrschluss, dass das Existieren eines Beweises kein Beweis für das Existieren ist."


hi "Eigentlich glaube ich, das es das ist. Und ich glaube nicht, dass du hier einen Umkehrschluss ziehen kannst."


show kenji tsun onlayer master
with charachange

ke "Nein, sei still, das ist Mathematik! Willst du sagen, dass Mathe Unrecht hat?"


"Ich glaube, dass {b}er{/b} Unrecht hat."


"Also hat sogar Kenji jemanden, den er mag. Es ist verlockend, ihn zu fragen, warum er und seine Ex sich getrennt haben – oder allgemein nachzuhaken – aber ich sollte es lassen."
"Nicht nur, weil es als Schnüffelei gewertet werden kann, sondern auch, weil er mich dann vielleicht das gleiche fragen würde."


stop music fadeout 8.0

"Dieses Gespräch lässt mich an Shizune denken, auch wenn meine Gedanken nur vage und verstreut sind. Mir kommen nur Fragen in den Sinn."


"Ich frage mich, ob ich überhaupt eine Gelegenheit hatte, Iwanako zu lieben. Diese ganze Situation mit ihr versetzt mir einen Stich, eine Erinnerung mit bitterem Beigeschmack."


"Shizune liegt mir viel mehr am Herzen. Dennoch fühlt es sich an, als würde ich ihr sogar jetzt noch hinterherlaufen. Ich habe zwar nichts dagegen, aber ich will diese Distanz zwischen uns schließen."


"Iwanakos Brief ist dafür verantwortlich, aber ich habe auch so schon seit einer Weile so empfunden. Ich bin ihr nähergekommen, aber das reicht mir noch nicht. Ich will es noch einmal versuchen – jetzt sofort."


hide kenji onlayer master
with charaexit

"Ich sage Kenji, dass er gehen soll, damit ich mich umziehen kann. Dann mache ich mich auf zum Schülerratszimmer."


scene bg school_courtyard onlayer master
with locationskip

"Das Schulgelände ist heute größtenteils menschenleer, was bei dem schönen Wetter heute eigentlich schade ist."


scene bg school_hallway3 onlayer master
with locationskip

play sound sfx_doorknock2

"Niemand antwortet, als ich an der Tür klopfe. Ich versuche trotzdem reinzugehen, aber es ist abgeschlossen. Als ich meine Hand vom Türknauf nehme, ist sie voller Staub. Es sieht so aus, als wäre niemand hier gewesen, seit wir abgereist sind."


"Da ich schon einmal hier und angezogen bin, kann ich auch genauso gut etwas in der Stadt essen gehen. Jedoch liegt mein Portemonnaie noch in meinem Zimmer."


scene ev misha_sad onlayer master:
    truecenter
    subpixel True zoom 1.05
    easein 10.0 zoom 1.0
with locationskip

"Auf dem Rückweg stolpere ich über Misha, die gerade an der hinteren Wand des Hauptgebäudes sitzt."


"Ihr Augen sind geschlossen. Sie schläft, und sieht dabei vollkommen friedlich aus. Es fiel mir immer schwer, mir vorzustellen, dass sie mal nicht andauernd ungeduldig auf ihren Zehenspitzen hin- und herspringt."


"Zuerst will ich sie rufen und sie fragen, ob sie Shizune gesehen hat, oder ob sie mit mir in die Stadt kommen will. Aber jetzt, wo ich sie so sehe, will ich sie nicht stören. Ich lasse sie in Ruhe."


scene black onlayer master
with dissolve

$ suppress_window_after_timeskip = True

label de_S25:

window hide None

scene bg school_council_bw onlayer master
with locationchange

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_pearly

nvl clear
nvl show dissolve

n "\n\n\nDie ersten paar Tage nach meiner Rückkehr habe ich fast vergessen, dass ich im Schülerrat bin. Ich konnte hier und da aufschnappen, dass der Schülerrat üblicherweise am Ende der Ferien mit Arbeit überschwemmt wird, aber das musste nicht unbedingt stimmen."


n "Die paar Male, in denen ich Shizune oder Misha zu fassen bekam, waren sie in zu großer Eile, als dass ich sie hätte fragen können, ob sie vielleicht Hilfe brauchen. Immer, wenn sie es nicht waren, bekam ich nur Misha in die Finger."


n "\n Shizune sagte dann immer nur, dass es zwar Arbeit gebe, aber nur so wenig, dass Misha oder ich uns langweilen würden."


n "\nNach einer Weile hatte ich mich wieder daran gewöhnt, etwas mehr Freizeit zu haben – obwohl es Phasen gab, in denen es mir wie zu viel Freizeit vorkam."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

scene bg school_council onlayer master
show shizu basic_normal2 onlayer master at center
with locationchange

window show

"Doch gerade als ich mich daran gewöhnt hatte, änderten sich die Dinge wieder. Jetzt befinde ich mich wieder im Schülerratszimmer und streite mit Shizune darüber, ob Taschentuchschachteln gute Wahlurnen sind oder nicht."


hi "Ich sage dir, solange wir die würfelförmigen und nicht die rechteckigen nehmen, reichen sie vollkommen."


hi "Misha, kannst du ihr das gebärden? Ich hab gerade irgendwie die Hände voll… Obwohl, vergiss es."


"Sie schneidet gerade Stimmzettel aus. Würde sie eine impulsive Bewegung machen, würde die Schere wahrscheinlich in irgendjemandes Kopf enden."


"Ich lasse den Eimer Plakatfarbe auf meinen kleinen Tisch im Schülerratszimmer fallen. Als mich die dadurch aufgeworfen Staubwolken im Gesicht treffen, muss ich husten. Wir waren wirklich lange nicht hier."


show shizu behind_blank onlayer master
with charachange

ssh "Meinst du, wir sollten die Größe der Stimmzettel ändern?"


show bg school_council onlayer master at bgright
show shizu behind_blank onlayer master at tworight
with charamove

show mishashort sign_confused onlayer master at twoleft
with charaenter

mi "Was~? Aber Shicchan, ich hab schon so viele davon ausgeschnitten…"


show shizu basic_normal onlayer master
with charachange

ssh "Wir können sie kleiner machen. Es wird effizienter sein. Wir müssen nur eine kleinere Schriftgröße nehmen. So passen mehr Stimmzettel in eine Schachtel. Wir bräuchten dann nur halb so viel Papier."


show shizu behind_smile onlayer master
with charachange

ssh "Das Wahlformat kann geändert werden. Es könnte mehr wie eine echte Wahl sein; dann könnten wir vielleicht mit weniger Schachteln auskommen."


show shizu adjust_happy onlayer master
with charachange

ssh "Mit dem gesparten Geld können wir Pizza essen gehen, oder vielleicht Chinesisch. Oder Kuchen, oder drei Schüsseln von diesen neuen Ramen, die ich ausprobieren will."


"Aufgeregt reibt Shizune mit einem Finger an ihrem Brillenrahmen entlang, während sie über weitere Wege nachdenkt, wie man auch nur einen halben Yen von unserem Budget sparen könnte."


"Da ich glaube, dass sie die Einzige ist, die die Höhe unseres Budgets überhaupt kennt, traue ich mich gar nicht zu fragen, wie klein es ist, dass sie solche Überlegungen anstellen muss."


hi "Was ist mit den Stimmzetteln, die Misha schon ausgeschnitten hat?"


show shizu basic_happy onlayer master
with charachange

ssh "Keine Sorge, keine Sorge. Ich kann daraus Notizzettel machen und sie im Schul-Shop verkaufen."


show mishashort perky_confused onlayer master
with charachange

mi "Aber Shicchan, süß sehen die nicht wirklich aus~…"


show shizu adjust_frown onlayer master
with charachange

"Shizune sieht das anscheinend anders. Jetzt streiten sie sich, aber es sieht aus, als bestünde der Streit lediglich aus einem abwechselnden Gebärden von „Nein, tun sie nicht.” und „Doch, tun sie.”"
"Sie tun das so lange, bis sie so müde sind, dass sie nur noch abwechselnd befehlend mit den Finger aufeinander zeigen."


"Es ist seltsam. Zum Teil weil es irgendwie lächerlich aussieht, aber auch weil ich noch nie gesehen habe, dass sie bei etwas nicht einer Meinung sind."


"Allerdings sahen die beiden die letzten Tage ziemlich gestresst aus."


"Shizune hat sich zunehmends in die Schülerratswahlen hineingesteigert, obwohl sie noch Monate entfernt sind. So müssen sich Politiker verhalten, wenn sie bemerken, dass ein Führungswechsel bevorsteht und ihre Zeit vorüber ist."


"Ich habe überhaupt Schwierigkeiten, Schülerrats-Angelegenheiten ernst zu nehmen – sogar jetzt, während ich meine Kalligrafie an Schildern übe, die nicht einmal eine Woche lang aufgehängt sein werden – aber ich kann verstehen, warum Shizune es tut."


"Schließlich ist sie seit drei Jahren die Schülerratspräsidentin. Ihrem Vater zufolge wollte sie den Job sogar schon viel länger. Ich schätze, drei Jahre ist eine zu kurze Karriere, als dass sie damit zufrieden wäre."


hi "Hat sich der letzte Schülerrat auch so viel Mühe gemacht, um einen reibungslosen Übergang für dich zu ermöglichen?"


show shizu behind_frustrated onlayer master
with charachange

"Shizune zieht ein verärgertes Gesicht, das mir sagt, dass sie ganz und gar nicht hilfreich waren."


hi "Dann vermute ich, dass du das alles tust, um ein gutes Beispiel abzugeben?"


show shizu basic_frown onlayer master
with charachange

shi "…"


show mishashort hips_frown onlayer master
with charachange

mi "Das kommt nur ins Spiel, wenn sie daraus etwas lernen, Hicchan~! Falls sie es nicht tun, werde ich megawütend~! Wenn sie sich als unzuverlässig erweisen, werde ich hart mit ihnen ins Gericht gehen."


"Wenn Misha das sagt, klingt es nicht sehr einschüchternd."


hi "Also habt ihr sie schon getroffen?"


show shizu adjust_smug onlayer master
with charachange

shi "…"


show mishashort hips_grin onlayer master
with charachange

mi "Ahaha~. Hicchan, bis jetzt gibt es noch keine Kandidaten."


hi "Was? Gar keinen?"


show shizu behind_smile onlayer master
show mishashort hips_smile onlayer master
with charachange

ssh "Nicht einmal für den Schülerratspräsidenten. Deswegen versuche ich ja, Interesse für diese Stelle zu wecken. Was meinst du?"


"Stolz präsentiert sie ein selbstgemachtes Poster. Es sieht sehr, äh, militant aus."



hi "Vielleicht siehst du das ganze etwas zu ernst."


show shizu adjust_frown onlayer master
with charachange

"Shizune runzelt die Stirn und spielt beleidigt mit ihrer Brille."


ssh "Ist das sonderbar?"


hi "Ja."


show shizu behind_smile onlayer master
with charachange

"Seltsamerweise scheint es sie zu freuen, dass ich anderer Meinung bin, und wenn sie nicht so sehr auf ihre momentane Tätigkeit konzentriert wäre, würde sie versuchen, mit mir darüber zu streiten – nur weil es für sie interessant wäre."


show shizu basic_normal onlayer master
with charachange

ssh "Was ist daran so sonderbar?"


show shizu adjust_smug onlayer master
with charachange

"Sieht so aus, als hätte sie es doch vor. Aber dann winkt Shizune abweisend mit ihrer Hand, als ob sie die Wörter in der Luft fangen und löschen wollte. Stattdessen beleidigt sie plötzlich ihre zukünftigen Nachfolger."


hi "Na ja, zum einen ist es komisch, weil in meiner alten Schule Wahlen erst in sechs Monaten stattfinden würden. Ich meine, ihr wisst ja – wir machen im März unseren Abschluss. Es ist ziemlich komisch, so früh darüber nachzudenken."


show shizu behind_blank onlayer master
with charachange

ssh "Hier ist es etwas anders."


show shizu adjust_frown onlayer master
with charachange

shi "…"


show mishashort sign_smile onlayer master
with charachange

mi "Hicchan, es würde mich schlaflos machen, wenn wir bis zum Tag unseres Abschieds keine Nachfolger haben~! Sagt Shizune."


show mishashort hips_grin onlayer master
with charachange

mi "Aber~! es ist nicht so, als ob die Schule ohne einen Schülerrat nicht mehr funktionieren würde. Auch wenn es schwieriger für sie wird, Formulare zu verteilen~!"


show mishashort cross_laugh onlayer master
with charachange

mi "Hahaha~."


show shizu basic_normal2 onlayer master
show mishashort cross_smile onlayer master
with charachange

"Shizune jedoch lacht nicht. Mishas Witz lässt sie zusammenzucken, als ob er ihr einen Stich versetzt hatte. Auch wenn Misha das nicht beabsichtigt hatte, war ihre Stichelei Shizune gegenüber wohl doch etwas grausam."


show shizu adjust_frown onlayer master
with charachange

ssh "Hmph. Ich versuche, mehr Leute zur Kandidatur zu bewegen, aber alle sind so faul."
ssh "Sie denken, sie könnten es auf die leichte Schulter nehmen, weil es noch keinen Stichtag gibt. Diese Faulpelze… Jetzt könnten sie sich einen Zeitvorteil verschaffen."


show shizu cross_angry onlayer master
with charachange

ssh "„Noch” sechs Monate entfernt? Wenn sie jetzt nicht die Initiative ergreifen, verdienen sie nicht eine Stimme!"


show mishashort sign_smile onlayer master
with charachange

mi "Denken die wirklich, dass es so ein leichter Job ist, dass man alles auf den letzten Drücker machen und locker in diese Rolle schlüpfen kann~? Beleidigend~! Wirklich~, wirklich~!"


show mishashort hips_frown onlayer master
with charachange

mi "Sie werden bei lebendigem Leibe gefressen, sobald sie sich an diesen kleinen Schreibtisch setzen müssen und sehen, wie viel Arbeit ansteht~!"


show shizu behind_frustrated onlayer master
with charachange

ssh "Wenn das eine echte Wahl wäre, wären sie in großen Schwierigkeiten. Ich hab neulich über japanische Wahlkampfregeln gelesen. Aus irgendeinem Grund nur über die schlechten."


hi "Aus irgendeinem Grund."


"Für einen Augenblick hat Shizune gerade wie ihr Vater „geredet”. Und es kam aus Mishas Mund. Unheimlich."


hi "Na ja, zum einen, Schattenshogun, ist das nicht dein Problem. {b}Sie{/b} werden gewählt. Zweitens ist es nur eine Schul-Wahl. Man bewirbt sich ja nicht für den Stadtrat oder das Parlament. Ich denke nicht, dass hier japanische Wahlkampfregeln gelten."


"Drittens, auch wenn ich es nicht sagen will, beunruhigt mich Shizunes Enthusiasmus über die Wahlen und Stimmen."


"Ihrem Vater zufolge wurde sie nicht einmal selbst gewählt. Wobei mir einfällt, dass ich mich auch nicht erinnern kann, dass Shizune das einmal erwähnt hätte."


"Hat sie dann diese Stelle bekommen, weil sie vom alten Schülerrat rekrutiert wurde und er zerfallen ist, bis nur noch sie übrig war? Irgendwie hab ich noch nie darüber nachgedacht."


"Ich weiß nicht, was ich davon halten soll, aber es würde mich nicht überraschen. Wir sind im Moment nur drei Mann stark."


"Falls sie wirklich unter solch traurigen Umständen Schülerratspräsidentin geworden ist, frage ich mich, ob es überhaupt eine Wahl geben wird."
"Das Interesse könnte extrem gering sein – oder sogar nicht vorhanden. Dann wäre ihre ganze Mühe für nichts und wieder nichts."


"Ich setze ein Ausrufezeichen auf das Ende des Posters, an dem ich gerade arbeite. Es ist etwas schlicht, darum glaube ich, dass es nicht schaden kann. Eigentlich ist es immer noch etwas zu schlicht. Ich mache das Ausrufezeichen doppelt so groß."


hi "Ich bleibe dabei, dass du etwas ruhiger werden musst. Wenn der Kram erst in ein paar Monaten relevant wird, arbeitest du vielleicht etwas zu hart daran. Das ist meine Meinung. Du machst dir zu viele Gedanken."


"Ich weiß nicht, wie man das Wort „relevant” gebärdet. Bei dem Versuch, schleudere ich unbeabsichtigt eine lange Farblinie auf das Poster. Unmöglich, dass ich das noch retten kann."


hi "Misha, kannst du sie das fragen?"


show mishashort sign_smile onlayer master
with charachange

show shizu adjust_happy onlayer master
with charachange

"Shizune kichert still und hat dabei ihre Zähne zusammengebissen, sodass sie eigentlich kein Geräusch dabei macht."


show shizu behind_blank onlayer master
with charachange

ssh "Weil es vieles gibt, worüber man sich Sorgen machen muss."


hi "Zum Beispiel?"


show shizu basic_normal onlayer master
with charachange

ssh "Zum Beispiel… Die Schachteln werden für gewöhnlich sehr schön, darum klauen sie die Leute. Das müssen wir einplanen."


show mishashort hips_grin onlayer master
with charachange

mi "Wahahah~! Wir sollten sie diesmal komisch aussehen lassen, dann klaut sie niemand! Was meinst du, Shicchan~?"


hi "Wir können schräge Gesichter draufmalen. Oder wir können ein kleines Bild von Shizune auf jede Einzelne kleben, auf dem steht: „Stehlen ist falsch.”"


show shizu behind_frown onlayer master
with charachange

ssh "Nein. Das ist nicht lustig! Das ist auch nicht das einzige Problem. Natürlich meine ich auch die Wahlbeteiligung…"


show shizu basic_normal2 onlayer master
with charachange

ssh "… Und das Worst-Case-Szenario wäre, gar keine Kandidaten zu haben."


"Sie lächelt, während sie das gebärdet. Es scheint zwar nur ein Scherz zu sein, aber mein Gefühl sagt mir etwas anderes."


show mishashort cross_laugh onlayer master
with charachange

"Sogar Misha versteht, dass die Möglichkeit sehr real ist, jedoch versucht sie, die Stimmung mit einem Lachen am Ende von Shizunes Aussage zu retten. Ohne Erfolg."


show shizu behind_frustrated onlayer master
with charachange

shi "…"


show shizu basic_angry onlayer master
with charachange

ssh "Was stimmt nur mit euch beiden nicht?"


show shizu adjust_frown onlayer master
with charachange

ssh "Ich hab nur einen Scherz gemacht. Es gibt dieses Jahr wirklich einige Interessierte. Würde ich mir diese ganze Arbeit machen, wenn es sie nicht gäbe? Ich bin doch nicht blöd."


show shizu behind_smile onlayer master
with charachange

ssh "Wenn die Wahlen vorüber sind, spendiere ich allen ein Abendessen. Ich bin bereits am Planen."


hi "Sogar für den neuen Schülerrat?"


show shizu adjust_smug onlayer master
with charachange

ssh "Nein, die können sich ihr eigenes Festessen besorgen. Es ist nur für den aktuellen Schülerrat. Ich bin froh, sobald ich nicht mehr die ganze Zeit diese undankbaren Jobs erledigen muss."


show mishashort hips_grin onlayer master
with charachange

mi "Ein Abendessen nur für uns~? Yay~! Das ist ja wie eine kleine Party, Shicchan~!"


stop music fadeout 3.0

"Obwohl sie sich offensichtlich zur Heiterkeit zwingt, sage ich nichts. Für die restliche Zeit, die glücklicherweise nicht allzu lang ist, arbeiten wir schweigend."


scene bg school_hallway3 onlayer master
with shorttimeskip

play music music_daily fadein 0.5

"Nach dem Unterricht stehe ich beim Schülerratszimmer vor einer verschlossenen Tür. Es ist seltsam, da Shizune zuvor so beschäftigt war, dass ich erwarten würde, dass sie nach der Schule weiterarbeitet."


"Vielleicht hat sie auf meinen Rat gehört und eine Pause gemacht. Ich hoffe, es ist so simpel."


scene bg school_courtyard_ss onlayer master
with locationskip

"Mit einem etwas mulmigem Gefühl mache ich einen kurzen Spaziergang um die Schule."
"Ich verliere mich in Gedanken. Ich weiß nicht mehr, wann meine Füße angefangen haben, sich zu bewegen, aber ich bin bereits so weit gelaufen, dass ich langsam müde werde. Bei meiner Kondition hat das aber nicht viel zu sagen."


"Nur ein kurzer Spaziergang auf dem Schulgelände und ich bin bereits erschöpft. Wirklich erbärmlich."


scene bg school_hallway3 onlayer master
with locationskip

"Ehe ich mich versehe, bin ich wieder zurück vor dem Schülerratsbüro. Und diesmal ist noch jemand anderes da."


show mishashort hips_smile onlayer master at center
with charaenter

mi "Hi, Hicchan~!"


hi "Es ist abgeschlossen."


"Als ich die Limonadendose in ihrer Hand sehe, fange ich reflexartig an, nach einem Verkaufsautomaten zu suchen. So durstig bin ich."


show mishashort sign_smile onlayer master
with charachange

mi "Das weiß ich, Hicchan~! Shicchan ist woanders, schätze ich~!"


hi "Seltsam."


show mishashort hips_grin onlayer master
with charachange

mi "Ahahaha~. Wir kleben nicht zusammen, Hicchan~."


"Sie nimmt einen großen Schluck von ihrer Limonade und kippt sich schließlich den letzten Rest einfach in den Mund. Es kommt mir vor, als würde sie mich verspotten."


show mishashort perky_smile onlayer master
with charachange

mi "Willst du eine, Hicchan~?"


hi "Nein, schon okay. Ich kann nicht das Getränk von jemand anderem annehmen – das ist unhöflich. Außerdem, du machst dich über mich lustig, oder? Du hast doch gerade alles runtergestürzt."


show mishashort sign_smile onlayer master
with charachange

mi "Ich hab noch eine andere in meiner Tasche~! Ich war vorbereitet, siehst du~, siehst du~? Ich bin genau wie Shicchan~!"


hi "Sie ist etwas zu vorbereitet. Immerhin ist es gut, dass etwas davon auf dich abfärbt. Nach… zwei Jahren?"


show mishashort cross_laugh onlayer master
with charachange

mi "Wahaha~!"


"Es ist etwas beunruhigend, wie sie mich beim Trinken anstarrt, aber ich bin zu dankbar, um mich darum zu sorgen."


hi "Du und Shizune, ihr ladet mich immer zu etwas ein. Es wird langsam peinlich für mich."


show mishashort hips_smile onlayer master
with charachange

mi "Echt~, Hicchan? Ahaha~. Lad mich dann mal zum Mittagessen ein, okay~? Dann~! sind wir quitt."


hi "Na ja, es ist lustig, dass du das sagst. Ich wollte dich fragen, ob du im Dorf etwas essen gehen willst…"


show mishashort hips_grin onlayer master
with charachange

mi "Juhu~ juhu~! Ich hab heute wirklich Hunger, Hicchan! Danke!"


show mishashort invis onlayer master at tworight
with dissolvecharamove

stop music fadeout 3.0

"… Gestern. Ich wollte sie gestern fragen. Misha unterbricht mich, bevor ich den Satz beenden kann, und ich habe keine Gelegenheit, sie zu korrigieren, da sie gerade wie wild lachend um mich herum springt, während sie aufgeregt mit den Armen flattert."


scene bg suburb_roadcenter_ss onlayer master
with locationskip

play music music_dreamy fadein 2.0

"Weil ich mein Portemonnaie schon bei mir habe, mache ich mich mit Misha zusammen auf den Weg ins Dorf, während sie energisch mit ihren Händen gestikuliert und sich fragt, wo wir hingehen sollten."
"Zumindest glaube ich das. Es könnte auch sein, dass sie mich fragt."


hi "Hast du eine Idee, wo wir hingehen könnten?"


show mishashort hips_smile_ss onlayer master at center
with charaenter

mi "Hmmm~. Ich will zum Teehaus, die haben da ein richtig großes Parfait."


hi "Ich hab gesehen, wie du das letztes Mal gegessen hast. Sah ziemlich groß aus."


show mishashort hips_grin_ss onlayer master
with charachange

mi "Nein nein nein~! Das, das ich meine, ist richtig, richtig~ groß! Und außerdem richtig teuer~!"


hi "Richtig, richtig~ teuer?"


show mishashort cross_laugh_ss onlayer master
with charachange

mi "Hahaha~! Ein bisschen~…"


hi "Oh man. Na ja, du und Shizune, ihr habt mich schon ein paar Mal zum Essen eingeladen, darum passt das schon."


show mishashort perky_confused_ss onlayer master
with charachange

mi "Hicchan, ich glaube nicht, dass ich das je getan hab~. Bist du dir sicher, dass es nicht nur Shicchan war?"


hi "Willst du wirklich gegen ein Gratisessen protestieren? Mach dir mal keinen Kopf."


scene bg suburb_shanghaiint onlayer master
with locationskip

"Wir erreichen das Shanghai, und werden überraschenderweise von einer anderen Kellnerin als Yuuko zu unserem Platz geführt."


"Sobald sie durch die Tür läuft, ruft Misha lautstark ihre Bestellung heraus. Sie scheint auf das Parfait zu brennen. Als es ankommt, sehe ich, dass es wirklich sehr groß und teuer aussieht."


show mishashort perky_confused_close onlayer master at center
with charaenter

mi "Willst du nichts bestellen, Hicchan~? Wenn du Hunger hast, können wir teilen."


hi "Nee. Ich mag keine Parfaits. Ich mag diese Zuckerkristalle nicht."



show mishashort sign_smile_close onlayer master
with charachange

mi "Du kannst sie rauspicken~!"


hi "Man kann Zuckerkristalle nicht einfach rauspicken, sei nicht albern."


show mishashort perky_smile_close onlayer master
with charachange

"Selbst wenn ich es könnte, Misha vermischt ihr Essen so sehr, dass es nicht mehr möglich ist. Es sieht auch irgendwie eklig aus."


"Ich frage mich, ob so viele Geschmacksrichtungen überhaupt zusammenpassen. Kann sie aus diesem Brei wirklich etwas herausschmecken? Aber es scheint, als ob es ihr wirklich schmecken würde."


show mishashort hips_grin_close onlayer master
with charachange

mi "Mmh~. Parfaits sind das Beste~. Ich hab empfindliche Zähne, darum ist Eiscreme ein no-go~. Kuchen ist mir zu weich, und wenn zu viel Glasur drauf ist, ist er langweilig. Aber Parfaits sind spannend."


show mishashort perky_smile_close onlayer master
with charachange

mi "Wie viele Cafés hier haben Parfaits~? Ich glaube zehn! Ich hab alle probiert; dieses hier ist das Beste. In dem hier ist etwas Flan drin."


hi "Du klingst, als wärst du eine Art Dessert-Expertin."


show mishashort hips_smile_close onlayer master
with charachange

mi "Nicht nur Desserts~! Ich will alle möglichen leckeren Sachen essen~."


show mishashort hips_grin_close onlayer master
with charachange

mi "Eines Tages werde ich genug Geld haben, um ein zwei Kilo Matsusaka Rindersteak zu kaufen~!"


hi "Das wären über hunderttausend Yen… So dekadentes Essen ist dann also so was wie dein Hobby, hm?"


"Die Hobbys von jemandem zu erfahren ist nichts, was Monate dauern sollte. Rückblickend bin ich sehr unhöflich gewesen. Außerdem… Das ist ein ziemlich kostspieliges Hobby."


show mishashort perky_confused_close onlayer master
with charachange

mi "Schätze schon~! … Dekadent~?"


hi "Jepp."


show mishashort hips_grin_close onlayer master
with charachange

"Misha kichert, während sie sich die Hand vors Gesicht hält."
"Es sieht aus, als wäre aus Versehen etwas Eis an ihre Nase gekommen. Sie bemerkt es nicht. Ich kann es nicht ignorieren. Ich wünschte, sie würde es abwischen. Ich will sie darauf hinweisen, aber plötzlich sagt sie:"


show mishashort perky_confused_close onlayer master
with charachange

mi "Ich weiß nicht, was das bedeutet."


hi "Oh. Ich schätze, es ist eh ein schlechtes Wort. Es ist zu negativ belegt. Epikureisch ist besser. So nennt man jemanden, der gerne leckeres Essen isst. Allerdings ist es ein Adjektiv. Das Substantiv ist Epikureer."


show mishashort cross_laugh_close onlayer master
with charachange

mi "Wahaha~!"


show mishashort cross_grin_close onlayer master
with charachange

mi "Hicchan, du bist zu wortreich."


hi "Sorry."


show mishashort perky_smile_close onlayer master
with charachange

mi "Hahaha~. Ich glaube, das ist das, was Shicchan an dir mag."


hi "Dass ich wortreich bin? Dann muss ich mir ein paar Thesauri kaufen."


show mishashort hips_grin_close onlayer master
with charachange

mi "Wahaha~! Nein, nicht so, Hicchan~!"


"Letztendlich beschließe ich doch, mir einen Kaffee zu bestellen, doch es dauert eine Weile, bis ich die Kellnerin auf mich aufmerksam machen kann. Und meinen Kaffee zu bekommen wird vermutlich genauso lange dauern."


"Das Teehaus füllt sich. Das ist nicht überraschend, da wir schon seit fast einer Stunde hier sind, während sie dieses Dessert bearbeitet hat."
"Ich will meinen Kaffee zum Mitnehmen bestellen, aber Misha bestellt auch einen, also bleiben wir wohl länger hier als ich dachte."


hi "Ich wünschte wirklich, dass es so einfach wäre. In letzter Zeit ist es schwierig, mit ihr zu reden."


show mishashort sign_smile_close onlayer master
with charachange

mi "Shicchan ist mit den Wahlen beschäftigt gewesen~!"


hi "Ich weiß, dass wir nicht die ganze Zeit Spaß haben können. Es ist nur, dass es so vieles gibt, was ich ihr sagen will."
hi "Aber immer wenn ein passender Augenblick kommt, vermassle ich es. Und im Moment gibt es nicht einmal solche Augenblicke. Wegen der Wahlen."


hi "Allerdings ist bis dahin noch Zeit."


show mishashort hips_frown_close onlayer master
with charachange

mi "Hicchan, glaubst du, dass Shizune dir aus dem Weg geht?"


"Misha klingt wütend. Das war zu erwarten, aber das denke ich überhaupt nicht."


hi "Nein."


show mishashort perky_sad_close onlayer master
with charachange

mi "Wirklich~?"


"Ihre verträumte Betonung lässt mich denken, dass sie von meiner Antwort enttäuscht ist. Wenn das so ist, glaubt sie es vielleicht selbst."
"Ich stelle ungern so eine Frage, aber ich bin sicher, dass Misha mir ehrlich antworten würde. Ansonsten würde ich nicht einmal im Traum daran denken."


hi "Und du?"


show mishashort hips_smile_close onlayer master
with charachange

mi "Nein, natürlich nicht, Hicchan~! Aber~…! Manchmal ist es frustrierend~. Shicchan hat so viel Energie und versucht ihre Begeisterung für die Dinge auf andere zu übertragen."


show mishashort perky_sad_close onlayer master
with charachange

mi "Aber es ist, als wüsste sie nicht, wie man damit umgeht, wenn am Ende alle wirklich aufgedreht sind. Oder~! Ich glaube, dass sie sicherstellen will, dass nichts schief geht. Wenn ich ihr aushelfen will, lehnt sie mich immer ab."


mi "Es ist zum Mäusemelken."


show mishashort hips_grin_close onlayer master
with charachange

mi "Ich denke wahrscheinlich nur zu viel drüber nach~! Stimmt's?"


"Misha nimmt einen großen Schluck von ihrem Kaffee, dann streckt sie die Zunge heraus."


show mishashort hips_laugh_close onlayer master
with charachange

mi "Au~! Heiß~ heiß~ heiß~… dachte, er wäre mittlerweile abgekühlt~!"


hi "Ist es wirklich schon so lange her?"


"Ich schaue auf meine Uhr. Es ist überhaupt nicht lange her, aber draußen kann man schon die Sonne langsam untergehen sehen."


hi "Nicht wirklich. Hm, aber es ist heute ziemlich schnell dunkel geworden, darum kann ich verstehen, warum du das gedacht hast."


show mishashort perky_sad_close onlayer master
with charachange

"Daraufhin schaut Misha nach draußen und gähnt fast augenblicklich. Sie sieht müde aus. Lustig, denn…"


hi "Bist du müde? Vor gerade zwei Sekunden warst du noch hellwach."


show mishashort sign_sad_close onlayer master
with charachange

mi "Ich werde müde, wenn es dunkel ist, Hicchan~."


hi "Einfach so? Bist du ein Vogel?"


show mishashort perky_smile_close onlayer master
with charachange

mi "Ahahaha~."


"Ich greife nach meinem eigenen Kaffee und nehme einen Schluck. Er ist überhaupt nicht heiß, aber sehr lecker."
"Ich schütte ihn so schnell wie möglich hinunter, weil ich jetzt auch zurück in mein Zimmer will. Misha versucht mich nachzumachen, aber ist es immer noch zu heiß für sie."


"Während ich darauf warte, dass sie austrinkt, beginne ich mich zu fragen, was sie vorhin meinte. Das, was Shizune an mir mag. Plötzlich bin ich sehr neugierig. Aber das jetzt wieder auszugraben, kommt mir unnötig vor."


show mishashort hips_grin_close onlayer master
play sound sfx_impact
with vpunch

"Während ich noch hin und her überlege, werde ich von Misha unterbrochen, die ihren leeren Pappbecher mit einem lauten Schlag auf den Tisch knallt."


show mishashort cross_grin_close onlayer master
with charachange

mi "Fertig~!"


"Scheinbar sehr zufrieden mit sich selbst gibt sie ein kurzes Lachen von sich. Irgendwie wie ein Kleinkind. Ich frage mich, ob sie diese Spiralfrisur schon hatte, als sie klein war. Oder war es eher wie ihr jetziger Look? Wohl eher Letzteres."


hi "Ich schätze, wir sollten dann zurück. Ich sehe die Kellnerin nicht. Versuch nicht einzuschlafen, während ich für den Eisbecher bezahle, okay?"


show mishashort sign_smile_close onlayer master
with charachange

mi "Kein Eisbecher – es war ein Parfait, Hicchan."


show mishashort cross_laugh_close onlayer master
with charachange

mi "Wahaha~."


hi "Du hast Eis auf deiner Nase."


stop music fadeout 2.0

scene black onlayer master
with dissolve


label de_S26:

scene bg school_scienceroom onlayer master at right
with locationchange

play sound sfx_paper
play music music_normal fadein 3.0

"Im Unterricht am nächsten Nachmittag habe ich gerade zwei Aufgaben eines Mathe-Logik-Arbeitsblattes gelöst, als mich ein zusammengefaltetes Blatt Papier am Kopf trifft."
"Ich bin mir sicher, dass ich weiß, von wem es kommt, aber nur zur Sicherheit sehe ich mich trotzdem kurz im Klassenzimmer um."


show shizu invis onlayer master at left
with None

show bg school_scienceroom onlayer master at left
show shizu behind_blank onlayer master at center
with dissolvecharamove

"Niemand in dieser Klasse kann sich gut verstellen. Ich weiß, dass alle gesehen haben, wer es nach mir geworfen hat, und als ich Shizune direkt anschaue, versucht sie nicht einmal, auf schüchtern zu machen."


"Auf dem Land ist alles so anders. Auf meiner alten Schule hätte ich jetzt keine Ahnung, wer es war."


"Ich falte das Papier auseinander und lese."


window hide

$ written_note("Misha ist abwesend! Hilf mir heute nach der Schule aus!")


window show
hi "Was soll dieser Zettel? Warum benutzt du nicht einfach Zeichensprache?"


"Einen Großteil von meinem Zeichensprachekenntnissen habe ich von Misha gelernt, da sie beim Sprechen immer gebärdet. Darum rutscht mir der Satz laut heraus, als ich ihn Shizune gebärde. Ein leises Gelächter geht durch dein Raum. Wie peinlich."


his "Ich werde helfen, wenn ich nicht viel machen muss."


show shizu basic_angry onlayer master
with charachange

ssh "Das ist albern, wenn Misha nicht da ist, musst du offensichtlich Arbeit für zwei erledigen."


"Ich weiß nicht, ob das wirklich etwas bedeutet. Immerhin hat sich Misha gestern hauptsächlich darüber beschwert, dass Shizune sich nicht von ihr helfen lässt. Und ich tue normalerweise auch nicht wirklich viel."


"Nachdem ich eine Weile so tue, als würde ich darüber nachdenken, schreibe ich einen Zettel zurück, um ihr zuzustimmen. Eigentlich bin ich glücklich darüber, dass sie mich gefragt hat, denn ich hatte schon seit einer Weile vor, mit ihr zu reden."


"Es ist eine gute Gelegenheit, aber ich glaube, ich sollte es zumindest so aussehen lassen, als ob ich etwas dagegen hätte."


hide shizu onlayer master
with charaexit

"Ich wende mich wieder meinem Arbeitsblatt zu und hänge sofort an der dritten Aufgabe fest. Nachdem ich eine Weile erfolglos herumgerechnet habe, werfe ich beiläufig meinen eigenen Zettel zu Shizune. Darauf steht:"


window hide

$ written_note("Warum ist Misha abwesend? Und was ist die Antwort auf Frage 3?")


show shizu behind_blank onlayer master at center
with charaenter

window show

ssh "Sie sagte mir, dass sie krank ist und Magenschmerzen hat. Sie bekommt oft Bauchschmerzen, aber ich wünschte, sie hätte sich diese Woche einen besseren Zeitpunkt dafür ausgesucht."


show shizu basic_normal2 onlayer master
with charachange

ssh "Benutz Zeichensprache."


"Ich glaube, dass die Bauchschmerzen von dem Parfait gestern kommen. Das Ding war größer als ihr Kopf, und sie hat es außerdem noch in Windeseile verschlungen."


"Aber wenn sie die so oft bekommt, ist es entweder ein Zufall oder sie hat die Angewohnheit, Dinge zu essen, die ihr lähmende Schmerzen bereiten können."


"Ich bemerke, dass der Lehrer uns missbilligend ansieht. Ich kann es ihm nicht verübeln. Wir „reden” im Unterricht, und mit Zeichensprache auf eine ziemlich auffällige und ablenkende Weise."
"Ich räuspere mich, um die Unterhaltung zu beenden, doch Shizune bekommt das nicht mit."


"Na ja, offensichtlich. Bevor ich versuche, die Botschaft noch einmal mit meinen Händen zu übermitteln, begreife ich, dass Shizune weiß, was los ist – es kümmert sie nur nicht."


show shizu adjust_smug onlayer master
with charachange

ssh "Willst du immer noch die Antwort zu Frage drei wissen? Ich sage sie dir, aber du musst mir dann die Antwort zu Frage 25 geben."


his "Hey, ich dachte gerade daran, wie ein Lehrer ohne Zeichensprachekenntnisse denken könnte, dass wir sie zum Schummeln missbrauchen, falls er das Schlimmste annimmt."
his "Ich kann nicht fassen, dass du genau das tust! Und bei 25 bin ich noch nicht."


show shizu behind_frown onlayer master
with charachange

ssh "Du wolltest wissen, was die Antwort zu Frage drei ist; du hast zuerst gefragt. Heuchler."


his "Du bist die Schülerratspräsidentin, du darfst nicht schummeln."


"Ich habe dafür keine Zeit, und ich vermute, dass ich die Geduld des Lehrers an ihre Grenzen bringe."
"Ich würde gerne weiter Seitenhiebe an sie austeilen, während ich an den Matheaufgaben vor mir arbeite, aber dafür würde ich mindestens zwei weitere Hände brauchen."


show shizu basic_normal onlayer master
with charachange

"Shizune hingegen ist etwas kreativer und umgeht diese Einschränkung, indem sie lange, halb gebrochene Sätze mit schlichteren Worten benutzt."
"Während mir von einigen besonders langen Gleichungen schwindlig wird, mache ich mir ein paar mentale Notizen."


show shizu adjust_smug onlayer master
with charachange

play sound sfx_impact2
with vpunch

"Kurz bevor die Glocke läutet, kappt sie ihren Füller und schmeißt ihn mit einem ohrenbetäubenden Knall triumphierend auf ihren Schreibtisch, was den ganzen Raum zusammenzucken lässt."
"Doch das ist schnell vergessen, da alle lieber in die Mittagspause gehen wollen, anstatt dem Ursprung des Geräuschs nachzugehen."


stop music fadeout 6.0

show shizu basic_normal_close onlayer master at twoleft
with characlose

"Nachdem sie sich ein paar Mal kurz gestreckt hat, steht sie auf und beugt sich über meine linke Schulter."


show shizu behind_frown_close onlayer master
with charachange

ssh "Bist du immer noch nicht fertig? Ich wollte dich fragen, ob ich deins auch gleich mit abgeben soll, wo ich schon aufstehe."


his "Es hat mich jemand abgelenkt. Ich musste den Lehrer anflehen, dass er mir neun Minuten zwischen jetzt und der Abgabezeit gibt, damit ich es fertig bekomme."
his "Übrigens ist es nicht einfach, es mit einer Hand zu lösen, während man mit der anderen eine Unterhaltung führt."


"Da er genauso sehr raus wollte wie ich, hat ihn diese Bitte nicht begeistert."


"Da ich nur noch eine Aufgabe zu lösen habe, sieht es aus, als würde mir Shizune nicht wirklich glauben. Sobald ich das fertige Blatt abgegeben habe, werde ich zum Schülerratsraum geschleift."


scene bg school_council onlayer master
with locationskip

play music music_happiness fadein 2.0

"Er ist unheimlicher- und ärgerlicherweise aufgeräumt. Ich kann nicht mehr finden, woran ich gestern gearbeitet habe."


his "Wo ist alles hin?"


show shizu behind_blank onlayer master at center
with charaenter

ssh "Ich hab etwas aufgeräumt."


his "Das sagt mir nichts. Das ist, als hättest du sogar vergessen, wo du die Sachen hingelegt hast, die du weggeräumt hast. Ach na ja, wenn ich es nicht finden kann, gehe ich am besten nach Hause."


show shizu basic_normal2 onlayer master
with charachange

ssh "Sie sind in dieser Schublade dort."


"Shizune schmollt, als ich die Poster heraushole, an denen ich gearbeitet habe. Dann sortiere ich sie etwas um, da sie sie nach Farben sortiert hat."
"Ich will sie damit nicht necken, ich habe nur mein eigenes System – auch wenn ich bezweifle, dass sie mir das glauben würde."


his "Ich mag es, wenn Dinge etwas unordentlich sind. Es ist natürlicher. Und es spart Zeit. Lass das Zeug einfach da, wo ich es liegengelassen habe, dann muss ich nicht die Schränke durchsuchen, nur um zu finden, woran ich gestern gearbeitet habe."


show shizu adjust_frown onlayer master
with charachange

ssh "Faul."


his "Das stimmt nicht. Ich bin nicht faul, du übertreibst nur einfach immer."


"Ich werfe einen kurzen Blick auf ihren Schreibtisch."
"Ein sorgfältig auf der Ecke platzierter Notizblock, dahinter ein kleiner Tischkalender, auf dem jedes Feld mit ordentlich aber mikroskopisch klein geschrieben Notizen versehen ist. Rechts sind drei Stiftschachteln – in blau, schwarz und rot."


his "Schau mal, du legst am Ende jedes Tages sogar die Stifte zurück in ihre ursprüngliche Schachtel – nach Farben geordnet und so. Ich glaube, das geht über normale Ordnungsliebe hinaus."


show shizu behind_frown onlayer master
with charachange

ssh "Was machst du denn mit ihnen? Schmeißt du sie in eine Tasse auf deinem Schreibtisch?"


his "Hey, ich finde, das ist aufgeräumt genug."


show shizu basic_frown onlayer master
with charachange

ssh "Du bist so unorganisiert, du kannst nicht einmal dein Haar richtig kämmen."


his "Das tut weh…"


"Es ist nicht so, als ob ich es nicht versuchen würde; sie wollen einfach nicht flach bleiben."
"Ich greife nach einer Stiftschachtel lasse sie fix aufploppen, um zu sehen, ob sie sie auch alle in die gleiche Richtung zeigend hineinlegt. Sie begreift, was ich denke und sieht nicht sehr erfreut aus."


play sound sfx_dropstuff

"Es stellt sich heraus, dass die Schachtel am Boden nicht richtig geschlossen war, und sobald ich sie aufhebe, fallen die Stifte wie ein Wasserfall heraus."


his "Mein Fehler. Ich heb sie auf, keine Sorge."


stop music fadeout 4.0
play sound sfx_impact

show shizu adjust_blush_close onlayer master
with vpunch

"Ich beuge mich nach unten, um die Stifte aufzuheben und vergessen dabei, dass sie mit ihrer auf die Stifte gerichteten Aufmerksamkeit unmöglich meine Gesten gesehen haben kann."
"Shizunes Kopf stößt gegen meine Brust – nicht allzu heftig, aber es bringt mich genug aus der Balance, dass ich hinfalle."


show shizu adjust_blush onlayer master
with charadistant

"Ich tue es mit einem Lachen ab und erwarte, dass sie dasselbe tut. Als sie stattdessen erstarrt und sich von mir entfernt, beschleicht mich ein Gefühl der Furcht."


"Das ist eine seltsame Reaktion. Ich fange an, mich zu fragen, warum sie sich so verhält. Es ist ziemlich offensichtlich: Sie ist gerade mit dem Kopf voran mit jemanden zusammengestoßen, der eine Herzkrankheit hat."



label de_S26a:

"Da sie die Reihen und Berge von Tablettenfläschchen auf meinem Nachttisch gesehen hat, wird sie wissen, dass ich eine habe."
"Oder zumindest weiß sie, dass ich etwas so Schwerwiegendes habe, dass ich so viele Medikamente brauche, was man aber nicht auf den ersten Blick erkennt."



label de_S26b:

"Shizune wird wissen, dass ich eine habe – vielleicht durch die Akten, zu denen sie als Mitglied des Schülerrats Zugriff hat. Zumindest wird sie wissen, dass ich etwas so Schwerwiegendes habe, dass ich unter medizinischer Beobachtung stehe."



label de_S26c:

"Also behandelt sie mich, als wäre ich aus Glas. Für sie ist es eine normale Reaktion. Ich habe nicht vergessen, wie sie ausgeflippt ist, als Emi mich umgerannt hat. Warum sollte es bei ihr anders sein?"


show shizu basic_normal onlayer master
with charachange

"Ich bin mir sicher, dass sie sich gerade daran erinnert. Ich kann es in ihrem Gesicht sehen. Sie scheint wütend auf sich selbst zu sein."


"Es wäre eine gute Gelegenheit, diesen Zusammenstoß anzusprechen. Ich will das zwar nicht wieder aufrollen, aber es wäre eine gute Idee. Es würde reinen Tisch machen."


"Trotzdem habe ich Angst und sage letztendlich nichts. Zum Teil weil ich mir vorstelle, wie ich ihre Aufmerksamkeit vom Boden auf mich lenken und dann gebärden muss, was für eine Art von Krüppel ich bin. Der Gedanke wird immer deprimierender."


hide shizu onlayer master
with charaexit

"Um ihn aus den Kopf zu kriegen, setze ich mich und beschließe, diese Poster fertigzustellen."
"Es sind einige dabei, an die ich mich nicht erinnern kann. An der superfeinen Handschrift, die von Rand zu Rand quer über die Poster geht, kann ich erkennen, dass Shizune sie gemacht haben muss."


"Das heißt, dass die Übrigen von Misha gemacht worden sein müssen. Sie sind viel effektvoller und mit kleinen Chibi-Bildern von uns versehen."
"Ich weiß nicht, was ich davon halte, als Maskottchen benutzt zu werden, aber ich bin nicht wirklich begeistert davon."


scene bg school_council_ss onlayer master
with shorttimeskip

play music music_tranquil fadein 3.0

"Einige Zeit vergeht – so lange, dass die Sonne draußen schon untergeht."
"Ich höre, wie Shizune ihren Stift weglegt und systematisch ihre Knöchel knacken lässt – einen nach dem anderen. In der Stille des Raumes ist es so laut, dass ich mich frage, ob sie meine Aufmerksamkeit sucht und blicke auf."


show shizu behind_blank_ss onlayer master
with charaenter

"Obwohl es nicht das war, was sie beabsichtigt hatte, fängt sie direkt an zu gebärden, als sich unsere Blicke kreuzen."


show shizu basic_normal_ss onlayer master
with charachange

ssh "Lass uns eine Pause machen."


his "Überrascht mich, dass du so etwas sagst."


show shizu adjust_happy_ss onlayer master
with charachange

ssh "Ist schon in Ordnung. Wir sind eh fast fertig. Und ich hab Hunger. Du auch?"


his "Ein bisschen."


show shizu basic_normal2_ss onlayer master
with charachange

ssh "Ich bin wirklich hungrig."


his "Wir könnten etwas bestellen."


show shizu behind_smile_ss onlayer master
with charachange

ssh "Ich hab an dich gedacht. Ich hab schon etwas zu essen dabei."


his "Wo denn?"


show shizu adjust_smug_ss onlayer master
with charachange

"Sie holt ein Zimtbrötchen unter dem Tisch hervor und hebt es langsam auf Kopfhöhe – wie ein Zauberer, der einen Stein schweren lässt."


show shizu behind_smile_ss onlayer master
with charachange

ssh "Aber!"


show shizu basic_sparkle_ss onlayer master
with charachange

ssh "Es gibt nur eins. Nicht genug für uns beide."


"Ah, wie dramatisch. Ich weiß, was das bedeutet. Mich beschleicht ein Gefühl von Déjà-vu."


his "Wir könnten es einfach teilen."


show shizu adjust_frown_ss onlayer master
with charachange

ssh "Das. Macht. Keinen. Spaß. Langweilig! Lass uns Shogi drum spielen."


"Und schon ist das Spielbrett hervorgeholt. Dieser Schreibtisch muss alles haben."


his "Nicht Schach?"


show shizu behind_smile_ss onlayer master
with charachange

ssh "Bei Schach sind die Beförderungen so langweilig. Das ist bei Shogi interessanter."


his "Wenn du meinst… Na ja, eigentlich bin ich ziemlich gut in Shogi, also soll es mir recht sein."


show shizu basic_happy_ss onlayer master
with charachange

ssh "Wirklich? Okay, dann können wir es etwas spannender machen. Jeder Zug muss innerhalb von dreißig Sekunden gemacht werden. Du darfst auch eine Regel hinzufügen."


his "Nein danke. Alles, was mir einfallen würde, würde mir eher schaden als helfen. Ein Dreißig-Sekunden-Zeitlimit ist schon zu knapp für mich."


his "Du lässt mich meine kleine Angeberei langsam bedauern."


scene bg school_council_ss onlayer master
show shizu basic_normal_close_ss onlayer master at center
with shorttimeskip


"Shizune darf nach einem Münzwurf den ersten Zug machen und fängt sofort damit an, all ihre Spielfiguren so schnell wie möglich aufzuwerten."
"Es wirkt wie ein ziemlich simpler Spielstil, und mir bleibt nichts anderes übrig, als es für eine Falle zu halten."


"Doch es ist keine. Was Shizune an diesem Spiel so reizt scheint die Tatsache zu sein, dass sie ihre Figuren aufwerten und meine stehlen kann. Sie ist sehr gut darin, aber das macht sie vorhersehbar."
"Letztendlich bin ich etwas besser, als ich erwartet hätte."


"Dennoch ist dieses Dreißig-Sekunden-Zeitlimit ziemlich mühsam. Das Spiel endet unentschieden. Ich denke, in dieser Situation würde man normalerweise noch einmal spielen oder die Punkte der Figuren zählen."


"Der Zeit wegen will Shizune nicht noch einmal Spielen, aber durch Punkte zu gewinnen stellt sie offensichtlich nicht zufrieden."


show shizu adjust_frown_close_ss onlayer master
with charachange

stop music fadeout 4.0

"Sie sitzt da, schiebt einen silbernen General von einem Ende zum anderen und überlegt, welche von den zwei Optionen sie wählen soll. Es dauert so lange, dass ich den Eindruck bekomme, dass sie die Wette vergessen hat."


"Schließlich hört sie auf, mit der Shogifigur herumzufummeln und legt sie hin."


show shizu behind_blank_close_ss onlayer master
with charachange

ssh "Ist Misha sauer auf mich?"


"Das kam jetzt wirklich plötzlich."


play music music_pearly fadein 5.0

"Shizunes Offenheit ist verwirrend – denn bei ihr ist diese Art von Offenheit ein Zeichen einer ernsten Situation."
"Sie hat kein verspieltes Lächeln auf ihrem Gesicht; stattdessen schaut sie mich mit ihrer stoischen Maske der Konzentration an – als wolle sie prüfen, ob ich ihr ehrlich antworte oder nicht."


"Es kränkt mich, dass sie das von mir denkt. Aber ich weiß nun, dass sie sich wohl vor Kurzem gestritten haben, als ich nicht dabei war, und es gibt mir ein warmes Gefühl, dass sie sich so umeinander sorgen."


his "Nein. Das bezweifle ich stark."


his "Wusstest du, dass sie denkt, dass du sauer auf sie bist?"


show shizu behind_sad_close_ss onlayer master
with charachange

"Shizune nickt langsam und widerwillig."


show shizu basic_normal2_close_ss onlayer master
with charachange

ssh "Ja."


his "Sie hat es nicht so direkt gefragt wie du. Irgendwie überrascht mich das, denn ich dachte, du wärst diejenige, die gerne Spielchen spielt."


show shizu behind_blank_close_ss onlayer master
with charachange

ssh "Nicht immer."


"…"


his "Streitet ihr euch wegen irgendetwas?"


show shizu adjust_frown_close_ss onlayer master
with charachange

ssh "Nein."


"Sie verneint es abrupt und ist nicht glücklich über diesen Gedanken. Mir kommt es vor, als wäre ich auf eine Landmine getreten."


show shizu behind_sad_close_ss onlayer master
with charachange

ssh "Tut mir leid. Eigentlich ja. Wegen einer Kleinigkeit."


show shizu behind_blank_close_ss onlayer master
with charachange

ssh "Ich weiß, dass sie kein Interesse am Schülerrat hat. Sie ist nur meinetwegen beigetreten. Ich bin immer noch dankbar dafür. Ich bin so glücklich, dass sie meine Freundin ist. Aber ich verstehe nicht, was diesmal ihr Problem ist."


his "Warum fragst du sie nicht einfach?"


show shizu basic_normal2_close_ss onlayer master
with charachange

ssh "Sie wird es mir nicht sagen. Ich werde es stattdessen selbst herausfinden. Ich war mir sicher, dass ich sehr scharfsinnig bin, auch wenn ich nicht hören kann. Das war dumm. Nun weiß ich es besser."


show shizu behind_sad_close_ss onlayer master
with charachange

ssh "Es ist wahrscheinlich etwas, an dem ich schuld bin."


stop music fadeout 8.0

"Shizune geht nicht weiter ins Detail oder erklärt, was es gewesen sein könnte. Ich bin mir sicher, dass das daran liegt, dass sie die Situation selbst nicht ganz versteht."


"Es ist seltsam zu sehen, dass die sonst so selbstsichere Shizune durch einen kleinen Streit mit einer Freundin so beunruhigt werden kann. Aber je mehr ich darüber nachdenke, desto mehr Sinn ergibt es."


"Sie sind sich viel näher als gewöhnliche Freunde, und Shizune ist auf eine Art ziemlich von anderen Leuten isoliert. Dass sie taub ist, spielt darin keine kleine Rolle."


"Aber ich bekomme das Gefühl, dass sie Misha als Puffer zwischen sich und anderen Menschen benutzt – nicht nur, weil es ihr aufgezwungen wird, sondern weil sie es selbst so will."
"Sie kann mit ihrem kleinen Block ausreichend gut kommunizieren. Sie hasst es nur. "


"Wenn man so lange durch eine dritte Person redet, verliert man irgendwann den Bezug, schätze ich. Es scheint unvermeidlich. Es ist gar kein so abwegiger Gedanke, dass sie nicht so gut mit Menschen umgehen kann."


hide shizu onlayer master
with charaexit

"Ich mache mich wieder an die Arbeit. Mit jeder Sekunde, die vergeht, will ich das Zimtbrötchen immer mehr, aber als ich die restlichen Shogifiguren auf Shizunes Tisch zähle, kann ich auf einen Blick erkennen, dass sie gewinnen würde."


"Falls wir ein Rückspiel machen würden, wäre ich auch zu hungrig, um mich zu konzentrieren. Durch meinen Wunsch, hier fertig zu werden und etwas zu essen, gebe ich den letzten Postern den letzten Schliff."


his "Fertig. Ich glaube, so viele reichen aus. Zu viele könnten übertrieben wirken."


play music music_shizune fadein 3.0

show shizu behind_blank_ss onlayer master at center
with charaenter

ssh "Okay."


his "Sonst nichts? Nur „okay”?"


show shizu adjust_frown_ss onlayer master
with charachange

shi "…?"


show shizu behind_blank_ss onlayer master
with charachange

ssh "… Wahrscheinlich werde ich selbst noch welche machen, nachdem ich das Wahlsystem ausgesucht hab."


his "Aaarghh. Zu viele Poster sind auch schlecht. Hast du noch nie von Übersättigung gehört?"


his "Ich glaube, du übertreibst es wirklich."


show shizu basic_normal_ss onlayer master
with charachange

"Sie wölbt ihre Finger und sieht dabei aus, als würde sie es fast selbst zugeben."


show shizu behind_blank_ss onlayer master
with charachange

ssh "Vielleicht."


his "Misha denkt das auch."


show shizu basic_normal2_ss onlayer master
with charachange

"Ich sehe zu, wie ihre Finger sich umeinander winden und aneinander ziehen, als würden sie einen Miniaturkrieg führen."


his "Es macht mir nichts aus, aber ich habe heute in ein paar Klassen herumgefragt und das Interesse ist gering. Es ist wie du gesagt hast. Daher…"


show shizu adjust_frown_ss onlayer master
with charachange

ssh "Ist meine Arbeit deswegen falsch?"


his "Nein. Aber… es macht sie irgendwie sinnlos."


show shizu basic_angry_ss onlayer master
with charachange

ssh "Ist sie nicht."


"Ja, aber für wen? Ich bezweifle, dass Shizune selbst das wirklich glaubt."


show shizu behind_frustrated_ss onlayer master
with charachange

ssh "Ich mache diese ganze Arbeit nicht nur für mein Ego."


his "Das meine ich nicht."


"Seit Tagen die erste Gelegenheit, mit ihr allein zu sein, und ich habe sie schon richtig versaut. Trotzdem sieht sie eigentlich nicht wütend aus."


"Es sieht eher so aus, als wäre sie frustriert, dass sie sich nicht klarer ausdrücken kann. Aber da sie eine Zeichensprache-Expertin ist, glaube ich nicht, dass das der Fall sein kann."


"Ich frage mich, welchen Vorteil ihr das Sprechen bringen würde, und ob sie selbst schon einmal darüber nach gedacht hat."


show shizu basic_frown_ss onlayer master
with charachange

ssh "Es ist ein weiteres meiner Projekte. Genau wie die Festivals. Ich tue es, weil es mein Job ist. Es ist nur, dass eine Schülerratswahl nicht so viel Spaß macht wie ein Festival – darum interessiert sie keinen."


"Sie tappt ihre Fingerspitzen aneinander, als wollte sie sagen: „Aber vielleicht…”. Sie hat irgendwie Recht, aber sie will das Problem wohl nicht mit nur einem simplen Satz zusammenfassen."


show shizu behind_frown_ss onlayer master
with charachange

ssh "Aber das ist mir egal. Ich will, dass die Leute aufgestachelt sind, aber dabei geht es nicht um mich. Ich will damit überhaupt nichts zu tun haben."


his "Was meinst du? Du gehst fast zu jedem Festival."


show shizu adjust_frown_ss onlayer master
with charachange

"Shizune winkt das mit gespielter Empörung ab."


show shizu behind_blank_ss onlayer master
with charachange

ssh " Na ja… ich muss doch auch Spaß haben. Aber weißt du, es ist nicht das Gleiche."


"Wenn sie einen Witz reißen kann, scheint sich ihre Stimmung gebessert zu haben."


show shizu basic_normal2_ss onlayer master
with charachange

ssh "Ich will nicht, das irgendjemand Wert darauf legt, dass ich mit etwas zu tun habe. Es ist nervig. Diese Verantwortung will ich nicht."


show shizu adjust_frown_ss onlayer master
with charachange

ssh "Die Dinge werden so schon langsam kompliziert genug. Je mehr Werbung ich für die Wahlen mache, desto mehr muss ich darin involviert sein."
ssh "Noch will niemand seine Karten offenlegen, und es kommt mir noch nicht so vor, als wäre meine Zeit vorüber - auch wenn sie es sein sollte."


show shizu behind_frustrated_ss onlayer master
with charachange

"Sie lehnt sich zurück, verschränkt ihre Arme und knirscht frustriert mit den Zähnen."


show shizu cross_angry_ss onlayer master
with charachange

ssh "Sie sind alle so faul; es ist unmöglich, sie zum Mitmachen zu bewegen. Überall sonst wären die Wahlen ein aufregendes Ereignis. Es ist unlogisch, warum muss hier jeder so anders sein? Wenn man sie nur irgendwie bestrafen könnte…"


show shizu adjust_angry_ss onlayer master
with charachange

ssh "… Wie zum Beispiel sie an ihren Schreibtisch festketten. Wählen ist Pflicht. Wenn man nicht wählt, wird man ausgepeitscht."


"Furchterregend. Ich frage mich, wie scheinheilig es wäre, wenn ich am Wahltag im Bett bleiben würde. Mit einer Grippe. Und einer Erkältung. Und einer Halsentzündung. Und einem verstauchten Knöchel."


his "Du solltest dich selbst auf eins davon malen."


his "Versteh mich nicht falsch. Nicht als Bestrafung."


"Ich halte eines von Mishas Postern hoch."


his "So wie dieses hier. Ein ziemlich nette Idee. Misha hatte einen guten Einfall. Es ist viel niedlicher als einfach nur Text. Ich denke, dass es dir gefallen würde. Ein kleines Maskottchen zu haben, würde bestimmt für etwas Stimmung sorgen."


show shizu basic_normal_ss onlayer master
with charachange

ssh "Vielleicht wenn es nur Misha ist."


his "Warum nicht ich? Jemand sagte mir, dass diese Schule etwas mehr Mädchen als Jungs hat… Diese Gruppe musst du auch bedienen."


show shizu adjust_blush_ss onlayer master
with charachange

"Diesmal kichert Shizune hörbar. Ich bin überrascht, und als sie mein Gesicht sieht, ist sie es ebenfalls. Ihr Gesicht läuft rot an. Es war ihr peinlich, dass sie ein Geräusch von sich gegeben hat. Ich war auch – gelinde gesagt – ziemlich verwirrt."



his "Warum malst du dich nicht selbst drauf?"


"Sie winkt meine Frage einfach ab."


show shizu basic_angry_ss onlayer master
with charachange

ssh "Es ist lästig."


his "Was meinst du mit lästig? Jeder weiß, dass du im Schülerrat bist."


"Mein Magen knurrt. Ich bin wohl noch hungriger, als ich gedacht habe. Shizune nutzt den Moment, um von meiner Frage abzulenken, indem sie das Thema wechselt."


show shizu behind_blank_ss onlayer master
with charachange

ssh "Stimmt etwas nicht?"


his "Nein. Mein Magen hat nur geknurrt."


show shizu basic_normal_ss onlayer master
with charachange

ssh "Ach so."


"Sie schaut auf das vergessene Gebäck auf dem Tisch und runzelt dann die Stirn. Sie findet es wohl unzureichend für zwei Personen."


show shizu adjust_happy_ss onlayer master
with charachange

ssh "Lass uns zum Shanghai gehen, wenn du so hungrig bist. So spät könnte es etwas voll sein, aber Yuuko arbeitet heute dort. Wir kriegen auf jeden Fall einen Tisch."


"Da ist etwas besorgniserregend Hinterlistiges hinter diesem Lächeln."


his "Passe. Ich bin diese Woche schon zweimal hintereinander da gewesen."



show shizu basic_frown_ss onlayer master
with charachange

"Shizune schmollt und lehnt sich gegen ihren Schreibtisch, während sie eine abwehrende Haltung einnimmt."


his "Was denn?"


show shizu adjust_frown_ss onlayer master
with charachange

ssh "Ich bin enttäuscht, dass du nein gesagt hast."


his "Na ja, ich kann nicht immer deiner Meinung sein."


show shizu behind_frown_ss onlayer master
with charachange

ssh "Du sagst sowieso viel zu selten deine Meinung. Es wäre am einfachsten für mich, wenn es so wäre, aber nicht sehr interessant, oder? Es gibt ein paar Entscheidungen, bei denen du mir widersprechen solltest. Du hast die Pflicht dazu."


his "Wie soll ich wissen, welche das sind?"


show shizu basic_normal_ss onlayer master
with charachange

ssh "Das ist einfach."


his "Nein, ist es nicht. Manchmal fällt es mir schwer zu sagen, ob du scherzt oder es ernst meinst."


stop music fadeout 9.0

"Obwohl – da sie komplett in Zeichensprache kommuniziert, wäre es ziemlich offensichtlich. Aber ich würde nicht sagen, dass das alles ist."


"Ich erinnere mich an meine Herzattacke. Iwanako wollte anfangs einfach nicht aufhören zu reden. Schließlich wünschte ich mir einfach nur noch, dass sie die Klappe hält."
"Zumindest hätte ich das, wenn ich nicht über jegliche Gesellschaft glücklich gewesen wäre. Nach und nach verfloss aber meine Dankbarkeit darüber."


"Als wir uns unterhielten, fühlte es sich lediglich an wie ein ritualisierter Austausch von Höflichkeiten. Iwanako hat sich große Mühe gegeben, ihre Gefühle zu verschleiern – die Gefühle, dass ich ein hoffnungsloser Fall war."
"Am Ende glich ihr äußeres Verhalten ihren inneren Gefühlen."


"Aus diesem Grund war ich in der Lage, es zu akzeptieren, als sie eines Tages nicht mehr auftauchte. Zu diesem Zeitpunkt hat es mich nicht mehr überrascht."
"Auch wenn sie sich selbst für einen Meister im Gefühle-Verstecken hielt, war ich nicht überrascht."


"Ich habe gehört, dass Spiele wie Shogi und Schach einem viel über einen Menschen verraten können. Ich wünschte, ich wüsste, was sie Shizune über mich gesagt haben."


"Es könnte sein, dass ich Iwanako etwas ähnlicher bin, als mir lieb ist… Ich schlage vor, dass wir uns was zu Essen kommen lassen."


scene black onlayer master
with dissolve



label de_S27:

scene bg school_hallway2 onlayer master
with locationchange

"Am nächsten Tag gehe ich in der Mittagspause zu meinem gewohnten Verkaufsautomaten, nur um festzustellen, dass mein Lieblingsgetränk bereits ausverkauft ist."
"Er ist so weitab von den meisten Klassenzimmern, zwischen einer Abstellkammer und der Bibliothek, dass ich dachte, dass fast niemand von ihm weiß."


"Ich hatte erwartet, dass ein in der Nähe der Bibliothek stehender Verkaufsautomat reichlich Kunden hat. Allerdings ist die Bibliothek die meiste Zeit ausgestorben, und wenn jemand kommt, sucht er nur nach etwas, um seine Referate zu füllen."


"Niemand bleibt länger dort, als es absolut nötig ist. Im letzten Monat hat mir das in die Hände gespielt, aber der Nachteil bei einem Automaten, von dem niemand etwas weiß, ist, dass er nie aufgefüllt wird."


play sound sfx_can

"Ich entscheide mich für eine Dose Orangenlimo und beschließe, sie hier zu trinken, anstatt damit zu warten, bis ich in der Cafeteria bin. Dann öffnet sich die Bibliothekstür neben mir."


show yuuko worried_down onlayer master at center
with charaenter

yu "Ah…"


show yuuko worried_up onlayer master
with charachange

yu "Ich habe nach dir gesucht!"


play music music_happiness fadein 2.0

"Yuuko scheint heute viel selbstsicherer zu sein als sonst, aber es ist nicht von Dauer: Gleich darauf fällt sie zurück in ihr leises Murmeln."


show yuuko worried_down onlayer master
with charachange

yu "B-Bring deine Bücher zurück, bitte. Ich meine… die Bibliotheksbücher. Die Bücher, die du ausgeliehen hast, sind längst überfällig. Manche von ihnen stehen auf der Warteliste…"


hi "Ups. Vergessen. Ich leihe immer neue aus, aber vergesse, die alten zurückzubringen."


show yuuko neurotic_up onlayer master
with charachange

yu "Das passiert mir andauernd in der Universitätsbibliothek, es ist so peinlich."


hi "Schicken sie dort auch jemanden los und versuchen, die Ausleiher zum Zurückbringen zu bewegen?"


show yuuko worried_up onlayer master
with charachange

yu "Nein… die Universität ist größer. Sie bemerken es nicht, wenn ich etwas länger als erlaubt ausleihe. Das ist praktisch, denn ihre Regeln über das zu lange Ausleihen vom Büchern sind… wirklich streng. Strenger als hier."


"Mir gefällt es, dass sie, obwohl sie das sagt, selbst irgendwie keine Probleme damit hat, Bücher zu lange auszuleihen. Das lässt sie, was meine eigene Abgabeverspätung betrifft, etwas scheinheilig wirken. Schätze, sie weiß, wie ich denke."


"Als sie die Bedeutung ihrer Worte ungefähr im gleichen Moment wie ich erkennt, verstummt sie und fängt an, wild mit den Armen herumzufuchteln."


show yuuko panic_up onlayer master
with charachange

yu "… Ähm… Äh… Das ist etwas anderes… als diese Situation! Es ist vollkommen anders…"


"Yuuko starrt für einen Augenblick auf ihre Nägel, als wollte sie auf sie beißen, reißt sich dann aber doch zusammen."


show yuuko worried_down onlayer master
with charachange

yu "Zum Beispiel die Ausleihdauer… Du hast manche dieser Bücher vor Monaten ausgeliehen, Hisao. Entschuldigung… es ist nur so, dass andere Leute sie auch lesen wollen. Wenn du aber nur ein langsamer Leser bist, ist das okay…"


hi "Nein, das ist voll und ganz mein Fehler. Um ehrlich zu sein, hab ich ein paar davon nicht mal gelesen. Ich sollte nicht immer weiter Bücher ausleihen, wenn ich noch Rückstände habe."


yu "Das ist nicht gut…"


hi "Nein, das ist es wirklich nicht…"


"Jetzt fange ich auch schon an, ihre Angewohnheit zu kopieren, zum Satzende hin immer leiser zu werden. Ihre Unbeholfenheit ist aus irgendeinem Grund sehr ansteckend."


"Abgesehen davon bin ich erstaunt. Yuuko scheint heute fast normal zu sein, auch wenn ab und zu ihre nervösen Ticks aus ihrem Kellnerjob auftauchen."


"Wenn ich es mir recht überlege, war sie nicht so, als wir uns zum ersten Mal getroffen haben. Sie war etwas tollpatschig und neurotisch, aber es war nicht annähernd so heftig, bis Shizune, Misha und ich sie im Shanghai getroffen haben."


"Es könnte sein, dass es Yuuko peinlich ist, wenn Kinder von der Schule sie beim Kellnern sehen."


"In dem Fall war es etwas seltsam von ihr, dass sie sich das der Schule am nächsten liegende Café zum Arbeiten ausgesucht hat. Wenn das so ist, ist es vielleicht ein Glücksfall, dass dieser Laden so wenige Kunden hat."


hi "Na ja, ich verstehe. Ich werde sie direkt nach der Schule zurückbringen."


show yuuko smile_up onlayer master
with charachange

yu "Bitte so bald wie möglich."


show yuuko worried_up onlayer master
with charachange

yu "Ähm… warte, kann ich dich noch um etwas bitten?"


hi "Klar, was denn?"


show yuuko worried_down onlayer master
with charachange

yu "Ich… ich muss für eine Weile weg, aber ich kann die Bibliothek nicht einfach unbeaufsichtigt lassen…"
yu "Entschuldige, aber könntest du aufpassen, während ich weg bin? Es ist nur für einen kurzen Moment und ich werde so schnell wie möglich zurück sein! Du bist im Schülerrat, darum bin ich mir sicher, dass es okay ist, wenn du es tust."


hi "Okay, ich tue es, mach dir keine Sor…"


show yuuko closedhappy_up onlayer master
with charachange

yu "Ich danke dir!"


show yuuko neurotic_up onlayer master
with vpunch

"Yuuko bewegt sich nach vorne, als ob sie so dankbar wäre, dass sie mich umarmen will, stoppt aber nach zwei Zentimetern, was die Bewegung letztlich sehr verwirrend aussehen lässt."


"Ich bin auch davon überrascht, dass sie so eine gute Körperbeherrschung hat, da sie scheinbar etwas tollpatschig ist."


hide yuuko onlayer master
with charaexit

stop music fadeout 6.0

"Bevor ich so etwas wie „gern geschehen” sagen kann, stürmt sie bereits los, als ob sie zu spät zu einer Verabredung kommen würde."


"Das könnte der Fall sein, aber ich kann mir da nicht ganz sicher sein. Es ist Yuuko, und sie scheint ein Mensch zu sein, der alles auf diese Weise angeht."


scene bg school_library onlayer master
with locationchange

"Jetzt, wo ich in der Bibliothek bin, komme ich mir etwas albern vor. Ich weiß nicht wirklich, was ich machen soll."
"Soll ich mich wie sonst auch hinsetzen und etwas lesen? Das würde wahrscheinlich reichen, aber es würde nicht Yuukos hohen Standards entsprechen."


"Vielleicht sollte ich mich an den Bibliothekartisch setzen und jedem, der hereinkommt, einen strengen und prüfenden Blick zuwerfen. Fürs Erste ahme ich den von Shizune nach und übe ein paar Mal mit der reflektierenden Fläche eines Stiftes."


"Ich finde, es sieht ziemlich gut aus. Frustrierenderweise kommt aber niemand herein, darum gebe ich die Idee schnell wieder auf und beschließe, mich stattdessen nach Hanako umzusehen."


"Es ist wie ausgestorben. Einmal denke ich, da wäre noch jemand, aber als ich einmal blinzele, ist die Person verschwunden."
"Ich bin gerade zu Yuukos Tisch zurückgekehrt und habe ein interessant aussehendes Buch aufgeschlagen, als sich eine mir vertraute Person in mein Blickfeld schiebt."


show kenji invis onlayer master:
    center
    xpos 0.4
with None

show kenji tsun onlayer master at center
with dissolvecharamove

play music music_kenji fadein 0.5

ke "Yo, Bibliothekar, ich hab dich gesucht – seit ungefähr zehn Minuten. Was? Du bist es? Mann, du musst ziemlich herumkommen, oder der Schülerrat sorgt dafür, dass du herumkommst. Diese Schlampen! Wie können sie nur?"


show kenji rage onlayer master
with charachange

ke "Sklaventreiberinnen!"


"Er muss übertreiben, da es mich nur dreißig Sekunden gekostet hat, eine langsame Runde durch den ganzen Raum zu machen. Aber dieser Gedanke wird durch meine Verwunderung, ihn hier zu sehen, nichtig gemacht."


hi "Wo bist du hergekommen? Was machst du hier?"


show kenji tsun onlayer master
with charachange

ke "Was? Darf ein Mann jetzt nicht mehr in die Bibliothek gehen? Kann ich nicht mal mehr in die Bibliothek gehen, ohne von so einem Jüngling wie dir deswegen verhört zu werden?"
ke "Ich sehe immer, wie ein Mädchen hier die ganze Zeit reinkommt, aber nie fragt sie jemand, was sie hier treibt."


ke "Ist es, weil sie liest und ich nicht?"


"Er muss Hanako meinen. Auch wenn sie beide andere Leute meiden, will ich ihm sagen, dass Bibliotheken üblicherweise zum Lesen da sind. Wenn er also nichts liest, dann lässt ihn das wesentlich verdächtiger aussehen als sie."


"Doch am Ende bin ich von seinem Erscheinen quasi aus dem Nichts zu überrascht."


hi "Das… Das sagt mir nicht, was du hier treibst."


show kenji neutral onlayer master
with charachange

ke "Ich bin deinetwegen hier."


"Seine Antwort verwirrt mich. Vielleicht bin ich eingeschlafen, und das alles ist nur ein komischer Traum, und dieser Kenji ist nicht echt, sondern in Wirklichkeit mein Unterbewusstsein."
"Wird er mir jetzt einen tiefgründigen aber vage formulierten Rat geben?"


show kenji tsun onlayer master
with charachange

ke "Deinetwegen wurde ich von Feministinnen aus meinem Wohnheim gejagt. Nun durchstreife ich diese Bibliothek wie ein Soldat ohne Land, oder wie ein Geist. Ich sollte dich heimsuchen, weil du mir alles ruiniert hast."


"Schade, es wäre eine interessanter Traum gewesen, aber es scheint, als wäre das hier die Realität."


ke "Ja, du musstest ja anfangen mit Frauen zu arbeiten, und das hat sie vor meine Tür gebracht."
ke "Erinnerst du dich daran? Weil du da warst, solltest du es. Von diesem Tag an wusste ich, dass sie mir auf der Spur waren. Ich hätte meinen Instinkten vertrauen sollen, aber ich war jung und dumm."


hi "Das ist nicht mal eine Woche her."


ke "Dann hat mein Papa angerufen und gesagt, dass einer meiner Briefe nicht angekommen ist. Das Postbüro kann ihn nicht verloren haben, darum muss er abgefangen worden sein. Informationskrieg!"


show kenji neutral onlayer master
with charachange

ke "Da wusste ich, dass mein Geheimversteck kompromittiert war. Jetzt bin ich auf der Flucht – wie ein Flüchtling. Es ist Alarmstufe Rot."


hi "Die Wohnheime sind nicht geheim. Dein Name und deine Zimmernummer stehen an dem Brett direkt beim Eingang."


show kenji rage onlayer master
with charachange

ke "Ich weiß, ich hab's gesehen. Sie sind teuflisch. Warum nicht gleich ein Fahndungs- poster aufhängen wie im Wilden Westen? „Gesucht: Tot oder Lebendig!”. Vermutlich lebendig, damit sie mich klonen oder mich in einen Grashüpfer verwandeln können."


show kenji tsun onlayer master at Position(ypos=1.15)
with Dissolvemove(0.5)

"Er springt ohne Vorwarnung auf den leeren Stuhl mir gegenüber, holt eine Zigarette hervor und fängt an, sie zwischen seinen Fingern zu drehen. Ich habe ihn noch nie zuvor rauchen sehen, darum ist es wahrscheinlich nur zur Show."


ke "Ich kann nicht mal mehr leben, wo ich will. So fängt alles an."


ke "Diese taktische Brillianz… Ich meine, sobald sie in deinem Haus sind, ist es vorbei – wie Termiten. Wenn der feministische Plan zur Herrschaft dort ANFÄNGT, wo zum Teufel können wir dann noch hin?"


show kenji happy onlayer master
with charachange

ke "Die einzige Frage ist, wie sie sich diese Taktik von Termiten abschauen konnten, wenn Frauen naturgemäß von Holz abgestoßen werden."


hi "„Du kannst niemals wieder nach Hause.” Ist das das Sprichwort?"


show kenji neutral onlayer master
with charachange

ke "Mann, mit dem niemals bin ich mir nicht sicher. Ich war gerade da. Ich wüsste nicht, wo ich sonst duschen und mir neue Klamotten holen kann."
ke "Und essen, und das Bad benutzen. Und Fernsehen gucken. Ich muss die Nachrichten sehen, um informiert zu bleiben."


"Für jemanden, der aus seinem Wohnheim verdrängt würde und auf der Flucht ist, hat er jedenfalls keine Hemmungen, mehrmals am Tag für längere Zeit dorthin zurückzukehren."


"Aber nun hat er sich langsam von mir abgewendet und spricht zu einem sich drehenden Schaukasten mit Mord-Krimis. Ihn zu unterbrechen würde wohl nichts bringen, schätze ich."


play sound sfx_can_clatter

"Ich trinke meine Limo aus und werfe die Dose in einen Korb bei der Tür. Sie trifft den Rand, landet aber dennoch drinnen. Ich balle triumphierend meine Faust."


show kenji neutral onlayer master at center
with dissolvecharamove

"Kenji steht rasch auf und fängt an, zur Tür zu gehen. Ich habe nicht wirklich aufgepasst; ich hoffe, ich habe meine Faust nicht zu einem unpassenden Moment geballt."


hi "Wo gehst du hin?"


show kenji tsun onlayer master
with charachange

ke "Du hast die ganze Zeit diesen Saft gesoffen."


hi "Und? Es war nicht einmal Saft, es war Limo. Und jetzt ist sie alle. Was meinst du mit „gesoffen”? Ich hab zwei Schlucke genommen."


ke "Ja, klar, du hattest ungefähr fünfzig Millionen Schlucke."


hi "Das geht nicht mal."


show kenji neutral onlayer master
with charachange

ke "Vielleicht für dich nicht; ich überschreite zu jeder Zeit die Grenzen des Unmöglichen. Okay, wie auch immer, jetzt hab ich auch Durst. Ich geh mir meinen eigenen Saft holen, ich bin sofort wieder da."


show kenji invis onlayer master at Position(xpos=0.4)
with dissolvecharamove

with Pause(0.5)

show kenji neutral onlayer master at center
with dissolvecharamove

"Er ist wirklich fast sofort wieder da – so schnell, dass ich ahne, dass er von meinem geheimen Verkaufsautomaten weiß."


ke "Ich hab dir auch einen geholt. Hoffe, du magst Traubensaft. Jetzt sind wir wegen der Pizza quitt."


hi "Danke."


show kenji neutral onlayer master at Position(ypos=1.15)
with charamove

"Ich will ihm sagen, dass ich ihm etwa das Zehnfache der Kosten einer Dose Traubensaft geliehen habe, aber das würde mich kleinlich wirken lassen."
"Ungehindert setzt sich Kenji hin und beginnt energisch, seinen Saft zu trinken wie ein Mann mit einer Fehde gegen Trauben."


show kenji happy onlayer master
with charachange

ke "Weißt du, es ist für mich ein Glückstreffer, dass ich hier auf dich gestoßen bin, Mann. Ich bräuchte dich für einen Gefallen."


"Obwohl es zynisch ist, frage ich mich, ob er mir diesen Saft nur geholt hat, damit er mich um diesen Gefallen bitten kann. Wenn ja, dann ist es ziemlich durchschaubar und schlecht getimed."
"Ich bezweifle allerdings, dass Kenji etwas so weit durchdenken würde. Geradeheraus um etwas zu bitten, ist eher seine Art."


ke "Ich brauche ein paar Buchempfehlungen von dir."


hi "Aber ich dachte, du liest nicht."


show kenji neutral onlayer master
with charachange

ke "Woher wusstest du das?"


hi "Du hast es mir gesagt. Du sagtest, dass du glaubst, dass die Leute dich diskriminieren, weil du nicht liest."


show kenji happy onlayer master
with charachange

ke "Nun, das tun sie. Und ich lese. Ich lese Hörbücher, denn das ist die Zukunft."


show kenji neutral onlayer master
with charachange

ke "Jedoch muss ich für Literatur ein Buch pro Monat lesen, und ich hab rausgefunden, dass die Schule solche Klassiker wie „Fortgeschrittene Kryptografie” nicht wirklich akzeptiert. Wenn ich nicht ein paar Bücher lese, werde ich durchfallen."


show kenji tsun onlayer master
with charachange

ke "Ich darf bei Literatur nicht durchfallen… Das würde mich ungebildet machen. Das würde bedeuten, dass meine Mutter Recht hatte. Das darf sie nicht. Ich muss einfach so viel Literatur wie möglich lernen."


hi "Kannst du nicht ein paar Zusatzkurse belegen?"


ke "Nein danke. Es ist schon schlimm genug, dass ich jetzt all diese bescheuerten DInger mit mir rumschleppen muss."


"Er greift nach einem Wörterbuch, blättert es durch und stellt es auf das Mord-Krimi Regal hinter ihm."


ke "Ich kann nicht fassen, dass das wirklich das Medium ist, mit dem sich unsere Vorfahren Pornos angesehen haben."


"Ich speie mein Getränk komplett über das Buch, das ich immer noch in den Händen halte, und beschädige es so sehr, dass es nicht mehr wieder in Ordnung zu bringen ist."
"Ich überprüfe rasch den Buchrücken und sehe, dass der empfohlene Verkaufspreis 7.900 Yen ist. Ich glaube, ich kriege eine Herzattacke."



show kenji happy onlayer master
with charachange

ke "Wow, zerstört. Hättest du nicht tun sollen, die nehmen Vandalismus hier superernst. Du wirst was auf die Mütze kriegen."


"Amüsiert gluckst er, bevor er einen einen äußerst langen und lauten Schluck von seiner Saftdose nimmt."


hi "Es ist kein Vandalismus, ich hab es nicht mit Absicht gemacht. Du hast mich mit deinem Statement dazu gebracht."


hi "Und was meinst du mit „was auf die Mütze kriegen”? Ich will nicht verhauen werden."


show kenji neutral onlayer master
with charachange

ke "Warte, entspann dich, ich meinte das nicht wörtlich. Sie werden es dir einfach in Rechnung stellen. Und dich wirklich, wirklich anbrüllen. Es war, als wollten sie mir den Arsch abbeißen. Trotzdem keine große Sache."


hi "Es ist mir egal, ob es nur bildlich gesprochen ist, ich will nicht auf die Mütze oder meinen Arsch abgebissen kriegen, oder sonst irgendeine Bestrafung, du… du Vollpfosten."


hi "Was soll ich tun? Ich bin einzige Person hier. Jedenfalls von der sie weiß. Ich kann das Buch nicht mal in den Müll werfen. Es wird gefunden werden – und dann weiß sie Bescheid."


show kenji tsun onlayer master
with charachange

ke "Verdammt, Alter, hör auf so schräg zu sein."


hi "Warum ist es schräg, keine Strafe zahlen zu wollen?"


ke "Mann, hör auf auszuflippen, Mann."


hi "Ich flippe nicht aus, ich versuche, Geld zu sparen."


ke "Geizhals."


show kenji invis onlayer master at center
with Dissolvemove(0.5)

hide kenji onlayer master
with None

stop music fadeout 1.0

"Ich bin kurz davor ihn zu erdrosseln, als ich Mishas „Wahaha” aus dem Flur kommen höre. Anscheinend hört Kenji es auch, und er nutzt die Gelegenheit, um schnell in der Autobiographie-Abteilung zu verschwinden. Wie der Wind."


show mishashort hips_grin onlayer master at center
with charaenter

play music music_comedy fadein 0.5

mi "Hi, Hicchan~!"


show bg school_library onlayer master at bgleft
show mishashort hips_grin onlayer master at twoleft
with charamove

show yuuko neurotic_down onlayer master at tworight
with charaenter

"Misha begrüßt mich ausgelassen, während sie eine verlegene Yuuko hinter sich herzieht."


show mishashort sign_confused onlayer master
with charachange

mi "Hicchan~! Hast du mit dir selbst gesprochen?"


"Wenn ich jetzt ja sage, lässt mich das vielleicht ein wenig verrückt aussehen, aber wenn ich Kenji auffliegen lasse und er mit seinen Tiraden weitermacht, macht das auch keinen besseren Eindruck."


hi "Ja."


show mishashort cross_grin onlayer master
with charachange

mi "Ahaha~! Schon okay~! Das muss dir nicht peinlich sein, Hicchan; ich mache das auch das manchmal, wenn ich allein bin! La~ la~ la~."


show yuuko worried_up onlayer master
with charachange

yu "Ähm… nichts ist passiert, während ich weg war?"


hi "Absolut nichts."


show yuuko worried_down onlayer master
with charachange

yu "Es riecht nach… Trauben."


hi "Ich hab nach Trauben duftendes Rasierwasser benutzt."


"Ich lüge schamlos und offensichtlich. Wegen ihrer Reaktion vermute ich, dass sie entweder weiß, dass ich lüge oder sie denkt, ich hätte einen miserablen Geschmack für Rasierwasser."


"Da meine Traubensaftdose immer noch genau hier steht, ist es wohl eher das Erstere. Glücklicherweise stellt sie keine weiteren Fragen."


hi "Was habt ihr beide gemacht?"


show mishashort sign_smile onlayer master
with charachange

mi "Wir haben zusammen zu Mittag gegessen~! Streng geschäftlich, streng geschäftlich~!"


"Ich versuche, mir Misha in einem Anzug vorzustellen, wie sie mit jemandem zu Mittag isst. Irgendwie kriege ich einfach kein Bild zusammen."


hi "Was für Geschäfte denn?"


show yuuko panic_up onlayer master
with charachange

yu "Das weißt du nicht?"


show mishashort hips_grin onlayer master
with charachange

mi "Ahaha~! Nichts, nichts~. Es ist normal, dass ein Teil des Schülerrats nicht weiß, was der andere macht~."


hi "Hey, hör mir auf mit „nichts, nichts”. Das ist überhaupt nicht normal. Das ist sogar schlecht. Wir sind nur zu dritt."


show yuuko neurotic_up onlayer master
with charachange

"Yuuko lacht nervös. Sie muss entsetzt sein."


show yuuko worried_down onlayer master
with charachange

yu "Misha sagt, dass du Poster in der Bibliothek aufhängen willst… für die Wahlen. Ähm… auch wenn sie noch sehr weit weg sind, schätze ich, dass das in Ordnung ist. Ich weiß nicht, ob ich solche Dinge überhaupt entscheiden darf…"


show mishashort cross_laugh onlayer master
with charachange

mi "Darfst du~! Ist das nicht klasse~? Ahaha~! Freust du dich nicht? Yay~ yay~!"


show yuuko panic_up onlayer master
with vpunch

"Misha packt Yuukos Hand und zwingt sie, freudig für sich selbst zu klatschen. Yuuko ist anscheinend nicht sehr erfreut darüber zu erfahren, dass sie mehr Verantwortung und Befugnisse hat, als sie zuvor dachte."


show mishashort sign_smile onlayer master
with charachange

mi "Hicchan~! Da du schon mal hier bist, kannst du mir beim Aufhängen helfen."


"Sie holt einen Riesenstapel Poster auf ihrer Tasche, teilt ihn in zwei wie ein halbes Kartendeck und reicht mir die leicht zerquetschte Hälfte."


show mishashort hips_smile onlayer master
with charachange

mi "Shicchan hatte eine echt gute Idee~! Wir können ein auch ein paar Flyer in die Bücher legen~! Dann können sie uns nicht mal ignorieren, wenn sie es wollten! Wir könnten sie sogar mit einer Sprungfeder versehen!"


"Misha versucht ihr Bestes, das genauso herüberzubringen wie Shizune. Es gelingt ihr fast, aber es klingt auch etwas bedrohlich."


hi "Sie hat wahrscheinlich gescherzt."


show mishashort perky_confused onlayer master
with charachange

mi "Mir gefiel es~."


show yuuko cry_up onlayer master
with charachange

yu "N-Nein… warte… nicht das…"


show mishashort cross_smile onlayer master
with charachange

mi "Ein superultraaggresiver Markting-Überraschungsangriff~! Wir werden auch bald von Tür zu Tür gehen~!"


hi "Das ist eine schreckliche Idee."


show mishashort cross_frown onlayer master
with charachange

"Misha schmollt auf ihre beste Shizune-Art und tappt genervt schnell ihre Finger aneinander."


mi "Hicchan~! Du findest jede Idee schrecklich…"


hi "Ja, aber diese Idee ist zu schrecklich. Zu schrecklich, um sie zu ignorieren. Das kann ich nicht durchgehen lassen."


show mishashort hips_smile onlayer master
with charachange

mi "Wahaha~! Hicchan, das klingt wie eine Herausforderung. Meuterei~, Meuterei~!"


show yuuko cry_down onlayer master
with charachange

yu "M-Meuterei ist schlecht… Nicht streiten."


show mishashort hips_grin onlayer master
with charachange

mi "Wahaha~! Das war nur ein Spaß~!"


show yuuko worried_down onlayer master
with charachange

yu "Okay…"


show yuuko worried_up onlayer master
with charachange

yu "Nicht streiten."


show mishashort cross_laugh onlayer master
with charachange

mi "Aha~ ha~ ha~."


"Sie wie Yuuko sich anhört, während sie versucht, standhaft zu sein, erinnert sie mich an eine Kindergärtnerin. Ich vermute, dass macht sie auf ihre eigene Art überzeugend."


hide mishashort onlayer master
hide yuuko onlayer master
with charaexit

stop music fadeout 5.0

"Die Poster aufzuhängen stellt sich als überraschend schwierig heraus, einfach weil die Bibliothek bereits alle paar Meter mit Pinbrettern und Flyern zugekleistert ist. Manche an so merkwürdigen Stellen, dass ich sie bisher noch nie bemerkt habe."


play sound sfx_warningbell

"Zu entscheiden, welche wir für unsere eigenen Poster abnehmen, zieht diese sonst eigentlich leichte Aufgabe sehr in die Länge. Als die Glocke zum Ende der Mittagspause läutet, haben Misha und ich noch einen beträchtlichen Stapel übrig."


"Als wir gehen, beschließe ich, eins bei der rechten Tür aufzuhängen. Es muss von Mishas Postern sein; es hat eine kleine Zeichnung von Shizune am unteren Rand."


scene black onlayer master
with dissolve

label de_S28:

scene bg school_scienceroom onlayer master
with locationchange

"Ein paar Tage später. Shizune geht los, um allein Mittag zu essen und kommt nicht zurück. Sie muss wirklich in Schülerratsarbeit ertrinken, aber ich weiß, dass sie sich die meiste Arbeit davon selbst gemacht hat."


scene bg school_hallway3 onlayer master
with shorttimeskip

"Als ich beim Schülerratsraum ankomme, finde ich die Tür unverschlossen vor. Bevor ich sie öffne, halte ich für eine Sekunde inne, um eventuell Mishas Lachen durch sie zu hören. Nichts."


"Ich nehme das fast als Zeichen, dass niemand drinnen ist, aber in dem Fall würde Shizune die Tür niemals unverschlossen lassen."


play sound sfx_dooropen

scene bg school_council onlayer master
with locationchange

"Sie sitzt an ihrem Schreibtisch und schläft auf ihrem Stuhl, ihre Arme über der Brust verschränkt. Was für eine versteifte Haltung; wenn ihre Augen nicht geschlossen wären, würde man nicht erkennen können, dass sie schläft."
"Eigentlich kann ich mir nicht einmal sicher sein, dass sie gerade schläft."


"Normalerweise würde ich auf den Tisch klopfen, um jemanden zu wecken, aber bei ihr würde das nicht funktionieren."
"Ich fange sofort damit an, mir ein paar Streiche auszudenken, die ich ihr beim Schlafen spielen könnte. Es ist enttäuschend, dass mein Gedankengang in diese Richtung geht."


show shizu basic_normal onlayer master at center
with charaenter

ssh "Hallo. Guten Tag."



play music music_shizune fadein 3.0

"Sie gebärdet die Begrüßung mit jeder Hand einzeln. Wirklich verwirrend."


his "Hey, was hast du gemacht? Heimlich gefaulenzt?"


show shizu behind_smile onlayer master
with charachange

"Shizune lächelt, senkt aber ihren Kopf, um das zu verbergen und gibt sich Mühe, verärgert auszusehen."


show shizu adjust_frown onlayer master
with charachange

ssh "Steh da nicht so rum, es macht mich nervös, wenn ich sitze und du nicht."


"Ich setze mich auf den nächstgelegenen Stuhl, während Shizune kurz innehält, um ihre Brille zu richten."


show shizu adjust_angry onlayer master
with charachange

ssh "Warum bist du so weit weg?"


his "Macht dich das auch nervös?"


"Sie presst ihre Lippen zusammen und sieht von meiner Stichelei nicht sehr erfreut aus."


his "Ich hatte etwas Freizeit, darum dachte ich, ich schaue vorbei und sehe nach, ob du immer noch beschäftigt bist."


show shizu behind_blank onlayer master
with charachange

ssh "Willst du mir helfen?"


his "Jepp."


show shizu adjust_smug onlayer master
with charachange

ssh "Zu schade."


show shizu behind_smile onlayer master
with charachange

ssh "Ich bin dir dankbar, aber es ist nicht nötig. Ich bin gerade mit dem Letzten fertig geworden, und jetzt ist alles fertig, was fertig sein sollte."


his "So förmlich. Misha war gestern genauso sachlich. Macht ihr beide mit der offiziellen Schülerratsarbeit jetzt auf ernst?"


show shizu basic_normal2 onlayer master
with charachange

ssh "Ich bin immer ernst. So wie Schülerratskandidaten auch sein sollten."


"Das kam schnell. Von Null auf sofort die Leute kritisieren, die noch nicht einmal ihre Kollegen sind. Und das bevor ich eine Chance hatte, meine Beine auszustrecken."


show shizu behind_frown onlayer master
with charachange

ssh "Zumindest die Präsidenten. Sie brauchen Initiative, vielleicht können sie dann alle andere motivieren, oder sie zumindest unter Druck setzen. Aber obwohl es einen Haufen von ihnen gibt, sind sie alle so unentschlossen."


show shizu basic_angry onlayer master
with charachange

ssh "Es gibt niemanden, der als Vize-Präsident kandidiert. Alle wollen nur den großen Preis, aber keiner von ihnen hat den richtigen Tatendrang dazu."
ssh "Und noch dazu sind die Schatzmeister immer so unzuverlässig. Ich hab beschlossen, meinen Einfluss zu nutzen, um diese Position einfach aufzulösen."


his "Warte mal bitte kurz. Kannst du das überhaupt? Ich glaube nicht, dass das so funktioniert."


show shizu adjust_frown onlayer master
with charachange

ssh "So ist es nun mal."


"Daraufhin starrt Shizune grimmig in die Ferne und reibt den Rahmen ihrer Brille. Das beantwortet meine Frage nicht, zukünftige Diktatorin."


show shizu behind_frown onlayer master
with charachange

ssh "Ich bin enttäuscht. Sie sollten ein Interesse daran haben, mich hier schneller rauszukriegen, weil sie selbst den Job wollen. Oder zumindest sollten sie dagegen sein, dass ich diesen Job habe."
ssh "Wenn diese beiden Gründe nicht ausreichen, um einen Haufen Schülerrat-Möchtegerne zu mobilisieren, war all meine Arbeit umsonst."


show shizu adjust_angry onlayer master
with charachange

ssh "Wenn sie es so langsam angehen wollen, werde ich mein Amt einfach so lange wie möglich behalten!"


play sound sfx_snap

"Shizune unterstreicht ihren Satz mit einem Fingerschnipp so laut wie ein Pistolenschuss. Ich frage mich, ob sie überhaupt weiß, wie laut sie das eigentlich kann."


"Es erregt durchaus Aufmerksamkeit, darum kann ich gut verstehen, warum es für eine stumme Person von unschätzbarem Wert ist. Vielleicht hat sie es deswegen geübt."


his "„All deine Arbeit”, hm? Das ist zu streng."


show shizu behind_blank onlayer master
with charachange

ssh "Ich hab immer gedacht, dass das die Feuerprobe wäre. Einen bleibenden Eindruck zu hinterlassen ist wichtig. Darum baue ich keine Sandschlösser – sie zerfallen, wenn man geht."


his "Vielleicht, aber wenn ich ein besonders gutes sehe, finde ich es trotzdem beeindruckend. Und dann sage ich das auch."


his "Irgendwie bewundere ich dich. Darum war es für mich nicht umsonst."


show shizu adjust_happy onlayer master
with charachange

"Sie zupft an ihrer Brille, als ob sie sie abnehmen wollte, und lächelt dabei schief."


show shizu basic_normal onlayer master
with charachange

ssh "Entschuldige."


show shizu behind_blank onlayer master
with charachange

ssh "Ich war leichtsinnig. Mir ist etwas Egoistisches rausgerutscht."


show shizu basic_normal onlayer master
with charachange

ssh "Ich wollte schon immer an der Spitze stehen. Es war egal, was es war, solange ich die Beste darin war, es vollkommen verstanden und mir zu Eigen gemacht habe."


show shizu adjust_happy onlayer master
with charachange

ssh "Als ob man ein Lied hört und dann davon träumt, ein Musiker zu werden. Oder wenn man ein Flugzeug sieht und sich wünscht, Pilot zu werden. Hast du jemals so einen Traum gehabt?"


his "Ja."


"Das erste Mal, als ich Fußball spielte, fragte ich mich, ob ich je gut genug werden könnte, um Leute zu begeistern. Doch das war nur ein Hirngespinst."
"Sowie ich die Lücke zwischen mir und den Leuten mit echtem Talent erkannte, lies ich diese Träume hinter mir."


"Na ja, mit meinem Herz kann ich sowieso kein Fußball mehr spielen."


his "Hast du immer noch solche Träume?"


show shizu basic_normal2 onlayer master
with charachange

ssh "Nein, sie sind unrealistisch. Das hab ich sehr schnell begriffen. Es gibt immer jemand Besseren."


"Ein wehmütiger Ausdruck huscht über ihr Gesicht. Sie sieht gerade seltsam erwachsen aus, als ob die Tage des erbitterten Kämpfens um die Vorherrschaft weit hinter ihr lägen."


"Natürlich weiß ich, dass nichts der Wahrheit ferner liegen könnte. Erst letzte Woche wollte sie sehen, wer von uns die größte Kaugummiblase machen kann. Es könnte aber sein, dass sie als Kind viel schlimmer war. Ein furchterregender Gedanke."


show shizu behind_smile onlayer master
with charachange

ssh "Mir gefiel das. Dass es immer jemanden gab, der besser war. Wenn jemand Besseres als ich auftauchte, wurde ich immer so aufgeregt. Ich wollte sie herausfordern."


show shizu adjust_frown onlayer master
with charachange

ssh "Auch wenn sie sich am Ende für gewöhnlich als besser herausstellten und ich mit Ehrfurcht zurückgelassen wurde."
ssh "Es gibt ein paar Menschen, die auf einem vollkommen anderen Level sind. Nach einer Weile wurde ich eifersüchtig. Ich wollte selbst so etwas haben."


his "Ist es das, was der Schülerrat für dich ist? Dieses „so etwas”?"


show shizu basic_normal onlayer master
with charachange

ssh "Nein nein. Auch wenn es manchmal so rüberkommt. Deswegen hab ich mich nicht dazu entschlossen. Das ist eine ganz andere Geschichte."


show shizu adjust_happy onlayer master
with charachange

ssh "Aber… mir gefällt es, die Schülerratspräsidentin zu sein. Auch wenn es harte Arbeit ist und ich mir immer mehr aufhalse, als ich bewältigen kann, bleibt es genau deswegen so aufregend."
ssh "Die Leute, die an der Spitze stehen, sollten sich eh nicht die ganze Zeit wohlfühlen können."


his "Du klingst wie eine Bäuerin."


"Obwohl sie ihr nicht stehen würden, würde Shizune mit Latzhose und Strohhut süß aussehen."


his "Na, wenn das nicht der Grund war, warum hast du dich dann für den Job beworben?"


show shizu behind_frown onlayer master
with charachange

ssh "Hab ich nicht, aber im Nachhinein hab ich beschlossen, trotzdem dabei zu bleiben. Ich wollte die Schülerratspräsidentin werden, weil der alte Schülerrat dämlich war."


show shizu basic_normal onlayer master
with charachange

ssh "Und ich will Leute aufstacheln, damit sie sagen können: „Das war interessant. Heute war interessant.” Solche Sachen. Unvergessliche Erfahrungen."


show shizu behind_smile onlayer master
with charachange

ssh "Ich bin glücklich, weil ich finde, dass wir erfolgreich waren. Du, Misha und ich."


show shizu basic_normal2 onlayer master
with charachange

ssh "Es ist auch ein bisschen Egoismus dabei. Zuerst dachte ich, es wäre nur etwas wie ein netter Bonus, aber ich bin gierig geworden."


show shizu behind_blank onlayer master
with charachange

ssh "Darum würde es mich glücklich machen, wenn die Wahlen problemlos verlaufen. Es wäre in meinen Augen der einzige Weg, mit dem mein Wunsch erfüllt werden kann."


his "Welcher Wunsch denn?"


show shizu adjust_blush onlayer master
with charachange

ssh "Das ist ein Geheimnis."


"Da sie wohl spürt, dass ich vielleicht nicht gewillt bin, so einen schwachen Ausweichversuch durchgehen zu lassen, winkt sie im Voraus jede weitere Frage ab, während ihr Gesicht vor Verlegenheit rot wird."
"Sie will es nur für sich behalten, weil es ihr zu peinlich ist."


"Ich bekomme ein Hungergefühl und schaue auf meine Uhr. Es ist früher, als es aussieht. Zu früh fürs Abendessen."


his "Hast du irgendwas zu Essen in deinem Schreibtisch?"


show shizu cross_wut onlayer master
with charachange

"Für einen Augenblick sieht es aus, als würde sie diese Frage verwirren, aber sie fängt sich schnell."


show shizu behind_frustrated onlayer master
with charachange

ssh "Schreibtische sind für Vorräte."


his "Lebensmittel sind Vorräte."


show shizu basic_normal onlayer master
with charachange

ssh "Du hättest zu Mittag essen sollen."


his "Ich hatte nicht damit gerechnet, dass es ein Problem werden würde. Wenn ich arbeiten würde, hätte ich nicht daran denken müssen. Ich wäre zu beschäftigt, um hungrig zu sein."


show shizu adjust_happy onlayer master
with charachange

"In einem kläglichen Versuch, ein Lachen zu verbergen, hält sie sich die Hand vor ihren Mund und versucht, es noch zusätzlich zu verschleiern, indem sie so tut, als ob sie ihre Brille mit dieser Hand nach oben schieben wollte."


his "Du hast ja anscheinend schon gegessen."


"Ich deute auf den Verpackungsstapel von chinesischem Essen, der wackelig auf dem Mülleimer steht."


show shizu basic_normal onlayer master
with charachange

ssh "Die sind von gestern."


his "Dann haben wir beide Hunger. Lass uns etwas zu Essen besorgen."


his "Nicht aus der Cafeteria. Da gab es nichts Gutes zu Mittag, daher bezweifle ich ernsthaft, dass dort noch etwas Gutes übrig sein wird. Wollen wir etwas bestellen?"


show shizu behind_frown onlayer master
with charachange

ssh "Zwei Tage hintereinander etwas zu bestellen ist unnatürlich. Lieber nur im Notfall. Das ist mein persönlicher Grundsatz."


"Deswegen sollte sie mit dem Gedanken spielen, ihren Schreibtisch mit ein paar Snacks zu bevorraten. So könnte man besser auf solche „Notfälle” reagieren."
"Ich will ihr das sagen, aber fünfmal zu gebärden, wie hungrig ich bin, hat mich zu sehr entkräftet, um jetzt noch einen auf Besserwisser zu machen."


"Auch wenn die Verlockung wirklich groß ist."


mi "Halli Hallo~!"


"Mishas charakteristische auf-und-ab Stimme schallt gedämpft durch die Tür. Eine Sekunde später platzt sie herein."


show shizu behind_blank onlayer master at tworight
show bg school_council onlayer master at bgright
with dissolvecharamove

show mishashort perky_confused onlayer master at twoleft
with charaenter

mi "…"


show mishashort perky_smile onlayer master
with charachange

mi "Hicchan~! Du bist ja auch hier~!"


hi "„Auch”? Woher wusstest du, dass hier schon jemand drin ist?"


show mishashort sign_smile onlayer master
with charachange

mi "Wenn es offen ist, ist auch jemand drin~."


show mishashort cross_laugh onlayer master
with charachange

mi " Wahaha~!"


show mishashort hips_grin onlayer master
with charachange

mi "Störe ich~?"


show shizu basic_normal onlayer master
with charachange

"Shizune schüttelt ihren Kopf."


show mishashort hips_smile onlayer master
with charachange

mi "Super~! Das ist wirklich super~! Aber~! Ich war mir sicher, dass ich stören würde. Macht ihr eine Pause?"


hi "Das dachte ich auch erst, aber es scheint, als wäre die ganze Schülerratsarbeit fürs Erste fertig. Bist du hier, weil du helfen wolltest?"


show mishashort perky_smile onlayer master
with charachange

mi "Wahaha~! Jepp~! So ist es, Hicchan!"


ssh "Sorry, dass ich dich enttäuschen muss. Wir haben gerade darüber diskutiert, ob wir uns zum Abendessen etwas bestellen sollen oder nicht."


show mishashort hips_grin onlayer master
with charachange

mi "Klingt nach Spaß~."


hi "Shizune sieht das allerdings nicht so spaßig. Sie sagt, dass sie nicht zwei Tage hintereinander Essen bestellen kann. Bist du auch hungrig? Weil wenn ja, könnten wir sie überstimmen."


show mishashort hips_smile onlayer master
with charachange

mi "Hm~ hm~, das klingt nach Spaß, Hicchan! Und ja, ich bin etwas hungrig…"


hi "Ich dachte, du würdest sagen, dass es sich nach Meuterei anhört."


show shizu adjust_frown onlayer master
with charachange

"Shizune greift an ihren Brillenrahmen, offenbar überzeugt davon, dass doch Meuterei in der Luft liegt. Aber da sie fair 2 zu 1 überstimmt würde, kann sie nichts dagegen tun. Misha hat bereits ihr furchtbar geschmackloses Handy gezückt."


show mishashort sign_smile onlayer master
with charachange

mi "Shicchan, du hast versprochen, dass wir nur mit dem Schülerrat was unternehmen würden, stimmt's~? Stimmt, stimmt~! Warum nicht das?"


show shizu behind_frown onlayer master
with charachange

"Shizune schüttelt lediglich ihren Kopf. Die letzte Party, bei der sie als Yamakus Schülerratspräsidentin teilnehmen kann, ist zu besonders für sie, als dass man dieses spontane und vorzeitige Abendessen dazu erklären könnte."


stop music fadeout 3.0

"Auch wenn ich mir sicher bin, dass die Richtige dann genauso sein wird: Eine Mahlzeit wie jede andere mit uns dreien."


scene bg school_dormext_full_ss onlayer master
with shorttimeskip

"Nachdem wir gegessen und aufgeräumt haben, verabschiede ich mich von ihnen und gehe zurück in mein Wohnheim. Obwohl ich nicht besonders müde bin, denke ich, dass ich heute Abend einfach direkt schlafen gehen werde."


"Wenn ich zu Hause wäre, würde meine Mama nörgeln, dass ich nach dem Essen nicht sofort schlafen gehen soll, aber was sie nicht weiß, macht sie nicht heiß."


scene bg school_dormhisao_ss onlayer master
with locationskip

"Sobald ich hereinkomme, wandert mein Blick zur Uhr, und ich stelle fest, dass es viel später ist als ich dachte."


"Es kommt mir auch ein bisschen lächerlich vor, dass ich auf die Uhr gucke, obwohl ich ein Handy und eine Armbanduhr habe. Ich nehme meine Uhr ab und halte sie in einer Hand, während mein Handy in der anderen liegt. Ich fühle mich mächtig – und dumm."


play sound sfx_doorknock

"Ich versuche erfolglos einzuschlafen, und bin froh, als mich jemand nach nur wenigen Minuten mit einem Klopfen an der Tür unterbricht. Ich nehme an, dass es niemand außer Kenji sein kann, deshalb bin ich verwundert, als es letztendlich Misha ist."


play sound sfx_dooropen

scene bg school_dormhallway onlayer master
show mishashort hips_smile onlayer master at center
with locationchange

mi "Hi, Hicchan~!"


show mishashort perky_sad onlayer master
with charachange

mi "Du scheinst dich nicht über meinen Besuch zu freuen~…"


hi "Doch, ich bin nur irgendwie überrascht. Ist Shizune doch noch etwas eingefallen, was ich erledigen soll?"


hi "Es ist spät, aber… egal. Es ist wohl gut, dass ich mich noch nicht umgezogen hab."


show mishashort sign_smile onlayer master
with charachange

mi "Nope~. Ich dachte einfach, dass ich mal vorbeikomme, Hicchan~!"


hi "Zum Spaß?"


"Nein, natürlich nicht. Sie will über etwas reden. Es muss etwas Wichtiges sein, wenn sie nicht will, dass Shizune davon erfährt."


hi "Willst du reinkommen?"


show mishashort hips_grin onlayer master
with charachange

mi "Ja~, danke, Hicchan!"


scene bg school_dormhisao_ss onlayer master
show mishashort invis onlayer master at center
with locationchange

show mishashort perky_smile_ss onlayer master at Position(ypos=1.13)
with dissolvecharamove

play sound sfx_doorclose

"Sie kommt herein und setzt sich sofort auf den Stuhl. Eine ganz normale Sache, aber ich hätte erwartet, dass sie sich aufs Bett setzt."


show mishashort cross_frown_ss onlayer master
with charachange

mi "Hicchan…"


"Misha runzelt streng die Stirn, die Arme über ihrer Brust verschränkt. Es ist, als wollte sie mich ins Verhör nehmen. Alles, was noch fehlt, ist der Schnurrbart und die baumelnde, flackernde Glühbirne an einem Faden."


mi "Hast du Shicchan traurig gemacht?"


play music music_drama fadein 6.0

hi "Wie meinst du das?"


show mishashort hips_frown_ss onlayer master
with charachange

mi "Als ich heute zum Büro ging, konnte Shicchan mich nicht kommen hören. Darum~ hab ich sie mit einem wirklich verwirrenden Gesichtsausdruck gesehen, als ich die Tür aufgemacht hab."
mi "Shicchan sah glücklich und traurig zugleich aus, und~ ich wollte wissen warum."


hi "Na ja, meinetwegen war es nicht. Ich hab ihn nicht einmal zu Gesicht bekommen."


hi "Ich denke, sie ist deprimiert darüber, dass sie in ein paar Monaten nicht mehr Schülerratspräsidentin sein wird."


show mishashort perky_confused_ss onlayer master
with charachange

mi "Hm~… Als ich Shicchan deswegen gefragt hab, hat sie gesagt, dass es okay wäre~!"


hi "Das hat nichts zu bedeuten. Shizune würde das zwar sagen, aber es ist lächerlich anzunehmen, dass sie so einfach loslassen kann."


hi "Ich meine, es gibt Momente, in denen sie mit mir um den letzten Apfel kämpft, oder die letzte Schokoladenmilch, oder sonst was. Und solches Zeug ist nicht mal wichtig."


show mishashort hips_frown_ss onlayer master
with charachange

mi "Schokoladenmilch ist wichtig."


hi "Okay, ist sie. Reg dich nicht auf. Aber nicht so sehr wie der Schülerrat für sie. Sie würde das nicht so locker nehmen."


show mishashort hips_grin_ss onlayer master
with charachange

mi "Wahaha~. Da hast du Recht~."


"Ich dachte, dass das ein Verhör werden soll, aber es hat den Anschein, als hätte Misha das schon vergessen."


show mishashort sign_smile_ss onlayer master
with charachange

mi "Aber~! Ich will nicht, dass Shicchan mich anlügt, damit ich mich besser fühle."


show mishashort hips_grin_ss onlayer master
with charachange

mi "Hahaha~! Die meisten Leute wissen nicht, wie ernst Shicchan ist und denken, dass sie nur eine Show abzieht. Ich bin froh, dass du sie verstehst, Hicchan."


hi "Es ist offensichtlich. Besonders so wie sie heute darüber gesprochen hat."


"Misha lehnt sich interessiert nach vorne, ihren Kopf dabei auf ihre Hände gestützt."


show mishashort cross_smile_ss onlayer master
with charachange

mi "Wirklich~? Was hat sie gesagt?"


"Sie stehen sich nah genug, dass ich mir nicht viel dabei denke, dass sie so neugierig ist."


hi "Warum sie dem Schülerrat beigetreten ist. Mehr oder weniger. Sie hat angefangen, aber dann entschieden, dass manche Dinge einfach geheim bleiben sollen."
hi "Und sie hat „Das ist ein Geheimnis” gebärdet. Darum glaube ich, dass es das ist, was sie mir gesagt hat: Es ist ein Geheimnis."


show mishashort sign_smile_ss onlayer master
with charachange

mi "Na ja~, wenn dir jemand sagt, dass er ein Geheimnis hat, ist das doch irgendwie in sich schon ein Geheimnis, Hicchan~!"


hi "So wie du meintest, dass Glück eine Fertigkeit ist?"


show mishashort hips_grin_ss onlayer master
with charachange

mi "Es ist möglich!"


show mishashort cross_laugh_ss onlayer master
with charachange

mi "Wahaha~!"


hi "Sei vorsichtig, nicht so laut."


show mishashort perky_confused_ss onlayer master
with charachange

mi "Wieso, Hicchan?"


hi "Du weckst noch die Hälfte der Leute in diesem Gebäude auf, und darüber hinaus sind Wohnheime nicht gemischt."


show mishashort hips_frown_ss onlayer master
with charachange

mi "Hicchan, denkst du an etwas Unanständiges?"


hi "Lass den Quatsch."


show mishashort hips_grin_ss onlayer master
with charachange

mi "Ahahaha~."


show mishashort hips_smile_ss onlayer master
with charachange

mi "Wenn du es bist, ist es okay, glaub ich."


"Das zu hören lässt mich begreifen, wie einfach es für mich die ganze Zeit gewesen ist, mit Misha zu reden – dass es nie nötig war, auf meine Gedanken aufzupassen… bis heute."


show mishashort perky_sad_ss onlayer master
with charachange

mi "Ich bin traurig, Hicchan."


mi "Es ist komisch… Je glücklicher Shicchan wird, desto deprimierter werde ich. Obwohl ich mich für Shicchan freuen sollte. Das tue ich auch… aber~ ich kann mit ihr nicht über meine Probleme reden."


hi "Warum nicht?"


show mishashort sign_sad_ss onlayer master
with charachange

mi "Genau wie Shicchan nicht mit mir über ihre Probleme reden kann. Es ist das Gleiche, Hicchan. Wenn wir diese Art von Problem haben, dann bin ich mir nicht mehr sicher, was ich tun soll. Ich frage mich… ob ich eine schlechte Freundin bin."






show mishashort perky_sad_close_ss onlayer master at center
with characlose

stop music fadeout 2.0

"Misha steht auf und lässt sich rasch auf das Bett fallen, sodass wir nur noch wenige Zentimeter voneinander entfernt sitzen. Nur ein paar Sekunden später schiebt sie ihren Kopf nach vorne, und gibt mir einen leichten Kuss."
"Er verfehlt meine Lippen – mehr weil sie schlecht gezielt hat als weil ich ausgewichen wäre."


hi "Was tust du?"


"Obwohl die Frage nur eine Formalität ist… Ich wäre bescheuert, wenn ich nicht wüsste, worauf sie hinauswill. Es ist nur, dass es so unwahrscheinlich scheint, dass ich immer noch die Hoffnung habe, nichts damit zu tun haben zu müssen."



show mishashort hips_grin_close_ss onlayer master
with charachange

"Jetzt beschließt sie, auf schüchtern zu machen und kichert sichtlich verlegen."


mi "…"


show mishashort perky_smile_close_ss onlayer master
with charachange

mi "Magst du mich, Hicchan?"


hi "Ja."


"Ihr Kopf ist in meiner Brust vergraben. Es fühlt sich an, als würde sie in meine Narbe sprechen. Vielleicht spürt sie sie an ihrer Wange."


"Ich hatte bisher so sehr versucht, sie vor beiden geheimzuhalten. Im Nachhinein kommt es mir idiotisch vor, dass ich mir darüber solche Sorgen gemacht habe."


show mishashort perky_sad_close_ss onlayer master
with charachange



label de_choiceS28:
menu:
    with menueffect
    mi "Bitte tröste mich, Hicchan. Nur für heute."
    "Misha trösten.":






        return m1
    "Ablehnen.":


        return m2


label de_S28a:

play music music_moonlight fadein 4.0

"Auch wenn ich so getan habe, als würde ich mich dagegen wehren, habe ich es doch so weit kommen lassen. Obwohl ich schon wusste, was sie vorhatte, lange bevor sie es angesprochen hat."


"Zumindest hatte ich nichts gegen dieses Resultat. Wenn ich noch einen weiteren Beweis dafür bräuchte: Ich habe sie immer noch nicht abgewiesen."


"Ich hätte es jederzeit tun können, und es war falsch von mir, es nicht früher getan zu haben. Aber es jetzt nicht zu tun, geht über simple Fahrlässigkeit hinaus."


show mishashort perky_sad_close_ss onlayer master:
    linear 0.2 alpha 0 ypos 1.1
with vpunch

hide mishashort onlayer master
with None

"Misha interpretiert mein Schweigen als Zustimmung und presst sich fest gegen mich, als würde sie versuchen, in meine Kleidung zu gelangen."
"Mein Arme sind umhüllt von der Zartheit ihrer Haut und der Wärme ihres Körpers. Aus Reflex drehe ich mich um und ende schließlich auf ihr."


"Sie sieht mich an, als würde sie erwarten, dass ich die Führung übernehme. Als ich ihren Blick erwidere, schließt sie nervös ihre Augen."
"Ich schätze, ich habe keine Wahl, und beginne sie ungeschickt auszuziehen – etwas, das ich noch nie zuvor getan habe."


label de_S28h:

scene evh misha_naked onlayer master:
    xalign 1.0 ypos 0.0 subpixel True
    easein 12.0 xalign 0.0
with whiteout

"Immerhin hatte ich bisher nur einmal Sex, und dabei war ich an einen Stuhl gefesselt."
"Dieses Mal habe ich die Kontrolle – so wie ich es mir damals gewünscht hätte. Aber so ist es auch ziemlich beängstigend. Ich beginne, indem ich ihre Bluse aufknöpfe und sie von ihren Schultern rutschen lasse."


"Ihre Figur ist kurviger als ich erwartet habe und passt gut zu ihrem süßen Gesicht."


"Ihr BH öffnet sich hinter ihrem Rücken, und ich habe Schwierigkeiten, ihn auszuziehen – teilweise weil Misha sich anscheinend wegen ihrer Brüsten schämt und versucht, sie halbherzig zu verstecken, bevor ich ihn überhaupt ausgezogen habe."


"Als ich ihren Rock öffne und anfange, ihr Höschen auszuziehen, leistet sie weitere Male schwachen, gespielten Widerstand. Es ist nur eine Formalität."


"Ich begreife nun, dass Formalitäten sehr wichtig für Misha sind. Darum begrüßt sie alle immer so fröhlich, sogar wenn sie sich wahrscheinlich nicht über die Begegnung freut."


"Jetzt sind ihre Augen geöffnet. Ich fahre mit meiner Hand hinauf zur Innenseite ihrer Hüfte, und fast lache ich, als sie schaudert und meine Hand beinahe zerquetscht, als sie ihre Beine zusammenpresst. Eine aufrichtige Reaktion. Und eine süße dazu. "


"Shizune war besser darin, ihre Unerfahrenheit zu verbergen, auch wenn sie genauso verlegen war."


hi "Bist du bereit?"


"Sie nickt, ohne mich anzusehen."


scene evh misha_sex_aside onlayer master:
    truecenter
    subpixel True zoom 1.05
    easein 6.0 zoom 1.0
with locationchange

"Als ich in sie eindringe, kann ich spüren, wie sie nervös verkrampft. Mir geht es genauso, als ich in ihrem Inneren einen Widerstand spüre. Ich bin so angespannt, dass es sich bei jeder Bewegung schmerzhaft mechanisch anfühlt."


"Ich frage mich, ob ich schneller werden sollte, so wie Shizune es getan hat."
"Aber Shizune ist ziemlich geradeheraus. Jetzt ist es einen andere Situation. Eine, die ich bereue. Ich fange an, tiefer in sie einzudringen, und Misha zuckt vor Schmerz zusammen."


mi "Bitte tu es schnell…"


scene evh misha_sex_closed onlayer master:
    zoom 1.0
with locationchange

mi "Au…"


"Ich stoppe."


scene evh misha_sex_aside onlayer master
with locationchange

mi "Nein, es ist okay."


"Und dann dringe ich noch tiefer in sie ein – bis zum Schaft. Ich spüre, wie Mishas Hände meine Arme umklammern und dann nach oben wandern, als ob sie versuchen würde, sie zu erklimmen."


"Sie packt mich an den Schultern und zieht sich an mich, wodurch wir noch enger verbunden werden. Ich kann nichts anderes tun, als es ihr gleichzutun."


scene evh misha_sex_closed onlayer master
with locationchange

mi "Ah~… aaah…"


"Als ich sie stöhnen höre, werde ich schneller und finde einen Rhythmus. Ihr Hände schließen sich hinter meinem Rücken, und ich spüre, wie sich ihre Ellenbogen in den Bereich unter meinen Rippen bohren, während ich weiter in sie stoße."


"Das Blut pocht in meinen Ohren wie ein Trommelschlag, bis ich sie kaum noch hören kann."


mi "Hnn~…"


scene evh misha_sex_aside onlayer master
with locationchange

mi "Das ist mein erstes Mal mit einen Mann. Es ist seltsam."


"Ich wünschte, sie würde aufhören zu reden. Ihre Stimme ist so leise und hauchend, dass ich Probleme habe, sie zu verstehen. Doch der traurige Unterton ist unverkennbar und verstärkt meine Schuldgefühle nur noch."


"Ich sollte sie trösten, aber das hier ist völlig körperlich, und wenn Misha dadurch irgendwie beruhigt ist, zeigt sie es nicht. Das wirft bei mir die Frage auf, ob meine Entscheidung richtig oder falsch war. Ich fange wirklich an, daran zu zweifeln."


scene evh misha_sex_closed onlayer master
with locationchange

"Trotzdem lässt mich ihr sanftes Gurren in mein Ohr weitermachen, genauso wie die glatte Enge um mein Glied. Schließlich verspannt sich ihr Körper und sie kommt zum Orgasmus. Ihr geschmeidiger Hals reibt sich an meinen Wangen."


scene evh misha_naked onlayer master
with whiteout

stop music fadeout 6.0

"Es dauert eine Minute, bis sie sich von mir löst. Das gibt mir die Gelegenheit, ihren Körper in vollem Umfang zu betrachten. Ihre pinke Haut ist gerötet und von Schweiß benetzt. Mir ist kalt."


mi "… Hicchan?"


"Ich kann nichts hören, außer dem Ticken der Uhr und meiner eigenen Atmung."


mi "… Schon okay, Hicchan."


"Ich suche mit meiner Hand nach Mishas und liebkose sie. Sie scheint so leicht und zart, sogar als sie so fest mein Handgelenk umschließt. Diese Gefühl ist mir vertraut."


scene black onlayer master
with dissolve




label de_S28b:

show mishashort perky_sad_close_ss onlayer master:
    linear 0.2 alpha 0 ypos 1.1
with vpunch

hide mishashort onlayer master
with None

play sound sfx_pillow

"Bevor ich antworten kann, drückt sie sich mit ihrem ganzen Körpergewicht an mich, und bringt mich so sehr aus dem Gleichgewicht, dass wir beide aufs Bett fallen. Wenn ich nicht schnell antworte, wird die Situation nur noch heikler."


"Ich weiß, dass ich es auch so schon viel zu weit habe gehen lassen."


"Also schubse ich sie von mir, auch wenn das nicht der taktvollste Weg ist, sie zurückzuweisen."
"Misha fällt rückwärts auf das Bettlaken – so sanft, als ob sie überhaupt nicht gefallen wäre. Mit geschlossenen Augen bleibt sie so eine Weile liegen, bevor sie mit einem hohlen Lachen aufsteht."


show mishashort invis onlayer master:
    center
    ypos 1.2
with None

show mishashort perky_sad_ss onlayer master at center
with dissolvecharamove

play music music_moonlight fadein 6.0

mi "Du hast Recht, Hicchan. Es tut mir leid."


scene black onlayer master
with shuteye

"Ich weiß nicht, wie ich mich fühle. Ein wenig bedauernd, auch wenn Bedauern eigentlich hasse. Traurig, aus vielerlei Gründen. Und auch ein bisschen wütend – auf sie und auf mich. Irgendwie scheint es sogar, als ob ich überhaupt nichts fühle."


hi "Das muss es nicht."


mi "Nein, Hicchan. Ist okay~. Es tut mir wirklich, wirklich~ leid."


mi "Aber… nur danach zu fragen, hat mir gereicht, glaube ich."


mi "Ich bin glücklicher, dass du nein gesagt hast."


hi "Stimmt das? Na ja, das ist gut."


mi "Jepp~, tut es. Danke, Hicchan."


"Sie setzt sich auf und lehnt sich gegen die Wand. Zumindest vermute ich das. Mein Kopf schmerzt so sehr, dass ich meine Augen lieber geschlossen halte."
"Ich liege auf meinem Bett und lausche dem Rascheln meiner Haare auf dem Bettlaken und dem draußen im Wind wiegendem Gras."


"Ich sollte wohl mehr sagen, um sie zu beruhigen, aber ich frage mich, ob das wirklich helfen würde. Vielleicht wäre es besser, nichts zu sagen. Ich weiß es einfach nicht, allerdings glaube ich, dass es für diese Situation keine richtige Lösung gibt."


mi "Gute Nacht, Hicchan."


play sound sfx_doorclose

stop music fadeout 4.0

"Daraufhin geht sie und lässt die Tür hinter sich wie ein schuldiges Flüstern zuschnappen."


"Vielleicht liegt es daran, dass ich den Tag schnell hinter mich bringen will, aber nachdem Misha weg ist, fällt mir das Einschlafen viel leichter. Es gelingt mir fast augenblicklich."


scene black onlayer master
with dissolve




label de_S29:

scene bg school_dormhisao onlayer master
with locationchange

play music music_night fadein 4.0

"Am Morgen darauf wache ich mit dem Gedanken auf, dass ich die meiste Zeit damit verbringen werde, Shizune und Misha aus dem Weg gehen."


"Was gestern Abend passiert ist, macht mich immer noch unbehaglich. Ich dachte, eine Nacht darüber zu schlafen, würde dieses Gefühl lindern. Ich komme mir wie ein Idiot vor, weil ich dachte, es wäre so einfach."


"Ich frage mich, ob Misha sich genauso fühlt. Falls ja, wird sie heute wahrscheinlich nicht zu Schule kommen."
"Ich habe dasselbe in Betracht gezogen, aber es wäre ziemlich verdächtig, und mich den ganzen Tag vor Angst drinnen zu verkriechen, begeistert mich nicht. Hat es nie wirklich."


scene bg school_scienceroom onlayer master
with locationskip

"Wie ich dachte, ist Misha heute morgen nicht im Unterricht."
"Shizune schon, aber heute ist mehr zu tun als sonst, daher schenkt sie der Mitarbeit ihre volle Aufmerksamkeit, und das heißt, es gibt für sie wenig Leerlauf, um eine Unterhaltung mit mir anzufangen."



label de_S29a:

"Es ist seltsam, dass ich vor dem Gedanken davonlaufe, dass ich mit Shizune reden muss, nachdem ich so viel Zeit mit dem Versuch verbracht habe, genau das zu tun, aber ich weiß nicht, wie ich mich sonst fühlen soll."
"Ich hatte Sex mit ihrer besten Freundin."


"Wenn ich so empfinde, frage ich mich, wie Misha sich fühlen muss. Genauso reuevoll? Als sie zu mir kam, war sie vor allem mehr deprimiert als sexy. Ich kann mir nur vorstellen, wie viel schlimmer es jetzt sein muss."


"Wenn ich so darüber nachdenke, will ich sie wiedersehen – wenn auch nur halbherzig. Die andere Hälfte von mir ist immer noch entsetzt, obwohl ich es hasse, dieses Wort zu benutzen."


"Ich schäme mich dafür, aber ich bin mir sicher, dass es gerade die einzige passende Beschreibung für mich ist. Es ist kein schönes Gefühl."



label de_S29b:

"Ich habe mich so sehr daran gewöhnt, Shizune und Misha zusammen zu sehen, dass ich bis gestern nicht begriffen hatte, wie selten das in letzter Zeit der Fall war."


"Es ist schade, denn der leere Platz neben ihr erinnert mich daran, dass sie ein Paar sind. Darum ist Gestern etwas, das ich mit mir ins Grab nehmen werde."


"Wenn ich so empfinde, frage ich mich, wie Misha sich fühlen muss. Genauso reuevoll? Als sie zu mir kam, war sie vor allem mehr deprimiert als sexy. Ich kann mir nur vorstellen, wie viel schlimmer es jetzt sein muss."


"Wenn ich so darüber nachdenke, will ich sie wiedersehen – wenn auch nur halbherzig. Die andere Hälfte von mir ist immer noch entsetzt, obwohl ich es hasse, dieses Wort zu benutzen."


"Ich schäme mich mich dafür, aber ich bin mir sicher, dass es gerade die einzige passende Beschreibung für mich ist. "



label de_S29x:

scene bg school_library onlayer master
with shorttimeskip

"Nicht in der Stimmung, den Rest des Tages im Unterricht zu verbringen, aber nicht gewillt, zurück zum Wohnheim zu gehen, verbringe ich die nächsten paar Stunden in der Bibliothek."


show shizu invis onlayer master at center
with None

show shizu behind_frown onlayer master at Position(ypos=1.14)
with dissolvecharamove

"Während ich träge durch die Seiten eines uninteressanten Geschichtsromans blättere, lässt sich Shizune schmollend auf den Stuhl mir gegenüber fallen."


show shizu adjust_frown onlayer master
with charachange

ssh "Ich glaube, es ist irgendwie sinnlos, zur Schule zu kommen und dann jeden Unterricht zu schwänzen."


his "Sorry."


show shizu behind_frustrated onlayer master
with charachange

ssh "Erzähl wenigstens allen, dass du krank bist."


his "Mir ist heute einfach nicht danach. Gestern ging es aber, und morgen wird es mir wahrscheinlich auch wieder besser gehen."
his "Ein Krankheitstag mitten in der Woche ist einfach zu verdächtig. Diese 24-Stunde-Grippe oder was auch immer wird nicht durchgehen."


show shizu adjust_frown onlayer master
with charachange

ssh "Es ist nicht verdächtig."


his "Doch, ist es."


show shizu basic_angry onlayer master
with charachange

"Ich wende mich wieder meinem Buch zu, und Shizune drückt es sanft nach unten. Im Gegensatz dazu schwankt ihr Gesichtsausdruck zwischen Wut und Sorge."


show shizu behind_blank onlayer master
with charachange

ssh "Stimmt etwas nicht?"


his "Wie bitte?"


show shizu basic_normal2 onlayer master
with charachange

ssh "Beschäftigt dich etwas? Weil du dich heute etwas verdächtig verhältst. Auf eine andere Art."


show shizu behind_blank onlayer master
with charachange

ssh "Wenn etwas ist, sag es mir einfach, oder ich werde sauer. Ich bin nicht gut darin, Menschen zu lesen."


"Wie lächerlich, das zu sagen, nachdem sie meine Stimmung so einfach erfasst hat."


"Sie scherzt lediglich zur Hälfte, aber da ist etwas Wahres dran. Schließlich kann sie nichts hören und muss sich auf das Lesen verlassen, um mit anderen zu kommunizieren."


"Es ist, als könnte man sich ausschließlich über Textnachrichten mit jemandem unterhalten. Irgendwie muss einen das fertigmachen."


"Wahrscheinlich starrt sie deswegen die Leute so aufmerksam an – um ihre Reaktion abzuwägen. Oder vielleicht bedrängt sie darum die Leute so stark, damit sie zu einer Reaktion gebracht werden."


"Ich hatte schon zuvor daran gedacht, aber es ist zu schwierig zu sagen, was Shizunes genaue Beweggründe für irgendetwas sind."


"Daher frage ich mich, wie viel davon als Witz gemeint war. Manchmal erkennt man es sofort. Diesmal jedoch nicht."
"Angenommen es war kein Witz, kann ich es ihr trotzdem nicht sagen. Aber weil es Zeichensprache ist, habe ich genug Zeit, mich zu sortieren und mir eine glaubhafte Lüge auszudenken."


his "Es ist nichts."


show shizu cross_wut onlayer master
with charachange

shi "…"


his "Ich hab nur in letzter Zeit viel über die Zukunft des Schülerrats nachgedacht. Ich vermute, dass Misha das gleiche tut… Na ja, auf ihre eigene Art."


show shizu behind_frustrated onlayer master
with charachange

ssh "Das tue ich auch, aber sie ist heute nicht hier. Ich wünschte, sie hätte mir Bescheid gesagt, denn ich könnte nachher ihre Hilfe gebrauchen. Deine auch, wenn du nicht zu beschäftigt bist."


his "Bin ich nicht…"


show shizu basic_normal onlayer master
with charachange

ssh "Danke."


show shizu behind_sad onlayer master
with charachange

ssh "Es kommt mir vor, als würde ich in letzter Zeit viele mir nahestehende Menschen verlieren."


"Mir fällt keine gute Antwort darauf ein. Etwas Beruhigendes und Selbstsicheres, dass sie sich keine Sorgen machen muss. „Ich bin für dich da. Ich bin keiner von diesen Leuten.”"


"Aber von wem redet sie dann? Und es wirkt so gekünstelt. Ich winke ab, aber kaum habe ich die Geste beendet, kommt sie mir extrem herzlos vor."


his "So solltest du nicht denken."


show shizu basic_normal2 onlayer master
with charachange

shi "…"


his "Ich bin vielleicht nur ein bisschen krank – nicht genug, um mir den Ärger mit der Krankmeldung zu machen. So ist es einfach leichter für mich."


show shizu behind_frown onlayer master
with charachange

ssh "So sollte man es nicht machen."


"Ich habe gehört, dass der harte und der richtige Weg oft derselbe sind. Also ist es wohl auch gut möglich, dass der einfache Weg der falsche ist."


show shizu basic_normal onlayer master
with charachange

ssh "Na schön. Wenn du sagst, dass es dir gut geht, dann reicht mir das."


his "Warte."


show shizu behind_blank onlayer master
with charachange

shi "…?"


his "Du hast mich gefragt, also tue ich dasselbe. Ist mit dir alles okay?"


show shizu basic_normal2 onlayer master
with charachange

ssh "Ja."


stop music fadeout 3.0

"Sie gebärdet es, ohne zu zögern. Danach wartet sie ab, ob ich weiter nachhake."


show shizu invis onlayer master at center
with dissolvecharamove

hide shizu onlayer master
with None

"Ich tue es nicht, und sie geht. Ich komme mir deswegen wie ein Idiot vor, auch wenn ich glaube, dass es so besser war."


"Ich bin eine ganze Weile in der Bibliothek gewesen und beschließe, zur Abwechslung rauf aufs Dach zu gehen."


play sound sfx_door_creak
play ambient sfx_rooftop fadein 1.0

scene bg school_roof_ss onlayer master
with locationskip

"Eine frische Brise trifft mich, sobald ich die Tür öffne. Ich glaube, das ist wirklich mein Lieblingsplatz in der Schule. Dann erkenne ich, dass ich nicht als Einziger hier oben bin. Ein Mädchen mit kaugummipinken Haaren steht vor mir."


"Ihr Rücken ist zu mir gewendet, aber ich muss ihr Gesicht nicht sehen, um zu wissen, wer es ist. Ich bin mir sicher, dass Misha der einzige Mensch auf der Welt mit solchen Haaren ist."


"Ich bekomme das Gefühl, dass ich zu einem schlechten Zeitpunkt auf sie gestoßen bin. Sie will offenbar allein sein, und ich frage mich, ob sie meine Anwesenheit schon bemerkt hat."
"Wenn nicht, werde ich sofort gehen. Aber das hat sie, und sie wendet sich mir zu."


$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

scene ev misha_roof_normal onlayer master:
    yalign 1.0 xalign 0.5 subpixel True
    easein 12.0 yalign 0.0
with whiteout

play music music_sadness fadein 8.0

mi "Oh, Hicchan. Ich habe jemanden hinter mir gehört, aber ich dachte nicht, dass du es bist. Diesmal hast du mich überrascht."


"Falls sie damit ihre Angewohnheit meint, mir von hinten aufzulauern und mich zu fragen, wer sie sei… Davon bin ich noch nie überrascht gewesen."


hi "Ich bin auch überrascht. Aber das trifft sich gut. Es gibt sowieso etwas, worüber ich mit dir reden wollte."


mi "…"


hi "Nicht das…"


hi "Was ist los mit dir und Shizune? Sie will es mir nicht verraten, daher frage ich dich."


"„Weil man von dir einfacher eine Antwort bekommt. Die gleiche Zeichensprache, die mir einen Spielraum gibt, sie anzulügen, ist für sie ein Puffer gegen meine Fragen, sodass sie ihnen leichter ausweichen kann.”"
"Als Misha zögert, dränge ich weiter."


hi "Gib mir eine ehrliche Antwort. Bitte."


mi "Es ist kompliziert, Hicchan… Es ist wegen etwas, das vor langer Zeit passiert ist. Ich dachte, ich könnte es einfach vergessen, aber~… es ist echt schwierig."
mi "Also~ deswegen und wegen des anstehenden Schulabschlusses, wollte ich mehr Zeit mit Shicchan verbringen~!"


scene ev misha_roof_sad onlayer master
with charachange

mi "Aber nun ist Shicchan immer beschäftigt. Darum~! haben wir uns gestritten. Aber ich hab mittlerweile genug davon."


mi "Weil~… Ich mag Shicchan."


hi "Das tue ich auch."


scene ev misha_roof_normal onlayer master
with charachange

mi "Wahaha~ Nein, nein~. Ich weiß, dass du sie magst, Hicchan. Ich meine, ich mag Shicchan auf die gleiche Art."


scene ev misha_roof_closed onlayer master
with charachange

mi "Ich will mit ihr zusammen sein."


"Misha schließt ihre Augen wie ein verurteilter Krimineller, der dem Henker seine letzte Sünde beichtet. Dadurch fällt es mir nur noch schwerer, eine Antwort zu finden, und ich weiß, dass ich ihr eine geben muss."


hi "Ach so. Das wusste ich nie."


scene ev misha_roof_normal onlayer master
with charachange

mi "Ich wollte nicht wirklich auf diese Schule gehen, Hicchan~. Aber es klang interessant, und selbst wenn mich alle hassen würden, dachte ich, sie würden mich wenigstens in Ruhe lasen."
mi "Ich nahm Kurse in Zeichensprache, aber ich war damals noch nicht sehr gut~."


mi "Shicchan hat versucht, Leute für den Schülerrat zu finden, weil er nur aus ihr und Lilly bestand. Dann kam sie zu mir. Ich konnte sie überhaupt nicht verstehen~."


scene ev misha_roof_angry onlayer master
with charachange

mi "Aber~! Shicchan wollte nicht ihren Stift und Block benutzen. Sie wusste, dass ich Zeichensprache-Unterricht nahm."
mi "Ich wurde schnell bloßgestellt; ich konnte gar nichts~… Das hat sie nur noch energischer gemacht. Ich hasste sie und dachte, sie macht sich über mich lustig."


scene ev misha_roof_normal onlayer master
with charachange

mi "Aber so war es nicht~…"


"Misha lächelt, während sie sich erinnert."


mi "Also~! Hab ich mich nach und nach in Shicchan verliebt und ihr dann gesagt… dass ich sie liebe."


scene ev shizu_flashback onlayer master:
    truecenter
    zoom 1.15 subpixel True
    easein 30.0 zoom 1.0
with whiteout

mi "Es war im Schülerratsraum, weißt du. Als wir nur zu zweit waren."


mi "Ich hatte diese Fantasie, dass Shicchan allein im Büro sitzt und versucht, alles ganz allein zu regeln. Es kam mir so einsam und so traurig vor~. Ich glaube, ich wollte, dass es so ist."


mi "So könnte ich für Shicchan da sein, und vielleicht würde mich Shicchan mögen."
mi "Ich glaubte das, obwohl ich dazu keinen Grund hatte. Ich wollte, dass es wahr wird, darum ließ ich mich weiter daran glauben, auch wenn ich denke, dass ich es besser wusste."


mi "Dieser Tag war auch wirklich, wirklich schön, Hicchan~. Wir waren mit allem fertig, und ich sah aus dem Fenster. Selbst durch das Fenster war das Licht so warm~… Ich wollte, dass dieser Moment nie zu Ende geht."


mi "Aber~! Dann sah ich zu Shicchan."
mi "Sie hatte ihren Rücken zum Fenster und arbeitete immer noch an etwas, als ob sie den Rest der Welt ausgeblendet hätte. Das Licht lag auf ihren Schultern, so wie ich mir als kleines Kind immer eine Decke um meine Schultern gelegt hatte."


"Misha hält einen Augenblick inne, als ob sie versucht, dieses Bild von Shizune in ihren Gedanken festzuhalten."


mi "Es war… hm~… Es war, als brachte mich dieser Anblick von Shicchan dazu, mit ihr zusammen sein zu wollen… Aber ich fühlte, dass das schwierig sein würde."


mi "Wahaha~. Das ist~ wirklich~ lange~ her. Damals war meine Frisur auch anders. Etwas chaotisch vielleicht~? Ich hab sie abgeschnitten, weil Shicchan immer davon gesprochen hatte."


mi "Jedenfalls~! Genau dann und dort hab ich es gesagt; es ihr gestanden~."


scene ev misha_roof_sad onlayer master
with whiteout

mi "Ich wurde zurückgewiesen~."


mi "Darum~ dachte ich: „Das war's dann”, Hicchan. Aber Shicchan versuchte immer, mich zu finden, und ich fing deswegen wieder an, sie zu hassen. Und als ich sie fragte, warum sie das tat, sagte sie, dass ich ihre Freundin wäre."


"Ein sanftes Rot ziert ihre Wangen. Ich frage mich, wie viel Erfahrung sie mit Weinen hat, dass sie sich so gut dagegen wehren kann. Wenn sie nicht eine Pause eingelegt hätte, um sich die Augen abzuwischen, hätte ich es vielleicht nie bemerkt."


scene ev misha_roof_closed onlayer master
with charachange

mi "Dass Shicchan das sagte, machte mich glücklich, aber auch traurig. Und auch wenn sie mich niemals damit verletzen wollte, tut es trotzdem weh. Sogar jetzt noch…"


mi "Shicchan weiß, wie man Leute manipulieren kann, Hicchan. Manchmal beabsichtigt sie es und manchmal nicht wirklich, aber es geschieht trotzdem~. Und manchmal bin ich mir einfach nicht sicher… was gerade der Fall ist. Und ich kriege Zweifel…"


mi "Ich wünschte einfach, dass Shicchan mich mag anstatt dich. Ich habe mich gefragt, ob ich anfange, dich und Shicchan zu hassen… Nur ein bisschen. Ich… mochte diesen Gedanken nicht."


hi "Also dachtest du, es wäre vielleicht besser, wenn ich gar nicht hier wäre?"


scene ev misha_roof_normal onlayer master
with charachange

"Sie sieht verwirrt aus. Der Gedanke ist ihr wohl noch nie in den Sinn gekommen."


mi "Das ist es nicht, Hicchan."


scene ev misha_roof_sad onlayer master
with charachange

mi "Ich hab in den letzten Tagen häufig darüber nachgedacht. Ich will niemanden hassen. Weder dich noch Shicchan. Es ist so bescheuert, dass ich je so gefühlt habe, nicht wahr, Hicchan? Ich will nie wieder an dieses Zeug denken müssen."


mi "Und Menschen zu vermissen – getrennt von ihnen zu sein; ich hab genug davon, und ich will auch nicht mehr daran denken müssen."


mi "Auch wenn ich das schon getan hab. Also!~ Ich bin wirklich die schlimmste Art von Mensch. Ich dachte nicht, dass es besser wäre, wenn Hicchan nie an diese Schule gekommen wäre. Ich dachte… wäre es nicht besser, wenn ich einfach sterben würde?"



label de_S29xa:


scene ev misha_roof_closed onlayer master
with charachange

mi "Schließlich hab ich nun etwas wirklich Schreckliches getan. Unverzeihlich schrecklich."


"Misha presst sich stärker gegen den Zaun in ihrem Rücken, als hoffte sie, hindurchschlüpfen zu können."


hi "Sei nicht blöd."


"Mich überrascht der Klang meiner Stimme."


hi "Entschuldigung."


hi "Ich hab begriffen, dass ich es hasse, wenn ich irgendetwas bedauere. Aber trotzdem ist es für mich unmöglich, etwas nicht zu bedauern."


hi "Gestern habe ich etwas Dummes getan. Das ist wahrscheinlich auch ein Teil des Grundes, warum ich gerade hier bin. Damit ich herausfinden kann, ob ich es vielleicht… irgendwie wiedergutmachen kann."


hi "Hast du jemals so darüber gedacht? Du hast gesagt, dass du schreckliche Dinge getan hast. Du kannst versuchen, sie wieder in Ordnung zu bringen."


scene ev misha_roof_normal onlayer master
with charachange

mi "Hicchan~, heißt das…"


"Ich weiß, dass sie denkt, dass ich das mehr für mich als für sie sage."


hi "Nein, heißt es nicht."


hi "Ich denke einfach, dass sich selbst umzubringen die schlechteste Entscheidung ist, zu der ein Menschen kommen kann."


mi "…"


mi "Hicchan, du bist so dramatisch."


scene ev misha_roof_closed onlayer master
with charachange

"Ob sie das ernst gemeint hat oder nicht, werde ich nie erfahren. Ich versuche es auch nicht."
"Sie gibt einen Seufzer von sich und schließt ihre Augen, als ob sie einschlafen würde. Ich spüre, dass diese gefährliche Stimmung, die von ihr ausging, vorüber ist."



label de_S29xb:

stop music fadeout 0.5
$ renpy.music.set_volume(0.0, 0.5, channel="ambient")

"Misha presst sich stärker gegen den Zaun in ihrem Rücken, als hoffte sie, hindurchschlüpfen zu können."


scene bg school_roof_ss onlayer master
show mishashort perky_confused_close_ss onlayer master at center
with vpunch

$ renpy.music.set_volume(1.0, 6.0, channel="ambient")

"Ohne wirklich darüber nachzudenken, greife ich ihre Hand. Meine Reflexe sind furchtbar, und ich erwische nur ein paar ihrer Finger, aber das ist unwichtig."


play music music_rain fadein 6.0

hi "Sorry. Du hast nur gerade etwas ziemlich Seltsames gesagt."


show mishashort perky_sad_close_ss onlayer master
with charachange

mi "Hahaha~. Ja~, schätze, das habe ich, Hicchan."


hi "Ja."


hi "Willst du wissen, was ich denke?"


hi "Shizune ist die Art von Mensch, die niemanden an sich heranlässt, es sei denn zu ihren eigenen Bedingungen. Es ist frustrierend, manchmal treibt es mich sogar zur Weißglut."


hi "Das hätte mich wahrscheinlich nicht gestört, als ich im Krankenhaus war und jeder, der mich ausgeschlossen hat, für mich gestorben war. Ich hatte das alles bis vor Kurzem vergessen. Ich hab einen Brief bekommen, in dem es genau darum ging."


hi "Ich war wütend. Ich dachte: „Wie kannst du mir unterstellen, dass ich mich von allen abgrenze und aufgebe? Haben das nicht alle mit mir getan? Was sollte ich denn sonst tun? Was kann ich tun?”"


hi "Ja, sogar jetzt weiß ich, dass es so war. Aber… sie hatte auch Recht. Ich habe mich abgegrenzt."


hi "Darum habe ich beschlossen, das nie wieder geschehen zu lassen."


show mishashort perky_confused_close_ss onlayer master
with charachange


label de_S29xba:

mi "Im Krankenhaus? Hicchan… Waren dafür die ganzen Tabletten?"



label de_S29xbb:

mi "Im Krankenhaus? Hicchan… Was…"



label de_S29xbc:

hi "Hör einfach zu, bitte."


hi "Shizune ist das Gegenteil meines früheren Ichs. Sie wollte Leute immer näher an sich ziehen."
hi "Ich glaube, das ist der einzige Grund, warum Shizune überhaupt an mir interessiert war. Und ich glaube, ich war irgendwie entschlossen, das nicht passieren zu lassen."


"Misha versteht mich voll und ganz und senkt ihren Blick."


hi "Ich hab nie gemerkt, wie schwierig das sein kann."


hi "Und jetzt will ich diesen Gefallen zurückzahlen, auch wenn es doppelt so lange dauert. Ich habe bereits eine zweite Sprache gelernt, nur um so weit zu kommen."


hi "Es war nicht so schwierig wie erwartet, aber schwierig war es auf jeden Fall. Manchmal fühlte es sich an, als würde ich einen Berg besteigen. So sehr haben meine Hände wehgetan."


hi "Und du hast dasselbe getan. Und aus dem gleichen Grund, oder nicht? Das ist wirklich erstaunlich. Darum macht es mich traurig, und etwas wütend, dass du so etwas Dummes sagen würdest."


mi "…"


hi "Jedenfalls ist das meine Meinung."


show mishashort perky_sad_close_ss onlayer master
with charachange

"Ihre Schultern erschlaffen. Dann rutscht sie fast bis auf den Boden, als ob sie ihre gesamte Kraft aufgebraucht hätte."


mi "Du bist zu dramatisch, Hicchan."


"Sagt sie, während sie wegsieht und ihren Kopf fast so weit dreht, als ob sie auf das Schulgelände sehen wollte, aber dafür ist es nicht weit genug."


mi "Wahaha~."



label de_S29y:

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg school_roof_ss onlayer master
show mishashort perky_confused_close_ss onlayer master at center
with locationchange

stop music fadeout 0.5
$ renpy.music.set_volume(0.2, 0.0, channel="sound")
play sound sfx_door_creak

"Die Tür hinter uns öffnet sich, das Geräusch kaum hörbar bei dem Wind hier oben."


scene bg school_roof_ss onlayer master at bgleft
show mishashort perky_confused_close_ss onlayer master at closeleft
with charamove

show shizu behind_blank_ss onlayer master at tworight
with charaenter

ssh "Ich hab euch zwei schon überall gesucht. Ist das hier ein Geheimtreffen?"


"Sie kommt zu uns und lehnt sich neben Misha gegen den Zaun, als ob sie innehalten und zu Atem kommen müsste, bevor sie sich wieder davon abstößt und fortfährt."


show shizu basic_normal_ss onlayer master
with charachange

ssh "Es ist langweilig, jeden Tag im Schülerratsraum zu sitzen, ohne dass einer von euch je vorbeikommt. Sich eine Auszeit zu nehmen ist in Ordnung, aber das ist einfach zu viel."


"Normalerweise würden Misha und ich uns in diesem Moment scherzhafte Ausreden für uns ausdenken. Aber diesmal herrscht nur Stille. Shizune, die wie sonst auch Widerstand erwartet, wird durch diese Stille aus dem Konzept gebracht."


$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_snap
show shizu adjust_happy_ss onlayer master
with Dissolve(0.3)

"Eine Sekunden vergehen in unbehaglicher Stille, die Shizune mit ihrem ohrenbetäubenden Fingerschnipp unterbricht. Sie lächelt, als würde sie „Heureka!” sagen."


show shizu basic_happy_ss onlayer master
with charachange

ssh "Lasst uns etwas zusammen unternehmen."


hi "Und was?"


show shizu behind_smile_ss onlayer master
with charachange

ssh "Irgendwas! Wir sollten zuerst zurück zum Schülerratsraum und uns dann dort etwas überlegen."


hi "Das klingt wie ein Trick, um uns zum Arbeiten zu kriegen."


show shizu basic_normal2_ss onlayer master
with charachange

ssh "Sehr witzig."



label de_S29ya:

show shizu behind_smile_ss onlayer master
with charachange

ssh "Es ist kein Trick. Versprochen. Es wird etwas Lustiges sein."


show mishashort perky_sad_close_ss onlayer master
with charachange

play music music_rain fadein 4.0

"Misha macht ein trauriges Gesicht – ganz anders als Shizunes herzliches Lächeln."


"Falls Misha wirklich eifersüchtig ist, weil ich ihr Shizune weggenommen habe, dann würde alles nur noch schlimmer, wenn wir drei zusammen sind."
"Ich kann mir vorstellen, dass es wie Salz in einer offenen Wunde wäre. Darum komme ich auf die Idee, sie zusammen Zeit verbringen zu lassen."


"Ich bin nicht so idealistisch, dass ich denke, ein Abend unter sich würde alles lösen – aber es könnte helfen. Es erscheint mir besser als mit ihnen zu gehen, denn meine Anwesenheit würde alles andere als helfen."


hi "Ihr Zwei könnt euch amüsieren gehen. Ich geh früh schlafen."


show shizu basic_normal_ss onlayer master
with charachange

ssh "Bist du sicher? Es ist gerade mal nach Mittag."


hi "Ich hab dir doch gesagt, ich fühle mich heute nicht so gut. Ich glaube, ich hab mir etwas eingefangen."


show shizu adjust_frown_ss onlayer master
with charachange

ssh "Ich dachte, du hättest gesagt, dass solche Ausreden nicht funktionieren."


"Erwischt."


show shizu basic_normal2_ss onlayer master
with charachange

ssh "Schon okay. Aber eine Einladung abzulehnen ist unhöflich. Ich erwarte, dass du das wiedergutmachst."


show shizu adjust_happy_ss onlayer master
with charachange

"Shizune dreht sich um, lächelt Misha an, und gebärdet etwas, das ich nicht sehen kann. Ich vermute, es ist etwas wie „sieht aus, als wären wir nur zu zweit.”"


stop music fadeout 3.0

"Das ist gut."


stop ambient fadeout 2.0

window hide


label de_S29yb:

show mishashort hips_grin_close_ss onlayer master
with charachange

play music music_comfort fadein 5.0

"Misha lacht und schafft es, ein gezügeltes „Wahaha” von sich zu geben. Dass Shizune es nicht sehen kann, gibt mir ein besseres Gefühl. Es bedeutet, dass es nicht nur für Shizune bestimmt war."


show shizu behind_smile_ss onlayer master
with charachange

ssh "Ich dachte daran, dass ihr beide mir eigentlich doch bei etwas helfen könntet."
ssh "Was gab es noch? Wir können nicht auswärts essen gehen. Wir haben gestern schon bestellt, und das hat bereits meinem Grundsatz widersprochen. Drei Tage hintereinander wäre unverzeihlich."


show mishashort perky_smile_close_ss onlayer master
with charachange

mi "Aber~! Das war eine Hausbestellung, Shicchan~! Essen gehen ist was anderes."


hi "Ja, total anders."


show shizu adjust_frown_ss onlayer master
with charachange

ssh "Ihr beide veralbert euch selbst."


show shizu basic_normal_close_ss onlayer master at closeright
with characlose

"Bevor ich antworten kann, greift Shizune nach meiner Hand und hält mich davon ab."
"Meine Möglichkeiten reduzieren sich so drastisch, dass ich keine Wahl habe, außer ihr eine Grimasse zu schneiden. Sie tut das gleiche, bevor sie ihre Hand auch zu Misha ausstreckt."


"Als Misha zögert, laufe ich so weit nach vorne, wie Shizunes Handgriff es mir erlaubt und ergreife ihre Hand selbst."


show mishashort hips_smile_close_ss onlayer master
with charachange

mi "… Hahaha."


"Ihr bleibt nur eine Sekunde zum Lächeln, bevor Shizune anfängt, uns ungeduldig in Richtig Tür zu ziehen, was uns wie eine menschliche Kette verbindet."


stop ambient fadeout 1.0

scene ev shizu_hands onlayer master
with locationskip

"Obwohl es gefährlich ist, scheint keiner von uns ans Loslassen zu denken, während wir durch die Schule, aus dem Haupteingang und über das Schulgelände laufen."


"Es kommt mir vertraut vor, als ob wir schon einmal so gelaufen sind. Wir drei – Hand und Hand. Natürlich war die Stimmung damals weitaus glücklicher."


"Ich kann die zurückbleibende Traurigkeit auf ihren Gesichtern sehen und frage mich, ob sich irgendetwas wirklich verändert hat. Ob das alles nur eine Ablenkung ist oder nicht. Aber ich glaube, ich bin einfach nur wieder zynisch. Es ist ein Anfang."


stop music fadeout 3.0

window hide
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
