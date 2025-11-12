class beneficios():
    def __init__(self, nombreBeneficio, precio):
        self.nombreBeneficio = nombreBeneficio
        self.precio = precio

    def __str__(self):
        return f"{self.nombreBeneficio} precio: {self.precio} $ coins"


class cambiarFecha(beneficios):
    def __init__(self, nombreBeneficio="cambiar fecha", precio=50):
        super().__init__(nombreBeneficio, precio)
        self.descripcion = "Pospones la fecha de entrega de un trabajo pagando coins"


class puntosExtra(beneficios):
    def __init__(self, nombreBeneficio="Puntos Extra para evaluaciones", precio=30):
        super().__init__(nombreBeneficio, precio)
        self.descripcion = "puntos adicionales por puntos, no mucho."


class tutorias(beneficios):
    def __init__(self, nombreBeneficio="tutoria", precio=40):
        super().__init__(nombreBeneficio, precio)
        self.descripcion = "una tutoria personalizada con el profe"


class excusaAusencia(beneficios):
    def __init__(self, nombreBeneficio="justificar falta", precio=25):
        super().__init__(nombreBeneficio, precio)
        self.descripcion = "si faltaste a tutoria por ejemplo, no se cobraria tu falta."


class reentrega(beneficios):
    def __init__(self, nombreBeneficio="reentregar actividad", precio=35):
        super().__init__(nombreBeneficio, precio)
        self.descripcion = "podes reentregar uan actividad"


class saltoTema(beneficios):
    def __init__(self, nombreBeneficio="ignorar un tema que no se", precio=60):
        super().__init__(nombreBeneficio, precio)
        self.descripcion = "si no sabes un tema lo podes remplazar por puntos"


class materialExtra(beneficios):
    def __init__(self, nombreBeneficio="material de estudio", precio=20):
        super().__init__(nombreBeneficio, precio)
        self.descripcion = "material adicional a cambio de coins"