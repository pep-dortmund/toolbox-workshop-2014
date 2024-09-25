# Erklärung:                                                                                                                      # <2-2>
# Importiere numpy unter dem Namen np                                                                                             # <2-2>
import numpy as np                                                                                                                # <2-6>
                                                                                                                                  # <2-6>
# Erklärung:                                                                                                                      # <3-3>
# Importiere matplotlib.pyplot unter dem Namen plt                                                                                # <3-3>
import matplotlib.pyplot as plt                                                                                                   # <3-6>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
# Erklärung:                                                                                                                      # <4-4>
# Importiere curve_fit aus scipy.optimize                                                                                         # <4-4>
from scipy.optimize import curve_fit                                                                                              # <4-6>
from scipy.constants import physical_constants                                                                                    # <4-6>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
# Erklärung:                                                                                                                      # <5-6>
# Importiere uncertainties unter dem Namen unc                                                                                    # <5-6>
# Importiere uncertainties.unumpy unter dem Namen unp                                                                             # <5-6>
# Importiere der Funktionen nominal_values und std_devs                                                                           # <5-6>
# aus uncertainties.unumpy, unter den kürzeren Namen                                                                              # <5-6>
# noms respektive stds                                                                                                            # <5-6>
import uncertainties as unc                                                                                                       # <5-6>
import uncertainties.unumpy as unp                                                                                                # <5-6>
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)                                                       # <5-6>
                                                                                                                                  # <2-6>
# Erklärung:                                                                                                                      # <2-2>
# Die Daten liegen im Ordner 'data'. Um die Dateien einlesen                                                                      # <2-2>
# zu können, reicht es deswegen nicht den Dateinamen anzugeben,                                                                   # <2-2>
# es muss der gesamte Pfad ('Orderabfolge') angegeben werden:                                                                     # <2-2>
#                                                                                                                                 # <2-6>
# Für die Datei: Messwerte_Bahn.txt also data/Messwerte_Bahn.txt                                                                  # <2-2>
#                                                                                                                                 # <2-6>
# Der Name der Variable in der die eingelesenen Werte gespeichert werden                                                          # <2-2>
# ist frei wählbar, es bietet sich bei 'langen' Skripten an (im Gegensatz zur Mathematik)                                         # <2-2>
# nicht nur einbuchstabige Abkürzungen zu verwenden, um nicht die Übersicht zu verlieren.                                         # <2-2>
# Also beispielsweise track_length statt L. Ein Kommentar zur erklären sollte aber drin sein.                                     # <2-2>
#                                                                                                                                 # <2-6>
# Es bietet sich an die Daten direkt beim Einlesen in eine sinnvolle Einheit umzuwandeln                                          # <2-2>
# (falls nötig) und diese mit einem Kommentar zu vermerken                                                                        # <2-2>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
# Erklärung:                                                                                                                      # <5-6>
# Die Dateien im Ordner data enthalten jetzt auch Spalten mit den Unsicherheiten                                                  # <5-6>
# für die meisten Messwerte.                                                                                                      # <5-6>
# Beim Importieren der Daten muss beachtet werden, dass:                                                                          # <5-6>
# (1) Messgröße und Unsicherheit jeweils eine eigene Variablennamen brauchen.                                                     # <5-6>
# Auch hier ist eine konsistente Benennung sinnvoll                                                                               # <5-6>
# z.B. l (Messwerte) und l_unc (zugehörige Unsicherheiten)                                                                        # <5-6>
#                                                                                                                                 # <5-6>
# (2) die Unsicherheitbehafteten Messwerte noch erstellt werden müssen,                                                           # <5-6>
# entweder durch unc.ufloat oder durch das unp.uarray                                                                             # <5-6>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
# Länge der schiefen Ebene                                                                                                        # <2-6>
l = np.genfromtxt("data/Messwerte_Bahn.txt", delimiter=",")/100 # m                                                               # <2-4>
l, l_unc = np.genfromtxt("data/Messwerte_Bahn.txt", delimiter=",", unpack=True)/100 # m                                           # <5-6>
l = unc.ufloat(l, l_unc)                                                                                                          # <5-6>
                                                                                                                                  # <2-6>
