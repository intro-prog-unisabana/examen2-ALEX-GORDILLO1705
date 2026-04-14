# lap_timer_client.py
# Programa cliente que lee tiempos de vuelta de un archivo
# e imprime la racha decreciente mas larga.

import lap_timer


def main():
    # TODO: Pedir el nombre del archivo al usuario usando input()
    
    # TODO: Abrir el archivo y leer el numero de vueltas n
    
    # TODO: Crear el cronometro usando lap_timer.init(n)
    
    # TODO: Leer los n tiempos de vuelta y agregarlos con lap_timer.add_lap()
    
    # TODO: Imprimir la racha decreciente mas larga
    #       usando lap_timer.longest_decreasing_streak()

  # lap_timer_client.py

    filename = input()

    with open(filename, 'r') as file:
        n = int(file.readline().strip())
        timer = lap_timer.init(n)

        for _ in range(n):
            lap_time = float(file.readline().strip())
            lap_timer.add_lap(timer, lap_time)

    print(lap_timer.longest_decreasing_streak(timer))


main()
    
if __name__ == "__main__":
    main()
    
