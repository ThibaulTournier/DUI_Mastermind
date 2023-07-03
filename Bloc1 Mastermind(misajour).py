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

def demander_entier():
    while True:
        try:
            entier = int(input())
            if 0 <= entier <= 7:
                return entier
            else:
                print("La valeur doit être comprise entre 0 et 7.")
        except ValueError:
            print("Veuillez saisir un entier valide.")

# Utilisation de la fonction


def tentative(solution, nbr_pions):
    print("Quelles couleurs proposez-vous ? (une couleur est un chiffre entre 0 et 7)")
    l=[]
    for i in range(nbr_pions):
        couleur = demander_entier()
        l.append(couleur)

    a = nb_couleurs_mal_placees(l, solution)
    b = nb_bien_places(l, solution)
    return l, a, b


def tentative2j(solution,nbr_pions):
    print('Joueurs 2, quelles couleurs proposez vous?(une couleur est un chiffre entre 0 et 7)')
    l=[]
    for i in range(nbr_pions):
        l.append(demander_entier())
    
    a=nb_couleurs_mal_placees(l,solution)
    b=nb_bien_places(l,solution)
    return l,a,b



def parti1joueur(nbr_pions):
    la_solution=generate_solution(nbr_pions)
    liste_des_reponses=[]
    liste_des_pions=[]
    nb_tentative=0
    la_proposition=[]
    
    while (nb_tentative<10)and(la_proposition!=la_solution):
        tentative1=tentative(la_solution,nbr_pions)
        la_proposition=tentative1[0]
        liste_des_reponses.append(la_proposition)
        liste_des_pions.append([tentative1[1],tentative1[2]])
        
        for i in range(len(liste_des_reponses)):
            for j in range(nbr_pions):
                print(liste_des_reponses[i][j],"|",end=" ")
            print("     ", 'x'*int(liste_des_pions[i][0]),'o'*int(liste_des_pions[i][1]))
        print("tentative ",nb_tentative+1) 
        if tentative1[1]+tentative1[2]==0:
            print('Rien ')
        nb_tentative+=1 
    if la_proposition==la_solution:
        print('Bravo')
    else: 
        print('perdu, voici la solution',la_solution)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') 

def joueur1(nbr_pions):
    solution=[]
    print('Entrez',nbr_pions,'chiffres entre 0 et 7')
    for i in range(nbr_pions):
        
        couleur = demander_entier()
        solution.append(couleur)
    print("\n"*20)
    return solution
    
def parti2joueurs(nbr_pions):
    solution=joueur1(nbr_pions)
    liste_des_reponses=[]
    liste_des_pions=[]
    nb_tentative=0
    la_proposition=[]
    while (nb_tentative<10)and(la_proposition!=solution):
        tentative1=tentative2j(solution,nbr_pions)
        la_proposition=tentative1[0]
        liste_des_reponses.append(la_proposition)
        liste_des_pions.append([tentative1[1],tentative1[2]])
        for i in range(len(liste_des_reponses)):
            for j in range(nbr_pions):
                print(liste_des_reponses[i][j],"|",end=" ")
            print("     ", 'x'*int(liste_des_pions[i][0]),'o'*int(liste_des_pions[i][1]))
        print("tentative ",nb_tentative+1) 
        if tentative1[1]+tentative1[2]==0:
            print('Rien ')
        nb_tentative+=1 
    print("tentative ",nb_tentative+1) 
    if tentative1[1]+tentative1[2]==0:
        print('Rien ')
    nb_tentative+=1 
    if la_proposition==solution:
        print('Bravo , joueur 2 a gagné')
    else: 
        print('Joueur 1 a gagné',solution)
def nb_couleur(liste,couleur):
    n=0
    for i in range(len(liste)):
        if liste[i]==couleur:
            n+=1
    return n




def bien_place(proposition,solution):
    nb_etoile=[]
    solution1=[]
    proposition1=[]
    for i in range(len(proposition)):
        if proposition[i]==solution[i]: 
            nb_etoile.append(0)  
        else:
            solution1.append(solution[i])
            proposition1.append(proposition[i])
            if proposition[i] in solution:
                
                nb_etoile.append(1)
            else:
                nb_etoile.append(-1)
            
    return nb_etoile, proposition1, solution1


