from datetime import datetime
import math


def write_data():
    name = input("Podaj swoje imię: ")
    print("Witaj", name)
    year_of_birth = int(input("Którego roku się urodziłaś/eś? "))
    month_of_birth = int(input("Którego miesiąca? "))
    day_of_birth = int(input("Którego dnia? "))
    current_date = datetime.now()
    try:
        birthdate = datetime(year_of_birth, month_of_birth, day_of_birth)
        days = current_date - birthdate
        print("Jesteś już", days.days, "dni na tym świecie")
        yp = math.sin(((2 * math.pi)/23) * days.days) #Fizyczna fala
        ye = math.sin(((2 * math.pi)/28) * days.days) #Emocjonalna fala
        yi = math.sin(((2 * math.pi)/33) * days.days) #Intelektualna fala

        print("Twoje biorytmy dzisiaj to:", yp, "- fizyczna fala", ye, "- emocjonalna fala", yi, "- intelektulana fala")

        if yp < -0.5 or yi < -0.5 or ye < -0.5:
            print("Auch, to musi być ciężki dzień")
            next_res = next_day(days.days)
            print("Twoje biorytmy dzisiaj to:", next_res[0], "- fizyczna fala", next_res[1], "- emocjonalna fala", next_res[2], "- intelektulana fala")
            print(next_res)
            if next_res[0] < yp or next_res[1] < ye or next_res[2] < yi:
                print("Jutro będzie GORZEJ. Przygotuj się")
            else:
                print("Nie martw się. Jutro będzie LEPIEJ")
        elif yp > 0.5 or yi > 0.5 or ye > 0.5:
            print("Musiało coś miłego się dzisiaj przydarzyć :). Masz bardzo wysokie biorytmy. Gratulacje")
        else:
            print("Masz normalne biorytmy")
    except:
        print("Podano błędne dane")



def next_day(days):
    next_day = days + 1
    yp = math.sin((2 * math.pi)/23 * next_day) #Fizyczna fala
    ye = math.sin((2 * math.pi)/28 * next_day) #Emocjonalna fala
    yi = math.sin((2 * math.pi)/33 * next_day) #Intelektualna fala

    return [yp, ye, yi]

#Program pisany jakieś pół godziny, 40 minut




write_data()


#============================================ POPRAWIONY KOD PRZEZ CHAT =====================================
import datetime

print("Chat's version")

def get_birthdate():
    year = int(input("Którego roku się urodziłaś/eś? "))
    month = int(input("Którego miesiąca? "))
    day = int(input("Którego dnia? "))
    return datetime.datetime(year, month, day)

def calculate_biorhythms(days):
    yp = math.sin(((2 * math.pi)/23) * days) # Fizyczna fala
    ye = math.sin(((2 * math.pi)/28) * days) # Emocjonalna fala
    yi = math.sin(((2 * math.pi)/33) * days) # Intelektualna fala
    return yp, ye, yi

def print_biorhythms(name, days, yp, ye, yi):
    print(f"Witaj {name}!")
    print(f"Jesteś już {days} dni na tym świecie.")
    print("Twoje biorytmy dzisiaj to:")
    print(f"Fizyczna fala: {yp}")
    print(f"Emocjonalna fala: {ye}")
    print(f"Intelektualna fala: {yi}")

def print_tomorrow_prediction(yp, ye, yi, next_res):
    print("Twoje biorytmy jutro to:")
    print(f"Fizyczna fala: {next_res[0]}")
    print(f"Emocjonalna fala: {next_res[1]}")
    print(f"Intelektualna fala: {next_res[2]}")
    if any(n < c for n, c in zip(next_res, (yp, ye, yi))):
        print("Jutro będzie GORZEJ. Przygotuj się")
    else:
        print("Nie martw się. Jutro będzie LEPIEJ")

def write_dataCHAT():
    try:
        name = input("Podaj swoje imię: ")
        birthdate = get_birthdate()
        current_date = datetime.datetime.now()
        days = (current_date - birthdate).days
        yp, ye, yi = calculate_biorhythms(days)

        print_biorhythms(name, days, yp, ye, yi)

        if any(x < -0.5 for x in (yp, ye, yi)):
            print("Auch, to musi być ciężki dzień")
            next_res = calculate_biorhythms(days + 1)
            print_tomorrow_prediction(yp, ye, yi, next_res)
        elif any(x > 0.5 for x in (yp, ye, yi)):
            print("Musiało coś miłego się dzisiaj przydarzyć :). Masz bardzo wysokie biorytmy. Gratulacje")
        else:
            print("Masz normalne biorytmy")
    except ValueError:
        print("Podano błędne dane")

write_dataCHAT()


