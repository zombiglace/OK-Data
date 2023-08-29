screen hubElements:

    if hubClickable["dog"] == 1:
        imagebutton:
            xpos 1400
            ypos 797
            idle "UI/imagebuttons/dog_idle.png"
            hover "UI/imagebuttons/dog_hover.png"
            action Jump("walkOut")

    if hubClickable["phone"] == 1:
        imagebutton:
            xpos 1175
            ypos 607
            idle "UI/imagebuttons/phone_idle.png"
            hover "UI/imagebuttons/phone_hover.png"
            action Jump("barOut")

    if hubClickable["phoneCall"] == 1:
        imagebutton:
            xpos 1175
            ypos 607
            idle "UI/imagebuttons/phone_idle.png"
            hover "UI/imagebuttons/phone_hover.png"
            action Jump("browserLabel")

    if hubClickable["watch"] == 1:
        imagebutton:
            xpos 230
            ypos 838
            idle "UI/imagebuttons/watch_idle.png"
            hover "UI/imagebuttons/watch_hover.png"
            action Jump("browserLabel")
    #...
    #add list of hub clickable elements here

#Screen when head phone is just visible with settings icons
screen phoneDown :
    imagebutton:
        xalign 0.9
        yalign 3.0
        idle "smartphone.png"
        action Jump("telplay")
    hbox:
        spacing 20
        xalign 0.87
        yalign 0.95
        imagebutton:
            if BluetoothState == True:
                idle "UI/settingsIcons/BluetoothON.png"
                hover "UI/settingsIcons/BluetoothOFF.png"
            else:
                idle "UI/settingsIcons/BluetoothOFF.png"
                hover "UI/settingsIcons/BluetoothON.png"
            action SetVariable("BluetoothState", not BluetoothState)
        imagebutton:
            if DataState == True:
                idle "UI/settingsIcons/DataON.png"
                hover "UI/settingsIcons/DataOFF.png"
            else:
                idle "UI/settingsIcons/DataOFF.png"
                hover "UI/settingsIcons/DataON.png"
            action SetVariable("DataState", not DataState)
        imagebutton:
            if LocalisationState == True:
                idle "UI/settingsIcons/LocalisationON.png"
                hover "UI/settingsIcons/LocalisationOFF.png"
            else:
                idle "UI/settingsIcons/LocalisationOFF.png"
                hover "UI/settingsIcons/LocalisationON.png"
            action SetVariable("LocalisationState", not LocalisationState)