def deux_liste_dist(l1,l2):
    nb_etoile=[]
    solution=[]
    for i in range(len(l1)):
        if l1[i] in l2:
            k=l2.index(l1[i])
            nb_etoile.append(min_int(nb_couleur(l1,l1[i]),nb_couleur(l2,l2[k])))
            
        else:
            nb_etoile.append(0)
    y=1
    for i in range(len(l1)):
        p=l1.index(l1[i])
        if (l1[i]==l1[p]):
            if i>p:
                nb_etoile[i]=nb_etoile[i]-y
                y+=1
    for i in range(len(nb_etoile)):
        if nb_etoile[i]>0:
            solution.append(1)
        else:
            solution.append(0)
    return solution

  
def parti_facile1j(proposition,solution):
    sol=[]
    
    j=bien_place(proposition,solution)
    k=deux_liste_dist(j[1],j[2])
    q=0
    for i in range(len(solution)):  
        if j[0][i]==0:
            sol.append('o')
        elif j[0][i]==-1:
            sol.append('_')
        else:
            sol.append('s')
    for i in range(len(sol)):
        if sol[i]=='s':
            if k[q]==1:
                sol[i]='*'
            else:
                sol[i]='_'
            q+=1
        elif sol[i]=='_':
            q+=1
                
            
    return sol

def parti_facile_1joueur(nbr_pions):
    liste_des_reponses=[]
    liste_des_pions=[]
    la_solution=generate_solution(nbr_pions)
    nb_tentative=0
    la_proposition=[]
    while (nb_tentative<10)and(la_proposition!=la_solution):
        tentative1=tentative(la_solution,nbr_pions)
        la_proposition=tentative1[0]
        liste_des_reponses.append(la_proposition)
        liste_des_pions.append(parti_facile1j(la_proposition,la_solution))
        for i in range(len(liste_des_reponses)):
            for j in range(nbr_pions):
                print(liste_des_reponses[i][j],"|",end=" ")   
            print('     ',end=" ")
            for j in range(nbr_pions):
                print(liste_des_pions[i][j],"|",end=" ")
            print(' ')
        print("tentative ",nb_tentative+1) 
        if tentative1[1]+tentative1[2]==0:
            print('Rien ')
        nb_tentative+=1 
    if la_proposition==la_solution:
        print('Bravo')
    else: 
        print('perdu, voici la solution',la_solution)
        

def  parti_facile_2joueur(nbr_pions):
    liste_des_reponses=[]
    liste_des_pions=[]
    la_solution=joueur1(nbr_pions)
    nb_tentative=0
    la_proposition=[]
    while (nb_tentative<10)and(la_proposition!=la_solution):
        tentative1=tentative(la_solution,nbr_pions)
        la_proposition=tentative1[0]
        liste_des_reponses.append(la_proposition)
        liste_des_pions.append(parti_facile1j(la_proposition,la_solution))
        for i in range(len(liste_des_reponses)):
            for j in range(nbr_pions):
                print(liste_des_reponses[i][j],"|",end=" ")   
            print('     ',end=" ")
            for j in range(nbr_pions):
                print(liste_des_pions[i][j],"|",end=" ")
            print(' ')
        print("tentative ",nb_tentative+1) 
        if tentative1[1]+tentative1[2]==0:
            print('Rien ')
        nb_tentative+=1 
    if la_proposition==la_solution:
        print('Bravo , joueur 2 a gagné')
    else: 
        print('perdu, voici la solution',la_solution)


def nbr_joueur():
    while True:
        try: 
            nb_joueur=int(input('Voulez vous jouer à 1 ou à 2 joueurs?'))
            if 1<=nb_joueur<=2:
                return nb_joueur
            else: 
                print("Veuillez saisir 1 ou 2")
        except ValueError:
            print("Veuillez saisir un entier valide.")            

             
def nbr_jetons():
    while True:
        try: 
            nb_jeton=int(input('Avec combien de jetons souhaitez vous jouer? Saisir un entier entre 0 et 7'))
            if 0<=nb_jeton<=7:
                return nb_jeton
            else: 
                print("Veuillez saisir un entier entre 0 et 7")   
        except ValueError:
            print("Veuillez saisir un entier valide.") 
                
def partif():
    while True:
        try: 
            question=input('Voulez vous jouer une partie facile?')
            if (question=='oui')or (question=='non'):
                return question
            else: 
                print("Veuillez répondre par oui ou non") 
        except ValueError:
            print("Veuillez saisir un entier valide.") 
joueur=nbr_joueur()
jetons=nbr_jetons()
facile=partif()
if joueur==1:
    if facile=='oui':
        parti_facile_1joueur(jetons)
    else:
        parti1joueur(jetons)
else:
    if facile=='oui':
        parti_facile_2joueur(jetons)
    else:
        parti2joueurs(jetons)
