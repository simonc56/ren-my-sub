#!/usr/bin/env python
# -*- coding:utf-8 -*-

# auteur             twolaw_at_free_dot_fr
# nom                ren-my-sub.en.py
# description        Renomme les fichiers de sous-titres correspondants aux
#                    fichiers vidéos du répertoire courant, pour leur donner
#                    exactement le même nom. Nécessaire pour que les lecteurs
#                    vidéo utilisent ces sous-titres automatiquement.
#                    Les fichiers de séries TV sont aussi pris en compte,
#                    par ex: 'dexter 3x04 xvid.srt' avec 'Dexter.S03E04.avi'.
# utilisation        1. Placer ce fichier python dans le répertoire contenant
#                    vos films et sous-titres, et l'exécuter.
#                    2. Choisir le mode: automatique renomme tous les fichiers
#                    srt qui correspondent à un film, manuel demande
#                    confirmation pour renommer chaque sous-titre.
# ------------------
# 01-avr-2011 v1     pour python3
# ------------------
    
import os, re, sys

print('*    Renomme les sous-titres    *')
print('*    correspondants aux films   *')
print('*   dans le répertoire courant  *\n')
#recuperation du chemin
if '/' in sys.argv[0]:
  chemin=os.path.abspath('/'.join(sys.argv[0].split('/')[:-1]))
else:
  chemin=os.getcwd()
print(chemin)

#recuperation des noms de fichiers
fichiers=os.listdir(chemin)

#mots inutiles a rejeter
naze=re.compile('the|le|les|un|une|hd(tv)?|xvid|divx|dvd(rip)?')

# reg expr. des extensions
subext=re.compile('srt$')
filmext=re.compile('(avi|mkv|mp4|mpg)$')

#separation de fichiers dans films et subs
films=[fich for fich in fichiers if filmext.search(fich)]
subs =[fich for fich in fichiers if subext.search(fich)]

print(len(films),'films trouves.')
print(len(subs), 'sous-titres trouves.')
auto=input('-> Mode: auto(a) ou manuel(m) ? ')
print('---------------------------------')

#separation des mots dans un fichier
def motsde(fichier):
    lesmots=re.split('\W+|_+',fichier)
    #enleve les mots de 1 lettre et l'extension
    mots=[i for i in lesmots if len(i)>1 and not subext.search(i) and not filmext.search(i)]
    #retourne une liste de listes
    return mots

#recupere n° de saison et episode si serie tv
#prend une liste de mots en entree
def estserie(mots):
    regex=re.compile('^(?P<sai>\d)(?P<epi>\d\d)$')
    regex2=re.compile('(?P<sai>\d{1,2})\D(?P<epi>\d\d)')
    for mot in mots:
        if regex.search(mot):
            episode=regex.search(mot).groups()
            return [int(i) for i in episode]
        elif regex2.search(mot):
            episode=regex2.search(mot).groups()
            return [int(i) for i in episode]
    return None

#prend en entree: liste de mots subs + liste de mots film
def corresp(sub, film):
    ok=0
    #parcours les 3 mots de chacun, si ca corresp: ok
    for i in range(min(len(sub),3)):
        for j in range(min(len(film),3)):
            if sub[i].lower()==film[j].lower() and not naze.search(sub[i].lower()): ok+=1
    #si mauvais episode de serie, on remet à 0
    if estserie(sub) and estserie(sub)!=estserie(film): ok=0
    return ok
    
#crée les listes de listes de mots
motsfilms=[motsde(i) for i in films]
motssubs=[motsde(i) for i in subs]

#parcours les subs
cpte=s=0
for sub_ in motssubs:
    f=0
    for film_ in motsfilms:
        #si correspondance et si noms pas strictement identiques
        if corresp(sub_, film_) and subs[s][:-3]!=films[f][:-3]:
            print('     FILM= %s' % films[f])
            print(' SS-TITRE= %s' % subs[s])
            reponse='n'
            if auto[0]!='a': reponse=input('Renomme? oui(o) non(n) ')
            if auto[0]=='a' or reponse[0]=='o':
                try:
                    os.rename(subs[s], films[f][:-3]+'srt')
                    cpte+=1
                except OSError:
                    print('/!\ Erreur d\'accès ou fichier déjà existant!')
                else:
                    print(' -> Sous-titre renommé.')
            else:
                    print(' -> Ne fait rien.')
            print('---------------------------------')
        f+=1
    s+=1
if cpte!=0: input('Terminé, %d sous-titres renommés!' % cpte)
else: input('Terminé, aucun sous-titre renommé.')

