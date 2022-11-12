# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

python early:
    import asyncio
    import copy
    import math
    import random
    import re
    import time
    import threading
    from functools import partial
    from pypresence import Presence, InvalidID

    renpy.music.register_channel("ambient", "sfx", True, tight=True)

    def format_time(t):
        t = int(t)

        minutes = t // 60

        if minutes > 60:
            hours = minutes // 60

            return str(hours) + ":" + str(minutes % 60).zfill(2) + ":" + str(t % 60).zfill(2)
        else:
            return str(minutes) + ":" + str(t % 60).zfill(2)

    high_contrast = im.matrix.colorize("#ccc", "#fff")

    def contrast_checker(image, mrx=im.matrix.identity()):
        return ConditionSwitch(
            "preferences.high_contrast", im.MatrixColor(image, high_contrast),
            "True", im.MatrixColor(image, mrx))

    def opacity(image, op=0.4, **options):
        return im.MatrixColor(image, im.matrix.opacity(op), **options)

    def main_menu_composer(st, at):
        _widgets = [ ("a4_shizune", (1491, 479), "gui/icons/16_tc4-shizune.png"),
                     ("a3_shizune", (1508, 645), "gui/icons/15_tc3-shizune.png"),
                     ("a2_shizune", (1393, 832), "gui/icons/14_tc2-shizune.png"),
                     ("a4_rin", (1183, 248), "gui/icons/13_tc4-rin.png"),
                     ("a3_rin", (1304, 338), "gui/icons/12_tc3-rin-rin.png"),
                     ("a3_rin", (1409, 454), "gui/icons/11_tc3-rin-hisao.png"),
                     ("a2_rin", (1409, 681), "gui/icons/10_tc2-rin.png"),
                     ("a4_lilly", (1053, 283), "gui/icons/09_tc4-lilly.png"),
                     ("a3_lilly", (1183, 439), "gui/icons/08_tc3-lilly.png"),
                     ("a2_lilly", (1302, 630), "gui/icons/07_tc2-lilly.png"),
                     ("a4_hanako", (888, 439), "gui/icons/06_tc4-hanako.png"),
                     ("a4_emi", (881, 621), "gui/icons/05_tc4-emi.png"),
                     ("a3_emi", (993, 786), "gui/icons/04_tc3-emi.png"),
                     ("a2_emi", (1069, 876), "gui/icons/03_tc2-emi.png"),
                     ("a3_hanako", (1058, 500), "gui/icons/02_tc3-hanako.png"),
                     ("a2_hanako", (1124, 645), "gui/icons/01_tc2-hanako.png"),
                     ("a1_monday.bundle_of_hisao", (1260, 826), "gui/icons/00_tc1-hisao.png") ]

        _args = [
            (1920, 1080),
            (0, 0), "gui/bg/main.png"
        ]

        for trigger, offset, widget in _widgets:
            if renpy.seen_label(trigger) or config.developer:
                _args.extend((offset, widget))

        _args.extend((
            (1650, 1010), Text(
                config.name + " v" + config.version +
                "\nRen'Py " + ".".join(str(el) for el in renpy.version(True)[:3]) +
                "\nMade by Fleeting Heartbeat Studios", color="#00000080", size=15, alt="Menu")
        ))

        return Composite(*_args), None

    def acdc_generic(x, n):
        if x < (1.0 / n):
            return (((2.0 / n) * (0.5 - math.cos(math.pi * (x * (n / 2.0))) / 2.0)) / 2.0) * (n / (n - 1.0))
        elif x > (1.0 - (1.0 / n)):
            return (((2.0 / n) * (0.5 - math.cos(math.pi * (1.0 - (((x - 1.0) * n) / 2.0))) / 2.0) / 2.0) + (1.0 - (2.0 / n))) * (n / (n - 1.0))
        else:
            return (x - (0.5 / n)) * (n / (n - 1.0))

    @renpy.atl_warper
    def acdc_warp(x):
        return acdc_generic(x, 10)

    @renpy.atl_warper
    def acdc20_warp(x):
        return acdc_generic(x, 20)

    class Trigger:
        def __init__(self, trig, image):
            self.trig = trig
            self.image = image

    def is_seen(img):
        if isinstance(img, Trigger):
            return renpy.seen_image(img.trig)
        else:
            return renpy.seen_image(img)

    def get_scene_name(name=None, _thread_replays=None):
        global _replays

        if not name:
            name = current_scene

        for replay_pack in (_thread_replays or _replays):
            for replay_stack in replay_pack[1]:
                for replay in replay_stack[1]:
                    if replay[1] == name:
                        return __(replay[0])

        return __("No scene")

    def get_track_name(track=None, _thread_tracks=None):
        global _tracks

        return (_thread_tracks or _tracks).get(track or store.renpy.music.get_playing()) or __("Nothing")

    def set_current_scene(name, jumped):
        global rpc

        rpc.data["is_watching"] = name == "act_op"

        if not jumped and name.startswith("a") and "." in name:
            store.current_scene = name
            rpc.data["current_scene"] = name
        else:
            rpc.data["current_scene"] = "0"

    config.label_callback = set_current_scene

    class RPCThread(threading.Thread):
        def __init__(self, store):
            threading.Thread.__init__(self, daemon=True)
            self.store = store

            self.data = {}
            self.rpc = None
            self.start_time = 0
            self.last_update = 0

        def run(self):
            self.start_time = time.time()

            __ = self.store.__

            asyncio.set_event_loop(asyncio.new_event_loop())
            self.rpc = Presence("1039954053079236628")
            self.rpc.connect()

            while True:
                if self.last_update + 15 > time.time():
                    time.sleep(self.last_update + 15 - time.time())
                    continue

                self.last_update = time.time()

                if not self.store.persistent.discord:
                    self.rpc.clear()
                    continue

                scene_name = self.store.get_scene_name(
                    self.data.get("current_scene", "0"),
                    self.store._replays
                )

                try:
                    params = {}

                    if self.data.get("is_watching", False):
                        params["state"] = __("Playing history")
                        params["details"] = __("Watching video")

                    elif scene_name == __("No scene"):
                        params["state"] = __("In main menu")
                        params["details"] = (
                            __("Listening") + " "
                            + self.store.get_track_name(
                                self.store.renpy.music.get_playing(),
                                self.store._tracks
                            )
                        )
                    else:
                        params["state"] = __("Playing history")
                        params["details"] = scene_name

                    self.rpc.update(
                        start=self.start_time,
                        large_image="logo",
                        **params
                    )
                except InvalidID:
                    # Will try to reconnect after every 5 seconds
                    self.last_update -= 10
                    try:
                        self.rpc.connect()
                    except:
                        pass

    rpc = RPCThread(store)

init 1000 python:
    rpc.start()

    config.keymap["rollback"] = ["mousedown_5"]
    config.keymap["rollforward"] = ["mousedown_4"]
    config.keymap["game_menu"].append("K_AC_BACK")

define null = Null()

default persistent._watched_videos = set()

define _videos = (
    "video/op_1.webm", "video/tc_act2_emi.webm", "video/tc_act2_hanako.webm",
    "video/tc_act2_lilly.webm", "video/tc_act2_rin.webm", "video/tc_act2_shizune.webm")

