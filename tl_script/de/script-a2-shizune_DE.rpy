label de_S8:

window hide None

scene bg school_dormhisao onlayer master
with locationchange

with Pause(1.0)

nvl clear

nvl show dissolve

play music music_dreamy fadein 5.0

n "\n\nAm nächsten Morgen rufe ich mir noch einmal die Ereignisse der letzten Nacht ins Gedächtnis. Der Abend war so perfekt, dass es mir schwer fällt, an etwas anderes zu denken."


n "Vielleicht ist das nicht der geeignetste Moment, um in Erinnerungen zu schwelgen, zumal ich gleich in der ersten Stunde einen Test schreibe."


n "Das ist einfach nicht fair. Was haben die sich nur dabei gedacht? Erst veranstalten sie ein großes Fest, in dem die Arbeit mehrerer Wochenendschichten steckt, und dann lassen sie uns gleich am nächsten Morgen eine Arbeit schreiben?"


n "Das ist doch wohl ein schlechter Witz."


n "Ich mache mir deswegen keine allzu großen Gedanken, aber ich frage mich trotzdem, ob sie sich damit nicht eine Woche Zeit hätten lassen können."


n "\n\nNa ja, immerhin ist das Wetter gut genug, um draußen noch ein wenig zu lernen, bevor der Unterricht losgeht."


nvl hide dissolve

scene bg school_courtyard onlayer master
with locationskip

nvl clear

nvl show dissolve

n "\n\nHier draußen ist es weitaus angenehmer, als es im Klassenzimmer wäre. Ganz zu schweigen von der Ruhe. So langsam bekomme ich den Eindruck, dass die Anderen heute länger schlafen werden."


n "Ich lege meine Unterrichtsnotizen für einen Moment beiseite und lasse meinen Blick über das Schulgelände schweifen, das noch immer mit Festbuden übersät ist."


n "Jetzt, da ich sie im Tageslicht und ohne die Menschenmassen und Laternen sehe, die meine Aufmerksamkeit auf sich lenken, bemerke ich etwas Ungewöhnliches."


n "Viele der Stände, die Shizune, Misha und ich gestern Nacht besucht haben, sind gleichzeitig auch die, an denen wir gearbeitet haben."


n "\n…"


n "\nNett. Hat sich Shizune das einfallen lassen? So wie ich sie kenne, war das kein Zufall. Hat sie gehofft, ich würde Gefallen an der Sache finden, wenn ich die Früchte unserer Arbeit sehe?"


play sound sfx_footsteps_soft fadein 5.0
stop music fadeout 4.0

nvl hide dissolve

show shizu basic_normal onlayer master at center
with charaenter

window show

"Als ich das Gras hinter mir rascheln höre, drehe ich mich um. Ich komme mir ein bisschen paranoid vor, aber alles, was ich vorfinde, ist Shizune, wie sie mit Unschuldsmiene hinter mir steht."


play music music_shizune fadein 1.0

show shizu adjust_happy onlayer master
with charachange

shi "…"


hi "Guten Morgen."


"Warum vergesse ich immer wieder, dass sie mich nicht hören kann?"


"Vielleicht liegt es daran, wie sehr ich mich daran gewöhnt habe, dass Misha für uns beide übersetzt. So bin ich kaum in Situationen gekommen, in denen ich wirklich mit Shizunes Taubheit und den Problemen konfrontiert war, die daraus entstehen können."


"Ich glaube, gestern war das erste Mal."


"Ich winke ihr dennoch zu. Zumindest das kann ich tun, aber ich bilde mir nicht einmal für eine Minute ein, auf diese Weise eine Unterhaltung mit ihr führen zu können, wenn man bedenkt, wie wenig Ahnung ich von Gebärdensprache habe."


"Wäre es unhöflich, einfach wieder auf meine Notizen zu schauen? Ich weiß wirklich nicht, was ich sonst tun könnte."


hi "Wo ist Misha?"


show shizu behind_blank onlayer master
with charachange

shi "…"


hi "Nicht nur, weil ich dich nicht verstehen kann. Ihr Zwei seid immer zusammen unterwegs. Euch getrennt voneinander zu sehen ist ungewöhnlich."


"Ich weiß, es ist unsinnig, aber aus irgendeinem Grund ist mir die Situation weniger peinlich, wenn ich mit ihr rede."


show shizu basic_normal2 onlayer master
with charachange

show shizu adjust_happy onlayer master
with charachange

show shizu behind_blank onlayer master
with charachange

"Überraschenderweise wird sie überhaupt nicht wütend. Sie beginnt zu gestikulieren; aber es ist anders als sonst. Shizunes Hände bewegen sich langsamer, und die Gesten sind simpler."


"Ich begreife schnell, dass es sich nicht um Gebärdensprache handelt. Sie versucht trotz allem, mit mir zu kommunizieren."


hi "Soll das die Gebärdenversion von allgemeinverständlicher Ausdrucksweise sein?"


show shizu behind_frown onlayer master
with charachange

"Ich habe Angst, dass ich wie ein Volltrottel aussehe, wenn ich versuche, ihr auf gleiche Art zu antworten."
"Shizunes Gesichtsausdruck sagt mir, dass sie langsam auch zu dem Schluss kommt, dass ein solches Hin und Her wohl nicht der beste Weg ist, um irgendetwas zu erreichen."


"Es muss doch einen besseren Weg geben."


"Auf einen Block schreiben? Papier und Stift hätte ich. Was gäbe es sonst noch?"


"Handys? Ich benutze meines kaum, deshalb habe ich es fast nie bei mir, und ich weiß nicht, ob Shizune überhaupt eins hat."


show shizu adjust_happy onlayer master
with charachange

show shizu basic_normal onlayer master
with charachange

"Sie ergreift die Initiative, indem sie einen Finger hebt und mir signalisiert zu warten. Sie zieht einen Block und einen Stift aus ihrer Tasche und schreibt ein einzelnes Wort darauf."


window hide

$ written_note("Hallo.")


show shizu basic_normal2 onlayer master
with charachange

window show

shi "…"


"Ich starre sie ausdruckslos an und erhalte einen ähnlichen, aber irgendwie bedrohlicheren Blick als Antwort. Sie streckt mir den Block energisch noch ein Stückchen entgegen. Offensichtlich will sie eine Antwort von mir."


window hide

$ written_note("Guten Morgen.")


show shizu behind_smile onlayer master
with charachange

window show

"Shizune strahlt mit unverhältnismäßig großer Freude. Triumphierend wirbelt sie den Stift in ihrer Hand, während sie darüber nachdenkt, was sie als nächstes schreiben könnte."


hi "Oh, komm schon, es ist ja nicht so, als hätten wir gerade das Feuer erfunden."


show shizu basic_frown onlayer master
with charachange

"Als ob sie mich gehört hätte, rückt Shizune mit einer schnellen Handbewegung ihre Brille zurecht und beginnt mit atemberaubender Geschwindigkeit zu schreiben."


window hide

$ written_note("Benutz den Block! Schreib schreib schreib schreib schreib schreib schreib schreib schreib schreib schreib schreib schreib schreib schreib schreib schreib schreib schreib schreib schreib!")


window show

"Ich bin verwirrt. Soll ich jetzt den Block nehmen und „okay” schreiben?"


"Das ist wohl das genaue Gegenteil von einer flüssigen Konversation. Ich beneide Misha, weil sie so problemlos mit Shizune kommunizieren kann."


window hide

show shizu behind_blank onlayer master
with charachange

$ written_note("Lernst du für den Test?")


window show

"Ich bin mir relativ sicher, dass ich bei simplen Ja- oder Nein-Fragen mit einem Nicken davonkomme."


window hide

show shizu adjust_smug onlayer master
with charachange

$ written_note("Du bist ziemlich früh dran. Die Meisten schlafen nach dem Fest aus. Das bedeutet, du bist abnormal.")


window show

"… Ist das so?"


window hide

$ written_note("Du bist doch auch hier.")


window show

"Bevor ich ihr meine Antwort jedoch aushändige, erinnere ich mich an meine Entdeckung von vorhin und füge hinzu:"


window hide

$ written_note("Du bist doch auch hier.\n\nDas Fest gestern hat Spaß gemacht. Ich habe heute bemerkt, dass ich viele von den Ständen, bei denen wir waren, zusammengebaut habe. Wahrscheinlich kamen sie mir deshalb so bekannt vor. War das wieder ein Spiel?")


show shizu behind_frown onlayer master
with charachange

window show

"Sie schüttelt empört den Kopf."


window hide

$ written_note("Keine Tricks.")


show shizu basic_normal2 onlayer master
with charachange

$ written_note("Ich dachte mir, dass die Stände, die du gebaut hast, die wichtigsten waren. Wir mussten sie uns anschauen. Schließlich sollte jeder die Früchte seiner Arbeit zu schätzen wissen. Ich wollte, dass du siehst und genießt, was du geschaffen hast.")


window show

"Irgendwie rührend. Dennoch würde ich gerne wissen, warum sie sich die Mühe gemacht hat, und frage sie danach."


window hide

show shizu behind_blank onlayer master
with charachange

stop music fadeout 3.0

$ written_note("Weil du so deprimiert warst.")


window show

"Ich will erwidern, dass ich die letzten Tage nicht deprimiert war, halte aber inne."
"Es stimmt – ich habe ganz schön Trübsal geblasen und war dabei meistens nicht einmal besonders subtil, also ist es möglich, dass sie das mitbekommen hat. Hat sie das alles nur getan, um mich aufzuheitern?"


hi "Danke."


"Das Wort ist mir herausgerutscht, bevor ich mich zurückhalten konnte, aber Shizune scheint es nicht bemerkt zu haben. Stattdessen schreibe ich das Gesagte noch einmal auf. Sie nickt einmal, als ob sie nicht daran gewöhnt wäre."


"Die Stille zwischen uns wächst mit jeder verstreichenden Sekunde, und es gibt nichts, was ich tun könnte, um sie zu beenden. Alles auf Papier aufschreiben zu müssen zerstört jegliche Hoffnung auf eine lockere Unterhaltung."


window hide

show shizu adjust_happy onlayer master
with charachange

$ written_note("Viel Erfolg bei der Klausur.")


window show

"Shizune hält mir den Block genau vor die Augen und reißt mich aus meinen Gedanken. Wie immer ergreift sie die Initiative."


hide shizu onlayer master
with charaexit

"Irgendwie fühle ich mich etwas niedergeschlagen, als sie im Schulgebäude verschwindet."


window hide

nvl clear
nvl show dissolve

n "\n\nDas waren vermutlich die längsten 20 Minuten meines Lebens. Alles nur, weil es so ungewohnt ist, sich mit jemandem zu unterhalten, indem man Zettel austauscht. Vor allem wenn einem die meiste Zeit praktisch nichts einfällt."


n "Das Erlebnis lässt in mir wieder den Wunsch aufsteigen, Gebärdensprache zu lernen."


n "Das ist allerdings einfacher gesagt als getan. Obwohl… In einer Schule wie Yamaku gibt es bestimmt auch Kurse in Gebärdensprache. In diesem Fall gäbe es eigentlich keinen Grund, die Idee nicht weiter zu verfolgen."


n "Die einzige Person, die mir momentan einfällt und von der ich glaube, dass ich sie fragen kann, ist Misha."


n "Wie dringend möchte ich das wissen? Es gibt zwei Möglichkeiten: Bis nach dem Unterricht warten oder gleich nach ihr suchen."


n "Ich schätze, ich werde sie gleich suchen gehen, aber ich bin mir nicht sicher, wo sie gerade steckt. Die besten Chancen habe ich wohl, wenn ich vor dem Mädchenwohnheim auf sie warte. Da sie ja nicht bei Shizune war, ist das vermutlich der einzige Ort, an dem sie sonst sein könnte."


nvl hide dissolve
nvl clear

scene bg school_dormext_full onlayer master
with locationchange

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_daily fadein 1.0

nvl show dissolve

n "\n\nAls Junge kann ich mich nicht einfach so frühmorgens vor dem Mädchenwohnheim herumtreiben. Aber Misha vor Shizunes Augen nach Kursen in Gebärdensprache zu fragen, wäre schlichtweg undenkbar."


n "Sie muss irgendwann einmal zum Unterricht. Immerhin sind wir in derselben Klasse, also muss sie diese Klausur auch schreiben."


n "Wenn ich hier warte, kann ich sicher sein, dass sie früher oder später vorbeikommt."


n "Ich hoffe nur, sie läuft nicht einfach an mir vorbei, während ich meine Notizen noch einmal durchgehe."


n "\n\nDie Wartezeit erweist sich als ziemlich lang. Während die anderen in der Schule verschwinden, frage ich mich langsam, ob Misha zu spät kommen wird."


n "Am Ende erspähe ich sie dann aber doch. Während sie über den Schulhof stürmt, wird mir klar, dass ich blind sein müsste, um ihr extrem auffälliges Haar zu übersehen."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

show misha hips_grin onlayer master at center
with charaenter

window show

mi "Hi, Hicchan~! Guten Morgen~!"


hi "Morgen."


"Ich habe nicht viel Zeit, bevor der Unterricht anfängt, also komme ich direkt zur Sache."


hi "Hey, kann ich dich was fragen?"


show misha perky_smile onlayer master
with charachange

mi "Eine Frage? Hm~… Okay Hicchan~! Kein Problem~! Ich hab Zeit. Aber nur, weil ich spät dran bin!"


hi "Was soll das heißen?"


show misha hips_grin onlayer master
with charachange

mi "Haha~. Ich hätte früher aufstehen sollen, aber ich war so müde~… Wäre ich früher aufgestanden, hätte ich noch lernen müssen. Aber da ich das nicht getan habe, kann's nicht schaden~! Was gibt's denn, Hicchan?"


hi "Na ja, es gibt hier Kurse für Gebärdensprache, oder?"


show misha hips_smile onlayer master
with charachange

mi "Jepp~! Es sind Wahlfächer! Warum fragst du, Hicchan?"


"Aus irgendeinem Grund versetzt mich diese Frage für einen Augenblick in Panik."


hi "Nur so. Es klingt interessant, aber ich schätze mal, es ist zu spät sich einzuschreiben, oder?"


"Ich bin gerade nicht sehr subtil, aber es wäre das erste Mal, dass Misha etwas derartiges bemerkt. Vermutlich bin ich vorsichtiger, als ich sein müsste."


show misha sign_smile onlayer master
with charachange

mi "Hm~? Ach weißt du Hicchan, ich habe gehört, dass pro Jahr immer weniger Schüler Gebärdensprache belegen. Also! Wenn du willst, bin ich mir sicher, dass sie dich mitmachen lassen~!"


show misha hips_grin onlayer master
with charachange

mi "Denkst du darüber nach, Gebärdensprache zu lernen, Hicchan?"


hi "… Schon."


show misha perky_smile onlayer master
with charachange

mi "Wenn du Gebärdensprache lernen würdest, Hicchan, dann würde das Shicchan wirklich glücklich machen~. Wenn du willst, können wir nach der Schule zum Lehrerzimmer. Sie werden dich bestimmt noch aufnehmen."


hi "Das wäre klasse."


hi "Aber sag Shizune nichts davon."


show misha perky_confused onlayer master
with charachange

mi "Warum nicht?"


hi "Es soll eine Überraschung sein. Davon abgesehen wäre es peinlich, wenn du es ihr jetzt direkt erzählst, und ich dann heute Nachmittag herausfinde, dass ich den Kurs gar nicht belegen darf."


show misha perky_smile onlayer master
with charachange

mi "Aw~. Du hast Recht, Hicchan. Das wird aber schwierig~… Es sind so gute Neuigkeiten…"


hi "Ich bin im Schülerrat, also sollte ich versuchen, es zu lernen. Auch wenn es nur die Grundlagen sind, ist das besser als nichts. Außerdem können Shizune und ich nicht immer nur über dich kommunizieren, als wärst du ein Telefon oder so was, stimmt's?"


"…"


with Pause(2.0)

show misha hips_laugh onlayer master
with charachange

mi "Wahaha~!"


show misha hips_grin onlayer master
with charachange

mi "Du hast Recht, Hicchan~!"


"…"


stop music fadeout 4.0
play sound sfx_warningbell

"Die Pausenglocke läutet den Beginn der ersten Stunde ein, was unsere Konversation unerwartet beendet. Ich schätze, ich werde einfach einen der Lehrer fragen, sobald der Unterricht vorbei ist."


"Ihre Reaktion war etwas merkwürdig, aber im Laufe des Tages vergesse ich das wieder."


scene black onlayer master
with dissolve


label de_S9:

scene bg school_scienceroom onlayer master
with locationchange

play sound sfx_normalbell

"Die Pausenglocke läutet, und die Gesten der Lehrerin vorne bedeuten, dass der Gebärdensprache-Unterricht für heute vorbei ist."


play music music_normal fadein 3.0

"Obwohl es überraschend leicht war, in diese Klasse zu kommen, sind erst wenige Tage vergangen, und ich bin noch nicht an diese Erfahrungen gewöhnt."
"Die Gesten selbst kann ich mir schneller aneignen als ich dachte, aber die meisten meiner Mitschüler sind schwerhörig."


"Darüber hinaus bevorzugt die Lehrerin vollständige Immersion. Ihre Stimme habe ich seit meiner Frage, ob ich den Kurs belegen könnte, nicht mehr gehört. Das Konzept ist ungewohnt – und außerdem wirklich stressig."


scene bg school_hallway3 onlayer master
with locationchange

"Gerade als ich einen Schritt aus der Klassenzimmertür gemacht habe, höre ich etwas links von mir den Ausbruch eines vertrauten Gelächters."


show misha hips_grin onlayer master at center
with charaenter

mi "Hi, Hicchan~!"

"Misha ist nicht in meinem Kurs für Gebärdensprache. In diesem Zusammenhang sehe ich sie also zum ersten Mal. Ich weiß immer noch nicht, ob ihre Abwesenheit in meinem Kurs ein gutes oder ein schlechtes Zeichen ist."


"Mit ihr wäre es interessanter – aber das Risiko, peinliche Momente zu erleben, würde dramatisch steigen."


hi "Hi."

show misha sign_smile onlayer master
with charachange

mi "Es überrascht mich, dich hier zu sehen, Hicchan! …Ah, genau! Du machst bei Gebärdensprache mit, stimmt's~? Stimmt~!"


show misha perky_smile onlayer master
with charachange

mi "Wie findest du es bisher, Hicchan?"


hi "Eine neue Sprache zu lernen ist nicht einfach, aber ich denke, langsam habe ich den Dreh raus. Es ist zwar anders als andere Sprachen, trotzdem ist es leichter als Englisch."


show misha cross_grin onlayer master
with charachange

mi "Haha~! Wirklich, Hicchan?"


show misha cross_smile onlayer master
with charachange

mi "Hm~… Finde ich auch~!"


"Das sollte eigentlich nur ein Scherz sein, aber sie meint es anscheinend vollkommen ernst."


"Ich frage mich, wie Misha mir alles so mühelos übersetzen kann, während sie sich gleichzeitig mit Shizune in einer ganz anderen Sprache unterhält."


"Bis jetzt habe ich es für selbstverständlich gehalten, wie erstaunlich das ist."


"Irgendjemand rempelt mich an der Schulter an und entschuldigt sich dafür. Hier ist es ziemlich voll geworden, was gegen Ende des Tages wohl normal ist."


hi "Ich schätze, wir sollten woanders weiterreden als mitten auf dem Gang. Gehen wir aufs Dach oder so."


show misha sign_smile onlayer master
with charachange

mi "Okay~!"

"Ich habe mich entschieden, das Gespräch unterwegs fortzusetzen. Überraschenderweise ist es still genug dafür."


$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0

scene bg school_staircase1 onlayer master
with locationchange

stop music fadeout 5.0

hi "Ich habe mich immer noch nicht daran gewöhnt, dass ich meine Lehrerin die ganze Zeit ansehen muss."
hi "Ich schätze, ich habe mich über die Jahre einfach zu sehr daran gewöhnt, den Vorträgen zuzuhören und nebenbei etwas herumzukritzeln. Sich Notizen zu machen ist so auch viel schwieriger."


hi "Die Klasse im Einführungskurs ist klein, und ich hinke schon hinterher. Ich habe wohl noch einiges zu tun."


play sound sfx_door_creak
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg school_roof onlayer master
with locationchange

hi "Ja, das ist viel besser."


"Ich drehe mich zu Misha um und sehe, dass sie mich mit den Händen auf der Hüfte und aufgeplusterten Backen anstarrt."


show misha hips_frown onlayer master
with charaenter

play music music_happiness fadein 4.0

mi "Hicchan, du hinkst hinterher? Das ist ganz und gar nicht gut!"


hi "Ich habe den Kurs eine Woche später als alle anderen begonnen. Ich hole das schon auf."


show misha sign_smile onlayer master
with charachange

mi "Okay, Hicchan, dann wollen wir doch mal sehen, was du gelernt hast~! Ich gebe dir Privatunterricht, okay~?"


"Das ist das erste Mal, dass ich den Satz „Ich gebe dir Privatunterricht” woanders als in einem schmutzigen Film höre. Das hat mich nicht einmal ansatzweise so angemacht, wie ich es mir vorgestellt habe."


hi "Ich weiß nicht, ob ich schon eine Privatlehrerin brauche."


show misha perky_sad onlayer master
with charachange

mi "Ohh…"


"Sie sieht enttäuschter aus als sonst. Dieser Gesichtsausdruck macht mich verlegen."


show misha hips_frown onlayer master
with charachange

mi "Ich möchte Lehrerin in Gebärdensprache werden, Hicchan! Aber~ es wäre wirklich toll, wenn ich erst mal versuche, jemanden darin zu unterrichten. Selbst wenn es nur für kurze Zeit ist, wäre das eine wertvolle Erfahrung."


hi "Äh, also, schon, das stimmt."


hi "Ich wusste gar nicht, dass du Lehrerin für Gebärdensprache werden willst."


"Ich kann mir kaum vorstellen, dass sie nicht bewusst versucht, Schuldgefühle in mir hervorzurufen. In so was ist sie nämlich viel zu gut."


"Trotzdem, das ergibt Sinn. Nach dem, was ich schon gesehen habe, ist sie ausgezeichnet in Gebärdensprache. Bestimmt hat sie auch die passende Stimme für Hörgeschädigte. Ich habe sie trotzdem nie als den Lehrertyp betrachtet."


show misha hips_grin onlayer master
with charachange

mi "Hahaha~! Das ist der Grund, warum ich auf diese Schule wollte, Hicchan!"


show misha sign_smile onlayer master
with charachange

mi "Die Schule ist außerdem richtig teuer, weißt du. Weil ich Lehrerin für Gebärdensprache werden will, muss ich weniger Studiengebühren bezahlen. Sonst wüsste ich nicht, ob ich hier bleiben könnte."


hi "Ach so. Ich glaube ja auch nicht, dass du schlecht im Unterrichten wärst. Ich weiß nur nicht, ob ich das jetzt schon brauche."


show misha perky_sad onlayer master
with charachange

mi "Du hast recht, Hicchan, du bist schlau."


hi "Na ja, nein, da würde ich überheblich klingen."


hi "In Ordnung, bitte gib mir Privatunterricht."


show misha cross_laugh onlayer master
with charachange

mi "Ahahaha~! Wirklich? Okay~! Okay okay okay~! Juhu~! Danke, Hicchan~! Ich geb mein Bestes!"


show misha sign_smile onlayer master
with charachange

mi "Lass uns direkt anfangen~!"


hi "Zu früh."


show misha perky_sad onlayer master
with charachange

"…"

mi "Ich vermisse Shicchan~…"


hi "Hast du sie nicht erst heute Morgen gesehen?"


show misha sign_smile onlayer master
with charachange

mi "Aber Hicchan, im Unterricht ist es schwierig, mit ihr zu kommunizieren! Und Schülerrat haben wir heute auch nicht~."


hi "Na ja, wir hatten die ganze Woche lang Prüfungen – ich bin froh, wenn die vorbei sind. Wenn wir da zusätzlich noch Schülerratssitzungen hätten, wäre ich ziemlich sauer."


show misha perky_confused onlayer master
with charachange

mi "Du hast aber nicht vor auszusteigen, sobald wieder mehr zu tun ist, oder, Hicchan?"


hi "Natürlich nicht. Ich bin schließlich Mitglied."


hi "Keine Sorge, ich werde nicht einfach so aufhören und nicht mehr auftauchen. Versprochen ist versprochen."


"Misha schweigt einen Moment und sieht nicht sehr überzeugt aus."


show misha sign_smile onlayer master
with charachange

mi "Shicchan ist der Schülerrat sehr wichtig, Hicchan. Seit du beigetreten bist, strengt sie sich noch mehr an als vorher, weil sie einen guten Eindruck machen will."


show misha hips_frown onlayer master
with charachange

mi "Ein paar andere Leute waren beigetreten, sind aber kurz danach nicht mehr wiedergekommen. Shicchan hat versucht, mehr Leute für den Schülerrat zu interessieren, war aber nicht erfolgreich."



show misha perky_sad onlayer master
with charachange

mi "Selbst wenn jemand den Willen zeigte beizutreten, kam er irgendwann nicht mehr. Sie haben sich Entschuldigungen ausgedacht und es immer weiter hinausgeschoben, bis sie dann gar nicht mehr gekommen sind."


show misha sign_smile onlayer master
with charachange

mi "Jedenfalls… glaube ich, dass du es wirklich ernst meinst, Hicchan."


"Meine Augen kleben an ihren Händen, die sich nahezu von allein bewegen. Mit sanften Gesten übersetzt sie alles, was sie sagt, für sich selbst."





show misha perky_smile onlayer master
with charachange

mi "Als du gesagt hast, dass du mitmachst, war sie wirklich glücklich."


show misha hips_smile onlayer master
with charachange

mi "Shicchan hält dich für interessant, Hicchan. Ein uninteressanter Mensch hätte nicht den Tatendrang, den man für einen Beitritt braucht. Oder er würde schnell wieder aufhören."


mi "Das hat Shicchan gesagt."


show misha hips_grin onlayer master
with charachange

mi "Also~! Es ist meine Pflicht sicherzustellen, dass du dabei bleibst~!"


hi "Willst du mich deshalb unterrichten? Du bist ein ziemliches Schlitzohr."


show misha cross_laugh onlayer master
with charachange

mi "Wirklich, Hicchan? Das ist das erste Mal, dass jemand so was über mich sagt~! Wahahaha~!"


"Keine Chance, dass ich der Arbeit im Schülerrat jetzt noch entgehen könnte."


"Wenn ich so an die letzten paar Tage zurückdenke, begreife ich langsam, warum ich in erster Linie eingetreten bin: Wegen Shizune. Ihr Konkurrenzdenken und ihre Willensstärke sind faszinierend."


"Misha kann ich das aber nicht sagen."


show misha sign_smile onlayer master
with charachange

mi "Okay, Hicchan, lass uns mal überprüfen, was du heute im Kurs gelernt hast~!"


hi "Du weißt doch noch gar nicht, was ich heute im Kurs gelernt habe."


show misha hips_grin onlayer master
with charachange

mi "Hm~, du hast recht, Hicchan~! Okay, dann fangen wir mit den Grundlagen an~! Ich werde dir einfach alles von Anfang an beibringen~!"


hi "Du machst Witze, oder?"


show misha perky_confused onlayer master
with charachange

mi "Häh~?"


hi "Du hast das ernst gemeint? Das wäre ja tagelanger Unterricht, und wir lernen noch nicht mal auf dem gleichen Niveau…"


show misha sign_smile onlayer master
with charachange

mi "Das ist wie Fahrradfahren, Hicchan~! Man verlernt es nie! Wahaha~!"


show misha sign_confused onlayer master
with charachange

mi "Allerdings weiß ich gar nicht, wie man Fahrrad fährt~…"


"Oh nein."


show misha hips_grin onlayer master
with charachange

mi "Richtig, richtig~. Ich will eines Tages Lehrerin sein, da weiß ich natürlich genau, was ich tue… Okay~! Okay okay okay~! Fangen wir an~!"


stop music fadeout 3.0

show misha perky_confused onlayer master
with charachange

mi "Äh…"


show misha sign_confused onlayer master
with charachange

mi "… Mmm~…"

show misha perky_sad onlayer master
with charachange

mi "Ahahaha~…"

"Sie gibt sich anscheinend größte Mühe, daher könnte das ein schlechtes Zeichen sein."
"Na ja, eine Sprache zu lernen ist halt etwas völlig anderes, als sie zu lehren, und der erste Schritt ist immer der Schwierigste. Um ehrlich zu sein, könnte ich es auch nicht besser."


"Trotzdem…"


show misha sign_confused onlayer master
with charachange

mi "Ähm… Offiziell eingeführt wurde die Gebärdensprache im 18. Jahrhundert von einem Franzosen namens…"
mi "Ah… dessen Namen ich nicht aussprechen kann, und er gründete im Jahre 1755 die erste öffentliche Schule für Schwerhörige, aber die ungeschriebene Geschichte der Gebärdensprache besagt, dass…"


show misha sign_sad onlayer master
with charachange

mi "Ich weiß echt nicht, wo ich anfangen soll. Tschuldigung~… Na ja~, wo kann man besser anfangen als bei der Geschichte der Gebärdensprache? Richtig~? Richtig~!"


show misha hips_grin onlayer master
with charachange

mi "Nein, warte, vielleicht doch das Alphabet. Okay~, jetzt ist das Alphabet dran!"


play music music_another fadein 0.5

show misha sign_smile onlayer master
with charachange

mi "Okay, Hicchan~! Das sind so nur die Grundlagen, auch wenn einige Leute glauben, dass das schon die komplette Gebärdensprache ist. Und sie vergessen, dass es jede Menge spezifische Gesten und Wörter gibt."


show misha hips_smile onlayer master
with charachange

mi "Trotzdem kommt man ohne die Grundlagen nicht weit! Das ist das A. Siehst du? Jetzt versuch du es!"


hi "Ich kenne das aber schon."


"Irgendwie amüsiere ich sie."


show misha hips_grin onlayer master
with charachange

mi "Hahaha! Ja, so ist es!"


show misha sign_smile onlayer master
with charachange

mi "Das ist jetzt B und das ist C."


"Misha formt mit jeder Hand ein Symbol, ohne näher zu erklären, welches nun welches ist."


show misha perky_smile onlayer master
with charachange

show misha sign_smile onlayer master
with charachange

show misha hips_grin onlayer master
with charachange

mi "Und jetzt D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, VWXY und Z~!"


"Jepp, das ist übel."


hi "Glaubst du, dass Shizune heute ein Paar Schülerratsaufgaben erledigen will? Wir könnten ihr helfen."


show misha sign_smile onlayer master
with charachange

