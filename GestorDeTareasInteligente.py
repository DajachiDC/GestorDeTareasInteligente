tareas = []

print("\n-----------------------")
print("Creado por: Dajachi")
print("\nRedes:\n")
print("YouTube: https://www.youtube.com/@Dajachi")
print("Twitter: https://twitter.com/Dajachi_?t=bdLmG03jQZQPYeqAwXXYIA&s=09")
print("Tik Tok: https://tiktok.com/@dajachi_?t=8l5UUUjLBvZ&_r=1")
print("GitHub: https://github.com/DajachiDC")
print("Blog: https://dajachicode.blogspot.com")
print("\n¡Gracias por utilizar el programa!")
print("-------------------------")

while True:
    print("\n*** Bienvenido al Gestor de Tareas Inteligente ***")
    print("\n1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
            nota = input("\nNota de la tarea: ")
            categoria = input("Ingrese la categoria de la tarea: ")
            fecha = input("Ingrese la fecha límite de la tarea (Formato: dd/mm/aaaa): ")
            nota = {'Nota': nota, 'Categoria': categoria, 'Fecha': fecha}
            tareas.append(nota)
            print("\nTarea agregada con éxito.")
        
    elif opcion == "2":
        if tareas:
            print("\nLista de tareas:")
            for i, tarea in enumerate(tareas, 1):
                print(f"\nTarea: {i}")
                print(f"Nota: {tarea['Nota']}")
                print(f"Categoría: {tarea['Categoria']}")
                print(f"Fecha límite: {tarea['Fecha']}")
        
        else:
            print("\nNo hay tareas para mostrar.")
        
    elif opcion == "3":
        if tareas:
            print("\nLista de tareas:")
            for i, tarea in enumerate(tareas, 1):
                print(f"{i}. {tarea['Nota']} - Categoría: {tarea['Categoria']} - Fecha límite: {tarea['Fecha']}")
            indice = int(input("\nIngrese el número de la tarea que desea eliminar: ")) - 1
            try:
                del tareas[indice]
                print("\nTarea eliminada con éxito.")
            except IndexError:
                print("\nEl índice de la tarea no es válido.")
        else:
            print("\nNo hay tareas para eliminar.")
    
    elif opcion == "4":
        print("\nGracias por utilizar el programa!!")
        break