define _replays = [
    (_("Act 1"), [
        (_("Prologue"), [
            (_("Out Cold"), "a1_monday.out_cold", _("On a cold, snowy day, Hisao's dreams were about to be realized, only to be cut short by a sudden heart attack.")),
            (_("Bundle of Hisao"), "a1_monday.bundle_of_hisao", _("Hisao is told about Yamaku Academy, where he will likely spend the rest of his high school days."))
        ]),
        (_("Act 1: Life Expectancy"), [
            (_("Gateway Effect"), "a1_monday.gateway_effect", _("Hisao steps into Yamaku Academy for the first time, and meets his homeroom teacher, Mutou.")),
            (_("Enter Stage Left"), "a1_monday.enter_stage_left", _("Introductions to the class, and meeting with the class representative and her interpreter.")),
            (_("In the Nursery"), "a1_monday.in_the_nursery", _("Misha and Shizune show Hisao the cafeteria, after which he goes to see the nurse.")),
            (_("Nobody's Room"), "a1_monday.nobodys_room", _("Hisao moves into his new room, meeting his hallmate Kenji in the process.")),
            (_("Smalltalk"), "a1_tuesday.smalltalk", _("Shizune and Misha tell Hisao about the upcoming festival and invite him to lunch.")),
            (_("Risk vs. Reward"), "a1_tuesday.risk_vs_reward", _("Shizune and Hisao battle for the world in a game of Risk.")),
            (_("Pseudo Tea Cosy"), "a1_tuesday.pseudo_tea_cosy", _("Looking for the library, Hisao gets lost and finds Lilly in a disused classroom.")),
            (_("Shared Library"), "a1_tuesday.shared_library", _("Finally finding his way to the library, Hisao meets and scares off Hanako.")),
            (_("Bizarre and Surreal"), "a1_tuesday.bizarre_and_surreal", _("Kenji reveals the dark secrets of Yamaku.")),
            (_("Lunch Evolution Theory"), "a1_wednesday.lunch_evolution_theory", _("Shizune and Misha badger Hisao into joining the Student Council before discussing lunch.")),
            (_("Short Sharp Shock"), "a1_wednesday.short_sharp_shock", _("On his way to lunch alongside Misha and Shizune, Hisao collides with Emi in the hallway.")),
            (_("Meet Cute"), "a1_wednesday.meet_cute", _("Hisao collides with a rampaging Emi on his way to lunch with Hanako and Lilly.")),
            (_("Detour Ahead"), "a1_wednesday.detour_ahead", _("Shizune and Misha take Hisao to their favourite teahouse, the Shanghai.")),
            (_("Sip (Part 1)"), "a1_wednesday.sip_p1", _("Hisao has a peaceful lunch with Lilly and Hanako.")),
            (_("It Builds Character"), "a1_wednesday.it_builds_character", _("Mutou tries to have a D&M talk with Hisao, but Misha interrupts and puts Hisao to work.")),
            (_("A Private Lunch"), "a1_wednesday.a_private_lunch", _("Searching for supplies, Hisao happens across a strange girl in the art room.")),
            (_("Waylay"), "a1_wednesday.waylay", _("While helping Rin carry some paint, Hisao is quizzed by the nurse.")),
            (_("The Other Green"), "a1_wednesday.the_other_green", _("Hisao watches Rin paint her mural.")),
            (_("The Running Girl"), "a1_thursday.the_running_girl", _("When attempting to do some morning exercise, Hisao meets Emi at the running track.")),
            (_("Soap"), "a1_thursday.soap", _("Kenji ambushes Hisao in the shower in an attempt to get some cash.")),
            (_("Cold War"), "a1_thursday.cold_war", _("Shizune and Lilly face off over budget requests.")),
            (_("Proof of Competency"), "a1_thursday.proof_of_competency", _("Shizune and Misha assault Hisao in an attempt to get him to join the Student Council.")),
            (_("Event Horizon"), "a1_thursday.event_horizon", _("Shizune and Misha assault Hisao in an attempt to get him to join the Student Council.")),
            (_("Above and Beyond"), "a1_thursday.above_and_beyond", _("Hisao gets a lecture about the noble duties of a Student Council.")),
            (_("Paint by Numbers"), "a1_thursday.paint_by_numbers", _("Hanako and Hisao lend a hand to Lilly's class by volunteering to help build their stall.")),
            (_("Things You Can Do"), "a1_thursday.things_you_can_do", _("After escaping from the clutches of Shizune and Misha, Hisao helps out Rin again.")),
            (_("Exercise"), "a1_friday.exercise", _("Another early morning sees Hisao running at the track with Emi.")),
            (_("Invisible Hat"), "a1_friday.invisible_hat", _("Kenji gives Hisao a few insider tips on how to socialize.")),
            (_("Home Field Advantage"), "a1_friday.home_field_advantage", _("Shizune and Misha hijack Hisao as he leaves his room for class.")),
            (_("No Recovery"), "a1_friday.no_recovery", _("Hisao struggles to class after his hijacking by the Student Council.")),
            (_("Slow Recovery"), "a1_friday.slow_recovery", _("Recovering from his heart flutter, Hisao eventually makes it to class.")),
            (_("No Free Lunch"), "a1_friday.no_free_lunch", _("Hisao is escorted to the student council office for his first official day there.")),
            (_("Foot and Mouth"), "a1_friday.foot_and_mouth", _("Emi drags Hisao to the roof to have lunch with Rin.")),
            (_("Mind Your Step"), "a1_friday.mind_your_step", _("Hisao and Lilly go shopping, meeting a very confused Rin on the way back.")),
            (_("Support"), "a1_saturday.support", _("Hisao has his first Saturday lesson, complete with a talking to from Mutou.")),
            (_("An Aesthetics"), "a1_saturday.support", _("Emi finds Hisao slacking around after class and recruits him to help Rin once again.")),
            (_("Creative Pain"), "a1_saturday.creative_pain", _("Hisao meets the art teacher, Nomiya, as Rin paints her mural.")),
            (_("Proper Exercise"), "a1_saturday.proper_exercise", _("Emi and Hisao discuss the importance of being in shape.")),
            (_("Sip (Part 2)"), "a1_saturday.sip_p2", _("In an attempt to kill time, Hisao goes for a walk around the school.")),
            (_("Shanghaied"), "a1_saturday.shanghaied", _("Tea, cake and competitions with Shizune and Misha at the Shanghai.")),
            (_("Quiet"), "a1_saturday.quiet", _("Hanako and Hisao read books for the festival.")),
            (_("Don't Panic"), "a1_sunday.dont_panic", _("After waking up on the day of the festival, Hisao is greeted by a ranting Kenji.")),
            (_("Is Carnival!"), "a1_sunday.is_carnival", _("Emi catches Hisao eating fried food and makes him accompany her as punishment.")),
            (_("Clouds in My Head"), "a1_sunday.clouds_in_my_head", _("Hisao keeps Rin and her now-finished mural company.")),
            (_("Promise of Time"), "a1_sunday.promise_of_time", _("After a trying morning at her stall, Hisao takes Lilly to find Hanako.")),
            ("Nc5xb3", "a1_sunday.nc5xb3", _("Unable to help Lilly at her stall, Hisao searches for Hanako at the festival.")),
            (_("Movement"), "a1_sunday.movement", _("Lilly finishes her duties and treats Hanako and Hisao to tea at the Shanghai.")),
            (_("Throwing Balls"), "a1_sunday.throwing_balls", _("True to his word, Hisao spends the day with Shizune and Misha.")),
            (_("The Deep End"), "a1_sunday.the_deep_end", _("Kenji and Hisao share a manly picnic on the roof instead of going to the festival."))
        ])
    ]),
    (_("Emi"), [
        (_("Act 2: Form"), [
            (_("Morning Run"), "a2_emi.morning_run", _("The first of Hisao's many morning runs with Emi.")),
            (_("Clouds, Time Travel, and Thou"), "a2_emi.clouds_time_travel_and_thou", _("Another rooftop lunch with Emi and Rin. Emi extracts from Hisao a promise to come see the track meet.")),
            (_("Questions That Need Answering!"), "a2_emi.questions_that_need_answering", _("Idle chat between Emi and Hisao. Hisao asks Emi a few more questions about her relationship with Rin.")),
            (_("Second Time's the Worst"), "a2_emi.second_times_the_worst", _("The second morning run. Hisao is almost dragged kicking and screaming around the track.")),
            (_("An Apple a Day"), "a2_emi.an_apple_a_day", _("Hisao pays a visit to the nurse along with Emi, finding out that the two have known each other for a while.")),
            (_("Track Meeting"), "a2_emi.track_meeting", _("The day of the track meet. Another facet of Emi's personality is revealed.")),
            (_("Down that Medicine Now"), "a2_emi.down_that_medicine_now", _("Hisao mentions a pain in his chest during a visit to the nurse and receives a lecture.")),
            (_("Piracy on the High Seas"), "a2_emi.piracy_on_the_high_seas", _("Hisao discusses his future as a pirate with Emi on the rooftop, then a letter from Iwanako spoils his day.")),
            (_("Famous Last Words"), "a2_emi.famous_last_words", _("Emi and Rin take Hisao along for a picnic, soon to be spoiled by rain.")),
            (_("Tracking Absences"), "a2_emi.tracking_absences", _("Hisao goes to the track as usual, but Emi is missing.")),
            (_("Dropping By"), "a2_emi.dropping_by", _("A bedside visit for a sick Emi, which quickly changes to something else entirely.")),
            (_("The First Morning After"), "a2_emi.the_first_morning_after", _("Hisao reminisces about last evening, deciding to do something to help Emi.")),
            (_("The (Real) Beginning"), "a2_emi.the_real_beginning", _("Another lunchtime on the rooftop, sans Rin."))
        ]),
        (_("Act 3: Perspective"), [
            (_("Eet Ees… Scienca"), "a3_emi.eet_ees_scienca", _("Mutou pulls Hisao into a short discussion about his future.")),
            (_("Definitions"), "a3_emi.definitions", _("Emi and Hisao attempt another picnic, this time without any intervention from Mother Nature.")),
            (_("Invisible Rock"), "a3_emi.invisible_rock", _("Back to the track in the morning, with business as usual… or so it seems.")),
            (_("Lunch and Science"), "a3_emi.lunch_and_science", _("Hisao sees Mutou again about his future in the sciences.")),
            (_("Up, Down, and Up Again"), "a3_emi.up_down_and_up_again", _("A frantic call from Emi brings Hisao to her room, where two surprises await him.")),
            (_("Storage Space"), "a3_emi.storage_space", _("Emi coaxes Hisao into the track storage shed.")),
            (_("After-School Plans"), "a3_emi.afterschool_plans", _("Emi has a serious talk with Hisao about the incoming exams.")),
            (_("Detached"), "a3_emi.detached", _("Hisao broods about his relationship with Emi.")),
            (_("Phantom Pain"), "a3_emi.phantom_pain", _("Hisao's attempt to show Emi his concern doesn't go nearly as well as he hoped.")),
            (_("Debate Expresses Doubt"), "a3_emi.debate_expresses_doubt", _("Hisao is confused by Emi's behavior and by an invitation to her house.")),
            (_("Guess Who's Coming… Never Mind"), "a3_emi.guess_whos_coming_never_mind", _("Dinner at the Ibarazaki's.")),
            (_("Instant Replay"), "a3_emi.instant_replay", _("Things finally come to a head at the track."))
        ]),
        (_("Act 4: Motion"), [
            (_("A Swing and a Miss"), "a4_emi.a_swing_and_a_miss", _("Hisao wonders if Emi is purposefully avoiding him.")),
            (_("Saving Throw"), "a4_emi.saving_throw", _("Things finally come to a head on the rooftop.")),
            (_("Whispers of the Past"), "a4_emi.whispers_of_the_past", _("Hisao, Emi and her mom go for a graveside visit.")),
            (_("Hooray for Socks"), "a4_emi.hooray_for_socks", _("Sex, drugs, but no rock and roll.")),
            (_("Clean Teeth"), "a4_emi.clean_teeth", _("Hisao wakes up, finding Emi sleeping next to him."))
        ])
    ]),
    (_("Hanako"), [
        (_("Act 2: Hide and Seek"), [
            (_("To Town, To Town"), "a2_hanako.to_town_to_town", _("A shopping trip at the convenience store with Hanako.")),
            (_("Tea Leaves"), "a2_hanako.tea_leaves", _("Hanako invites Hisao to have lunch with her and Lilly.")),
            (_("Office Confessional"), "a2_hanako.office_confessional", _("Hisao and Misha discuss the plight of Hanako.")),
            (_("Chess and Slides"), "a2_hanako.chess_and_slides", _("Hisao ditches the Student Council to read with Hanako.")),
            (_("Rise and Shine"), "a2_hanako.rise_and_shine", _("An invitation from Lilly to a tea party after hours.")),
            (_("Mad Hatter"), "a2_hanako.mad_hatter", _("Hanako, Hisao and Lilly meet together to have tea in Lilly's room.")),
            (_("Small Change"), "a2_hanako.small_change", _("Kenji is forced to repay his loan.")),
            (_("Absenteeism"), "a2_hanako.absenteeism", _("Hisao and Lilly discuss Hanako's school attendance.")),
            (_("Equivalent Exchange"), "a2_hanako.equivalent_exchange", _("In return for learning about his heart, Hanako reveals part of her past to Hisao."))
        ]),
        (_("Act 3: Castling"), [
            (_("Invitation"), "a3_hanako.invitation", _("Lilly finds Hisao cleaning up the Tea Room and tells him about Hanako's birthday.")),
            (_("Shady Encounter"), "a3_hanako.shady_encounter", _("An unexpected chat with Miki while reminiscing about the past.")),
            (_("Antiques and Pie"), "a3_hanako.antiques_and_pie", _("Lilly and Hisao shop for a present in the city.")),
            (_("Falling"), "a3_hanako.falling", _("Hanako has a panic attack during class.")),
            (_("Treading Softly"), "a3_hanako.treading_softly", _("Lilly has bad news to discuss with Hisao and Hanako.")),
            (_("Reaching Out"), "a3_hanako.reaching_out", _("Hisao reaches out to a withdrawn Hanako.")),
            (_("One More Year"), "a3_hanako.one_more_year", _("Our trio is joined by an unexpected guest as they celebrate Hanako's birthday party.")),
            (_("One Piece of Paper"), "a3_hanako.one_piece_of_paper", _("Hisao enjoys his first hangover, before receiving a troubling letter.")),
            (_("Stripes and Solids"), "a3_hanako.stripes_and_solids", _("Heart-to-heart during a game of pool.")),
            (_("Beginning of the End"), "a3_hanako.beginning_of_the_end", _("Lilly's departure for her trip."))
        ]),
        (_("Act 4: Scars"), [
            (_("Truancy"), "a4_hanako.truancy", _("Lunch with the Student Council and worry about Hanako shutting herself in.")),
            (_("Faraway Presence"), "a4_hanako.faraway_presence", _("Hisao phones Lilly for advice after Hanako secludes herself for another day.")),
            (_("Misstep"), "a4_hanako.misstep", _("Hisao tries to pull Hanako out of her room, with startling results.")),
            (_("Cut Petals"), "a4_hanako.cut_petals", _("Hisao finds his future relationship with Hanako prematurely ended.")),
            (_("Continuing Melody"), "a4_hanako.continuing_melody", _("Hanako returns to class, to Hisao's relief.")),
            (_("Shanghai Studiousness"), "a4_hanako.shanghai_studiousness", _("Attempting to avoid distractions, Hisao tries studying at the Shanghai.")),
            (_("His Past"), "a4_hanako.his_past", _("In an attempt to come closer to Hanako, Hisao shares a part of his past with her.")),
            (_("City Rendezvous"), "a4_hanako.city_rendezvous", _("The two share a date in the city.")),
            (_("Whispered Touch"), "a4_hanako.whispered_touch", _("Hisao and Hanako spend the night together.")),
            (_("Indeterminate Future"), "a4_hanako.indeterminate_future", _("The events of the previous night weigh heavily on Hisao.")),
            (_("Adulthood"), "a4_hanako.adulthood", _("The end of two children, the beginning of two adults."))
        ])
    ]),
    (_("Lilly"), [
        (_("Act 2: Past"), [
            (_("Earl Grey"), "a2_lilly.earl_grey", _("Hisao shares the first of many lunchbreaks with Hanako and Lilly, recovering from the day before.")),
            (_("A Pound Sterling"), "a2_lilly.a_pound_sterling", _("Questioned by Kenji on Lilly's nationality, Hisao decides to investigate and finds out a great deal more.")),
            (_("Presents and Presence"), "a2_lilly.presents_and_presence", _("While out in search of a present for Hanako, Lilly and Hisao meet Akira and her cousin.")),
            (_("Unidentified Drinking Object"), "a2_lilly.unidentified_drinking_object", _("The trio hold a birthday party for Hanako, interrupted by the surprise appearance of a sibling.")),
            (_("The Day After"), "a2_lilly.the_day_after", _("Hisao and Lilly awaken and try to recuperate from the previous evening's events.")),
            (_("A Brief History of Thyme"), "a2_lilly.a_brief_history_of_thyme", _("Hisao and Lilly go to get some groceries.")),
            (_("Little Wing"), "a2_lilly.little_wing", _("A shared lunch on the roof takes an unfortunate turn.")),
            (_("Bon Voyage"), "a2_lilly.bon_voyage", _("Lilly and Akira get seen off as they leave for a trip to their family in Scotland."))
        ]),
        (_("Act 3: Present"), [
            (_("Day by Day"), "a3_lilly.day_by_day", _("Hisao idly lets a day without Lilly slip by, having a talk with Mutou about Yamaku.")),
            (_("Minor Discord"), "a3_lilly.minor_discord", _("Hisao has lunch with Kenji, then gives some handouts to an alarmingly silent Hanako.")),
            (_("Dissonance"), "a3_lilly.dissonance", _("With Hanako withdrawing into herself completely, Hisao offers what little help he can before calling Lilly.")),
            (_("A World Away"), "a3_lilly.a_world_away", _("Hisao's reassured mind begins to wonder about the relationship between he and Lilly.")),
            (_("Renewal"), "a3_lilly.renewal", _("Hisao, Hanako, and Hideaki welcome Akira and Lilly after their return from Scotland.")),
            (_("Northern Sojourn"), "a3_lilly.northern_sojourn", _("The trio begins their holiday in Hokkaido.")),
            (_("Prelude"), "a3_lilly.prelude", _("A morning walk begins a chain of events.")),
            (_("Crescendo"), "a3_lilly.crescendo", _("Lilly's true feelings are told in the endless gold of the wheat fields.")),
            (_("Diminuendo"), "a3_lilly.diminuendo", _("Our couple shares their first night together.")),
            (_("Gray Outlook"), "a3_lilly.gray_outlook", _("Confined to the summerhouse, Lilly and Hisao are forced to come to terms with their relationship.")),
            (_("Rhapsody in Blue"), "a3_lilly.rhapsody_in_blue", _("A bathing Hisao reflects on where he and Lilly are in life, before being joined by someone.")),
            (_("The Momentary Present"), "a3_lilly.the_momentary_present", _("Traveling back to Yamaku, Hisao and Lilly idly talk between themselves."))
        ]),
        (_("Act 4: Future"), [
            (_("Slow Steps 'Fore a Waltz"), "a4_lilly.slow_steps", _("Back at the school, the events of Hokkaido come to the fore.")),
            (_("Pajamas and Suits"), "a4_lilly.pajamas_and_suits", _("Settling back into daily life. Akira joins the trio during one of their tea parties.")),
            (_("Correct Procedure"), "a4_lilly.correct_procedure", _("Hisao and Lilly arrange a date, before Akira swings by.")),
            (_("Out and About"), "a4_lilly.out_and_about", _("Hisao and Lilly go on their first date, finding out about each other's pasts.")),
            (_("A Morning's Reverie"), "a4_lilly.a_mornings_reverie", _("Hisao and Lilly discuss their ambitions for the future.")),
            (_("Blackout"), "a4_lilly.blackout", _("The trio muse on the upcoming holidays, before Hisao experiences sight as Lilly does.")),
            (_("Context"), "a4_lilly.context", _("Hisao gets called out by Akira and the two talk about her sibling.")),
            (_("A Faraway Future"), "a4_lilly.a_faraway_future", _("Lilly reveals her family's offer to join them in Scotland.")),
            (_("Farewell"), "a4_lilly.farewell", _("Farewells to Akira and Lilly the evening before they leave Japan.")),
            (_("False Cadence"), "a4_lilly.false_cadence", _("Hisao rushes to confront Lilly, realizing her conflict.")),
            (_("Under a Maudlin Sky"), "a4_lilly.under_a_maudlin_sky", _("Waking in the hospital ward, Hisao struggles to come to terms with his life.")),
            (_("Under a Bright Sky"), "a4_lilly.under_a_bright_sky", _("Lilly rejoins Hisao, the two beginning their life together anew.")),
            (_("Forwards, with Gusto!"), "a4_lilly.forwards", _("Lilly and Hisao see off Akira."))
        ])
    ]),
    (_("Rin"), [
        (_("Act 2: Disconnect"), [
            (_("A Wider Field of Vision"), "a2_rin.a_wider_field_of_vision", _("Hisao spends a lunch break with Rin watching clouds on the rooftop.")),
            (_("Studies in Grayscale"), "a2_rin.studies_in_grayscale", _("Rin and Hisao draw portraits of each other at his first art club meeting.")),
            (_("Interstitial"), "a2_rin.interstitial", _("Kenji lends a “borrowed” book to Hisao.")),
            (_("Self Study"), "a2_rin.self_study", _("Misha and Shizune catch Hisao meditatively doodling during class.")),
            (_("Hisao's Smile"), "a2_rin.hisaos_smile", _("Rin talks to Hisao about his happy expressions, or lack of them.")),
            (_("Things You Like"), "a2_rin.things_you_like", _("Brief musings with Yuuko about books and Yamaku.")),
            (_("Target Audience"), "a2_rin.target_audience", _("The day of the track meet. Facets of Emi's and Rin's personalities get revealed.")),
            (_("Eternity In an Hour"), "a2_rin.eternity_in_an_hour", _("Nomiya incites discussion of art during a club meeting.")),
            (_("Underwater and a Maple with a Name"), "a2_rin.underwater_and_maple", _("Rin leads Hisao into the woods, where they ponder their immediate future.")),
            (_("Iwanako's Regret"), "a2_rin.iwanakos_regret", _("A letter from Iwanako arrives.")),
            (_("In Her Own Image"), "a2_rin.in_her_own_image", _("Hisao pushes Rin to have her own art exhibition.")),
            (_("Umbrella Logic Cake"), "a2_rin.umbrella_logic_cake", _("Emi, Hisao and Rin get rained on and seek refuge in the Shanghai.")),
            (_("Six Meters Closer to Heaven"), "a2_rin.six_meters_closer", _("Rin and Hisao DON'T eat lunch on the roof, due to a distinct lack of Emi.")),
            (_("Indecision"), "a2_rin.indecision", _("Emi gets rid of her cold, while Rin catches her own.")),
            (_("Signal Interference"), "a2_rin.signal_interference", _("Hisao goes visit Rin in her room.")),
            (_("Dandelions"), "a2_rin.dandelions", _("Conclusions get drawn on a hilltop."))
        ]),
        (_("Act 3: Distance"), [
            (_("22nd Corner"), "a3_rin.tt_corner", _("The art club team checks out the gallery for Rin's future exhibition.")),
            (_("The Scent of Light"), "a3_rin.the_scent_of_light", _("Hisao happens upon a sleeping Rin in the art room.")),
            (_("Things You Can't Give Up"), "a3_rin.things_you_cant_give_up", _("Emi and Hisao discuss Rin's personality.")),
            (_("BADAAN!"), "a3_rin.badaan", _("Yuuko's thoughts on motivation.")),
            (_("Rose-Tinted Glasses"), "a3_rin.rosetinted_glasses", _("Nomiya expounds at length about art as a career.")),
            (_("The Edge of the World"), "a3_rin.the_edge_of_the_world", _("Hisao confesses to Rin and gets shot down. Or does he?")),
            (_("The Context of Rin"), "a3_rin.the_context_of_rin", _("An awkward and silent afternoon at the atelier.")),
            (_("Fast Forward"), "a3_rin.fast_forward", _("The preparations for the exhibition settle into a strange routine.")),
            (_("Self-Destruction"), "a3_rin.self_destruction", _("Rin experiments with smoking to get a fresh look at creativity.")),
            (_("Reverse Escapism"), "a3_rin.reverse_escapism", _("Hisao takes Rin on a walk through the night streets.")),
            (_("Boundless"), "a3_rin.boundless", _("Sae and Nomiya give Hisao some insight on artists' lives.")),
            (_("Delirium"), "a3_rin.delirium", _("Hisao surprises a desperate Rin in the atelier.")),
            (_("Things You Hate"), "a3_rin.things_you_hate", _("Unpleasant aftermath of an incredible night.")),
            (_("Shards of Ire"), "a3_rin.shards_of_ire", _("The strained relationship between the two blows apart."))
        ]),
        (_("Act 4: Dream"), [
            (_("Illusions for People"), "a4_rin.illusions_for_people", _("Hisao talks about his misgivings to Nomiya, to little effect.")),
            (_("Demused"), "a4_rin.demused", _("Hisao's patience comes to an end.")),
            (_("The Scene"), "a4_rin.the_scene", _("Meeting with Rin at the exhibition opening.")),
            (_("Wavelength"), "a4_rin.wavelength", _("Hisao lethargically whiles away the last day of exams.")),
            (_("Blue Period"), "a4_rin.blue_period", _("A rainy day, the 22nd Corner, and a brief history of Picasso.")),
            (_("The World Only You Can See"), "a4_rin.the_world_only_can_you_see", _("Rin and Hisao part after the rain.")),
            (_("Desperate Glory"), "a4_rin.desperate_glory", _("A frantic Nomiya queries Hisao about Rin's whereabouts.")),
            (_("Problems of Self-Referential Logic"), "a4_rin.problems_of_self_referential_logic", _("Hisao finds Rin in her hiding place, and convinces her to reconcile with Nomiya.")),
            (_("Measuring Shadows"), "a4_rin.measuring_shadows", _("Rin's apology to the art teacher isn't well-received.")),
            (_("Raison d'être"), "a4_rin.raison_detre", _("Hisao comforts an upset Rin.")),
            (_("Without Breathing, Without a Sound"), "a4_rin.wb_and_ws", _("On the first day of summer vacation, Rin comes to Hisao's room.")),
            (_("Proof of Existence"), "a4_rin.proof_of_existence", _("Everything comes together on that dandelion-covered hilltop."))
        ])
    ]),
    (_("Shizune"), [
        (_("Act 2: Learning to Read"), [
            (_("Message Passing"), "a2_shizune.message_passing", _("Shizune and Hisao explore methods of communication.")),
            (_("Talk to the Hand"), "a2_shizune.talk_to_the_hand", _("Hisao begins studying a new language, and a tutor appears.")),
            (_("Chinese Whispers"), "a2_shizune.chinese_whispers", _("Kenji manages to coerce Hisao to do a favor for him, but Hisao runs into trouble in many forms.")),
            (_("Advanced Game Theory"), "a2_shizune.advanced_game_theory", _("RISK isn't enough any more to satiate Shizune's hunger. What's worse, a new opponent makes her appearance.")),
            (_("Bread, Scissors, Paper"), "a2_shizune.bread_scissors_paper", _("A lazy afternoon becomes dramatic as suddenly a piece of bread becomes an object of extreme interest.")),
            (_("Interface"), "a2_shizune.interface", _("Shizune and Hisao find a connection.")),
            (_("Spring into Action"), "a2_shizune.spring_into_action", _("Hisao has to mediate between Lilly and Shizune, but luckily things work out in the end.")),
            (_("Past Imperfective"), "a2_shizune.past_imperfective", _("The Student Council reminisces about past years while relaxing at the Shanghai.")),
            (_("When Stars Embrace"), "a2_shizune.when_stars_embrace", _("It's finally time for Tanabata!"))
        ]),
        (_("Act 3: Sleight of Hand"), [
            (_("Force Feedback"), "a3_shizune.force_feedback", _("Hisao finds out that Shizune is going to visit her family, and manages to come along.")),
            (_("United Nations"), "a3_shizune.united_nations", _("The trip to Shizune's house, meeting her little brother, and a sudden fishing contest.")),
            (_("Use-Mention Distinction"), "a3_shizune.use_mention_distinction", _("Hideaki tries to entertain Hisao for a day, meeting with little success.")),
            (_("Family Plot"), "a3_shizune.family_plot", _("Our trio meets Shizune's father and immediately beats a hasty retreat.")),
            (_("Pangrammatic Window"), "a3_shizune.pangrammatic_window", _("A request from Hideaki to learn sign language unexpectedly escalates into a shouting match with Jigoro.")),
            (_("Closer"), "a3_shizune.closer", _("Shizune and Hisao join together for the first time.")),
            (_("Confrontation"), "a3_shizune.confrontation", _("Jigoro belittles the Student Council and Hisao rises up to the challenge.")),
            (_("The Anchor"), "a3_shizune.the_anchor", _("Back to Yamaku. A letter from Iwanako prompts a lengthy discussion from Kenji on the finer points of girlfriends.")),
            (_("Roadmap"), "a3_shizune.roadmap", _("The Student Council worries about their replacement, and Hisao ends up treating Misha to a parfait somehow.")),
            (_("Acute Triangle"), "a3_shizune.acute_triangle", _("An afternoon of work with Shizune shows Hisao that something is amiss between the girls.")),
            (_("Dewey Decimated"), "a3_shizune.dewey_decimated", _("Yuuko gets Hisao to watch the library for her. The arrival of Kenji makes the attempt meet with mixed success.")),
            (_("Tongue-Tied"), "a3_shizune.tongue_tied", _("Misha visits Hisao in his room, and things go in an unexpected direction.")),
            (_("Look Aside"), "a3_shizune.look_aside", _("Hisao meets a depressed Misha on the roof. He ends up pushing her and Shizune together.")),
            (_("Look Ahead"), "a3_shizune.look_ahead", _("Hisao meets a depressed Misha on the roof. Shizune joins them and pulls the whole council back to work."))
        ]),
        (_("Act 4: To My Other Self"), [
            (_("Grand Strategy"), "a4_shizune.grand_strategy", _("Shizune confesses to Hisao some of her goals and failures.")),
            (_("Off by One"), "a4_shizune.off_by_one", _("A failed attempt to cheer up Misha gets converted into an impromptu date for Hisao and Shizune.")),
            (_("Invasion"), "a4_shizune.invasion", _("Jigoro and Hideaki pay Shizune an unexpected and somewhat unpleasant visit.")),
            (_("Parfait"), "a4_shizune.parfait", _("Hisao and Shizune stalk Misha. Hisao finally manages to corner her and discuss things properly.")),
            (_("The Summit"), "a4_shizune.the_summit", _("Kenji and Shizune meet in Hisao's room. Miraculously, nothing explodes.")),
            (_("Succession"), "a4_shizune.succession", _("The current Student Council shapes up their successors before engaging in “extracurricular activities.”")),
            (_("Sneaking Mission"), "a4_shizune.sneaking_mission", _("The show of Misha's determination spurs Shizune to set her sights on greater things.")),
            (_("Infinity"), "a4_shizune.infinity", _("Our trio renews their friendship, with their graduation looming close ahead.")),
            (_("Present Tense"), "a4_shizune.present_tense", _("Hisao stumbles into Lilly at lunch, and the two talk about Shizune.")),
            (_("Spiral"), "a4_shizune.spiral", _("Runaround, stonewalling, and Kenji nighttime ambush.")),
            (_("Terminal"), "a4_shizune.terminal", _("An early-morning talk with Shizune in the silent school."))
        ])
    ])
]