mi "Natürlich nicht, Hicchan~!! Komm schon, ich mach's noch mal! A, B, C, D, E, F, G, H, I, J, K… Und jetzt du~!"


hi "Also muss heute echt keine Arbeit im Schülerrat erledigt werden, oder so was in der Art?"


show misha hips_smile onlayer master
with charachange

mi "Was redest du denn da, Hicchan? Komm schon, Zeichen, Zeichen~!"


hi "Etwa so?"


show misha sign_smile onlayer master
with charachange

mi "Nein, so!"


hi "Etwa…"


show misha perky_smile onlayer master
with charachange

show misha sign_smile onlayer master
with charachange

mi "So~!"


hi "Äh… häh…"


show misha perky_sad onlayer master
with charachange

mi "Ich wünschte, Shicchan wäre hier. Mit ihr wäre das so viel einfacher. Hahaha, so wird Gebärdensprache jedenfalls meistens gelehrt – mit zwei Lehrern~! Wusstest du das, Hicchan?"


hi "Nein."


"Ich spiele in meinem Kopf durch, wie dieser Unterricht mit Shizune wäre."


"…"

show misha hips_frown onlayer master
with charachange

mi "Hicchan~! Passt du auf?"


hi "Klar."


show misha sign_smile onlayer master
with charachange

mi "Shicchan sagt, Gebärdensprache ist anders als alle anderen, weil man über alles nachdenken muss, bevor man es sagt. Das heißt, jedes Wort hat mehr Gewicht, Hicchan. Jedes einzelne Wort ist wichtiger als sonst."


show misha cross_smile onlayer master
with charachange

mi "Also~, sei bitte aufmerksam."


show misha sign_smile onlayer master
with charachange

"Sie macht mit ihrer Zusammenfassung des Grundwissens der Gebärdensprache weiter. Schließlich beginnt sie mit Unterrichtstoff, den ich wiedererkenne."


"Letztendlich bin ich doch beeindruckt. Bis es soweit war, hatte sie sich einige Patzer geleistet, aber wenn sie ernst bleibt, ist sie eine ziemlich gute Lehrerin."


stop music fadeout 4.0

scene bg school_roof_ss onlayer master
show misha sign_smile_ss onlayer master at center
with shorttimeskip

"Nach einer Weile bemerke ich allmählich, wie spät es geworden ist. Ich bedanke mich bei Misha, verabschiede mich und gehe zurück in mein Zimmer."


stop ambient fadeout 1.0

scene bg school_dormhisao_ss onlayer master
with locationskip

"Ich habe heute eine Menge gelernt."


scene black onlayer master
with dissolve



label de_S10:

play sound sfx_doorknock

scene bg school_dormhisao onlayer master
with vpunch

"Durch donnernde Schläge gegen meine Tür werde ich aus dem Schlaf gerissen."


"Mein erster Gedanke ist, dass es Shizune sein könnte. Im Ernst, wer um diese Uhrzeit so laut an die Tür hämmert, muss entweder taub oder ein Idiot sein."


hi "Wer ist da?"


"Wenn das Shizune ist, kann sie mich natürlich nicht hören und schon gar nicht antworten."


"Es kommt keine Antwort, und irgendwie freue ich mich darüber. Ich habe Shizune schon eine Weile nicht mehr gesehen."


play sound sfx_dooropen

scene bg school_dormhallway onlayer master
show kenji tsun onlayer master at center
with locationchange

play music music_kenji fadein 2.0

"Als ich die Tür öffne, sehe ich Kenji im Gang stehen. Seine Augen huschen nervös von einer Seite zur anderen."


hi "Oh, du bist's."


show kenji neutral onlayer master
with charachange

ke "Ja, ich bin's. Was ist das denn für eine Reaktion?"


hi "Tja, ich hätte dir eine persönlichere Antwort gegeben, wenn du mir geantwortet hättest, wer da ist."


show kenji tsun onlayer master
with charachange

"Kenji schaut mich finster an und schiebt seine Brille nach oben, genau wie Shizune."


ke "Warum machst du so ein komisches Gesicht?"


"Ich frage mich, wie er gerade jetzt meinen Gesichtsausdruck erkennen kann, obwohl er das Millionen andere Male nicht geschafft hat, wenn ich seinetwegen mein Gesicht verzogen habe. Ich würde gerne nachhaken, aber ich bin viel zu müde."


hi "Shizune schiebt ihre Brille genauso hoch. Du weißt schon, die Präsidentin des Schülerrats. Ich finde das nur ein bisschen seltsam."


show kenji rage onlayer master
with charachange

ke "Was zum Teufel? Was meinst du damit, ein Mädchen macht das gleiche? Du meinst, sie berührt ihre Brille? Das ist ganz allein mit Stil."


ke "Wer ist diese Schlampe? Warum mischen sich Schlampen in meine Angelegenheiten ein und machen mich nach?"


show kenji tsun onlayer master
with charachange

"Seine Persönlichkeit wechselt augenblicklich von Wut zu Angst."


ke "Versucht sie etwa, mich zu ersetzen? Körperfresser? Nein, warte, das ist eine exakte Kopie. Körperfresserinnen?"


ke "Es ist, als hätten sich meine zwei schlimmsten Ängste vereinigt."


show kenji rage onlayer master
with charachange

ke "Das ist es!"


"Ich kann nicht glauben, dass da was dran ist…"


show kenji neutral onlayer master
with charachange

ke "Hey, gehst du heute ins Dorf?"


hi "Öh, vielleicht später."


show kenji happy onlayer master
with charachange

ke "Okay. Geil. Ich habe ein paar… Dinge auf der Poststelle und ich möchte, dass du sie für mich dort abholst. Ein paar heikle und geheime Dinge."


"Er spricht im Flüsterton, als ob das Sprechen über seine Post im normalen Tonfall sie in Gefahr bringen würde."


hi "Man kann seine Post direkt hierher schicken lassen, weißt du."


show kenji neutral onlayer master
with charachange

ke "Nein, kann man nicht. Man kann sich seine Post in die Schule schicken lassen, und dann holt sie der Schülerrat ab, und dann wird sie einem gegeben. Das ist nicht die gleiche Post wie die, die in unseren Händen landet."


ke "Ich traue dem Schülerrat nicht. Viele Typen hier bekommen ihre Post nicht, weißt du."


show kenji tsun onlayer master
with charachange

ke "Wahrscheinlich stehlen sie alles! Glauben sie, nur weil die Post zu ihnen geschickt wird, haben sie die Lizenz zu stehlen?"
ke "Ich sehe sie förmlich vor mir, wie sie bis zum Hals in Post stecken und sich so viel von der ganzen Beute schnappen, wie sie tragen können. Ekelhaft."


hi "Wo kann ich diesen Zusteller finden, der Post aus dem Nichts in deine Hände zaubern kann?"


ke "Weiß nicht, ich wette, der Schülerrat hat ihn umgebracht, um das Monopol auf den ganzen Scheiß der Schüler zu bewahren."


hi "So funktioniert das nicht."


hi "Jedenfalls ist es das, was du wolltest? Schön, ich kann deine Post für dich abholen, aber irgendwann komme ich auf all diese Gefallen wieder zurück. Du schuldest mir schon Geld."


show kenji neutral onlayer master
with charachange

ke "Danke, dass du mich daran erinnerst. Ich zahle es dir zurück, nachdem ich mein Paket bekommen habe."


ke "Ja, mein Fehler, bis dahin kann ich dich wirklich nicht bezahlen. Ich bin immer noch pleite."


hi "Dann mache ich das im Prinzip für Geld, wie bei einem Job. Warum brauchst du zuerst das Paket? Ist da Geld drin?"


show kenji happy onlayer master
with charachange

ke "Nö."


"Ich bin vollkommen sprachlos."


hi "Warum bekommst du es nicht?"


show kenji neutral onlayer master
with charachange

ke "Weil ich heute vorhabe, mein Zimmer in eine Einsatzzentrale umzugestalten."


ke "Im Lauf der Zeit habe ich immer mehr begriffen, wie gefährlich der Feminismus ist. Er ist wirklich überall, selbst in Orten wie dem Iran. Du kannst dir nicht vorstellen, welche Ausmaße er hat."


show kenji tsun onlayer master
with charachange

ke "Wenn der Krieg beginnt und wir das Konzept der Nationen nicht überwunden haben, um für unser Geschlecht zu kämpfen, wird es Chaos geben."


ke "Niemand wird wissen, wer welche Seite übernimmt, und ein Krieg gegen den Feminismus würde nicht nur den 3. Weltkrieg bedeuten, sondern auch das Ende allen Lebens auf der Erde, wie wir es kennen."


ke "Wenn wir verlieren, werden all unsere gefügigen, japanischen Frauen von einer Bande soziopathischer lesbischer Rassisten vergewaltigt und versklavt."


ke "Währenddessen wird die Hand voll Männer, die nicht im Krieg umgekommen ist, kastriert und gezwungen, Toiletten zu reparieren und riesige Monumente zum Gedenken an den feministischen Sieg zu errichten."


hi "Das ist irre. Du bist irre. Ich glaube, du denkst zu viel darüber nach."


ke "Tag für Tag begreife ich immer mehr, dass du keine Eier hast."


hi "Wir haben nur etwa vier Mal miteinander gesprochen."


show kenji neutral onlayer master
with charachange

ke "Oh. Sorry."

hi "Ja, wie auch immer, ich werde dein Paket holen."


show kenji happy onlayer master
with charachange

ke "Super."


play sound sfx_doorslam

stop music fadeout 0.5

scene bg school_dormhisao onlayer master
with vpunch

"Ich schließe die Tür und hüpfe sofort wieder ins Bett."


play ambient sfx_alarmclock

"In dem Moment, als mein Kopf auf das Kissen fällt, werden meine Ohren von einem quälend lauten Klingeln angegriffen. Von meinem Wecker. Das heißt, dass ich eigentlich erst jetzt aufstehen sollte."


"An Wochentagen zumindest."


play sound sfx_impact

"Ich greife ihn mir und schleudere ihn ohne hinzuschauen weg. Er bleibt zwischen Bett und Wand stecken, aber der Lärm hört nicht auf. Tatsächlich scheint er sogar lauter zu werden."


stop ambient

"Während ich den Wecker herauszerre, muss ich einsehen, dass ich nicht wieder einschlafen werde. Das einzige, was mir im Moment einfällt, ist ins Dorf zu gehen und Kenjis blödes Paket zu holen. Aber dazu ist es noch zu früh."


"Nach dem Duschen nehme ich meine Medikamente. Eigentlich bin ich sogar sehr hungrig, da ich gestern kein Abendessen und davor nur ein ganz leichtes Mittagessen hatte."


"Ich kaue auf den Pillen herum wie auf einer Lammkeule. Sie sind unfassbar bitter und ekelhaft."


"Na ja, gute Medizin schmeckt schlecht, oder so in der Art. Ich bin immer noch hungrig und muss noch eine Menge Zeit totschlagen. Also entscheide ich mich dafür, ins Dorf zu gehen und irgendwo etwas zum Frühstück zu finden."


"Ich kann mich nicht daran erinnern, wann ich das letzte Mal auswärts gegessen habe. Außerdem ist schönes Wetter, also warum nicht?"


scene bg school_road onlayer master
with locationskip

play music music_soothing fadein 3.0

"Der Weg ins Dorf ist länger als ich dachte, vielleicht weil es schon eine Weile her ist, und wahrscheinlich weil ich selten allein hierherkomme. Weil es noch so früh am Morgen ist, gibt es kaum Autos auf den Straßen. Das macht es ungewöhnlich still."


scene bg suburb_roadcenter onlayer master
with locationchange

"Als erstes suche ich einen Ort, wo man essen kann. Ich muss sofort an das Shanghai denken, will aber etwas Nahrhafteres als Butterbrötchen und Kuchen."


"Da es noch so früh ist, entscheide ich mich dennoch, erst Kenjis Paket abzuholen."


"Das Abholen beim Postamt hat nicht sehr lange gedauert. Aber als ich es sah, war ich wütend darüber, wie nervig es wird, dieses Ding den ganzen Weg zurück in die Schule zu schleppen."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

show kenjibox onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)




"Ich hatte vor, eine kleine Weile umherzuwandern, aber mit diesem Ding wird das ein echtes Problem. Ich schätze, jetzt ist meine einzige Möglichkeit das Shanghai."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

show kenjibox onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide kenjibox onlayer master
with None

"Alles andere hat geschlossen. Und die wenigen Restaurants, die geöffnet haben, bieten in etwa das gleiche Menü. Diese Tatsache bestärkt mich darin, die Zeit bei Yuuko zu verbringen."


stop music fadeout 4.0

scene bg suburb_shanghaiext onlayer master
with locationchange

"Bevor ich überhaupt die Tür öffnen und eintreten kann, tippt mir jemand von hinten auf die Schulter. Ich drehe mich um und sehe Shizune. Instinktiv suche ich nach Misha, aber anscheinend ist sie nicht hier."


show shizu adjust_happy onlayer master at center
with charaenter

ssh "Guten Morgen."


"Sieht so aus, als würden sich die Kurse in Gebärdensprache schon langsam auszahlen. Ich komme in Versuchung, das zurückzugebärden, aber dann glaubt sie vielleicht, ich wüsste viel mehr, als das wirklich der Fall ist."


"Für den Moment winke ich ihr nur und öffne die Tür. Vermutlich ist sie eher wegen ihrer Morgentees hierhergekommen und nicht nur, um mich zu begrüßen. Es zeigt sich, dass ich recht habe, da mir Shizune in das Teehaus folgt."


play sound sfx_storebell

scene bg suburb_shanghaiint onlayer master at bgright
with locationchange

"Hier drin ist völlig tote Hose. Es ist zwar noch nicht ganz Hauptgeschäftszeit, aber jedes andere Café, das ich unterwegs gesehen habe, hatte wenigstens ein paar Kunden."


"Überhaupt ist das Shanghai jedes mal ziemlich leer gewesen, wenn ich daran vorbeigegangen bin. Wie halten sie sich bloß im Geschäft?"


show yuukoshang happy_down onlayer master at center
with charaenter

yu "Hallo! Vielen Dank, dass Sie sich entschieden haben, unser Lokal zu besuchen!"


show yuukoshang neurotic_down onlayer master at Transform(ypos=1.25)
with Dissolvemove(0.2)

play sound sfx_impact
with vpunch

with Pause(0.3)

show yuukoshang neurotic_down onlayer master at center
with charamove

"Yuuko verbeugt sich mit der Kraft einer fallenden Axt und stößt sich den Kopf an der Kiste in meinen Händen, die daraufhin auf den Boden geschleudert wird."


play music music_comedy

show yuukoshang panic_up onlayer master
with charachange

yu "Oh nein, tut mir leid, tut mir wirklich sehr, sehr leid, bitte vergib mir!"


hi "Schon okay, und du brauchst auch nicht zu sagen: „Hallo, danke, dass Sie sich für unser Lokal entschieden haben!” Wir kennen dich doch."


show yuukoshang worried_up onlayer master
with charachange

yu "Aber das gehört zu meinem Job."


show yuukoshang worried_down onlayer master
with charachange

yu "Ihr seid früh dran, was darf ich euch bringen?"


hi "Im Moment möchte ich bloß etwas Kaffee."


show shizu invis onlayer master at right
with None

show yuukoshang worried_down onlayer master at twoleft
show shizu behind_blank onlayer master at tworight
show bg suburb_shanghaiint onlayer master at center
with dissolvecharamove

"Ich frage mich, was Shizune will. Ohne Misha ist es nicht einfach, das herauszufinden, weil ich sie nicht einfach fragen kann. Darüber habe ich noch nichts gelernt. Sie ist hier, also bedeutet das sicherlich, dass sie auch etwas will."


hi "Äh, ich weiß wirklich nicht, was Shizune gern hätte. Das Übliche? Hat sie so etwas?"


hi "Halt, sie könnte ja doch etwas anderes wollen. Vielleicht solltest du uns eine Speisekarte geben, nur für den Fall."


"Ich sehe mich nach einer um, finde aber nichts, das auch nur entfernt an eine Speisekarte erinnert."


show yuukoshang neurotic_up onlayer master
with charachange

yu "Speisekarten… Ich werde sofort eine suchen."


hi "Häh?"


show yuukoshang worried_up onlayer master
with charachange

yu "Ähm… Es gibt Speisekarten. Sie sind bloß… rar."


"Es ist doch nur eine Speisekarte, keine Sammleredition."


show shizu basic_normal2 onlayer master
with charachange

shi "…"

hi "Krass."


show yuukoshang neutral_down onlayer master
with charachange

yu "Sagt das Shizune?"


hi "Nee, sie kann dich nicht hören. Für ein Café ist es einfach krass, dass du gezwungen bist, so einen Aufwand für eine Speisekarte zu betreiben."


show yuukoshang worried_up onlayer master
with charachange

yu "Krass…?"


show yuukoshang neurotic_down onlayer master
with charachange

yu "Ja… das stimmt. Es ist so unlogisch. Es gibt so vieles…"
yu "Zum Beispiel, warum heißt es Shanghai? Dies ist ein Teehaus im westlichen Stil… aber der Name ist chinesisch… und die Architektur ist altmodisch, aber meine Uniform ist so modern und aufwändig…"


"Sie sieht aus, als fiele sie gleich in Ohnmacht. Dann würde sie bestimmt vornüber fallen und wieder alles durcheinanderbringen."


show yuukoshang panic_up onlayer master
with charachange

yu "Ich kann hier nicht mehr arbeiten."


"Was für ein schlechter Ort, um ihren logischen Gedankengang zu Ende zu bringen."


hi "Nein, komm schon. Diese Art der Einrichtung macht diesen Ort doch so besonders. Es gibt eine Menge Cafés in der Umgebung, weißt du. Ich finde es charmant, wirklich. Bitte hör nicht auf. Das Geschäft läuft doch gut, oder?"


show yuukoshang worried_up onlayer master
with charachange

yu "Nicht wirklich…"


hi "Hör mal, ich denke, das ist eine gute Arbeit für dich. Sie passt zu dir, du solltest nicht aufhören."


"Ich musste noch nie zuvor so eine Art von Krise lösen."


stop music fadeout 2.0




"Letztendlich schaffe ich es, sie zu beruhigen, und überzeuge sie davon, dass Shizune ganz bestimmt nur das will, was sie sonst hier bestellt."


hide yuukoshang onlayer master
with charaexit

show shizu basic_normal2 onlayer master at center
show bg suburb_shanghaiint onlayer master at bgleft
with charamove

show shizu basic_normal2 onlayer master:
    ypos 1.15
with charamove

"Als Yuuko geht, um uns unsere Getränke zu bringen, hat sich Shizune bereits einen Tisch ausgesucht."


play music music_dreamy fadein 4.0

"Da es keine anderen Kunden gibt und Yuuko nicht gerade zu den gesprächigsten Menschen gehört, ist es sehr still."


"Nicht, dass mich das stört, aber ich würde gern irgendwie mit ihr kommunizieren. Es gab bisher nur wenige Momente, in denen wir allein waren. Shizune und Misha sind fast immer zusammen – als wären sie eins."


"Nun sind wir nur zweit, aber ich kann sie weder verstehen noch mich verständlich machen. Es ist furchtbar."


hi "Hast du deinen kleinen Notizblock heute nicht dabei? Ich weiß ja, dass Wochenende ist und so, aber so unvorbereitet kenne ich dich gar nicht."



hi "Na ja, gut. Ich mag ihn eh nicht besonders. Trotzdem wäre er jetzt nützlich."


show shizu behind_blank onlayer master
with charachange

shi "…"

show shizu basic_normal onlayer master
with charachange

shi "… …"

"Shizune fängt an, in kurzen Schüben zu gestikulieren. Zwischendurch trinkt sie immer mal wieder einen Schluck Tee. Seltsam, dass sie nicht die geringsten Anstalten macht, ihr übliches Verhalten zu ändern."


"Ich rede die meiste Zeit mit ihr, da ich so eine langanhaltende Stille nicht gewöhnt bin."
"Einen Moment lang frage ich mich, ob es ihr ähnlich geht – irgendwie. Trotzdem unwahrscheinlich. Sie ist wohl mehr der Typ, der sich jedem gegenüber gleich verhält, ohne sich zu ändern."


hi "Hey, bestimmt ist Misha dem Schülerrat deinetwegen beigetreten. Damit wären wir schon zwei, weißt du. Ich bin nur dort, weil du mich dazu gezwungen hast."


hi "Na ja, nicht wirklich gezwungen, glaube ich. Ich bin deinetwegen beigetreten."


"Das klingt sogar etwas romantisch und ich spüre, wie ich ein wenig rot werde. Ich komme mir wie ein Idiot vor."



hi "Dafür weiß ich immer noch nicht, warum DU dort bist. Rückblickend hätte ich es gleich am Anfang fragen müssen, aber ich bin wirklich neugierig darauf. Ich muss daran denken, Misha irgendwann zu fragen."

show shizu behind_blank onlayer master
with charachange

shi "…"

hi "Schön, mit dir zu reden, auch wenn du mich nicht verstehen kannst. Ich würde gern wissen, ob es bei dir genauso ist."


hi "Das wäre wirklich… großartig."


show shizu adjust_happy onlayer master
with charachange

shi "…"

hi "So natürlich wie bei Misha wird die Gebärdensprache bei mir wohl nie aussehen, aber es ist doch schon ein Fortschritt, wenn man von Stift und Papier wegkommt, stimmt's?"


show shizu basic_normal2 onlayer master
with charachange

shi "…"

stop music fadeout 4.0

"Wir sind schon seit einer Weile mit unseren Getränken fertig, als Shizunes Blick auf das Paket fällt, das neben mir auf einem eigenen Stuhl thront."


show shizu adjust_happy onlayer master
with charachange

shi "…"

hi "Ich habe es nur für jemanden abgeholt, es gehört mir nicht."


play music music_running fadein 0.5

show shizu basic_sparkle onlayer master
with charachange

"Shizune zieht es sich näher heran, und als sie Anstalten macht, es zu öffnen, rutscht mir fast das Herz in die Hose. Ich versuche hastig, das Paket wiederzubekommen, indem ich ein Bein um den Stuhl wickle."


hi "Verdammt, nicht öffnen. Du kannst nicht einfach so die Post anderer Leute aufmachen, das ist gegen das Gesetz."


show shizu basic_frown onlayer master
with charachange

shi "…"

hi "Nein!"


show shizu cross_angry onlayer master
with charachange

shi "…!"

"Einmal in Fahrt ist sie kaum noch zu bremsen. Ihr begeisterter Blick spricht Bände – sie sieht aus, als ob sie mit mir um dieses blöde Paket kämpfen würde. Das könnte ganz schnell in einem Tauziehen enden."


show shizu behind_frown onlayer master
with charachange

"Mittlerweile bin ich fast aufgestanden und rudere mit meinen Armen wie ein Fluglotse, bevor sie endlich zur Ruhe kommt."


show shizu behind_frown onlayer master at center
with charamove

"Shizune zieht einen Schmollmund, da ihre Neugier nicht befriedigt wurde, und macht Anstalten zu gehen."


"Es wird wohl langsam Zeit. Wir sind eine ganze Weile hier gewesen. Ehe ich selbst aufstehe, nehme ich die Kiste schützend an mich."


show shizu basic_happy onlayer master
with charachange

"Auf einmal legt Shizune aufgeregt ihre Fingerspitzen aneinander, holt einen Filzstift aus ihrer Tasche und fängt an, auf Kenjis Paket zu schreiben."


hi "Hey, was machst du? Ich habe doch gesagt, es gehört mir nicht!"


hi "Hey!"


"Ich kann sie nicht einmal sehen, weil das Paket meine Sicht blockiert."


hi "Schön, dann lass es mich wenigstens absetzen."


"Ich muss es ohnehin lesen, was auch immer sie schreibt."


window hide

$ written_note("Ich helfe dir beim Tragen.", {"background":Frame("vfx/cardboard.jpg",0,0, tile=True)})


show shizu adjust_smug onlayer master
with charachange

window show

"Sieht dennoch nicht so aus, als sei sie fertig, und Shizune zeichnet eine stürmische Linie, um den Haken an der Sache anzuzeigen."


window hide

$ written_note("Ich helfe dir beim Tragen.\n ___________________\n\nAber – es ist ein Spiel! Es verliert der Erste, der stolpert. Und der Verlierer muss es den restlichen Weg selbst tragen.", {"background":Frame("vfx/cardboard.jpg",0,0, tile=True)})


window show

hi "Das ist albern. Zu fünfzig Prozent muss ich es am Ende so oder so selbst tragen."


"In Wahrheit bin ich hier gerade der Alberne. Ich habe vergessen, dass sie mich nicht hören kann. Ich höre auf zu sprechen und schüttle den Kopf."


show shizu behind_blank onlayer master
with charachange

shi "…"

show shizu cross_angry onlayer master
with charachange

shi "…!"

show shizu adjust_angry onlayer master
with charachange

shi "…!"

"Ich kann sie absolut nicht verstehen, aber sie kommt sehr energisch auf mich zu. Sie denkt eindeutig, dass es eine Spitzenidee ist."


"Also, wenn sie das Paket fallen lässt oder so, muss sie es tragen. Das würde mir die Sache natürlich viel einfacher machen."


"Die Chance liegt bei 50-50, dann… ist sie wahrscheinlich höher als bei jedem ihrer anderen Pläne. In Ordnung, ich mach's."


show shizu basic_normal_close onlayer master
with characlose

"Wenn ich darüber nachdenke, bin ich mir nicht sicher, wie wir das anstellen sollen. Dann greift sich Shizune das eine Ende der Kiste und hebt es an, bevor ich die andere Seite packe. Ist das überhaupt richtig? So zu laufen ist recht unbequem."


show bg suburb_shanghaiext onlayer master
with locationchange

"Wir verlassen das Café, und ich hoffe insgeheim, dass die Straßen immer noch menschenleer sind. Yuuko schien über unser Treiben verwirrt zu sein. Ich kann mir vorstellen, dass es mit mehr Zuschauern nur noch schlimmer wäre."


show shizu adjust_happy_close onlayer master
with charachange

show shizu basic_normal_close onlayer master
with charachange

"Shizune scheint es dagegen gar nichts auszumachen, mit diesem unnatürlich angewinkelten Arm zu laufen. Sie grinst siegessicher und macht ab und zu einige bizarre Gesten."


show bg suburb_roadcenter onlayer master
with locationchange

"Mit der Zeit kommen Leute vorbei, die uns anstarren, und die allmorgendliche Menschenmenge beginnt, die Straßen zu füllen."


"Ich fühle mich zwar blöd dabei, aber wenn ich es jetzt aufgebe, wird Shizune es mit Sicherheit als Kapitulation werten. Das kann ich nicht zulassen, wo ich mich doch bisher ganz gut geschlagen habe."


show shizu adjust_happy_close onlayer master
with charachange

show shizu basic_normal_close onlayer master
with charachange

"Am Anfang habe ich Shizunes zaghafte Handzeichen als ihre vorweggenommene Schadenfreude abgetan, doch ich merke schnell, dass sie mir in Wahrheit den Weg signalisiert, den sie gehen will."


"Mir dämmert, dass das hier kein Wettkampf ist. Das Ganze hat viel weniger von einer Herausforderung als von einer Übung in Teamarbeit. Nur, dass Shizune eine Strafe fürs Scheitern statt einer Belohnung für gute Arbeit ausgesprochen hat."


stop music fadeout 3.0

show shizu adjust_blush_close onlayer master
with charachange

"Unsere Finger berühren sich unter dem Paket, und Shizune zieht ihre Hand weg, wobei sie beinahe ihre Pakethälfte fallen lässt."


"Und damit heißt es für sie: Game Over."


"Besonders glücklich wirkt sie nicht. Denkt sie, ich hätte das getan, um sie absichtlich verlieren lassen? Wenn es so ist, macht sie daraus keine große Sache. In der Liebe und im Krieg ist alles erlaubt."


show shizu basic_frown onlayer master
with charadistant

"Ich sollte es ihr besser abnehmen und selbst tragen, aber als ich es versuche, schubst sie mich weg."


play music music_shizune fadein 1.0

"Sie starrt mich zornig an, als wolle sie mit mir schimpfen. Kann sie aber nicht. Mit dem Paket in den Händen ist sie im Grunde genommen geknebelt."


show shizu basic_normal2 onlayer master
with charachange

show shizu basic_normal onlayer master
with charachange

"Vielleicht hat sie das auch gemerkt, denn für einen kurzen Moment huscht ein trauriger Ausdruck über ihr Gesicht, als müsse sie einsehen, dass sie doch mit Einschränkungen fertigwerden muss."


"Allerdings ist sie immer noch genauso stolz wie immer, selbst wenn es zu ihrem Nachteil ist. Sie würde es nicht wollen, wenn ich ihr die Wettschulden erlasse."


"Während des Spiels ist alles erlaubt, aber das Resultat muss akzeptiert werden: Wettschulden sind Ehrenschulden."


"Shizune ist wirklich ein interessanter Mensch."


show bg school_dormext_full onlayer master
with shorttimeskip

"Der Marsch zurück zur Schule verlief ohne Vorkommnisse. Shizune hat die Kiste immer mal wieder wie einen riesigen Zauberwürfel gedreht. Es kommt mir vor, als hätte sie ein weiteres Spiel erfunden, um sich zu amüsieren."


"Für den Inhalt kann das nicht gut sein, aber ich mache mir nicht viel daraus, sie daran zu hindern."


"Möglich, dass sie auf diese Art ihren Alltag bewältigt, indem sie aus allem ein Spiel macht. Auch wenn ich das nicht mit Sicherheit sagen kann."


"Ich glaube, es macht einfach keinen Sinn, Shizune einer Psychoanalyse zu unterziehen. In der kurzen Zeit, in der wir uns kennen, wurde ich schon ziemlich oft überrascht."


show shizu basic_normal2 onlayer master at centertremble_nl
with None

stop music fadeout 6.0

"Shizune zittert. Der Wind ist aufgefrischt und die Schule ziemlich hoch gelegen. Klar, dass ihr kalt ist. Wenn ich ihr meine Jacke gebe, würde sie nicht trotzdem ablehnen?"


play sound sfx_rustling

show shizu basic_normal2_close onlayer master at center
with characlose

"Ich ziehe meine Jacke aus und lege sie ihr über die Schultern, bevor sie protestieren kann. Ihre Schultern sind so schmal und zierlich, dass ich meine Hände länger darauflegen möchte."


show shizu adjust_blush_close onlayer master
with Dissolve(0.2)

"Logischerweise zuckt Shizune überrascht zusammen, als meine Finger sie streifen."


hi "Verzeihung."


show shizu basic_normal_close onlayer master
with charachange