# Framerate der Kamera                                                                                                            # <2-4>
# Framerate der Kamera (hat keine Unsicherheit, fps_unc = 0)                                                                      # <5-6>
fps = np.genfromtxt("data/Messwerte_Kamera.txt", delimiter=",") # 1/s                                                             # <2-4>
fps, fps_unc = np.genfromtxt("data/Messwerte_Kamera.txt", delimiter=",", unpack=True) # 1/s                                       # <5-6>
                                                                                                                                  # <2-6>
# Erklärung:                                                                                                                      # <2-2>
# Die Daten aus Dateien mit mehreren spalten muss man in einer extra Zeile skalieren                                              # <2-2>
# Masse und Umfang der Kugel                                                                                                      # <2-6>
m_b, u_b = np.genfromtxt("data/Messwerte_Kugel.txt", delimiter=",", unpack=True)                                                  # <2-4>
m_b, m_b_unc, u_b, u_b_unc = np.genfromtxt("data/Messwerte_Kugel.txt", delimiter=",", unpack=True)                                # <5-6>
m_b = m_b/1000 # kg                                                                                                               # <2-4>
u_b = u_b/100 # m                                                                                                                 # <2-4>
m_b = unc.ufloat(m_b,m_b_unc)/1000 # kg                                                                                           # <5-6>
u_b = unc.ufloat(u_b,m_b_unc)/100 # m                                                                                             # <5-6>
                                                                                                                                  # <2-6>
# Messreihe: Starthöhe und Startframe und Endframe (Kugel)                                                                        # <2-6>
h_b, Fi_b, Ff_b = np.genfromtxt("data/Messwerte_Frames_Kugel.txt", delimiter=",", unpack=True)                                    # <2-4>
h_b, h_b_unc, Fi_b, Fi_b_unc, Ff_b, Ff_b_unc = np.genfromtxt("data/Messwerte_Frames_Kugel.txt", delimiter=",", unpack=True)       # <5-6>
h_b = h_b/100 # m                                                                                                                 # <2-4>
h_b = unp.uarray(h_b, h_b_unc)/100 # m                                                                                            # <5-6>
Fi_b = unp.uarray(Fi_b, Fi_b_unc)                                                                                                 # <5-6>
Ff_b = unp.uarray(Ff_b, Ff_b_unc)                                                                                                 # <5-6>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
# Masse und Umfang des Zylinders                                                                                                  # <2-6>
m_c, u_c, d_c = np.genfromtxt("data/Messwerte_Zylinder.txt", delimiter=",", unpack=True)                                          # <2-4>
m_c, m_c_unc, u_c, u_c_unc, d_c, d_c_unc = np.genfromtxt("data/Messwerte_Zylinder.txt", delimiter=",", unpack=True)               # <5-6>
m_c = m_c/1000 # kg                                                                                                               # <2-4>
u_c = u_c/100 # m                                                                                                                 # <2-4>
d_c = d_c/100 # m                                                                                                                 # <2-4>
m_c = unc.ufloat(m_c, m_c_unc)/1000 # kg                                                                                          # <5-6>
u_c = unc.ufloat(u_c, u_c_unc)/100 # m                                                                                            # <5-6>
d_c = unc.ufloat(d_c, d_c_unc)/100 # m                                                                                            # <5-6>
                                                                                                                                  # <2-6>
# Messreihe: Starthöhe und Startframe und Endframe (Zylinder)                                                                     # <2-6>
h_c, Fi_c, Ff_c = np.genfromtxt("data/Messwerte_Frames_Zylinder.txt", delimiter=",", unpack=True)                                 # <2-4>
h_c, h_c_unc, Fi_c, Fi_c_unc, Ff_c, Ff_c_unc = np.genfromtxt("data/Messwerte_Frames_Zylinder.txt", delimiter=",", unpack=True)    # <5-6>
h_c = h_c/100 # m                                                                                                                 # <2-4>
h_c = unp.uarray(h_c, h_c_unc)/100 # m                                                                                            # <5-6>
Fi_c = unp.uarray(Fi_c, Fi_c_unc)                                                                                                 # <5-6>
Ff_c = unp.uarray(Ff_c, Ff_c_unc)                                                                                                 # <5-6>
                                                                                                                                  # <2-6>
