import cv2
from matplotlib import pyplot as plt

# Opening image
img = cv2.imread("stop2.jpeg")

# OpenCV opens images as BRG
# but we want it as RGB We'll
# also need a grayscale version
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Use minSize because for not
# bothering with extra-small
# dots that would look like STOP signs
stop_data = cv2.CascadeClassifier('stop_data.xml')

found = stop_data.detectMultiScale(img_gray,
                                   minSize=(20, 20))

# Don't do anything if there's
# no sign
amount_found = len(found)

if amount_found != 0:

    # There may be more than one
    # sign in the image
    for (x, y, width, height) in found:
        # We draw a green rectangle around
        # every recognized sign
        cv2.rectangle(img_rgb, (x, y),
                      (x + height, y + width),
                      (0, 255, 0), 5)

# Creates the environment of
# the picture and shows it
plt.subplot(1, 1, 1)
plt.imshow(img_rgb)
plt.show()

# Haar Cascades bazują na prostych cechach obrazu, zwanych cechami Haar. Są to prostokątne wzory, które sumują piksele w jasnych i ciemnych regionach obrazu. Typowe cechy Haar to:
#
#     Cechy krawędziowe: prostokąty, gdzie jedna strona jest jasna, a druga ciemna.
#     Cechy liniowe: prostokąty z trzema poziomymi lub pionowymi regionami (jasne-ciemne-jasne lub ciemne-jasne-ciemne).
#     Cechy czterokątne: prostokąty podzielone na cztery równe części, dwie jasne i dwie ciemne.
#
# Potem liczona jest suma wartości pikseli powyżej danego piksela i na lewo od niego.
# Następnie selekcjonowane są najbardziej dyskryminujące cechy spośród wszystkich możliwych cech Haar. Proces ten tworzy silny klasyfikator, łączący wiele słabych klasyfikatorów.
# Następnie model jest szkolony na danych obrazach w kilku etapach:
#
#     Pierwszy etap szybko odrzuca większość obszarów niebędących obiektem, używając prostych cech.
#     Kolejne etapy stosują bardziej złożone cechy i dokładniej analizują regiony zakwalifikowane przez wcześniejsze etapy.
#     Jeśli region przejdzie przez wszystkie etapy kaskady, jest uznawany za obiekt poszukiwany.