# se crea una funcion while para poder crear el loop
while(True):
    esc = input('ingrese dato, escriba salir si quiere finalizar: ')  
    # si la entrada es "salir" se usa el comando break para salir del loop
    if(esc=='salir'):
        break
print('Fin')
