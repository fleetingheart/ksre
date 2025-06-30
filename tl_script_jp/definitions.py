import sys

translates = {}
characters = {}
drugs = {}

s_scenes_old = (
    ("Prologue", None, None, ("Act 1","Prologue")),
    ("Out Cold", "NOP1", "On a cold, snowy day, Hisao's dreams were about to be realized, only to be cut short by a sudden heart attack.", ("Act 1","Prologue")),
    ("Bundle of Hisao", "NOP2", "Hisao is told about Yamaku Academy, where he will likely spend the rest of his high school days.", ("Act 1","Prologue")),
    ("Act 1: Life Expectancy", None, None, "Act 1"),
    ("Gateway Effect", "A1", "Hisao steps into Yamaku Academy for the first time, and meets his homeroom teacher, Mutou.", "Act 1"),
    ("Enter Stage Left", "A2", "Introductions to the class, and meeting with the class representative and her interpreter.", "Act 1"),
    ("In the Nursery", "A3", "Misha and Shizune show Hisao the cafeteria, after which he goes to see the nurse.", "Act 1"),
    ("Nobody's Room", "A4", "Hisao moves into his new room, meeting his hallmate Kenji in the process.", "Act 1"),
    ("Smalltalk", "A5", "Shizune and Misha tell Hisao about the upcoming festival and invite him to lunch.", "Act 1"),
    ("Risk vs. Reward", "A6", "Shizune and Hisao battle for the world in a game of Risk.", "Act 1"),
    ("Pseudo Tea Cosy", "A7", "Looking for the library, Hisao gets lost and finds Lilly in a disused classroom.", "Act 1"),
    ("Shared Library", "A8", "Finally finding his way to the library, Hisao meets and scares off Hanako.", "Act 1"),
    ("Bizarre and Surreal", "A9", "Kenji reveals the dark secrets of Yamaku.", "Act 1"),
    ("Lunch Evolution Theory", "A10", "Shizune and Misha badger Hisao into joining the Student Council before discussing lunch.", "Act 1"),
    ("Short Sharp Shock", "A11_1", "On his way to lunch alongside Misha and Shizune, Hisao collides with Emi in the hallway.", "Act 1"),
    ("Meet Cute", "A11_2", "Hisao collides with a rampaging Emi on his way to lunch with Hanako and Lilly.", "Act 1"),
    ("Detour Ahead", "A12", "Shizune and Misha take Hisao to their favourite teahouse, the Shanghai.", "Act 1"),
    ("Sip (Part 1)", "A13", "Hisao has a peaceful lunch with Lilly and Hanako.", "Act 1"),
    ("It Builds Character", "A15", "Mutou tries to have a D&M talk with Hisao, but Misha interrupts and puts Hisao to work.", "Act 1"),
    ("A Private Lunch", "A16", "Searching for supplies, Hisao happens across a strange girl in the art room.", "Act 1"),
    ("Waylay", "A17", "While helping Rin carry some paint, Hisao is quizzed by the nurse.", "Act 1"),
    ("The Other Green", "A18", "Hisao watches Rin paint her mural.", "Act 1"),
    ("The Running Girl", "A19", "When attempting to do some morning exercise, Hisao meets Emi at the running track.", "Act 1"),
    ("Soap", "A20", "Kenji ambushes Hisao in the shower in an attempt to get some cash.", "Act 1"),
    ("Cold War", "A21", "Shizune and Lilly face off over budget requests.", "Act 1"),
    ("Proof of Competency", "A22", "Shizune and Misha assault Hisao in an attempt to get him to join the Student Council.", "Act 1"),
    ("Event Horizon", "A22_2", "Shizune and Misha assault Hisao in an attempt to get him to join the Student Council.", "Act 1"),
    ("Above and Beyond", "A23_1", "Hisao gets a lecture about the noble duties of a Student Council.", "Act 1"),
    ("Things You Can Do", "A23_2", "After escaping from the clutches of Shizune and Misha, Hisao helps out Rin again.", "Act 1"),
    ("Paint by Numbers", "A24", "Hanako and Hisao lend a hand to Lilly's class by volunteering to help build their stall.", "Act 1"),
    ("Exercise", "A25", "Another early morning sees Hisao running at the track with Emi.", "Act 1"),
    ("Invisible Hat", "A26", "Kenji gives Hisao a few insider tips on how to socialize.", "Act 1"),
    ("Home Field Advantage", "A26_1", "Shizune and Misha hijack Hisao as he leaves his room for class.", "Act 1"),
    ("Slow Recovery", "A27_1", "Recovering from his heart flutter, Hisao eventually makes it to class.", "Act 1"),
    ("No Recovery", "A27_2", "Hisao struggles to class after his hijacking by the Student Council.", "Act 1"),
    ("No Free Lunch", "A28", "Hisao is escorted to the student council office for his first official day there.", "Act 1"),
    ("Foot and Mouth", "A29", "Emi drags Hisao to the roof to have lunch with Rin.", "Act 1"),
    ("Mind Your Step", "A30", "Hisao and Lilly go shopping, meeting a very confused Rin on the way back.", "Act 1"),
    ("Support", "A31", "Hisao has his first Saturday lesson, complete with a talking to from Mutou.", "Act 1"),
    ("An Aesthetics", "A32", "Emi finds Hisao slacking around after class and recruits him to help Rin once again.", "Act 1"),
    ("Creative Pain", "A33", "Hisao meets the art teacher, Nomiya, as Rin paints her mural.", "Act 1"),
    ("Proper Exercise", "A34", "Emi and Hisao discuss the importance of being in shape.", "Act 1"),
    ("Sip (Part 2)", "A35", "In an attempt to kill time, Hisao goes for a walk around the school.", "Act 1"),
    ("Shanghaied", "A36", "Tea, cake and competitions with Shizune and Misha at the Shanghai.", "Act 1"),
    ("Quiet", "A37", "Hanako and Hisao read books for the festival.", "Act 1"),
    ("Don't Panic", "A38", "After waking up on the day of the festival, Hisao is greeted by a ranting Kenji.", "Act 1"),
    ("Is Carnival!", "A39", "Emi catches Hisao eating fried food and makes him accompany her as punishment.", "Act 1"),
    ("Nc5xb3", "A42", "Unable to help Lilly at her stall, Hisao searches for Hanako at the festival.", "Act 1"),
    ("Movement", "H2", "Lilly finishes her duties and treats Hanako and Hisao to tea at the Shanghai.", "Act 1"),
    ("Promise of Time", "A41", "After a trying morning at her stall, Hisao takes Lilly to find Hanako.", "Act 1"),
    ("Clouds in My Head", "A40", "Hisao keeps Rin and her now-finished mural company.", "Act 1"),
    ("Throwing Balls", "A44", "True to his word, Hisao spends the day with Shizune and Misha.", "Act 1"),
    ("The Deep End", "A43", "Kenji and Hisao share a manly picnic on the roof instead of going to the festival.", "Act 1"),
    ("Act 2: Form", None, None, ("Act 2","Emi")),
    ("Morning Run", "E3", "The first of Hisao's many morning runs with Emi.", ("Act 2","Emi")),
    ("Clouds, Time Travel, and Thou", "E4", "Another rooftop lunch with Emi and Rin. Emi extracts from Hisao a promise to come see the track meet.", ("Act 2","Emi")),
    ("Questions That Need Answering!", "E5", "Idle chat between Emi and Hisao. Hisao asks Emi a few more questions about her relationship with Rin.", ("Act 2","Emi")),
    ("Second Time's the Worst", "E6", "The second morning run. Hisao is almost dragged kicking and screaming around the track.", ("Act 2","Emi")),
    ("An Apple a Day", "E7", "Hisao pays a visit to the nurse along with Emi, finding out that the two have known each other for a while.", ("Act 2","Emi")),
    ("Track Meeting", "E8", "The day of the track meet. Another facet of Emi's personality is revealed.", ("Act 2","Emi")),
    ("Down that Medicine Now", "E9", "Hisao mentions a pain in his chest during a visit to the nurse and receives a lecture.", ("Act 2","Emi")),
    ("Piracy on the High Seas", "E10", "Hisao discusses his future as a pirate with Emi on the rooftop, then a letter from Iwanako spoils his day.", ("Act 2","Emi")),
    ("Famous Last Words", "E11", "Emi and Rin take Hisao along for a picnic, soon to be spoiled by rain.", ("Act 2","Emi")),
    ("Tracking Absences", "E12", "Hisao goes to the track as usual, but Emi is missing.", ("Act 2","Emi")),
    ("Dropping By", "E13", "A bedside visit for a sick Emi, which quickly changes to something else entirely.", ("Act 2","Emi")),
    ("The First Morning After", "E14", "Hisao reminisces about last evening, deciding to do something to help Emi.", ("Act 2","Emi")),
    ("The (Real) Beginning", "E15", "Another lunchtime on the rooftop, sans Rin.", ("Act 2","Emi")),
    ("Act 3: Perspective", None, None, ("Act 3","Emi")),
    (u"Eet Ees… Scienca", "E16", "Mutou pulls Hisao into a short discussion about his future.", ("Act 3","Emi")),
    ("Definitions", "E17", "Emi and Hisao attempt another picnic, this time without any intervention from Mother Nature.", ("Act 3","Emi")),
    ("Invisible Rock", "E18", "Back to the track in the morning, with business as usual… or so it seems.", ("Act 3","Emi")),
    ("Lunch and Science", "E19", "Hisao sees Mutou again about his future in the sciences.", ("Act 3","Emi")),
    ("Up, Down, and Up Again", "E20", "A frantic call from Emi brings Hisao to her room, where two surprises await him.", ("Act 3","Emi")),
    ("Storage Space", "E21", "Emi coaxes Hisao into the track storage shed.", ("Act 3","Emi")),
    ("After-School Plans", "E22", "Emi has a serious talk with Hisao about the incoming exams.", ("Act 3","Emi")),
    ("Detached", "E23", "Hisao broods about his relationship with Emi.", ("Act 3","Emi")),
    ("Phantom Pain", "E24", "Hisao's attempt to show Emi his concern doesn't go nearly as well as he hoped.", ("Act 3","Emi")),
    ("Debate Expresses Doubt", "E25", "Hisao is confused by Emi's behavior and by an invitation to her house.", ("Act 3","Emi")),
    (u"Guess Who's Coming… Never Mind", "E26", "Dinner at the Ibarazaki's.", ("Act 3","Emi")),
    ("Instant Replay", "E27", "Things finally come to a head at the track.", ("Act 3","Emi")),
    ("Act 4: Motion", None, None, ("Act 4","Emi")),
    ("A Swing and a Miss", "E28", "Hisao wonders if Emi is purposefully avoiding him.", ("Act 4","Emi")),
    ("Saving Throw", "E29", "Things finally come to a head on the rooftop.", ("Act 4","Emi")),
    ("Whispers of the Past", "E30", "Hisao, Emi and her mom go for a graveside visit.", ("Act 4","Emi")),
    ("Hooray for Socks", "E31", "Sex, drugs, but no rock and roll.", ("Act 4","Emi")),
    ("Clean Teeth", "E32", "Hisao wakes up, finding Emi sleeping next to him.", ("Act 4","Emi")),
    ("Act 2: Hide and Seek", None, None, ("Act 2","Hanako")),
    ("To Town, To Town", "H3", "A shopping trip at the convenience store with Hanako.", ("Act 2","Hanako")),
    ("Tea Leaves", "H4", "Hanako invites Hisao to have lunch with her and Lilly.", ("Act 2","Hanako")),
    ("Office Confessional", "H5_1", "Hisao and Misha discuss the plight of Hanako.", ("Act 2","Hanako")),
    ("Chess and Slides", "H5_2", "Hisao ditches the Student Council to read with Hanako.", ("Act 2","Hanako")),
    ("Rise and Shine", "H6", "An invitation from Lilly to a tea party after hours.", ("Act 2","Hanako")),
    ("Mad Hatter", "H7", "Hanako, Hisao and Lilly meet together to have tea in Lilly's room.", ("Act 2","Hanako")),
    ("Small Change", "H8", "Kenji is forced to repay his loan.", ("Act 2","Hanako")),
    ("Absenteeism", "H9", "Hisao and Lilly discuss Hanako's school attendance.", ("Act 2","Hanako")),
    ("Equivalent Exchange", "H10", "In return for learning about his heart, Hanako reveals part of her past to Hisao.", ("Act 2","Hanako")),
    ("Act 3: Castling", None, None, ("Act 3","Hanako")),
    ("Invitation", "H11", "Lilly finds Hisao cleaning up the Tea Room and tells him about Hanako's birthday.", ("Act 3","Hanako")),
    ("Shady Encounter", "H12", "An unexpected chat with Miki while reminiscing about the past.", ("Act 3","Hanako")),
    ("Antiques and Pie", "H13", "Lilly and Hisao shop for a present in the city.", ("Act 3","Hanako")),
    ("Falling", "H14", "Hanako has a panic attack during class.", ("Act 3","Hanako")),
    ("Treading Softly", "H15", "Lilly has bad news to discuss with Hisao and Hanako.", ("Act 3","Hanako")),
    ("Reaching Out", "H16", "Hisao reaches out to a withdrawn Hanako.", ("Act 3","Hanako")),
    ("One More Year", "H17", "Our trio is joined by an unexpected guest as they celebrate Hanako's birthday party.", ("Act 3","Hanako")),
    ("One Piece of Paper", "H18", "Hisao enjoys his first hangover, before receiving a troubling letter.", ("Act 3","Hanako")),
    ("Stripes and Solids", "H19", "Heart-to-heart during a game of pool.", ("Act 3","Hanako")),
    ("Beginning of the End", "H20", "Lilly's departure for her trip.", ("Act 3","Hanako")),
    ("Act 4: Scars", None, None, ("Act 4","Hanako")),
    ("Truancy", "H21", "Lunch with the Student Council and worry about Hanako shutting herself in.", ("Act 4","Hanako")),
    ("Faraway Presence", "H22", "Hisao phones Lilly for advice after Hanako secludes herself for another day.", ("Act 4","Hanako")),
    ("Misstep", "H23", "Hisao tries to pull Hanako out of her room, with startling results.", ("Act 4","Hanako")),
    ("Cut Petals", "H24", "Hisao finds his future relationship with Hanako prematurely ended.", ("Act 4","Hanako")),
    ("Continuing Melody", "H25", "Hanako returns to class, to Hisao's relief.", ("Act 4","Hanako")),
    ("Shanghai Studiousness", "H26", "Attempting to avoid distractions, Hisao tries studying at the Shanghai.", ("Act 4","Hanako")),
    ("His Past", "H27", "In an attempt to come closer to Hanako, Hisao shares a part of his past with her.", ("Act 4","Hanako")),
    ("City Rendezvous", "H28", "The two share a date in the city.", ("Act 4","Hanako")),
    ("Whispered Touch", "H29", "Hisao and Hanako spend the night together.", ("Act 4","Hanako")),
    ("Indeterminate Future", "H30", "The events of the previous night weigh heavily on Hisao.", ("Act 4","Hanako")),
    ("Adulthood", "H31", "The end of two children, the beginning of two adults.", ("Act 4","Hanako")),
    ("Act 2: Past", None, None, ("Act 2","Lilly")),
    ("Earl Grey", "L1", "Hisao shares the first of many lunchbreaks with Hanako and Lilly, recovering from the day before.", ("Act 2","Lilly")),
    ("A Pound Sterling", "L2", "Questioned by Kenji on Lilly's nationality, Hisao decides to investigate and finds out a great deal more.", ("Act 2","Lilly")),
    ("Presents and Presence", "L3", "While out in search of a present for Hanako, Lilly and Hisao meet Akira and her cousin.", ("Act 2","Lilly")),
    ("Unidentified Drinking Object", "L4", "The trio hold a birthday party for Hanako, interrupted by the surprise appearance of a sibling.", ("Act 2","Lilly")),
    ("The Day After", "L5", "Hisao and Lilly awaken and try to recuperate from the previous evening's events.", ("Act 2","Lilly")),
    ("A Brief History of Thyme", "L6", "Hisao and Lilly go to get some groceries.", ("Act 2","Lilly")),
    ("Little Wing", "L7", "A shared lunch on the roof takes an unfortunate turn.", ("Act 2","Lilly")),
    ("Bon Voyage", "L8", "Lilly and Akira get seen off as they leave for a trip to their family in Scotland.", ("Act 2","Lilly")),
    ("Act 3: Present", None, None, ("Act 3","Lilly")),
    ("Day by Day", "L9", "Hisao idly lets a day without Lilly slip by, having a talk with Mutou about Yamaku.", ("Act 3","Lilly")),
    ("Minor Discord", "L10", "Hisao has lunch with Kenji, then gives some handouts to an alarmingly silent Hanako.", ("Act 3","Lilly")),
    ("Dissonance", "L11", "With Hanako withdrawing into herself completely, Hisao offers what little help he can before calling Lilly.", ("Act 3","Lilly")),
    ("A World Away", "L12", "Hisao's reassured mind begins to wonder about the relationship between he and Lilly.", ("Act 3","Lilly")),
    ("Renewal", "L13", "Hisao, Hanako, and Hideaki welcome Akira and Lilly after their return from Scotland.", ("Act 3","Lilly")),
    ("Northern Sojourn", "L14", "The trio begins their holiday in Hokkaido.", ("Act 3","Lilly")),
    ("Prelude", "L15", "A morning walk begins a chain of events.", ("Act 3","Lilly")),
    ("Crescendo", "L16", "Lilly's true feelings are told in the endless gold of the wheat fields." , ("Act 3","Lilly")),
    ("Diminuendo", "L17", "Our couple shares their first night together.", ("Act 3","Lilly")),
    ("Gray Outlook", "L18", "Confined to the summerhouse, Lilly and Hisao are forced to come to terms with their relationship.", ("Act 3","Lilly")),
    ("Rhapsody in Blue", "L19", "A bathing Hisao reflects on where he and Lilly are in life, before being joined by someone.", ("Act 3","Lilly")),
    ("The Momentary Present", "L20", "Traveling back to Yamaku, Hisao and Lilly idly talk between themselves.", ("Act 3","Lilly")),
    ("Act 4: Future", None, None, ("Act 4","Lilly")),
    ("Slow Steps 'Fore a Waltz", "L21", "Back at the school, the events of Hokkaido come to the fore.", ("Act 4","Lilly")),
    ("Pajamas and Suits", "L22", "Settling back into daily life. Akira joins the trio during one of their tea parties.", ("Act 4","Lilly")),
    ("Correct Procedure", "L23", "Hisao and Lilly arrange a date, before Akira swings by.", ("Act 4","Lilly")),
    ("Out and About", "L24", "Hisao and Lilly go on their first date, finding out about each other's pasts.", ("Act 4","Lilly")),
    ("A Morning's Reverie", "L25", "Hisao and Lilly discuss their ambitions for the future.", ("Act 4","Lilly")),
    ("Blackout", "L26", "The trio muse on the upcoming holidays, before Hisao experiences sight as Lilly does.", ("Act 4","Lilly")),
    ("Context", "L27", "Hisao gets called out by Akira and the two talk about her sibling.", ("Act 4","Lilly")),
    ("A Faraway Future", "L28", "Lilly reveals her family's offer to join them in Scotland.", ("Act 4","Lilly")),
    ("Farewell", "L29", "Farewells to Akira and Lilly the evening before they leave Japan.", ("Act 4","Lilly")),
    ("False Cadence", "L30", "Hisao rushes to confront Lilly, realizing her conflict.", ("Act 4","Lilly")),
    ("Under a Maudlin Sky", "L31", "Waking in the hospital ward, Hisao struggles to come to terms with his life.", ("Act 4","Lilly")),
    ("Under a Bright Sky", "L32", "Lilly rejoins Hisao, the two beginning their life together anew.", ("Act 4","Lilly")),
    ("Forwards, with Gusto!", "L33", "Lilly and Hisao see off Akira.", ("Act 4","Lilly")),
    ("Act 2: Disconnect", None, None, ("Act 2","Rin")),
    ("A Wider Field of Vision", "R1", "Hisao spends a lunch break with Rin watching clouds on the rooftop.", ("Act 2","Rin")),
    ("Studies in Grayscale", "R2", "Rin and Hisao draw portraits of each other at his first art club meeting.", ("Act 2","Rin")),
    (u"Interstitial", "R3", "Kenji lends a “borrowed” book to Hisao.", ("Act 2","Rin")),
    ("Self Study", "R4", "Misha and Shizune catch Hisao meditatively doodling during class.", ("Act 2","Rin")),
    ("Hisao's Smile", "R5", "Rin talks to Hisao about his happy expressions, or lack of them.", ("Act 2","Rin")),
    ("Things You Like", "R6", "Brief musings with Yuuko about books and Yamaku.", ("Act 2","Rin")),
    ("Target Audience", "R7", "The day of the track meet. Facets of Emi's and Rin's personalities get revealed.", ("Act 2","Rin")),
    ("Eternity In an Hour", "R8", "Nomiya incites discussion of art during a club meeting.", ("Act 2","Rin")),
    ("Underwater and a Maple with a Name", "R9", "Rin leads Hisao into the woods, where they ponder their immediate future.", ("Act 2","Rin")),
    ("Iwanako's Regret", "R10", "A letter from Iwanako arrives.", ("Act 2","Rin")),
    ("In Her Own Image", "R11", "Hisao pushes Rin to have her own art exhibition.", ("Act 2","Rin")),
    ("Umbrella Logic Cake", "R12", "Emi, Hisao and Rin get rained on and seek refuge in the Shanghai.", ("Act 2","Rin")),
    ("Six Meters Closer to Heaven", "R13", "Rin and Hisao DON'T eat lunch on the roof, due to a distinct lack of Emi.", ("Act 2","Rin")),
    ("Indecision", "R14", "Emi gets rid of her cold, while Rin catches her own.", ("Act 2","Rin")),
    ("Signal Interference", "R15", "Hisao goes visit Rin in her room.", ("Act 2","Rin")),
    ("Dandelions", "R16", "Conclusions get drawn on a hilltop.", ("Act 2","Rin")),
    ("Act 3: Distance", None, None, ("Act 3","Rin")),
    ("22nd Corner", "R17", "The art club team checks out the gallery for Rin's future exhibition.", ("Act 3","Rin")),
    ("The Scent of Light", "R18", "Hisao happens upon a sleeping Rin in the art room.", ("Act 3","Rin")),
    ("Things You Can't Give Up", "R19", "Emi and Hisao discuss Rin's personality.", ("Act 3","Rin")),
    ("BADAAN!", "R20", "Yuuko's thoughts on motivation.", ("Act 3","Rin")),
    ("Rose-Tinted Glasses", "R21", "Nomiya expounds at length about art as a career.", ("Act 3","Rin")),
    ("The Edge of the World", "R22", "Hisao confesses to Rin and gets shot down. Or does he?", ("Act 3","Rin")),
    ("The Context of Rin", "R23", "An awkward and silent afternoon at the atelier.", ("Act 3","Rin")),
    ("Fast Forward", "R23_2", "The preparations for the exhibition settle into a strange routine.", ("Act 3","Rin")),
    ("Self-Destruction", "R24", "Rin experiments with smoking to get a fresh look at creativity.", ("Act 3","Rin")),
    ("Reverse Escapism", "R25", "Hisao takes Rin on a walk through the night streets.", ("Act 3","Rin")),
    ("Boundless", "R26", "Sae and Nomiya give Hisao some insight on artists' lives.", ("Act 3","Rin")),
    ("Delirium", "R27", "Hisao surprises a desperate Rin in the atelier.", ("Act 3","Rin")),
    ("Things You Hate", "R28", "Unpleasant aftermath of an incredible night.", ("Act 3","Rin")),
    ("Shards of Ire", "R29", "The strained relationship between the two blows apart.", ("Act 3","Rin")),
    ("Act 4: Dream", None, None, ("Act 4","Rin")),
    ("Illusions for People", "R30", "Hisao talks about his misgivings to Nomiya, to little effect.", ("Act 4","Rin")),
    ("Demused", "R31", "Hisao's patience comes to an end.", ("Act 4","Rin")),
    ("The Scene", "R32", "Meeting with Rin at the exhibition opening.", ("Act 4","Rin")),
    ("Wavelength", "R35", "Hisao lethargically whiles away the last day of exams.", ("Act 4","Rin")),
    ("Blue Period", "R36", "A rainy day, the 22nd Corner, and a brief history of Picasso.", ("Act 4","Rin")),
    ("The World Only You Can See", "R37", "Rin and Hisao part after the rain.", ("Act 4","Rin")),
    ("Desperate Glory", "R34", "A frantic Nomiya queries Hisao about Rin's whereabouts.", ("Act 4","Rin")),
    ("Problems of Self-Referential Logic", "R38", "Hisao finds Rin in her hiding place, and convinces her to reconcile with Nomiya.", ("Act 4","Rin")),
    ("Measuring Shadows", "R39", "Rin's apology to the art teacher isn't well-received.", ("Act 4","Rin")),
    (u"Raison d'être", "R40", "Hisao comforts an upset Rin.", ("Act 4","Rin")),
    ("Without Breathing, Without a Sound", "R41", "On the first day of summer vacation, Rin comes to Hisao's room.", ("Act 4","Rin")),
    ("Proof of Existence", "R42", "Everything comes together on that dandelion-covered hilltop.", ("Act 4","Rin")),
    ("Act 2: Learning to Read", None, None, ("Act 2","Shizune")),
    ("Message Passing", "S8", "Shizune and Hisao explore methods of communication.", ("Act 2","Shizune")),
    ("Talk to the Hand", "S9", "Hisao begins studying a new language, and a tutor appears.", ("Act 2","Shizune")),
    ("Chinese Whispers", "S10", "Kenji manages to coerce Hisao to do a favor for him, but Hisao runs into trouble in many forms.", ("Act 2","Shizune")),
    ("Advanced Game Theory", "S11", "RISK isn't enough any more to satiate Shizune's hunger. What's worse, a new opponent makes her appearance.", ("Act 2","Shizune")),
    ("Bread, Scissors, Paper", "S12", "A lazy afternoon becomes dramatic as suddenly a piece of bread becomes an object of extreme interest.", ("Act 2","Shizune")),
    ("Interface", "S13", "Shizune and Hisao find a connection.", ("Act 2","Shizune")),
    ("Spring into Action", "S14", "Hisao has to mediate between Lilly and Shizune, but luckily things work out in the end.", ("Act 2","Shizune")),
    ("Past Imperfective", "S15", "The Student Council reminisces about past years while relaxing at the Shanghai.", ("Act 2","Shizune")),
    ("When Stars Embrace", "S16", "It's finally time for Tanabata!", ("Act 2","Shizune")),
    ("Act 3: Sleight of Hand", None, None, ("Act 3","Shizune")),
    ("Force Feedback", "S17", "Hisao finds out that Shizune is going to visit her family, and manages to come along.", ("Act 3","Shizune")),
    ("United Nations", "S18", "The trip to Shizune's house, meeting her little brother, and a sudden fishing contest.", ("Act 3","Shizune")),
    ("Use-Mention Distinction", "S19", "Hideaki tries to entertain Hisao for a day, meeting with little success.", ("Act 3","Shizune")),
    ("Family Plot", "S20", "Our trio meets Shizune's father and immediately beats a hasty retreat.", ("Act 3","Shizune")),
    ("Pangrammatic Window", "S21", "A request from Hideaki to learn sign language unexpectedly escalates into a shouting match with Jigoro.", ("Act 3","Shizune")),
    ("Closer", "S22", "Shizune and Hisao join together for the first time.", ("Act 3","Shizune")),
    ("Confrontation", "S23", "Jigoro belittles the Student Council and Hisao rises up to the challenge.", ("Act 3","Shizune")),
    ("The Anchor", "S24", "Back to Yamaku. A letter from Iwanako prompts a lengthy discussion from Kenji on the finer points of girlfriends.", ("Act 3","Shizune")),
    ("Roadmap", "S25", "The Student Council worries about their replacement, and Hisao ends up treating Misha to a parfait somehow.", ("Act 3","Shizune")),
    ("Acute Triangle", "S26", "An afternoon of work with Shizune shows Hisao that something is amiss between the girls.", ("Act 3","Shizune")),
    ("Dewey Decimated", "S27", "Yuuko gets Hisao to watch the library for her. The arrival of Kenji makes the attempt meet with mixed success.", ("Act 3","Shizune")),
    ("Tongue-Tied", "S28", "Misha visits Hisao in his room, and things go in an unexpected direction.", ("Act 3","Shizune")),
    ("Look Aside", "S29_1", "Hisao meets a depressed Misha on the roof. He ends up pushing her and Shizune together.", ("Act 3","Shizune")),
    ("Look Ahead", "S29_2", "Hisao meets a depressed Misha on the roof. Shizune joins them and pulls the whole council back to work.", ("Act 3","Shizune")),
    ("Act 4: To My Other Self", None, None, ("Act 4","Shizune")),
    ("Grand Strategy", "S30", "Shizune confesses to Hisao some of her goals and failures.", ("Act 4","Shizune")),
    ("Off by One", "S31", "A failed attempt to cheer up Misha gets converted into an impromptu date for Hisao and Shizune.", ("Act 4","Shizune")),
    ("Invasion", "S32", "Jigoro and Hideaki pay Shizune an unexpected and somewhat unpleasant visit.", ("Act 4","Shizune")),
    ("Parfait", "S33", "Hisao and Shizune stalk Misha. Hisao finally manages to corner her and discuss things properly.", ("Act 4","Shizune")),
    ("Present Tense", "S38", "Hisao stumbles into Lilly at lunch, and the two talk about Shizune.", ("Act 4","Shizune")),
    ("Spiral", "S39", "Runaround, stonewalling, and Kenji nighttime ambush.", ("Act 4","Shizune")),
    ("Terminal", "S40", "An early-morning talk with Shizune in the silent school.", ("Act 4","Shizune")),
    ("The Summit", "S34", "Kenji and Shizune meet in Hisao's room. Miraculously, nothing explodes.", ("Act 4","Shizune")),
    ("Succession", "S35", "The current Student Council shapes up their successors before engaging in “extracurricular activities.”", ("Act 4","Shizune")),
    ("Sneaking Mission", "S36", "The show of Misha's determination spurs Shizune to set her sights on greater things.", ("Act 4","Shizune")),
    ("Infinity", "S37", "Our trio renews their friendship, with their graduation looming close ahead.", ("Act 4","Shizune")),
)

