
# Libreria de funciones para registrar tiempos de vuelta en una carrera.
#
# Estructura del diccionario (timer):
#   - 'max':   numero maximo de vueltas permitidas (int)
#   - 'times': lista con los tiempos de cada vuelta (list)
#   - 'total': tiempo acumulado de todas las vueltas (float)


# Libreria de funciones para registrar tiempos de vuelta en una carrera.

def init(max_laps):
    """
    Crea y retorna un diccionario para almacenar hasta max_laps vueltas.
    """
    return {
        'max': max_laps,
        'times': [],
        'total': 0.0
    }


def add_lap(timer, time):
    """
    Agrega una nueva vuelta con el tiempo especificado.
    Retorna el diccionario modificado.
    """
    if len(timer['times']) < timer['max']:
        timer['times'].append(time)
        timer['total'] += time
        return timer
    else:
        raise ValueError("No se puede agregar mas vueltas")


def count(timer):
    """
    Retorna el numero de vueltas agregadas.
    """
    return len(timer['times'])


def cumulative_time(timer):
    """
    Retorna el tiempo acumulado de todas las vueltas.
    """
    return timer['total']


def format_laps(timer):
    """
    Retorna una representacion en cadena de los tiempos.
    Formato: [t1, t2, t3, ..., tn]
    """
    return str(timer['times'])


def fastest_lap(timer):
    """
    Retorna el tiempo mas rapido de cualquier vuelta.
    """
    if not timer['times']:
        return None
    return min(timer['times'])


def fastest_multi_lap(timer, k):
    """
    Retorna el tiempo acumulado mas rapido de cualquier k vueltas consecutivas.
    """
    times = timer['times']

    if len(times) < k or k <= 0:
        return None

    min_time = float('inf')

    for i in range(len(times) - k + 1):
        current_sum = sum(times[i:i+k])
        if current_sum < min_time:
            min_time = current_sum

    return min_time


def longest_decreasing_streak(timer):
    """
    Retorna la longitud maxima de una secuencia de vueltas consecutivas
    donde los tiempos disminuyen estrictamente.
    """
    times = timer['times']

    if not times:
        return 0

    max_streak = 1
    current_streak = 1

    for i in range(1, len(times)):
        if times[i] < times[i - 1]:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 1

    return max_streak


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
