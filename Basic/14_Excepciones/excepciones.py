def sum_dos():
    while True:
        num_uno = input("Numero 1: ")
        num_dos = input("Numero 2: ")
        try:
            resultado = int(num_uno) + int(num_dos)
        except Exception as e:
            print("Necesito que me des dos numeros, no valores distintos a numeros.")
            print(f"ERROR: {e}")
        else:
            break
        finally:
            print("Manejo de excepcion finalizado")
            
    """
    Si se ejecuta correctamente el try, se ejecutará el else, si se ejecuta el except, 
    el else no se ejecutará. Pero en cualquier caso, el finally se ejecutrá 
    """ 
       
    return resultado

print(sum_dos())