#Smartphone home screen
#Each argument is one application icon that can be avaible or not
screen telephoneplayer(A1=True,A2=True,A3=True,B1=True,B2=True,B3=True) :
    imagebutton:
        xalign 0.5
        ypos 150
        idle "smartphone.png"

    imagebutton:
        xalign 0.5
        yalign 0.95
        idle "masquetelephone.png"
        hover "masquetelhiver.png"
        action Hide("telephoneplayer"), Jump("lPhoneDown")

    frame:
        background None
        xalign 0.5
        yalign 0.4
        xmaximum 360
        ymaximum 700
        grid 3 2:
            spacing 20
            imagebutton:
                xalign 0.5
                yalign 0.5
                if A1:
                    idle "UI/applications/appOKDATA.png"
                    hover "UI/applications/appOKDATA_hover.png"
                    action Jump("selfie")
                else:
                    idle "UI/applications/appOKDATA_out.png"
            imagebutton:
                xalign 0.5
                yalign 0.5
                if A2:
                    idle "UI/applications/appphoto.png"
                    hover "UI/applications/appphotohover.png"
                    action Jump("selfie")
                else:
                    idle "UI/applications/appphotoout.png"
            imagebutton:
                xalign 0.5
                yalign 0.5
                if A3:
                    idle "UI/applications/appphoto.png"
                    hover "UI/applications/appphotohover.png"
                    action Jump("selfie")
                else:
                    idle "UI/applications/appphotoout.png"
            imagebutton:
                xalign 0.5
                yalign 0.5
                if B1:
                    idle "UI/applications/appphoto.png"
                    hover "UI/applications/appphotohover.png"
                    action Jump("selfie")
                else:
                    idle "UI/applications/appphotoout.png"
            imagebutton:
                xalign 0.5
                yalign 0.5
                if B2:
                    idle "UI/applications/appphoto.png"
                    hover "UI/applications/appphotohover.png"
                    action Jump("selfie")
                else:
                    idle "UI/applications/appphotoout.png"
            imagebutton:
                xalign 0.5
                yalign 0.5
                if B3   :
                    idle "UI/applications/appphoto.png"
                    hover "UI/applications/appphotohover.png"
                    action Jump("selfie")
                else:
                    idle "UI/applications/appphotoout.png"


    hbox:
        xalign 0.5
        yalign 0.2
        spacing 20
        imagebutton:
            if BluetoothState == True:
                idle "UI/settingsIcons/BluetoothON.png"
                hover "UI/settingsIcons/BluetoothOFF.png"
            else:
                idle "UI/settingsIcons/BluetoothOFF.png"
                hover "UI/settingsIcons/BluetoothON.png"
            action SetVariable("BluetoothState", not BluetoothState)
        imagebutton:
            if DataState == True:
                idle "UI/settingsIcons/DataON.png"
                hover "UI/settingsIcons/DataOFF.png"
            else:
                idle "UI/settingsIcons/DataOFF.png"
                hover "UI/settingsIcons/DataON.png"
            action SetVariable("DataState", not DataState)
        imagebutton:
            if LocalisationState == True:
                idle "UI/settingsIcons/LocalisationON.png"
                hover "UI/settingsIcons/LocalisationOFF.png"
            else:
                idle "UI/settingsIcons/LocalisationOFF.png"
                hover "UI/settingsIcons/LocalisationON.png"
            action SetVariable("LocalisationState", not LocalisationState)


screen browserWindow:
    add "UI/browser/frameDataBook.png" xalign 0.5 yalign 0.5
    side "c b r":
         area (700, 200, 646, 700)

         viewport id "vp":
             draggable True
             vbox:
                 spacing 30
                 imagebutton:
                     idle "UI/browser/eventBanner.png"
                 imagebutton:
                     idle "UI/browser/eventBirtdhay.png"
                 imagebutton:
                     idle "UI/browser/alarmArticle.png"
             #add "UI/browser/feedDataBook.png"

         bar value XScrollValue("vp")
         vbar value YScrollValue("vp")

screen callPhone:
    add "smartphoneBlack.png" xalign 0.5 yalign 0.5
    add "UI/call/incoming_call_mother.png" xalign 0.5 yalign 0.5
    imagebutton:
        xalign 0.5
        yalign 0.69
        idle "UI/call/answer_idle.png"
        hover "UI/call/answer_hover.png"
        action Hide("")

style bubble_tuto:
    background "#e226c0"
    xpadding 30
    ypadding 30

screen bubbleTuto(value="mon texte", posX=0, posY=0):
    add "UI/bubbletuto/bubbletop.png" xpos posX ypos posY
    frame:
        style "bubble_tuto"
        xpos posX
        ypos posY+20
        text value xalign 0.5 yalign 0.5

screen dataMap:
    add "smartphone.png" xalign 0.5 yalign 0.5
    add "UI/applications/dataMap.png" xalign 0.5 yalign 0.5
    frame:
        background #ffffff
        xalign 0.5
        yalign 0.65
        text "{color=#000000}{size=-10}Veuillez activer la \ngéolocalisation pour \nconnaitre l'itinéraire{/size}{/color}" xalign 0.5 yalign 0.5

screen phoneCall:
    add "smartphoneBlack.png" xalign 0.5 yalign 0.5


#Screen phone when selfie photo is display
screen selfie :
    add "smartphoneBlack.png" xalign 0.5 yalign 0.5
    add "UI/applications/selfie.png" xalign 0.5 yalign 0.5
    imagebutton:
        xalign 0.5
        yalign 0.8
        idle "UI/applications/Icons/send_idle.png"
        hover "UI/applications/Icons/send_hover.png"
        action Jump("barOutAfter")