shi "…"

show shizu adjust_happy_close onlayer master
with charachange

shi "…"

"Ihre Finger tänzeln über der Schachteloberfläche. Ich spiele mit dem Gedanken, sie ihr wegzunehmen, aber das würde sie kaum zulassen."
"Shizune macht mit ihren Händen eine schnelle Geste, so gut es gerade geht. Dann macht sie eine kleine Pause, als wolle sie noch mehr sagen."


"Ich bin mir sicher, dass das „Danke” bedeutet. Ich freue mich, dass ich es verstehen konnte."


scene black onlayer master
with dissolve

$ suppress_window_after_timeskip = True



label de_S11:

window hide None

scene bg school_cafeteria onlayer master
with locationchange

nvl clear

nvl show dissolve

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_normal fadein 0.5

n "\n\nDer Lehrer für Gebärdensprache meint, ich sei recht gut."


n "Ich versuche, nicht so sehr daran zu denken, aber ich habe mich so stark in die Sache vertieft, dass es mir schwer fällt, nicht ein paar Mal am Tag darauf zurückzukommen. Ich nehme an, ich begreife es schneller als erwartet, aber es reicht noch nicht."


n "Es ist auch leicht zu verstehen. Gut, beim Lesen der Gesten muss ich meine Gedanken zusammennehmen, aber das Ausführen ist einfach genug."


n "Das Gestikulieren an sich ist machbar, nur brauche ich noch ein wenig mehr Übung. Aber gleichzeitig verstehen und gebärden? Auch nur halb so schnell wie Misha? Unmöglich."


n "Gemessen an meinem Level ist mein jetziger Stand gut, aber um wirklich mit Shizune kommunizieren zu können, muss ich noch mehr daran arbeiten."


n "\nIch gebe mein Bestes, Schritt für Schritt zu lernen, indem ich während des Mittagessens so viel Wissen wie möglich in mich hineinstopfe."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear

nvl hide dissolve

window show

"Ich schaue auf, während ich „Einführung in die japanische Gebärdensprache” lese, ob Shizune oder Misha in der Nähe sind."


"Da ich meine Stunde Mittagspause opfere, bin ich ihnen natürlich seit ein paar Tagen aus dem Weg gegangen. So soll es auch bleiben, wenn ich nicht will, dass Shizune davon erfährt."


"Wie ich so mit dem Rücken zur Ecke alle zehn Minuten den Raum absuche, fühle ich mich wie ein Verbrecher, der seiner Verhaftung entgehen will."


"…"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

nvl show dissolve

nvl clear

n "\n\nBei jeder Gelegenheit fragt mich Misha, warum Shizune nichts von meinem Kurs in Gebärdensprache wissen soll."


n "Rückblickend gab es tatsächlich keinen besonderen Grund, aber ich glaube, ich weiß jetzt warum."


n "Wenn ich will, dass Shizune mich als Gleichgestellten sieht, dann ist Gebärdensprache ein wichtiger Schritt in diese Richtung."


n "Ein weiterer wichtiger Schritt ist, dass sie nichts davon weiß, bis wir endlich unter den gleichen Bedingungen sprechen können und ich es auch sicher beherrsche – nicht wie ein irgendein Stümper."


n "Alles andere wäre eine Beleidigung, finde ich. Sie würde es genauso sehen."


n "\nFür mich ist das die einzige Option. Besonders jetzt, wo ich mich entschieden habe, es voll durchzuziehen."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear

nvl hide dissolve

window show

"Shizunes Ausstrahlung ist gewaltig. Es ist wirklich leicht, sie kommen zu sehen oder auf andere Art zu spüren."
"Höchstwahrscheinlich deshalb, weil Mishas Haare in einer Menschenmenge wie ein Leuchtfeuer aufblitzen. Und man hört ihr Lachen auf einem Kilometer Entfernung."


"Obwohl es das Gleiche wäre, wenn Misha sie nicht begleitet. Sie ist im Kern sehr geradlinig und effizient, da überrascht es nicht, dass sich das auf ihre Gangart abfärbt."


"Dadurch kann ich meine Unterlagen wegräumen und meine beste Unschuldsmiene aufsetzen, lange bevor sie mich sehen und auf mich zukommen."


show shizu behind_smile onlayer master at tworight
show misha perky_smile onlayer master at twoleft
with charaenter

hi "Hi."

show shizu adjust_smug onlayer master
with charachange

ssh "Schülerrat."


show misha hips_grin onlayer master
with charachange

mi "Schülerrat~!"


"„Schülerrat” war das Erste, was ich lernen wollte; ich dachte, es wäre später bestimmt nützlich."


hi "Ja, hab mich in letzter Zeit davor gedrückt, was?"


show misha sign_smile onlayer master
show shizu behind_smile onlayer master
with charachange

mi "Jepp~!"


show shizu behind_smile_close onlayer master at closeright
show misha perky_smile_close onlayer master at closeleft
with characlose

show shizu behind_smile_close onlayer master:
    ypos 1.07
show misha perky_smile_close onlayer master:
    ypos 1.1
with charamove

stop music fadeout 3.0

"Shizune setzt sich rechts vor mir und Misha links. Es war wohl ein Fehler, mich in die Ecke zu setzen. Jetzt haben sie mich in die Enge getrieben."


scene bg school_lobby onlayer master
with shorttimeskip

"Am Ende wurde ich ins Büro des Schülerrats geschleppt. Na ja, egal. Ich habe sogar schon angefangen, die beiden ein bisschen zu vermissen."


"Es macht die Sache auf die eine oder andere Art auch einfacher: Zufrieden mit ihrem Fang fragt sie gar nicht, wo ich die ganze Zeit gewesen bin."


"Vor der Tür stehend frage ich mich aber, was so wichtig sein könnte, dass sie mich so verbissen zurückbringen wollten."


scene bg school_council onlayer master at bgright
with locationchange

hi "Spiele."


play music music_another fadein 0.5

"Es sind mehr Spiele draußen als Bücher."
"Das erklärt zumindest, warum bei jedem meiner Besuche auf jedem Tisch und zeitweise auch auf dem Fußboden Bücherstapel aufgeschichtet sind: Sie brauchen diesen Raum, um all diese Spiele irgendwo unterzubringen."


show misha cross_laugh onlayer master
with charaenter

mi "Hahaha~!"

show misha hips_grin onlayer master
with charachange

mi "Es ist langweilig, immer nur gegeneinander zu spielen, Hicchan. So, nun bist du am Zug, okay? Okay~! Also abgemacht~!"


hi "Ich hab doch noch gar nichts gesagt!"


show shizu invis behind misha at right onlayer master
with None

show misha hips_grin onlayer master at twoleft
show bg school_council onlayer master at center
show shizu basic_normal onlayer master at tworight
with dissolvecharamove

show shizu behind_blank onlayer master
with charachange

shi "…"

show misha sign_smile onlayer master
with charachange

mi "Hicchan, das ist einer der letzten Tage, an dem wir es so locker angehen lassen können. Darum~ ist es besonders wichtig, dass wir das Beste draus machen, denkst du nicht auch?"


show misha cross_smile onlayer master
with charachange

mi "Außerdem ist bald Tanabata, da haben wir noch eine Menge Arbeit vor uns."


show misha hips_grin onlayer master
show shizu behind_smile onlayer master
with charachange

mi "Also spiel erst mal mit uns~!"


"Stimmt schon, wenn ich so darüber nachdenke. Ich habe es nicht einmal bemerkt, weil ich so stark auf das Studium der Gebärdensprache konzentriert war. Nach jedem Fest kommt ein noch Größeres."


"Ich würde gern wissen, ob Shizune wieder versuchen wird, ein paar neue Mitglieder zur Unterstützung zu gewinnen."


hi "Du hast recht."


show misha cross_laugh onlayer master
with charachange

mi "Hahaha~! Wuhu~! Hicchan stimmt zu~! Das wird gefeiert!"


show shizu basic_happy onlayer master
with charachange

ssh "Ich weiß, wir sollten spielen."


show misha sign_smile onlayer master
with charachange

mi "Spielen wir, um das zu feiern, Hicchan~!"


hi "Ich weiß nicht recht, so was nimmt immer ein übles Ende für mich."


show misha perky_sad onlayer master
with charachange

mi "Hicchan hat Angst wegen der Wetteinsätze~."


"Misha macht ein sehr enttäuschtes Gesicht. Schwer zu sagen, ob sie mich aufzieht, da ihre Mimik von Natur aus so übermäßig ausgeprägt ist. Ein Mädchen, das stets aufs Ganze geht."


"Ich drehe mich zu Shizune um. Gut, dieses Mädchen macht sich definitiv über mich lustig."


hi "Hey, lasst das. Ja, ich mache mit, aber nur wenn ihr mir sagt, was auf dem Spiel steht."


show shizu adjust_smug onlayer master
with charachange

shi "…"

show misha cross_grin onlayer master
with charachange

mi "Typisch Japaner, hebt die Folgen über alles andere."


show misha sign_smile onlayer master
with charachange

mi "Hicchan, hast du je von der Redewendung „den Wald vor lauter Bäumen nicht sehen” gehört?"


hi "Nein."


"Eine Lüge. Aber ich habe meinen Stolz, und der ist im Moment ziemlich verletzt."


hi "Okay, ich mache mit, aber das Spiel will ich aussuchen."


show shizu adjust_happy onlayer master
show misha perky_smile onlayer master
with charachange

"Misha nickt."


hi "Zusätzlich denke ich mir die Strafe aus, wenn ihr verliert."


show shizu cross_angry onlayer master
with charachange

"Shizune formt ein X mit ihren Armen. Entweder bedeutet das „abgelehnt” oder sie bereitet ihren Spezialangriff vor."


hi "Aha, wer hat jetzt Angst vor den Folgen?"


show shizu behind_frown onlayer master
with charachange

ssh "Er denkt nur an Rache. Dass er wegen dieses kleinen Witzes immer noch auf so gehässige Gedanken kommt…"


show shizu basic_frown onlayer master
with charachange

ssh "Wenn dich ein … beißen würde, würdest du bestimmt zurückbeißen."


"Shizune beschreibt ein Wort, das ich nicht deuten kann."


show misha hips_frown onlayer master
with charachange

mi "Hicchan denkt nur an Rache~, obwohl es bloß ein kleiner Witz war. Wenn dich ein Gürteltier beißen würde, würdest du bestimmt zurückbeißen!"


hi "Gürteltier?"


show misha sign_smile onlayer master
with charachange

mi "Es wäre unklug, ein Gürteltier zurückzubeißen, Hicchan!"


show shizu behind_blank onlayer master
with charachange

shi "…"

show misha cross_laugh onlayer master
with charachange

mi "Aber Hicchan würde es natürlich trotzdem machen~! Hahaha!"


hi "Natürlich."


show shizu adjust_smug onlayer master
with charachange

"Shizune rückt mit einem kurzen Schwung ihrer Hand ihre Brille zurecht."


show shizu behind_smile onlayer master
with charachange

shi "…"

show misha sign_smile onlayer master
with charachange

mi "Hicchan, wir hatten überhaupt nichts geplant, falls du gewinnst oder verlierst. Du warst derjenige, der so was vermutet hat~."


hi "Warum wohl?"


show misha hips_grin onlayer master
with charachange

mi "Hm~, ich auch~! Aber na ja~! Da ist nix. Stimmt dich das um, Hicchan?"


hi "Also… ja."


show misha hips_laugh onlayer master
with charachange

"Mit Hochgeschwindigkeit lässt Misha ihre Arme wie eine Windmühle kreiseln. Komische Angewohnheit. So etwas kann man nur im Büro des Schülerrats erleben, und das bei gerade mal drei Leuten."


"Irgendwo anders würde sie damit wohl das eine oder andere Gesicht verletzen."


show misha hips_grin onlayer master
with charachange

mi "Wuhu juhu~! Und los geht's~!"


hi "Noch nicht."


show misha hips_smile onlayer master
with charachange

mi "…"

show shizu behind_blank onlayer master
with charachange

shi "…"

mi "…"

shi "…"

hi "Okay, okay."

hi "Jedenfalls muss jeder von uns spielen können. Das ist meine Bedingung."


hi "Ich mag keine Spiele, bei denen eine Person als absoluter Vollprofi dominiert oder nur zwei von uns spielen dürfen, während einer zuschaut. Wir sollten es alle gleich gut spielen können."


show shizu basic_normal onlayer master
with charachange

shi "…"

show misha sign_smile onlayer master
with charachange

mi "Dame?"


"Im gleichen Augenblick, in dem sie das sagt, zaubert sie ein Damespiel hervor und platziert es auf dem Tisch."


hi "Das können bloß zwei Leute spielen. Ich habe gesagt…"


show misha hips_grin onlayer master
with charachange

mi "Okay okay~! Hicchan, wie sieht's aus mit… Monopoly?"


"Eine Monopoly-Schachtel wird langsam aber bestimmt in meine Richtung geschoben. Ich nehme sie Misha aus den Händen und lege sie unter meinen Stuhl."


hi "Ich mag keine Spiele, die nur vom Losglück abhängen. Glück hat nichts mit Können zu tun. Solche Spiele brauchst du gar nicht erst vorzuschlagen!"


show misha perky_confused onlayer master
with charachange

mi "Glück ist auch eine Art Können, weißt du."


hi "Nein, ist es nicht!"


show shizu adjust_smug onlayer master
with charachange

shi "…"

show misha sign_smile onlayer master
with charachange

mi "Doch, wenn man durchgehend Glück hat~! Stimmt's~?"


hi "Das hat überhaupt nichts miteinander zu tun."


show shizu adjust_happy onlayer master
show misha hips_grin onlayer master
with charachange

mi "Hm~, hm~ hm~ hm~~. Bakkarat? Murmeln? Spiel des Lebens? Das Leiterspiel? Roulette? Blackjack? Paper Football? Trivial Pursuit?"


"Misha fängt begeistert an, eine Fülle an Spielen aufzuzählen, als ob sie von einer Liste ablesen würde."


"Mit jedem Vorschlag füllt sich ihr Platz mit neuen Schachteln, Spielbrettern und Figuren."
"Es ist eine bizarre Spielesammlung von Kinder- bis Erwachsenenspielen, darunter auf Hochglanz polierte Glücksspielutensilien, die in dieser Abstellkammer völlig fehl am Platze wirken."


show misha sign_smile onlayer master
with charachange

mi "Dreier-Schach?"


hi "Geht das überhaupt?"


show shizu behind_smile onlayer master
with charachange

ssh "Versuchen wir es."


show misha cross_laugh onlayer master
with charachange

mi "Ja, ja~, versuchen wir's, auf jeden Fall~! Ahahahaha~!"


show shizu basic_happy onlayer master
show misha hips_grin onlayer master
with charachange

"Mit einer ausladenden Geste ziehen sie hinter sich ein Schachbrett hervor – wie zwei Nachwuchszauberer. Nun, für Zaubertricks braucht man sehr geschickte Hände, und die haben sie ja im Übermaß."


"Nicht, dass ich überrascht wäre. Irgendwie beunruhigend ist es trotzdem."


hi "Lasst das!"


stop music fadeout 2.0

ha "E-Entschuldigung…?"


show shizu basic_normal onlayer master
show misha perky_confused onlayer master
with charachange

"Eine sehr zaghaft klingende Stimme lässt mich aufblicken."


show hanako invis onlayer master at offscreenright
with None

show misha perky_confused onlayer master at left
show shizu basic_normal onlayer master at center
show bg school_council onlayer master at bgleft
show hanako emb_downtimid onlayer master:
    xanchor 0.7 xpos 1.0
with dissolvecharamove

ha "Ich ha-habe meinen Schülerausweis verloren, und ich habe gehört, dass… man hier erfahren kann, woher man einen neuen bekommt. Wenn ich störe, d-dann kann ich später wiederkommen."


show hanako emb_timid onlayer master
with charachange

"Hanakos Blick fällt auf eine Landschaft aus aufgestapelten Berichtsheften, sporadisch hingestellten Stühlen und umgekippten Brettspieltürmen."


"Ich schätze mal, der Schülerrat gibt momentan nicht gerade das straff organisierte Bild ab, das er nach außen hin zeigen sollte."


hi "Hallo."


"Das ist das Einzige, was mir einfällt, um das Eis zu brechen. Leider scheint sie jetzt noch verschreckter zu sein."


show hanako def_worry onlayer master
with charachange

ha "…"

show hanako def_strain onlayer master
with charachange

ha "Ah…{w=0.5} mein Schülerausweis…{w=0.5} Ich…"


show misha sign_smile onlayer master
with charachange

mi "Du bist doch in unserer Klasse, oder? Stimmt's? Stimmt~! Also~! Sei nicht so ängstlich, okay? Komm schon!"


show shizu behind_smile onlayer master
with charachange

shi "…"

show misha hips_grin onlayer master
with charachange

mi "Jepp, auch wenn wir älter sind als du, wir beißen nicht!"


hi "Wir sind nicht älter, sondern in der gleichen Klasse."


play music music_happiness fadein 3.0

"Dennoch bin ich ihnen dankbar, dass sie sich eingeschaltet haben."


show misha hips_smile onlayer master
with charachange

mi "Was wolltest du gleich noch mal? Einen Ausweis, stimmt's~? Stimmt~!"


show hanako basic_distant onlayer master
with charachange

ha "Ja."


"Ihre Augen gleiten an Misha vorbei. Zaghaft wie sie ist, fällt es ihr schwer, Augenkontakt zu halten. Ihr umherschweifender Blick bleibt am Schachbrett auf dem Tisch hängen."


show hanako basic_normal onlayer master
with charachange

show hanako basic_distant onlayer master
with charachange

"Für einen kurzen Moment weiten sich Hanakos Augen. Shizune bemerkt es ebenfalls."


show shizu basic_happy onlayer master
with charachange

shi "…"

show misha perky_smile onlayer master
with charachange

mi "Magst du Schach?"


show hanako defarms_strain onlayer master
with charachange

ha "Eh!?"


show shizu adjust_smug onlayer master
with charachange

shi "…!"

show misha hips_smile onlayer master
with charachange

mi "Du magst Schach, was~? Ja klar, eindeutig~!"


show misha hips_grin onlayer master
show shizu adjust_happy onlayer master
with charachange

mi "Willst~{w=0.2} du~{w=0.2} mit~{w=0.2} uns~{w=0.2} spielen~?"


"Zögern. Ob sie lieber die Flucht ergreifen will? Ich will mich nicht einmischen, das würde kein gutes Ende nehmen."


show hanako basic_normal onlayer master
with charachange

"Zu meiner Überraschung nimmt Hanako den Vorschlag anscheinend sehr ernst. Sie drückt ihre Finger nachdenklich zusammen, während sie darüber grübelt."


"Eine so lange Überlegung kommt einer Bestätigung gleich."


show misha sign_smile onlayer master
with charachange

mi "Wir machen Mittagspause, also musst du eh warten. Warum spielst du dann nicht solange mit uns~? Gib dir 'nen Ruck, das macht Spaß, wirklich~! Du magst Schach, richtig? Sag ich doch, ganz bestimmt, das sieht man, also~! Bitte~, machst du's?"


show hanako cover_distant onlayer master
with charachange

ha "Okay…"

show misha cross_laugh onlayer master
with charachange

mi "Wahaha~! Juhu~! Geschafft, geschafft, okay okay okay~! Das ist toll~!"


scene ev shizu_chess_large onlayer master:
    subpixel True xanchor 1140 yanchor 1100 xpos 400 ypos 300 zoom 1.0
    easein 10.0 yanchor 1050
with flash



"Das Schachbrett ist vorbereitet."


"Der Eröffnungszug ist wichtig."


show ev shizu_chess_large onlayer master:
    ease 1.0 xpos 400 xanchor 1400 yanchor 400 ypos 300
    acdc_warp 10.0 xanchor 1300

"Shizune scheint es allerdings nicht zu kümmern."


show ev shizu_chess_large onlayer master:
    ease 0.5 xanchor 800 yanchor 360
    easein 10.0 xanchor 700 yanchor 360

"Hanako wägt ihre Züge vorsichtig ab, verschiebt ihre Figuren ein kleines Stückchen, zieht sie dann wieder verunsichert zurück, zweifelt immer wieder an sich selbst."


"Sie beherrscht Schach wirklich gut, eine Gelegenheitsspielerin ist sie jedenfalls nicht. Auf jeden Fall ist sie mit Leidenschaft dabei."


"Shizune kann sie nicht auf die leichte Schulter nehmen. Egal was sie tut, Hanako hat eine passende Antwort."


"Trotzdem stimmt irgendwas mit dem Spielverlauf nicht."


scene ev shizu_chess_base onlayer master:
    truecenter subpixel True zoom 1.05
    easein 5.0 zoom 1.0
with flash

"Shizune macht ihre Züge zu schnell."
"Nein, nicht wirklich, aber mit unlogischer Geschwindigkeit. Es ist, als ob sie gar nicht darüber nachdenkt, was sie als nächstes tut. Entweder spielt Shizune auf dem Niveau eines Supercomputers, oder sie nimmt das Ganze nicht allzu ernst."


"Vielleicht ist Hanako aber auch einfach nicht besonders gut."


scene ev shizu_chess_base onlayer master
show sc_shiz normal onlayer master:
    xalign 1.0 yalign 0.0
with charachange

"Shizune erzwingt einen Austausch der Schachfiguren."


scene ev shizu_chess_base3 onlayer master
with charachange

"Hanako benötigt mit fortschreitender Spieldauer immer mehr Zeit, obwohl es noch gar nicht so lange läuft. Plötzlich wird alles klar: Shizune hat viel mehr Zeit, um ihren nächsten Zug zu planen, weil Hanako stundenlang braucht, ehe sie sich bewegt."


"Trotzdem ist es ein interessantes Spiel."


window hide

nvl clear

$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl show dissolve

n "\n\nSchwarzer Springer auf F6."


n "Läufer auf D3."


n "Anscheinend nehmen beide das Spiel ernst. Vielleicht kommt dieser Eindruck auch daher, dass sie sich so wie es aussieht nicht sehr nahe stehen. Zumindest bis jetzt scheint auch keine von ihnen stärker zu spielen als die andere."


n "Shizune ist für Hanako eine mysteriöse Gegnerin, und Hanako ist für Shizune ein Rätsel. Hanako zeigt mit ihrer gerunzelten Stirn, wie sehr sie sich reinhängt. Sie will wirklich gewinnen, und Shizune sowieso."


n "Dass sie kaum miteinander vertraut sind, ist etwas deprimierend, bringt aber Leben ins Spiel und ermöglicht es beiden, die andere als große Herausforderung zu betrachten."


n "Vielleicht könnten sie auch darüber hinaus Freundinnen werden, oder wenigstens Schach-Rivalen. Ein optimistischer Gedanke."


n "Obwohl sie ja, wenn ich an das Risiko-Spiel gegen Shizune denke, nicht der Mensch ist, der andere zum Spaß vernichten will."


nvl clear

n "\n\n\nDas Spiel geht weiter."


n "Shizune macht zwölf Züge in vier Minuten. Eine furchterregende Gegnerin."


n "Doch Hanako behauptet sich gut, auch wenn ihr König etwas umzingelt ist."


n "Bauer auf H6."


n "Weißer Springer auf E6."


n "Das Ende ist nah."


n "\n\n…"

stop music fadeout 3.0

n "Das Spiel ist aus."


nvl clear

nvl hide dissolve

scene bg school_council onlayer master
show shizu adjust_happy onlayer master at center
show misha perky_smile onlayer master at left
show hanako basic_normal onlayer master at right
with locationchange

window show

shi "…"

show misha sign_smile onlayer master
with charachange

mi "Das war wirklich ein schönes Spiel~!"


$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_ease fadein 5.0

show hanako cover_bashful onlayer master
with charachange

ha "D-Danke…"


show shizu behind_smile onlayer master
with charachange

shi "…"

show misha hips_smile onlayer master
with charachange

mi "Es war echt knapp~, ich dachte, ich würde verlieren. Du bist sehr talentiert."


"Bescheidenheit im Zeichen des Sieges und eine ausgestreckte Hand für den Besiegten. Vielleicht, weil Hanako ihre Niederlage so gut wegsteckt."


show shizu basic_normal onlayer master
with charachange

shi "…"

show misha perky_smile onlayer master
with charachange

mi "Das Spiel macht Spaß, aber es hat so lang gedauert. Fast die gesamte Stunde!"


mi "Schach ist zu formelhaft, besonders auf diesem Niveau. Was haltet ihr von ein paar verbesserten Regeln~?"


hi "Was?"


show hanako cover_worry onlayer master
with charachange

ha "Ver… bessert…?"


show shizu basic_sparkle onlayer master
with charachange

show shizu adjust_smug onlayer master
with charachange

show shizu basic_happy onlayer master
with charachange

shi "… … …"

show misha hips_smile onlayer master
with charachange

mi "Ja, ja~! Wie Tempo-Schach oder Schach mit zusätzlichen Figuren."
mi "Wir könnten auch Paare bilden und Doppelteam-Schach spielen, mit ein oder zwei Brettern, ganz nach Laune! Los los los los das wird lustig, ganz, ganz sicher~! Normales Schach ist zu langsam, methodisch und langweilig."


show misha hips_grin onlayer master
with charachange

mi "Ich will ein Schach spielen, das schnelles Denken und Mut belohnt! Eins von denen. Schach mit so etwas zu vergleichen ist wie Dame mit Go oder Tic Tac Toe mit Shogi zu vergleichen, stimmt's? Stimmt~!"


show misha cross_laugh onlayer master
with charachange

mi "Wahahaha~! Selbst Laser-Schach wäre spannender. Wählt etwas, wählt~!"


show hanako defarms_strain onlayer master
with charachange

ha "Aaaah…"

"Wie ein Kaninchen vor der Schlange. Man sieht, wie Hanakos Gedanken kreisen, als ob sie gleich in Ohnmacht fallen würde, was verschiedene Gefühle in mir auslöst."
"Vorrangig finde ich es lustig, aber ich rücke lieber etwas näher, falls sie wirklich umkippt."


scene ev shizu_chess_base2 onlayer master:
    truecenter subpixel True zoom 1.05
    easein 5.0 zoom 1.0
with flash

"Das Spielbrett ist wieder bereit, mit dem Unterschied, dass es diesmal nicht einmal knapp ausgeht."


"Hanako kann nicht einen Zug machen, aus Angst, mit Shizunes Hand zusammenzustoßen. Ihre Bewegungen umfassen das gesamte Spielfeld. Der reinste Ansturm. Überall, wo Hanako eine Figur hinstellen will, ist Shizune schon da."


"Das ist das schnellste Spiel, das ich je in meinem Leben gesehen habe."


scene bg school_council onlayer master
show shizu basic_sparkle onlayer master at center
show misha hips_grin onlayer master at left
show hanako defarms_strain onlayer master at right
with locationchange

mi "Ändern wir die Regeln und spielen noch mal~! Am besten so um die sechs mal, wie bei Kasparov und Deep Blue~!"


hide hanako onlayer master
with easeoutright

"Hanako entschuldigt sich und flieht aus dem Zimmer."


show shizu basic_normal onlayer master
show misha perky_confused onlayer master
with dissolve

mi "Häh? Warte!"


hide misha onlayer master
with charaexit

mi "Ah, wollte sie nicht wissen, woher sie einen neuen Ausweis bekommt? Entschuldige! Hallo~? Komm zurück, bitte! Halt, halt~! Halt~!"


stop music fadeout 3.0

"Komisch, je weiter Misha sich fortbewegt, desto lauter scheint der Klang ihrer Stimme zu werden."


show bg school_council onlayer master at bgright
show shizu basic_normal onlayer master at tworight
with charamove

show misha perky_sad onlayer master at twoleft
with charaenter

mi "Ich konnte sie nicht einfangen~…"


show shizu adjust_happy onlayer master
with charachange

play music music_normal fadein 3.0

shi "…"

"Shizune klopft ihr beruhigend auf die Schulter."


hi "Schon gut."


show misha hips_smile onlayer master
with charachange

mi "Schon gut~!"


hi "Du bist ja recht gut gelaunt für jemanden, der einen Klaps auf die Schulter braucht."


show misha cross_laugh onlayer master
with charachange

mi "Ahahaha~!"

"…"

show shizu basic_normal2 onlayer master
with charachange

shi "…"

show misha sign_smile onlayer master
with charachange

mi "Hicchan, hasst du Spiele, für die man Glück braucht?"


"Eine Frage wie aus heiterem Himmel, aber anscheinend eine wichtige."


"Wenn nicht, warum würde Shizune mich beobachten und auf meine Reaktion warten? Selbst als ich in ihre Richtung starre, versucht sie, es zu verbergen, indem sie betont beiläufig eine Schachfigur zwischen ihren Fingern tanzen lässt."


show misha hips_grin onlayer master
with charachange

mi "Du hast doch mal gesagt, dass du keine Spiele magst, bei denen man Losglück braucht, nicht wahr, Hicchan?"


hi "Ja, aber dass man Glück braucht, muss nicht heißen, dass es in einem Spiel ausschließlich um Glück geht."
hi "Ich hasse Spiele nicht, nur weil Glück ein Bestandteil ist. Für die meisten Spiele braucht man ohnehin etwas Glück. Dadurch bleiben sie interessant."


hi "Ich schätze, dass ein Spiel langweilig wird, bei dem man von Beginn an genau weiß, wie weit man kommen kann. Dann ist es kein richtiges Spiel, oder? Immer der gleiche Trott."


hi "Ein Spiel, bei dem man wenig bis gar keine Kontrolle hat, ist nichts für mich."


show shizu behind_smile onlayer master
with charachange

ssh "Verstehe."


show shizu adjust_smug onlayer master
with charachange

shi "…"

show misha hips_smile onlayer master
with charachange

mi "Dieses Mädchen ist nicht besonders gut in Schach."


show shizu basic_normal onlayer master
with charachange

shi "…"

show misha sign_smile onlayer master
with charachange

mi "Schach ist ein formelhaftes Spiel. Also~! Es passt nicht zu ihr… An Hanako ist nichts Formelhaftes. Jemand, der so oberflächlich Schach spielt und immer nur bis zum nächsten Zug denkt, ist kein ernstzunehmender Schachspieler."


show misha perky_smile onlayer master
with charachange

mi "Jeder, der Schach so sehr liebt, dass seine Augen funkeln, wenn sie ein Schachbrett sehen, würde sich auch damit beschäftigen."


mi "Wenn man sich gelegentlich mit dem Spiel befasst, kann man lernen, selbst gegen Profis mindestens die nächsten zwei Züge vorherzusagen."


show misha hips_frown onlayer master
with charachange

