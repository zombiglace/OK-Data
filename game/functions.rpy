# function to call to add value to one of lifebar element
# value = number to increment
# key = wich lifebar element has to be increment
# condition = if condition is not empty, increment will be effective if the condition is true else it will decrement
# losemessage = message to display if player lose points
# winmessage = message to display if player earn points
# labelNext = allow to jump to another label at the end of the function if needed
# Exemple d'usage de la fonction :
# addPoints(5,'point_sante',BluetoothState,True,"Vous n'avez pas désactivé le bluetooth", "Vous avez bien pensé à désactiver le bluetooth")
label addPoints(values = 0, key = '', condition = '', conditionValue = True, losemessage='', winmessage='', labelNext= ''):
    $ oldValue = points[key][0]
    if not condition:
        $ points[key][0] += values
    else:
        if condition == conditionValue:
            $ points[key][0] += values
        else:
            $ points[key][0] -= values
    $ newValue = points[key][0]
    nvl clear
    #you lose points
    if newValue < oldValue :
        show screen barre_de_vie with hpunch
        if losemessage:
            $ phrases = losemessage.split("µ")
            $ nbrPhrases = len(phrases)
            $ i = 0
            while i < nbrPhrases:
                $ phrase = phrases[i]
                e_nvl '[phrase]'
                $ i = i + 1
    #nothing happens
    elif newValue == oldValue :
        return
    #you earn points
    else:
        if winmessage:
            #e_nvl '[winmessage]'
            $ phrases = winmessage.split("µ")
            $ nbrPhrases = len(phrases)
            $ i = 0
            while i < nbrPhrases:
                $ phrase = phrases[i]
                e_nvl '[phrase]'
                $ i = i + 1
    #If needed, after text messages, jump to this label if needed
    if not labelNext:
        return
    else:
        $ renpy.scene(layer = "screens")
        $ renpy.jump(labelNext)


label checkClueALL():
    python:
        for key, value in combinaisonClues.items():
            if (whatInsideTop == value[0] and whatInsideBottom == value[1]) or (whatInsideTop == value[1] and whatInsideBottom == value[0]):
                if value[4] == False:
                    phrase = value[3]
                    renpy.say(e_nvl, phrase)
                    cluesDisplay += value[2]
                    value[4] = True
                    if categoriesIndex < len(combinaisonClues) :
                        categoriesIndex += 1
                    else:
                        renpy.jump('endAlgorithm')
                else:
                    renpy.say(e_nvl, "Tu as déjà trouvé cet indice")

#clean the clues spot
label clearClues():
    $ whatInsideTop = ""
    $ whatInsideBottom = ""

#Function to display information when click on specific word
style infoStyle:
    xalign 0.5
    

init python:
  def information_display(txt):
    renpy.call_in_new_context("infoLabel",txt)

label infoLabel(txt):
    info "[txt]"

define config.hyperlink_handlers = {
    "information": information_display
}