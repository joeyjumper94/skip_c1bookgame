label skip_c1booksort_skip_choice:
    if persistent.c1booksort:#aced the book game in a previous run
        $ renpy.pause (0.3)
        play sound "fx/system3.wav"
        call syscheck from skip_c1booksort_syscheck
        call skiptut from skip_c1booksort_skiptut
        if skipbeginning == False:
            if system == "normal":
                s "My records indicate you have already experienced this section in a satisfactory manner. Would you like to skip to this minigame?"
            elif system == "advanced":
                s "It looks like you've aced this minigame before. skip it?"
            else:
                s "So, it turns out you've completed this minigame. Either you could do this again, or we could save some time and just skip past it."
        $ skipbeginning = False
        menu:
            "Yes. I want to skip ahead.":
                play sound "fx/system3.wav"
                s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
                $ persistent.skipnumber += 1
                call skipcheck from skip_c1booksort_skipcheck
                play sound "fx/booksort.wav"
                $ renpy.pause (4.0)
                show remy normal with easeinright
                Ry "Oh, you're done? Let's take a look, then. "
                $ mp.remybooks = 8
                $ mp.save()
                $ remymood += 3
                show remy smile with dissolve
                Ry "Seems you got it all right. Well done, [player_name]. "
                menu:
                    "Phew, that was hard work. ":
                        $ renpy.pause (0.5)
                        show remy normal with dissolve
                        Ry "It does gets easier with practice. "
                        jump remycont
                    "That wasn't too hard... ":
                        $ renpy.pause (0.5)
                        show remy normal with dissolve
                        jump remycont
                    "I didn't know I could have this much fun in a library. ":
                        $ renpy.pause (0.5)
                        show remy normal with dissolve
                        Ry "I can't tell if you are serious, but I appreciate your help regardless. "
                        jump remycont
            "No. Don't skip ahead.":
                play sound "fx/system3.wav"
                s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
    else:
        pass
    label skip_c1booksort_skip_no:
        pass