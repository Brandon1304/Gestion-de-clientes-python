import os

#Tabla hash para asociar clientes con sus archivos
clientes = {}

#Carpeta donde se guardarán los archivos
CARPETA_CLIENTES = "clientes"

#Crear carpeta si no existe
if not os.path.exists(CARPETA_CLIENTES):
    os.makedirs(CARPETA_CLIENTES)


def nombre_archivo(nombre):
    return nombre.replace(" ", "_") + ".txt"


def crear_cliente():
    nombre = input("Nombre del cliente: ")

    if nombre in clientes:
        print("⚠️ El cliente ya existe.")
        return

    servicio = input("Descripción del servicio solicitado: ")
    archivo = nombre_archivo(nombre)
    ruta = os.path.join(CARPETA_CLIENTES, archivo)

    with open(ruta, "w", encoding="utf-8") as f:
        f.write(f"Cliente: {nombre}\n")
        f.write("Servicios:\n")
        f.write(f"- {servicio}\n")

    clientes[nombre] = archivo
    print(f"✅ Cliente '{nombre}' creado correctamente.")


def consultar_cliente():
    nombre = input("Nombre del cliente a consultar: ")

    if nombre not in clientes:
        print("❌ Cliente no encontrado.")
        return

    ruta = os.path.join(CARPETA_CLIENTES, clientes[nombre])

    with open(ruta, "r", encoding="utf-8") as f:
        print("\n📄 Información del cliente:")
        print(f.read())


def actualizar_cliente():
    nombre = input("Nombre del cliente a actualizar: ")

    if nombre not in clientes:
        print("❌ Cliente no encontrado.")
        return

    nuevo_servicio = input("Nueva descripción del servicio: ")
    ruta = os.path.join(CARPETA_CLIENTES, clientes[nombre])

    with open(ruta, "a", encoding="utf-8") as f:
        f.write(f"- {nuevo_servicio}\n")

    print(f"🔄 Cliente '{nombre}' actualizado correctamente.")


def eliminar_cliente():
    nombre = input("Nombre del cliente a eliminar: ")

    if nombre not in clientes:
        print("❌ Cliente no encontrado.")
        return

    ruta = os.path.join(CARPETA_CLIENTES, clientes[nombre])
    os.remove(ruta)
    del clientes[nombre]

    print(f"🗑️ Cliente '{nombre}' eliminado correctamente.")


def listar_clientes():
    if not clientes:
        print("📭 No hay clientes registrados.")
        return

    print("\n📋 Lista de clientes:")
    for cliente in clientes:
        print(f"- {cliente}")


def cargar_clientes():
    for archivo in os.listdir(CARPETA_CLIENTES):
        if archivo.endswith(".txt"):
            nombre = archivo.replace("_", " ").replace(".txt", "")
            clientes[nombre] = archivo


def menu():
    cargar_clientes()

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Crear nuevo cliente")
        print("2. Consultar cliente")
        print("3. Actualizar cliente")
        print("4. Eliminar cliente")
        print("5. Listar clientes")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_cliente()
        elif opcion == "2":
            consultar_cliente()
        elif opcion == "3":
            actualizar_cliente()
        elif opcion == "4":
            eliminar_cliente()
        elif opcion == "5":
            listar_clientes()
        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción no válida.")



# Ejecutar programa final
menu()


