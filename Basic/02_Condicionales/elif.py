ingreso_mensual = 73000
gasto_mensual = 3000

#if anidados y else if (elif)

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Estas bien pa")
    else:
        print("Estas gastando como lima nueva mano")
elif ingreso_mensual > 1000: 
    print("Estas bien en Argentina")
elif ingreso_mensual > 500:
    print("Estas bien en Venezuela")
else:
    print("Sos pobre")

