def déplacemet_total(coordonnée_base ,transform ) :
    x_total=(transform[0]- coordonnée_base[0])/60
    y_totlal=(transform[1]- coordonnée_base[1])/60
    return (x_total,y_totlal)

print(déplacemet_total((340,640),(160,160)))