define _gallery_images = (
    ("thumb/other_iwanako.jpg", Trigger("ev other_iwanako_start", "evul other_iwanako")),
    ("thumb/hisao_class.jpg", "ev hisao_class_start", "ev hisao_class_move", "ev hisao_class_end"),
    ("thumb/kenji_rooftop.jpg", "ev kenji_rooftop"),
    ("thumb/hisao_teacup.jpg", Trigger("ev hisao_teacup", "evul hisao_teacup")),
    ("thumb/hisao_letter.jpg", "ev hisao_letter_closed", "ev hisao_letter_open", "ev hisao_letter_open_2"),
    ("thumb/akira_park.jpg", Trigger("ev akira_park", "evul akira_park")),
    ("thumb/emi_knockeddown.jpg", "ev emi_knockeddown"),
    ("thumb/emi_run_face.jpg", "ev emi_run_face"),
    ("thumb/emitrack_blocks.jpg", "ev emitrack_blocks", "ev emitrack_blocks_close", "ev emitrack_blocks_close_grin"),
    ("thumb/emitrack_running.jpg", "ev emitrack_running"),
    ("thumb/emitrack_finishtop.jpg", "ev emitrack_finishtop"),
    ("thumb/emitrack_finish.jpg", "ev emitrack_finish"),
    ("thumb/picnic.jpg", "ev picnic_normal", "ev picnic_rain"),
    ("thumb/emi_sleep.jpg", "ev emi_sleep_unsure", "ev emi_sleep_normal", "ev emi_sleep_weep", "ev emi_sleep_cry"),
    ("thumb/emi_sleepy.jpg", "ev emi_sleepy", "ev emi_sleepy_face", "ev emi_sleepy_legs"),
    ("thumb/emi_firstkiss.jpg", "ev emi_firstkiss"),
    ("thumb/emi_bed.jpg", "ev emi_bed_normal", "ev emi_bed_smile", "ev emi_bed_happy", "ev emi_bed_unsure", "ev emi_bed_frown", "ev emi_parkback", "ev emi_parkback_frown"),
    ("thumb/emi_forehead.jpg", "ev emi_forehead"),
    ("thumb/emi_grinding.jpg", "evh emi_grinding_victory", "evh emi_grinding_wink", "evh emi_grinding_grin", "evh emi_grinding_half_undress", "evh emi_grinding_half_grin", "evh emi_grinding_off_yawn", "evh emi_grinding_off_closesurprise", "evh emi_grinding_off_closearoused", "evh emi_grinding_off_aroused", "evh emi_grinding_off_arousedclosed", "evh emi_grinding_off_come", "evh emi_grinding_off_end"),
    ("thumb/emi_shed.jpg", "evh emi_shed_base1", "evh emi_shed_base3", "evh emi_shed_base3", "evh emi_shed_base4"),
    ("thumb/emi_grave.jpg", "ev emi_grave"),
    ("thumb/emi_cry_down.jpg", Trigger("ev emi_cry_down", "evul emi_cry_down")),
    ("thumb/emi_miss.jpg", "evh emi_miss_closed", "evh emi_miss_open"),
    ("thumb/emi_ending.jpg", "ev emi_ending_smile", "ev emi_ending_serious", "ev emi_ending_glad"),
    ("thumb/hana_library.jpg", "ev hana_library", "ev hana_library_read", "ev hana_library_gasp"),
    ("thumb/hanako_shanghaiwindow.jpg", "ev hanako_shanghaiwindow"),
    ("event/hanako_presents1.jpg", "ev hanako_presents1", "ev hanako_presents2"),
    ("thumb/hanako_crayon.jpg", "ev hanako_crayon1", "ev hanako_crayon2"),
    ("thumb/hanako_breakdown.jpg", Trigger("evfg hanako_breakdown", "evul hanako_breakdown_down"), Trigger("evfg hanako_breakdown_up", "evul hanako_breakdown_up"), Trigger("evfg hanako_breakdown_closed", "evul hanako_breakdown_closed")),
    ("thumb/hanako_cry.jpg", "ev hanako_cry_closed", "ev hanako_cry_closed", "ev hanako_cry_open", "ev hanako_cry_away"),
    ("thumb/hanako_billiards.jpg", "ev hanako_billiards_break", "ev hanako_billiards_distant", "ev hanako_billiards_serious", Trigger("ev hanako_billiards_timid_med", "ev hanako_billiards_timid"), "ev hanako_billiards_smile", "ev hanako_billiards_smile_close"),
    ("thumb/hanako_emptyclassroom.jpg", Trigger("evfg hanako_emptyclassroom", "evul hanako_emptyclassroom")),
    ("thumb/hanako_rage.jpg", "ev hanako_rage", "ev hanako_rage", "ev hanako_rage_sad"),
    ("thumb/hisao_scar.jpg", "ev hisao_scar"),
    ("thumb/hanako_scars.jpg", "ev hanako_scars"),
    ("thumb/hanako_bed.jpg", "evh hanako_bed_boobs_blush", "evh hanako_bed_boobs_blush", "evh hanako_bed_boobs_glance", "evh hanako_bed_crotch_blush", "evh hanako_bed_crotch_glance"),
    ("thumb/hanako_missionary.jpg", "evh hanako_missionary_underwear", "evh hanako_missionary_underwear", "evh hanako_missionary_open", "evh hanako_missionary_closed", "evh hanako_missionary_clench"),
    ("thumb/hanako_after.jpg", "ev hanako_after_worry", "ev hanako_after_smile"),
    ("thumb/hanako_park.jpg", "ev hanako_park_alone", "ev hanako_park_away", "ev hanako_park_look", "ev hanako_park_closed"),
    ("thumb/hanako_goodend.jpg", "unlock_ev hanako_goodend_close", "unlock_ev hanako_goodend", "unlock_ev hanako_goodend_muffin"),
    ("thumb/lilly_tearoom.jpg", "ev lilly_tearoom", "ev lilly_tearoom_open"),
    ("thumb/lilly_touch.jpg", "ev lilly_touch_uni", "ev lilly_touch_cheong", "ev lilly_touch_cas"),
    ("thumb/lilly_crane.jpg", "ev lilly_crane"),
    ("thumb/lilly_bedroom.jpg", "ev lilly_bedroom"),
    ("thumb/lilly_hanako_hug.jpg", Trigger("ev lilly_hanako_hug", "unlock_ev lilly_hanako_hug_end")),
    ("thumb/lilly_sleeping.jpg", "ev lilly_sleeping", "ev lilly_sleeping_smile"),
    ("thumb/lilly_trainride.jpg", Trigger("evfg lilly_trainride", "ev lilly_trainride"), Trigger("evfg lilly_trainride_smiles", "ev lilly_trainride_smiles"), "ev lilly_trainride_ni"),
    ("thumb/lilly_wheat.jpg", "unlock_ev lilly_wheat_close", "ev lilly_wheat_small"),
    ("thumb/lilly_handjob.jpg", "evhunlock lilly_handjob_chest_frown_small", "evhunlock lilly_handjob_chest_normal_small", "evh lilly_handjob_stroke_flustopen_small", "evh lilly_handjob_stroke_normopen_small", "evh lilly_handjob_stroke_normshut_small"),
    ("thumb/lilly_cowgirl.jpg", "evh lilly_cowgirl_cry_small", "evh lilly_cowgirl_frown_small", "evh lilly_cowgirl_smile_small", "evh lilly_cowgirl_strain_small", "evh lilly_cowgirl_weaksmile_small"),
    ("thumb/lilly_bath.jpg", "evh lilly_bath_emb_small", "evh lilly_bath_grab_small", "evh lilly_bath_moan_small", "evh lilly_bath_open_small", "evh lilly_bath_smile_small"),
    ("thumb/lilly_afterbath.jpg", "evh lilly_afterbath_open_small", "evh lilly_afterbath_shut_small"),
    ("thumb/lilly_kissing.jpg", "ev lilly_kissing"),
    ("thumb/lilly_masturbate.jpg", "evh lilly_masturbate", "evh lilly_masturbate_come", "evh lilly_masturbate_come_face"),
    ("thumb/lilly_restaurant.jpg", Trigger("ev lilly_restaurant_listen", "evul lilly_restaurant_listen"), Trigger("ev lilly_restaurant_sheepish", "evul lilly_restaurant_sheepish"), "ev lilly_restaurant_eat", "ev lilly_restaurant_chew", "ev lilly_restaurant_wine"),
    ("thumb/lilly_sheets.jpg", "ev lilly_sheets"),
    ("thumb/lilly_airport.jpg", "ev lilly_airport", "ev lilly_airport_end"),
    ("thumb/lilly_hospitalwindow.jpg", "ev lilly_hospitalwindow"),
    ("thumb/lilly_hospital.jpg", Trigger("ev lilly_hospitalclosed", "unlock_ev lilly_hospitalclosed"), Trigger("ev lilly_hospital", "unlock_ev lilly_hospital")),
    ("thumb/lilly_goodend.jpg", "unlock_ev lilly_goodend"),
    ("thumb/rin_eating.jpg", "ev rin_eating"),
    ("thumb/rin_artclass.jpg", "ev rin_artclass1", "ev rin_artclass2", "ev rin_artclass3", "ev rin_artclass4"),
    ("thumb/hisao_mirror.jpg", Trigger("ev hisao_mirror", "ev hisao_mirror_800")),
    ("thumb/rin_painting.jpg", "ev rin_painting_base", "ev rin_painting_foot", "ev rin_painting_faceconcerned", "ev rin_painting_concerned", "ev rin_painting_reply"),
    ("thumb/rin_rain.jpg", "ev rin_rain_away", "ev rin_rain_towards"),
    ("thumb/rin_high.jpg", "ev rin_high_frown", "ev rin_high_grin", "ev rin_high_grinwide", "ev rin_high_oneeye", "ev rin_high_open", "ev rin_high_smile", "ev rin_high_sleep"),
    ("thumb/rin_kiss.jpg", "ev rin_kiss"),
    ("thumb/rin_nap.jpg", "ev rin_nap_total", "ev rin_nap_total_awind", "ev rin_nap_close_awind", "ev rin_nap_close_awind_tears"),
    ("thumb/rin_wisp.jpg", "ev rin_wisp1", "ev rin_wisp2", "ev rin_wisp3", "ev rin_wisp4", "ev rin_wisp5"),
    ("thumb/rin_galleryskylight.jpg", "ovl rin_galleryskylight"),
    ("thumb/rin_orange.jpg", "ev rin_orange", "ev rin_orange_large"),
    ("thumb/rin_masturbate.jpg", "ev rin_masturbate_away","ev rin_masturbate_surprise", "ev rin_masturbate_frown", "ev rin_masturbate_doubt", "ev rin_masturbate_hug"),
    ("thumb/rin_relief.jpg", "evh rin_relief_down", "evh rin_relief_up"),
    ("thumb/rin_gallery.jpg", "ev rin_gallery"),
    ("thumb/rin_trueend.jpg", "ev rin_trueend_normal", "ev rin_trueend_smile", "ev rin_trueend_weaksmile", "ev rin_trueend_sad", "ev rin_trueend_closed", "ev rin_trueend_hug", "ev rin_trueend_hugclosed", "ev rin_trueend_gone"),
    ("thumb/rin_wet.jpg", "ev rin_wet_pan_down", "ev rin_wet_arms", "ev rin_wet_face_up", "ev rin_wet_face_down", "ev rin_wet_towel_up", "ev rin_wet_towel_down", "ev rin_wet_towel_touch"),
    ("thumb/rin_h2.jpg", "evh rin_h2_pan_surprise", "evh rin_h2_pan_away", "evh rin_h2_pan_closed", "evh rin_h2_nopan_closed", "evh rin_h2_hisao_closed"),
    ("thumb/rin_pair.jpg", "ev rin_pair_base_clothes","ev rin_pair_base"),
    ("thumb/rin_h.jpg", "evh rin_h_closed", "evh rin_h_left", "evh rin_h_normal", "evh rin_h_right", "evh rin_h_strain", "evh rin_h_closed_close", "evh rin_h_left_close", "evh rin_h_normal_close", "evh rin_h_right_close", "evh rin_h_strain_close"),
    ("thumb/rin_goodend.jpg", Trigger("rin goodend_1", "ev rin_goodend_1"), Trigger("rin goodend_1b", "ev rin_goodend_1b"), Trigger("rin goodend_2", "ev rin_goodend_2")),
    ("thumb/shizu_shanghai.jpg", "ev shizu_shanghai", "ev shizu_shanghai_borednormal", "ev shizu_shanghai_smirknormal", "ev shizu_shanghai_smirklaugh"),
    ("thumb/showdown.jpg", "ev showdown"),
    ("thumb/shizu_chess.jpg", "ev shizu_chess_base", "ev shizu_chess_base3", "ev shizu_chess_base2"),
    ("thumb/kenji_glasses.jpg", Trigger("evmg kenji_glasses_closed", "evul kenji_glasses_closed"), Trigger("evmg kenji_glasses_frown", "evul kenji_glasses_frown"), Trigger("evmg kenji_glasses_normal", "evul kenji_glasses_normal")),
    ("thumb/shizu_tanabata.jpg", "ev shizutanabata"),
    ("thumb/shizu_confess.jpg", "ev shizuconfess_normal", "ev shizuconfess_closed", "ev shizuconfess_smile"),
    ("thumb/shizu_hands.jpg", "ev shizu_hands"),
    ("thumb/shizu_couch.jpg", "ev shizu_couch"),
    ("thumb/shizune_car.jpg", "ev shizune_car"),
    ("thumb/shizu_fishing.jpg", "ev shizu_fishing_ah", "ev shizu_fishing_sl"),
    ("thumb/shizune_tied.jpg", "evh shizune_hcg_tied_blush_small", "evh shizune_hcg_tied_smile_small", "evh shizune_hcg_tied_stare_small", "evh shizune_hcg_tied_close_small", "evh shizune_hcg_tied_kinky1_small", "evh shizune_hcg_tied_kinky2_small", "evh shizune_hcg_tied_kinky3_small", Trigger("evh shizune_hcg_tied_kinky3_small", "evhul shizune_hcg_tied_hisao2_small")),
    ("thumb/misha_sad.jpg", "ev misha_sad"),
    ("thumb/misha_naked.jpg", "evh misha_naked"),
    ("thumb/misha_sex.jpg", "evh misha_sex_aside", "evh misha_sex_closed"),
    ("thumb/misha_roof.jpg", "ev misha_roof_closed", "ev misha_roof_angry", "ev misha_roof_normal", "ev misha_roof_sad"),
    ("thumb/shizu_roof.jpg", "ev shizu_roof","ev shizu_roof_smile", "ev shizu_roof_towardsnormal", "ev shizu_roof_towardsangry", "ev shizu_roof2_towardsangry"),
    ("thumb/shizu_flashback.jpg", "ev shizu_flashback"),
    ("thumb/shizu_undressing.jpg", "evh shizu_undressing_clothed_stare", "evh shizu_undressing_clothed_kiss", "evh shizu_undressing_clothed_blush", "evh shizu_undressing_unclothed_blush", "evh shizu_undressing_unclothed_closed", "evh shizu_undressing_unclothed_kiss", "evh shizu_undressing_unclothed_talk"),
    ("thumb/shizu_pushdown.jpg", "evh shizu_pushdown"),
    ("thumb/shizu_straddle.jpg", "evh shizu_straddle_open", "evh shizu_straddle_tease", "evh shizu_straddle_closed", "evh shizu_straddle_smile", "evh shizu_straddle_come"),
    ("thumb/shizu_table.jpg", "evh shizu_table_smile", "evh shizu_table_normal", "evh shizu_table_comeopen", "evh shizu_table_comeclosed"),
    ("thumb/misha_nightclass.jpg", "ev misha_nightclass"),
    ("thumb/shizu_badend.jpg", "ev shizu_badend"),
    ("thumb/shizu_goodend.jpg", "ev shizu_goodend", "ev shizu_goodend_pan"),
    ("thumb/cutin.png", "pills", "stuffedcat", "teaset", "shangpai", "wine", "musicbox closed", "musicbox open", "hanaphone", "phonestrap", "hanaphonestrap", "insert startpistol","invite", "sc_comp", "brailler", "chessboard", "kenjibox", "jigorocard", "letter_insert", "letter_open_insert", "letter_open_insert_2", "stallphoto_insert"),
    ("thumb/completionbonus.jpg", "completionbonus")
)

