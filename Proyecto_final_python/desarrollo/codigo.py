import json

def crear_camper():
    camper = {}
    camper["documento"] = int(input("Ingrese el documento del camper: "))

    file = "data/campers.json"

    try:
        with open(file, "r") as campers_file:
            users = json.load(campers_file)
    except json.JSONDecodeError:
        users = []

    for existing_camper in users:
        if existing_camper["documento"] == camper["documento"]:
            print("Lo siento, este camper ya se encuentra en la base de datos.")
            return

    camper["apellidos"] = input("Ingrese los apellidos del estudiante: ")
    camper["nombre"] = input("Ingrese el nombre del estudiante: ")
    camper["direccion"] = input("Ingrese la dirección del estudiante: ")
    camper["no_celular"] = int(input("Ingrese el No. de celular del estudiante: "))
    camper["no_fijo"] = int(input("Ingrese el No. fijo del estudiante: "))
    camper["acudiente"] = input("Ingrese el nombre del acudiente: ")
    camper["estado"] = "Inscrito"
    users.append(camper)

    with open(file, "w") as campers_file:
        json.dump(users, campers_file, indent=4)

    print("¡Enhorabuena!, el camper se ha registrado exitosamente...")

def listar_campers():
    try:
        with open("data/campers.json", "r") as file:
            users = json.load(file)
    except json.JSONDecodeError:
        users = []

    for user in users:
        print("Documento: {}\nNombre: {}\nApellidos: {}\nTeléfono: {}\nAcudiente: {}\nEstado: {}\n{}".format(
            user["documento"],
            user["nombre"],
            user["apellidos"],
            user["no_celular"],
            user["acudiente"],
            user["estado"],
            '-' * 30  
        ))

def registrar_nota_camper():
    with open("data/campers.json", "r+") as campers_file:
        users = json.load(campers_file)
        
        id = int(input("\nIngrese el documento del estudiante del cual desea registrar prueba: "))
        student_found = False

        for user in users:
            if id == user["documento"]:
                student_found = True

                if user["estado"] == "Aprobado":
                    print("\nYa se han registrado resultados de prueba de ingreso para este estudiante.")
                else:
                    print(f"\nUsted ha seleccionado al estudiante {user['nombre']} {user['apellidos']}.")
                    
                    nota_teorica = float(input("Ingrese la nota teórica del estudiante: "))
                    nota_practica = float(input("Ingrese la nota práctica del estudiante: "))
                    n_final = (nota_practica + nota_teorica) / 2

                    if n_final >= 60:
                        user["estado"] = "Aprobado"
                        print(f"El estudiante {user['nombre']} ha sido APROBADO.")
                    else:
                        user["estado"] = "NO aprobado"
                        print(f"El estudiante {user['nombre']} ha sido REPROBADO.")
                break

        if not student_found:
            print("\nCamper no encontrado.")

        campers_file.seek(0)
        json.dump(users, campers_file, indent=4)

def asignar_rutas_campers():

    with open("data/campers.json", "r") as f:
        campers_file = json.load(f)

    with open("data/rutas.json", "r") as f:
        rutas_file = json.load(f)

    # Cargar datos de áreas de entrenamiento desde el archivo JSON
    with open("data/areas_entrenamiento.json", "r") as f:
        areas_entrenamiento = json.load(f)

    # Filtrar campers aprobados
    campers_aprobados = [camper for camper in campers_file if camper["estado"] == "Aprobado"]

    for camper in campers_aprobados:
        id_camper = camper["documento"]

        # Verificar si el ID ya está presente en alguna ruta
        id_presente = any(id_camper in ruta["campers"] for ruta in rutas_file.values())

        if not id_presente:
            id_ruta = None
            for key, ruta in rutas_file.items():
                if len(ruta["campers"]) < 33 and id_camper not in ruta["campers"]:
                    id_ruta = key
                    break

            if id_ruta is not None:
                # Verificar si hay capacidad en el área de entrenamiento
                area_entrenamiento = rutas_file[id_ruta]["area_entrenamiento"]
                if len(areas_entrenamiento[area_entrenamiento]["campers"]) < 33:
                    # Actualizar información de la ruta en el camper
                    camper["id_ruta"] = id_ruta
                    camper["trainer"] = rutas_file[id_ruta]["trainer"]
                    camper["ruta"] = rutas_file[id_ruta]["ruta"]

                    # Agregar el ID del camper a la lista de campers en la ruta
                    rutas_file[id_ruta]["campers"].append(id_camper)

                    # Actualizar el área de entrenamiento del camper
                    areas_entrenamiento[area_entrenamiento]["campers"].append(id_camper)
                    

    with open("data/rutas.json", "w") as f:
        json.dump(rutas_file, f, indent=2)


    with open("data/campers.json", "w") as f:
        json.dump(campers_file, f, indent=2)


    with open("data/areas_entrenamiento.json", "w") as f:
        json.dump(areas_entrenamiento, f, indent=2)

    print("Se han asignado automáticamente las rutas para los campers.")