# Erklärung:                                                                                                                      # <2-2>
# Ein gewisses Maß an Struktur in der Benennung von Variablen hilft bei der Orientierung,                                         # <2-2>
# gerade in der Zusammenarbeit mit euren jeweiligen Partnern.                                                                     # <2-2>
# Man muss es aber auch nicht übertreiben. Gerade ein Sprachenmix aus deutsch und englisch                                        # <2-2>
# ist nicht besonders tragisch: z.B. steht m_b für mass_ball aber u_b für umfang_ball,                                            # <2-2>
# aber das p_b für perimeter_ball würde mir persönlich nicht so klar werden.                                                      # <2-2>
                                                                                                                                  # <2-6>
# Erklärung:                                                                                                                      # <2-2>
# Auch die einzelnen "Arbeitsschritte" der Auswertung sollten in einem                                                            # <2-2>
# kurzen Kommentar erklärt werden.                                                                                                # <2-2>
# Erklärung:                                                                                                                      # <2-2>
# Die folgenden Berechnungen funktionieren alle weiterhin, nur jetzt mit automatischer Fehlerrechnung                             # <5-6>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
# Berechnung der benötigten Größen: Radius und Trägheitsmoment                                                                    # <2-6>
                                                                                                                                  # <2-6>
# Radius der Kugel                                                                                                                # <2-6>
r_b = u_b/(2*np.pi)                                                                                                               # <2-6>
                                                                                                                                  # <2-6>
# Äußerer Radius des Zylinders                                                                                                    # <2-6>
ro_c = u_c/(2*np.pi)                                                                                                              # <2-6>
                                                                                                                                  # <2-6>
# Innerer Radius des Zylinders                                                                                                    # <2-6>
ri_c = ro_c - d_c                                                                                                                 # <2-6>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
# Trägheitsmoment der Kugel                                                                                                       # <2-6>
I_b = 2/5 * m_b * r_b**2                                                                                                          # <2-6>
                                                                                                                                  # <2-6>
# Trägheitsmoment des Zylinders                                                                                                   # <2-6>
I_c = 1/2 * m_c * (ro_c**2 + ri_c**2)                                                                                             # <2-6>
                                                                                                                                  # <2-6>
print("Trägheitsmoment (Kugel)")                                                                                                  # <2-6>
print(I_b)                                                                                                                        # <2-6>
                                                                                                                                  # <2-6>
print("Trägheitsmoment (Zylinder)")                                                                                               # <2-6>
print(I_c)                                                                                                                        # <2-6>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
# Berechnung der Rollzeiten aus den Messwerten der Frames und Framerate                                                           # <2-6>
t_b = (Ff_b - Fi_b)/fps                                                                                                           # <2-6>
t_c = (Ff_c - Fi_c)/fps                                                                                                           # <2-6>
                                                                                                                                  # <2-6>
# Berechnung des Mittelwerts für die Zeitdauer t für jede (dreifach gemessene) Höhe                                               # <2-6>
                                                                                                                                  # <2-6>
# Erklärung:                                                                                                                      # <2-2>
# Es ist ein neuer Name (t_b_mean) notwendig, wenn die alten Werte in t_b                                                         # <2-2>
# noch verfügbar bleiben sollen                                                                                                   # <2-2>
#                                                                                                                                 # <2-2>
# Hieran sieht man (schon im Kleinen) die Nützlichkeit der numpy arrays                                                           # <2-2>
# und der möglichen Manipulationen:                                                                                               # <2-2>
# reshape(-1,3):                                                                                                                  # <2-2>
# Im array t_b liegen die zu mittelnden Werte immer genau hintereinander                                                          # <2-2>
# durch reshape(-1,3) wird aus t_b ein 2D array erzeugt, das in jeder                                                             # <2-2>
# Zeile 3 Spalten hat. Das bedeutet: Nach jeweils 3 Werten in t_b wird eine neue                                                  # <2-2>
# Zeile begonnen, damit sind in jeder Zeile genau die Werte die gemittelt werden sollen.                                          # <2-2>
# Die -1 als Anzahl der Zeilen ist gibt numpy die Anweisung, diese Anzahl                                                         # <2-2>
# selbst zu berechnen.                                                                                                            # <2-2>
#                                                                                                                                 # <2-2>
# mean(axis=1):                                                                                                                   # <2-2>
# Bei einem 2D array bezeichnet axis=0 die Zeilen und axis=1 die Spalten.                                                         # <2-2>
# Berechnet den Mittelwert "entlang der axis 1", d.h. die axis 1 ist die "Dimension"                                              # <2-2>
# des arrays, über die summiert wird (die danach nur noch einen Wert enthält).                                                    # <2-2>
# Da jede Zeile genau die drei Werte enthält, die zu mitteln sind, enthält jede                                                   # <2-2>
# Zeile danach genau den jeweiligen Mittelwert.                                                                                   # <2-2>
                                                                                                                                  # <2-6>