define adv = ADVCharacter(ctc="ctc", ctc_position="fixed", what_prefix=_("“"), what_suffix=_("”"))
define narrator = Character(what_prefix="", what_suffix="")

define hi  = Character(_("Hisao"),    who_color="#629276")
define ha  = Character(_("Hanako"),   who_color="#897CBF")
define emi = Character(_("Emi"),      who_color="#FF8D7C")
define rin = Character(_("Rin"),      who_color="#b14343")
define li  = Character(_("Lilly"),    who_color="#F9EAA0")
define shi = Character(_("Shizune"),  who_color="#72ADEE")
define mi  = Character(_("Misha"),    who_color="#FF809F")
define ke  = Character(_("Kenji"),    who_color="#CC7C2A")
define mu  = Character(_("Mutou"),    who_color="#FFFFFF")
define nk  = Character(_("Nurse"),    who_color="#FFFFFF")
define no  = Character(_("Nomiya"),   who_color="#E0E0E0")
define yu  = Character(_("Yuuko"),    who_color="#2c9e31")
define sa  = Character(_("Sae"),      who_color="#D4D4FF")
define aki = Character(_("Akira"),    who_color="#eb243b")
define hh  = Character(_("Hideaki"),  who_color="#6299FF")
define hx  = Character(_("Jigoro"),   who_color="#99AACC")
define emm = Character(_("Meiko"),    who_color="#995050")
define sk  = Character(_("Shopkeep"), who_color="#7187A8")
define mk  = Character(_("Miki"),     who_color="#AD735E")

