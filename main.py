# Breve descripción del sistema:
# Este sistema modela personajes de un videojuego RPG utilizando POO.
# Se implementa encapsulamiento para proteger la salud (vida) del personaje,
# previniendo valores irreales (como vida negativa). Además, se utiliza herencia
# para crear la clase 'Mago', la cual introduce la mecánica de 'Maná' y sobrescribe
# el comportamiento de curación, demostrando el polimorfismo.

# Creación de la clase base
class PersonajeRPG:
    def __init__(self, nombre, clase_personaje, nivel, vida_maxima, dano_base):
        self.nombre = nombre
        self.clase_personaje = clase_personaje
        self.nivel = nivel
        self.vida_maxima = vida_maxima
        self.dano_base = dano_base
        
        # Aplicación de Encapsulamiento
        # Se usa doble guion bajo (__) para hacer el atributo privado.
        self.__vida_actual = vida_maxima 

    # Aplicación de Encapsulamiento (Getter)
    @property
    def vida_actual(self):
        """Permite consultar la vida de forma segura."""
        return self.__vida_actual

    # Aplicación de Encapsulamiento (Setter)
    @vida_actual.setter
    def vida_actual(self, valor):
        """Valida las modificaciones a la vida para que no haya errores lógicos."""
        if valor < 0:
            self.__vida_actual = 0
            print(f" Seguridad: La vida de {self.nombre} no puede ser negativa. Ajustada a 0.")
        elif valor > self.vida_maxima:
            self.__vida_actual = self.vida_maxima
            print(f" Seguridad: La vida de {self.nombre} no puede exceder el máximo ({self.vida_maxima}).")
        else:
            self.__vida_actual = valor

    # Métodos operativos (Clase Base)
    def mostrar_estado(self):
        print(f"\n--- ESTADO DE {self.nombre.upper()} ---")
        print(f"Clase: {self.clase_personaje} | Nivel: {self.nivel}")
        print(f"Vida: {self.vida_actual}/{self.vida_maxima} | Daño Base: {self.dano_base}")

    def recibir_dano(self, cantidad_dano):
        print(f" {self.nombre} recibe {cantidad_dano} puntos de daño.")
        # Al restar, Python llama automáticamente al setter, validando el dato
        self.vida_actual -= cantidad_dano 
        if self.vida_actual == 0:
            print(f" ¡{self.nombre} ha sido derrotado!")

    def curarse(self, cantidad_curacion):
        if self.vida_actual == 0:
            print(f" {self.nombre} está derrotado y no puede curarse.")
            return
        print(f" {self.nombre} recibe curación de {cantidad_curacion} puntos.")
        self.vida_actual += cantidad_curacion


# Uso de super() y Herencia
class Mago(PersonajeRPG):
    def __init__(self, nombre, nivel, vida_maxima, dano_base, mana_maximo, elemento):
        # Se inicializan los atributos heredados con super()
        super().__init__(nombre, "Mago", nivel, vida_maxima, dano_base)
        
        # Se añaden 2 atributos nuevos exclusivos de la subclase
        self.mana_maximo = mana_maximo
        self.mana_actual = mana_maximo
        self.elemento = elemento 

    # Sobrescritura de métodos (Polimorfismo)
    def mostrar_estado(self):
        """Amplía el método original para mostrar los nuevos atributos mágicos."""
        super().mostrar_estado() # Llama al método de la clase padre
        print(f"Maná: {self.mana_actual}/{self.mana_maximo} | Elemento: {self.elemento}")

    # Sobrescritura de métodos (Polimorfismo)
    def curarse(self, cantidad_curacion):
        """El Mago usa su propia regla de curación: gasta maná para curarse el doble."""
        if self.mana_actual >= 10:
            print(f" {self.nombre} canaliza magia (-10 Maná) para potenciar su curación.")
            self.mana_actual -= 10
            # Llama al curarse del padre, pero con el valor duplicado
            super().curarse(cantidad_curacion * 2) 
        else:
            print(f"⚠️ {self.nombre} no tiene maná para usar magia curativa. Usa poción normal.")
            super().curarse(cantidad_curacion)


# Instanciación y pruebas
print("=== 1. CREACIÓN DE OBJETOS INDEPENDIENTES ===")
# 1 objeto de la clase base y 2 de la subclase
espadachin = PersonajeRPG("Kirito", "Espadachin", nivel=5, vida_maxima=200, dano_base=35)
maga_fuego = Mago("Azuna", nivel=5, vida_maxima=120, dano_base=15, mana_maximo=50, elemento="Fuego")
mago_hielo = Mago("Zephyr", nivel=4, vida_maxima=110, dano_base=12, mana_maximo=150, elemento="Hielo")

# Polimorfismo en acción: mostrar_estado actúa diferente según el tipo de objeto
espadachin.mostrar_estado()
maga_fuego.mostrar_estado()

print("\n=== 2. PRUEBAS DE ENCAPSULAMIENTO ===")
print("-> Intentando hackear el juego: dar vida negativa a Kirito")
espadachin.vida_actual = -500 
print(f"Vida verificada tras el intento: {espadachin.vida_actual}")

print("\n-> Intentando hackear el juego: dar vida excesiva a Zephyr")
mago_hielo.vida_actual = 9999 
print(f"Vida verificada tras el intento: {mago_hielo.vida_actual}")


print("\n=== 3. PRUEBAS DE HERENCIA Y POLIMORFISMO ===")
# El guerrero se cura con lógica normal
espadachin.recibir_dano(50)
espadachin.curarse(20)

print("\n")
# La maga usa la lógica sobrescrita (gasta maná y potencia el efecto)
maga_fuego.recibir_dano(80)
maga_fuego.curarse(20)

print("\n=== ESTADO FINAL DE LOS OBJETOS ===")
espadachin.mostrar_estado()
maga_fuego.mostrar_estado()