t_b_mean = t_b.reshape(-1,3).mean(axis=1)                                                                                         # <2-6>
                                                                                                                                  # <2-6>
# Erklärung:                                                                                                                      # <2-2>
# Das Array h_b enthält jede Höhe dreifach, auch die Auswahl                                                                      # <2-2>
# der einzelnen Höhen kann durch array Manipulation geschehen.                                                                    # <2-2>
#                                                                                                                                 # <2-2>
# Die Benennung der Variable (h_b_mean) wurde so gewählt,                                                                         # <2-2>
# dass diese zur zugehörigen Variable für die Zeitdauern passt                                                                    # <2-2>
#                                                                                                                                 # <2-2>
# reshape(-1, 3):                                                                                                                 # <2-2>
# analog zur Manipulation von t_b                                                                                                 # <2-2>
# [:,0]                                                                                                                           # <2-2>
# Aus jeder Zeile (= erster Index ist ':') wird die 'nullte' Spalte (= zweiter Index ist '0')                                     # <2-2>
# ausgewählt, d.h. in jeder Zeile bleibt genau eine Höhe erhalten.                                                                # <2-2>
                                                                                                                                  # <2-6>
h_b_mean = h_b.reshape(-1,3)[:,0]                                                                                                 # <2-6>
                                                                                                                                  # <2-6>
# Erklärung:                                                                                                                      # <2-2>
# analog für die andere Messreihe                                                                                                 # <2-2>
                                                                                                                                  # <2-6>
t_c_mean = t_c.reshape(-1,3).mean(axis=1)                                                                                         # <2-6>
h_c_mean = h_c.reshape(-1,3)[:,0]                                                                                                 # <2-6>
                                                                                                                                  # <2-6>
# Ausgabe verarbeiteten der Messwerte                                                                                             # <2-6>
                                                                                                                                  # <2-6>
print("Messwerte (Kugel)")                                                                                                        # <2-6>
print("alle Zeiten")                                                                                                              # <2-6>
print(t_b)                                                                                                                        # <2-6>
print("alle Höhen")                                                                                                               # <2-6>
print(h_b)                                                                                                                        # <2-6>
print("Höhe")                                                                                                                     # <2-6>
print(h_b_mean)                                                                                                                   # <2-6>
print("gemittlelte Zeit")                                                                                                         # <2-6>
print(t_b_mean)                                                                                                                   # <2-6>
print("\n")                                                                                                                       # <2-6>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
print("Messwerte (Zylinder)")                                                                                                     # <2-6>
print("alle Höhen")                                                                                                               # <2-6>
print(h_c)                                                                                                                        # <2-6>
print("alle Zeiten")                                                                                                              # <2-6>
print(t_c)                                                                                                                        # <2-6>
print("Höhe")                                                                                                                     # <2-6>
print(h_c_mean)                                                                                                                   # <2-6>
print("gemittlelte Zeit")                                                                                                         # <2-6>
print(t_c_mean)                                                                                                                   # <2-6>
print("\n")                                                                                                                       # <2-6>
                                                                                                                                  # <2-6>
# Erstelle Plots der Messwerte t_._mean und h_._mean                                                                              # <3-6>
                                                                                                                                  # <2-6>
# Erklärung:                                                                                                                      # <3-3>
# Funktionen für die Funktionsgleichungen der Theorie-Funktionen                                                                  # <3-3>
#                                                                                                                                 # <3-3>
# In Funktionen können Variablen verwendet werden, die außerhalb (global) definiert wurden                                        # <3-3>
# wie hier: l, ri_c und ro_c                                                                                                      # <3-3>
# Solche globalen Variablen können bei größeren Skripten/Programmen zu einem Problem werden                                       # <3-3>
# es ist also zumindest Vorsicht geboten                                                                                          # <3-3>
                                                                                                                                  # <2-6>
