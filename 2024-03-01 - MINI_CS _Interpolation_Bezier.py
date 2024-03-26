# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:28:49 2024

@author: Alain ETIENNE, Arts et Métiers - Campus de Metz
"""


import math

def f(a : float, t : float) -> tuple[float]:
    return a*(math.cos(t) + math.sin(t)), a*(math.sin(t)+t*math.cos(t))

def echantillonner(f, nb_point : int) -> list[tuple]:
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
    list[tuple]
        Liste contenant, sous la forme de tuple, l'ensemble des points d'interpolation

    """
    
    # TODO : A compléter, puis retirer l'instruction pass
    result=[(1,0)]
    for t in range (1/nb_point,1+nb_point,1/nb_point):
        result.append(f(1,t)[0],f(1,t)[1])
    return result

        

def determiner_poles(points_interpolation : list[tuple]) -> list[tuple]:
    
    
    
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
    pass

def calculer_points_courbe_Bezier(liste_poles : list[tuple], nb_points : int) -> list[tuple]:
    """
    Fonction qui retourne les coordonnées des points de la courbe de Bezier, construits sur les poles passés en argument

    Parameters
    ----------
    liste_poles : list[tuple]
        Liste contenant, sous la forme de tuple, l'ensemble des poles de la courbe de Bezier
    nb_points : int
        Nombre de points équirépartis de la courbe de Bezier souhaités

    Returns
    -------
    list[tuple]
        DESCRIPTION.

    """   
    # TODO : A compléter, puis retirer l'instruction pass
    pass   

def afficher_courbe(liste_points : list[tuple]) -> None:
    """
    Procédure d'affichage d'une courbe connue de manière discréte (par un ensemble de points)

    Parameters
    ----------
    liste_points : list[tuple]
        Points connus de la fonction (ou courbe) que l'on sohaite afficher

    Returns
    -------
    None
        Aucun retour n'est souhaité, uniquement l'affichage via matplotlib

    """
    # TODO : A compléter, puis retirer l'instruction pass
    pass

def distance(A:list[tuple],B:list[tuple])->list[float]:
    result=[]
    if len(A)=len(B):
        for i in range(len(A)):
            result.append(math.sqrt((A[i][0]-B[i][0])**2+(A[i][1]-B[i][1])**2))
        return result

def afficher_erreur(nb_point_comparaison : int) -> list[float]:
    
    """
    Fonction qui retourne, pour un nombre de points identique et équirépartis dans leurs domaines, l'erreur commise (la distance) entre la courbe de référenc et la courbe d'interpolation de Bezier

    Parameters
    ----------
    nb_point_comparaison : int
        Nombre de points de comparaison.

    Returns
    -------
    list[float]
        Liste contenant les écarts entre les points de la courbe d'origine et de la courbe d'interpolation de Bezier

    """    
    # TODO : A compléter, puis retirer l'instruction pass

    return distance(echantilloner(f,nb_point),calculer_points_courbe_Bezier(determiner_poles(echantilloner(f,nb_point))))

