# Dado un conjunto de puntos en un plano cartesiano, se te pide encontrar los dos puntos más cercanos entre sí. Implementa una función llamada pares_cercanos que tome una lista de coordenadas (puntos en el plano) y devuelva las coordenadas de los dos puntos más cercanos junto con su distancia. Utiliza el algoritmo "Divide y Vencerás" para resolver este problema de manera eficiente, este ejercicio deberá usar Decoradores, como args y kwargs.

# Ejemplo:
# Entrada: [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
# Salida: Las coordenadas de los puntos más cercanos son (2, 3) y (3, 4) y su distancia es 1.4142135623730951

import time

# Decorador para medir el tiempo de ejecución de una función
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} tomó {end_time - start_time:.6f} segundos.")
        return result
    return wrapper

# Decorador para verificar si los puntos son válidos
def validate_points(func):
    def wrapper(*args, **kwargs):
        points = args[0]
        if not all(isinstance(point, tuple) and len(point) == 2 for point in points):
            raise ValueError("Los puntos deben ser tuplas de longitud 2")
        return func(*args, **kwargs)
    return wrapper

# Función para calcular la distancia entre dos puntos
def distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

# Función para encontrar los dos puntos más cercanos usando Divide y Vencerás
def closest_pair(points):
    n = len(points)
    if n <= 3:
        min_dist = float("inf")
        pair = None
        for i in range(n):
            for j in range(i+1, n):
                dist = distance(points[i], points[j])
                if dist < min_dist:
                    min_dist = dist
                    pair = (points[i], points[j])
        return pair, min_dist
    
    mid = n // 2
    left_pair, left_dist = closest_pair(points[:mid])
    right_pair, right_dist = closest_pair(points[mid:])
    
    if left_dist < right_dist:
        min_dist = left_dist
        min_pair = left_pair
    else:
        min_dist = right_dist
        min_pair = right_pair
    
    strip = []
    for point in points:
        if abs(point[0] - points[mid][0]) < min_dist:
            strip.append(point)
    strip.sort(key=lambda point: point[1])
    
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and strip[j][1] - strip[i][1] < min_dist:
            dist = distance(strip[i], strip[j])
            if dist < min_dist:
                min_dist = dist
                min_pair = (strip[i], strip[j])
            j += 1

    return min_pair, min_dist


# Decoramos la función para medir el tiempo de ejecución y validar los puntos
@measure_time
@validate_points
def find_closest_pair(points):
    return closest_pair(points)

# Ejemplo de uso
if __name__ == "__main__":
    coordinates =  [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    closest_points, min_distance = find_closest_pair(coordinates)
    print("Los puntos más cercanos son:", closest_points)
    print("La distancia entre ellos es:", min_distance)