mi "Warum weiß jemand, der das Spiel so liebt… mit so viel Leidenschaft… so wenig darüber? Weniger sogar als einer, der nur kurzzeitig Interesse dafür findet?"


"Shizune stellt die Figur in ihrer Hand ab. Ein Turm."


show shizu behind_frown onlayer master
with charachange

shi "…"

show misha hips_smile onlayer master
with charachange

mi "Ihre Empfindungen sind echt, aber die für das Spiel sind es nicht. Verstehst du, Hicchan~?"


show misha perky_smile onlayer master
with charachange

mi "Es gibt kein Glück im Schach~! Es ist sehr wichtig, das zu begreifen."
mi "Glück im Spiel ist eine gute Sache, da jeder eine Chance bekommt. Genug, um mitzuhalten, aber nicht so viel, dass Können bestraft wird. Ich finde Schach langweilig, weil es kein Spiel ist – eher eine Formelsammlung."


show misha sign_smile onlayer master
with charachange

mi "Hanako ist auch nicht der Typ, der so was lieben würde~."


show shizu adjust_angry onlayer master
with charachange

shi "…"

show misha cross_frown onlayer master
with charachange

mi "Wenn man etwas als wertvoll ansieht, kämpft man dafür. Sich anzustrengen ist ein Beweis deiner Wert… Wertschätzung? Zumindest denke ich das."
mi "Oder~! Man gibt sofort auf~! Weil es so kostbar ist, dass es dir den Verstand raubt. Das Erste ist stürmische Liebe, das Zweite ist sanfte."


show shizu basic_normal2 onlayer master
with charachange

shi "…"

show misha hips_smile onlayer master
with charachange

mi "Ich hab versucht, sie aus der Reserve zu locken, und ihren König gejagt. Ich war jedoch nicht erfolgreich, da sie an ihrem Muster festgehalten hat."


mi "Die kniffligsten Momente waren die, wo sie am schnellsten agierte. Daraus folgt, dass sie genau wusste, wie man sich in solchen Situationen verhält."


show misha sign_smile onlayer master
with charachange

mi "Das heißt, jemand hat es ihr beigebracht. Verstehst du, Hicchan~?"


hi "Nicht wirklich."


show shizu adjust_happy onlayer master
with charachange

shi "…"

show misha hips_grin onlayer master
with charachange

mi "Wer Schach so sehr liebt, jedoch nicht alles geben kann, dann deshalb, weil sie nicht das Spiel, sondern die Erinnerungen liebt, die damit verbunden sind. Es bedeutet ihr zu viel, um es als Mittel eines Wettbewerbs zu betrachten."


show shizu behind_blank onlayer master
with charachange

shi "…"

show misha perky_smile onlayer master
with charachange

mi "Deswegen kann man sich auf diesem Weg nicht anfreunden. Nicht ohne Worte."


stop music fadeout 5.0

"Nun, deine Art, Freunde zu gewinnen, kommt nicht bei jedem an, Shizune."


"Ihr Gesichtsausdruck zeigt keine Traurigkeit, so weit ich es beurteilen kann, dafür schmerzten ihre Worte aber umso mehr."


hi "Hey, lass uns spielen."


hi "Wo das Brett schon mal hier ist."


play sound sfx_warningbell

"Doch das Läuten der Klingel unterbricht mich."


scene black onlayer master
with dissolve

$ suppress_window_after_timeskip = True


label de_S12:

window hide None

scene bg school_council onlayer master
with locationchange

nvl clear

nvl show dissolve

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_daily fadein 0.5

n "\nEs ist wieder alles beim Alten. Ich bin ja zu einem recht ungewöhnlichen Zeitpunkt hier hergewechselt und kann kaum behaupten, dass die ersten Wochen normal waren. Die Wogen haben sich geglättet und ein normales Level erreicht."


n "Ich bin schon länger hier als ich dachte."


n "Vor meiner Ankunft an dieser Schule muss ich eine Menge verpasst haben. Es fällt mir schwer, nicht daran zu denken. Oder an das, was alles in der Zwischenzeit in meiner alten Schule passiert sein könnte."


n "Ich möchte bloß wissen, woher plötzlich diese Gefühle kommen. Ich habe ja nicht gerade viel zurückgelassen."


n "Hier gibt es viel mehr, was ich mag. Sonst würde mich doch so etwas wie der Schülerrat kaltlassen – oder Shizune und Misha. Man hätte mich schon zur Mitarbeit drängen müssen, wenn diese Schule so gewesen wäre, wie ich sie mir ausgemalt hatte."


n "Selbst diese Alltagsroutine macht mich irgendwie froh."


n "Mir graut es vor dem Berg Arbeit, der mich nach dem Unterricht im Schülerrat erwartet. Ich spiele mit dem Gedanken, meine Pflichten zu vernachlässigen, nur dieses eine Mal. Und trotzdem ist es schön, wenn man etwas zu tun hat."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

window show

show shizu basic_normal onlayer master
with charaenter

"Shizune legt einen Stapel Anwesenheitslisten neben mich."


show shizu adjust_happy onlayer master
with charachange

ssh "Noch mal danke fürs Aushelfen."



show shizu adjust_happy onlayer master at tworight
show bg school_council onlayer master at bgright
with charamove

show misha hips_grin onlayer master at twoleft
with charaenter

mi "Danke noch mal, Hicchan~!"


"Eine Menge Arbeit. Ich musste wieder eine Stunde Gebärdensprache sausen lassen. Da ich jetzt aber so weit bin, dass ich den größten Teil der Unterhaltungen zwischen Shizune und Misha verstehen kann, bin ich darüber nicht allzu besorgt."


"Shizune weiß immer noch nichts davon. Und ich bin fest entschlossen, dass das so bleibt, bis ich mit meinen Fähigkeiten zufrieden bin. Mag sein, dass das etwas kindisch von mir ist."


show shizu behind_frown onlayer master
with charachange

ssh "In weniger als fünf Tagen ist Tanabata, aber erst morgen fangen sie damit an, die Stände zu aufzubauen."


show misha sign_smile onlayer master
with charachange

mi "Hicchan, wir müssen morgen bestimmt wieder beim Aufbau der Stände helfen."


hi "Warum? Was für einen Sinn hatte es dann sie auseinanderzunehmen? Das hat doch Tage gedauert, oder?"


show misha hips_grin onlayer master
with charachange

mi "Jepp! Das stimmt~! Obwohl Hicchan nicht da war~."


hi "Ich hätte geholfen, wenn ihr mich gefragt hättet."


show shizu basic_normal onlayer master
with charachange

ssh "Es wäre sinnlos gewesen, dich mit Aufräumarbeiten zu langweilen, nachdem du so viel Spaß beim Fest hattest."


show misha hips_smile onlayer master
with charachange

mi "Es wäre sinnlos gewesen, dich gleich nach dem Fest mit Aufräumarbeiten zu langweilen. Das hätte den ganzen Spaß verdorben."


show shizu behind_smile onlayer master
with charachange

ssh "Außerdem…"


show misha hips_grin onlayer master
with charachange

mi "Ahahaha~! Hicchan ist faul, du hättest sowieso wieder versucht abzuhauen~! Shicchan spielt nicht gern Jagdhund."


hi "Das tut weh."


show shizu adjust_smug onlayer master
with charachange

"Shizune hält sich ihre Hand vor den Mund und beginnt zu zittern. Ich brauche eine Sekunde, um begreifen, dass sie lacht. Hauptsächlich weil sie es völlig lautlos macht."


"Ein etwas seltsamer Anblick, aber im Großen und Ganzen die gleiche ausgelassene Stimmung wie bei Misha, nur nicht ohrenbetäubend."


show misha sign_smile onlayer master
show shizu adjust_happy onlayer master
with charachange

mi "Hm~, das ist wirklich eine gute Frage, Hicchan."


hi "Häh?"


show misha hips_grin onlayer master
with charachange

mi "Die Stände~!"


show shizu basic_normal2 onlayer master
with charachange

ssh "Es ist eine Platzfrage. Die Schule hat keine Möglichkeit, so viele Stände zu lagern, weil jeder Einzelne ziemlich groß ist. Für ein Außenlager wird man nichts ausgeben, also kam es zu dieser Entscheidung. Ineffizient, aber billig."


show misha sign_smile onlayer master
with charachange

mi "Weil~ die Schule keine Möglichkeit hat, so viele Stände zu lagern, Hicchan."


show shizu behind_frown onlayer master
with charachange

shi "…"

show misha perky_confused onlayer master
with charachange

mi "Ah, ja ja~, doch, hat sie, aber man will nichts bezahlen~! Tschuldigung, Shicchan~…"


show shizu basic_normal2 onlayer master
with charachange

ssh "Es liegt an der vorigen Generation."


show shizu behind_frustrated onlayer master
with charachange

ssh "Die Schulleitung hatte entschieden, dass die Lagerkosten zu stark gestiegen waren. Und der Schülerrat vor uns war zu schwach, ihnen zu erklären, dass es Schwachsinn ist, zweimal im Jahr sechzig Stände auf- und abzubauen."


show shizu adjust_angry onlayer master
with charachange

shi "…!"

show misha cross_grin onlayer master
with charachange

mi "Okay~!!"

show shizu behind_smile onlayer master
with charachange

shi "…"

show misha perky_smile onlayer master
with charachange

mi "Hicchan, wir sollten was essen~! Ich fühle mich, als wir hätten wir den ganzen Tag gearbeitet~…"


hi "Haben wir. Ich bin mittlerweile auch hungrig geworden. Eigentlich wollte ich ja Mittag essen, aber es war total überfüllt. Keine Ahnung warum, aber das war's mir nicht wert."


show misha cross_laugh onlayer master
with charachange

mi "Ahahaha~! Es war deswegen so voll, weil sie heute ganz besonders interessante Gerichte angeboten haben."


hi "Zum Beispiel? Nein, sag's nicht. Ist ja im Prinzip egal, ich kann's eh nicht mehr essen."


show shizu adjust_smug onlayer master
show misha hips_grin onlayer master
with charachange

"Shizune sieht merkwürdig zufrieden mit sich aus. Ich frage mich, was der Grund dafür ist."


show shizu behind_smile onlayer master
with charachange

ssh "In weiser Voraussicht habe ich das hier vorbereitet."


"Strahlend vor Selbstzufriedenheit erstellt sie aus ihrer Tasche ein breites Sortiment an Lebensmitteln, das offenbar zu neunzig oder mehr Prozent aus der Kantine stammt."


stop music fadeout 5.0

"Außerdem ist das eine stattliche Menge. Gibt es nicht eine Grenze, wie viel ein Einzelner kaufen darf?"


"Dann sind diese Güter mit Sicherheit unrechtmäßig erworben."


hi "Das Kalbs-Kotelett-Brot ist jedes Mal nach einer Minute ausverkauft. Ich bin beeindruckt, dass du eins bekommen hast."


hi "Vielen Dank."


show misha perky_smile onlayer master
show shizu basic_sparkle onlayer master
with charachange

"Meine Hand fliegt zum Brot, aber im gleichen Moment greift auch Shizune danach."


play music music_another fadein 0.5

show shizu basic_happy_close onlayer master
with characlose

"Eine Sekunde lang stoppt sie ihre Hand, als sie meine berührt, drängt dann aber mit doppelter Anstrengung nach vorn, während in ihren Augen wieder dieser lodernde Kampfgeist aufblitzt. Ihre Finger spitzeln durch meine und suchen nach der Lücke."


"Ich werde keinen Zentimeter weichen und bin bereit, dieses Brot mit meinem Leben verteidigen. Diese Gelegenheit kommt vielleicht nie wieder."


"Mir ist vollkommen klar, dass das Brot bis zur Ungenießbarkeit zerquetscht wird, wenn wir so weitermachen."


hi "Misha… Sag ihr, dass das Brot zerquetscht wird, wenn sie nicht nachgibt."


show misha perky_confused onlayer master
with charachange

mi "Hmmmmm? Warum machst du's nicht selbst?"


"Ich bin erschrocken, wie lässig es aus ihr herauspurzelt, dass ich mich ganz normal mit Shizune unterhalten könnte, wenn ich will."
"Man möchte meinen, das war Absicht, doch sie scheint vielmehr durch ihr Trinkpäcken abgelenkt zu sein, da sie die Verpackung des Strohhalms nicht aufbekommt."


hi "Ist das nicht eindeutig? Ich kann das Brot nicht loslassen."


show misha sign_smile onlayer master
with charachange

mi "Nun, das kann ich Shicchan nicht sagen."


show misha hips_grin onlayer master
with charachange

"Sie streckt die Handflächen zum Himmel und zuckt breit grinsend mit den Schultern."


hi "Warum nicht?"


show misha sign_smile onlayer master
with charachange

mi "Denn~! Du wärst im Vorteil, also kann ich dir nicht trauen~! Wenn Shicchan antworten möchte, muss sie das Brot loslassen, dann gewinnst du. Wer weiß, wer weiß, vielleicht ist es genau das, was du willst, Hicchan?"


show misha cross_smile onlayer master
with charachange

mi "Das wäre nicht fair, ich bin lieber neutral! Wie die Schweiz~!"


hi "Die Schweiz?"


show misha perky_smile onlayer master
with charachange

mi "Kennst du die Schweiz?"


hi "Natürlich… Sie ist neutral, sie sind neutral."


show shizu basic_sparkle_close onlayer master
with charachange

"Shizune starrt mich mit einem großspurigen Blick an, während ihre Zungenspitze zwischen den Zähnen hervorlugt und weiter mit Nachdruck am Kalbs-Kotelett-Brot zwischen uns zerrt."


show shizu adjust_happy onlayer master
with charadistant

"Mit einem Mal lässt sie los und hält die Hände mit den Innenflächen nach außen hoch. Die universelle Friedensgeste."


show shizu behind_blank onlayer master
with charadistant

ssh "Ein erbärmlicher Versuch, das hier zu klären, findest du nicht? Außerdem könnte das Brot brechen."


show shizu behind_frown onlayer master
with charadistant

"Sie starrt mich mit träger Miene an, die sich schnell in eine missbilligende Grimasse verwandelt."


show shizu adjust_angry onlayer master
with charadistant

shi "…!"

show misha hips_frown onlayer master
with charachange

mi "Hicchan! Lass das Brot los! Wir verhandeln gerade!"


"Widerwillig lasse ich das Brot los."


show misha perky_smile onlayer master
show shizu behind_blank onlayer master
with charachange

"Mishas Hände schnellen von der Seite hervor, wobei sie auf dem Weg zum Ziel ihre Finger auf dem Tisch trommeln lässt."


show misha hips_grin_close onlayer master
with characlose

mi "Ah~! Haha~! Lasst euch nicht stören, Kalbsfleisch mag ich nicht mal so besonders. Ich nehme mir einfach dieses Sandwich hier~! Und natürlich was zu trinken…"


show misha perky_smile onlayer master
with charadistant

"Sie nimmt sich vorsichtig ihr Essen und zieht sich dann sofort zurück."


"Eigentlich hat sie Recht. Bei all den Delikatessen könnte ich einfach etwas anderes aussuchen. Auch das Hühnchen-Katsudon-Brot ist sehr beliebt und rangiert in Geschmack und Nachfrage weit oben. Allerdings habe ich vorhin schon eins gegessen."


show shizu basic_angry onlayer master
with charachange

ssh "Du bist so kindisch, Hisao. Es wäre doch kein Problem, dir etwas anderes zu nehmen. Das Hühnchen-Katsudon-Brot ist lecker."


show misha hips_smile onlayer master
with charadistant

mi "Du bist so kindisch, Hicchan. Warum nimmst du nicht stattdessen das Hühnchen-Katsudon-Brot? Es ist lecker~!"


hi "Das habe ich aber schon gegessen."


show shizu behind_frown onlayer master
with charachange

shi "…"

show misha hips_frown onlayer master
with charachange

mi "Hicchan~! Du bist ja regelrecht besessen. Was an dem Kalbs-Kotelett-Brot ist sooo be-son-ders?"


hi "Man kann es nur schwer bekommen. Raritäten schmecken besser."


show shizu basic_frown onlayer master
with charachange

ssh "Du benimmst dich wie ein Kind."


show misha cross_frown onlayer master
with charachange

mi "Du benimmst dich wie ein Kind, Hicchan."


hi "Warum isst du nicht das Hühnchen-Brot?"


show shizu adjust_blush onlayer master
with charachange

ssh "Das ist unwichtig."


"Shizune läuft knallrot an, bevor sie mit einem gerissenen Lächeln fortfährt."


stop music fadeout 6.0

show shizu basic_happy onlayer master
show misha perky_smile onlayer master
with charachange

ssh "Man kann mit dir nicht argumentieren. Es gibt wohl nur einen Weg, das zu klären: Wir werden darum spielen."


show misha sign_smile onlayer master
with charachange

mi "Macht nichts: Wir werden stattdessen darum spielen~!"


"Irgendwie habe ich das vorhergesehen. Das ist die logische Konsequenz."


"Shizune hat bis jetzt fast durchgehend gelernt. Jetzt, wo unser Finale vorbei ist, muss die überschüssige Energie irgendwo hin."


hi "Was spielen?"


hide misha onlayer master
with None
show misha perky_smile behind shizu onlayer master at twoleft
with None

show shizu behind_blank_close onlayer master
with characlose

ssh "Das älteste bekannte Spiel der Menschheit, auf dem, wie man weiß, das Schicksal ganzer Nationen ruhte: Schere, Stein, Papier."


show misha sign_smile onlayer master
with charachange

mi "Wir spielen Schere, Stein, Papier."


show misha perky_confused onlayer master
with charachange

mi "Echt? Das klingt so ernst, Shicchan…"


play music music_shizune fadein 1.0

"Ihr Gesicht zeigt nicht einen Hauch von Humor. Sie meint es todernst."


hi "Okay, okay."

show shizu adjust_happy_close onlayer master
with charachange

"Sie zieht ihre Hand zurück und ich tue es ihr gleich."


hi "Los!"


show shizu basic_angry_close onlayer master
with charachange

"Wir haben beide Stein gewählt. Unentschieden. Ich dachte, das wäre der perfekte Plan. Stein ist unzerstörbar. Shizune sieht beunruhigt aus, angesichts dieser schicksalhaften Wende. Läuft es nicht wie geplant?"


show shizu adjust_angry_close onlayer master
with charachange

ssh "Noch mal!"


show shizu basic_frown_close onlayer master
with charachange

"Zweimal Papier."


hi "Mist."


show shizu adjust_angry_close onlayer master
with charachange

ssh "Noch mal!!"


show shizu basic_frown_close onlayer master
with charachange

"Wir ziehen wieder zwei Steine hervor, doch beim dritten Mal präsentieren wir Scheren."


show misha hips_grin onlayer master
with charachange

mi "Sieht witzig aus, darf ich mitspielen?"


show misha cross_laugh onlayer master
with charachange

mi "Hahahaha~!"

show shizu behind_frown_close onlayer master
with charachange

ssh "… … …"

show misha perky_smile onlayer master
with charachange

mi "Das ist ein Duell, Shicchan?"


show shizu adjust_angry_close onlayer master
with charachange

shi "…"

show misha sign_confused onlayer master
with charachange

mi "Äh~, Duellregeln? Hm~… Das stimmt, das stimmt~! Die kenne ich wirklich nicht…"


show shizu cross_angry_close onlayer master
with charachange

shi "…"

show misha perky_confused onlayer master
with charachange

"Je schneller sie die Zeichen gebärdet, desto schwerer ist es, ihr zu folgen. Selbst Misha scheint Probleme zu haben."


hi "Wovon spricht sie?"


show shizu adjust_angry_close onlayer master
with charachange

ssh "Einmal noch!"


show shizu basic_frown_close onlayer master
with charachange

"Wieder Gleichstand. Jedes Mal verlangt Shizune eine Wiederholung, bis sie diesen Schritt am Ende ganz überspringt und Schere, Stein, Papier mit immer sorgloserer Hingabe ausspielt."


"Obwohl wir inzwischen völlig planlos spielen – der Gleichstand bleibt. Eine mathematische Ausnahmesituation."


stop music fadeout 8.0

show misha hips_grin onlayer master
with charachange

"Misha, die über uns zu schweben scheint, sieht uns zu und lacht jedes Mal, wenn wir ziehen. Nach sechzehn Runden schiebt Shizune ihren Stuhl vom Tisch weg und steht auf."


show shizu behind_blank_close onlayer master
with charachange

shi "…!"

show misha hips_smile onlayer master
with charachange

mi "Es reicht, Hicchan~! Ich weiß, was ich falsch gemacht habe, in der nächsten Runde ist alles vorbei, also mach dich darauf gefasst, okay~? Okay~!"


show misha sign_smile onlayer master
with charachange

mi "Ich habe deine Gedankengänge studiert und~ ich weiß, wie du spielst. Ich werde deinen nächsten Zug voraussehen und ihn fachgerecht bekämpfen."


"Das ist mir neu. Ich kann mich nämlich nicht mehr daran erinnern, warum wir das ganze überhaupt machen."


show shizu adjust_happy_close onlayer master
with charachange

"Shizune grinst selbstsicher und mit einem Ausdruck furchtlosen Wagemuts. Reiner Kampfgeist brennt in ihren ruhigen Augen, als sie die Hand zurückzieht und mich somit wortlos auffordert, es ihr gleichzutun."


"Ihre Haltung ist beeindruckend, wie ein Profi-Bowler oder so, nur für eine Handbewegung."


show shizu basic_happy_close onlayer master
with charachange

"Zweimal Papier."


play music music_comedy

show shizu cross_stunned_close onlayer master
with charachange

"Mit einem Mal erschlafft Shizunes Körper und sie reibt sich mit einem Ausdruck der Verzweiflung die Schläfen, während sie einen langen Seufzer ausstößt, als würde man einem Reifen die Luft raus lassen."
"Ich bemerke, dass ich mittlerweile noch viel hungriger geworden bin."


hi "Wir können es uns doch teilen."


show shizu behind_blank_close onlayer master
with charachange

"Ich breche das Brot entzwei und biete eine Shizune an. Sie nimmt das Stück."


show shizu adjust_happy_close onlayer master
with charachange

ssh "Dankeschön."


"Sie schaut auf das Brot in ihrer Hand und untersucht es."


show shizu basic_normal2_close onlayer master
with charachange

ssh "Aber irgendwie erscheint mir die Sache sinnlos."


show shizu basic_normal2_close onlayer master
with charachange

"Unabhängig davon isst sie das Brot trotzdem."


"Wie aus heiterem Himmel fällt mir Misha auf, die das Geschehen außerhalb meines Blickfeldes beobachtet hat."


show misha hips_grin onlayer master
with charachange

mi "Hicchan~… Das war sehr romantisch, finde ich."


hi "Ach, komm schon."


show misha cross_laugh onlayer master
with charachange

mi "Wahahahahaha~!"

show misha hips_smile onlayer master
with charachange

stop music fadeout 5.0

"Lachend beißt sie in ihr zweites Sandwich."


"Wir essen eine Weile in schweigsamer Runde und schaffen es, weiteren Wettkämpfen aus dem Weg zu gehen. Anschließend geht es zurück an die Arbeit."


scene bg school_council_ss onlayer master
with shorttimeskip

play music music_tranquil fadein 3.0

"Beim üblichen Aktenordnen denke ich mir, dass das Shizunes Art sein könnte, die Woche mit einem Höhepunkt zu beginnen."


"Die wahre Arbeit wird letztendlich morgen anfangen, und da sie mit dem Budenbauen buchstäblich alle Hände voll zu tun haben wird, dürfte sie nicht viel zum „Reden” kommen."


"Wahrscheinlich wird's wieder eintönig und ermüdend – wie beim ersten Mal."
"In diesem Punkt weiß ich ihre Anstrengungen zu würdigen. Solche Tage wie heute sind einfach schön, als eine Art Aufmunterung vor den bevorstehenden Tagen. Ich glaube, das war auch ihr Hintergedanke."


"… Da fällt mir ein, dass ich immer noch Kenjis Paket loswerden muss. Das Mist-Ding ist sperrig, aber seit ich es abgeholt habe, ist es mir nicht gelungen, ihn zu erwischen."


scene bg school_lobby_ss onlayer master
with locationchange

"Nachdem der Schülerrat für heute verschoben wurde, trenne ich mich kurz von Shizune und Misha, um zum Getränkeautomaten zu laufen. Obwohl der Weg nicht weit ist, habe ich schon nach wenigen Sekunden das Gefühl, nicht allein zu sein."


scene black onlayer master
with hands_in

"Ein Paar Hände verdecken meine Augen."


mi "Wer bin ich~!"


hi "Shizune?"

mi "Wahahaha~! Ich bin's, Hicchan~!"


hi "Ja, ich weiß."


scene bg school_lobby_ss onlayer master
with hands_out

with Pause(0.3)

show misha hips_frown_close_ss onlayer master at Slide(0.3, 0.5, 0.5, 0.5, 1.0)
with Dissolve(1.0)

mi "Warum hast du dann gesagt, es wäre Shicchan? Ist schon in Ordnung, wenn man manchmal falsch liegt, Hicchan~! Du bist zu stolz."


show misha sign_smile_close_ss onlayer master at center
with charachange

mi "Jedenfalls hast du doch nach dem Schülerbüro in der Regel keine Pläne, stimmt's? Also~, du gehst einfach nur schnurstracks zum Studentenwohnheim?"


hi "Wo soll ich denn sonst hingehen?"


show misha hips_grin_close_ss onlayer master
with charachange

mi "Okay, das ist toll~! Das ist toll, Hicchan~! Ich wollte heute mal mit dir reden, das passt also perfekt!"


"Zwei Oberschüler nach dem Unterricht, allein in einem stillen, leeren Gebäude. Als die Sonne den Himmel in ein romantisches Bernsteingelb taucht, sagt das süße Mädchen, dass es reden möchte."


"Was für eine geheimnisvolle und einladende Atmosphäre. Meine Vorstellungskraft läuft auf Hochtouren. Es wird zwar sicherlich nicht annähernd so aufregend, wie ich es mir ausmale, aber es macht Spaß, es durchzuspielen."


play sound sfx_can
show misha perky_confused_close_ss onlayer master
with Dissolve(0.2)

"Das knallende Geräusch beim Öffnen meines Dosen-Kaffees begräbt alle Hoffnungen, diese kitschige Stimmung aufrechtzuerhalten. In dieser Situation kommt es mir unglaublich laut vor. Ich seufze – vor Enttäuschung und Erleichterung."


hi "Also, was ist?"


show misha perky_smile_close_ss onlayer master
with charachange

mi "Hm? Oh! Ja, eigentlich~… Ich liege in einigen Fächern etwas zurück und wenn ich den Stoff nicht aufhole, habe ich ein Problem~! Ich kann es nicht mehr vor mir herschieben."


show misha perky_sad_close_ss onlayer master
with charachange

mi "Meine Lehrer sind der Meinung, dass ich wirklich ernster an die Sache rangehen muss, darum sollte ich zuhören, besonders~ weil es schon das dritte Mal ist."


mi "Tut mir leid~! Es tut mir so leid, Hicchan."


hi "Wofür entschuldigst du dich?"


show misha sign_sad_close_ss onlayer master
with charachange

mi "Ich kann euch beide für ein paar Tage nicht beim Schülerrat unterstützen~. Es ist nur für drei Tage, wirklich! Ich gebe mein Bestes und komme so schnell es geht zurück! Aber~…"


"Ich bin nicht gerade glücklich darüber."
"Wir werden diese Woche ganz schön beschäftigt sein, was? Ein denkbar schlechtes Timing. Einen Moment lang liegt mir die Frage auf der Zunge, ob Shizune nicht ihre Verbindungen spielen lassen könnte, um ihr aus der Klemme zu helfen."


"Doch Misha wirkt, als sei ihre Entschuldigung aufrichtig. Es wäre an dieser Stelle einfach unverschämt von mir, so etwas zu sagen."


"Wenn sie außerdem behauptet, es nicht mehr verschieben zu können, dann glaube ich ihr das auch. Gerade wenn man bedenkt, wie unerwartet ernst ihr der Schülerrat manchmal ist."


hi "Ja, ich verstehe. Ist schon gut. Du und Shizune habt es ja letztes Jahr ganz allein geschafft, nicht wahr? Also werde ich es auch hinkriegen. Mach dir keine Sorgen."


show misha hips_grin_close_ss onlayer master
with charachange

mi "Wirklich? Vielen Dank, Hicchan~! Wirklich~! Wuhu juhu~! Ich hätte nicht gedacht, dass Hicchan es so gut aufnimmt~! Ich habe angenommen, du machst dir Sorgen wegen~ der vielen Arbeit für Tanabata und all dem~!"


"Verdammt, schon komisch, wie gut sie mich kennt."


show misha sign_smile_close_ss onlayer master
with charachange

mi "… Aber~! Hicchan nimmt es ganz gelassen~! Bin ich froh~…"


hi "Haha, ja. Stimmt schon, das ging mir durch den Kopf. Ist aber keine große Sache. Wegen so was werde ich nicht gleich durchdrehen."


hi "Nichtsdestotrotz wird es sicher etwas nerven, wenn Shizune und ich zum Reden wieder diesen Notizblock hin- und herschieben."


show misha hips_frown_close_ss onlayer master
with charachange

mi "Hicchan, sag Shizune doch einfach, dass du auch die Gebärdensprache beherrschst! Ich kapiere das nicht."


hi "Noch nicht. Ich kann zwar das meiste gut verstehen, aber ich möchte auf Nummer sicher gehen. Ha, obwohl es eigentlich egal ist. Die Geheimniskrämerei bringt mich noch um, dabei wäre es toll, ein richtiges Gespräch mit ihr zu führen."


hi "Mach dir keine Sorgen. Irgendwann muss ich es ihr ja sagen. Ehrlich gesagt suche ich nach einer günstigen Gelegenheit."


show misha hips_smile_close_ss onlayer master
with charachange

mi "Das wird kein Problem sein, Hicchan~!"


hi "Und warum nicht?"


stop music fadeout 3.0

show misha sign_smile_close_ss onlayer master
with charachange

mi "Na ja~, weil ich… irgendwie… Shicchan erzählt hab, dass du sie verstehen kannst. Sie hat sich genau wie du den Kopf zerbrochen, dass ihr euch nicht verständigen könnt~! Also~! Ich war besorgt, aber am Ende ist ja alles gut ausgegangen~!"


show misha sign_confused_close_ss onlayer master
with charachange

mi "Hahaha?"

"Ich dreh durch."


play music music_running

hi "AAAAAAAAAAHHH!!"

hi "Hast du eine Ahnung, wie ich jetzt dastehe? Verdammt, ich hab hier praktisch den halben Tag dagesessen und so getan, als könnte ich keine Gebärdensprache! Und du willst mir allen Ernstes erzählen, dass sie's die ganze Zeit gewusst hat?"