def theory_t_ball(h):                                                                                                             # <3-3>
     return np.sqrt(7/5 * 1/h * 2* l**2/9.81)                                                                                     # <3-3>
                                                                                                                                  # <2-6>
def theory_t_cylinder(h):                                                                                                         # <3-3>
    return np.sqrt((3 + ri_c**2/ro_c**2) * l**2/9.81 * 1/h)                                                                       # <3-3>
                                                                                                                                  # <2-6>
# Erklärung:                                                                                                                      # <4-4>
# Umwandeln der Theorie-Funktion zu einer Fit-Funktion:                                                                           # <4-4>
# Die Funktion erhält ein zusätzliches Argument für jeden Fitparameter, hier: g und t0                                            # <4-4>
# diese müssen auch in der Funktion verwendet werden.                                                                             # <4-4>
#                                                                                                                                 # <4-4>
# Namen sind wie immer beliebig und es gibt nicht "den einen richtigen Namen",                                                    # <4-4>
# aber es bietet sich wie immer an sprechende Namen zu verwenden, hier z.B.                                                       # <4-4>
# "fit_g_ball" als Abkürzung für "Fitfunktion für den Parameter g aus den Messwerten für die Kugel"                               # <4-4>
                                                                                                                                  # <2-6>
def fit_g_ball(h, g, t0):                                                                                                         # <4-4>
    return np.sqrt(7/5 * 1/h * 2* l**2/g) + t0                                                                                    # <4-4>
                                                                                                                                  # <2-6>
def fit_g_cylinder(h, g, t0):                                                                                                     # <4-4>
    return np.sqrt((3 + ri_c**2/ro_c**2) * l**2/g * 1/h) + t0                                                                     # <4-4>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
# Erklärung:                                                                                                                      # <5-6>
# Nur für die Erstellung der Plots und Fits ändert sich etwas:                                                                    # <5-6>
# Weder scipy noch matplotlib können direkt mit den unsicherheitbehafteten                                                        # <5-6>
# Messwerten umgehen.                                                                                                             # <5-6>
# Folgendes muss dafür geändert werden:                                                                                           # <5-6>
#                                                                                                                                 # <5-6>
# (1) in der Fitfunktion müssen mit der Funktion noms()                                                                           # <5-6>
# die Unsicherheiten von Konstanten entfernt werden                                                                               # <5-6>
#                                                                                                                                 # <5-6>
# (2) mit Unsicherheiten der unabhängigen Variable kann curve_fit nicht umgehen,                                                  # <5-6>
# diese müssen mit noms() entfernt werden.                                                                                        # <5-6>
#                                                                                                                                 # <5-6>
# (3) die Werte und Unsicherheiten der abhängigen Variable (gemessene Funktionswerte)                                             # <5-6>
# müssen getrennt übergeben werden: noms() und stds()                                                                             # <5-6>
#                                                                                                                                 # <5-6>
# (4) die Darstellung der Messwerte im Plot wird durch errorbar() ersetzt,                                                        # <5-6>
# um die Unsicherheiten anzeigen zu können                                                                                        # <5-6>
#                                                                                                                                 # <5-6>
# In der Aufgabe 3-curve_fit muss eine Funktion ucurve_fit geschrieben werden,                                                    # <5-6>
# die die scipy Funktion curve_fit verwendet, die aber den Umgang mit den                                                         # <5-6>
# Unsicherheiten abstrahiert, sodass man das nicht jedes Mal aufs neue machen muss.                                               # <5-6>
                                                                                                                                  # <2-6>
def fit_g_ball(h, g, t0):                                                                                                         # <5-6>
    return np.sqrt(7/5 * 1/h * 2* noms(l)**2/g) + t0                                                                              # <5-6>
                                                                                                                                  # <2-6>
def fit_g_cylinder(h, g, t0):                                                                                                     # <5-6>
    return np.sqrt((3 + noms(ri_c**2/ro_c**2)) * noms(l)**2/g * 1/h) + t0                                                         # <5-6>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
# Erklärung:                                                                                                                      # <4-4>
# Hier ist Vorsicht geboten, da die Fit-Funktion und Messwerte zusammen passen müssen                                             # <4-4>
# an solchen Stellen zahlt sich eine konsistente Benennung aus.                                                                   # <4-4>
# Berechnung der Fitparameter für die Kugel                                                                                       # <4-6>
                                                                                                                                  # <2-6>