rp_actmark = None
s_scenes_new = (("プロローグ", rp_actmark, rp_actmark, ("Act 1","Prologue")),
    ("寒空", "NOP1", "雪の降る寒い日、久夫の叶いかけた夢が、突然の心臓発作によって打ち砕かれる。", ("Act 1","Prologue")),
    ("失意の久夫", "NOP2", "久夫は山久学園のことを聞く。そこは、高校生活の残りを送ることになる場所。", ("Act 1","Prologue")),
    ("Act 1: 推定寿命", rp_actmark, rp_actmark, "Act 1"),
    ("入り口効果", "A1", "山久学園に足を踏み入れた久夫は、学級担任の武藤と会う。", "Act 1"),
    ("舞台上手へ", "A2", "クラスへの自己紹介、学級委員とその通訳との出会い。", "Act 1"),
    ("医療棟で", "A3", "ミーシャと静音に食堂へと案内された後、久夫はナースに会いに行く。", "Act 1"),
    ("空虚な部屋", "A4", "久夫は新しい部屋に移る途中、隣室の健二と会う。", "Act 1"),
    ("おしゃべり", "A5", "静音とミーシャは、久夫に学園祭が近いことを教え、昼食に誘う。", "Act 1"),
    ("リスクと報酬", "A6", "静音と久夫は、世界制覇を賭けたゲーム「リスク」で戦う。", "Act 1"),
    ("安らぎの紅茶", "A7", "図書室を探していて迷った久夫は、空き教室でリリーと出会う。", "Act 1"),
    ("図書室で二人", "A8", "図書室にたどり着いた久夫は華子と出会うが、彼女は怯えて逃げてしまう。", "Act 1"),
    ("奇怪千万", "A9", "健二が山久の隠された秘密を打ち明ける。", "Act 1"),
    ("昼ごはん進化論", "A10", "昼食を食べる場所を決める前に、静音とミーシャは久夫を生徒会に勧誘する。", "Act 1"),
    ("鋭い衝撃", "A11_1", "ミーシャと静音と一緒に昼食に行こうとした久夫は、廊下で笑美と衝突する。", "Act 1"),
    ("最悪の出会い", "A11_2", "華子とリリーと一緒に昼食に行こうとした久夫は、走ってきた笑美と衝突する。", "Act 1"),
    ("行きつく所へ", "A12", "静音とミーシャは、2人のお気に入りの茶館『上海』に久夫を連れていく。", "Act 1"),
    ("ティータイム (その1)", "A13", "久夫はリリーと華子と一緒に、穏やかな昼食をとる。", "Act 1"),
    ("習慣形成", "A15", "武藤は久夫に大事な話をしようとするが、ミーシャが割り込んで久夫に用事を頼む。", "Act 1"),
    ("遅弁", "A16", "資材を探していると、久夫は美術室で風変わりな少女と出会う。", "Act 1"),
    ("待ち伏せ", "A17", "琳を手伝ってペンキを運んでいると、久夫はナースに問い詰められる。", "Act 1"),
    ("あの緑", "A18", "久夫は琳が壁画を描くところを眺める。", "Act 1"),
    ("駆ける少女", "A19", "朝の運動に励もうとした久夫は、競技場のトラックで笑美と出会う。", "Act 1"),
    ("石鹸", "A20", "金を手に入れようとして、健二はシャワー室で久夫を狙う。", "Act 1"),
    ("冷戦", "A21", "静音とリリーは予算請求の件で火花を散らす。", "Act 1"),
    (u"やる気の証", "A22", "静音とミーシャは、生徒会に入るよう久夫をしつこく勧誘する。", "Act 1"),
    ("事象の地平線", "A22_2", "静音とミーシャは、生徒会に入るよう久夫をしつこく勧誘する。", "Act 1"),
    ("さらに上を目指して", "A23_1", "久夫は生徒会の崇高な責務について講義を受ける。", "Act 1"),
    ("自分ができること", "A23_2", "静音とミーシャの魔の手から逃れた久夫は、またも琳を手伝う。", "Act 1"),
    ("ペンキ塗り", "A24", "華子と久夫は、リリーのクラスの屋台作りに協力する。", "Act 1"),
    ("運動", "A25", "早朝、久夫と笑美はふたたび一緒にトラックを走る。", "Act 1"),
    ("透明帽子", "A26", "健二は久夫に、人付き合いの仕方についての秘訣を伝授する。", "Act 1"),
    ("ホームグラウンドの利点", "A26_1", "静音とミーシャは、授業に行こうと部屋を出る久夫を拉致する。", "Act 1"),
    ("緩やかな回復", "A27_1", "心臓の動悸から回復し、久夫はようやく授業に出席する。", "Act 1"),
    ("回復不可能", "A27_2", "生徒会に連れ去られた後、久夫は授業に戻ろうと悪戦苦闘する。", "Act 1"),
    ("無料の昼食なんてない", "A28", "正式なメンバーとして初めて、久夫は生徒会室に行く。", "Act 1"),
    ("足と口", "A29", "笑美は久夫を屋上まで連れて行き、琳と一緒に昼食をとる。", "Act 1"),
    ("足元に注意", "A30", "久夫とリリーは買い物に行き、帰り道で混乱状態の琳と会う。", "Act 1"),
    ("支え", "A31", "久夫にとって初めての土曜日の授業は、武藤の説教でしめくくられる。", "Act 1"),
    ("美学", "A32", "笑美は放課後に暇を持て余している久夫を見つけ、またしても琳の手伝いに駆り出す。", "Act 1"),
    ("産みの苦しみ", "A33", "琳が壁画を描いている間に、久夫は美術教師の野宮と出会う。", "Act 1"),
    ("適度な運動", "A34", "笑美と久夫は、健康維持の大切さについて話し合う。", "Act 1"),
    ("ティータイム (その2)", "A35", "暇をつぶすため、久夫は学園の周りを散歩する。", "Act 1"),
    ("上海航路", "A36", "静音とミーシャと一緒に『上海』へ。お茶、ケーキ、そして勝負。", "Act 1"),
    ("お静かに", "A37", "学園祭の前日、華子と久夫は読書をする。", "Act 1"),
    ("あわてるな", "A38", "学園祭当日、目を覚ました久夫はやかましく騒ぐ健二に迎えられる。", "Act 1"),
    ("学園祭 !", "A39", "笑美は久夫が揚げ物を食べているところを捕まえ、罰として久夫にお供をさせる。", "Act 1"),
    ("チェックメイト", "A42", "リリーの屋台を手伝えなかった久夫は、学園祭の中で華子を探す。", "Act 1"),
    ("ムーブメント", "H2", "リリーは自分の仕事を終えて、華子と久夫を上海のお茶でもてなす。", "Act 1"),
    ("時の約束", "A41", "リリーの屋台で骨の折れる午前を過ごした後、久夫は彼女といっしょに華子を探す。", "Act 1"),
    ("私の頭の中の雲", "A40", "久夫は、琳と完成した壁画のそばで過ごす。", "Act 1"),
    ("ボール投げ", "A44", "約束通りに、久夫は静音とミーシャと一緒に一日を過ごす。", "Act 1"),
    ("どん底", "A43", "学園祭を楽しむかわりに、健二と久夫は屋上で男らしいピクニックをする。", "Act 1"),
    ("Act 2: フォーム", rp_actmark, rp_actmark, ("Act 2","Emi")),
    ("朝練", "E3", "笑美とのたくさんのランニングのはじまり。", ("Act 2","Emi")),
    ("雲と時間旅行と汝", "E4", "再び笑美と琳と一緒の屋上の昼食。笑美は久夫に、陸上競技会を見に行くと約束させる。", ("Act 2","Emi")),
    ("答えの必要な質問 !", "E5", "笑美と久夫のたわいないおしゃべり。久夫は笑美に琳との関係をもっと詳しくたずねる。", ("Act 2","Emi")),
    ("2度目が一番最悪", "E6", "2度目の朝のランニング。久夫はじたばた叫びながらトラックのまわりを半ばひきずられていく。", ("Act 2","Emi")),
    ("一日一個のリンゴ", "E7", "久夫は笑美とともにナースを訪問し、以前から2人が知り合い同士だということを知る。", ("Act 2","Emi")),
    ("陸上競技会", "E8", "陸上競技会の日。笑美の性格の別の側面が明らかになる。", ("Act 2","Emi")),
    ("その薬、今すぐ飲め", "E9", "ナースの診察の際に久夫は胸の痛みのことを話し、説教を食らう。", ("Act 2","Emi")),
    ("大海原の海賊稼業", "E10", "久夫は屋上で笑美と海賊稼業について話し合うが、岩魚子からの手紙が彼の一日を台無しにする。", ("Act 2","Emi")),
    ("名台詞", "E11", "笑美、琳、久夫の3人でピクニックに出かけるが、すぐに雨によって台無しになってしまう。", ("Act 2","Emi")),
    ("欠席調査", "E12", "久夫は普段通りにトラックに行くが、笑美は来ない。", ("Act 2","Emi")),
    ("立ち寄り", "E13", "病気の笑美を見舞いに行ったとたん、事態は急展開する。", ("Act 2","Emi")),
    ("事後の朝", "E14", "久夫は昨日の出来事を回想し、笑美を助けるためになにかしようと決意する。", ("Act 2","Emi")),
    ("（本当の）始まり", "E15", "いつも通りの、しかし琳のいない、屋上でのランチタイム。", ("Act 2","Emi")),
    ("Act 3: パースペクティブ", rp_actmark, rp_actmark, ("Act 3","Emi")),
    (u"それは……科学です", "E16", "武藤は久夫に、将来について短い議論をする。", ("Act 3","Emi")),
    ("定義", "E17", "笑美と久夫はもう一度ピクニックを試みる、今度は母なる自然からの邪魔は入らない。", ("Act 3","Emi")),
    ("目に見えない岩", "E18", "いつも通りの、朝のトラックでの走り込み……と思いきや。", ("Act 3","Emi")),
    ("お昼ご飯と科学", "E19", "久夫は科学の道に進むことについて、武藤に再び相談する。", ("Act 3","Emi")),
    ("上がって、下がって、また上がり", "E20", "笑美からの取り乱した電話で久夫は笑美の部屋へ急ぐ。そこで2つの驚きが待っている。", ("Act 3","Emi")),
    ("体育倉庫", "E21", "笑美は久夫を陸上倉庫へと誘い込む。", ("Act 3","Emi")),
    ("放課後の予定", "E22", "次の試験について笑美は久夫と真剣な話をする。", ("Act 3","Emi")),
    ("切り離されて", "E23", "久夫は笑美との関係についてあれこれ考え込む。", ("Act 3","Emi")),
    ("幻肢痛", "E24", "久夫が笑美に心配していることを伝えようとするが、不本意な結果に終わる。", ("Act 3","Emi")),
    ("議論は疑念の現れ", "E25", "久夫は、笑美の振る舞いと笑美の家への招待に混乱する。", ("Act 3","Emi")),
    (u"お客さんは……やっぱりなし", "E26", "茨崎家での夕食。", ("Act 3","Emi")),
    ("リプレイ映像", "E27", "ついにトラックで事情が明らかになる。", ("Act 3","Emi")),
    ("Act 4: モーション", rp_actmark, rp_actmark, ("Act 4","Emi")),
    ("空振り", "E28", "久夫は笑美に避けられているのではと怪しむ。", ("Act 4","Emi")),
    ("セービングスロー", "E29", "ついに屋上で事情が明らかになる。", ("Act 4","Emi")),
    ("過去のささやき", "E30", "久夫、笑美、そして笑美の母親は墓参りに出かける。", ("Act 4","Emi")),
    ("靴下バンザイ", "E31", "セックス、ドラッグ、しかしロックンロールはなし。", ("Act 4","Emi")),
    ("きれいな歯", "E32", "久夫が目を覚ますと、笑美が自分の隣で眠っている。", ("Act 4","Emi")),
    ("Act 2: かくれんぼ", rp_actmark, rp_actmark, ("Act 2","Hanako")),
    ("町へ、町へ", "H3", "華子と一緒にコンビニまでお買いもの。", ("Act 2","Hanako")),
    ("茶葉", "H4", "華子は、リリーと一緒に昼食を食べようと久夫を誘う。", ("Act 2","Hanako")),
    ("懺悔の生徒会室", "H5_1", "久夫とミーシャは華子の苦境について話し合う。", ("Act 2","Hanako")),
    ("チェスとジェットコースター", "H5_2", "久夫は生徒会を放り出して、華子と一緒に本を読む。", ("Act 2","Hanako")),
    ("朝の目覚め", "H6", "リリーからの放課後ティーパーティーへの誘い。", ("Act 2","Hanako")),
    ("マッド・ハッター", "H7", "華子、久夫そしてリリーは一緒に集まって、リリーの部屋で紅茶を飲む。", ("Act 2","Hanako")),
    ("小さな変化", "H8", "健二は借金の返済を強いられる。", ("Act 2","Hanako")),
    ("無断欠席", "H9", "久夫とリリーは華子の出席状況について話し合う。", ("Act 2","Hanako")),
    ("等価交換", "H10", "久夫の心臓について知ったことのお返しに、華子は久夫に自分の過去の一部を打ち明ける。", ("Act 2","Hanako")),
    ("Act 3: キャスリング", rp_actmark, rp_actmark, ("Act 3","Hanako")),
    ("招待", "H11", "リリーは久夫が紅茶部屋を片付けているのを見つけ、華子の誕生日のことを話す。", ("Act 3","Hanako")),
    ("怪しい邂逅", "H12", "過去への回想と、思いがけない美貴との雑談。", ("Act 3","Hanako")),
    ("アンティークとパイ", "H13", "リリーと久夫は、街でプレゼントのための買い物をする。", ("Act 3","Hanako")),
    ("落下", "H14", "華子が授業中にパニック発作を起こす。", ("Act 3","Hanako")),
    ("ゆっくりと前へ", "H15", "リリーは久夫と華子に悪い知らせを伝える。", ("Act 3","Hanako")),
    ("手を伸ばして", "H16", "久夫は引きこもる華子に手を差し伸べる。", ("Act 3","Hanako")),
    ("もう一年", "H17", "華子の誕生日を祝っていると、我らが三人衆に意外なゲストが加わる。", ("Act 3","Hanako")),
    ("一枚の紙片", "H18", "久夫は初めての二日酔いを味わったあと、やっかいな手紙を受け取る。", ("Act 3","Hanako")),
    ("ソリッドとストライプ", "H19", "ポケットビリヤードで遊ぶ間の、率直な話し合い。", ("Act 3","Hanako")),
    ("終わりの始まり", "H20", "リリーの旅立ち。", ("Act 3","Hanako")),
    ("Act 4: キズアト", rp_actmark, rp_actmark, ("Act 4","Hanako")),
    ("ずる休み", "H21", "生徒会との昼食、そして閉じこもる華子への憂慮。", ("Act 4","Hanako")),
    ("遠くにありて", "H22", "華子はさらに一日引きこもり、久夫はリリーに助言を求めて電話する。", ("Act 4","Hanako")),
    ("つまずき", "H23", "久夫は華子を部屋から引き出そうとするが、驚愕する結果になる。", ("Act 4","Hanako")),
    ("切られた花弁", "H24", "久夫は、華子との自分の未来の関係が、早すぎる終わりを告げたことを知る。", ("Act 4","Hanako")),
    ("続くメロディ", "H25", "華子はクラスに戻り、久夫は安心する。", ("Act 4","Hanako")),
    ("上海で勉強", "H26", "気が散らないように、久夫は上海で勉強しようとする。", ("Act 4","Hanako")),
    ("彼の過去", "H27", "華子ともっと親しくなるために、久夫は自分の過去を華子と分かち合う。", ("Act 4","Hanako")),
    ("シティ・ランデブー", "H28", "2人は街でデートする。", ("Act 4","Hanako")),
    ("ささやきと接触", "H29", "久夫と華子は一夜を共に過ごす。", ("Act 4","Hanako")),
    ("不確かな未来", "H30", "昨夜の出来事が久夫に重くのしかかる。", ("Act 4","Hanako")),
    ("成熟", "H31", "2人の子供たちの終わり、2人の大人たちの始まり。", ("Act 4","Hanako")),
    ("Act 2: 過去", rp_actmark, rp_actmark, ("Act 2","Lilly")),
    ("アールグレイ", "L1", "昨日の疲れから回復し、久夫は華子とリリーと一緒の昼休みの最初の一日を、共に過ごす。", ("Act 2","Lilly")),
    ("1ポンド貨", "L2", "健二からリリーの国籍を問われた久夫は、それよりもっと詳しく調べようとする。", ("Act 2","Lilly")),
    ("プレゼントと存在", "L3", "華子のプレゼントを探している間、リリーと久夫は晃と彼女のいとこに出会う。", ("Act 2","Lilly")),
    ("未確認飲料物体", "L4", "3人は華子のために誕生日パーティーを開くが、きょうだいの突然の登場に中断される。", ("Act 2","Lilly")),
    ("あくる日", "L5", "目覚めた久夫とリリーは、昨夜の出来事から回復しようとする。", ("Act 2","Lilly")),
    ("華子、『タイム』を所望する", "L6", "久夫とリリーは食料品を買いに出かける。", ("Act 2","Lilly")),
    ("小さな翼", "L7", "屋上でみんなと分け合う昼食は残念な展開になる。", ("Act 2","Lilly")),
    ("旅立ち", "L8", "リリーと晃は見送られながら、スコットランドの家族に会いに旅立つ。", ("Act 2","Lilly")),
    ("Act 3: 現在", rp_actmark, rp_actmark, ("Act 3","Lilly")),
    ("一日、一日", "L9", "久夫はぼんやりと、リリーのいない日々が過ぎるにまかせ、山久について武藤と話す。", ("Act 3","Lilly")),
    ("小さな諍い", "L10", "久夫は健二と昼食をとり、気がかりなほど黙りこくっている華子にプリントを渡す。", ("Act 3","Lilly")),
    ("不協和音", "L11", "完全に引きこもる華子。久夫はできる限りの助けを申し出てから、リリーに電話する。", ("Act 3","Lilly")),
    ("遠い世界", "L12", "久夫は安心する一方、自分とリリーの関係について思いを巡らせる。", ("Act 3","Lilly")),
    ("再生", "L13", "久夫、華子、そして秀明は、スコットランドから帰ってきた晃とリリーを出迎える。", ("Act 3","Lilly")),
    ("北への旅", "L14", "3人で、北海道での休暇。", ("Act 3","Lilly")),
    ("前奏", "L15", "朝の散歩から、一連の出来事が始まる。", ("Act 3","Lilly")),
    ("クレッシェンド", "L16", "リリーの本当の気持ちが、果てしない黄金色の小麦畑で語られる。" , ("Act 3","Lilly")),
    ("ディミニュエンド", "L17", "一緒に過ごす初めての夜。", ("Act 3","Lilly")),
    ("前途は灰色", "L18", "夏の別荘に閉じ込められ、リリーと久夫は自分たちの関係を受け入れざるをえない。", ("Act 3","Lilly")),
    ("ラプソディ・イン・ブルー", "L19", "久夫が風呂に入りながらリリーとの関係を考えていると、何者かが一緒に入ってくる。", ("Act 3","Lilly")),
    ("一瞬の今", "L20", "山久に戻る旅路の間、久夫とリリーはぼんやりと2人で話す。", ("Act 3","Lilly")),
    ("Act 4: 未来", rp_actmark, rp_actmark, ("Act 4","Lilly")),
    ("ワルツの前のスローステップ", "L21", "学校に戻ると、北海道での出来事が話題になる。", ("Act 4","Lilly")),
    ("パジャマとスーツ", "L22", "日常生活に戻る。お茶会の間、晃が3人に加わる。", ("Act 4","Lilly")),
    ("正しい手順", "L23", "久夫とリリーはデートの約束をする。その後、晃が顔を出す。", ("Act 4","Lilly")),
    ("外出", "L24", "久夫とリリーは初めてのデートに行き、お互いの過去について知る。", ("Act 4","Lilly")),
    ("朝のまどろみ", "L25", "久夫とリリーは将来の抱負について話し合う。", ("Act 4","Lilly")),
    ("ブラックアウト", "L26", "3人は、近々やってくる休みについて考えにふけり、久夫はリリーの見ている視界を経験する。", ("Act 4","Lilly")),
    ("ことの成り行き", "L27", "久夫は晃に呼び出され、2人はリリーのことについて話す。", ("Act 4","Lilly")),
    ("遠い未来", "L28", "リリーはスコットランドの家族と一緒に暮らそうという家族の申し出を明らかにする。", ("Act 4","Lilly")),
    ("別れ", "L29", "2人が日本を離れる前の晩、晃とリリーにお別れを告げる。", ("Act 4","Lilly")),
    ("偽終止", "L30", "リリーの葛藤に気付いた久夫は、リリーに正面から向き合うために駆けつける。", ("Act 4","Lilly")),
    ("涙降る空の下で", "L31", "病院で目覚めた久夫は、自分の人生を受け入れようとして葛藤する。", ("Act 4","Lilly")),
    ("輝く空の下で", "L32", "リリーは久夫の元に戻り、2人は一緒の人生を新しく歩み始める。", ("Act 4","Lilly")),
    ("元気に前へ !", "L33", "リリーと久夫は晃を見送る。", ("Act 4","Lilly")),
    ("Act 2: すれ違い", rp_actmark, rp_actmark, ("Act 2","Rin")),
    ("広い視野", "R1", "久夫は昼休みを屋上で雲を見ながら琳と過ごす。", ("Act 2","Rin")),
    ("灰色の研究", "R2", "初めての美術部の活動で、琳と久夫はお互いのポートレートを描く。", ("Act 2","Rin")),
    (u"割り込み", "R3", "健二は久夫に「借りた」本を貸す。", ("Act 2","Rin")),
    ("自習", "R4", "ミーシャと静音は授業の間、瞑想にふけりながらいたずら書きをしている久夫を捕まえる。", ("Act 2","Rin")),
    ("久夫の笑顔", "R5", "琳は久夫に、彼の幸福な表情、あるいはその欠落について話す。", ("Act 2","Rin")),
    ("好きなもの", "R6", "本と山久について、優子との簡単な物思い。", ("Act 2","Rin")),
    ("対象視聴者", "R7", "陸上競技会の日。笑美のいろいろな面と琳のいろいろな性格が明らかになる。", ("Act 2","Rin")),
    ("永遠の1時間", "R8", "野宮が部活動で芸術について議論を喚起する。", ("Act 2","Rin")),
    ("水の中、名を持つ楓", "R9", "琳は久夫を森林へといざない、そこで2人は近い将来のことをじっくり考える。", ("Act 2","Rin")),
    ("岩魚子の後悔", "R10", "岩魚子からの手紙が届く。", ("Act 2","Rin")),
    ("彼女自身のイメージで", "R11", "久夫は琳が自分の作品の展覧会を開くのを後押しする。", ("Act 2","Rin")),
    ("傘と論理とケーキ", "R12", "笑美、久夫そして琳は雨に降られて、上海に避難する。", ("Act 2","Rin")),
    ("天国に6メートル近く", "R13", "琳と久夫は、笑美がいないのが明らかなので、屋上で昼食を食べ「ない」。", ("Act 2","Rin")),
    ("優柔不断", "R14", "笑美は風邪を治すが、今度は琳が風邪を引いてしまう。", ("Act 2","Rin")),
    ("シグナル・インタフェース", "R15", "久夫は琳を部屋に訪ねる。", ("Act 2","Rin")),
    ("たんぽぽ", "R16", "丘の上で結論が下される。", ("Act 2","Rin")),
    ("Act 3: 溝", rp_actmark, rp_actmark, ("Act 3","Rin")),
    ("22番目の角", "R17", "美術部チームは琳の将来の展覧会のために画廊を下見する。", ("Act 3","Rin")),
    ("光の薫り", "R18", "久夫は美術室で眠っている琳に偶然遭遇する。", ("Act 3","Rin")),
    ("諦められないもの", "R19", "笑美と久夫は琳の人となりについて話し合う。", ("Act 3","Rin")),
    ("バターン !", "R20", "モチベーションについての、優子の考察。", ("Act 3","Rin")),
    ("バラ色メガネを通して", "R21", "野宮は芸術を職業とすることについて長々と説明する。", ("Act 3","Rin")),
    ("世界の果て", "R22", "久夫は琳に告白して、振られる。本当に？", ("Act 3","Rin")),
    ("琳の状況", "R23", "アトリエの奇妙でしんとした午後。", ("Act 3","Rin")),
    ("早送り", "R23_2", "展覧会の準備は奇妙なパターンにはまる。", ("Act 3","Rin")),
    ("自己破壊", "R24", "琳は創造性について新鮮な見方をするために、たばこを試す。", ("Act 3","Rin")),
    ("非現実逃避", "R25", "久夫は琳を夜道の散歩へと連れ出す。", ("Act 3","Rin")),
    ("限界の欠如", "R26", "さえと野宮は久夫に芸術家の生き様についていくつかの見識を説く。", ("Act 3","Rin")),
    ("錯乱", "R27", "久夫はアトリエで自暴自棄になっている琳を驚かす。", ("Act 3","Rin")),
    ("大嫌いなもの", "R28", "信じられない夜の不愉快な結末。", ("Act 3","Rin")),
    ("怒りのかけら", "R29", "緊迫した2人の関係はバラバラに吹き飛ぶ。", ("Act 3","Rin")),
    ("Act 4: 夢", rp_actmark, rp_actmark, ("Act 4","Rin")),
    ("人々のための幻想", "R30", "久夫は自分の不安を野宮に伝えるが、ほとんど効果はない。", ("Act 4","Rin")),
    ("物思いから醒まされて", "R31", "久夫の忍耐は終わりを迎える。", ("Act 4","Rin")),
    ("問題のシーン", "R32", "展覧会のオープニングでの、琳との遭遇。", ("Act 4","Rin")),
    ("波長", "R35", "久夫は、試験の最終日、無気力にダラダラと過ごす。", ("Act 4","Rin")),
    ("青の時代", "R36", "雨の降る日、22nd Corner、そしてピカソの略史。", ("Act 4","Rin")),
    ("君だけに見える世界", "R37", "琳と久夫は雨のあとで、別れる。", ("Act 4","Rin")),
    ("絶望的な栄光", "R34", "取り乱した野宮は久夫に琳の居場所について問いただす。", ("Act 4","Rin")),
    ("自己参照論理の問題", "R38", "久夫は琳が隠れているのを見つけ、野宮に謝るよう説得する。", ("Act 4","Rin")),
    ("影を測る", "R39", "琳の美術教師への謝罪は、歓迎されない。", ("Act 4","Rin")),
    (u"レゾンデートル", "R40", "久夫は動転する琳をなぐさめる。", ("Act 4","Rin")),
    ("息もなく、音もなく", "R41", "夏休みの初めの日に、琳が久夫の部屋にやってくる。", ("Act 4","Rin")),
    ("存在の証明", "R42", "たんぽぽに覆われた丘の上で、すべてがあるべき場所に収まる。", ("Act 4","Rin")),
    ("Act 2: 読む練習", rp_actmark, rp_actmark, ("Act 2","Shizune")),
    ("伝言のやりとり", "S8", "静音と久夫はコミュニケーションの手段を探る。", ("Act 2","Shizune")),
    ("手に向かって話しかけて", "S9", "久夫は新しい言語を勉強し始め、個人指導者が登場する。", ("Act 2","Shizune")),
    ("伝言ゲーム", "S10", "健二は久夫に無理矢理頼み事をするが、久夫はさまざまな困難に見舞われる。", ("Act 2","Shizune")),
    ("上級ゲーム理論", "S11", "もうリスクゲームでは静音の飢えを満たせない。さらに新しい敵までもが登場する。", ("Act 2","Shizune")),
    ("じゃん・けん・パン", "S12", "一切れのパンが突然強烈な興味の対象になり、けだるげな午後が劇的なものに変わる。", ("Act 2","Shizune")),
    ("インターフェイス", "S13", "静音と久夫はつながりを見出す。", ("Act 2","Shizune")),
    ("即時対応", "S14", "久夫はリリーと静音の仲裁をするはめになるが、幸い最後には丸く収まる。", ("Act 2","Shizune")),
    ("過去不完全型", "S15", "上海でくつろいでいる間、生徒会は過去の年月を回想する。", ("Act 2","Shizune")),
    ("星々が抱き合うとき", "S16", "ついに七夕の日が来た！", ("Act 2","Shizune")),
    ("Act 3: 器用な手つき", rp_actmark, rp_actmark, ("Act 3","Shizune")),
    ("フォースフィードバック", "S17", "久夫は静音が実家に戻るのを知って、ついて行くことに成功する。", ("Act 3","Shizune")),
    ("国際連合", "S18", "静音の実家への旅、彼女の弟との出会い、そして突然の魚釣り競争。", ("Act 3","Shizune")),
    ("使用と言及の区別", "S19", "秀明は久夫をもてなそうとするが、あまりうまくいかない。", ("Act 3","Shizune")),
    ("家族陰謀", "S20", "我らが三人衆は静音の父に会い、すぐさま早々に引き上げる。", ("Act 3","Shizune")),
    ("パングラム", "S21", "秀明の手話を学びたいという要望は、治五郎との怒鳴りあいという予想外の事態に発展する。", ("Act 3","Shizune")),
    ("もっとそばに", "S22", "静音と久夫は、はじめて、ひとつになる。", ("Act 3","Shizune")),
    ("対決", "S23", "治五郎が生徒会を過小評価するので、久夫はその挑戦を受けて立つ。", ("Act 3","Shizune")),
    ("錨", "S24", "山久に戻る。岩魚子からの手紙と、ガールフレンドの詳細について健二の長話。", ("Act 3","Shizune")),
    ("ロードマップ", "S25", "生徒会は自分たちの後任について心配し、久夫はなぜかミーシャにパフェをおごるはめになる。", ("Act 3","Shizune")),
    ("鋭角三角関係", "S26", "静音との午後の仕事で、久夫は静音とミーシャの仲がぎくしゃくしていることを見て取る。", ("Act 3","Shizune")),
    ("十進分類法", "S27", "優子は久夫に図書室の番を頼む。健二の到着で、その試みは半分失敗、半分成功する。", ("Act 3","Shizune")),
    ("もつれる舌", "S28", "ミーシャは久夫を部屋に訪ねる。そして物事は予想しない方向へ向かう。", ("Act 3","Shizune")),
    ("脇を見て", "S29_1", "久夫は落ち込んだミーシャと屋上で出会う。そしてミーシャと静音を無理矢理引き合わせる。", ("Act 3","Shizune")),
    ("正面を見て", "S29_2", "久夫は落ち込んだミーシャと屋上で出会う。静音は2人に合流し、みんなを仕事にひき戻す。", ("Act 3","Shizune")),
    ("Act 4: もう一人の私へ", rp_actmark, rp_actmark, ("Act 4","Shizune")),
    ("大戦略", "S30", "静音は久夫に自身の目標と失敗を告白する。", ("Act 4","Shizune")),
    ("わずかなずれ", "S31", "ミーシャを元気づけようという失敗した試みは、久夫と静音の即興デートに変化する。", ("Act 4","Shizune")),
    ("侵略", "S32", "治五郎と秀明が突然静音を訪れるが、どこか不愉快なものに終わる。", ("Act 4","Shizune")),
    ("パフェ", "S33", "久夫と静音はミーシャのあとをつける。久夫はとうとうミーシャを追い詰め、きちんと話をする。", ("Act 4","Shizune")),
    ("現在形", "S38", "久夫は昼食の時、リリーに偶然出会い、2人は静音について話す。", ("Act 4","Shizune")),
    ("らせん", "S39", "その場しのぎの言い逃れ、はぐらかし、そして健二の夜襲。", ("Act 4","Shizune")),
    ("終焉", "S40", "沈黙の学園で静音と早朝の会話。", ("Act 4","Shizune")),
    ("頂点", "S34", "健二と静音が久夫の部屋で邂逅する。奇跡的に、何も爆発しない。", ("Act 4","Shizune")),
    ("引き継ぎ", "S35", "課外活動に従事する前に、在任中の生徒会が後任を鍛え上げる。", ("Act 4","Shizune")),
    ("隠密行動", "S36", "ミーシャが示した決意は、静音がより広い物事に目を向けるのに拍車をかける。", ("Act 4","Shizune")),
    ("無限", "S37", "卒業を間近に控え、我らが3人は友情を新しくする。", ("Act 4","Shizune")),
)

