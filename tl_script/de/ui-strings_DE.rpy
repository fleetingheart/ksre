init -2 python:





    init_language("de")

    displayDict["de"].styleoverrides = {"font": mainfont,
                                        "language": "western",
                                        "line_spacing": 0}

    displayDict["de"].timeformat = "%b %d, %H:%M"

    displayDict["de"].selector_padding = 0 
    displayDict["de"].nvl_paragraph_distance = 10 

    displayDict["de"].sayfont = mainfont

    displayDict["de"].quote_outer_open = u"“"
    displayDict["de"].quote_outer_close = u"”"
    displayDict["de"].quote_inner_open = u"‘"
    displayDict["de"].quote_inner_close = u"’"

    displayDict["de"].activeLanguage = "Deutsch"
    displayDict["de"].allLanguages = {}
    displayDict["de"].allLanguages["de"] = displayDict["de"].activeLanguage
    displayDict["de"].allLanguages["en"] = "Englisch"
    displayDict["de"].allLanguages["it"] = "Italienisch"
    displayDict["de"].allLanguages["fr"] = u"Französisch"
    displayDict["de"].allLanguages["es"] = "Spanisch"
    displayDict["de"].allLanguages["jp"] = "Japanisch"

    displayDict["de"].act_term = u"Akt"

    displayDict["de"].main_menu_start = u"Start"
    displayDict["de"].main_menu_load = u"Laden"
    displayDict["de"].main_menu_extra = u"Extras"
    displayDict["de"].main_menu_config = u"Optionen"
    displayDict["de"].main_menu_quit = u"Beenden"

    displayDict["de"].game_menu_return = u"Zurück"
    displayDict["de"].game_menu_show = u"Bild anzeigen"
    displayDict["de"].game_menu_history = u"Textarchiv"
    displayDict["de"].game_menu_skip = u"Skip-Modus"
    displayDict["de"].game_menu_auto = u"Auto-Modus"
    displayDict["de"].game_menu_config = u"Optionen"
    displayDict["de"].game_menu_save = u"Speichern"
    displayDict["de"].game_menu_load = u"Laden"
    displayDict["de"].game_menu_main = u"Hauptmenü"
    displayDict["de"].game_menu_quit = u"Beenden"
    displayDict["de"].game_menu_current_scene = u"Aktuelle Szene"
    displayDict["de"].game_menu_current_music = u"Aktuelles Musikstück"
    displayDict["de"].game_menu_replay_indicator = u"Wiederholung"

    displayDict["de"].return_button_text = u"Zurück"

    displayDict["de"].hdisabled_label = u"Nur jugendfreie Inhalte zeigen"
    displayDict["de"].config_page_caption = u"Optionen"
    displayDict["de"].config_fullscreen_label = u'Vollbildmodus'
    displayDict["de"].config_transitions_label = u'Übergänge deaktivieren'
    displayDict["de"].config_skip_unseen_label = u'Ungelesene Texte überspringen'
    displayDict["de"].config_skip_after_choice_label = u'Überspringen nach Wahlpunkten'
    displayDict["de"].config_textspeed_label = u'Textgeschwindigkeit'
    displayDict["de"].config_afmspeed_label = u'Verzögerung Auto-Modus'
    displayDict["de"].config_musicvol_label = u"Musiklautstärke"
    displayDict["de"].config_musicvol_jukebox_label = u"Vol."
    displayDict["de"].config_sfxvol_label = u"SFX Lautstärke"
    displayDict["de"].config_sfxtest_label = u"Test"
    displayDict["de"].config_gamepad_label = u"Tastenbelegung Gamepad…"

    displayDict["de"].config_language_sel = u"Sprachauswahl…"
    displayDict["de"].config_language_caption = u"Optionen > Sprachauswahl"
    displayDict["de"].config_language_restart_note = u"Hinweis: Wenn im laufenden Spiel eine andere Sprache ausgewählt wird, wird das Spiel an der letzten Textabzweigung fortgesetzt."

    displayDict["de"].gamepad_caption = u"Optionen > Tastenbelegung Gamepad"
    displayDict["de"].gamepad_key_na = u"Nicht zugewiesen"
    displayDict["de"].gamepad_request_key = u"Knopf drücken, dem “%s” zugewiesen werden soll.\n.Um die Belegung zurückzusetzen, Maus klicken oder Select-Taste betätigen."

    displayDict["de"].yesno_okay = u"Fortsetzen"
    displayDict["de"].yesno_savesuccess = u"Spielstand erfolgreich gespeichert."
    displayDict["de"].yesno_quit = u"Willst du Katawa Shoujo\nwirklich beenden?"
    displayDict["de"].yesno_return_to_main = u"Willst du wirklich zum\nHauptmenü zurückkehren?"
    displayDict["de"].save_page_caption = u"Speichern"
    displayDict["de"].new_save_button = u"Neuen Spielstand anlegen"
    displayDict["de"].load_page_caption = u"Laden"
    displayDict["de"].yesno_load_in_game = u"Willst du deinen Fortschritt\nwirklich nicht speichern?"
    displayDict["de"].yesno_save_overwrite = u"Willst du diesen Spielstand\nwirklich überschreiben?"
    displayDict["de"].yesno_delete_savegame = u"Willst du diesen Spielstand\nwirklich löschen?"
    displayDict["de"].play_time_label = u"Spielzeit"
    displayDict["de"].show_manual_saves = u"Manuell"
    displayDict["de"].show_auto_saves = u"Automatisch"

    displayDict["de"].text_history_caption = u"Textarchiv"
    displayDict["de"].text_history_note = u"Hinweis"

    displayDict["de"].extra_menu_caption = "Extras"
    displayDict["de"].extra_music_button_label = "Spieldose"
    displayDict["de"].extra_gallery_button_label = "Galerie"
    displayDict["de"].extra_scene_button_label = u"Bücherei"
    displayDict["de"].extra_omake_button_label = "Omake"
    displayDict["de"].extra_opening_button_label = "Kino"
    displayDict["de"].commentary_label = u"Kommentare ermöglichen"

    displayDict["de"].video_page_caption = "Extras > Kino"


    displayDict["de"].music_page_caption = "Extras > Spieldose"
    displayDict["de"].music_stop_button_text = "Stopp"
    displayDict["de"].music_now_playing = "Gerade gespielt"

    displayDict["de"].gallery_page_caption = "Extras > Galerie"
    displayDict["de"].gallery_onelocked = "Ein Bild noch nicht freigespielt."
    displayDict["de"].gallery_manylocked = u"%d Bilder noch nicht freigespielt."
    displayDict["de"].gallery_singlelocked = u"Bild %d von %d ist noch nicht freigespielt."
    displayDict["de"].gallery_num_page_prefix = "Seite"
    displayDict["de"].gallery_num_page_error = "Keine Bilder darstellbar"

    displayDict["de"].scene_page_caption = u"Extras > Bücherei"
    displayDict["de"].scene_completion_label = u"Spielstand: %s%%"
    displayDict["de"].scene_playthrough_label = u"Bereits gewählte Entscheidungen markieren (empfohlen)"
    displayDict["de"].scene_launch_path = u"Möchtest du wirklich die\ngesamte Route beginnen?"

    displayDict["de"].name_ha_ = u"Mädchen mit violettem Haar"
    displayDict["de"].name_emi_ = u"Mädchen mit Zöpfen"
    displayDict["de"].name_rin_ = u"Seltsames Mädchen"
    displayDict["de"].name_li_ = u"Mädchen mit gewelltem Haar"
    displayDict["de"].name_mi_ = u"Lachendes Mädchen"
    displayDict["de"].name_ke_ = "Flurnachbar mit Brille"
    displayDict["de"].name_mu_ = "Großer Mann"
    displayDict["de"].name_yu_ = "Bibliothekarin"
    displayDict["de"].name_no_ = "Mann mit silbernem Haar"
    displayDict["de"].name_sa_ = "Galeristin"
    displayDict["de"].name_aki_ = "Gut angezogene Person"
    displayDict["de"].name_nk_ = u"Lächelnder Mann"
    displayDict["de"].name_hh_ = u"Schlankes Mädchen"
    displayDict["de"].name_emm_ = "Frau mit Zopf"
    displayDict["de"].name_hx_ = "Riesiger Mann"







    displayDict["de"].s_scenes = ((u"Prolog", rp_actmark, rp_actmark, (u"Akt 1",u"Prolog")),
                                    (u"Kaltstart", u"NOP1", u"An einem kalten, verschneiten Tag durchkreuzt ein Herzanfall Hisaos Träume, kurz bevor sie in Erfüllung gehen.", ("Act 1",u"Prolog")),
                                    (u"Hisao-Bündel", u"NOP2", u"Hisao erfährt von der Yamaku-Akademie, wo er wahrscheinlich den Rest seiner Schulzeit verbringen muss.", ("Act 1",u"Prolog")),
                                    (u"Akt 1: Lebenserwartung", rp_actmark, rp_actmark, "Act 1"),
                                    (u"Eintrittseffekt", u"A1", u"Hisao betritt zum ersten Mal die Yamaku-Akademie und trifft seinen Klassenlehrer, Mutou.", "Act 1"),
                                    (u"Auftritt von Links", u"A2", u"Vorstellung vor der Klasse und das Treffen mit der Klassensprecherin und ihrer Übersetzerin.", "Act 1"),
                                    (u"Pflegerversicherung", u"A3", u"Misha und Shizune zeigen Hisao die Cafeteria, danach sucht er den Chefpfleger auf.", "Act 1"),
                                    (u"Niemandes Raum", u"A4", u"Hisao bezieht sein neues Zimmer und trifft dabei auf seinen Flurnachbarn Kenji.", "Act 1"),
                                    (u"Smalltalk", u"A5", u"Shizune und Misha erzählen Hisao vom anstehenden Schulfest und laden ihn zum Essen ein.", "Act 1"),
                                    (u"Risiko und Chance", u"A6", u"Shizune und Hisao kämpfen in einer Partie Risiko um die Weltherrschaft.", "Act 1"),
                                    (u"Orientierungslos", u"A7", u"Auf der Suche nach der Bibliothek verläuft sich Hisao und trifft in einem ungenutzten Klassenzimmer auf Lilly.", "Act 1"),
                                    (u"Gemeinsame Bibliothek", u"A8", u"Nachdem Hisao endlich die Bibliothek gefunden hat, trifft und verschreckt er Hanako.", "Act 1"),
                                    (u"Bizarr und Surreal", u"A9", u"Kenji enthüllt die finsteren Geheimnisse der Yamaku.", "Act 1"),
                                    (u"Evolutionstheorie zum Essen", u"A10", u"Shizune und Misha drängeln Hisao in den Schülerrat, bevor sie über das Mittagessen diskutieren.", "Act 1"),
                                    (u"Kurz und Schmerzhaft", u"A11_1", u"Auf dem Weg zum Mittagessen mit Shizune und Misha kollidiert Hisao auf dem Flur mit Emi.", "Act 1"),
                                    (u"Atemberaubend Niedlich", u"A11_2", u"Auf dem Weg zum Mittagessen mit Hanako und Lilly kollidiert Hisao mit Emi, die über die Flure tobt.", "Act 1"),
                                    (u"Umleitung Voraus", u"A12", u"Shizune und Misha bringen Hisao in ihr Lieblingsteehaus, das Shanghai.", "Act 1"),
                                    (u"Nippen (Teil 1)", u"A13", u"Hisao verbringt ein friedliches Mittagessen mit Lilly und Hanako.", "Act 1"), 
                                    (u"Stärkt den Charakter", u"A15", u"Mutou versucht ein ernstes Gespräch mit Hisao zu führen, aber Misha unterbricht sie und hat Arbeit für Hisao", "Act 1"),
                                    (u"Eine Private Mahlzeit", u"A16", u"Auf der Suche nach Material stößt Hisao im Kunstraum auf ein seltsames Mädchen.", "Act 1"),
                                    (u"Wegelagerei", u"A17", u"Hisao hilft Rin, einige Farbdosen zu tragen, und wird von Doc ausgefragt.", "Act 1"),
                                    (u"Das Andere Grün", u"A18", u"Hisao schaut Rin beim Malen des Wandgemäldes zu.", "Act 1"),
                                    (u"Das Rennende Mädchen", u"A19", u"Beim ersten Frühsport begegnet Hisao auf dem Sportplatz Emi.", "Act 1"),
                                    (u"Seife", u"A20", u"Kenji legt sich in der Dusche auf die Lauer, um Hisao etwas Geld abzuknöpfen.", "Act 1"),
                                    (u"Kalter Krieg", u"A21", u"Shizune und Lilly streiten sich über Budgetpläne.", "Act 1"),
                                    (u"Kompetenznachweis", u"A22", u"Shizune und Misha überfallen Hisao und wollen ihn zu einem Teil des Schülerrats machen.", "Act 1"),
                                    (u"Ereignishorizont", u"A22_2", u"Shizune und Misha überfallen Hisao und wollen ihn zu einem Teil des Schülerrats machen.", "Act 1"),
                                    (u"Erwartungen Übertreffen", u"A23_1", u"Hisao bekommt einen Vortrag über die hehren Pflichten des Schülerrats.", "Act 1"),
                                    (u"Was Du Tun Kannst", u"A23_2", u"Hisao entkommt den Fängen Shizunes und Mishas und hilft wieder Rin.", "Act 1"),
                                    (u"Malen nach Zahlen", u"A24", u"Hanako und Hisao gehen Lillys Klasse zur Hand und helfen beim Bau ihres Standes.", "Act 1"),
                                    (u"Training", u"A25", u"An einem neuen Morgen sehen sich Hisao und Emi auf der Laufbahn wieder.", "Act 1"),
                                    (u"Der Unsichtbare Hut", u"A26", u"Kenji gibt Hisao ein paar Insidertipps, wie er besser unter die Leute kommt.", "Act 1"),
                                    (u"Heimvorteil", u"A26_1", u"Shizune und Misha schnappen sich Hisao, als er zum Unterricht will.", "Act 1"),
                                    (u"Keine Erholung", u"A27", False, "Act 1"), 
                                    (u"Langsame Erholung", u"A27_1", u"Hisao erholt sich von seinem Herzflimmern und schafft es noch zum Unterricht.", "Act 1"),
                                    (u"Keine Erholung", u"A27_2", u"Hisao quält sich zum Unterricht, nachdem er vom Schülerrat kassiert worden ist.", "Act 1"),
                                    (u"Nichts ist Umsonst", u"A28", u"Hisao wird an seinem ersten Tag im Amt zum Schülerratsbüro eskortiert.", "Act 1"),
                                    (u"Hand und Fuß", u"A29", u"Emi schleppt Hisao auf das Dach der Schule, um dort zusammen mit Rin zu essen.", "Act 1"),
                                    (u"Ohne Ziel", u"A30", u"Hisao und Lilly gehen einkaufen und treffen auf dem Rückweg eine sehr verwirrte Rin.", "Act 1"),
                                    (u"Unterstützung", u"A31", u"Hisao hat seinen ersten Samstagsunterricht und ein ernstes Gespräch mit Mutou.", "Act 1"),
                                    (u"Farbenleere", u"A32", u"Emi entdeckt Hisao beim Nichtstun und rekrutiert ihn wieder einmal, um Rin zu Helfen.", "Act 1"),
                                    (u"Wehen des Schaffens", u"A33", u"Hisao trifft den Kunstlehrer Nomiya, während Rin an ihrem Wandgemälde arbeitet.", "Act 1"),
                                    (u"Richtiges Training", u"A34", u"Emi und Hisao besprechen, wie wichtig es ist, in Form zu sein.", "Act 1"),
                                    (u"Nippen (Teil 2)", u"A35", u"Um Zeit totzuschlagen, macht Hisao sich zu einen Spaziergang um die Schule auf", "Act 1"),
                                    (u"Schanghaien", u"A36", u"Tee, Kuchen und Wettstreit mit Shizune und Misha im Shanghai.", "Act 1"),
                                    (u"Stille", u"A37", u"Hanako und Hisao lesen zusammen Bücher vor dem Schulfest.", "Act 1"),
                                    (u"Keine Panik", u"A38", u"Hisao wacht am Tag des Schulfestes auf und wird von einem fluchenden Kenji begrüßt.", "Act 1"),
                                    (u"Karneval!", u"A39", u"Emi ertappt Hisao beim Fastfoodessen und zwingt ihn zur Strafe, sie den ganzen Tag zu begleiten.", "Act 1"),
                                    (u"Nc5xb3", u"A42", u"Hisao kann Lilly am Stand nicht helfen und macht sich auf die Suche nach Hanako.", "Act 1"),
                                    (u"Bewegung", u"H2", u"Lilly ist mit ihrem Dienst fertig und läd Hanako und Hisao zum Tee ins Shanghai ein.", "Act 1"), 
                                    (u"Versprechen der Zeit", u"A41", u"Nach einem anstrengendem Vormittag an ihrem Stand begleitet Hisao Lilly auf der Suche nach Hanako.", "Act 1"),
                                    (u"Wolken in meinem Kopf", u"A40", u"Hisao leistet Rin und ihrem vollendeten Wandgemälde Gesellschaft.", "Act 1"),
                                    (u"Bälle Werfen", u"A44", u"Hisao hält sein Versprechen und verbringt den Tag mit Shizune und Misha.", "Act 1"),
                                    (u"In die Tiefe", u"A43", u"Kenji und Hisao machen ein männliches Picknick auf dem Dach, anstatt zum Schulfest zu gehen.", "Act 1"),
                                    (u"Akt 2: Form", rp_actmark, rp_actmark, ("Act 2",u"Emi")),
                                    (u"Frühsport", u"E3", u"Das erste von Hisaos vielen morgendlichen Trainings mit Emi.", ("Act 2",u"Emi")),
                                    (u"Wolken, Zeitreisen und Du", u"E4", u"Ein weiteres Mittagessen auf dem Dach mit Emi und Rin. Emi entlockt Hisao das Versprechen zum Sportfest zu kommen.", ("Act 2",u"Emi")),
                                    (u"Fragen ohne Antworten", u"E5", u"Smalltalk zwischen Emi und Hisao. Hisao fragt Emi über ihre Beziehung zu Rin aus.", ("Act 2",u"Emi")),
                                    (u"Das Zweite Mal ist das Schlimmste", u"E6", u"Das zweite Morgentraining. Hisao quält sich über den Sportplatz.", ("Act 2",u"Emi")),
                                    (u"Ein gelöstes Siegel", u"E7", u"Hisao besucht mit Emi zusammen Doc und findet heraus, dass die beiden sich schon länger kennen.", ("Act 2",u"Emi")),
                                    (u"Wettrennen", u"E8", u"Das Sportfest. Eine weitere Facette von Emis Persönlichkeit wird enthüllt.", ("Act 2",u"Emi")),
                                    (u"Es ist Arznei, nicht Gift…", u"E9", u"Hisao erwähnt bei einem Besuch bei Doc einen Brustschmerz und wird zurechtgewiesen.", ("Act 2",u"Emi")),
                                    (u"Piraten der Sieben Meere", u"E10", u"Hisao bespricht seine Zukunft als Pirat mit Emi auf dem Dach, dann verdirbt ihm ein Brief von Iwanako den Tag.", ("Act 2",u"Emi")),
                                    (u"Berühmte Letzte Worte", u"E11", u"Emi und Rin nehmen Hisao mit auf ein Picknick, das bald von Regen unterbrochen wird.", ("Act 2",u"Emi")),
                                    (u"Laufend Abwesend", u"E12", u"Hisao geht wie üblich zum Sportplatz, aber Emi ist nicht da.", ("Act 2",u"Emi")),
                                    (u"Besuchszeit", u"E13", u"Ein Krankenbesuch bei Emi, der sich schnell zu etwas ganz anderem entwickelt.", ("Act 2",u"Emi")),
                                    (u"Der Erste Morgen Danach", u"E14", u"Hisao denkt über den vorigen Abend nach und beschließt, etwas für Emi zu tun.", ("Act 2",u"Emi")),
                                    (u"Der (Wahre) Anfang", u"E15", u"Ein weiteres Mittagessen auf dem Dach - dieses Mal ohne Rin.", ("Act 2",u"Emi")),
                                    (u"Akt 3: Perspektive", rp_actmark, rp_actmark, ("Act 3",u"Emi")),
                                    (u"Eet Ees… Scienca", u"E16", u"Mutou führt mit Hisao ein kurzes Gespräch über dessen Zukunft.", ("Act 3",u"Emi")),
                                    (u"Definitionen", u"E17", u"Emi und Hisao probieren ein weiteres Picknick, dieses Mal ohne Eingriffe von Mutter Natur.", ("Act 3",u"Emi")),
                                    (u"Stolperfalle", u"E18", u"Morgens zurück auf dem Sportplatz; alles wie immer… so scheint es zumindest.", ("Act 3",u"Emi")),
                                    (u"Mittagessen und Wissenschaft", u"E19", u"Hisao spricht wieder mit Mutou über seine Zukunft in der Wissenschaft.", ("Act 3",u"Emi")),
                                    (u"Hoch, Runter und wieder Hoch", u"E20", u"Ein panischer Anruf von Emi bringt Hisao zu ihrem Zimmer, wo ihn zwei Überraschungen erwarten.", ("Act 3",u"Emi")),
                                    (u"Stauraum", u"E21", u"Emi lockt Hisao in den Materialschuppen am Sportplatz.", ("Act 3",u"Emi")),
                                    (u"Nach der Schule", u"E22", u"Emi hat ein ernstes Gespräch mit Hisao über die anstehenden Prüfungen.", ("Act 3",u"Emi")),
                                    (u"Losgelöst", u"E23", u"Hisao denkt über seine Beziehung mit Emi nach.", ("Act 3",u"Emi")), 
                                    (u"Phantomschmerz", u"E24", u"Hisaos Versuch, mit Emi über seine Sorgen zu reden, läuft nicht so gut wie er gehofft hatte.", ("Act 3",u"Emi")),
                                    (u"Debatte unentschieden", u"E25", u"Hisao ist verwirrt von Emi's Verhalten und von einer Einladung zu ihr nach Hause.", ("Act 3",u"Emi")),
                                    (u"Rate wer zum Essen kommt", u"E26", u"Abendessen bei den Ibarazakis.", ("Act 3",u"Emi")),
                                    (u"Letzte Chance", u"E27", u"Auf dem Sportplatz kommt es zur alles entscheidenden Begegnung.", ("Act 3",u"Emi")),
                                    (u"Akt 4: Bewegung", rp_actmark, rp_actmark, ("Act 4",u"Emi")),
                                    (u"Schwung, Schlag… und Vorbei", u"E28", u"Hisao fragt sich, ob Emi ihm absichtlich aus dem Weg geht.", ("Act 4",u"Emi")),
                                    (u"Rettungswurf", u"E29", u"Auf dem Dach kommt es zur alles entscheidenden Begegnung.", ("Act 4",u"Emi")),
                                    (u"Stimmen der Vergangenheit", u"E30", u"Hisao, Emi und ihre Mutter besuchen ein Grab.", ("Act 4",u"Emi")),
                                    (u"Ein Hoch auf Socken", u"E31", u"Sex, Drogen, aber kein Rock and Roll.", ("Act 4",u"Emi")),
                                    (u"Saubere Zähne", u"E32", u"Hisao wacht auf, während Emi neben ihm schläft.", ("Act 4",u"Emi")),
                                    (u"Akt 2: Versteckspiel", rp_actmark, rp_actmark, ("Act 2",u"Hanako")),
                                    (u"Auf in die Stadt", u"H3", u"Eine Einkaufstour zusammen mit Hanako.", ("Act 2",u"Hanako")),
                                    (u"Teeblätter", u"H4", u"Hanako lädt Hisao ein, mit Ihr und Lilly zu essen.", ("Act 2",u"Hanako")),
                                    (u"Beichtbüro", u"H5_1", u"Hisao und Misha unterhalten sich über Hanakos Probleme.", ("Act 2",u"Hanako")),
                                    (u"Schach und Achterbahnen", u"H5_2", u"Hisao reißt vor dem Schülerrat aus, um mit Hanako zu lesen.", ("Act 2",u"Hanako")),
                                    (u"Frühaufsteher", u"H6", u"Eine Einladung von Lilly zu einer abendlichen Teeparty.", ("Act 2",u"Hanako")),
                                    (u"Der Verrückte Hutmacher", u"H7", u"Hanako, Hisao und Lilly treffen sich zum Teetrinken in Lillys Zimmer.", ("Act 2",u"Hanako")),
                                    (u"Kleingeld", u"H8", u"Kenji wird gezwungen seinen Kredit abzubezahlen.", ("Act 2",u"Hanako")),
                                    (u"Abwesenheit", u"H9", u"Hisao und Lilly unterhalten sich über Hanakos Anwesenheitsquote.", ("Act 2",u"Hanako")),
                                    (u"Äquivalenter Austausch", u"H10", u"Nachdem Hisao ihr von seinem Herzen erzählt hat, erzählt Hanako ihm etwas über ihre Vergangenheit.", ("Act 2",u"Hanako")),
                                    (u"Akt 3: Rochaden", rp_actmark, rp_actmark, ("Act 3",u"Hanako")),
                                    (u"Einladung", u"H11", u"Lilly trifft Hisao beim Aufräumen des Teeraums und erzählt ihm von Hanakos Geburtstag.", ("Act 3",u"Hanako")),
                                    (u"Begegnung im Schatten", u"H12", u"Erinnerungen an die Vergangenheit und ein unerwartetes Gespräch mit Miki.", ("Act 3",u"Hanako")),
                                    (u"Antiquitäten und Kuchen", u"H13", u"Lilly und Hisao kaufen in der Stadt Geschenke ein.", ("Act 3",u"Hanako")),
                                    (u"Fallen", u"H14", u"Hanako hat im Unterricht einen Panikanfall.", ("Act 3",u"Hanako")),
                                    (u"Auf Leisen Sohlen", u"H15", u"Lilly hat schlechte Nachrichten für Hisao und Hanako.", ("Act 3",u"Hanako")),
                                    (u"Sich Sorgen", u"H16", u"Hisao sorgt sich um Hanako, die sich auf ihr Zimmer zurückgezogen hat.", ("Act 3",u"Hanako")),
                                    (u"Ein Jahr Älter", u"H17", u"Ein unerwarteter Gast erscheint zu Hanakos Geburtstagsfeier.", ("Act 3",u"Hanako")),
                                    (u"Ein Blatt Papier", u"H18", u"Hisao genießt seinen ersten Kater, und erhält dann einen unerwünschten Brief.", ("Act 3",u"Hanako")),
                                    (u"Volle und Halbe", u"H19", u"Aussprache bei einem Billardspiel.", ("Act 3",u"Hanako")),
                                    (u"Anfang vom Ende", u"H20", u"Lillys Abreise nach Schottland.", ("Act 3",u"Hanako")),
                                    (u"Akt 4: Narben", rp_actmark, rp_actmark, ("Act 4",u"Hanako")),
                                    (u"Fehlzeiten", u"H21", u"Mittagessen mit dem Schülerrat und Sorge um Hanako, die sich in ihrem Zimmer einschließt.", ("Act 4",u"Hanako")),
                                    (u"Ferne Präsenz", u"H22", u"Hisao bittet Lilly per Telefon um Rat, nachdem Hanako sich einen weiteren Tag nicht blicken lässt.", ("Act 4",u"Hanako")),
                                    (u"Fehltritt", u"H23", u"Hisao versucht, Hanako aus ihrem Zimmer zu holen - mit überraschendem Ergebnis.", ("Act 4",u"Hanako")),
                                    (u"Schnittblumen", u"H24", u"Hisaos zukünftige Beziehung mit Hanako wird vorzeitig beendet.", ("Act 4",u"Hanako")),
                                    (u"Das Leben Geht Weiter", u"H25", u"Hanako kommt zu Hisaos Erleichterung in die Klasse zurück.", ("Act 4",u"Hanako")),
                                    (u"Studium im Shanghai", u"H26", u"Um Ablenkungen zu vermeiden, geht Hisao zum Lernen ins Shanghai.", ("Act 4",u"Hanako")),
                                    (u"Seine Vergangenheit", u"H27", u"Um Hanako näher zu kommen, erzählt Hisao ihr von seiner Vergangenheit.", ("Act 4",u"Hanako")),
                                    (u"Rendevouz in der Stadt", u"H28", u"Die zwei gehen zusammen in die Stadt.", ("Act 4",u"Hanako")),
                                    (u"Geflüsterte Berührung", u"H29", u"Hisao und Hanako verbringen die Nacht zusammen.", ("Act 4",u"Hanako")),
                                    (u"Unbestimmte Zukunft", u"H30", u"Die Ereignisse der vergangenen Nacht lasten schwer auf Hisao.", ("Act 4",u"Hanako")),
                                    (u"Erwachsen Werden", u"H31", u"Das Ende von zwei Kindern, der Anfang von zwei Erwachsenen.", ("Act 4",u"Hanako")),
                                    (u"Akt 2: Vergangenheit", rp_actmark, rp_actmark, ("Act 2",u"Lilly")),
                                    (u"Earl Grey", u"L1", u"Hisao verbringt die erste von vielen Mittagspausen mit Hanako und Lilly und erholt sich vom Vortag.", ("Act 2",u"Lilly")),
                                    (u"Ein Pfund Sterling", u"L2", u"Nachdem Kenji ihn nach Lillys Nationalität gefragt hat, fragt Hisao nach und lernt noch eine ganze Menge mehr.", ("Act 2",u"Lilly")),
                                    (u"Präsente und Präsenz", u"L3", u"Während sie nach einen Geschenk für Hanako suchen, treffen Lilly und Hisao Akira und ihren Cousin.", ("Act 2",u"Lilly")),
                                    (u"Unbekanntes Trinkobjekt", u"L4", u"Bei Hanakos Geburtstagsfeier taucht überraschend Lillys Schwester auf.", ("Act 2",u"Lilly")),
                                    (u"Der Tag Danach", u"L5", u"Hisao und Lilly wachen auf und versuchen, sich von den Ereignissen des Vorabends zu erholen.", ("Act 2",u"Lilly")),
                                    (u"Das Universum in der Nussschale", u"L6", u"Hisao und Lilly gehen Lebensmittel einkaufen.", ("Act 2",u"Lilly")),
                                    (u"Kleine Flügel", u"L7", u"Ein gemeinsames Essen auf dem Dach nimmt eine unglückliche Wendung.", ("Act 2",u"Lilly")),
                                    (u"Bon Voyage", u"L8", u"Lilly und Akira werden auf ihre Reise zu ihrer Familie nach Schottland verabschiedet.", ("Act 2",u"Lilly")),
                                    (u"Akt 3: Gegenwart", rp_actmark, rp_actmark, ("Act 3",u"Lilly")),
                                    (u"Tag für Tag", u"L9", u"Hisao verbringt seine Tage ohne Lilly, und unterhält sich mit Mutou über die Yamaku.", ("Act 3",u"Lilly")),
                                    (u"Kleiner Misston", u"L10", u"Hisao isst mit Kenji zu Mittag, und bringt dann einer erschreckend stillen Hanako Unterrichtsmaterial vorbei.", ("Act 3",u"Lilly")),
                                    (u"Dissonanz", u"L11", u"Als Hanako sich völlig in sich zurückzieht, versucht Hisao erst zu helfen und ruft dann Lilly an.", ("Act 3",u"Lilly")),
                                    (u"Am Anderen Ende der Welt", u"L12", u"Nachdem er sich beruhigt hat denkt Hisao über seine Beziehung zu Lilly nach.", ("Act 3",u"Lilly")),
                                    (u"Erneuerung", u"L13", u"Hisao, Hanako, und Hideaki begrüßen Akira und Lilly nach ihrer Rückkehr aus Schottland.", ("Act 3",u"Lilly")),
                                    (u"Aufenthalt im Norden", u"L14", u"Die drei fahren in den Urlaub nach Hokkaido.", ("Act 3",u"Lilly")),
                                    (u"Vorspiel", u"L15", u"Bei einem Morgenspaziergang beginnt eine Kette von Ereignissen.", ("Act 3",u"Lilly")),
                                    (u"Crescendo", u"L16", u"Lillys wahre Gefühle werden in einem goldenen Weizenfeld ausgesprochen.u" , ("Act 3",u"Lilly")),
                                    (u"Diminuendo", u"L17", u"Unser Paar verbringt seine erste Nacht zusammen.", ("Act 3",u"Lilly")),
                                    (u"Trübe Aussichten", u"L18", u"In das Sommerhaus eingesperrt, müssen Lilly und Hisao sich über ihre Beziehung klar werden.", ("Act 3",u"Lilly")),
                                    (u"Rhapsodie in Blau", u"L19", u"Ein badender Hisao denkt über sich und Lily nach, als jemand zu ihm kommt.", ("Act 3",u"Lilly")),
                                    (u"Dieser Augenblick", u"L20", u"Auf dem Rückweg zur Yamaku unterhalten sich Hisao und Lilly.", ("Act 3",u"Lilly")),
                                    (u"Akt 4: Zukunft", rp_actmark, rp_actmark, ("Act 4",u"Lilly")),
                                    (u"Walzer Tanzt Man Langsam", u"L21", u"Zurück in der Schule, werden die Ereignisse von Hokkaido nochmal zum Thema.", ("Act 4",u"Lilly")),
                                    (u"Pyjamas und Anzüge", u"L22", u"Der tägliche Trott setzt wieder ein. Akira besucht das Trio bei einer Teeparty.", ("Act 4",u"Lilly")),
                                    (u"Richtige Verfahrensweise", u"L23", u"Hisao und Lilly planen ein Date, bevor Akira zu Besuch kommt.", ("Act 4",u"Lilly")),
                                    (u"Unterwegs", u"L24", u"Hisao und Lilly gehen auf ihr erstes Date, und erfahren von der Vergangenheit des jeweils anderen.", ("Act 4",u"Lilly")),
                                    (u"Morgenträumerei", u"L25", u"Hisao und Lilly sprechen über ihre Pläne für die Zukunft.", ("Act 4",u"Lilly")),
                                    (u"Schwarz", u"L26", u"Die Drei unterhalten sich über die bevorstehenden Ferien; dann erfährt Hisao wie Lilly sich fühlen muss.", ("Act 4",u"Lilly")),
                                    (u"Kontext", u"L27", u"Hisao trifft sich mit Akira, und die beiden unterhalten sich über ihre Schwester.", ("Act 4",u"Lilly")),
                                    (u"Eine Ferne Zukunft", u"L28", u"Lilly erzählt von dem Angebot ihrer Familie zu ihnen nach Schottland zu kommen.", ("Act 4",u"Lilly")),
                                    (u"Abschied", u"L29", u"Abschied von Akira und Lilly am Vorabend ihrer Abreise aus Japan.", ("Act 4",u"Lilly")),
                                    (u"Falsche Kadenz", u"L30", u"Hisao glaubt, Lilly verstanden zu haben, und eilt ihr hinterher.", ("Act 4",u"Lilly")),
                                    (u"Unter Trübem Himmel", u"L31", u"Nach dem Aufwachen im Krankenhaus, versucht Hisao sich mit seinem Leben abzufinden.", ("Act 4",u"Lilly")),
                                    (u"Unter Klarem Himmel", u"L32", u"Lilly kehrt zu Hisao zurück, und die zwei fangen ihr gemeinsames Leben noch einmal an.", ("Act 4",u"Lilly")),
                                    (u"Vorwärts, mit Elan!", u"L33", u"Lilly und Hisao verabschieden Akira.", ("Act 4",u"Lilly")),
                                    (u"Akt 2: Losgelöst", rp_actmark, rp_actmark, ("Act 2",u"Rin")),
                                    (u"Ein Besserer Überblick", "R1", u"Hisao beobachtet in der Mittagspause mit Rin die Wolken am Himmel.", ("Act 2",u"Rin")),
                                    (u"Graustudien", "R2", u"Rin und Hisao zeichnen bei seinem ersten Kunstklubtreffen Portraits voneinander.", ("Act 2",u"Rin")),
                                    (u"Interstitiell", "R3", u"Kenji leiht Hisao ein “geborgtes” Buch aus.", ("Act 2",u"Rin")),
                                    (u"Selbststudien", "R4", u"Misha und Shizune erwischen Hisao wie er im Unterricht zeichnet.", ("Act 2",u"Rin")),
                                    (u"Hisaos Lächeln", "R5", u"Rin redet mit Hisao über seinen fröhlichen Gesichtsausdruck, oder das Fehlen desselben.", ("Act 2",u"Rin")),
                                    (u"Was Du Magst", "R6", u"Kurzer Austausch mit Yuuko über Bücher und die Yamaku.", ("Act 2",u"Rin")),
                                    (u"Zielgruppe", "R7", u"Das Sportfest. Facetten von Emis und Rins Persönlichkeiten werden enthüllt.", ("Act 2",u"Rin")),
                                    (u"Ewigkeit in einer Stunde", "R8", u"Nomiya stößt während des Klubtreffens eine Diskussion über Kunst an.", ("Act 2",u"Rin")),
                                    (u"Unter Wasser und ein Ahorn mit Namen", "R9", u"Rin führt Hisao in den Wald, wo sie über ihre nähere Zukunft nachdenken.", ("Act 2",u"Rin")),
                                    (u"Iwanakos Reue", "R10", u"Ein Brief von Iwanako kommt an.", ("Act 2",u"Rin")),
                                    (u"Nach Ihrem Eigenen Bildnis", "R11", u"Hisao überredet Rin ihre Kunst ausstellen zu lassen.", ("Act 2",u"Rin")),
                                    (u"Regenschirm, Logik und Kuchen", "R12", u"Emi, Hisao und Rin geraten in den Regen und suchen Zuflucht im Shanghai.", ("Act 2",u"Rin")),
                                    (u"Sechs Meter Näher am Himmel", "R13", u"Rin und Hisao essen NICHT auf dem Dach zu Mittag, weil Emi nicht da ist.", ("Act 2",u"Rin")),
                                    (u"Unschlüssigkeit", "R14", u"Emi wird ihre Erkältung los, während Rin sich eine einfängt.", ("Act 2",u"Rin")),
                                    (u"Signalstörung", "R15", u"Hisao besucht Rin in ihrem Zimmer.", ("Act 2",u"Rin")),
                                    (u"Pusteblumen", "R16", u"Auf einem Hügel werden Entscheidungen getroffen.", ("Act 2",u"Rin")),
                                    (u"Akt 3: Distanziert", rp_actmark, rp_actmark, ("Act 3",u"Rin")),
                                    (u"22nd Corner", "R17", u"Hisao, Rin und Nomiya besuchen die Galerie, in der Rins Ausstellung stattfinden soll.", ("Act 3",u"Rin")),
                                    (u"Der Geruch des Lichts", "R18", u"Hisao findet im Kunstraum eine schlafende Rin.", ("Act 3",u"Rin")),
                                    (u"Was Du Nicht Aufgeben Kannst", "R19", u"Emi und Hisao sprechen über Rins Persönlichkeit.", ("Act 3",u"Rin")),
                                    (u"KABUMM!", "R20", u"Yuukos Gedanken zum Thema Motivation.", ("Act 3",u"Rin")),
                                    (u"Durch die Rosa Brille", "R21", u"Nomiya hält einen langwierigen Vortrag über eine Karriere als Künstler.", ("Act 3",u"Rin")),
                                    (u"Der Rand der Welt", "R22", u"Hisao gesteht Rin seine Gefühle und wird abgewiesen - oder doch nicht?", ("Act 3",u"Rin")),
                                    (u"Thema “Rin”", "R23", u"Ein peinlich stiller Nachmittag im Atelier.", ("Act 3",u"Rin")),
                                    (u"Schneller Vorlauf", u"R23_2", u"Die Vorbereitungen für die Ausstellung werden zu einer seltsamen Routine.", ("Act 3",u"Rin")),
                                    (u"Selbstzerstörung", "R24", u"Rin experimentiert mit Rauchen, um eine neue Sichtweise auf Kreativität zu finden.", ("Act 3",u"Rin")),
                                    (u"Umgekehrter Eskapismus", "R25", u"Hisao macht mit Rin einen Spaziergang durch die nächtlichen Straßen.", ("Act 3",u"Rin")),
                                    (u"Grenzenlos", "R26", u"Sae und Nomiya geben Hisao einen Einblick in das Leben von Künstlern.", ("Act 3",u"Rin")),
                                    (u"Delirium", "R27", u"Hisao überrascht eine verzweifelte Rin im Atelier.", ("Act 3",u"Rin")),
                                    (u"Was Du Hasst", "R28", u"Unangenehmes Nachspiel einer unglaublichen Nacht.", ("Act 3",u"Rin")),
                                    (u"Scherben des Zorns", "R29", u"Die angespannte Beziehung zwischen den Beiden zerbricht.", ("Act 3",u"Rin")),
                                    (u"Akt 4: Traum", rp_actmark, rp_actmark, ("Act 4",u"Rin")),
                                    (u"Selbsttäuschung", "R30", u"Hisao spricht mit Nomiya über seine Bedenken - ohne Erfolg.", ("Act 4",u"Rin")),
                                    (u"Uninspiriert", "R31", u"Hisaos Geduld ist am Ende.", ("Act 4",u"Rin")),
                                    (u"Die Szene", "R32", u"Treffen mit Rin bei der Eröffnung der Ausstellung.", ("Act 4",u"Rin")), 
                                    (u"Wellenlänge", "R35", u"Hisao verbringt den Tag nach den Abschlussprüfungen mit Faulenzen.", ("Act 4",u"Rin")),
                                    (u"Blaue Periode", "R36", u"Ein verregneter Tag in der Galerie und ein kurzer Vortrag über Picasso.", ("Act 4",u"Rin")),
                                    (u"Die Welt, die nur Du Siehst", "R37", u"Rin und Hisao trennen sich nach dem Regen.", ("Act 4",u"Rin")),
                                    (u"Verzweifelter Ruhm", "R34", u"Ein hektischer Nomiya erkundigt sich bei Hisao, wo Rin ist.", ("Act 4",u"Rin")), 
                                    (u"Probleme Selbstbezogener Logik", "R38", u"Hisao findet Rin in ihrem Versteck und überredet sie, mit Herrn Nomiya zu reden.", ("Act 4",u"Rin")),
                                    (u"Fenster zur Seele", "R39", u"Rins Entschuldigung bei Herrn Nomiya kommt nicht gut an.", ("Act 4",u"Rin")),
                                    (u"Raison d'être", "R40", u"Hisao tröstet eine niedergeschlagene Rin.", ("Act 4",u"Rin")),
                                    (u"Ohne zu Atmen, Ohne ein Geräusch", "R41", u"Am ersten Tag der Sommerferien kommt Rin in Hisaos Zimmer.", ("Act 4",u"Rin")),
                                    (u"Existenzbeweis", "R42", u"Auf dem Hügel mit den Pusteblumen findet alles ein Ende.", ("Act 4",u"Rin")),
                                    (u"Akt 2: Lesen lernen", rp_actmark, rp_actmark, ("Act 2",u"Shizune")),
                                    (u"Zettelwirtschaft", u"S8", u"Shizune und Hisao loten Verständigungsmöglichkeiten aus.", ("Act 2",u"Shizune")),
                                    (u"Sprich zur Hand", u"S9", u"Hisao beginnt, eine neue Sprache zu lernen, und findet eine Lehrerin.", ("Act 2",u"Shizune")),
                                    (u"Stille Post", u"S10", u"Kenji überredet Hisao ihm einen Gefallen zu tun, Aber Hisao hat dabei mehrere Probleme.", ("Act 2",u"Shizune")),
                                    (u"Spieltheorie für Fortgeschrittene", u"S11", u"RISIKO ist nicht mehr genug, um Shizune zufriedenzustellen - und dann taucht auch noch einen neue Gegnerin auf.", ("Act 2",u"Shizune")),
                                    (u"Schere, Brot, Papier", u"S12", u"Ein ruhiger Nachmittag entwickelt sich dramatisch, als plötzlich ein Stück Brot zum Objekt der Begierde wird.", ("Act 2",u"Shizune")),
                                    (u"Schnittstelle", u"S13", u"Shizune und Hisao finden eine Gemeinsamkeit.", ("Act 2",u"Shizune")),
                                    (u"Aktiv werden", u"S14", u"Hisao muss zwischen Lilly und Shizune vermitteln, aber zum Glück geht alles gut aus.", ("Act 2",u"Shizune")),
                                    (u"Unvollendete Vergangenheit", u"S15", u"Der Schülerrat erinnert sich beim Entspannen im Shanghai an die vergangenen Jahre.", ("Act 2",u"Shizune")),
                                    (u"Wenn Sterne Umarmen", u"S16", u"Endlich Tanabata!", ("Act 2",u"Shizune")),
                                    (u"Akt 3: Fingerfertigkeit", rp_actmark, rp_actmark, ("Act 3",u"Shizune")),
                                    (u"Rückkopplung", u"S17", u"Hisao findet heraus, dass Shizune ihre Familie besuchen wird, und darf mitkommen.", ("Act 3",u"Shizune")),
                                    (u"Vereinte Nationen", u"S18", u"Die Fahrt zu Shizune nach Hause, das Treffen mit ihrem kleinen Bruder und ein plötzlicher Angelwettbewerb.", ("Act 3",u"Shizune")),
                                    (u"Theorie und Praxis", u"S19", u"Hideaki versucht Hisao zu unterhalten, was ihm nur sehr begrenzt gelingt.", ("Act 3",u"Shizune")),
                                    (u"Familienbande", u"S20", u"Das Trio trifft Shizunes Vater und bläst sofort hastig zum Rückzug.", ("Act 3",u"Shizune")),
                                    (u"Pangrammatisches Gedicht", u"S21", u"Eine Bitte von Hideaki, ihm Zeichensprache beizubringen, eskaliert unerwarteterweise zu einem Streit mit Jigoro.", ("Act 3",u"Shizune")),
                                    (u"Näher", u"S22", u"Shizune und Hisao verbinden sich zum ersten Mal.", ("Act 3",u"Shizune")),
                                    (u"Konfrontation", u"S23", u"Jigoro redet den Schülerrat schlecht, und Hisao nimmt die Herausforderung an.", ("Act 3",u"Shizune")),
                                    (u"Der Anker", u"S24", u"Zurück an der Yamaku. Ein Brief von Iwanako löst eine längere Diskussion mit Kenji über Freundinnen aus.", ("Act 3",u"Shizune")),
                                    (u"Fahrplan", u"S25", u"Der Schülerrat sorgt sich um geeignete Nachfolger, und am Ende muss Hisao Misha irgendwie ein Parfait ausgeben.", ("Act 3",u"Shizune")), 
                                    (u"Akutes Dreieck", u"S26", u"Ein Arbeitsnachmittag mit Shizune lässt Hisao merken, dass zwischen den Mädchen etwas nicht in Ordnung ist.", ("Act 3",u"Shizune")),
                                    (u"Dewey Dezimiert", u"S27", u"Yuuko bittet Hisao für sie auf die Bibliothek aufzupassen. Durch Kenjis Ankunft ist der Erfolg etwas zwiespältig.", ("Act 3",u"Shizune")),
                                    (u"Sprachlos", u"S28", u"Misha besucht Hisao in seinem Zimmer, und die Dinge entwickeln sich in eine unerwartete Richtung.", ("Act 3",u"Shizune")),
                                    (u"Zur Seite Schauen", u"S29_1", u"Hisao findet auf dem Dach eine deprimierte Misha. Hisao versucht, sie wieder mit Shizune zu versöhnen.", ("Act 3",u"Shizune")),
                                    (u"Vorausschauen", u"S29_2", u"Hisao findet auf dem Dach eine deprimierte Misha. Shizune kommt dazu und zerrt den Schülerrat zurück an die Arbeit.", ("Act 3",u"Shizune")),
                                    (u"Akt 4: An Mein Anderes Ich", rp_actmark, rp_actmark, ("Act 4",u"Shizune")),
                                    (u"Übergeordnete Strategie", u"S30", u"Shizune verrät Hisao einige ihrer Ziele und einige ihrer Fehler.", ("Act 4",u"Shizune")),
                                    (u"Um Eins Daneben", u"S31", u"Ein fehlgeschlagener Versuch Misha aufzumuntern wird kurzerhand zu einem Date zwischen Hisao und Shizune umfunktioniert.", ("Act 4",u"Shizune")),
                                    (u"Invasion", u"S32", u"Jigoro und Hideaki statten Shizune einen unerwarteten und etwas unangenehmen Besuch ab.", ("Act 4",u"Shizune")),
                                    (u"Parfait", u"S33", u"Hisao und Shizune verfolgen Misha. Hisao schafft es schließlich, sie zu stellen und in Ruhe mit ihr zu reden.", ("Act 4",u"Shizune")),
                                    (u"Präsens", u"S38", u"Hisao trifft beim Mittagessen zufällig auf Lilly, und die beiden reden über Shizune.", ("Act 4",u"Shizune")), 
                                    (u"Spirale", u"S39", u"Hinhaltetaktiken und ein nächtlicher Hinterhalt von Kenji.", ("Act 4",u"Shizune")),
                                    (u"Anschluss", u"S40", u"Ein frühmorgendliches Gespräch mit Shizune in der stillen Schule.", ("Act 4",u"Shizune")),
                                    (u"Der Gipfel", u"S34", u"Kenji und Shizune treffen sich in Hisaos Zimmer. Wundersamerweise explodiert nichts.", ("Act 4",u"Shizune")), 
                                    (u"Nachfolge", u"S35", u"Der aktuelle Schülerrat bringt seine Nachfolger in Form und betätigt sich dann in “außerschulischen Aktivitäten.”", ("Act 4",u"Shizune")),
                                    (u"Schleichmission", u"S36", u"Mishas Entschlossenheit spornt Shizune an, sich noch höhere Ziele zu setzen.", ("Act 4",u"Shizune")),
                                    (u"Unendlichkeit", u"S37", u"Das Trio erneuert seine Freundschaft, und der Schulabschluss steht kurz bevor.", ("Act 4",u"Shizune")),
                                    )



    displayDict["de"].creditstring = """{image=ui/flourish_left.png} {b}Autoren{/b} {image=ui/flourish_right.png}
Anonymous22
Aura
cpl_crud
Suriko
TheHivemind

{image=ui/flourish_left.png} {b}Editoren{/b} {image=ui/flourish_right.png}
Kagami
Losstarot
Silentcook

{image=ui/flourish_left.png} {b}Musik{/b} {image=ui/flourish_right.png}
Blue123
NicolArmarfi

{image=ui/flourish_left.png} {b}Künstler{/b} {image=ui/flourish_right.png}
gebyy-terar
Kamifish
moekki
pimmy
raemz
Raide



{image=ui/flourish_left.png} {b}Zusätzliches Material{/b} {image=ui/flourish_right.png}
climatic
Doomfest
yujovi

{image=ui/flourish_left.png} {b}FMV Animation{/b} {image=ui/flourish_right.png}
Mike Inel

{image=ui/flourish_left.png} {b}Regie{/b} {image=ui/flourish_right.png}
delta
Raide
yujovi

{image=ui/flourish_left.png} {b}Technik{/b} {image=ui/flourish_right.png}
delta

{image=ui/flourish_left.png} {b}Produktion{/b} {image=ui/flourish_right.png}
cpl_crud
Suriko

{image=ui/flourish_left.png} {b}Deutsche Übersetzung{/b} {image=ui/flourish_right.png}
Mirage
ekalz (Hikari Translations)
Dangel (Hikari Translations)
Fink
Vyse
Marq
Lunar

{image=ui/flourish_center.png}


{image=ui/flourish_left.png} {b}Vielen Dank an{/b} {image=ui/flourish_right.png}
Ambi07
abscess
Anonymous
Celiest
ContinualNaba
Dark_Mercury
DuaneMoody
Fink
frumplstlskn
Ismuth
Japesland
Juno
kekekeke
konflikti
Magaran
Mirage_GSM
OverCoat
Peorth
Petaru
silentkyon
skim
stirfriedweasel
Syureria
TcDohl
tottori
VCR

{image=ui/flourish_left.png} {b}Ein besonderer Dank an{/b} {image=ui/flourish_right.png}
hir
PyTom
RAITA
replicated"""


    displayDict["de"].drugs_wordlist  =  [u"Disopyramid",
                        u"Warfarin",
                        u"Diltiazem",
                        u"Felodipin",
                        u"Propanolol",
                        u"Penbutolol",
                        u"Carteolol",
                        u"Procainamid",
                        u"Heparin",
                        u"Phenytoin",
                        u"Verapamil",
                        u"Chinidin",
                        u"Flecainid",
                        u"5mg/Tag",
                        u"400mg/Tag",
                        u"15ml/Tag",
                        u"100mg/Tag",
                        u"10ml/48Std.",
                        u"10ml/Tag",
                        u"200mg/12Std.",
                        u"50mg/12Std.",
                        u"500mg/48Std.",
                        u"125mg/12Std.",
                        u"25ml/Tag",
                        u"Albträume",
                        u"Abnahme der Konzentrationsfähigkeit",
                        u"Bradykardie",
                        u"Klinische Depressionen",
                        u"Schlaflosigkeit",
                        u"Erektile Dysfunktion",
                        u"Sehstörungen",
                        u"Herzversagen",
                        u"Übelkeit",
                        u"Benommenheit",
                        u"Halluzinationen",
                        u"Bronchospasmen",
                        u"Dyspnoe",
                        u"Erschöpfung",
                        u"Hypotonie",
                        u"Herzblock",
                        u"Kalte Extremitäten",
                        u"Diarrhoe",
                        u"Herzstillstand",
                        u"Kammerflimmern",
                        u"Ataxie",
                        u"Asthma"]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