params, covariance_matrix = curve_fit(fit_g_ball, h_b_mean, t_b_mean)                                                             # <4-4>
param_uncertainties = np.sqrt(np.diag(covariance_matrix))                                                                         # <4-6>
params, covariance_matrix = curve_fit(fit_g_ball, noms(h_b_mean), noms(t_b_mean), sigma=stds(t_b_mean))                           # <5-6>
param_uncertainties = np.sqrt(np.diag(covariance_matrix))                                                                         # <4-6>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
# Erklärung:                                                                                                                      # <4-4>
# Ansehnliche Ausgabe der Parameter aufs Terminal                                                                                 # <4-4>
print("Fitparameter (Kugel)")                                                                                                     # <4-6>
for name, value, uncertainty in zip("gt", params, param_uncertainties):                                                           # <4-6>
    print(f"{name} = {value:8.3f} ± {uncertainty:.3f}")                                                                           # <4-6>
print("\n")                                                                                                                       # <4-6>
                                                                                                                                  # <2-6>
# Erklärung:                                                                                                                      # <3-3>
# Die Werte für h die im Plot der Theorie-Funktionen verwendet werden, damit diese                                                # <3-3>
# auch tatsächlich aussieht wie eine differenzierbare Funktion.                                                                   # <3-3>
# Der Bereich in dem diese Werte liegen entspricht, aber dem der Messwerte ca. [0.03, 0.33]                                       # <3-3>
h_plot = np.linspace(0.03, 0.33, 205)                                                                                             # <3-6>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
# Fit Parameter für den Zylinder                                                                                                  # <4-4>
# Fitparameter für den Zylinder                                                                                                   # <5-6>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
# Erklärung:                                                                                                                      # <3-3>
# Erstellen einer figure mit einem subplot darin (1 Zeile x 1 Spalte an subplots)                                                 # <3-3>
fig, ax = plt.subplots(1, 1, layout="constrained")                                                                                # <3-6>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
# Erklärung:                                                                                                                      # <3-3>
# Einstellung der Achsenbeschriftungen                                                                                            # <3-3>
ax.set_xlabel("$h$ / m")                                                                                                          # <3-6>
ax.set_ylabel("$t$ / s")                                                                                                          # <3-6>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
# Erklärung:                                                                                                                      # <3-3>
# Darstellen der Messwerte mit Legendeneintrag                                                                                    # <3-3>
ax.plot(h_b_mean, t_b_mean, "k+", label="Daten: Kugel")                                                                           # <3-4>
ax.plot(h_plot, theory_t_ball(h_plot),  label="Theorie")                                                                          # <3-3>
                                                                                                                                  # <2-6>
# Erklärung:                                                                                                                      # <4-4>
# Theorie-Funktion durch Fit-Funktion mit Fit-Parametern ersetzen                                                                 # <4-4>
ax.plot(h_plot, fit_g_ball(h_plot, *params),  label="Fit")                                                                        # <4-6>
                                                                                                                                  # <2-6>
ax.errorbar(noms(h_b_mean), noms(t_b_mean), yerr=stds(t_b_mean), fmt="k+", label="Daten: Kugel")                                  # <5-6>
ax.plot(h_plot, fit_g_ball(h_plot, *params),  label="Fit")                                                                        # <4-6>
ax.legend()                                                                                                                       # <3-6>
fig.savefig("plot_kugel.pdf")                                                                                                     # <3-3>
fig.savefig("plot-g_kugel.pdf")                                                                                                   # <4-6>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
# Erklärung:                                                                                                                      # <4-4>
# Analog für die Messreihe des Zylinders                                                                                          # <4-4>
# Achtung! Copy-and-paste ist natürlich gängige Praxis,                                                                           # <4-4>
# aber alle Variablen müssen angepasst werden.                                                                                    # <4-4>
                                                                                                                                  # <2-6>