characters["Hisao"] = "久夫"
characters["Hanako"] = "華子"
characters["Emi"] = "笑美"
characters["Rin"] = "琳"
characters["Lilly"] = "リリー"
characters["Shizune"] = "静音"
characters["Misha"] = "ミーシャ"
characters["Kenji"] = "健二"
characters["Mutou"] = "武藤"
characters["Nurse"] = "ナース"
characters["Nomiya"] = "野宮"
characters["Yuuko"] = "優子"
characters["Sae"] = "さえ"
characters["Akira"] = "晃"
characters["Hideaki"] = "秀明"
characters["Jigoro"] = "治五郎"
characters["Meiko"] = "芽依子"
characters["Shopkeep"] = "店主"
characters["Miki"] = "美貴"
characters["???"] = "？？？"
characters["{s}Shizune{/s} Misha"] = "{s}静音{/s} ミーシャ"
characters["Purple-haired girl"] = "紫色の髪の少女"
characters["Twintails girl"] = "ツインテールの少女"
characters["Strange girl"] = "謎の少女"
characters["Wavy-haired girl"] = "ウェーブヘアの少女"
characters["Laughing girl"] = "笑っている少女"
characters["Bespectacled hallmate"] = "眼鏡をかけた生徒"
characters["Tall man"] = "背の高い男"
characters["Librarian"] = "司書"
characters["Silver-haired man"] = "白髪の男"
characters["Gallery owner"] = "画廊のオーナー"
characters["Well-dressed person"] = "身なりの良い人"
characters["Smiling man"] = "笑っている男"
characters["Slim girl"] = "スリムな少女"
characters["Woman with braid"] = "三つ編みの女性"
characters["Huge man"] = "大男"

