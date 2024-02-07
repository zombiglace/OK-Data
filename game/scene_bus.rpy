label bus:
hide screen hubElements
show screen birthdayPicture with moveinbottom
a "oh là là, ça date ça..."
call addPoints(-5,'point_sociaux',"","","Chaque photo stocké sur un serveur, n'est plus à vous")
show screen notificationWinted with dissolve
a "Oh mince, j'avais complétement zappé !"
a "Allez je vais le cherche de suite sinon il va encore repartir"
$ renpy.scene(layer = "screens")
scene busAdFreeze
show busAdReveal
$ renpy.pause(3.0, hard=True)
a "c'est bon, ce n'est pas encore mon bus"
a "mais...mais..."
a "C'est pas possible c'est Thierry !"
a "Mais comment ils ont eu cette photo, je l'ai déjà vu"
a "C'est moi qui l'ai prise, j'en suis sûre, elle doit être sur mon téléphone"
show screen appsPhone(True,True,True,False,False,False)
while True:
    empty ""

label serachInGallery:
    show screen galeryOpening
    show screen galeryNoFilter
    hide screen galeryOpening
    a "Cherchons"
    a "Il faut que je fasse le tri"
    show screen galeryFilter
    hide screen galeryNoFilter
    a "Non je n'ai rien...comment c'est possible"
    hide screen appsPhone
    show screen appsPhone(False,True,True,False,False,False)
    a "Elle doit être ailleurs..."
    while True:
        empty ""

label searchInDataCloud:
    a "elle est peut être sur le cloud..."
    show screen freeWifi
    a "il me reste encore un peu de forfais"
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
    add "UI/applications/galeryOpening.jpg" xalign 0.5 yalign 0.5
    add "smartphoneFrameTransparent.png" xalign 0.5 yalign 0.5

screen galeryNoFilter:
    add "UI/applications/galeryNoFilter.jpg" xalign 0.5 yalign 0.5
    add "smartphoneFrameTransparent.png" xalign 0.5 yalign 0.5

screen galeryFilter:
    add "UI/applications/galeryFilter.jpg" xalign 0.5 yalign 0.5
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
            action Call("addPoints",-5,"point_sociaux","","","Faites attention µSur des réseaux publics, vous n'êtes pas protégé ! ","")
        imagebutton:
            idle "UI/applications/no_idle.png"
            hover "UI/applications/no_hover.png"
            action Call("addPoints",5,"point_sociaux","","Bravo","Faites attention µSur des réseaux publics, vous n'êtes pas protégé ! ","")

    add "smartphoneFrameTransparent.png" xalign 0.5 yalign 0.5
