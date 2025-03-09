#Datos de entrada
tareas=[]
contador_id=1 # Variable global para asignar IDs consecutivos

#Datos de Proceso
def agregar_tarea():
    global contador_id  # Permite modificar el contador fuera de la función
    tarea = input("Ingrese la nueva tarea: ")
    tareas.append({"id": contador_id,"tarea":tarea,"completada": False})
    contador_id +=1 # Incrementa el ID automáticamente
    print("Tarea agregada")

def ver_tareas():
    print("\nLista de tareas:")
    for tarea in tareas:
        estado="OK" if tarea["completada"] else "Pendiente"  
        print(f"{tarea["id"]}.{tarea['tarea']}- Estado: {estado}")

def completar_tarea():
    num = int(input("Ingrese el ID de la tarea completada: "))
    for tarea in tareas:
        if tarea["id"]==num:
            tarea["completada"]=True
            print("Tarea marcada como completada")
            return
    print("ID no encontrado.")

def eliminar_tarea():
    num = int(input("Ingrese el ID de la tarea a eliminar: "))
    global tareas
    tareas = [tarea for tarea in tareas if tarea["id"]!=num]
    print("Tarea eliminada.")

#Datos de salida
opcion = 0
while opcion !=5:
    print("\n1. Agregar tarea\n2. Ver tareas\n3. Marcar como completada\n4. Eliminar tarea\n5. Salir")
    opcion = int(input("Elige una opción: "))
    if opcion==1:
       agregar_tarea()
    elif opcion==2:
        ver_tareas()
    elif opcion == 3:
        completar_tarea()
    elif opcion == 4:
        eliminar_tarea()
    elif opcion == 5:
        print("Saliendo del programa...")
    else:
        print("Opción inválida.")        

    
