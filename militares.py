class AttackBehavior:
    def atacar(self):
        pass

class ataque_armas(AttackBehavior):
    def atacar(self):
        print("En esta estrategia se utilizan armas")

class ataque_flechas(AttackBehavior):
    def atacar(self):
        print("En esta estrategia se utilizan flechas")

class ataque_espadas(AttackBehavior):
    def atacar(self):
        print("En esta estrategia se utilizan espadas")

class Unidad_militar:
    def __init__(self, tipo_ataque : AttackBehavior):
        super().__init__()
        self.ataque = tipo_ataque

    def perform_attack(self):
        self.ataque.atacar()

class soldados(Unidad_militar):
    def __init__(self, tipo_ataque : AttackBehavior):
        super().__init__(tipo_ataque)

class arqueros(Unidad_militar):
    def __init__(self, tipo_ataque : AttackBehavior):
        super().__init__(tipo_ataque)

class caballeros(Unidad_militar):
    def __init__(self, tipo_ataque : AttackBehavior):
        super().__init__(tipo_ataque)

if __name__ == "__main__":
    estrategia = ataque_armas()
    Unidad_militar_jugador= soldados(estrategia)
    Unidad_militar_jugador.perform_attack()
    