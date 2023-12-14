from random import randint

def detecte_obstacle(choix_joueur,lst_obstacle,coordonnée : tuple) :
    pas_obstacle=True
    for i in range(len(choix_joueur["Joueur1"])) :
        if coordonnée== ((choix_joueur["Joueur1"][i].rect.x,choix_joueur["Joueur1"][i].rect.y)) :
            pas_obstacle=False
        elif coordonnée== ((choix_joueur["Joueur2"][i].rect.x,choix_joueur["Joueur2"][i].rect.y)) :
            pas_obstacle=False
    for i in range (len(lst_obstacle)) :
        if coordonnée==lst_obstacle[i] :
            pas_obstacle=False
    return pas_obstacle

def detecte_obstacle2(choix_joueur,coordonnée : tuple) :
    pas_obstacle=True
    for i in range(len(choix_joueur["Joueur1"])) :
        if coordonnée== ((choix_joueur["Joueur1"][i].rect.x,choix_joueur["Joueur1"][i].rect.y)) :
            pas_obstacle=False
        elif coordonnée== ((choix_joueur["Joueur2"][i].rect.x,choix_joueur["Joueur2"][i].rect.y)) :
            pas_obstacle=False
    return pas_obstacle


def create_obstacle(choix_joueur) :
    obstacle_aléatoire= [0,0]
    lst_coordonnée_possible_x=[(100+i*60) for i in range (10)]
    lst_coordonnée_possible_y=[(100+i*60) for i in range (10)]
    trouver_place_obstacle=True

    while trouver_place_obstacle :
        essaie=(lst_coordonnée_possible_x[randint(0,9)],lst_coordonnée_possible_x[randint(0,9)])
        if detecte_obstacle2(choix_joueur,essaie) :
            trouver_place_obstacle=False
    return essaie

def supprimer_élement(choix_joueur,joueur,coordonnée) : 
    for i in range (len(choix_joueur[joueur])) :
        if choix_joueur[joueur][i]==coordonnée :
            choix_joueur[joueur].pop(i)           
    return choix_joueur

def search_element(choix_joueur,coordonnée) :
    for i in range(len(choix_joueur["Joueur1"])) :
        if (choix_joueur["Joueur1"][i].rect.x,choix_joueur["Joueur1"][i].rect.y)==coordonnée :
            return i,"Joueur1"
        elif (choix_joueur["Joueur2"][i].rect.x,choix_joueur["Joueur2"][i].rect.y)==coordonnée :
            return i,"Joueur2"
    return None 

#verifie dans quele carré le joueur clique
def search_coordinate(coordonate) :
    possible_coordonate_x=[(100+i*60) for i in range (10)]
    possible_coordonate_y=[(100+i*60) for i in range (10)]
    if coordonate[0]<40 or coordonate[0]>700 or coordonate[1]<40 or coordonate[1]>700 :
        return None
    else :
        for i in range (len(possible_coordonate_x)) :
            for j in range (len(possible_coordonate_y)) :
                if (coordonate[0]>=possible_coordonate_x[j] and coordonate[0]< possible_coordonate_x[j]+60) and (coordonate[1]>=possible_coordonate_x[i] and coordonate[1]< possible_coordonate_x[i]+60) :
                    return (possible_coordonate_x[j],possible_coordonate_y[i])
                
def valeur_absolue(a : int) :
    if a>0 :
        return a
    else :
        return -a

#utilisation des vecteurs pour savoir si l'unité est en mesure de se déplacer sur la case souhaitée : Xb - Xa)/60 pour l'abcisse 
# (Yb-Ya)/60 pour l'ordonnée, la somme de la valeur absolue des deux  sont le nombre totale de case déplacépour connaitre le nombre totale 
# de case déplacé, on divise par 60 car un carré fais, 60 pixels sur 60 pixels                   
def compte_case(coordonnée_base,transform) :
    x_total=(transform[0]- coordonnée_base[0])/60
    y_totlal=(transform[1]- coordonnée_base[1])/60
    return (valeur_absolue(x_total)+valeur_absolue(y_totlal))

def déplacemet_total(coordonnée_base,transform) :
    x_total=(transform[0]- coordonnée_base[0])/60
    y_totlal=(transform[1]- coordonnée_base[1])/60
    return (x_total,y_totlal)

def modificate_place(elem_graphique,deplacement) :
    if ((elem_graphique.rect.x + deplacement[0]*60) >=100) and ((elem_graphique.rect.x + deplacement[0]*60) <=640) and ((elem_graphique.rect.y + deplacement[0]*60) <=640) and ((elem_graphique.rect.x + deplacement[0]*60) >=100) : 
        elem_graphique.rect.x+=deplacement[0]*60 
        elem_graphique.rect.y+=deplacement[1]*60
    return elem_graphique

def search_coordinate2(coordonate) :
    possible_coordonate_x=[(i*60) for i in range (10)]
    possible_coordonate_y=[(i*60) for i in range (10)]
    if coordonate[0]<0 or coordonate[0]>540 or coordonate[1]<0 or coordonate[1]>540 :
        return None
    else :
        for i in range (len(possible_coordonate_x)) :
            for j in range (len(possible_coordonate_y)) :
                if (coordonate[0]>=possible_coordonate_x[j] and coordonate[0]< possible_coordonate_x[j]+60) and (coordonate[1]>=possible_coordonate_x[i] and coordonate[1]< possible_coordonate_x[i]+60) :
                    return (possible_coordonate_x[j],possible_coordonate_y[i])
                
def modificate_list_position(lst_position,coordonate_base,coordonate_want) :
    lst_modificate=[]
    for i in range (len(lst_position)) :
        if lst_position[i]==coordonate_base :
            lst_modificate.append(coordonate_want)
        else :
            lst_modificate.append(lst_position[i])
    return lst_modificate

