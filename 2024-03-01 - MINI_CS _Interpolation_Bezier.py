# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:28:49 2024

@author: Alain ETIENNE, Arts et Métiers - Campus de Metz
"""



import math
import matplotlib.pyplot as plt
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
    for i in range (1,nb_point):
        result.append(f(1,i*pas)) # on fixe ici arbitrairement a à 1 pour coller à la fonction donnée
    return result

# print (echantillonner(f, 20))&

def factorielle(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorielle(n-1)

# print(factorielle (5))
# print(factorielle (0))
        
def coeff_bernstein(i,n,t):
    return (factorielle(n)/(factorielle(i)*factorielle(n-i))*t**i*(1-t)**(n-i))

# print(i_parmis_n(1, 4))
    
def base_bernstein(n:int):
    """calcul la base de bernstein a partir de n le nombre de points"""
    B=[[0 for i in range (n+1)]for j in range (n+1)]
    pas = 1/(n+1)
    for i in range(n+1):
        for j in range (n+1):
            B[i][j]=coeff_bernstein(i, n,j*pas )
    return B

# print (base_bezier(10))
        
def produit_vect_mat(vect,mat):
    L=[]
    for i in range(len(vect)):
        a=0
        for j in range (len(vect)):
            a+=vect[j]*mat[j][i]
        L.append(a)
    return L
    
# print(produit_vect_mat([1,1,1],[[2,3,3],[5,5,5],[6,7,8]]))

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
    B=base_bernstein(len(points_interpolation))
    inv_B=np.linalg.inv(B)
    poles_x=produit_vect_mat([points_interpolation[i][0] for i in range (len(points_interpolation))],inv_B)
    poles_y=produit_vect_mat([points_interpolation[i][1] for i in range (len(points_interpolation))],inv_B)
    poles=[(poles_x[i],poles_y[i]) for i in range (len(poles_x))]
    return poles
    
# print( determiner_poles([(1, 0), (1.0487294296656446, 0.09991668229042665), (1.094837581924854, 0.19933383317463074), (1.1382092104096415, 0.2977537941640056), (1.1787359086363027, 0.3946826463633095), (1.2163163809651676, 0.4896320646821841), (1.2508566957869456, 0.5821211533990214), (1.2822705203028302, 0.6716782569520341), (1.3104793363115357, 0.7578427399098047), (1.3354126364639072, 0.8401667301699348), (1.3570081004945758, 0.9182168195493894), (1.375211750990165, 0.9915757160633873), (1.3899780883047137, 1.0598438423408425), (1.4012702042850953, 1.1226408747929257), (1.4090598745221796, 1.179607218336833), (1.413327628897155, 1.2304054116786998), (1.4140628002466882, 1.2747214583772553), (1.4112635510252747, 1.3122660791425276), (1.4049368778981477, 1.3427758810710815), (1.3950985942532572, 1.366014439780063)]))
    

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
        L[-1]=liste_poles[-1]
        pas =1/n
        for i in range (1,n-1):
            L[i]=(pas*i*liste_poles[i][0]+(1-pas*i)*liste_poles[i-1][0],pas*i*liste_poles[i][1]+(1-pas*i)*liste_poles[i-1][1])
        return calculer_points_courbe_Bezier(L, nb_points)        
    
# print (calculer_points_courbe_Bezier([(0.23744937423310336, -0.02312763376211935), (2.374676800858042, -0.012135345550141174), (-4.909478327719842, -0.23417312643892174), (25.993131521218174, 3.528881838824944), (-82.5136949122766, -16.541358844932518), (231.207116996512, 62.19257431969277), (-517.4226683961233, -171.87693258119498), (971.9090855288468, 383.1454180193432), (-1516.4801032222895, -687.363971182489), (1996.3553787708588, 1019.3445488701182), (-2209.1988880565914, -1249.4087958882592), (2068.9795511084776, 1280.4283017375528), (-1628.876428926469, -1091.388959254713), (1081.9777129650647, 778.8528815501686), (-597.0855337758676, -458.2115887189866), (276.54733098227916, 225.2201684107631), (-102.34935097670109, -87.80284858516802), (33.4063724822621, 30.212683548755194), (-6.562200509075666, -6.145666898120254), (3.2783337984937013, 3.2483400010693018)], 25))

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

    plt.plot([liste_points[i][0] for i in range (len(liste_points))], [liste_points[i][1] for i in range (len(liste_points))], label='Interpolation')
    plt.title("Interpolation par une courbe de Bézier")
    plt.grid(True)
    plt.show()

# afficher_courbe(calculer_points_courbe_Bezier(determiner_poles(echantillonner(f, 20)),100))

def distance(A:list,B:list)->list:
    result=[]
    if len(A)==len(B):
        for i in range(len(A)):
            result.append(math.sqrt((A[i][0]-B[i][0])**2+(A[i][1]-B[i][1])**2))
        return result
    
# print (distance ([(0,0)],[(0,1)]))

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

plt.plot([determiner_poles(echantillonner(f,4))[i][0] for i in range (4)], [determiner_poles(echantillonner(f,4))[i][1] for i in range (4)], label='Interpolation')
plt.plot([calculer_points_courbe_Bezier(determiner_poles(echantillonner(f,4)),6)[i][0] for i in range (6)], [calculer_points_courbe_Bezier(determiner_poles(echantillonner(f,4)),6)[i][1] for i in range (6)], label='Interpolation')
plt.title("Interpolation par une courbe de Bézier")
plt.grid(True)
plt.show()
