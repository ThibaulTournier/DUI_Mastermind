# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 21:06:06 2023

@author: Utilisateur
"""
import msvcrt
import os 
import sys
from getpass import getpass
from random import randint
couleurs=[0,1,2,3,4,5,6,7]
proposition=[1,2,4,5]
solution=[1,0,1,2]
def nb_bien_places(proposition, solution):
    n=0
    for i in range(len(proposition)):
        if proposition[i]==solution[i]:
            n+=1
    return n

def nb_bien_places_couleur(proposition, solution, couleur):
    n=0
    for i in range(len(proposition)):
        if (proposition[i]==couleur) and (solution[i]==couleur):
            n+=1
    return n

def compte_occurences(liste):
    l=[]
    for i in range(8):
        n=0
        for j in range(len(liste)):
            if liste[j]==i:
                n+=1
        l.append(n)
    return l

def min_int(x,y):
    if x<y:
        return x
    else :
        return y

def nb_couleurs_mal_placees(proposition, solution):
    occurence_proposition=compte_occurences(proposition)
    occurence_solution=compte_occurences(solution)
    nbr_couleurs_mp=0
    for i in range(8):
        x=occurence_proposition[i]
        y=occurence_solution[i]
        mal_place=min(x,y)-nb_bien_places_couleur(proposition,solution,i)
        nbr_couleurs_mp+=mal_place
    return nbr_couleurs_mp

def generate_solution(nbr_pions):
    l=[]
    for i in range(nbr_pions):
        l.append(randint(0,7))
    return l

def tentative(solution,nbr_pions):
    print('Quelles couleurs proposez vous?')
    l=[]
    for i in range(nbr_pions):
        l.append(int(input()))
    a=nb_couleurs_mal_placees(l,solution)
    b=nb_bien_places(l,solution)
    return l,a,b

def tentative2j(solution,nbr_pions):
    print('Joueurs 2, quelles couleurs proposez vous?')
    l=[]
    for i in range(nbr_pions):
        l.append(int(input()))
    a=nb_couleurs_mal_placees(l,solution)
    b=nb_bien_places(l,solution)
    return l,a,b



def parti1joueur(nbr_pions):
        
    la_solution=generate_solution(nbr_pions)
    nb_tentative=0
    la_proposition=[]
    while (nb_tentative<10)or(la_proposition==la_solution):
        tentative1=tentative(la_solution,nbr_pions)
        la_proposition=tentative1[0]
        print('x'*tentative1[1],'o'*tentative1[2],"tentative:",nb_tentative+1)
        nb_tentative+=1 
    if la_proposition==la_solution:
        print('Bravo')
    else: 
        print('perdu, voici la solution',la_solution)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') 

def joueur1(nbr_pions):
    solution=[]
    for i in range(nbr_pions):
        couleur = int(input("Couleur {} : ".format(i + 1)))
        solution.append(couleur)
    print("\n"*20)
    return solution
    
def parti2joueurs(nbr_pions):
    solution=joueur1(nbr_pions)
    nb_tentative=0
    la_proposition=[]
    while (nb_tentative<10)and(la_proposition!=solution):
        tentative1=tentative2j(solution,nbr_pions)
        la_proposition=tentative1[0]
        print('x'*tentative1[1],'o'*tentative1[2],"tentative:", nb_tentative+1)
        nb_tentative+=1 
    if la_proposition==solution:
        print('Bravo, joueur 2 à gagné')
    else: 
        print('Joueur 1 a gagné',solution)   
        
    
nb_joueur=int(input('Voulez vous jouer à 1(1) ou à 2(2) joueurs?'))
if nb_joueur==1:
    nb_jetons=int(input('Combien de pions voulez vous utiliser?'))
    parti1joueur(nb_jetons)
else:
    nb_jetons=int(input('Combien de pions voulez vous utiliser?'))
    parti2joueurs(nb_jetons)
        