hi "Bestimmt hat sie gedacht: „Dieser Kerl ist ein kompletter Trottel, wenn er vorgibt, mich nicht zu verstehen.” Ich hab 'nen Vollidioten aus mir gemacht."


hi "Wie konntest du das zulassen?!"


show misha hips_frown_close_ss onlayer master
with charachange

"Misha runzelt nur sprachlos die Stirn, da sie so eine Reaktion offenbar nicht erwartet hat. Erst als ich mich wieder beruhigt habe, spricht sie wieder."


show misha hips_smile_close_ss onlayer master
with charachange

mi "… Aber, Hicchan, ich glaube ganz einfach, dass es so am besten ist~!"


"Das sagt sie mir, ohne mit der Wimper zu zucken. Auf diesen Moment hat sie während meiner Panikattacke gewartet."


"Mit ihrer sonnigen Art hat sie es geschafft. Jetzt wirkt es so, als hätte sie die Zeit von dem Punkt, als die Bombe geplatzt ist, bis jetzt quasi herausgeschnitten. Schon komisch."


hi "Du denkst immer nur einspurig, weißt du das?"


show misha hips_grin_close_ss onlayer master
with charachange

mi "Ja~!"


stop music fadeout 4.0

"Das Kind ist in den Brunnen gefallen. Wenn Misha mit so unerschrockener Sicherheit glaubt, dass alles gut wird, sollte ich der Sache vielleicht noch eine Chance geben."


"Und wenn's nicht gut geht, nehme ich die Beine in die Hand…"


"Zur Aussöhnung bietet sie mir an, noch ein Getränk aus dem Automaten zu kaufen, nur für den Fall. Auch wenn es nur ein kleines Zeichen der Entschuldigung ist, aber es ist wohl der Gedanke, der zählt. Und sie meint es ehrlich."


"Außerdem ist es ein Gratisgetränk, also nehme ich es an."


scene black onlayer master
with dissolve


label de_S13:

scene bg school_dormhisao onlayer master
with locationchange

"Ich schlucke meine alltägliche Handvoll Pillen mit einem Glas herunter."


"Nach gut und gern acht Stunden Schlaf weiß ich echt nicht mehr, wovor ich letzte Nacht so eine Angst hatte. Während ich ein besonders großes Kaliber einer Tablette entzweikaue, versuche ich meine Sorgen mit Vernunft wegzudenken."


$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_dreamy fadein 2.0

window hide

nvl clear

nvl show dissolve

n "\nShizune wusste, dass ich gestern den ganzen Tag den Kurs in Gebärdensprache besucht habe, und hat daraus keine große Sache gemacht."


n "Sie ist zwar stumm, aber das heißt nicht, dass sie ihre Gefühle nicht ausdrücken kann. Nein, in Wahrheit scheint sie auf die Art viel direkter zu sein."


n "Sie redet nicht lang um den heißen Brei herum oder hält sich zurück. Bei so einem kompromisslosen Charakter kann es kein Missverständnis geben."


n "Wenn sie also damals schon nicht sauer war, warum sollte sie es jetzt sein? Das würde nicht zu ihr passen und überhaupt habe ich ja nichts falsches getan."


n "Mit dem Abebben meiner Ängste kommt mir der Gedanke, dass ich einige Tage allein mit Shizune ohne Misha verbringen werde. Gestern habe ich mir keine echten Gedanken darüber gemacht, aber die Vorstellung wird immer bedrückender. Stimmt schon, dass ich Gebärdensprache ganz gut beherrsche, aber…"


n "Auf jeden Fall würde ich nicht behaupten, dass ich mehr als das Grundniveau verstehe. Ich bezweifle, dass ich mithalten kann, wenn sie wie so oft die Geschwindigkeit beim Gebärden anzieht."


n "Auch das Ausführen der Gesten ist nicht gerade meine Stärke. Beides gleichzeitig zu schaffen wie Misha ist noch Wunschdenken."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

scene bg school_scienceroom onlayer master
show misha hips_grin onlayer master at twoleft
show shizu behind_smile onlayer master at tworight
with shorttimeskip

window show

mi "Hicchan~!"

hi "Was?"


show misha sign_smile onlayer master
with charachange

mi "Vergiss nicht, du wolltest heute beim Budenaufbau aushelfen~! Hinter der Schule, nach Ende des Unterrichts, okay~?"


hi "Ich weiß, ich weiß."


show shizu adjust_happy onlayer master
with charachange

shi "…"

show misha hips_smile onlayer master
with charachange

mi "Als du uns das letzte Mal geholfen hast, hast du dir unsere Hochachtung verdient~! Diesmal ist es sogar noch wichtiger, Schwänzen ist da unverzeihlich, okay?"


"Ich will nach dem Grund fragen, aber dazu komme ich nicht. Außerdem hinkt Misha im Unterricht hinterher, da scheint es keine gute Idee zu sein, sie abzulenken. Ich kann sie auch zu Mittag fragen, und genauso kommt es auch."


scene bg school_cafeteria onlayer master
show misha sign_smile onlayer master at twoleft
show shizu behind_blank onlayer master at tworight
with shorttimeskip

mi "Weil, Hicchan, ein Fest, das das Dorf feiert, genau das ist, wonach es klingt. Es ist dazu da, deine Heimat und ihre Geschichte zu feiern."


show misha hips_grin onlayer master
with charachange

mi "Tanabata ist anders, da geht's um Wünsche und Liebe~! Das macht es doch definitiv bedeutender, stimmt's? Jepp~, natürlich stimmt's~."


hi "Ist das denn wirklich der Sinn des Festes?"


show shizu basic_frown onlayer master
with charachange

shi "…"

show misha cross_frown onlayer master
with charachange

mi "Hicchan, du verstehst einfach keinen Spaß…"


"Misha plustert verstimmt die Backen auf, um die Luft dann wie ein Ballon auszupusten."


show misha hips_frown onlayer master
with charachange

mi "So was muss man wertschätzen, selbst wenn's letzten Endes nur eine Ausrede ist, etwas Leckeres zu essen und sich rauszuputzen~!"


show misha sign_smile onlayer master
with charachange

mi "Ich wäre enttäuscht, wenn du nicht mitmachst, okay?"


stop music fadeout 5.0

"Bevor ich etwas entgegnen kann, dreht sie sich zur Seite und inhaliert eine Krokette."


scene bg school_gardens2 onlayer master
with shorttimeskip

"Nach dem Unterricht treffe ich Shizune hinter der Schule, wo sie anscheinend schon irgendwann gestern alles vorbereitet hat."


show shizu adjust_happy onlayer master at center
with charaenter

"Sie grüßt mich mit einem kurzen Winken. Mit einem ausladenden Schwung des Hammer in ihrer Hand zeigt sie dann zu den Ständen hinter ihr. Manche sind schon halb fertig, andere noch immer ein verstreuter Haufen zusammengeschnürter Bretter."


hide shizu onlayer master
with charaexit

show bg school_gardens2_ss as overlay onlayer master at Alphain(20.0), center
with None

play ambient sfx_stallbuilding fadein 8.0

"Die Zeit vergeht und ich bemerke, dass die Pillen gerade ausreichen. Ich werde schneller müde als sonst. Zum Glück dreht mir Shizune den Rücken zu; ich kann also einige Pausen einlegen, ohne dass sie nach dem Grund fragt."


"Beim Pausieren fange ich jedoch an nachzudenken und fühle mich schuldig, dass ich ihre Unfähigkeit ausnutze, meinen Hammerschlag zu hören. Es ist furchtbar, sich darüber noch zu freuen."


"Ihre Arbeitsmoral ist vorbildlich. Man sieht, dass es sie langweilt und sogar nervt, aber das mindert ihr Tempo nicht im geringsten. Wenn ein Arm beim Zusammennageln der Stände ermüdet, nimmt sie halt den anderen."


hi "Shizu…"

"Als ich ihren Namen rufe, komme ich mir vor wie ein Idiot."


"Ich kann ihr nicht sagen, was ich denke. In meiner Hand liegt schließlich auch ein Hammer, ich muss einfach mithalten."


"Ich kann jetzt nicht schlappmachen, vor allem wenn wir nur zu zweit sind. Keine Zeit und keine Gelegenheit zum Gebärden. Nicht einmal für ein „Gut gemacht”."


"Selbst für so etwas Normales müsste ich zunächst meinen Hammer weglegen, ihre Aufmerksamkeit erlangen und ihr es dann gestikulieren."


"Eine einfache Geste verwandelt sich eine unnötig komplexe Handlung, wie ein einzelner Schritt auf einer Straße, die länger ist als gedacht."


"Ich kenne sie jetzt lang genug, um das zu wissen, und habe es trotzdem vergessen."


"Die Luft ist erfüllt vom rhythmischen Klingen der Nägel, die ins Holz geschlagen werden."


"Nach einer Weile geht es eigentlich sogar. Um der Monotonie zu entkommen, versuche ich mein Hämmern erst an das von Shizune anzupassen und dann zu variieren, um einen Takt zu bilden. Natürlich bemerkt sie davon nichts."


"Was die Frage aufwirft, ob ihr durch das Fehlen von jeglichem Geräusch die Arbeit noch schleppender und langweiliger vorkommt."


stop ambient fadeout 3.0

"Ob es seltsam ist, die Ergebnisse ihre Handlungen nicht hören zu können, obwohl sie die Vibrationen über ihre Finger spürt? Oder kümmert es sie gar nicht, weil sie ja gar keine Vorstellung von Klängen hat?"


"Völlig abgelenkt bemerke ich erst jetzt, dass Shizune sich an mich herangeschlichen hat."


scene bg school_gardens2_ss onlayer master
show shizu adjust_happy_ss onlayer master at center
with charaenter

play music music_soothing fadein 5.0

ssh "Pause?"


his "Ja, glaub schon."


show shizu behind_smile_ss onlayer master
with charachange

ssh "Okay, machen wir eine."


show shizu basic_normal_ss onlayer master
with charachange

ssh "Du kannst Gebärdensprache verstehen."


show shizu behind_blank_ss onlayer master
with charachange

ssh "Das macht alles viel leichter für uns beide. Obwohl du es vor mir versteckt hast."


hi "Hahaha…"

show shizu basic_normal2_ss onlayer master
with charachange

ssh "Warum?"


his "Warum was?"


show shizu behind_blank_ss onlayer master
with charachange

ssh "Warum hast du dich entschieden, Gebärdensprache zu lernen?"


"Sie mustert mich eindringlich, als ob sie die Antwort aus meinen Augen herauslesen wollte."


"Unheimlich, wie durchdringend ihr Blick sein kann, schwarz wie ein See bei Nacht."


his "Weil ich es so wollte. Ich dachte, es wäre sicher nützlich. Und das war es ja auch, oder?"


show shizu adjust_happy_ss onlayer master
with charachange

ssh "Ja."


show shizu basic_normal_ss onlayer master
with charachange

shi "…"

his "Entschuldige, ich habe nichts davon verstanden."


his "Siehst du? Diese Sache kommt immer wieder vor. Ich wünschte, Misha wäre hier."


show shizu behind_blank_ss onlayer master
with charachange

ssh "Sie muss nacharbeiten, nicht wahr? Das ist zum Teil auch meine Schuld. Misha braucht keine Nachhilfestunden. Ihre Noten sind nicht die Besten, aber sie weiß, wie ihre Entscheidungen andere beeinflussen. Das hat sie vielen Menschen voraus."


show shizu basic_angry_ss onlayer master
with charachange

ssh "Besonders gewissen Blondinen."


hi "Ah…"

"So etwas vergisst sie nicht so einfach."


show shizu behind_smile_ss onlayer master
with charachange

ssh "Deine Gebärdensprache ist sehr gut. Du lernst außergewöhnlich schnell."


his "Ich nehme ja nun schon eine Weile am Unterricht teil. Dann schnappt man es leichter auf – durch Praxis, Osmose und solche Sachen. Ist gar nicht so schlecht."


his "Und wenn ich mal richtig feststecke, gibt es ja noch Misha."


show shizu adjust_smug_ss onlayer master
with charachange

shi "…"

show shizu behind_smile_ss onlayer master
with charachange

shi "…"

"Das war wohl zu voreilig. Ich habe kein Wort verstanden. Zeit zurückzurudern."


his "Ja, also, so einfach ist es doch nicht. Eigentlich ist es sauschwer. Wie das Aufsammeln von Glasscherben."


his "Aber spannend ist es auch irgendwie. Wie ein Abenteuer. Ach, nee…"


show shizu basic_normal2_ss onlayer master
with charachange

ssh "Glasscherben aufzusammeln ist kein Abenteuer."


his "Aber hallo. Das ist eine echte Herausforderung."


show shizu behind_blank_ss onlayer master
with charachange

ssh "Mit Schaufel und Besen nicht."


"Ich bin frustriert und deprimiert."


"Als ich aufblicke, bemerke ich, dass sie eine Dose Mineralwasser in der Hand hält."


hi "Wo hast du die denn her?"


show shizu adjust_happy_ss onlayer master
with charachange

"Ich habe das gestikulieren vergessen, aber sie musste nur meinem Blick folgen, um mich zu verstehen, und zaubert noch eine hinter ihrem Rücken hervor. Sie wirft mir die Dose zu und ich fange sie beidhändig auf."


show shizu behind_smile_ss onlayer master
with charachange

ssh "Ich habe dir auch eine mitgebracht."


play sound sfx_can

"Sie macht eine Pause, um mit ihrem Fingernagel unter den Verschluss zu schlüpfen und diesen aufzureißen, bevor sie die Dose beiseite stellt."


show shizu basic_normal_ss onlayer master
with charachange

ssh "Wenn du dich so anstrengst mir zu helfen, muss ich auch auf dich aufpassen. Das versteht sich von selbst."


show shizu behind_blank_ss onlayer master
with charachange

ssh "Wenn du vorhast Gebärdensprache zu lernen, ist das aber was völlig anderes. Natürlich bin ich beeindruckt. Aber der Unterschied liegt in der Wiedergutmachung."


show shizu adjust_happy_ss onlayer master
with charachange

stop music fadeout 8.0

ssh "Ich bin sehr glücklich."


show shizu behind_smile_ss onlayer master
with charachange

"Sie leert die Dose in einem Zug, streckt die Arme hinter ihren Rücken und springt auf."


show shizu adjust_smug_ss onlayer master
with charachange

ssh "OK! Zurück an die Arbeit!"


hide shizu onlayer master
with charaexit

"Und das war's. Shizune kehrt mit der gleichen Leidenschaft zur Arbeit zurück wie zuvor. Der einzige Hinweis, dass sie eine Pause hatte, ist ein Lächeln, von dem noch eine Spur auf ihrem Gesicht zurückgeblieben ist."


show bg school_gardens2_ni as overlay onlayer master at Alphain(10.0), center
with None

"Während ich ebenfalls weitermache, denke ich darüber nach, dass Misha Recht damit hatte, dass sich alles zum Besten wendet. Alles scheint darauf hinauszulaufen."


"Als es dunkel wird, schaut Misha vorbei, die so müde aussieht wie ich mich fühle, und Shizune beschließt, für heute Schluss zu machen."


"Während wir unser Tageswerk beenden und jeder seine Wege zu den Wohnheimen geht, fällt mir auf, wie fließend sie miteinander reden und wie unbeschwert sie lachen."


"Jetzt bewundere ich Mishas Geschick in Gebärdensprache nur noch mehr. Ob ich je ihr Niveau erreichen oder überhaupt die Zeit dafür haben werde?"


scene black onlayer master
with dissolve


label de_S14:

scene black onlayer master
with None

play sound sfx_impact

scene bg school_dormhisao onlayer master
with vpunch

"Das erste, was diesen Morgen passiert, ist, dass ich mal wieder über Kenjis Paket stolpere und kopfüber auf den Boden fliege, bevor ich überhaupt richtig wach bin."


show kenjibox onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Am liebsten würde ich mit dem erstbesten stumpfen Gegenstand wie bei einem Homerun auf das Ding einschlagen, aber selbst dazu fehlt mir an diesem Morgen die Energie…"
"Außerdem würde der Inhalt sicherlich Schaden nehmen. Und das wäre gemein."


show kenjibox onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide kenjibox onlayer master
with None

scene bg school_dormhallway onlayer master
with locationchange

"Ich schiebe es in den Hausflur, wo es ohne großen Widerstand entlangschlittert und mit einem dumpfen, fast lautlosen Rumms an Kenjis Tür stößt. Sofort entriegeln sich der Reihe nach ein Dutzend Schlösser wie eine aufsteigende Tonleiter."


play music music_kenji fadein 0.5

show kenji tsun onlayer master at Slide(0.4, 0.5, 0.5, 0.5, 0.5)
with charaenter

ke "Wer ist da?"


"Trotz der Frage läuft er blindlings auf den Flur – irgendwie ohne über das Paket zu stolpern. Es hätte beinahe elegant ausgesehen, wenn ich mir nicht sicher wäre, dass es purer Zufall war."


hi "Ich bin's, hab deine Post abgeholt. Dein Paket liegt da unten."


show kenji happy onlayer master at center
with charachange

ke "Weiß ich. Vielen Dank, Mann."


hi "… Ja, egal."


hi "Was ist denn drin?"


show kenji tsun onlayer master
with charachange

"Er zuckt zusammen und verhält sich plötzlich abwehrend und beunruhigt."


ke "Gar nichts."


hi "Komm schon, sag's mir, ich bin neugierig."


hi "Weißt du, ich hab mir fast das Genick gebrochen, als ich darüber gestolpert bin."
hi "Und vorher musste ich diese lächerlich große Kiste herumschleppen, mir die Sicht versperren lassen und dabei noch Straßen überqueren… Da kannst du mir zumindest sagen, was drin ist."


ke "Das ist geheimes Material. Wenn ich es dir sage, ist es kein scheiß Geheimnis mehr. Es ist nichts Wichtiges."


hi "Na, wenn es nichts Wichtiges ist, kannst du es mir ja sagen."


ke "Wenn es nichts Wichtiges ist, warum willst du es dann wissen?"


hi "Was ist daran verkehrt?"


ke "Warum willst du es wissen?"


hi "Warum darf ich es nicht wissen?"


show kenji neutral onlayer master
with charachange

ke "Warum antwortest du auf meine Fragen mit Fragen?"


hi "Warum beantwortest du nicht meine erste Frage?"


ke "Warum beantwortest du nicht meine letzte Frage?!"


"Ich bekomme mit, dass unsere Stimmen mit jeder Antwort lauter werden. Am Ende des Ganges springt eine Tür auf und jemand streckt verwundert den Kopf raus, um zu sehen, was los ist."


"Wir müssen wie Idioten aussehen, aber ich wette, von uns beiden bin ich der einzige mit ausreichend Scham, um das zu begreifen."



hi "Schön, du kannst es mit ins Grab nehmen. Ich muss mich auf die Schule vorbereiten."


show kenji tsun onlayer master
with charachange

ke "Nein, verdammt. Warum hast du es so eilig? Bleib noch ein bisschen. Willst du Kaffee? Ist schon eine Weile her. Weißt du, ich dachte, du wärst tot, weil du dir mit dem Paket so viel Zeit gelassen hast."


hi "Sei froh, dass ich überhaupt bereit war, das Paket zu liefern, Klugscheißer!"


show kenji neutral onlayer master
with charachange

ke "Whoa, beruhig dich. Mann, bist du streitlustig. Liegt es an der Sache mit dem Schülerrat? Ich habe gehört, du hängst jetzt mit denen rum."


hi "Du hast es von mir gehört. Als ich es dir erzählt habe."


ke "Echt?"


ke "Ja, also, egal, Mann. Der springende Punkt ist: Sie sind schrecklich."


show kenji tsun onlayer master
with charachange

ke "Du bist der Neue, natürlich kannst du das nicht wissen, aber sie ist eine sehr polarisierende Gestalt. Bevor du hierherkamst, hat sie versucht, eine Abzeichenregelung einzuführen. Lange Geschichte. Vielleicht solltest du dich setzen."


"Ich schaue mich nach einem Stuhl um, finde aber keinen, weil wir in einem verdammten Flur stehen. Ich hebe den Finger, um ihm das zu sagen, aber er hat schon angefangen zu erzählen."
"Um die Armbewegung nicht zu verschwenden, werfe ich einen Blick auf die Uhr."


ke "Es wäre eine wahre Schreckensherrschaft geworden, wenn es so gekommen wäre."


hi "Moment, du verurteilst sie für etwas, das nicht einmal passiert ist?"


stop music fadeout 8.0

ke "Ja. Jedenfalls ging es in ihrer Idee um Verdienstabzeichen, es hätte aber auch Strafabzeichen gegeben."


hi "Wozu wären die gut gewesen?"


show kenji neutral onlayer master
with charachange

ke "Ich weiß nicht, es ist nie umgesetzt worden. Schien aber eine böse Sache zu sein. Als ich davon hörte, habe ich ein paar Wochen lang nicht mehr mein Zimmer verlassen."


hi "Du hast also mitbekommen, dass es eine massive Veränderung geben soll und dich in deinem Zimmer versteckt, um sie auszusitzen."


show kenji tsun onlayer master
with charachange

ke "Nee, ich hatte mich entschieden, etwas dagegen zu unternehmen."
ke "Nach einer Weile fand ich das Büro des Schülerrats und marschierte mit einer Liste Forderungen und einem Haufen Leute hinein, die ich mir geschnappt hatte, damit es so aussieht, als hätte ich Unterstützer."


hi "Moment, es ist also nicht nur gar nicht passiert, es hat nicht einmal jemanden interessiert?"


show kenji rage onlayer master
with charachange

play music music_tension

"Kenji hört mich nicht, da er richtig in Fahrt gekommen ist. Aufgestachelt von seinem eigenen Gegeifer beginnt er, komplett auszuflippen und wild mit den Armen zu rudern, was aussieht wie die Erkennungszeichen von Gangs."


ke "Ich bin zu ihrem Schreibtisch und meinte: „Hey, du Faschistin! Was soll das mit den Abzeichen? Wie weltfremd bist du eigentlich in deinem Elfenbeinturm? Schaust selbstgefällig auf uns herab, als wären wir ein Haufen Trottel?"
ke "Was glaubst du, wer du bist?”"


ke "„Der Grad deines elitären Denkens ist schrecklich, du bist bestimmt einer dieser abgehobenen reichen Snobs mit Chauffeuren, die sie in Slums fahren, damit sie auf den Abschaum zeigen und ihn auslachen können…”"


ke "„… und nur kostspielige Kaffeebohnen trinken, die von den letzten lebenden Dinosauriern ausgeschissen und dann in einem Schädel aus massivem Gold aufgebrüht wurden.”"


ke "„Und wie konntest du? Geh und schlag ein Geschichtsbuch auf; weißt du nicht, dass das Bürgertum für solchen Scheiß immer in blutigen Revolutionen gestürzt wird? Dumm! Du bist eine Idiotin!”"


ke "„Klar, normalerweise schaffen die Revolutionäre am Ende nur ein heilloses Riesenchaos, aber Fanatiker sind die Einzigen, die eine Regelung wie diese entwerfen würden…”"


ke "„… So etwas würde man nur erschaffen, damit die Menschen leiden müssen, nur dass es real ist und du es zu einer Institution machen willst! Wo soll die Schändung unserer Rechte enden? Wir sind Menschen! Das ist keine Gerechtigkeit!”"


show kenji neutral onlayer master
with charachange

ke "Das habe ich gesagt."


show kenji rage onlayer master
with charachange

ke "Dann hab ich noch schreiend hinzugefügt: „Sie können uns unsere Sachen nehmen, aber nicht unsere Freiiiiiiheiiiiiit!”, um die Massen zu mobilisieren."
ke "Wie in dem Film über das Leben von William Wallace, wo sie ihm seine Sachen nahmen, aber nicht seine Freiheit, und ihn dann umbrachten."


stop music fadeout 5.0

show kenji tsun onlayer master
with charachange

ke "… Aber sie hat mich einfach ignoriert und nicht einmal von ihrem kleinen Papier-Scheiß aufgesehen."


ke "Vielleicht habe ich sie so sehr mit meiner Logik überwältigt, dass sie sich in Verleugnung flüchten musste. Vielleicht ist sie nur ein Arschloch. Jedenfalls hat sie nicht geantwortet und die Zukunft konnte nicht verändert werden."


ke "Zu allem Überfluss habe ich auf dem Rückweg gemerkt, dass ich meinen Schülerausweis irgendwo verloren hatte."
ke "Das ist meine Lebensgeschichte. Ein ewiger und scheinbar sinnloser Kampf. Wie der Versuch, eine Ziegelmauer mit Schwämmen an den Händen zu erklimmen."


hi "Hey, du hast gesagt, nichts habe sich verändert, aber sie hat niemanden gezwungen, diese dämlichen Abzeichen zu tragen. Also hat sich etwas verändert."


play music music_kenji fadein 0.5

show kenji happy onlayer master
with charachange

ke "Ja, das stimmt. Okay, dann sind sie vielleicht doch nicht so übel."


"Ich glaube, das hat etwas zu bedeuten, wenn ich Kenji dazu bringe, zuzugeben, dass zwei Frauen vielleicht doch nicht so übel sind."
"Ich werde das so hinnehmen. Besonders weil ich so aus diesem Gespräch aussteigen kann; ich habe nicht bemerkt, wie viel Zeit verstrichen ist."


stop music fadeout 2.0

scene bg school_dormext_full onlayer master
with locationchange

"Ich versuche, meine Morgenroutine so schnell es geht durchzuziehen. Als ich das Wohnheim verlasse, schaue ich noch einmal auf meine Uhr und sehe, dass ich bereits zu spät bin."


scene bg school_scienceroom onlayer master
with shorttimeskip

play music music_daily fadein 1.0

"Zum Glück verläuft der Rest des Tages entspannter, und nach Schulschluss treffe ich mich wieder mit Shizune."


scene bg school_gardens2 onlayer master
with locationskip

"Hinter dem Schulgebäude sehe ich sie an einer fertigen Bude lehnen, die teilweise noch mit Papier- und Leimresten gesprenkelt ist – Überreste von ihrer letzten Benutzung."
"Geistesabwesend wirbelt sie einen Nagel in ihrer Hand und hat mich noch nicht bemerkt."


"Der Drang, mich anzuschleichen, ist unwiderstehlich. Jahrelanges Studium von Tierdokumentationen hat mich auf diesen Augenblick vorbereitet."
"Ich bin in Windrichtung, die Bedingungen sind hervorragend. Aber je mehr ich darüber nachdenke, desto schlechter kommt mir mein Einfall vor."


"Wenn sie mich auf halbem Weg entdeckt, stehe ich da wie ein Depp, und wenn sie nicht weiß, dass ich es bin, ende ich mit einer Verletzung."
"So oder so würde ich auch etwas unsensibel wirken. Am besten, ich versuche nichts Lustiges… so enttäuschend es auch ist."


show shizu adjust_blush onlayer master at center
with charaenter

"Ich laufe auf sie zu, wodurch sie ein wenig aufschreckt."


his "Warum so überrascht? Habe ich dich beim Blaumachen erwischt?"


show shizu behind_blank onlayer master
with charachange

ssh "Nein, ich habe nur eine Pause gemacht."


his "Du siehst nicht so aus, als wärst überhaupt ins Schwitzen gekommen. Das ist doch mal eine Pause, Präsidentin."


show shizu behind_frustrated onlayer master
with charachange

"Shizunes Augen huschen hin und her. Ich habe es wohl hinbekommen, sie durcheinander zu bringen."


"Ihr Gesichtsausdruck zeigt Verärgerung und auch ein bisschen Nervosität, aber nachgeben kann sie nicht; das wäre für sie undenkbar. Ihre ineinander gekreuzten Finger tanzen ungeduldig."


show shizu basic_normal2 onlayer master
with charachange

ssh "Du verhältst dich heute ziemlich herausfordernd. Willst du mich zur Weißglut treiben? Willst du einen Wettkampf? Wir werden ackern, um zu sehen, wer bis Sonnenuntergang die meisten Buden aufgebaut hat."


his "Nein, nein! Ich ziehe dich auf. Schon gut, es wäre ja kein richtiger Schülerrat, wenn man nicht die Schülerratspräsidentin aufziehen kann. Stimmt doch, oder?"


show shizu behind_frown onlayer master
with charachange

ssh "Das steht nicht in der Satzung des Schülerrats, also stimmt es nicht."


his "Es gibt keine Satzung!"


"Zumindest glaube ich das. Das Einzige, dem sie Treue schwören, ist ein Stapel Menüs zum Mitnehmen."


show shizu adjust_smug onlayer master
with charachange

ssh "Jedenfalls gut, dass du endlich hier bist, obwohl du schon eher hättest auftauchen können. Schnapp dir einen Hammer und wir machen da weiter, wo wir aufgehört haben."


hide shizu onlayer master
with charaexit

play ambient sfx_stallbuilding fadein 0.5

"Bei der heutigen Montage fällt mir langsam auf, dass es weitaus weniger Arbeit ist als erwartet. Mit etwas Glück könnten wir, wie Shizune gemeint hat, tatsächlich schon am Ende des Tages fertig sein."


"Als ich diese Arbeit das letzte Mal für die zwei erledigt habe, haben sie, Misha und ich fast vier Tage gebraucht. Das kann doch nicht nur Einbildung sein."


stop ambient fadeout 2.0

his "Weißt du, es scheint gar nicht so viel Arbeit zu sein."


show shizu behind_blank onlayer master at center
with charaenter

ssh "Ist es auch nicht."


play ambient sfx_parkambience fadein 10.0

"Die Antwort schreit nach mehr. Weil der Hammer jetzt nicht gerade hilfreich ist, legt sie ihn beiseite, um die Sache ausführlicher darzulegen."


show shizu basic_happy onlayer master
with charachange

ssh "Für zwei Personen wäre es unmöglich, so viel Arbeit in weniger als zwei Wochen zu schaffen. In Wahrheit demontiere ich die Hälfte der Buden nicht, sondern lagere sie irgendwo. Na ja, eher verstecke ich sie vor aller Augen."


show shizu adjust_smug onlayer master
with charachange

"Sie wackelt verschmitzt mit dem Finger."


show shizu adjust_happy onlayer master
with charachange

ssh "Das ist aber ein Geheimnis und es wäre unangemessen, alle Tricks und Kniffe zu enthüllen."


his "Du bist keine Zauberin."


show shizu behind_smile onlayer master
with charachange

"Zwinkernd zieht sie zwei Plastikbehälter aus ihrer Tasche und stellt sie auf ein nahegelegenes Brett, bevor sie die Arme anhebt, als wolle sie sagen: „Ta-da!”"


show shizu adjust_happy onlayer master
with charachange