# Berechnung der Fitparameter für den Zylinder                                                                                    # <4-6>
params, covariance_matrix = curve_fit(fit_g_cylinder, h_c_mean, t_c_mean)                                                         # <4-4>
param_uncertainties = np.sqrt(np.diag(covariance_matrix))                                                                         # <4-6>
params, covariance_matrix = curve_fit(fit_g_cylinder, noms(h_c_mean), noms(t_c_mean), sigma=stds(t_c_mean))                       # <5-6>
param_uncertainties = np.sqrt(np.diag(covariance_matrix))                                                                         # <4-6>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
print("Fitparameter (Zylinder)")                                                                                                  # <4-6>
for name, value, uncertainty in zip("gt", params, param_uncertainties):                                                           # <4-6>
    print(f"{name} = {value:8.3f} ± {uncertainty:.3f}")                                                                           # <4-6>
print("\n")                                                                                                                       # <4-6>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
fig, ax = plt.subplots(1, 1, layout="constrained")                                                                                # <3-6>
                                                                                                                                  # <2-6>
ax.set_xlabel("$h$ / m")                                                                                                          # <3-6>
ax.set_ylabel("$t$ / s")                                                                                                          # <3-6>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
ax.plot(h_c_mean, t_c_mean, "k+", label="Daten: Zylinder")                                                                        # <3-4>
ax.errorbar(noms(h_c_mean), noms(t_c_mean), yerr=stds(t_c_mean), fmt="k+", label="Daten: Zylinder")                               # <5-6>
ax.plot(h_plot, theory_t_cylinder(h_plot),  label="Theorie")                                                                      # <3-3>
ax.plot(h_plot, fit_g_cylinder(h_plot, *params),  label="Fit")                                                                    # <4-6>
ax.legend()                                                                                                                       # <3-6>
fig.savefig("plot_zylinder.pdf")                                                                                                  # <3-3>
fig.savefig("plot-g_zylinder.pdf")                                                                                                # <4-6>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
# Erklärung:                                                                                                                      # <4-4>
# Verwenden der physikalischen Konstanten aus scipy                                                                               # <4-4>
# hier: g                                                                                                                         # <4-4>
# physical_constants enthält 3er-tuple, der erste Eintrag                                                                         # <4-4>
# der tuple ist der Wert der Konstante, deswegen [0]                                                                              # <4-4>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
def fit_I_ball(h, I, t0):                                                                                                         # <4-6>
    g = physical_constants["standard acceleration of gravity"][0]                                                                 # <4-6>
    return np.sqrt(2/g * 1/h * l**2 * (1 + I/(m_b * r_b**2)) ) + t0                                                               # <4-4>
    return np.sqrt(2/g * 1/h * noms(l)**2 * (1 + I/(noms(m_b * r_b)**2)) ) + t0                                                   # <5-6>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
def fit_I_cylinder(h, I, t0):                                                                                                     # <4-6>
    g = physical_constants["standard acceleration of gravity"][0]                                                                 # <4-6>
    return np.sqrt(2/g * 1/h * l**2 * (1 + I/(m_c * ro_c**2) )) + t0                                                              # <4-4>
    return np.sqrt(2/g * 1/h * noms(l)**2 * (1 + I/(noms(m_c * ro_c**2)) )) + t0                                                  # <5-6>
                                                                                                                                  # <2-6>
# Erklärung:                                                                                                                      # <4-4>
# Durch den Fit wird diese Warnung auf das Terminal ausgegeben:                                                                   # <4-4>
# .../v16515/auswertung.py:197: RuntimeWarning: invalid value encountered in sqrt                                                 # <4-4>
#  return np.sqrt(2/g * 1/h * l**2 * (1 + I/(m_c * ro_c**2) )) + t0                                                               # <4-4>
#                                                                                                                                 # <4-4>
# Diese bedeutet, dass während des Fits negative Werte für I 'ausprobiert' wurden,                                                # <4-4>
# von denen die Wurzel nicht berechnet werden konnte.                                                                             # <4-4>
# Man kann das verhindern, in dem man die Parameter auf den physikalisch möglichen                                                # <4-4>
# Bereich einschränkt. Dies tut man mit dem zusätzlichen Parameter bounds für curve_fit,                                          # <4-4>
# hier müsste                                                                                                                     # <4-4>
# bounds=([0,-np.inf],[+np.inf,+np.inf])                                                                                          # <4-4>
# als zusätzliches Argument für curve_fit ergänzt werden.                                                                         # <4-4>
# bounds gibt den minimalen und den maximalen Wert für alle Parameter an,                                                         # <4-4>
# und zwar zuerst alle Minima und dann alle Maxima,                                                                               # <4-4>
# in diesem konkreten Beispiel steht bounds also für: 0 < I < +np.inf und -np.inf < t0 < +np.inf                                  # <4-4>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
# Berechnung der Fitparameter für die Kugel                                                                                       # <4-6>
params, covariance_matrix = curve_fit(fit_I_ball, h_b_mean, t_b_mean)                                                             # <4-4>
param_uncertainties = np.sqrt(np.diag(covariance_matrix))                                                                         # <4-6>
params, covariance_matrix = curve_fit(fit_I_ball, noms(h_b_mean), noms(t_b_mean), sigma=stds(t_b_mean))                           # <5-6>
param_uncertainties = np.sqrt(np.diag(covariance_matrix))                                                                         # <4-6>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
print("Fitparameter (Kugel)")                                                                                                     # <4-6>
for name, value, uncertainty in zip("It", params, param_uncertainties):                                                           # <4-6>
    # in kg*m² sehr klein, umwandlung zu kg*cm²                                                                                   # <4-6>
    if name == "I":                                                                                                               # <4-6>
        value *= 10000                                                                                                            # <4-6>
        uncertainty *= 10000                                                                                                      # <4-6>
    print(f"{name} = {value:8.3f} ± {uncertainty:.3f}")                                                                           # <4-6>
