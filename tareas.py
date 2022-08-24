#se crea una funcion while para poder crear el loop, utilizando la funcion break en caso de escribir "salir"

while(True):
    esc = input('ingrese dato, escriba salir si quiere finalizar: ')
    if(esc=='salir'):
        break
print('Fin')