ssh "Heute habe ich für uns beide Mittagessen gemacht."


show shizu behind_smile onlayer master
with charachange

ssh "Du kannst das hier haben. Das Essen ist in der Tasche verrutscht und jetzt teilweise vermischt."


"Sie übergibt mir einen Behälter. Ich öffne ihn. Sieht einfach aus, aber lecker. Sie reicht mir ein Paar Essstäbchen, als wären sie ihr gerade wieder eingefallen, und ich probiere von dem, was aussieht wie gegrilltes Rindfleisch."


his "Schmeckt echt gut."


his "Magst du es nicht, wenn dein Essen mit anderem in Berührung kommt?"


show shizu basic_normal onlayer master
with charachange

ssh "Tue ich nicht."


his "Ganz schön wählerisch."


show shizu behind_blank onlayer master
with charachange

ssh "Manchmal mische ich mir meine Mahlzeiten selbst, aber nicht immer und nicht alles. Ich mag es nicht, wenn man es für mich mischt. Wichtig ist, dass man eine Wahl hat."


show shizu basic_normal onlayer master
with charachange

"Sie richtet energisch den Zeigefinger auf, um das Gesagte zu unterstreichen, bricht dann die Essstäbchen auseinander und fängt an zu essen."


"Während ich weiteresse, fallen mir zwei Dinge auf. Erstens ist alles außer dem Reis frittiert. Sogar das Gemüse ist frittiert."


"Und es gibt sehr viel Fleisch. Ist sie so etwas die ganze Zeit? Ich frage mich, wie sie trotz dessen so schlank bleiben kann."


"Zweitens kann ich während des Essens nicht mit ihr reden. Mit vollem Mund zu sprechen ist sowieso etwas unhöflich, aber da unsere Hände voll mit Essstäbchen und Schüsseln sind, ist eine Kommunikation ausgeschlossen. Genau wie gestern."


"Obwohl wir Zeit miteinander verbringen und ich mir Zeit fürs Lernen der Gebärdensprache genommen habe, kommt es mir vor, als würde ich weniger mit ihr sprechen. Allerdings glaube ich, sie auch besser zu verstehen."


stop music fadeout 4.0

show shizu basic_normal onlayer master at tworight
show bg school_gardens2 onlayer master at bgright
with charamove

show lilly cane_smileclosed onlayer master at twoleft
with charaenter

"Ich höre eine Art Klopfen an einem der Stände, und als ich den Kopf hebe, sehe ich, wie sich Lilly mit ihrem Gehstock ihren Weg zu uns ertastet."


hi "Hi."


"Fast wäre mir ein „Hab dich gar nicht gesehen” herausgerutscht."


show lilly cane_surprised onlayer master
with charachange

li "Oh, Hisao, bist du das? Ich dachte, ich hätte den angenehmen Geruch einer gekochten Mahlzeit wahrgenommen, und habe mich gefragt, wer das sein mag."


show shizu behind_frustrated onlayer master
with charachange

ssh "Was sagt sie?"


play music music_happiness fadein 6.0

"Es ist schwierig, meine Hände zu bewegen, während ich zu Lilly etwas völlig Anderes sage. Das muss der Grund sein, warum Misha die ganze Zeit gleich alles übersetzt. Wirkt zwar etwas idiotisch, vereinfacht die Sache aber bestimmt sehr."


show shizu basic_happy onlayer master
with charachange

"Bei meiner Übersetzung formt Shizune ihre Finger entzückt zu einem Zelt, als hätte sie einen Witz gehört."


show shizu adjust_smug onlayer master
with charachange

ssh "Das ganze Essen wurde schon vor Stunden gekocht, aber wenn jemand so langsam ist wie du, die noch nicht einmal ein Stück Papier ohne eine Woche Verspätung abgeben kann, läuft die zeitliche Wahrnehmung wahrscheinlich etwas anders ab!"


hi "Das… ist nicht sehr nett."


show lilly cane_displeased onlayer master
with charachange

"Über Lillys Gesicht huscht ein Stirnrunzeln als Reaktion auf eine Antwort, die sie nicht hören konnte."


hi "Ah, tut mir leid. Wir essen nur unser verspätetes Mittagessen. Die Präsidentin des Schülerrats hat alles gekocht."


show lilly cane_reminisce onlayer master
with charachange

li "Ist die Präsidentin des Schülerrats jetzt gerade hier?"


hi "Ist sie."


show lilly cane_listen onlayer master
with charachange

li "Entschuldigung, das habe ich nicht bemerkt. Normalerweise ist ihre Präsenz deutlich stärker zu spüren."
li "Mir war gar nicht bewusst, dass der Schülerrat heute Mittagessen draußen anbietet, warum wurde ich nicht eingeladen? Aber es ist sicher schön, wenn man genug Zeit für so etwas hat."


show shizu behind_frustrated onlayer master
with charachange

ssh "Was sagt sie?"


"…"

show shizu basic_angry onlayer master
with charachange

ssh "Wenn ich dich irgendwohin einlade, würdest du ja doch nur zu spät kommen."


"Aber Shizunes Worte liegen außerhalb von Lillys Wahrnehmung und diese Tatsache treibt sie nur noch mehr in den Wahnsinn."


show shizu behind_frown onlayer master
with charachange

ssh "Bitte übersetz das für mich vollständig."


"Welch höfliche Wortwahl. Schade, dass sie mich im Grunde genommen bittet, die Kriegshunde von der Leine zu lassen."
"Ich kann aber auch nicht nichts tun. Es ist ein isolierendes Gefühl, dass man nicht einmal etwas erwidern oder verstanden werden kann. Das würde sie mir nie verzeihen."


"Ich werde einfach versuchen, ihre Worte ein bisschen abzumildern."


hi "Nun, eigentlich wurde das alles schon vor einer ganzen Weile gekocht."


show lilly cane_weaksmile onlayer master
with charachange

li "Wirklich? Wie schön."


show shizu cross_angry onlayer master
with charachange

ssh "Dreh dich hierher, es ist äußerst respektlos, den Gesprächspartner nicht anzusehen. Das ist nicht die feine Art, wie sich eine geschniegelte und gestriegelte Lady aufführen sollte."


hi "Die Hälfte von dem, was ich sage, stammt wirklich von Shizune. Sie mag es nicht, wenn man sie nicht ansieht, wenn sie versucht, etwas klarzustellen. Sie ist, äh, genau rechts von meiner Stimme."


"Dennoch kann ich verstehen, warum Lilly es nicht tut. Dies ist eine äußerst heikle Situation und das einzige Verbindungsglied für einen Dialog zwischen den beiden zu sein, macht nicht gerade Mut."


"In Wahrheit hatte ich total vergessen, was beim letzten Mal passiert ist, als sie so wie gerade die Messer wetzten. Es ist offensichtlich, dass sich Shizune erinnert, doch auch Lilly verhält sich auf ihre Art feindselig."


show lilly cane_displeased onlayer master
with charachange

li "Es tut mir leid, derartige Formalitäten sind mir vollkommen entfallen. Ich vergaß, dass die Präsidentin des Schülerrats zu der Sorte Menschen gehört, die solchen Respekt beansprucht und sich jederzeit an die Regeln hält."


show lilly cane_listen onlayer master
with charachange

li "Vermutlich musst du als Schülerregentin den Laden fest im Griff haben. Andererseits hat sie gewiss auch Zeit für ihren Spaß, also kann das nicht ganz stimmen."


show shizu adjust_angry onlayer master
with charachange

ssh "Der Schülerrat ist weder eine Diktatur noch ein Nullsummenspiel!"


play sound sfx_snap

"Shizune streckt Lilly den Zeigefinger wie den Lauf einer Pistole entgegen und schnippt explosiv mit den Fingern, worauf Lilly zurückweicht und sichtbar verärgert reagiert."


show lilly back_listen onlayer master
show lillyprop back_cane onlayer master at twoleft
with charachange

li "Ach so? Dann ist es noch beeindruckender, dass du schon so lange dazugehörst und so tust, als wäre es eins. Ich bewundere deine Hartnäckigkeit. Um alles zu bewältigen, musst du ebenfalls sehr verantwortungsbewusst sein."


show shizu behind_frown onlayer master
with charachange

ssh "Nicht so sehr, wie ich es gern wäre. Du kannst dich aber auch nicht über dich beklagen, stimmt's?"


show shizu cross_rage onlayer master
with charachange

ssh "Du bist sehr verantwortungsbewusst; Aktionen wie die, eine Abgabefrist zu verlängern, nur um dann wieder vor der Nächsten zu stehen? Das ist das perfekte Beispiel für Verantwortungsbewusstsein!"


hi "Shizune freut sich, das zu hören. Aber du scheinst auch ziemlich verantwortungsbewusst zu sein, meint sie."


show lilly cane_surprised onlayer master
hide lillyprop onlayer master
with charachange

li "Meint sie das wirklich?"


hi "Mehr oder weniger…"


"Lilly scheint nicht sehr zufrieden zu sein."


hi "Wir halten hier kein Kaffeekränzchen ab, das ist nur eine kleine Mittagspause. Eigentlich bauen wir hier draußen die Buden für das Fest auf."


show shizu behind_frown onlayer master
with charachange

ssh "Woher sollst du es auch wissen, wo du nie rausgehst. Ist dir der Tee ausgegangen?"


hi "Gehst du ins Dorf? Einkaufen?"


show lilly back_devious onlayer master
show lillyprop back_cane onlayer master at twoleft
with charachange

li "Nein. Wie ich zuvor sagte, bin ich bloß vorbeigegangen, nur falls du es nicht gehört hast. Ich würde ungern die Präsidentin des Schülerrats unterbrechen. Ihr macht zwar jetzt nichts, müsst aber sehr beschäftigt sein."


show lilly cane_listen onlayer master
hide lillyprop onlayer master
with charachange

li "Auf jeden Fall, Hisao, bin ich mir sicher, dass die Präsidentin des Schülerrats in der Lage ist, wenn nötig für euch beide Arbeit zu finden oder zu machen."


show shizu cross_rageclosed onlayer master
with charachange

ssh "Ich fress dich auf!"


hi "Jepp, sehr beschäftigt."


"„Auffressen” ist ein schwieriges Wort. Ich bin erleichtert, dass ich es verstehen kann. Dennoch keine Zeit zum Feiern, nicht wegen so etwas. Vielleicht hören sie stattdessen mit dem Gekabbel auf. Darauf würde ich trinken."


show lilly cane_listen onlayer master
with charachange

li "Einen schönen Tag noch, Hisao. Auf Wiedersehen, Präsidentin des Schülerrats."


hi "Danke, dir auch."


show shizu basic_frown onlayer master
with charachange

ssh "Schön elegant bleiben."


hide lilly onlayer master
with charaexit

show shizu basic_normal2 onlayer master at center
show bg school_gardens2 onlayer master at center
with dissolvecharamove

stop music fadeout 4.0

"Als Lilly uns verlässt, stürzt sich Shizune so schnell es geht auf die Überreste ihres Mittagessens, als sei jeder Bissen ein Mittel, um zu vergessen, was hier eben alles geschehen ist."


hide shizu onlayer master
with charaexit

"Als sie alles hintergeschaufelt hat, kehrt sie mit der gleichen Einstellung geradewegs zur Arbeit zurück. Schön, dass sie sich den Frust weghämmert, aber sie ist sicher nicht mehr in der Stimmung zum Reden."


show bg school_gardens2_ss onlayer master
with shorttimeskip

play music music_tranquil fadein 3.0

"Ungefähr zwei Stunden später hört sie auf, nachdem sie in der Zeit nonstop alle Buden durchgegangen ist."


"Ich fühle mich immer noch unwohl dabei, sie anzusprechen. So leicht kann ein Gespräch abebben. Nachdem es so lange gedauert hat, allein und direkt mit ihr zu sprechen, tut das fast weh."


show shizu basic_normal_ss onlayer master at center
with charaenter

ssh "Deine Übersetzung war gut."



his "Wirklich?"


show shizu adjust_happy_ss onlayer master
with charachange

ssh "Erste Sahne!"


"Ihr Daumen geht hoch, um das zu unterstreichen."


show shizu behind_blank_ss onlayer master
with charachange

ssh "… für dein Niveau."


show shizu basic_normal_ss onlayer master
with charachange

ssh "Viele taube Leute gibt es an der Schule nicht und die Gebärdensprachkurse stehen schon seit einer Weile am Rande der Streichung. Du hast sicher nicht viele Klassenkameraden, oder?"


show shizu behind_blank_ss onlayer master
with charachange

ssh "Wenn man Gebärdensprache erst in diesem Alter lernt, ist die Geschwindigkeit begrenzt. Darum schwindet das Interesse, weil einfache Kommunikation viel aufwändiger ist als sonst. So ist es wohl bei allen Sprachen."


show shizu basic_normal2_ss onlayer master
with charachange

ssh "In so einem Fall sind Gespräche in Gebärdensprache weniger … als sie es im Normalfall wären."


his "Das Wort verstehe ich nicht. Weniger was?"


show shizu behind_blank_ss onlayer master
with charachange

show shizu basic_normal2_ss onlayer master
with charachange

ssh "Sp—{w=0.2}o—{w=0.2}n—{w=0.2}t—{w=0.2}a—{w=0.2}n."


show shizu behind_blank_ss onlayer master
with charachange

ssh "Misha ist die Einzige, die die Sprache wirklich erfasst."


his "Jepp, das ist absolut richtig."


show shizu behind_sad_ss onlayer master
with charachange

show shizu behind_blank_ss onlayer master
with charachange

"Ihr Gesichtsausdruck ändert sich für einen Moment, verschwindet jedoch zu schnell, um ihn deuten zu können. Ich glaube, da sollte ich besser nicht nachhaken."


"Was ich mich wirklich interessiert, ist…"


his "Warum streitet ihr Zwei euch so viel?"


show shizu basic_frown_ss onlayer master
with charachange

"Angespannt und mit deutlich gerunzelter Stirn faltet und überlappt Shizune ihre Finger immer wieder, als würde sie einen unsichtbaren Kartenstapel durchmischen."


show shizu behind_frustrated_ss onlayer master
with charachange

ssh "Die zwei Streitereien, die du kennst, sind es gar nicht wert, „so viel” genannt zu werden. Wenn du letztes Jahr hier gewesen wärst, könntest du das behaupten."


his "Ich habe gehört, es war ein hartes Jahr. Irgendwas davon, wie du versucht hast, eine Abzeichenregelung einzuführen."


show shizu cross_wut_ss onlayer master
with charachange

his "Ha ha, überrascht? Tja, darüber möchte ich später auf jeden Fall mehr wissen, aber… du magst Lilly nicht besonders, oder? Weich nicht meiner Frage aus."


show shizu behind_frustrated_ss onlayer master
with charachange

ssh "Ich weiche überhaupt nichts aus."


show shizu basic_angry_ss onlayer master
with charachange

ssh "Sie war bis letztes Jahr Teil des Schülerrats. Wir sind nicht sehr gut miteinander zurechtgekommen. Sie wollte so weitermachen wie der alte Schülerrat. Der war einfach so ineffektiv. Er war dumm und unverschämt."


show shizu behind_frown_ss onlayer master
with charachange

ssh "Ich wollte mehr bewerkstelligen und so kam es zum Streit."


show shizu basic_frown_ss onlayer master
with charachange

ssh "Zu vielen Streitereien."


show shizu adjust_angry_ss onlayer master
with charachange

ssh "Sie hat nichts rechtzeitig auf die Reihe gekriegt."


show shizu behind_frustrated_ss onlayer master
with charachange

ssh "Dann hat sie gemeint, was ich vorhabe sei sinnlos und bloß Freizeitbeschäftigung. Sieht das hier für dich wie sinnlose Freizeitbeschäftigung aus?"


"Shizune gestikuliert energisch."


show shizu basic_frown_ss onlayer master
with charachange

ssh "Wirklich sinnlos ist doch ein Schülerrat, der gar nichts tut. Schwach, träge und langweilig. Insbesondere langweilig!"


show shizu adjust_angry_ss onlayer master
with charachange

ssh "Tatenlos im Büro zu sitzen empfinde ich nicht als spannend, sondern als Zeitverschwendung. Warum wäre ich dann hier? So etwas bringt mein Blut nicht in Wallung. Mit ihr zu diskutieren hingegen schon!"


show shizu behind_blank_ss onlayer master
with charachange

ssh "Wenn sie vorher auch so motiviert gewesen wäre, müsste sie jetzt nicht so viel Einsatz als meine Feindin zeigen. Aber wenn sie ein derartiges Temperament zeigt, ist sie noch nicht ganz verloren. Das ist doch was! Das ist immerhin noch spannend."


his "Verstehe."


his "Und was ist mit der Geschichte mit den Abzeichen?"


show shizu adjust_happy_ss onlayer master
with charachange

stop music fadeout 4.0

"Sie lacht und bedeckt ihren Mund mit der Hand, als wolle sie es verstecken. Ihr Lachen ist das Einzige, was sie oft zu verbergen versucht."


show shizu behind_smile_ss onlayer master
with charachange

ssh "Das war doch nur ein Witz."


show shizu adjust_happy_ss onlayer master
with charachange

ssh "Manchmal etwas Spaß zu haben ist auch wichtig."


stop ambient fadeout 0.5

scene black onlayer master
with dissolve



label de_S15:

scene bg school_dormext_full onlayer master
with locationchange

play music music_normal fadein 0.5

"Am nächsten Tag, bin ich zu Beginn der Mittagspause dabei, die Gegend zu durchzuforsten, weil meinem Lieblingsautomat bei den Schlafräumen mein Lieblingsdosenkaffee ausgegangen ist. Der Umweg dauert doch länger als ich dachte."


scene bg school_gardens onlayer master
with locationchange

"Es ist in letzter Zeit so hektisch geworden, dass ich eine Weile brauche, um zu merken, warum auf meinem Rückweg durch den Schulgarten zur Cafeteria ein anderer Geruch in der Luft liegt. Das Gras ist frisch gemäht worden."


"Eine Erkenntnis, die mich innehalten lässt, um mich ein wenig umzusehen."
"Eine komische Gruppe Studenten, die auf dem Rasen spielt oder plaudert, und zwei Lehrer inmitten eines Gesprächs auf dem Pfad vor mir sorgen für eine äußerst idyllische Szene."


stop music fadeout 2.0

"Leider kriecht nach einer Weile ein Gefühl unmittelbarer Bedrohung in mir hoch. Das Gefühl, nicht allein zu sein."


play music music_kenji fadein 0.5

show kenji neutral onlayer master at center
with charaenter

ke "Hey, Hisao, bist du's?"


hi "Ja, ich bin's."


"Ich sollte wohl glücklich sein, dass er es ist und kein, sagen wir, Messerstecher. Kenji beginnt so zu reden, als würde er das Gespräch mit jemand anderem als mir führen."


show kenji happy onlayer master
with charachange

ke "Wusste ich's doch. Der Haarschnitt ist unverkennbar. Kein normaler Mensch würde so einen Haarschnitt tragen."


"Unbewusst fange ich an, mir über den Hinterkopf zu streichen. Als mir das bewusst wird, fühle ich mich beleidigt, wenn auch zu überrascht, um mich überhaupt darüber zu ärgern."


hi "Ja… Was machst du hier?"


show kenji neutral onlayer master
with charachange

ke "Temperaturmessungen."


show kenji happy onlayer master
with charachange

ke "Der Winter steht vor der Tür. Für Frauen ist es zu kalt, um rauszugehen und ihre Sex and the City-Picknicks zu veranstalten und dann in großen Trauben überfüllte Innenstädte noch mehr zu verstopfen."


ke "Wenn es soweit ist, sind die Männer wieder in der Lage, ungehindert durch die Straßen zu ziehen und ihr Territorium in Anspruch zu nehmen."


show kenji neutral onlayer master
with charachange

ke "Zur Vorbereitung auf jenen Tag habe ich seit letzter Woche nichts außer Pizza gegessen, um Energie zu tanken."


hi "Okay."

hi "Bären machen das so."


show kenji happy onlayer master
with charachange

ke "Echt? Es gibt viel, das wir von den Bären lernen können."


"Kenji nickt, um sich mit Nachdruck selbst zuzustimmen."


show kenji neutral onlayer master
with charachange

ke "Okay, hör dir diesen Scheiß an: Ich war heute im Dorf und habe Milch gekauft. Sie hatten eine neue Angestellte, so ein Hipster-Mädchen mit Basecap und darauf zwei Hockeyschläger. Ich nenne es das „Hipster-Hockey-Basecap-Mädchen”."


ke "Mir fiel auf, dass der Milch das Preisschild fehlte, also teilte ich ihr mit, sie solle rüberkommen und die Milch kennzeichnen – für zukünftige Generationen."


"Er war heute im Dorf? Dann muss er den Unterricht am Morgen geschwänzt haben. Ich will ihn zurechtweisen, aber sein Redeschwall lässt mich nicht zu Wort kommen."


show kenji tsun onlayer master
with charachange

ke "Sie meinte zu mir, ich solle sie in Ruhe lassen, weil sie krank ist."
ke "Krank? Krank!? Wir leben hier in einer Gesellschaft. Man kann nicht einfach so aus einer menschlichen Interaktion aussteigen, weil man krank ist. Weißt du, wie viel Mühe es mich allein gekostet hat, heute früh aufzustehen?"


show kenji rage onlayer master
with charachange

ke "Also ich schon, und ich bin diesen Morgen aufgestanden, um hinunter zu gehen und Milch zu kaufen."
ke "Nicht um meine lebensnotwendigen Fragen wegwischen zu lassen, von so einer Hipster-Idioten-Studentin, die eine {b}Hockeybasecap{/b} auf Arbeit trägt. {b}Drinnen{/b}."


show kenji tsun onlayer master
with charachange

ke "Dabei habe ich nur versucht, die Richtigkeit ihrer Waren aufrecht zu erhalten. Eine Milchpackung ohne Preisschild? Wenn ich so etwas sehe, führt das einfach zu Fragen. Wichtigen Fragen. Es ist ihr Job, sie zu beantworten, verdammt."


ke "Das ist das Problem mit den Frauen, kein Pflichtbewusstsein."


show kenji neutral onlayer master
with charachange

ke "Ich leide oft an Durchfall, aber ich beschwere mich nicht. Ich rackere unermüdlich weiter und tue, was getan werden muss, denn das ist es, was einen Mann ausmacht. Auch mit Durchfall muss man weitermachen, für den Traum einer besseren Zukunft."


hi "Weißt du, häufiger Durchfall ist eine üble Sache."


hi "Viellicht solltest du aufhören, so viel Milch zu trinken."


ke "Das geht nicht. Nur damit kann ich meine unglaubliche Stärke beibehalten. Und in dieser Welt… ist die männliche Stärke das Einzige, das sich nicht von dieser Fotzenknecht-Gesellschaft einschüchtern lässt."


show kenji happy onlayer master
with charachange

ke "Das ist der Grund, warum ich überall herumlaufe und offene Einmachgläser mit Oliven stehen lasse. Manchmal nur, um zu zeigen, dass ich's kann."


hi "Kühlst du sie nach dem Öffnen?"


show kenji tsun onlayer master
with charachange

ke "Was? Mann, keine Ahnung, das ist unwichtig."


hi "Nach dem Öffnen musst du tiefkühlen. Jedes Kind weiß das."


show kenji neutral onlayer master
with charachange

ke "In erster Linie müsste man dazu erst einmal das Glas aufbekommen, also egal."


hi "Ah, das stimmt."


show kenji happy onlayer master
with charachange

ke "Ich bin genial."


"Er reibt sich selbstbewusst das Kinn, was ich eher von einem Wissenschaftler erwartet hätte, bis ich Mutou traf und gewaltig enttäuscht wurde."


show kenji neutral onlayer master
with charachange

ke "Auf jeden Fall kann ich nicht wieder zurück in dieses Geschäft, da es ganz klar von Schlampen kompromittiert wurde. Außer… ich verkleide mich. Vielleicht, indem ich eine andere Brille aufsetze."


hi "Die schlechteste Verkleidung aller Zeiten."


show kenji tsun onlayer master
with charachange

ke "Pffft, in all den Jahren hat's bisher einwandfrei geklappt. Eigentlich brauche ich keine Brille, um zu sehen. Sondern wegen des Effekts. Und um meine Identität zu wahren. Ich bin wie Superman."


hi "Die schlechteste Verkleidung aller Zeiten."


show kenji happy onlayer master
with charachange

ke "Ich sag dir mal was: Wenn die Leute meinen Studentenausweis sehen, erkennen sie mich nicht einmal."


hi "Echt? Darf ich mal sehen?"


show kenji neutral onlayer master
with charachange

ke "Das geht nicht. Ich kann nicht durch die Gegend spazieren und jedem meinen Ausweis zeigen. Es ist lange her. Aus einer anderen Zeit. Ich hatte eine Hippiefrisur."


stop music fadeout 2.0

"Während ich versuche, mir das vorzustellen, nimmt Kenji die Brille ab."


$ ksgallery_unlock("evul kenji_glasses_closed")
scene evbg kenji_glasses onlayer master:
    truecenter
    subpixel True zoom 0.82
    acdc_warp 20.0 zoom 0.8
show evmg kenji_glasses_closed onlayer master at kenji_mg_out
show evfg kenji_glasses onlayer master:
    truecenter
    subpixel True zoom 1.0
    acdc_warp 20.0 zoom 0.8
with whiteout

play music music_friendship


"Nachdem die Brille fort ist, blinzelt er, was ihn noch müder erscheinen lässt, als er es sowieso schon ist."
"Er hatte recht: Er sieht wirklich ganz anders aus. So, als er hätte er jahrelang nicht geschlafen. Aber nicht so krass anders, als dass es eine gute Verkleidung abgäbe."


hi "Du brauchst mehr Schlaf."


$ ksgallery_unlock("evul kenji_glasses_frown")
show evmg kenji_glasses_frown onlayer master at kenji_mg_out
with charachange

ke "Quatsch."


hi "Du siehst aus, als hättest du's nötig."


$ ksgallery_unlock("evul kenji_glasses_normal")
show evmg kenji_glasses_normal onlayer master at kenji_mg_out
with charachange

ke "Unmöglich. Das sind die Augen eines Mannes, der viel gesehen hat. Schamanenaugen. Viel Furchtbares. Das kannst du dir nicht einmal vorstellen."


ke "Zum Beispiel, wie ich ein Flaschenschiff gebaut habe und sich meine Mutter draufgesetzt hat. Überall lagen blutige Fetzen Blumendruck herum. Das nenne ich Lebenserfahrung."


"Kenji sieht nicht sonderlich beängstigt aus, obwohl das für mich der erste von ihm geschilderte Vorfall gewesen ist, bei dem er allen Grund hätte, traumatisiert zu sein."


"Gerade erzählt er ungefähr 30 Grad links von an mir vorbei – er scheint also in der Tat nahezu blind zu sein. Ich wedle mit meiner Hand vor seinem Gesicht, ohne große Wirkung."


ke "Mann, ich hoffe, du hast gemerkt, dass ich nur Spaß mache."


"Ich lache, um so zu tun, als ob. Irgendwie ist es schwieriger als sonst, ihm in die Augen zu sehen."


show evmg kenji_glasses_closed onlayer master at kenji_mg_out
with charachange

ke "Ganz nebenbei – Menschen mit kleinen Augen tragen große Brillen."


hi "Das habe ich mal irgendwo gelesen. Dadurch wirken die Augen weniger perlenartig."


ke "Echt? Wusste ich gar nicht."


stop music
$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_scratch


scene bg school_gardens onlayer master
show kenji tsun onlayer master at center
with locationchange

$ renpy.music.set_volume(1.0, 2.0, channel="sound")

"Kenji setzt sich die Brille wieder auf. Komischerweise fühle ich mich erleichtert, bis mir einfällt, dass ich immer noch mit ihm zu tun habe, ob mit oder ohne Brille."


play music music_kenji fadein 2.0

ke "Na ja, jedenfalls… Dieses Künstler-Mädchen wollte mich mal porträtieren, glaube ich. Ich musste bestimmt fünf Mal mit ihr sprechen, bevor ihre Worte Sinn ergaben."


"Das muss dann wohl Rin gewesen sein."


hi "Wie hat sie ausgesehen?"


show kenji neutral onlayer master
with charachange

ke "Weiß nicht. Eine Frau mit Sandalen."


"Ich hatte auf etwas Genaueres gehofft, wie: „Sie hatte keine Arme.” Rin trägt zwar Sandalen, aber die Wahrscheinlichkeit, dass es noch eine andere freigeistige Künstlerin mit Sandalen außer ihr gibt, ist leider ziemlich hoch."


show kenji happy onlayer master
with charachange

ke "Sicher, ich habe daran gedacht. Eines Tages, wenn ich alle Zeugnisse meiner Existenz verbrannt habe, mag es in Ordnung gehen, ein Porträt zu hinterlassen, das die Leute an den Retter der Menschheit erinnert – als Vorlage für die Statue."


show kenji neutral onlayer master
with charachange

ke "Dann habe ich darüber noch weiter nachgedacht und musste ihr eine Abfuhr erteilen. Es war verlockend, aber sie wollte es für so ein Schulprojekt. Es wäre ausgestellt worden."


show kenji tsun onlayer master
with charachange

ke "Man hätte gefragt, wer ich sei, nur dass ich die Gesellschaft noch gar nicht gerettet habe. Das wäre sinnlos. Und wenn mich dann jemand erkannt hätte, hätte ich mich rechtfertigen müssen."


ke "Mit einer solchen Ereigniskette will ich nichts zu tun haben. Ich will nicht in irgendwelche krassen Situationen verwickelt werden. So ein Scheiß passiert ständig. Aufzufallen ist eine todsichere Methode, um auf einer Liste zu landen."


show kenji neutral onlayer master
with charachange

ke "Daher treffe ich diese Vorsichtsmaßnahmen, um die Menschen in meinem Alltagsleben zu blenden. Bis ich am Zug bin."


hi "Sicher."


hi "Welche Liste?"


ke "Es gibt viele Listen."


show kenji happy onlayer master
with charachange

ke "Was machst du hier überhaupt?"


hi "Nichts. Mich hat der Zufall hierher verschlagen."


ke "Passiert mir auch die ganze Zeit. Na, hoffe, es läuft es gut für dich. Ich glaube, ich gehe zurück in mein Zimmer. Ich muss noch den Fernseher programmieren, um meine Shows aufzunehmen."


hi "Du hast einen Fernseher?"


ke "Ja, komm doch mal rüber, wir können uns das Spiel anschauen. In HD."


stop music fadeout 4.0

hide kenji onlayer master
with charaexit

"Bevor ich nachhaken kann, wovon er redet, ist er fort. Er ging, wie er kam: mit null Rücksicht auf andere. Irgendwie erstaunlich."


