label barOut:
    nvl clear
    show screen phoneDown
    syrielle_nvl "Salut frangine ! On se retrouve au \n {u}Bar chez Thon Thon \n rue du port{/u}"
    hide screen hubElements
    show screen dataMap
    empty ""
    while LocalisationState == False:
        empty ""
    hide screen dataMap
    scene bar
    show barSister
    empty ""
    s "Ça fait longtemps, je suis heureuse de te revoir ! "
    s "Aller, on se fait un {a=information:Un selfie est une pratique photographique narcissique, visant à se prendre soi même en photo de manière ouf, visant à se prendre soi même en photo de manière ouf}Selfie{/a} et on l’envoie à Pierrot, il sera content de revoir ses sœurettes ! "
    s "Mais attention ! pas de gaffes sur son anniversaire surprise ! "
    a "OK, je prends mon téléphone."
    show screen selfie
    with dissolve
    while True:
        empty ""

label barOutAfter:
    nvl clear
    call addPoints(5,'point_localisation',LocalisationState, False, "Raté ! \n En laissant ta géolocalisation activée, ta localisation sera présente dans les métadonnées de ta photo. N’importe qui peut ainsi savoir où tu étais.", "Bravo  ! \n Tu gagnes des points de géolocalisation, en pensant à la désactiver. De cette façon, ta photo ne contient pas d'information de localisation.") from _call_addPoints
    hide screen selfie
    $ hubClickable["phone"]= 0
    $ hubClickable["phoneCall"]= 1
    jump hub
