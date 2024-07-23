import matplotlib.pyplot as plt
import numpy as np
import math

def calculate_distance(angle):
    g = 9.81  # Przyspieszenie ziemskie [m/s^2]
    v0 = 50  # Początkowa prędkość [m/s]
    h = 100  # Wysokość trebusza [m]

    alpha_rad = math.radians(angle)  # Konwersja kąta na radiany

    # Obliczanie zasięgu za pomocą podanego wzoru
    d = (v0 * math.sin(alpha_rad) + math.sqrt(v0 ** 2 * math.sin(alpha_rad) ** 2 + 2 * g * h)) * (v0 * math.cos(alpha_rad)) / g

    return d

def plot_trajectory(angle):
    g = 9.81  # Przyspieszenie ziemskie [m/s^2]
    v0 = 50  # Początkowa prędkość [m/s]
    h = 100  # Wysokość trebusza [m]
    alpha_rad = math.radians(angle)  # Konwersja kąta na radiany

    # Czas lotu
    t_flight = (2 * v0 * math.sin(alpha_rad)) / g

    # Czas próbkowania
    dt = 0.01
    t = np.arange(0, t_flight, dt)

    # Trajektoria pocisku
    x = v0 * np.cos(alpha_rad) * t
    y = h + (v0 * np.sin(alpha_rad) * t) - (0.5 * g * t**2)

    # Rysowanie trajektorii
    plt.plot(x, y, label='Trajektoria pocisku', color='blue')
    plt.xlabel('Dystans [m]')
    plt.ylabel('Wysokość [m]')
    plt.title('Trajektoria pocisku')
    plt.grid(True)
    plt.legend()
    plt.savefig('trajektoria.png')
    plt.show()

def main():
    target_distance = np.random.randint(50, 341)
    print(f"Cel znajduje się w odległości: {target_distance} m")
    attempts = 0

    while True:
        alpha = float(input("Podaj kąt strzału w stopniach: "))
        distance = calculate_distance(alpha)

        print(f"Pocisk doleci na odległość: {distance:.2f} m")

        if target_distance - 5 <= distance <= target_distance + 5:
            print("Cel trafiony!")
            print(f"Liczba prób strzału: {attempts + 1}")
            plot_trajectory(alpha)
            break
        else:
            print("Pocisk chybił celu. Spróbuj ponownie.")
            attempts += 1

if __name__ == "__main__":
    main()