"Jetzt, wo Kenji weg ist, widme ich mich wieder dem Schulgarten in all seiner Sommerpracht. Zwecklos, er hat die Stimmung ruiniert."


scene bg school_cafeteria onlayer master
with locationchange

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 1.0

"Als ich erschöpft aber lebendig zurück in die Cafeteria komme, habe ich vor, wieder mit Shizune zu Mittag zu essen. Sie sitzt schon mit Misha zusammen an einem Tisch."


"Wenn es jemand anderes wäre, wären sie zu weit weg, als dass ich sie hören könnte, aber das sind Shizune und Misha."


"Wenn ich wollte, könnte ich sie mühelos „belauschen.” Den Gedanken kann ich mir nicht verkneifen, aber ich beherrsche mich."


"Auch wenn es nur ein paar Tage waren, müssen sie viel aufzuholen haben. Ich tendiere dazu, sie einfach in Ruhe zu lassen, damit sie das tun können."


"Aber sie entdecken mich und winken mich sofort zu sich rüber."


show misha hips_grin onlayer master at twoleft
show shizu basic_normal onlayer master at tworight
with charaenter

stop ambient fadeout 5.0
play music music_shizune fadein 1.0

mi "Hi, Hicchan~!"

"Auch wenn es noch nicht sehr lange her ist, dass wir uns zuletzt gesehen haben, zucke ich zusammen, als ich ihre Stimme höre."


"In den letzten paar Tagen hatte ich vergessen, dass die Kommunikation mit Shizune fast vollkommen still verläuft. Und um mich darauf zu konzentrieren, es richtig zu machen, hatte ich sogar die Umgebungsgeräusche ausgeblendet."


"Na ja, ich werde mich schon wieder daran gewöhnen. Ich bin froh, dass sie wieder da ist."


show misha sign_smile onlayer master
with charachange

mi "Ich bin fertig mit dem Nachholen~! Gerade rechtzeitig~, ich werde das Fest nicht sausen lassen müssen. Wahaha~"


show shizu adjust_smug onlayer master
with charachange

ssh "Falls sie dir das wirklich aufzwingen würden, würde ich dich mit Schülerratsarbeit da rausholen."


show misha perky_confused onlayer master
with charachange

mi "Falls sie mir das wirklich aufzwingen würden, würdest du mich mit Schülerratsarbeit da rausholen~?"


hi "Das ist Machtmissbrauch."


show shizu behind_frown onlayer master
with charachange

shi "…"

show misha hips_frown onlayer master
with charachange

mi "Nein, das ist es nicht, Hicchan~!"


show misha sign_smile onlayer master
with charachange

mi "Shicchan sagt, dass es ein Problem wäre, wenn wir nur zwei Schülerratsmitglieder als Aufpasser beim Fest hätten, oder nicht? Ja~, absolut! Es müssen mindestens drei sein! Es ist zum Besten aller, es ist vollkommen logisch, es ist notwendig~!"


show shizu adjust_happy onlayer master
show misha perky_smile onlayer master
with charachange

"Shizune lehnt sich etwas über den Tisch, als Misha ihre etwas verstörenden und militanten Rechtfertigungen mit einer kindischen, quirligen auf-und-ab Stimme von sich gibt."


"Shizune sieht trotzdem sehr glücklich aus. Sie legt ihre Finger aneinander und versucht, sich ein Lachen zu verkneifen. Als Misha das sieht, fängt sie an zu schmollen."


hi "Wenn du das sagst."


"Eigentlich bin ich gerade glücklich darüber, dass wir so mühelos miteinander reden können. Wir alle drei."


"Am Anfang dachte ich, dass ich in einer schlechten Lage wäre. Ich war mir sicher, dass Shizune es hassen würde, die Reiseführerin für den Neuen spielen zu müssen."


"So eine Last wollte ich auch nicht sein. Selbst wenn sie nicht taubstumm wäre, wäre es ebenfalls unbehaglich."


"Gerade eben sagte sie, dass wir alle beim Festival sein müssten, der gesamte Schülerrat. Ich glaube nicht, dass der Schülerrat tatsächlich für Tanabata zuständig ist. Es ist lediglich Shizunes Art zu sagen, dass wir es zusammen feiern sollen."


"Es ist schön, Freunde zu haben."


"Ein simpler Gedanke, aber es macht mich wirklich glücklich, dass wir so einfach Freundschaft schließen konnten. Obwohl sie es durch die Blume sagte, bin ich froh, dass Shizune so davon überzeugt ist, dass sie es überhaupt zum Ausdruck bringt."


show shizu basic_normal onlayer master
with charachange

ssh "Warum hast du gewartet, bis wir dich zu uns rübergewunken haben, um dich zu uns zu setzen?"


"Eine plötzliche Frage. Shizune hat einen erwartungsvollen Blick, während Misha das Gestikulierte ausspricht. Ich habe Lust sie zu ärgern."


hi "Willst du so sehr, dass ich bei dir sitze?"


show shizu behind_blank onlayer master
with charachange

ssh "Wir sind im Schülerrat. Wir sollten so oft wie möglich zusammen sitzen. Ist doch logisch."


show shizu adjust_happy onlayer master
with charachange

ssh "Außerdem würde jeder die Gelegenheit ergreifen, bei zwei süßen Mädchen zu sitzen."


"Sie hält inne, damit ich etwas wie: „Du bist gar nicht so süß!” sagen könnte und mich in eine offensichtliche No-Win-Situation fahre. Als ich nicht darauf anspringe, wird Shizune energischer und fährt fort."


show shizu basic_happy onlayer master
with charachange

ssh "Du bist abnormal."


"Nun, ich habe nicht damit gerechnet, dass sie es damit abschließt."


hi "Bezeichne andere Leute nicht so vorschnell als abnormal. Das ist arrogant."


show shizu adjust_smug onlayer master
with charachange

ssh "Du nennst andere Leute vorschnell arrogant. Das macht dich wiederum arrogant, und Arroganz ist ebenfalls abnormal. Du bist doppelt abnormal."


hi "So funktioniert das nicht. Es gibt auch Graustufen."


show misha hips_grin onlayer master
with charachange

mi "Hahaha~."

"Während sie sich auf ihren Arm lehnt, schließt Misha ihre Augen und gibt ein leises, langsames Kichern von sich."


hi "Lach nicht…"


show shizu behind_blank onlayer master
with charachange

ssh "Lach bei so etwas nicht."


"Ich bemerke, dass Misha alles gebärdet, was ich zu Shizune sage, auch wenn ich es selbst tue. Es ist überflüssig, aber eine unbewusste Bewegung für Misha. Anderseits kann ich auch nicht aufhören."


"Wenn ich mich zurücklehne und weniger gebärde, nur weil Misha wieder da ist – wozu war das alles dann gut? Meine Gewöhnung an das Gebärden zu verlieren will ich genauso wenig riskieren. Meine Hände sind sowieso schon ziemlich langsam."


show misha sign_smile onlayer master
with charachange

mi "Hicchan, du und Shicchan redet jetzt viel mehr miteinander. Hin und her, es macht auch wirklich Spaß! Wie ein altes, verheiratetes Paar, stimmt's~ stimmt's~?"


"Auf vielerlei Arten eine verfängliche Bemerkung. Auch wenn es keine Absicht gewesen sein kann, da sie von Misha kommt."


hi "Das ist kein Kompliment."


"Shizune reagiert nicht auf Mishas Versuch, uns beide zu verkuppeln. Vielleicht hat sie es nicht gesehen. Auch das kommt ab und zu vor."
"Ich frage mich, ob es wirklich nur das ist, und warum ich mir so viele Gedanken darum mache. Aber ich will nicht allzu sehr darüber nachdenken."


"Ich will gehen. Ich habe weiterhin das Gefühl, dass ich Mishas Zeit mit Shizune raube, und es könnte sein, dass Misha das eingeworfen hat, weil sie das gleiche denkt."
"Allerdings bezweifle ich, dass die beiden mich gehen lassen werden. Für so etwas sind sie zu nett."


hi "Wie auch immer, Shizune, wenn du es wirklich wissen willst: Ich wollte mich nicht zu euch setzen, weil ich euch nicht stören wollte."


hi "Ich dachte, dass ihr beide viel zu bereden hättet, weil Misha wegen ihrer Nachhilfestunden weg war und ich euch lieber allein lassen sollte, damit ihr das nachholen könnt. Darum wollte ich mich zurückhalten."


hi "Keine Sorge, Misha, ich versuche nicht, Shizune für mich allein zu haben."


show misha cross_laugh onlayer master
with charachange

mi "Wahaha~! Hicchan! So ist es nicht~."


show shizu basic_normal onlayer master
with charachange

shi "…"


show misha hips_smile onlayer master
with charachange

mi "Du bist so rücksichtsvoll, Hicchan! Shicchan tut es leid~, und sie entschuldigt sich."


hi "Ich denke nicht, dass man sich deswegen entschuldigen müsste, also mach dir darum keinen Kopf. Hey, meint ihr beide nicht, dass wir feiern sollten, dass Misha wieder da ist? Ich schon."


show misha cross_frown onlayer master
with charachange

mi "Hicchan~! Normalerweise ist Arbeit nachholen zu müssen nicht etwas, das man feiern würde."


show shizu adjust_happy onlayer master
with charachange

ssh "Doch, es ist eine gute Idee."


hi "Das Timing ist perfekt, und Shizune hat gesagt, dass der Schülerrat manchmal auch etwas Spaß haben sollte. Du hast das doch auch gehört, oder, Misha? Es sollte klargehen."


show shizu behind_blank onlayer master
with charachange

shi "…"


hi "Obwohl, warte. Musstest du nicht Arbeit nachholen, weil du vorher so viel Unterricht verpasst hast? Dann wäre zu es dumm fürs Feiern zu schwänzen. Vielleicht ist der Zeitpunkt jetzt doch nicht so ideal, aber wir könnten nach der Schule gehen."


show misha sign_smile onlayer master
with charachange

mi "Wohin wollen wir?"


"Misha spricht Shizunes Frage laut aus, bevor sie sie überhaupt zu Ende formuliert hat. Beide ignorieren mich vollkommen."


hi "Hey, hört mir zu, ihr kurzsichtiges Schülerrats-Zweierteam!"


show shizu adjust_smug onlayer master
with charachange

shi "…"


show misha hips_grin onlayer master
with charachange

mi "Wahaha~! Hicchan, du gehörst doch auch zu diesem Team!"


hi "Ah, ja, schätze schon."


show misha hips_smile onlayer master
with charachange

mi "Ja ja~! Das tust du, Hicchan!"


show shizu behind_smile onlayer master
with charachange

ssh "Du bist vergesslich {b}und{/b} machst nur Ärger. Mir tut das Mädchen leid, das sich in dich verliebt."


show misha sign_smile onlayer master
with charachange

mi "Also~! Wo sollten wir deiner Meinung nach hingehen?"


"Ich muss unwillkürlich loslachen, und will anmerken, dass Misha, die eben noch die meisten Bedenken hatte, nun diejenige mit dem größten Enthusiasmus ist. Aus irgendeinen Grund kann ich mich nicht dazu überwinden. Aber das ist auch okay."


stop music fadeout 4.0

"Nach einer kurzen Diskussion über unser Ziel scheint das Shanghai der einzige Ort zu sein, den wir alle kennen und besuchen wollen."


"Ein Teehaus scheint kein allzu schlechter Ort zum Feiern zu sein, besonders weil ich mir sicher bin, dass sie dort Kuchen servieren – und mit Kuchen lässt es sich am besten Feiern."


scene bg suburb_shanghaiext onlayer master
with shorttimeskip

"Yuuko habe ich schon eine Weile nicht gesehen, genauso wenig wie die Mädchen. Aus all diesen Gründen – und weil es so nah ist – stehe ich mit Shizune und Misha vor dem kleinem Teehaus, ehe ich mich versehe."


play sound sfx_storebell

scene bg suburb_shanghaiint onlayer master
with locationchange

show yuukoshang neutral_down onlayer master at center
with charaenter

yu "Willkommen!"


play music music_dreamy fadein 2.0

"Es ist eine Weile her, seit ich Yuukos Stimme gehört habe, darum überrascht mich ihre energiegeladene Begrüßung aufs Neue. Etwa wie eine extrem nervöse Misha."


show yuukoshang neutral_down onlayer master at tworight
show bg suburb_shanghaiint onlayer master at bgright
with charamove

show misha perky_smile onlayer master at twoleft
with charaenter

mi "Hi~! Aber~! du musst das nicht immer machen, wenn es nur wir sind."


show yuukoshang worried_up onlayer master
with charachange

yu "Doch, muss ich…"


show misha sign_confused onlayer master
with charachange

mi "Aber…"


show misha cross_laugh onlayer master
with charachange

mi "Okay~! Okay~! Wenn du das sagst, Yuuko! Hahahahaha~!"


"Ich nutze diesen Moment, um mich im Teehaus umzusehen, und bemerke, dass es so leer wie immer ist. Es ist Mittagszeit; eigentlich die Stoßzeit für ein Lokal dieser Art. Und dennoch ist es karg wie eh und je."
"Ich verstehe das nicht. Es muss einen Grund dafür geben."


show yuukoshang worried_up onlayer master at center
show misha hips_smile onlayer master at left
show bg suburb_shanghaiint onlayer master at center
with dissolvecharamove

show shizu behind_blank_close onlayer master:
    yalign 1.0 xpos 1.0 xanchor 0.8
with charaenter

"Shizune tippt mir sanft auf dem Arm, um meine Aufmerksamkeit zu bekommen."


show shizu adjust_happy_close onlayer master
with charachange

ssh "Was möchtest du bestellen?"


show yuukoshang neurotic_up onlayer master
with charachange

"Yuuko sieht etwas aufgewühlt aus, nachdem Misha die Frage automatisch weitergibt."


yu "N-Nein, ich sollte eigentlich… fragen… Gibt es etwas, dass ich für euch tun kann?"



show shizu behind_smile_close onlayer master:
    ypos 1.1
show misha perky_smile onlayer master:
    ypos 1.14
with dissolvecharamove

hi "Im Moment nur einen Kaffee, schätze ich. Danke."


show yuukoshang neutral_down onlayer master
with charachange

"Die Entschlossenheit, die Yuuko angesichts ihrer Kellner-Pflichten an den Tag legt, ist richtig bewundernswert. Genauso wie die Geschwindigkeit, mit der sie uns nach unserer Bestellung blitzartig unsere Kuchenstücke und Getränke an den Tisch bringt."


hide yuukoshang onlayer master
with charachange

show shizu behind_smile_close onlayer master:
    closeright
    ypos 1.1
show misha perky_smile onlayer master:
    twoleft
    ypos 1.14
with charamove

"Andererseits sind wir die einzigen Gäste hier. Wer weiß, wie es mit einem vollen Laden wäre."


"Shizune und Misha schlagen sofort begeistert zu, als sie ihren Kuchen serviert kriegen – wahrscheinlich weil sie sich mit Besteck in den Händen nicht unterhalten können."


"Immerhin besteht der ganze Sinn mit Freunden zu essen darin, dass man sich dabei unterhalten kann. Es leuchtet ein, dass es bei ihnen genauso ist."


"Ich bin gerade mal zur Hälfte mit meinem Kuchen fertig, als ich das klirren ihrer Gabeln höre, die sie auf ihre leeren Teller zurücklegen."


hi "Es ist ungesund so zu schlingen."


show misha hips_grin onlayer master
with charachange

mi "Hahaha~! Hicchan klingt wie ein alter Mann~!"


"Ich erschaudere und fühle mich sofort, als wäre ich geohrfeigt worden."


show shizu adjust_happy_close onlayer master
with charachange

shi "…"


show misha sign_smile onlayer master
with charachange

mi "Wirst du morgen einen Yukata tragen, Hicchan?"


hi "Nein, ich hab nicht mal einen. Na ja, selbst wenn, wäre ich nicht der Typ, der so etwas tut."


hi "Was ist mit euch? Werdet ihr euch schick machen?"


show shizu behind_blank_close onlayer master
show misha perky_smile onlayer master
with charachange

ssh "Natürlich."


hi "Was meinst du mit „natürlich”? Das letzte Mal habt ihr euch nicht festlich gekleidet."


show shizu basic_normal2_close onlayer master
with charachange

ssh "Einmal ist keinmal! Es ist auch eine vollkommen andere Situation. Zum einen war das nicht Tanabata, und zum anderen war das Fest auf dem Schulgelände, und da sollten Schüler ihre Uniformen tragen."


"Offensichtlich ein Witz, aber ihr Ausdrucksweise ist nicht anders als sonst. Das ist nicht normal, aber das war ihr Humor auch nie. Ich bin daran gewöhnt."


"Dass sie ausgefallene Dinge so ernst sagt, gefällt mir wohl ein wenig besser, als wenn sie bei ersten Themen herumalbern würde."


"Was mich auf jeden Fall noch mehr stört ist, dass ich angefangen habe, eine Stimme mit ihrem Gebärden zu verknüpfen. Und das rasselt irgendwie mit dem aneinander, was Misha laut ausspricht. Ich bin verwirrt."


show shizu behind_smile_close onlayer master
with charachange

ssh "Diesmal werde ich mich rausputzen!"


show misha sign_smile onlayer master
with charachange

mi "Diesmal werde ich mich rausputzen! Du wirst sehen, Hicchan!"


show misha hips_smile onlayer master
with charachange

mi "Nicht nur Shicchan, sondern ich auch~!"


show misha hips_grin onlayer master
with charachange

mi "Vielleicht~ mach ich auch meine Haare anders."


hi "Tu das nicht, ich kann mir dich kaum mit einem anderen Aussehen vorstellen."


show shizu adjust_happy_close onlayer master
with charachange

"Shizune wedelt mit dem Finger und lächelt."


show shizu adjust_smug_close onlayer master
with charachange

ssh "So eine voreilige und harte Ablehnung. Was wäre, wenn ich meine Haare anders machen würde?"


hi "Vielleicht solltest du deine Haare lang wachsen lassen und sie zu Spiralen drehen."


show shizu behind_blank_close onlayer master:
    xpos 1.0 xanchor 0.8
show misha hips_smile onlayer master:
    left
    ypos 1.14
with dissolvecharamove

show yuukoshang neutral_up behind misha at center onlayer master
with charaenter

"Sie sieht gar nicht begeistert aus. Zum Glück sehe ich, wie Yuuko gerade zu uns hinüberkommt, wahrscheinlich um unsere Teller abzuräumen oder zu fragen, ob wir noch etwas brauchen."


hi "Yuuko, was machst du denn an Tanabata?"


show yuukoshang panic_up onlayer master
with charachange

yu "Heh?"


"Es ist, als ob sie auf dem Weg hierher geübt hätte, wie sie am reibungslosesten fragen könnte, ob ich noch etwas Kaffee möchte. Aber sie hat keine Ahnung, wie sie auf eine von mir gestellte Frage antworten soll. Ich fühle mich mies."


show yuukoshang worried_down onlayer master
with charachange

yu "Ich… werde arbeiten."


show misha perky_sad onlayer master
with charachange

mi "Yuuko~, sie lassen dich an Feiertagen arbeiten? Ohhhh…"


show yuukoshang neutral_down onlayer master
with charachange

yu "W-Wir haben die meisten Kunden an Feiertagen, und manchmal Touristen. Es stört mich nicht. Ich muss mich anstrengen."


show shizu adjust_happy_close onlayer master
show misha perky_smile onlayer master
with charachange

ssh "Das verstehe ich vollkommen. Wie bewundernswert."


"Shizune nickt ihr in Verbundenheit zu. Durch ihre geteilte Entschlossenheit, die Besten zu sein, spürt sie wohl eine Art Verbindung mit Yuuko."
"Wobei es für sie eine Sache des Stolzes ist. Yuuko hingegen denkt vielleicht einfach, dass sie diesen Job wirklich, wirklich braucht. Und eventuell eine Gehaltserhöhung."


hi "Die meisten Kunden, was? Wie viele Leute besuchen euch denn an einem durchschnittlichen Feiertag?"


show yuukoshang neurotic_up onlayer master
with charachange

yu "Ah, nun…"


show yuukoshang worried_up onlayer master
with charachange

yu "…"


hide yuukoshang onlayer master
with charaexit

show shizu behind_smile_close onlayer master:
    closeright
    ypos 1.1
show misha perky_smile onlayer master:
    twoleft
    ypos 1.14
with dissolvecharamove

"Yuuko geht weg und fängt an, eine Tasse mit Umrührstäbchen zu reinigen. Das ist unhöflich. So etwas tut eine anständige Kellnerin nicht! Dennoch habe ich dadurch meine Antwort – irgendwie. Eindeutig ist, dass das Geschäft bestenfalls dürftig läuft."


"Ich fange an mich zu fragen, ob das Shanghai überhaupt offen bleiben wird. Vielleicht war dieses „Teehaus im Multikulti-Stil” ein ungeheuer erfolgreicher Trend, bevor ich herkam."
"Doch nun ist davon nichts mehr zu sehen und sie belassen es so, während sie sich mit neuen Gerätschaften ausrüsten."


"Vielleicht ist der Eigentümer reich und hat eine Art Wette mit jemanden abgeschlossen, oder er hat einen verrückten Plan, um zu sehen, wer das meiste Geld verlieren kann."
"Vielleicht verpasse ich bei jedem Besuch einfach nur die Kundenscharen um ein paar Sekunden."


"Oder vielleicht ist dieses Lokal einfach eine Fassade für Waffenschieber."


hi "Da sonst keiner hier ist, warum setzt du dich nicht zu uns?"


"Wir können uns über Unwirtschaftlichkeit unterhalten… Aber Yuuko scheint nicht darauf anzuspringen und schüttelt energisch ihren Kopf."


show misha hips_grin onlayer master
with charachange

mi "Ich hab noch nie wirklich Tanabata gefeiert, oder mich für so etwas schick gemacht~! Endlich kann ich meinen Yukata tragen. Yay yay~!"


hi "Was meinst du mit „noch nie”? Was war denn letztes Jahr?"


show misha sign_smile onlayer master
with charachange

mi "Hm~… letztes Jahr haben Shicchan, ich und die Klassensprecherin der 3-2 eine Bude für das Fest betrieben! Es war ein Nudel-Stand, glaube ich~? Ja, das war es~! Jupp!"


show shizu adjust_blush_close onlayer master
with charachange

"Die blinde Klassensprecherin der 3-2 muss Lilly sein. Ich bin überrascht, dass sie bei etwas in der Lage waren zusammenzuarbeiten, aber wahrscheinlich wäre Misha der bestmögliche Puffer für solche Sachen, wenn man bedenkt, wie unschuldig sie ist."


show misha hips_grin onlayer master
with charachange

mi "Shicchan hat gekocht und Lilly die Bestellungen angenommen, und ich hab für sie Übersetzt~!"


show misha hips_smile onlayer master
with charachange

mi "Shicchan hat die ganze Zeit gesagt: „Es ist so ineffizient~! Misha~! Warum musst du der Mittelsmann sein? Eher~, warum haben wir überhaupt einen Mittelsmann? Hm~?”"
mi "„Es würde reichen, wenn ich mich ums Kochen kümmere und du um die Bestellungen! Das ergibt überhaupt keinen Sinn!”"


show misha sign_smile onlayer master
with charachange

mi "Aber~! Ich denke, dass am Ende alle Spaß hatten. Stimmt's, Shicchan~?"


show shizu behind_frustrated_close onlayer master
with charachange

shi "… … …"


"Shizune richtet widerwillig ihre Brille, was Misha zum laut Loslachen bringt."


show misha hips_grin onlayer master
with charachange

mi "Es war die Idee des alten Schülerrats~! Darum~!"


hi "Wie war der letzte Schülerrat denn so?"


"Shizune beschließt, endlich wieder ins Gespräch einzusteigen, oder eher – sie kann sich nicht zurückhalten."


show shizu basic_angry_close onlayer master
with charachange

ssh "Schrecklich."


"Das war direkt. Sie schließt mit einer hackenden Bewegung ab, als ob sie ein Urteil über ihn fällen würde. Ich hoffe, sie erläutert das ein wenig."


show shizu adjust_angry_close onlayer master
with charachange

shi "…"


show misha sign_confused onlayer master
with charachange

mi "Auf Universitäten und einigen Privatschulen können die Schülerräte Kontrolle über Millionen von Yen haben, um das Budget nach Bedarf zu verteilen! Wow~! Wirklich? Millionen?"
mi "Ah, richtig~! Und sie werden auch viel mehr in schulische Aktivitäten eingebunden, Hicchan!"


"Nach Mishas Ton zu schließen ist das anscheinend für sie neuer als für mich."


show misha hips_frown onlayer master
with charachange

mi "Der Schülerrat dieser Schule war dagegen ein Witz~! Gebt den Leuten keine Machtpositionen, wenn sie nicht einmal Macht haben! Was soll das bringen~?"


show shizu behind_blank_close onlayer master
with charachange

ssh "Darum…"


show misha sign_smile onlayer master
with charachange

mi "… wollte ich, dass wir immer mehr Arbeit kriegen! Es war hart, die Schule und die anderen Schülerratsmitglieder davon zu überzeugen."
mi "Eigentlich~ ist ein Großteil der Arbeit, von der du mitbekommen hast, von mir übernommen worden. Davon hat Lilly gesprochen."


show misha hips_grin onlayer master
with charachange

mi "Wenn Shicchan nicht gewesen wäre, würde der Schülerrat tagein tagaus nur Anwesenheitslisten sortieren."


show misha cross_laugh onlayer master
with charachange

mi "Hahaha~! Wär dir das lieber, Hicchan?"


show misha sign_smile onlayer master
with charachange

mi "Natürlich, Hicchan, haben die meisten Mitglieder aufgehört zu kommen, sobald die Arbeit allmählich anfing mehr zu werden."


show misha hips_laugh onlayer master
with charachange

mi "Wahahaha~!"


show shizu basic_normal2_close onlayer master
show misha hips_smile onlayer master
with charachange

shi "…"


"Shizune faltet ihre Finger sorgfältig. Es sieht aus, als würde sie etwas hinzufügen wollen, kann sich aber nicht dazu überwinden."


"Wie sie sagte, Gebärdensprache gibt einem etwas mehr Zeit, um über das nachzudenken, was man „sagen” möchte. Ich schätze, sie hat das Gefühl, dass sie darüber nicht reden kann."


show shizu behind_blank_close onlayer master
with charachange

ssh "Damals ist damals, und jetzt ist jetzt. Lasst uns morgen einfach Spaß haben."


"Dafür entscheidet sie sich letztendlich."


hi "Na klar."


show shizu adjust_happy_close onlayer master
with charachange

shi "…"


show misha perky_smile onlayer master
with charachange

stop music fadeout 5.0

mi "Okay~! Dann ist der Schülerrat für heute ver-taaagt!"


show misha hips_grin onlayer master
with charachange

mi "Er muss enthusiastisch vertagt werden, weil heute ein guter Tag war."


show misha cross_laugh onlayer master
with charachange

mi "Ahahaha~!"


scene bg school_road_ss onlayer master
with shorttimeskip

"Als wir das Teehaus verlassen, scheint die Schule schon vorüber zu sein, da ich Schüler von der Schule herunterkommen sehen kann, während wir die zu ihr führende Straße nach oben laufen."


"Einige der Leute, die Schuluniform tragen, werfen Shizune beim Vorbeilaufen Blicke zu, und ich frage mich, ob sie sie als die Schülerratspräsidentin erkennen oder ob ihre Augen einfach nur von Mishas Kopf angezogen werden."


"Es ist unmöglich, das Stimmgewirr zu überhören, das in der Luft liegt, und das Thema sind fast immer die Pläne für Tanabata. Ich frage mich, wie viele von ihnen die Stände besuchen werden, die ich wieder zusammengebaut habe."


"Es erfüllt mich mit etwas Stolz – ein Gefühl, dass ich durch das Aushelfen meiner Schule noch nie bekommen habe."


"Vielleicht fühlt sich Shizune genauso. Beinahe will ich nachfragen, aber es kommt mir dämlich vor."


scene bg school_courtyard_ss onlayer master
with locationskip

"Darum behalte ich den Gedanken einfach im Hinterkopf, während wir drei das Schulgelände betreten und uns dann trennen. Shizune zum Schülerratszimmer und Misha und ich zu unseren Wohnheimen."


"Erst nachdem sie weg sind begreife ich, dass ich wieder einmal nicht gefragt habe, wann und wo sie sich morgen treffen wollen."


$ suppress_window_after_timeskip = True

scene black onlayer master
with dissolve


label de_S16:

window hide None

scene black onlayer master
with dissolve

scene bg school_dormhisao onlayer master
with openeye

window show

"Obwohl heute ein Feiertag ist, wache ich zur gleichen Zeit auf wie immer – an einem Tag, an dem jeder sonst wahrscheinlich für weitere sechs Stunden ausschläft."


play music music_pearly fadein 3.0

"Ich nehme zum ersten Mal seit einigen paar Tagen wieder mein Pillen. Zugegebenermaßen habe ich meine Medikamente vernachlässigt. Beim Anblick der Reihen von Tablettenfläschchen frage ich mich, wie ich das hinbekommen habe."


"Siebzehn verschiedene Medikamente. Nachdem ich alle genommen habe, fühle ich mich voll genug, um das Frühstuck auszulassen."


"Da ich schon mal wach bin, kann ich auch gleich einen Spaziergang machen."


scene bg school_dormext_full onlayer master
with locationskip

"Das Wetter draußen sieht gut aus und erzeugt eine idyllische Atmosphäre, von der ich oft geträumt habe."


"Es ist schon immer eine romantische Vorstellung von mir gewesen, durch die Landschaft zu schlendern und die frische Luft genießen zu können."


"Jetzt, da ich eine Gelegenheit dazu habe, kann ich nicht widerstehen – auch wenn es vielleicht albern scheint."


scene bg school_courtyard onlayer master
with locationchange

"Ich halte vor dem Hauptgebäude mit dem Gedanken, mir etwas zum Trinken zu kaufen und beschließe dann, es zu betreten und vielleicht etwas auf dem Dach herumzulungern."


"Die Aussicht könnte um diese Zeit ziemlich cool sein, und ich bin mir sicher, dass niemand sonst dort oben sein wird. Ich bin noch nie allein dort gewesen."


$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0

scene bg school_staircase1 onlayer master
with locationchange

"Die Schule ist heute still. Verlassen. Meine durch das Treppenhaus hallenden Schritte sind zermürbend laut."


"Weil ich so viel Zeit im Gebärdensprache-Unterricht oder bei der Arbeit mit Shizune in absoluter Stille verbringe, sollte es mich eigentlich nicht stören. Trotzdem tut es das."


