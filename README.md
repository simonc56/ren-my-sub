Description
-----------

Renomme les fichiers de sous-titres correspondants aux
fichiers vidéos du répertoire courant, pour leur donner
exactement le même nom. Nécessaire pour que les lecteurs
vidéo utilisent ces sous-titres automatiquement.

Les fichiers de séries TV et leur numérotation d'épisodes
sont aussi pris en compte, par ex: 'dexter 3x04 xvid.srt'
avec 'Dexter.S03E04.avi'.


Utilisation
-----------

1. Placer le fichier python dans le répertoire contenant
   vos films et sous-titres, et le lancer.
2. Choisir le mode: automatique renomme tous les fichiers
   de sous-titre qui correspondent à un film, manuel demande
   confirmation pour renommer chaque sous-titre.


Script en action (exemple)
--------------------------

    *    Renomme les sous-titres    *
    *    correspondants aux films   *
    *   dans le répertoire courant  *

    -> Mode: auto(a) ou manuel(m) ? m
    ---------------------------------
         FILM= mulholland drive.avi
     SS-TITRE= Mulholland.Drive.2001.[Special.Edition].srt
    Renomme? oui(o) non(n) o
     -> Sous-titre renommé.
    ---------------------------------
         FILM= The.Simpsons.S22E15.HDTV.Xvid-LOL.avi
     SS-TITRE= simpsons 22x15.srt
    Renomme? oui(o) non(n) o
     -> Sous-titre renommé.
    ---------------------------------
         FILM= BiG.Bang.Theory.S02E18.en.avi
     SS-TITRE= The Big Bang Theory - 218 - The Work Song Nanocluster.srt
    Renomme? oui(o) non(n) o
     -> Sous-titre renommé.