def visualizar_rutas():

    try:
        with open("data/rutas.json", "r") as file:
            rutas_file = json.load(file)
    except json.JSONDecodeError:

        rutas_file = {}

    for key, ruta in rutas_file.items():
        print(f"\nInformación de la Ruta {key}:\n{'=' * 40}")
        print(f"Nombre de la Ruta: {ruta['ruta']}")
        print(f"Trainer: {ruta['trainer']}")
        print(f"Área de Entrenamiento: {ruta['area_entrenamiento']}\n")

        if ruta["campers"]:
            print("Campers asignados:")
            for camper_id in ruta["campers"]:
                print(f"  - Camper ID {camper_id}")
        else:
            print("No hay campers asignados a esta ruta.")
        
        print('=' * 40)

def cargar_json(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        data = []
    return data

def listar_campers_inscritos():
    

    campers_file = cargar_json("data/campers.json")


    campers_inscritos = [camper for camper in campers_file if camper["estado"] == "Inscrito"]

    if campers_inscritos:
        print("Campers en estado 'Inscrito':")
        for camper in campers_inscritos:
            print(
                f"\nDocumento: {camper['documento']}"
                f"\nNombre: {camper['nombre']}"
                f"\nApellidos: {camper['apellidos']}"
                f"\nTeléfono: {camper['no_celular']}"
                f"\nEstado: {camper['estado']}"
                f"\n{'-' * 30}"
            )
    else:
        print("No hay campers en estado 'Inscrito'.")

def listar_campers_aprobados():

    campers_file = cargar_json("data/campers.json")


    campers_aprobados = [camper for camper in campers_file if camper["estado"] == "Aprobado"]

    if campers_aprobados:
        print("Campers que aprobaron el examen:")
        for camper in campers_aprobados:
            print(
                f"\nDocumento: {camper['documento']}"
                f"\nNombre: {camper['nombre']}"
                f"\nApellidos: {camper['apellidos']}"
                f"\nTeléfono: {camper['no_celular']}"
                f"\nAcudiente: {camper['acudiente']}"
                f"\nEstado: {camper['estado']}"
                f"\n{'-' * 30}"  # Línea separadora
            )
    else:
        print("No hay campers que hayan aprobado el examen.")

def listar_campers_estado_critico():

    campers_file = cargar_json("data/campers.json")


    campers_criticos = [camper for camper in campers_file if camper["estado"] == "NO aprobado"]

    if campers_criticos:
        print("Campers en estado crítico (NO aprobaron el examen):")
        for camper in campers_criticos:
            print(
                f"\nDocumento: {camper['documento']}"
                f"\nNombre: {camper['nombre']} {camper['apellidos']}"
                f"\nTeléfono: {camper['no_celular']}"
                f"\nAcudiente: {camper['acudiente']}"
                f"\nEstado: {camper['estado']}"
                f"\n{'-' * 30}"  # Línea separadora
            )
    else:
        print("No hay campers en estado crítico.")
