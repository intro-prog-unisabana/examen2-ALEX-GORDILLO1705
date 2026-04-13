# lap_timer.py
# Libreria de funciones para registrar tiempos de vuelta en una carrera.
#
# Estructura del diccionario (timer):
#   - 'max':   numero maximo de vueltas permitidas (int)
#   - 'times': lista con los tiempos de cada vuelta (list)
#   - 'total': tiempo acumulado de todas las vueltas (float)


def init(max_laps):
    """
    Crea y retorna un diccionario para almacenar hasta max_laps vueltas.
    """
    # TODO: Implementar
    pass


def add_lap(timer, time):
    """
    Agrega una nueva vuelta con el tiempo especificado.
    Retorna el diccionario modificado.
    """
    # TODO: Implementar
    pass


def count(timer):
    """
    Retorna el numero de vueltas agregadas.
    """
    # TODO: Implementar
    pass


def cumulative_time(timer):
    """
    Retorna el tiempo acumulado de todas las vueltas.
    """
    # TODO: Implementar
    pass


def format_laps(timer):
    """
    Retorna una representacion en cadena de los tiempos.
    Formato: [t1, t2, t3, ..., tn]
    """
    # TODO: Implementar
    pass


def fastest_lap(timer):
    """
    Retorna el tiempo mas rapido de cualquier vuelta.
    """
    # TODO: Implementar
    pass


def fastest_multi_lap(timer, k):
    """
    Retorna el tiempo acumulado mas rapido de cualquier k vueltas consecutivas.
    """
    # TODO: Implementar
    pass


def longest_decreasing_streak(timer):
    """
    Retorna la longitud maxima de una secuencia de vueltas consecutivas
    donde los tiempos disminuyen estrictamente.
    """
    # TODO: Implementar
    pass


def main():
    # crear un cronometro para el record mundial de 100m de Usain Bolt,
    # dividiendo la carrera en 10 segmentos (o "vueltas")
    timer = init(10)
    timer = add_lap(timer, 1.85)
    timer = add_lap(timer, 1.02)
    timer = add_lap(timer, 0.91)
    timer = add_lap(timer, 0.87)
    timer = add_lap(timer, 0.85)
    timer = add_lap(timer, 0.82)
    timer = add_lap(timer, 0.82)
    timer = add_lap(timer, 0.82)
    timer = add_lap(timer, 0.83)
    timer = add_lap(timer, 0.90)

    # imprimir estadisticas
    print("numero de vueltas =", count(timer))                    # 10
    print("tiempo acumulado =", cumulative_time(timer))           # 9.69
    print("vuelta mas rapida =", fastest_lap(timer))              # 0.82
    print("50m mas rapidos =", fastest_multi_lap(timer, 5))       # 4.14
    print("racha mas larga =", longest_decreasing_streak(timer))  # 6

    # imprimir tiempos
    # [1.85, 1.02, 0.91, 0.87, 0.85, 0.82, 0.82, 0.82, 0.83, 0.9]
    print(format_laps(timer))


if __name__ == "__main__":
    main()
