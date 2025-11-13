from beneficios import beneficios, cambiarFecha, puntosExtra, tutorias, excusaAusencia, reentrega, saltoTema, materialExtra
from usuario import profesor, estudiante
from tareas import trabajoPractico

print("STEFY COINS")

profesor1 = profesor(
    id=1,
    nombre="Juan",
    apellido="Perez",
    edad=40,
    especialidad="Matematica",
    correo="t4yl0r.4l1s0n.sw1ft.shake.it.off@gmail.com",  
    password="obxs caxi bqco dviq"     
)


estudiante1 = estudiante(
    nombre="Stefi",
    apellido="Lopez",
    edad=22,
    legajo=1234,
    curso="4to A",
    correo="t4yl0r.4l1s0n.sw1ft.shake.it.off@gmail.com",  
    password="obxs caxi bqco dviq",
    id=1,
    coins=100  
)

profesor1.estudiante.append(estudiante1)


print("Tarea enviada")

tarea1 = trabajoPractico(
    consigna="Resolver ejercicios de álgebra lineal",
    fechaEntrega="20/11/2025",
    criterioEvaluacion="Todos los ejercicios correctos"
)

tarea2 = trabajoPractico(
    consigna="Proyecto final de programación",
    fechaEntrega="25/11/2025",
    criterioEvaluacion="Código funcional y documentado"
)


profesor1.asignarTarea(estudiante1, tarea1)
profesor1.asignarTarea(estudiante1, tarea2)


print("visualizacion de tarea")
estudiante1.checkearTareas()


print("estudiante entrega tarea")
estudiante1.entregarTarea(tarea1)

estudiante1.checkearTareas()

print("aprobacion de tarea")
profesor1.aprobarTarea(estudiante1, tarea1)

estudiante1.checkearTareas()


print("beneficios disponibles")

beneficios_disponibles = [
    cambiarFecha(),
    puntosExtra(),
    tutorias(),
    excusaAusencia(),
    reentrega(),
    saltoTema(),
    materialExtra()
]

estudiante1.verBeneficiosDisponibles(beneficios_disponibles)


print("estudiante compra beneficios")


tutoria = tutorias()
estudiante1.canjearBeneficio(tutoria, profesor1)


puntos = puntosExtra()
estudiante1.canjearBeneficio(puntos, profesor1)

salto = saltoTema()
estudiante1.canjearBeneficio(salto, profesor1)

print("profesor mira como el estudiante cnajea el beneficio")
profesor1.visualizarBeneficios(estudiante1)

estudiante1.checkearTareas()
print("Fin de la prueba")