define mi_shi     = Character(_("Shizune"), who_color="#FF809F")
define mi_not_shi = Character(_("{s}Shizune{/s} Misha"), who_color="#FF809F")

define mystery = Character("???")

define ssh = Character(kind=shi, what_prefix="[[", what_suffix="]")
define his = Character(kind=hi, what_prefix="[[", what_suffix="]")

define ha_  = Character(_("Purple-haired girl"), kind=ha)
define emi_ = Character(_("Twintails girl"), kind=emi)
define rin_ = Character(_("Strange girl"), kind=rin)
define li_  = Character(_("Wavy-haired girl"), kind=li)
define mi_  = Character(_("Laughing girl"), kind=mi)
define ke_  = Character(_("Bespectacled hallmate"), kind=ke)
define mu_  = Character(_("Tall man"), kind=mu)
define yu_  = Character(_("Librarian"), kind=yu)
define no_  = Character(_("Silver-haired man"), kind=no)
define sa_  = Character(_("Gallery owner"), kind=sa)
define aki_ = Character(_("Well-dressed person"), kind=aki)
define nk_  = Character(_("Smiling man"), kind=nk)
define hx_  = Character(_("Huge man"), kind=hx)
define hh_  = Character(_("Slim girl"), kind=hh)
define emm_ = Character(_("Woman with braid"), kind=emm)

