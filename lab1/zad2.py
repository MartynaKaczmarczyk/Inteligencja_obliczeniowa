import numpy as np
import matplotlib.pyplot as plt
import math
import random

def calculate_position(v0, alpha, h, t):
    g = 9.81
    x = v0 * t * math.cos(alpha)
    y = h + (v0 * t * math.sin(alpha)) - (0.5 * g * t**2)
    return x, y


def STRZAŁ():
    g = 9.81 #m/s^2
    h = 100  #m
    v0 = 50  #m/s
    distance_object = random.randint(50, 340)
    print("Cel namierzony w odległości:", distance_object)
    attempt = 0
    while True:
        try:
            attempt += 1
            alpha = int(input("Skalibruj trebusza: "))
            alpha_rad = math.radians(alpha)
            distance = (v0 * math.sin(alpha_rad) + math.sqrt(v0 ** 2 * math.sin(alpha_rad) ** 2 + 2 * g * h)) * (v0 * math.cos(alpha_rad)) / g
            print(distance)
            if distance < distance_object + 5 and distance > distance_object - 5:
                print(f"Cel trafiony :) za {attempt} podejściem")
                break
        except:
            print("Wprowadź liczbę")

    time_end = (v0 * math.sin(math.radians(alpha)) + math.sqrt((v0 * math.sin(math.radians(alpha))) ** 2 + 2 * 9.81 * h)) / 9.81
    time_values = np.linspace(0, time_end, 1000)

    positions = [(0, h)]
    for t in time_values:
        x, y = calculate_position(v0, alpha_rad, h, t)
        if y >= 0:
            positions.append((x, y))
        else:
            break
    x_values, y_values = zip(*positions)

    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, label="Trajectory of projectile")
    plt.title("Projectile Motion for the Trebuchet")
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    angle_label = "Kąt rzutu: {}°".format(alpha)
    plt.text(5, 90, angle_label, fontsize=12, bbox=dict(facecolor='white', alpha=0.5))
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=2)
    plt.legend()
    plt.savefig('trajektoria.png')
    plt.show()

STRZAŁ()