print("\n")                                                                                                                       # <4-6>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
fig, ax = plt.subplots(1, 1, layout="constrained")                                                                                # <4-6>
                                                                                                                                  # <2-6>
ax.set_xlabel("$h$ / m")                                                                                                          # <4-6>
ax.set_ylabel("$t$ / s")                                                                                                          # <4-6>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
ax.plot(h_c_mean, t_c_mean, "k+", label="Daten: Kugel")                                                                           # <4-4>
ax.errorbar(noms(h_b_mean), noms(t_b_mean), yerr=stds(t_b_mean), fmt="k+", label="Daten: Kugel")                                  # <5-6>
ax.plot(h_plot, fit_I_cylinder(h_plot, *params),  label="Fit")                                                                    # <4-6>
ax.legend()                                                                                                                       # <4-6>
fig.savefig("plot-I_kugel.pdf")                                                                                                   # <4-6>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
# Berechnung der Fitparameter für den Zylinder                                                                                    # <4-6>
params, covariance_matrix = curve_fit(fit_I_cylinder, h_c_mean, t_c_mean)                                                         # <4-4>
param_uncertainties = np.sqrt(np.diag(covariance_matrix))                                                                         # <4-6>
params, covariance_matrix = curve_fit(fit_I_cylinder, noms(h_c_mean), noms(t_c_mean), sigma=stds(t_c_mean))                       # <5-6>
param_uncertainties = np.sqrt(np.diag(covariance_matrix))                                                                         # <4-6>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
print("Fitparameter (Zylinder)")                                                                                                  # <4-6>
for name, value, uncertainty in zip("It", params, param_uncertainties):                                                           # <4-6>
    # in kg*m² sehr klein, umwandlung zu kg*cm²                                                                                   # <4-6>
    if name == "I":                                                                                                               # <4-6>
        value *= 10000                                                                                                            # <4-6>
        uncertainty *= 10000                                                                                                      # <4-6>
    print(f"{name} = {value:8.3f} ± {uncertainty:.3f}")                                                                           # <4-6>
print("\n")                                                                                                                       # <4-6>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
fig, ax = plt.subplots(1, 1, layout="constrained")                                                                                # <4-6>
                                                                                                                                  # <2-6>
ax.set_xlabel("$h$ / m")                                                                                                          # <4-6>
ax.set_ylabel("$t$ / s")                                                                                                          # <4-6>
                                                                                                                                  # <2-6>
                                                                                                                                  # <2-6>
ax.plot(h_c_mean, t_c_mean, "k+", label="Daten: Zylinder")                                                                        # <4-6>
ax.errorbar(noms(h_c_mean), noms(t_c_mean), yerr=stds(t_c_mean), fmt="k+", label="Daten: Zylinder")                               # <5-6>
ax.plot(h_plot, fit_I_cylinder(h_plot, *params),  label="Fit")                                                                    # <4-6>
ax.legend()                                                                                                                       # <4-6>
fig.savefig("plot-I_zylinder.pdf")                                                                                                # <4-6>