define n = Character(kind=nvl, ctc=config.nvl_page_ctc, ctc_position="fixed", window_background="gui/bg/nvl.png", window_top_padding=60, window_left_padding=55, window_right_padding=70)

define rinbabble = Character(kind=n, what_prefix="{color=#FF8D7C}{b}" + _("Rin") + "{/b}{/color}\n" + _("“"), what_suffix=_("”"))

define nb = Character(kind=nvl, what_color="#666666", window_top_padding=210, window_xpadding=100)
define centered_b = nb
define centered_alive = nb

define _current_replay = None

default current_scene = ""

default credits_vid = None

# Act 1

define FR_EMI    = 1
define FR_HANAKO = 2
define FR_LILLY  = 3
define FR_RIN    = 4
define FR_SHIZU  = 5
define FR_KENJI  = 6

default force_route = None

default choices = list()

default attraction_sc = 0
default attraction_hanako = 0

default wanted_introduce = None

default talk_with_hanako = False
default wait_for_shizu   = False

default promised = None

default side_lilly = None

default go_for_it = None

default kick_shizu = None

default fun_fun_at_office = None

default are_student_council = None

default not_much_talking = None

default interested_in_art = None

init python:
    def go_through_lilly():
        return talk_with_hanako and side_lilly

    def go_through_shizu():
        return wait_for_shizu and not side_lilly

    def get_tired():
        return promised and go_for_it

    def got_kenji():
        return kick_shizu or fun_fun_at_office or not_much_talking

# Emi

default run_with_emi = None

default pressed_emi = None

default have_a_minute = None

default got_advice = None

default talk_to_her_mom = None

default let_misha_know = None

# Hanako

default ask_hanako = None

default like_hanako = None

default go_to_the_city = None

default agree_with_lilly = None

# Lilly

default want_true = None

default address_it = None

default mention_the_letter = None

# Rin

default rin_amazing = None

default its_refreshing = None

default be_like_rin = None

default believes_in_rin = False
default believes_in_half = False

default what_about_emi = None

default cant_leave_alone = None

default want_to_support = None

default explain = False

default is_true = None

# Shizune

default refuse_misha = None
