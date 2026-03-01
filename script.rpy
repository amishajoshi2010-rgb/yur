image bg starter = "background1.png"
image bg stairs = "stairs1.jpeg"
image bg setting1 = "setting1.png"
image bg setting2 = "setting2.png"
image bg doors = "doors1.png"
image black = Solid((0, 0, 0, 255))

image anormal = "name.png"
image aquestion = "nameq.png"
image atalkingh = "nametalkingh.png"
image atalkings = "nametalkings.png"
image aangry = "nameangyrypng"

define e = Character("Name")
define g = Character("Little Girl")
define n = Character("Narrator")
define a = Character("Antagonist")
label start:
    $save_name: "Introduction"
    scene background1 
    n " You awaken to find yourself in a rural area with tattered buildings. Someone unknown lays beside you, clearly knocked out."
    n "You try to remember what happened, but you can't seem to remember anything."
    n "Terrified at the unfamiliarity you begin to stand, with trouble, and face a random direction prepared to run to wherever the world takes you, until suddenly a weirdly excited voice is heard."
    pause 3
    show name
    a "Oh my god, who are you? I swear I know you from somewhere! What's your name?"
    n "It seems like, like the peculiarity of this, you can't remember. This is your chance to name yourself and begin again."
    # enter name here
    e "My name is... but I don't know who you are..."
    a "Anyway, let's stick together! We're in the same situation anyway."
    n "Walking down the street, there is a particular building which you see."
    n "It looks slightly better than the rest, and you want to go in."
    n " Antagonist's eyes follow yours, before her expression turns panicked."
    pause
    a "I wouldn't suggest going there."
    e "Why?"
    a "I just have a bad feeling about this place."

    menu:
        "Drag them into the building":
            jump intobuilding_path
        "Follow her towards another.":
            jump following_path
label intobuilding_path:
    e "Nah, I'm going into this one. I have a good feeling and I don't know who you are."
    n "Antagonists face flashes with anger before turning back into an eerie smile. (maybe show this as an image and remove this line)"
    a "Okay, fine! Let's go!"
    pause 2.5
    n "You both enter."
    scene doors 
    n " Within, stairs face two doors where you're left to make a choice."
label following_path:
    a "Okay, great. Trust me on this, that building over there is much better."
    n "The building looks less destroyed, yet your stomach churns. Despite this, you still go in."
    n "Within, stairs face two doors where you're left to make a choice."
label continue_game:
    n "Door One is where lights flash and bumping music plays."
    n "Door two remains quiet and dark..."
    menu:
        "Door ONE":
            jump one_path
        "Door TWO":
            jump two_path
label one_path:
    a "This place is amazing! You were right!"
    n "Inside, people are all around dancing and laughing. Drinks of every colour are placed on circular tables and people also sit, playing cards."
    n "You pause at the scene, unsure how to feel."
    a "Are you okay?"
    menu:
        "Yeah, I'm okay.":
            jump okay1_path
        "Nah, lets get out of here.":
            jump nah1_path

label two_path:
    n "The place is covered in vines and the walls are filled with chopped bricks."
    a "I don’t know how to feel about this place    ."
    n "You scan the place, unsure how to feel about it."
    a "Are you okay?"


label okay1_path:
   a "Phew! That was rough! Wait… what’s here?"
   n "To your left, another two doors are side by side, but they have completely different feelings compared to the other ones. On the other side, is a balcony which faces inside the building. The cracked roof is closer than before."
   n "You realise you are one floor up in the building."
   a "Another two doors?!?! This is insane. We should leave."
   e "We’re already here this much. We might as well pick another door."
   n "Room 3 has a red glow and calming, ambient music playing. Room 4 has a yellow-light glow within."


label nah1_path:
   n "When you enter, it’s like a playground. Ball pits, jumping castles and slides. A little kid comes up to you, yet something feels off."
   a "Awww, little kids! Hi! What’s your name?"
   g "Violet. Wanna play?"
   a "Yes, sure! ____, you wanna join?"
   menu:
       "Yes, I'll play!":
            jump play_path
       "No, I’ll just watch.":
           jump watch_path

label play_path:
    "die"
    jump cont

label watch_path:
    "watch die"
    jump cont

label cont:
    return