drugs["Disopyramide"] = "ジソピラミド"
drugs["Warfarin"] = "ワルファリン"
drugs["Diltiazem"] = "ジルチアゼム"
drugs["Felodipine"] = "フェロジピン"
drugs["Propanolol"] = "プロプラノロール"
drugs["Penbutolol"] = "ペンブトロール"
drugs["Carteolol"] = "カルテオロール"
drugs["Procainamide"] = "プロカインアミド"
drugs["Heparin"] = "ヘパリン"
drugs["Phenytoin"] = "フェニトイン"
drugs["Verapamil"] = "ベラパミル"
drugs["Quinidine"] = "キニジン"
drugs["Flecainide"] = "フレカイニド"
drugs["5mg/day"] = "5mg/日"
drugs["400mg/day"] = "400mg/日"
drugs["15ml/day"] = "15ml/日"
drugs["100mg/day"] = "100mg/日"
drugs["10ml/48hrs"] = "10ml/48時間"
drugs["10ml/day"] = "10ml/日"
drugs["200mg/12hrs"] = "200mg/12時間"
drugs["50mg/12hrs"] = "50mg/12時間"
drugs["500mg/48hrs"] = "500mg/48時間"
drugs["125mg/12hrs"] = "125mg/12時間"
drugs["25ml/day"] = "25ml/日"
drugs["nightmares"] = "悪夢"
drugs["decreased concentration"] = "集中力低下"
drugs["bradycardia"] = "徐脈"
drugs["clinical depression"] = "鬱病"
drugs["insomnia"] = "不眠症"
drugs["erectile dysfunction"] = "勃起不全"
drugs["abnormal vision"] = "視覚異常"
drugs["heart failure"] = "心臓麻痺"
drugs["nausea"] = "悪心"
drugs["dizziness"] = "眩暈"
drugs["hallucinations"] = "幻覚"
drugs["bronchospasm"] = "気管支痙攣"
drugs["dyspnea"] = "呼吸困難"
drugs["fatigue"] = "疲労"
drugs["hypotension"] = "低血圧"
drugs["heart block"] = "心臓ブロック"
drugs["cold extremities"] = "四肢冷感"
drugs["diarrhea"] = "下痢"
drugs["cardiac arrest"] = "心停止"
drugs["ventricular fibrillation"] = "心室細動"
drugs["ataxia"] = "失調症"
drugs["asthma"] = "喘息"

