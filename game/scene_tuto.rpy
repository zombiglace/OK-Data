label tuto:
    $ posY = 175
    scene hub
    show hubDogCouch
    show screen barre_de_vie
    medBubble "Vos {a=information: C'est une information qui permet d’identifier directement ou indirectement une personne.}données personnelles{/a} sont réparties en 6 catégories"
    medBubble "Les données de centre d’intérêt"
    medBubble "Les données de santé"
    medBubble "Les données de convictions"
    medBubble "Les données de localisation"
    medBubble "Les données de réseaux sociaux"
    medBubble "Les données administratives"
    medBubble "Au-dessus de chaque icône est indiqué le nombre de points restants."
    call addPoints(-5,'point_administrative')
    medBubble "Tu perds des points si tu ne prêtes pas attention à préserver ta vie privée."
    call addPoints(5,'point_administrative')
    medBubble "Au contraire, tu gagneras des points : \nEn faisant les bons choix, \nEn regardant les contenus supplémentaires,\nEn allant vous promener!" 
    jump hub
