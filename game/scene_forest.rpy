label forest :
  nvl clear
  hide screen hubElements
  show screen barre_de_vie
  show walkingForest
  a "Oh c'est tellement bien d'être en forêt loin des réseaux, je me sens ressourcée"
  call addPoints(2,'point_localisation')
  a "Je récupère des points de vie privée (localisation)"
  call addPoints(2,'point_sociaux')
  a "Je récupère des points de vie privée (sociaux)"
  call addPoints(2,'point_sante')
  a "Je récupère des points de vie privée (santé)"
  call addPoints(2,'point_administrative')
  a "Je récupère des points de vie privée (administrative)"
  call addPoints(2,'point_interet')
  a "Je récupère des points de vie privée (interet)"
  call addPoints(2,'point_conviction')
  a "Je récupère des points de vie privée (conviction)"
  a "Je suis trop content"
  $ hubClickable["forest"]= 0
  jump hub
