#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# author             twolaw_at_free_dot_fr
# name               ren-my-sub.en.py
# description        It renames subtitle files matching video files in the current
#                    directory to make them strictly similar and so media players
#                    will us it. Also works with tv series numbering like
#                    'dexter 3x04 xvid.srt' with 'Dexter.S03E04.avi'.
# how to use         1. Place this python file in the directory containing your
#                    movies and srt subtitles, then run it.
#                    2. Choose the mode: automatic mode will rename all matching
#                    subtitles, manual mode will ask you to confirm each file to
#                    be renamed.
# ------------------
# 01-apr-2011 v1     for python3
# ------------------

import os, re, sys

print('*       Rename subtitles       *')
print('*    corresponding to movies   *')
print('*   in the current directory   *\n')
#get the path
if '/' in sys.argv[0]:
  chemin='/'.join(sys.argv[0].split('/')[:-1])
else:
  chemin=os.getcwd()
print(chemin)

#get files names
fichiers=os.listdir(chemin)

#useless words to reject
naze=re.compile('the|le|les|un|une|hd(tv)?|xvid|divx|dvd(rip)?')

# reg expr. of extensions
subext=re.compile('srt$')
filmext=re.compile('(avi|mkv)$')

#split files into films and subs
films=[fich for fich in fichiers if filmext.search(fich)]
subs =[fich for fich in fichiers if subext.search(fich)]

print(len(films),'movies found.')
print(len(subs), 'subtitles found.')
auto=input('-> Mode: auto(a) or manual(m) ? ')
print('---------------------------------')

#slit words of a file
def motsde(fichier):
    lesmots=re.split('\W+|_+',fichier)
    #remove 1 letter words and the extension
    mots=[i for i in lesmots if len(i)>1 and not subext.search(i) and not filmext.search(i)]
    #return list of lists
    return mots

#get season and episode number if tv series
#needs a words list in entry
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

#needs: words lists of subs + words lists of films
def corresp(sub, film):
    ok=0
    #check 3 first words of each, if it matches: ok
    for i in range(min(len(sub),3)):
        for j in range(min(len(film),3)):
            if sub[i].lower()==film[j].lower() and not naze.search(sub[i].lower()): ok+=1
    #if bad tv series episode, back to 0
    if estserie(sub) and estserie(sub)!=estserie(film): ok=0
    return ok
    
#create words lists of lists
motsfilms=[motsde(i) for i in films]
motssubs=[motsde(i) for i in subs]

#here we go, check every srt file
cpte=s=0
for sub_ in motssubs:
    f=0
    for film_ in motsfilms:
        #if match and if names not strictly similar
        if corresp(sub_, film_) and subs[s][:-3]!=films[f][:-3]:
            print('    MOVIE= %s' % films[f])
            print(' SUBTITLE= %s' % subs[s])
            reponse='n'
            if auto[0]!='a': reponse=input('Rename? yes(y) no(n) ')
            if auto[0]=='a' or reponse[0]=='y':
                try:
                    os.rename(subs[s], films[f][:-3]+'srt')
                    cpte+=1
                except OSError:
                    print('/!\ Access error or file already exists!')
                else:
                    print(' -> Subtitle renamed.')
            else:
                    print(' -> Do nothing.')
            print('---------------------------------')
        f+=1
    s+=1
if cpte!=0: input('Finished, %d subtitles renamed!' % cpte)
else: input('Finished, no subtitle renamed.')

