from estructura.utilidades import limpiar_pantalla
from estructura.menus import menu_campers, menu_matriculas, menu_principal, menu_reportes
from desarrollo.codigo import crear_camper, listar_campers,registrar_nota_camper, asignar_rutas_campers, visualizar_rutas,listar_campers_inscritos,listar_campers_aprobados,listar_campers_estado_critico

def campers():
    limpiar_pantalla()
    op = menu_campers()
    if op==1:
        crear_camper()
    if op==2:
        listar_campers()
    if op==3:
        registrar_nota_camper()

def matriculas():
    limpiar_pantalla()
    op = menu_matriculas()
    if op==1:
        asignar_rutas_campers()
    if op==3:
        visualizar_rutas()

def reportes():
    limpiar_pantalla()
    op = menu_reportes()
    if op==1:
        listar_campers_inscritos()
    if op==2:
        listar_campers_aprobados()
    if op==4:
        listar_campers_estado_critico()


while True:
    
    #limpiar_pantalla()
    op=menu_principal()
    if  op==1:
       campers()
    if  op==2:
        matriculas()
    if  op==3:
        reportes()
    elif op==4:
       print("Saliendo")
       break
       