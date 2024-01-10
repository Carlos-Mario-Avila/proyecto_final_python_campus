from estructura.utilidades import validar_opcion

def menu_principal():
    print("====================================")
    print("           Menú Principal           ")
    print("====================================")
    print("1. Campers")
    print("2. Matriculas")
    print("3. Reportes")
    print("4. Salir")
    print("====================================")
    op = validar_opcion("Selecciona una opción: ", 1, 4)
    return op

def menu_campers():
    print("====================================")
    print("          Menú de Campers           ")
    print("====================================")
    print("1. Crear Campers")
    print("2. Listar Campers")
    print("3. Registrar Notas de Camper")
    print("4. Nota de Módulos")
    print("5. Salir")
    print("====================================")
    op = validar_opcion("Selecciona una opción: ", 1, 5)
    return op

def menu_matriculas():
    print("====================================")
    print("         Menú de Matrículas          ")
    print("====================================")
    print("1. Asignación de Rutas a Campers")
    print("2. Editar Ruta de Camper")
    print("3. Ver Matrículas")
    print("4. Salir")
    print("====================================")
    op = validar_opcion("Selecciona una opción: ", 1, 4)
    return op

def menu_reportes():
    print("==========================================================")
    print("                      Menú de Reportes                    ")
    print("==========================================================")
    print("1. Listar Campers en Estado Inscrito")
    print("2. Listar Campers que Aprobaron Examen")
    print("3. Listar Trainers Trabajando en el Campus")
    print("4. Listar Campers en Estado Crítico")
    print("5. Listar Campers y Trainers Asociados a una Ruta")
    print("6. Listar Campers Aprobados y No Aprobados por Módulos")
    print("7. Salir")
    print("==========================================================")
    op = validar_opcion("Selecciona una opción: ", 1, 7)
    return op
