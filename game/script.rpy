# This is used for top-level game structure.
# Should not include any actual events or scripting; only logic and calling other labels.

label start:

    # Set the ID of this playthrough
    $ anticheat = persistent.anticheat

    # We'll keep track of the chapter we're on for poem response logic and other stuff
    $ chapter = 0

    #If they quit during a pause, we have to set _dismiss_pause to false again (I hate this hack)
    $ _dismiss_pause = config.developer

    # Each of the girls' names before the MC learns their name throughout ch0.
    $ s_name = _("Саёри")
    $ m_name = _("Моника")
    $ n_name = _("Нацуки")
    $ y_name = _("Юри")
    $ mum_name = _("Мама")
    $ tchr_name = _("Учитель")
    $ drk_name = _("Директор")
    $ guide_name = _("Экскурсовод")
    $ h_name = _("Ханако")

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True

    #This section detemines the "Act Structure" for the game.
    # persistent.playthrough variable marks each of the major game events (Sayori hanging, etc.)
    #Here is an example of how you might do that
    if persistent.playthrough == 0:
        #Call example script
        call mainscript from _call_mainscript
#		from _call_mainscript
    return

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
