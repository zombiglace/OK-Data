label browserLabel:
    $ hubClickable["phoneCall"]= 0
    scene hub
    hide screen hubElements
    hide screen phoneDown
    show Player_Sitting
    show screen callPhoneIncoming
    while True:
        empty ""

label browserLabelCall:
    show screen callPhoneAnswer
    a "Ouiiiii maman"
    m "Salut ma grande"
    m "ça va ?"
    jump browserLabelAfterCall
    while True:
        empty ""

label browserLabelAfterCall:
    hide screen callPhoneIncoming
    hide screen callPhoneAnswer
    scene lounge
    show loungeIdle
    show screen phoneDown
    a "Alors Maman, qu’est-ce que je peux faire pour toi ?"
    m "Un ami de ton frère m'a demandé de lui envoyer des photos sur Databook, je ne sais pas comment ça marche … "
    a "Mais tu n’as pas de compte Databook !? il va falloir t’en créer un."
    m "Oh je préfère que tu le créé toi !Tiens voila mes papiers d’identité si tu en as besoin."
    hide screen phoneDown
    show loungeZoom
    empty ""
    show screen browserWindowSubscribe
    show loungeHandIn onlayer overlay
    hide loungeIdle
    while True:
        empty ""

label browserLabelFeed:
    #call addPoints(5,'point_sociaux',GoodState,True,"Vous perdez des points ! µEvitez de donner trop d’informations. Les champs obligatoires (indiquées par un astérisque) sont suffisants. µCela contribue à divulguer vos données personnelles d’identité.µDes grandes Société comme ici DATABOOK récoltent ces données et les revendent ensuite µ cela à des fins de marketing ou à d’autres sociétés parfois peu scrupuleuses. ", "Bravo ! µ\n Il est parfois bon de ne pas trop en dire.µLes champs obligatoires (indiquées par un astérisque) sont suffisants. µTrop de précision sur votre identité contribue à divulguer vos données personnelles d’identité.µ Des grandes Société comme ici DATABOOK récoltent ces données et les revendent ensuite \n soit à des fins de marketing soit à d’autres sociétés parfois peu scrupuleuses.") from _call_addPoints_1
    show loungeZoomFix
    show screen browserWindowFeed
    hide screen browserWindowSubscribe
    hide screen browserWindowSubscribeFake
    hide screen browserWindowSubscribeTrue
    show screen barre_de_vie
    a "Voila maman, il ne te reste plus qu'à lire l'évènement \n qu'ils ont créé pour l'anniversaire de Thierry ! "
    while True:
        empty ""

label insideEventPage:
    hide screen browserWindowFeed
    show screen insideEvent
    show screen barre_de_vie
    a "Tu as vu ? Ils proposent de partager des photos"
    m "C'est incroyable"
    while True:
        empty ""

#Screens used in scene_browser

screen insideEvent:
    add "UI/browser/frameDataBook.png" xpos 42 ypos 97
    side "c b r":
        area (358, 160, 675, 800)
        viewport id "vp":
            draggable True
            vbox:
                spacing 0
                imagebutton:
                    idle "UI/browser/EventPage.png"
                hbox:
                    xalign 0.7
                    spacing 10
                    imagebutton:
                        idle "UI/browser/sendPhotosDatabook.png"
                        hover "UI/browser/sendPhotosDatabook.png"
                        action Call("addPoints",-2,'point_administrative',"","","Vous auriez dû envoyer vos photos via mail","",'hub')
                    imagebutton:
                        idle "UI/browser/sendPhotosMail.png"
                        hover "UI/browser/sendPhotosDatabook.png"
                        action Call("addPoints",2,'point_administrative',"","","","Vous avez bien fait",'hub')
        bar value XScrollValue("vp")
        vbar value YScrollValue("vp")
