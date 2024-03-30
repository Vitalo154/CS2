# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:28:49 2024

@author: Alain ETIENNE, Arts et Métiers - Campus de Metz
"""



import math
import matplotlib as plt
import numpy as np

def f(a : float, t : float) -> tuple:
    return a*(math.cos(t) + math.sin(t)), a*(math.sin(t)+t*math.cos(t))

def echantillonner(f, nb_point : int) -> list:
    """
    Fonction qui retourne l'ensemble de points d'interpolation, construit sur la fonction f passée en argument

    Parameters
    ----------
    f : Pointeur de fonction
        Fonction que l'on souhaiter interpoler
    nb_point : int
        Nombre de points d'interpolation

    Returns
    -------
    list
        Liste contenant, sous la forme de tuple, l'ensemble des points d'interpolation

    """
    
    # TODO : A compléter, puis retirer l'instruction pass
    result=[(1,0)]
    pas=1/nb_point
    for t in range (1/nb_point,1+nb_point,1/nb_point):
        result.append(f(1,t))
        t+=pas
    return result

def factorielle(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorielle(n-1)
        
def i_parmis_n(i,n):
    return (factorielle(n)/(factorielle(i)*factorielle(n-i)))
    
def base_bezier(n:int):
    """calcul la base de bezier a partir de n le nombre de points"""
    B=[[0 for i in range (n)]for j in range (n)]
    pas = 1/n
    for i in range(n+1):
        for j in range (n+1):
            B[i][j]=i_parmis_n(j,n)*(i*pas)**j*(1-i*pas)**(n-j)
    return B
        
def produit_vect_mat(mat,vect):
    L=[]
    for i in range(len(vect)):
        a=0
        for j in range (len(vect)):
            a+=vect[j]*mat[j][i]
        L.append(a)
    return L
    
def determiner_poles(points_interpolation : list) -> list:
    """
    Fonction qui calcule, puis de retourne les pôles de la courbe de Bézier en fonction d'une liste de points d'interpolation

    Parameters
    ----------
    points_interpolation : list
        Liste contenant les positions (sous forme de tuple) des points d'interpolation

    Returns
    -------
    list
        Liste contenant les positions (sous forme de tuple) des poles de la courbe de Bezier

    """
    # TODO : A compléter, puis retirer l'instruction pass
    B=base_bezier(len(points_interpolation))
    inv_B=np.linalg.inv(B)
    poles_x=produit_vect_mat([points_interpolation[i][0] for i in range (len(points_interpolation))],inv_B)
    poles_y=produit_vect_mat([points_interpolation[i][1] for i in range (len(points_interpolation))],inv_B)
    poles=[(poles_x[i],poles_y[i]) for i in range (len(poles_x))]
    return poles
    
    
    

def calculer_points_courbe_Bezier(liste_poles : list, nb_points : int) -> list:
    """
    Fonction qui retourne les coordonnées des points de la courbe de Bezier, construits sur les poles passés en argument

    Parameters
    ----------
    liste_poles : list
        Liste contenant, sous la forme de tuple, l'ensemble des poles de la courbe de Bezier
    nb_points : int
        Nombre de points équirépartis de la courbe de Bezier souhaités

    Returns
    -------
    list
        DESCRIPTION.

    """   
    # TODO : A compléter, puis retirer l'instruction pass
    if len(liste_poles)>=nb_points:
        return liste_poles
    else:
        n=len(liste_poles)+1
        L=[0 for i in range (n)]
        L[0]=liste_poles[0]
        pas =1/n
        for i in range (1,n):
            L[i]=pas*i*liste_poles[i]+(1-pas*i)*liste_poles[i-1]
        L.append(liste_poles[-1])
        return calculer_points_courbe_Bezier(L, nb_points)        
    
    

def afficher_courbe(liste_points : list) -> None:
    """
    Procédure d'affichage d'une courbe connue de manière discréte (par un ensemble de points)

    Parameters
    ----------
    liste_points : list
        Points connus de la fonction (ou courbe) que l'on sohaite afficher

    Returns
    -------
    None
        Aucun retour n'est souhaité, uniquement l'affichage via matplotlib

    """
    # TODO : A compléter, puis retirer l'instruction pass

    plt.plot((liste_points[i][0] for i in range (len(liste_points))), (liste_points[i][1] for i in range (len(liste_points))), label='Interpolation')
    plt.title("Interpolation par une courbe de Bézier")
    plt.grid(True)
    plt.show()


def distance(A:list,B:list)->list:
    result=[]
    if len(A)==len(B):
        for i in range(len(A)):
            result.append(math.sqrt((A[i][0]-B[i][0])**2+(A[i][1]-B[i][1])**2))
        return result

def afficher_erreur(nb_point_comparaison : int) -> list:
    
    """
    Fonction qui retourne, pour un nombre de points identique et équirépartis dans leurs domaines, l'erreur commise (la distance) entre la courbe de référenc et la courbe d'interpolation de Bezier

    Parameters
    ----------
    nb_point_comparaison : int
        Nombre de points de comparaison.

    Returns
    -------
    list[]
        Liste contenant les écarts entre les points de la courbe d'origine et de la courbe d'interpolation de Bezier

    """    
    # TODO : A compléter, puis retirer l'instruction pass

    return distance(echantillonner(f,nb_point_comparaison),calculer_points_courbe_Bezier(determiner_poles(echantillonner(f,nb_point_comparaison))))
