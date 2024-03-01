label bus:
hide screen hubElements
show screen birthdayPicture with moveinbottom
a "oh là là, ça date ça..."
#show screen notificationWinted with dissolve
e_nvl "Vous avez reçu un colis Winted, pensez à le récupérer à temps"
a "Oh mince, j'avais complétement zappé !"
a "Allez !  je vais le chercher tout de suite sinon il va encore repartir"
$ renpy.scene(layer = "screens")
scene busAdFreeze
show busAdReveal
$ renpy.pause(3.0, hard=True)
a "mais...mais..."
a "C'est la photo de Pierre mon frère!"
a "Mais comment c'est possible, c'est ma photo en plus ! "
a "Elle doit même encore être sur mon téléphone"
show screen appsPhone(True,True,False,False,False,False)
while True:
    empty ""

label searchInGallery:
    show screen galeryOpening
    a "..."
    show screen galeryNoFilter
    hide screen galeryOpening
    a "Cherchons"
    a "Il faut que je fasse le tri !"
    show screen galeryFilter
    hide screen galeryNoFilter
    a "Non je n'ai rien...comment ça se fait ?"
    hide screen appsPhone
    show screen appsPhone(False,True,True,False,False,False)
    a "Elle doit être ailleurs..."
    while True:
        empty ""

label searchInDataCloud:
    a "elle est peut être sur le cloud..."
    show screen freeWifi
    a "il me reste encore un peu de forfait"
    while True:
        empty ""

label travelToStore:
    hide busAdFreeze
    hide screen galeryFilter
    show getInsideBus
    $ renpy.pause(3.0, hard=True)
    a "mais comment ils ont obtenu cette photo..."
    $ renpy.pause(3.0, hard=True)
    show exitBus
    $ renpy.pause(3.0, hard=True)
    show getInStore
    $ renpy.pause(3.0, hard=True)
    show homeStore

#All scenes elements used in this label
screen galeryOpening:
    add "UI/applications/galeryOpening.png" xalign 0.5 yalign 0.5
    add "smartphoneFrameTransparent.png" xalign 0.5 yalign 0.5

screen galeryNoFilter:
    add "UI/applications/galeryNoFilter.png" xalign 0.5 yalign 0.5
    add "smartphoneFrameTransparent.png" xalign 0.5 yalign 0.5

screen birthdayPicture:
    add "UI/Cadre/frameBirthday.png" xalign 0.5 yalign 0.5

screen notificationWinted:
    add "UI/Cadre/notificationWinted.png" xalign 0.75 yalign 0.8

screen freeWifi:
    add "smartphone.png" xalign 0.5 yalign 0.5
    add "UI/applications/FreeWifi.png" xalign 0.5 yalign 0.5
    hbox:
        xalign 0.5
        yalign 0.65
        spacing 10
        imagebutton:
            idle "UI/applications/yes_idle.png"
            hover "UI/applications/yes_hover.png"
            action Call("addPoints",-5,"point_sociaux","","","Faites attention, sur des réseaux publics vous n'êtes pas protégé ! ","")
        imagebutton:
            idle "UI/applications/no_idle.png"
            hover "UI/applications/no_hover.png"
            action Call("addPoints",5,"point_sociaux","","Bravo","Faites attention, sur des réseaux publics vous n'êtes pas protégé ! ","")

    add "smartphoneFrameTransparent.png" xalign 0.5 yalign 0.5

screen cloudPhotos:
    add "smartphone.png" xalign 0.5 yalign 0.5
