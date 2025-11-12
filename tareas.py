class Tarea():
    def __init__(self,valor,descripcion,consigna,fechaEntrega,criterioEvaluacion, coin_otorga=10):
        self.valor = valor
        self.descripcion = descripcion
        self.consigna=consigna
        self.fechaEntrega=fechaEntrega
        self.criterioEvaluacion=criterioEvaluacion
        self.entrega=False
        self.aprobado=False
        self.coin_otorga = coin_otorga

    def cambiarEstado(self, nuevo_estado):
        self.estado = nuevo_estado

    def __str__(self):
        return f"{self.titulo} - {self.estado}"

class trabajoPractico(Tarea):
    def __init__(self,consigna,fechaEntrega,criterioEvaluacion):
        descripcion = "un trabajo practico"
        valor = 200
        super().__init__(valor,descripcion,consigna,fechaEntrega,criterioEvaluacion)
        
class proyectoExtra(Tarea):
        def __init__(self,consigna,fechaEntrega,criterioEvaluacion):
            descripcion = "proyectos extra"
            valor = 1000
            super().__init__(valor,descripcion,consigna,fechaEntrega,criterioEvaluacion)