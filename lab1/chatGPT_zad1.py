import math
from datetime import datetime, timedelta

def calculate_biorhythms(birthdate, current_date):
    days = (current_date - birthdate).days
    yp = math.sin(2 * math.pi / 23 * days)
    ye = math.sin(2 * math.pi / 28 * days)
    yi = math.sin(2 * math.pi / 33 * days)
    return yp, ye, yi

def main():
    name = input("Podaj swoje imię: ")
    birthdate_str = input("Podaj datę urodzenia w formacie RRRR-MM-DD: ")
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    current_date = datetime.now()

    print(f"Witaj, {name}!")

    days_alive = (current_date - birthdate).days
    print(f"Jesteś już {days_alive} dni na tym świecie.")

    yp, ye, yi = calculate_biorhythms(birthdate, current_date)
    print("Twoje biorytmy na dziś:")
    print(f"Fala emocjonalna: {yp:.2f}")
    print(f"Fala fizyczna: {ye:.2f}")
    print(f"Fala intelektualna: {yi:.2f}")

    if yp > 0.5 and ye > 0.5 and yi > 0.5:
        print("Gratulacje! Masz wysokie biorytmy dzisiaj.")
    elif yp < -0.5 or ye < -0.5 or yi < -0.5:
        print("Przeżywasz trudny dzień. Pamiętaj, że każdy ma gorsze momenty.")
        next_day = current_date.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
        yp_next, ye_next, yi_next = calculate_biorhythms(birthdate, next_day)
        print("Twoje biorytmy na jutro:")
        print(f"Fala emocjonalna: {yp_next:.2f}")
        print(f"Fala fizyczna: {ye_next:.2f}")
        print(f"Fala intelektualna: {yi_next:.2f}")
        if yp_next > yp and ye_next > ye and yi_next > yi:
            print("Nie martw się. Jutro będzie lepiej.")
        else:
            print("Niestety, biorytmy na jutro nie wyglądają lepiej.")
    else:
        print("Twoje biorytmy są neutralne. Nic szczególnego dzisiaj.")

if __name__ == "__main__":
    main()


#Czas pisany przez chat: 5-10 minut