"Dadurch werden die leisesten Geräusche, die ich sonst nicht einmal bemerkt hätte, scheinbar laut wie ein Kanonenschlag. Mir kommt es vor, als würde ich durch einen Ort schleichen, an dem ich nicht sein dürfte."
"Ich frage mich, warum ich dieses Gefühl kriege. Vielleicht spukt es an der Schule ja."


play sound sfx_door_creak
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
stop music fadeout 3.0

scene bg school_roof onlayer master at left
with locationchange

"Als ich die Tür zum Dach öffne, sehe ich, dass ich nicht allein bin. Misha lehnt sich gegen den Zaun und lässt ihren Blick über das Schulgelände schweifen, ohne mich zu bemerken."


"Sofort weiß ich, was zu tun ist: Ich muss meine Hände über ihre Augen legen und fragen: „Wer bin ich?”. Das muss sein."


"Auf dem halben Weg fällt mir ein, wie das aussehen würde, wenn Shizune plötzlich vorbeikäme. Vielleicht ist sie ja nur kurz ein paar Sandwiches besorgen und sieht dann, wie ich auf diese Weise an Misha heranschleiche."


"Ich bete still, dass mir solch ein zufälliges Missverständnis erspart bleibt."


show bg school_roof onlayer master at right
with charamove

hi "Wer bin ich?"


mi "Hicchan!"


"Sagt sie ohne ein Sekunde zu zögern, ohne auch nur ein bisschen von ihrem normalen Ton abzuweichen. Der Spaß war vorüber, bevor er überhaupt angefangen hat."


play music music_soothing fadein 1.0

show misha hips_grin_close onlayer master at Slide(0.6, 0.5, 0.5, 0.5, 0.5)
with charaenter

mi "Hi, Hicchan! Guten Morgen~!"


show misha sign_confused_close onlayer master at center
with charachange

"Reflexartig versucht sie, mit ihren Händen eine Begrüßung zu gebärden und verheddert sie dabei im Zaun."


hi "Guten Morgen. Ich hab nicht damit gerechnet, dich hier zu finden. Warum bist du so früh wach?"


show misha perky_smile_close onlayer master
with charachange

mi "Ich könnte dich dasselbe fragen, Hicchan! Warum bist du so früh wach? Ich hab nicht damit gerechnet, dich hier zu finden."


hi "Ich hab zuerst gefragt."


show misha hips_grin_close onlayer master
with charachange

mi "Hm~… du hast Recht. Wahaha~!"


show misha sign_smile_close onlayer master
with charachange

mi "Du klingst genau wie Shicchan."


hi "Nein, tue ich nicht."


"… sage ich so unüberzeugend wie nur möglich. Glücklicherweise bemerkt Misha nicht, was für ein schlechter Schauspieler ich bin."


hi "Freust du dich auf heute Abend?"


show misha hips_smile_close onlayer master
with charachange

mi "Na sicher, Hicchan~! Ich mag keine Feste, oder vielleicht nicht so sehr wie Shicchan, aber bei den Tanabata-Buden gibt es immer interessante Dinge zu kaufen und allerlei saisonales Essen. Und~! Ich komme dazu, meinen Yukata zu tragen!"


"Ihre Wortwahl ist etwas seltsam. Es klingt, als wollte sie sagen, dass sie keine Feste mag, aber alles, was mit ihnen zu tun hat. Ich weiß nicht, ob es sich lohnt da nachzuhaken, und vielleicht verstehe ich es auch einfach nur falsch."


show misha perky_smile_close onlayer master
with charachange

mi "Was ist mir dir, Hicchan~?"


hi "Natürlich freue ich mich darauf, andernfalls würde ich doch zu Hause bleiben, oder? Das wäre doch logisch."


show misha hips_grin_close onlayer master
with charachange

mi "Ahaha~! Hicchan, so logisch bist du auch wieder nicht~! Das ist wirklich überraschend! Hm, okay, obwohl. Ich wollte nur sichergehen, weil du letztes Mal nicht so amüsiert ausgesehen hast. Ich und Shicchan haben uns deswegen etwas Sorgen gemacht."


hi "Hey, ich hatte Spaß. Ich schätze, es hat mir letztendlich mehr Spaß gemacht als erwartet."


show misha perky_smile_close onlayer master
with charachange

mi "Wirklich, Hicchan~? Wahahaha~! Welchen Teil davon? Verrat's mir~!"


hi "Na ja, da war das Feuerwerk zum Schluss. Es war… wirklich schön."


hi "Ich glaube, du hast es verschlafen."


show misha hips_smile_close onlayer master
with charachange

mi "Oh~… Ich schlafe immer so früh ein. Aber~! Ich werde es dieses Jahr nicht verschlafen! Ich werde auf jeden Fall wach bleiben!"


hi "Ich glaube nicht, dass sie bei Tanabata ein Feuerwerk machen. Es ist eine vollkommen anderen Stimmung."



hi "Vielleicht bekommst du Shizune dazu, eine Petition dafür zu starten. Und dazu das Feuerwerk etwas früher anzusetzen."


show misha cross_laugh_close onlayer master
with charachange

mi "Hahahahahaha~! Vielleicht tue ich das~! Das ist eine tolle Idee, Hicchan!"


hi "Ah, nein, nein ist es nicht! Lass das. Das war nicht ernst gemeint."


hi "Obwohl… Vielleicht würde es Shiccha… Shizune ärgern."


show misha hips_grin_close onlayer master
with charachange

mi "Wahaha~. Es klingt so, als würde dir das gefallen, Hicchan."


show misha cross_smile_close onlayer master
with charachange

mi "Hicchan~! Magst du Shicchan?"


"Ja oder nein – ich kann keins davon sagen. Und weil ich gerade sitze, kann ich mich nicht einmal unauffällig absetzen."


hi "Sei nicht albern; du bist diejenige, die ich mag."


show misha perky_smile_close onlayer master
with charachange

mi "Ahahaha~! Wirklich, Hicchan! Hm~! Nein, du veralberst mich, oder? Du musst Shizune mehr mögen."


hi "Misha, du ziehst zu schnell Schlussfolgerungen."


show misha sign_smile_close onlayer master
with charachange

mi "Aber du hast sie fast Shicchan genannt! Darum~! Ich hab Recht, oder?"


hi "Das ist nur, weil du sie die ganze Zeit so nennst. Es ist in meinem Kopf hängengeblieben. Sich Gesprochenes einzuverleiben ist ganz normal, weißt du."
hi "Außerdem war es nur ein kleiner Ausrutscher. Und nach deiner Logik müsstest du sie mehr mögen als ich. Und… machst du dich über mich lustig oder so?"


show misha cross_laugh_close onlayer master
with charachange

mi "Wahaha~!"


show misha perky_smile_close onlayer master
with charachange

mi "Vielleicht~."


show misha hips_smile_close onlayer master
with charachange

mi "Ich hab Hunger. Hast du gefrühstückt, Hicchan?"


hi "Nein. Nur Medikamente."


show misha sign_confused_close onlayer master
with charachange

mi "Hm…"


"Misha wirbelt mit ihren Fingern träge in der Luft herum, um ihre Hände zu beschäftigen, während sie denkt."


show misha hips_grin_close onlayer master
with charachange

mi "Dann sollten wir etwas essen gehen~! Glaubst du, dass sie heute Frühstück servieren?"


"Das ist wirklich etwas, was ein Mitglied des Schülerrats wissen sollte. Das würde ich zumindest gerne sagen. Aber ich bin selbst im Schülerrat und weiß es nicht."


hi "Als ich in dieses Gebäude hereingekommen bin, sah es nicht so aus, als ob jemand in der Küche arbeiten würde. Aber ich bin mir nicht sicher."


show misha perky_smile_close onlayer master
with charachange

mi "Hey, Hicchan, hast du schon mal von diesen Verkaufsautomaten gehört, von denen man Burger, Suppen und sogar Pizza bekommen kann? Wäre es nicht klasse, wenn wir einen von denen in unserer Schule hätten~?"


hi "Ich weiß nicht… Ich fand diese Automaten schon immer unheimlich."


show misha hips_smile_close onlayer master
with charachange

mi "Stell dir vor, wie cool es wäre, wenn wir so einen Automaten an unserer Schule hätten, Hicchan! Es wäre fast wie Zauberei, oder nicht?"


mi "Warmes Essen, das aus einem Verkaufsautomaten kommt, ist so unglaublich, dass ich mir das niemals vorstellen könnte. So einen Automaten zu sehen wäre ein Traum!"


show misha perky_sad_close onlayer master
with charachange

mi "Hm~… Aber wir haben im ganzen Dorf nicht einen davon. Es ist sowieso noch zu früh, um ins Dorf zu gehen. Ich werde nicht frühstücken können, Hicchan, das ist die wichtigste Mahlzeit am Tag. Das sagen alle~! Ah, ich will was essen!"


hi "Du bist wirklich albern. Wenn es dich so sehr plagt, kaufe ich dir eine Limonade."


show misha hips_frown_close onlayer master
with charachange

"Misha plustert ihre Backen auf und zieht ein ernstes Gesicht."


mi "Hicchan, Limonade ist kein Frühstück. Es ist wie Wasser~."


hi "Es ist nicht wie Wasser, es ist eine Flüssigkeit. Wasser ist kein Essen. Flüssigkeit kann Essen sein."


"„Na wer hört sich jetzt wie Shizune an, Misha?”, würde ich gerne sagen. Selbst ihre Betonung erinnert mich an Shizunes unerschrockene, nüchterne Art, das Lächerliche zu verkünden. Aber wenn ich das sagen würde, wäre ich derjenige, der wie sie klingt."


"Es ist furchtbar, ihr Drang sich mit anderen zu messen färbt wirklich auf mich ab."


hi "Dann lass uns etwas zu Essen besorgen."


show misha cross_frown_close onlayer master
with charachange

mi "…"


show misha cross_laugh_close onlayer master
with charachange

mi "Okay. Ahahahaha~!"


stop music fadeout 3.0
stop ambient fadeout 1.0

scene bg school_lobby onlayer master
with locationskip

"Wie vorauszusehen war, ist unsere Suche nach etwas Essbarem so früh am Morgen in einem leeren Schulgebäude ein Fehlschlag."


"Wir beschließen, fürs Erste aufzugeben, aber Misha zieht allein los, nachdem sie geschworen hat, etwas zum Frühstück zu finden – obwohl es inzwischen schon eher Mittag ist."


scene bg school_dormhisao onlayer master
with locationskip

"Ich gehe zurück in mein Wohnheim. Die nächsten Stunden vergehen langsam, und ich verbringe sie damit, meinen Lesestoff nachzuholen."


show bg school_dormhisao_ni as overlay onlayer master at Alphain(6.0), center
with None

play music music_dreamy fadein 6.0

"Einige dieser Bücher habe ich nicht angerührt, seit ich im Krankenhaus war. Wenn ich daran zurückdenke, ist es noch gar nicht so lange her, obwohl es mir definitiv so vorkommt."


"Ein freier Tag und mir fällt nichts ein, was ich unternehmen könnte."
"Ich mache ein kurzes Nickerchen, und als ich mich zum zweiten Mal heute umziehe, bemerke ich, dass ich mich eigentlich gar nicht richtig mit Shizune oder Misha auf einen Treffpunkt oder eine Uhrzeit geeinigt habe."


"Vermutlich werden sie mich irgendwann abholen kommen, aber ich würde ziemlich bescheuert aussehen, wenn es soweit kommen würde."


scene bg school_dormhisao_ni onlayer master
with None

"Es ist bereits Abend, darum sollte ich mir wenigstens Mühe geben, sie vorher zu finden."


scene bg school_courtyard_ni onlayer master
with locationskip

"Es ist gar nicht so einfach, die beiden zu finden, obwohl das Gelände nicht gerade überfüllt ist und man Mishas pinke Haare eigentlich auch in großen Menschenmengen kaum übersehen kann."


scene bg school_gate_ni onlayer master
with locationchange

"Endlich treffe ich sie am Haupttor, wo ich als erstes nachgesehen hatte."


show shizuyu basic_happy_ni onlayer master at center
with charaenter

ssh "Hallo!"


"Sie versucht ihre übliche Begrüßung mit einer kleinen Verbeugung am Ende zu unterstreichen."


show shizuyu basic_happy_ni onlayer master at tworight
show bg school_gate_ni onlayer master at bgright
with charamove

show misha sign_smile_yuk_ni onlayer master at twoleft
with charaenter

mi "Hicchan~! Wie geht's dir?"


"Es ist seltsam, sie in Yukatas zu sehen. Auch wenn ich ganzen Abend über schon Yukatas gesehen habe."


"Der von Shizune ist einfach und geschmackvoll. Wenn ich darüber nachdenke, passt diese Wahl sehr gut zu ihr. Auch wenn ihre Gesten und ihr Verhalten oft etwas pompös sind, würde sie wohl eher sterben, als sich so anzuziehen."


"Was meinen Blick anzieht ist ihre Haarnadel. Ein Perlenblume, die sanft im Mondlicht schimmert."


"Sie sieht hübsch an ihr aus, aber irgendwie kommt sie mir auch fehl am Platz vor. Als ob sie zu aufwändig für eine Oberschülerin wäre, oder vielleicht für jemanden, der heimlich so verspielt ist wie Shizune."


"Mishas Yukata hingegen entspricht meinen Erwartungen, darum passt sie eigentlich etwas {b}zu{/b} gut zu ihr. Zusammen mit ihren kaugummipinken Haaren sieht sie niedlich aus, aber unzeitgemäß."


hi "Ihr seht gut aus, ihr Zwei."


show misha perky_smile_yuk_ni onlayer master
with charachange

mi "Danke, Hicchan~!"


show shizuyu cross_angry_ni onlayer master
with charachange

shi "…"


mi "Hicchan, du bist etwas zu spät. Wir warten hier schon seit einer Weile auf dich, hast du den Ort oder die Zeit vergessen?"


mi "Na ja~! Lass uns losgehen, Hicchan~!"


show shizuyu cross_happy_ni onlayer master
with charachange

shi "…"


"Dass Misha nicht mehr auf die Antwort zu dieser Frage wartet, rettet mich vor einem potentiell peinlichen Geständnis – nämlich, dass ich sie schon seit mindestens einer Stunde gesucht habe."


"Wenn ich Shizune und Misha so fröhlich sehe, ist es schwierig, nicht in Feierstimmung zu verfallen und diesen schönen Abend zu genießen."


"Was mir Sorgen bereitet ist, dass ich heute ein paar Probleme habe, Shizunes Gesten zu verstehen. Ich bin seit fast einer Woche nicht mehr beim Gebärdensprache-Unterricht gewesen, darum wundert es mich nicht."
"Vielleicht habe ich mich in letzter Zeit zu sehr ablenken lassen und falle zurück. Es wäre sicherlich nicht das erste Mal."


hi "Wartet mal – wo gehen wir hin? Ins Dorf?"


show shizuyu basic_happy_ni onlayer master
with charachange

ssh "Ja."


hi "Das ergibt keinen Sinn. Wir haben uns noch nicht mal angesehen, was auf dem Schulgelände ist. Außer ihr habt beschlossen, euch zu amüsieren, während ich nicht da war."


show shizuyu cross_happy_ni onlayer master
with charachange

ssh "Wir kommen wieder; wir arbeiten uns von unten nach oben."


show misha sign_smile_yuk_ni onlayer master
with charachange

mi "Hahaha~! Hicchan, wir müssen so oder so ins Dorf gehen und wiederkommen, wenn wir alles sehen wollen. Darum~! Auf diese Weise werden wir direkt bei unseren Wohnheimen sein, wenn wir fertig und müde sind. Das ist der perfekte Plan~!"


show shizuyu basic_happy_close_ni onlayer master at closeright
with characlose

stop music fadeout 2.0

"Zugegebenermaßen ist das logisch. Shizune lässt mir eh nicht viel Zeit zum Widersprechen, da sie mich am Arm packt und sanft versucht, mich mitzuziehen."


scene ev shizutanabata onlayer master:
    truecenter zoom 8.0 rotate 45.0 subpixel True
    easein 1.0 zoom 1.1 rotate 0.0
    easein 8.0 zoom 1.0
with locationskip

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_crowd_outdoors fadein 2.0
play music music_ease

"Die Straßen sind nur von Mondlicht und von tief hängenden Papierlaternen erleuchtet. Die Atmosphäre ist sehr beruhigend."


"Nun, da wir im Dorf sind, läuft Shizune etwas langsamer, um sich die Sehenswürdigkeiten anzusehen."


"Darum beschließe ich, etwas schneller zu laufen, um sie zu ärgern, aber sie passt ihr eigenes Tempo zügig meinem Laufschritt an. Sie gibt ein stummes Lachen von sich, bevor sie mit ihrer freien Hand etwas zu Misha gestikuliert."


shi "…"


mi "Was willst du zuerst machen, Hicchan~?"


hi "Wir wäre es mit ein paar Spielen, falls es hier welche gibt?"


mi "Ich dachte, du magst keine Spiele, Hicchan."


hi "Ich hab nichts dagegen."


"Zum zweiten Mal heute spüre ich, wie ihre schmalen Finger meine umschließen."
"Es kommt mir vor, als wäre ich die ganze Zeit über von Shizunes Willen mitgezogen worden. Ab und zu ist es anstrengend, aber meistens habe ich nicht wirklich etwas dagegen."


"Manche Menschen haben einfach die Fähigkeit, andere sturmartig in ihr Leben zu ziehen. Dieses Wort passt manchmal zu Shizune, glaube ich. Auch wenn ich es Misha zuvor nicht sagen wollte, ich mag sie."


mi "Hicchan, diesmal wirst du auch für mich eine Puppe gewinnen, stimmt's~?"


hi "Darüber machst du dir immer noch Gedanken? Okay, werde ich."


$ renpy.music.set_volume(1.0, 2.0, channel="ambient")

scene bg suburb_tanabata_ni onlayer master at bgright
show nightwash onlayer master
with shorttimeskip

"Während wir umherstreifen und versuchen, so viele alberne Sachen wie möglich zu tun, vergeht die Zeit schneller als ich dachte."


show misha perky_smile_yuk behind nightwash at center onlayer master
with charaenter

mi "Slush-Eis! Hicchan, willst du einen Becher~?"


"Misha stürmt zu dem Stand, ohne auch nur auf meine Antwort zu warten."


show misha perky_smile_yuk onlayer master at twoleft
show bg suburb_tanabata_ni onlayer master at center
with charamove

show shizuyu cross_happy_close behind nightwash at closeright onlayer master
with charachange

ssh "Die sehen lecker aus, ich will auch einen. Wir spielen Schere-Stein-Papier um zu sehen, wer für alle bezahlen darf."


hi "Oder… jeder könnte einfach für seinen eigenen bezahlen."


show misha sign_smile_yuk onlayer master
with charachange

mi "Hicchan~, welche Sorte willst du?"


hi "Das Blaue."


show shizuyu basic_angry_close onlayer master
with charachange

ssh "Blau ist keine Sorte."


hi "Das wusste ich…"


ssh "Etwas nach Farbe zu kaufen ist kindisch."


hi "Du bist kindisch. Was holst du dir? Holst du dir Erdbeere? Ha! Das ist so eine kindische Sorte; nur Kinder essen Erdbeere."


show shizuyu cross_angry_close onlayer master
with charachange

ssh "Du solltest einfach neutral nehmen, das ist die erwachsenste Sorte."


"Ich will wissen, woher sie ihre Persönlichkeit hat. Ich frage mich, ob ich das auch denken würde, wenn sie nicht die erste Schülerin gewesen wäre, mit der ich an meinem ersten Tag hier eine Unterhaltung begonnen habe."


"Es ist absolut möglich, dass ich all die Dinge nicht bemerkt hätte, deretwegen ich mich zu ihr hingezogen fühle."


"Falls ich nicht gewusst hätte, dass sie mich nicht hören kann; dass sie so wetteifernd ist, so erpicht darauf, mich in den Schülerrat zu holen, so verspielt und doch so scharfsinnig…"


"Ohne diese ständig neuen Facetten, die mein Interesse an ihr Wach halten – wäre sie mir ohne diese so ans Herz gewachsen?"


"Wahrscheinlich denke ich zu viel darüber nach."


hi "Willst du dir nicht etwas wünschen?"


show misha perky_confused_yuk onlayer master
with charachange

mi "Shicchan wünscht sich nie etwas, Hicchan!"


hi "Ach wirklich? Nicht einmal zu Neujahr? Warum das?"


show shizuyu basic_happy_close onlayer master
with charachange

shi "…"


"Shizune legt ihre Finger aneinander, antwortet aber nicht."


ssh "Es ist ein Geheimnis."


show misha sign_smile_yuk onlayer master
with charachange

mi "Ich weiß es~!"


mi "Hicchan, soll ich es dir verraten?"


show shizuyu cross_blush_close onlayer master
with charachange

shi "…!"


hi "Bitte."


show shizuyu basic_angry_close onlayer master
with charachange

"Shizune gebärdet so viele Variationen von kraftvollen Nein-Gesten wie ihr einfallen."


show misha perky_smile_yuk onlayer master
with charachange

mi "Wahaha~! Ich erzähl's dir später, okay?"


show misha perky_sad_yuk onlayer master
with charachange

stop music fadeout 5.0

mi "Eigentlich bin ich müde. Ich denke, ich werde früh ins Bett gehen~."


show shizuyu cross_blush_close onlayer master
with charachange

ssh "Wirklich?"


hi "Es kommt nicht so vor, als wären wir schon lange hier gewesen."


"Wenn man Spaß hat, vergeht die Zeit wie im Flug."


show misha sign_smile_yuk onlayer master
with charachange

mi "Aber~! das sind wir, Hicchan. Vielleicht kann ich vorher noch Yuuko besuchen und dann zurück? Oder~… Ich weiß nicht."


show misha perky_smile_yuk onlayer master
with charachange

mi "Na ja, ist ja auch egal. Habt Spaß ohne mich, okay~?"


hi "Wir gehen sowieso bald zurück zur Schule, Misha."


hide misha onlayer master
with charaexit

show shizuyu cross_blush_close onlayer master at center
show bg suburb_tanabata_ni onlayer master at bgleft
with charamove

"Misha will es nicht hören und verlässt uns trotzdem. Shizune scheint sich auch zu fragen warum, aber während ich es nur denke, gebärdet sie es – wahrscheinlich um die möglichen Gründe zu diskutieren."


scene bg suburb_tanabata_ni onlayer master at bgleft
show nightwash onlayer master
with shorttimeskip

"Nachdem wir beide alles gesehen haben, was es zu sehen gab, überprüfe ich die Uhrzeit und bemerke, dass es ziemlich spät geworden ist. Meine Energie fällt langsam ab, und es ist ein Wunder, dass ich überhaupt so viel hatte."


"Shizune sieht auch langsam etwas erschöpft aus. Wir machen uns auf den Rückweg zur Schule."


stop ambient fadeout 0.5

scene bg school_courtyard_ni onlayer master
with locationskip

play ambient sfx_cicadas fadein 0.5

"Sie wirkt enttäuscht, als sie das erleuchtete und vor Schülern wimmelnde Schulgebäude sieht."


his "Stimmt was nicht?"


show shizuyu basic_aside_ni onlayer master at center
with charaenter

ssh "Ich wollte aufs Dach gehen, aber jetzt sind dort zu viele Leute. Ich bin müde, also ist es vielleicht besser so."


his "Wahrscheinlich sind Pärchen auf dem Dach. So ist das doch an Tanabata."


his "Andererseits bin ich mir nicht sicher. Ist es wirklich so? Bevor ich herkam, bin ich noch nie auf so einem Fest gewesen."


shi ""


his "Ich bin enttäuscht. Ich dachte, du wolltest am Ende noch sehen, was die Schule geplant hat; das Beste für den Schluss aufheben."
his "Jetzt sagst du mir, dass du doch nicht willst? Nicht mal ein bisschen? Ich dachte, du hättest mehr Energie. Ich bin gar nicht müde."


show shizuyu basic_happy_ni onlayer master
with charachange

"Das scheint ihren Kampfgeist zu entfachen, denn Shizune wird sofort munter. Gerade dann merke ich, dass ich gar keine Idee hatte, wo ich sie hinführen könnte. Und ich habe selbst keine Lust zum Hauptgebäude zu gehen."


scene bg school_gardens_ni onlayer master at Fullpan(4.0, dir="right")
with locationchange

"Glücklicherweise ist der Bereich hinter der Schule heute menschenleer. Und er sieht beeindruckend aus."
"Ich wusste nie zu würdigen, wie ausgedehnt und gepflegt er ist, bis ich ihn bei Nacht gesehen habe. Im Mondlicht scheint er sich ins Unendliche zu erstrecken."


show shizuyu basic_happy_ni onlayer master at center
show bg school_gardens_ni onlayer master at right
with charaenter

ssh "Es ist wunderschön, auch wenn es nur eine Wiese ist."


"Zuvor dachte ich, dass sie zu unreif sei, um solch altmodische Klamotten wie heute Nacht zu tragen, aber in diesem Augenblick sieht sie in ihnen ziemlich hübsch aus."


"Es erinnert mich an diesen vergangenen Tag, an dieses andere Fest, zu dem ich mit ihr gegangen bin. Damals sah sie genau so aus."


$ renpy.music.set_volume(0.5, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_serene fadein 1.0

window hide

nvl clear

nvl show dissolve

n "\nIch will ihr sagen, dass ich sie mag. Entschlossen, in einem Zug. Aber auch nur daran zu denken ist einfach so peinlich."


n "Und je mehr ich sie mag, desto peinlicher ist es mir und desto mehr Angst habe ich, ihr meine Gefühle zu gestehen. Sogar jetzt, wo ich es tun könnte, ohne eine dritte Person zum Übersetzen zu brauchen."


n "Geschweige denn… Was, wenn sich das wiederholt, was beim letzten Mal passiert ist? Dann werde ich vielleicht nicht so einfach mit einem monatelangem Krankenhausaufenthalt davonkommen. Ich will nicht einmal daran denken."


n "Ich versuche, diese Gedanken so gut es geht aus meinem Kopf zu verdrängen, sie als irrationale Ängste abzutun."



n "Dennoch…"


n "Als ich zum ersten Mal all meine Tabletten gesehen hatte, hatte ich dieses Bild vor Augen, wie sie auf mich herabregnen – genug, um mich zu ersticken."


n "Ich denke immer noch von Zeit zu Zeit daran. Ich kann nicht behaupten, dass es keine berechtigte Sorge ist. Jedoch sind Zeiten wie diese schön genug, dass ich das vergessen kann."


nvl clear
nvl hide dissolve

$ renpy.music.set_volume(1.0, 1.0, channel="music")
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene ev shizuconfess_normal onlayer master
with flash

window show

ssh "Was ich an dieser Schule am meisten mag ist, dass sie auf dem Gipfel eines Berges steht."


his "Weil du so viel näher am Himmel bist?"


ssh "Genau."


his "Mir gefällt es auch, aber eher wegen der frischen Luft."


his "Du bist so wetteifernd. Zu wetteifernd. Wenn dich ein Wal beißen würde, würdest du zurückbeißen."


scene ev shizuconfess_smile onlayer master
with charachange

shi "…"


"Es bringt sie zum Lachen, und sie zwinkert."


ssh "Wäre das so schlimm?"


"Ihr Lächeln ist ansteckend."


his "Ja."


shi "…"


scene ev shizuconfess_closed onlayer master
with charachange

ssh "Es stimmt. Ich bin furchtbar… ein bisschen."


scene ev shizuconfess_smile onlayer master
with locationchange

ssh "Aber wenn ich Menschen glücklich machen kann, bin ich nicht ganz so furchtbar, oder? Dann ist es okay. Ich habe viele Beispiele zu meiner Verteidigung."


"Vielleicht ist sogar dieser Augenblick ein Spiel für sie."


his "Das stimmt."


stop music fadeout 2.0

"Das ist ein romantischer Moment. Ich weiß nicht, ob so eine Gelegenheit wiederkehren wird, und ich fühle mich gezwungen, etwas Peinliches und Dummes zu sagen."
"Wenn ich zu sehr darüber nachdenke, bezweifle ich, dass meine Hände mir gehorchen werden."


his "Willst du meine Freundin sein?"


scene bg school_gardens_ni onlayer master at right
show shizuyu cross_blush_ni onlayer master
with locationchange

shi "…"


"Ich hoffe, ich habe es richtig gebärdet."


"Ich bin nervös. So sehr, dass ich losrennen will – dennoch bin ich wie angewurzelt."
"Vor ein paar Minuten noch konnte ich rein gar nichts hören, nun nehme ich jedes einzelne Umgebungsgeräusch war. Ich bin wirklich nervös. Ich frage mich, ob man es mir ansieht."


"Eben vergingen die Stunden noch wie Sekunden. Jetzt vergehen Sekunden wie Äonen."


show shizuyu basic_blush_ni onlayer master
with charachange

"Dann sehe ich, wie Shizune zögernd ihre Hände hebt und anfängt zu gebärden, wobei sie aber jede Geste mittendrin abbricht."


"Es ist, wie sie gesagt hat: Gebärdensprache gibt einem die Gelegenheit, seine Worte genau zu überlegen. Und gerade jetzt gibt sie sich damit größte Mühe."


"Eine Situation, auf die sie keine Antwort findet. Es muss undenkbar sein."
"So stoisch wie Shizune auch zu sein versucht, sie kann ihre rot werdenden Wangen nicht verbergen – was sie äußerst süß und feminin macht. Zu wissen, dass sie genauso nervös ist, beruhigt mich."


"Das ist ein weiterer Gedanke, bei dem ich mich selbst beim Wetteifern mit ihr erwische."


show shizuyu cross_happy_ni onlayer master
with charachange

ssh "Okay."


play music music_romance fadein 1.0

show shizuyu basic_happy_close_ni onlayer master
with characlose

"Das ist eine schlichte Antwort. Doch sowie ich das denke, macht Shizune einen Schritt nach vorn und umarmt mich."


stop ambient fadeout 3.0

window hide

nvl clear

nvl show dissolve

n "\n\n\n\n\n\n\n\n\nEine unsichere und vorsichtige Umarmung, als ob ich aus Eierschale bestehen würde, und als ob sie nicht wüsste, wie man jemanden umarmt. Doch um ehrlich zu sein, ist es etwas, mit dem ich ebenfalls keine Erfahrung habe."


n "Unter meinen Fingern ist ihr Yukata kühl und geschmeidig, aber dennoch kann ich Shizunes Wärme spüren."


n "Am Ende dachte sie, dass dies die bestmögliche Geste wäre, um mir zu zeigen, wie sie empfindet."


stop music fadeout 3.0

nvl hide dissolve
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