# Append KV to translates
translates["“"] = "「"
translates["”"] = "」"
translates["(replay)"] = "(リプレイ)"
translates["No scene"] = "シーンなし"
translates["Nothing"] = "何もない"
translates["Playing history"] = "プレイ履歴"
translates["Watching video"] = "ビデオを見る"
translates["In main menu"] = "メインメニュー"
translates["Listening"] = "聴く"
translates["Act 1"] = "Act 1"


def cleanup_key(key: str):
    return (key
            .strip()
            .replace("“", "'")
            .replace("”", "'")
            .replace("‘", "'")
            .replace("’", "'"))

for old, new in zip(s_scenes_old, s_scenes_new):
    if old[1] != new[1]:
        print(f"Scene ID mismatch: {old[1]} != {new[1]}")
        exit(1)
    translates[cleanup_key(old[0])] = new[0]
    if old[2] is not None:
        translates[cleanup_key(old[2])] = new[2]

tl = open(sys.argv[1], "r", encoding="utf-8-sig").readlines()

pre = "    "
for i in range(len(tl)):
    t = tl[i].strip()

    if t.startswith("# TODO"):
        # Skip TODOs
        continue

    if t.startswith("old \""):
        tl_key = t[5:-1]
        if tl_key in translates.keys():
            tl[i+1] = f"{pre}new \"{translates[tl_key]}\"\n"
        elif cleanup_key(tl_key) in translates.keys():
            tl[i+1] = f"{pre}new \"{translates[cleanup_key(tl_key)]}\"\n"
        elif tl_key in characters.keys():
            tl[i+1] = f"{pre}new \"{characters[tl_key]}\"\n"
        else:
            print(f"missing: {tl_key}")
            exit(1)
#
# tl.append("\n")
# for drug_key in drugs.keys():
#     tl.append(f"{pre}drug \"{drug_key}\" \"{drugs[drug_key]}\"\n")

open("tl-" + sys.argv[1], "w", encoding="utf8").write("".join(tl))
