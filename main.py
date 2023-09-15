# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
# #     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# #
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

# true_or_false = False
# print(type(true_or_false))

# active_user = True
# fruits = ['aple','orange', 'kiwi', 'watermelon']
# print(fruits[-1])

# fruits = ['aple','orange', 'kiwi', 'watermelon']
# lietuvis_pilietis = {
# 'id':1,
# 'Vardas': 'Antanas',
# 'Amzius': 34,
# 'Miestas':'Klaipeda'
# }
# print(lietuvos_pilietis)
# print("Vardas:", lietuvos_pilietis["Vardas"])
# print("Po")
# lietuvis_pilietis['Vardas'] = "Giedrius"
import random
# lietuvos_pilietis = {
#     'id': 1,
#     'Vardas': 'Antantas',
#     'Amzius': 34,
#     'Miestas': 'Klaipeda'
# }
# # print(lietuvos_pilietis)
# print("Pries:")
# print("Vardas: ", lietuvos_pilietis["Vardas"])
# print("Po: ")
# lietuvos_pilietis['Vardas'] = "Giedrius"
# print("Vardas: ", lietuvos_pilietis["Vardas"])
# # print(type(fruits))


# temperaturos = [20, 25, 22, 18, 22]
#
# suma = sum(temperaturos)
# print(suma)
#
# kiekis = len(temperaturos)
# print(kiekis)
#
# vidutine_temp = suma/kiekis
# print("Vidutine temperatura yra: ", vidutine_temp)

# sudetis = 5 + 5
# atimtis = 6 - 2
# dalyba_be_liekanos = 15//3
# daugyba = 5 * 9
# laipsnis = 2 ** 3
# # dalyba_liekana = 10 % 3
# print(laipsnis)

# 1. Sukurkite kintamąjį vardas ir priskirkite jam savo vardą.
# Tada parašykite programą, kuri išspausdina sveikinimo žinutę su jūsų vardu;

# vardas = ("Inga")
# print("Sveikinimai" "," + vardas + "!")


# 2. Sukurkite kintamuosius skaicius1 ir skaicius2,
# ir priskirkite jiems du skaičius. Parašykite programą, kuri juos sudeda ir išspausdina sumą.

# # create variable skaicius1 with value 8
# skaicius1 = 8
# # create variable number2 with value 18
# skaicius2 = 18
# # add skaicius1 and skaicius2
# sudetis = skaicius1 + skaicius2
# # print result
# print(sudetis)

# 3. Parašykite programą, kuri prašo vartotojo įvesti skaičių ir
# nustato, ar tai yra lyginis ar nelyginis skaičius.

#create a variable skaicius

# skaicius = int("4")
# rezultatas = "lyginis" if skaicius %2 == 0 else "nelyginis"
# print (skaicius, rezultatas)
#
# 4. Sukurkite žodyną pavadinimu telefonu_knygute, kuriam raktai yra žmonių vardai, o reikšmės - jų telefono numeriai.
# Parašykite programą, kuri leidžia vartotojui ieškoti telefono numerio pagal žmogaus vardą.

# telefonu_knyga = {}
# vardas = ('Inga')
# telefono_numeris = ("37068409130")
# print("vardas" ":"
# "telefono_numeris" ":")

# skaicius = 42
# if skaicius <42:
# print("Lygus")
# else:
# print("Nelygus")

# sarasas = [1,2,3,4,5]
# for elementas in sarasas:
#     print("Elementas: " , elementas)

# for i in range(5):
#     print(i)

# for i in range(2, 8):
#     print(i)

# for i in range(5, 0, -1):
#     print(i)

# skaiciai = [24, 11, 72, 34, 7, 84]
# # koks didziausas skaicius mano sarase
#
# didziausias_skaicius = skaiciai[0]
#
# for skaicius in skaiciai:
#  if skaicius > didziausias_skaicius:
#      didziausias_skaicius = skaicius
# print("Didziausias skaicius yra:", didziausias_skaicius)

# skaicius = input("Koks tavo vardas:")
# print(skaicius)

# skaicius = float(input("Parasykite skaiciu:"))
#
# print(skaicius)

# skaicius = int(input("Iveskite skaiciu:"))
# suma = 0
# for i in range(1, skaicius + 1):
#     suma += i
# print("Skaiciu suma nuo 1 iki", skaicius, "yra", suma)

# is saraso isfiltruoti lyginius skaicius

# sarasas = [2, 5, 11, 12, 25, 9]
# lyginiai_skaiciai = []
# for skaicius in sarasas:
#     if skaicius %2 ==0:
#         lyginiai_skaiciai.append(skaicius)
# print("lyginiai_skaiciai ", lyginiai_skaiciai)

# pyramides su zvaigzdutemis

# eiluciu_sk = int(input("Iveskite sveika skaiciu "))
# for eilute in range (1, eiluciu_sk+1):
#      tarpas = eiluciu_sk - eilute
#      zvaigzdutes = 2 * eilute-1
#      print(" " * tarpas + "*" * zvaigzdutes)

# surasti pirminius skaicius tarp intervalo [10, 50]. isvesti pirminius skaicius

# pradzia = 10
# pabaiga = 50

# print(f"pirminiai skaiciai tarp {pradzia} ir {pabaiga} yra: ")
# for skaicius in range (pradzia, pabaiga+1):
#     if skaicius > 1:
#         for daliklis in range(2, skaicius):
#             if (skaicius% daliklis) ==0:
#                 break
#         else :
#             print(skaicius)

# Patikrinti zodzius is saraso ir atspausdinti zodzius, kurie prasideda A

# zodziai_is_a = ["as", "tu", "jis", "asta", "marius"]
# raide = "a"
# for zodis in zodziai_is_a:
#     if zodis[0].lower()== raide.lower():
#         print(zodis)

# sudaryti ir isvesti daugybos lentele

# print("daugybos lentele nuo 1 iki 10")
# for i in range(1,11):
#     for j in range(1,11):
#         rezultatas = i*j
#         print(f"{i} * {j} = {rezultatas}")
#     print()

# patikrinti, ar skaicius, kuri ivede vartotojas, yra teigiamas, neigiamas ar lygus nuliui

# skaicius = int(input("iveskite skaiciu_> "))
# if skaicius > 0:
#     print("ivestas skaicius yra teigiamas")
# elif skaicius <0:
#     print("ivestas skaicius yra neigiamas")
# else:
#     print("ivestas skaicius yra lygus 0")

# isvesti fizz skaiciams, kurie dalijasi is 3, buzz skaiciams, kurie dalijasi is 5, fizzbuzz skaiciai, kurie dalijasi is 3 ir 5
# intervale nuo 1 iki 100

# for skaicius in range(1, 101):
#     if skaicius % 3 ==0 and skaicius %5 ==0:
#         print("fizzbuzz")
#     elif skaicius % 3 ==0:
#         print("fizz")
#     elif skaicius % 5 ==0:
#         print("buzz")
#     else:
#         print(skaicius)

# pasleptas_skaicius = random.randint(1, 100)
# bandymai = 0
# maksimalus_bandymu_skaicius = 3
# while bandymai < maksimalus_bandymu_skaicius:
#     spejimas = int(input("atspekite paslepta skaiciu nuo 1 iki 100: "))
#     bandymai+=1
#     if spejimas == pasleptas_skaicius:
#         print(f"Valio! Atspejote skaiciu per {bandymai} bandymus")
#         break
#     elif spejimas < pasleptas_skaicius:
#         print("Bandykite didesni skaiciu")
#     else:
#         print("Bandykite mazesni skaiciu:)")
#     if bandymai >= maksimalus_bandymu_skaicius:
#         print(f"Jus pasiekete maksimalu bandymu skaiciu. pasleptas skaicius buvo {pasleptas_skaicius}")




# sukurti skaiciu atspejimo zaidima. generuoti atsitiktini skaiciu,
# o vartotojas turi atspeti per tam tikra bandymu skaiciu


# sukurti zodziu sarasa, kur saugomi zodziai ir ju ilgiai, isvesti zodzius, kurie ilgesni nei 6 simboliai

# zodziai = ["kaimas", "miestas", "savivaldybe", "miestelis", "gyvenviete", "mama", "tetis"]
# zodynas = {}
# for zodis in zodziai:
#     zodynas[zodis] = len(zodis)
# for zodis, ilgis in zodynas.items():
#     if ilgis > 6:
#         print(f"{zodis}: {ilgis} simboliai")

# 1. Sukurkite žodyną ir trumpą tekstą.
# Atspasudinkite žodžius, kurie pasikartojo daugiau nei 3 kartus.

# tekstas = "ir vel ruduo, ir vel tamsu, ir vel vejuota"
# zodynas ={}
# zodziai = tekstas
# for zodis in zodziai:
#         zodynas[zodis] = zodynas
# print("Zodziai, kurie kartojasi daugiau nei 3 kartus:")
# for zodis, skaicius in zodynas.items():
#     if skaicius >3:
#         print(f"{zodis}: {skaicius} kartai")

# trumpas_tekstas = "visi visi visi norėjo alaus, bet buvo tik tuščios alaus bačkos ir rarūgusio vyno alaus buteliuose"
# žodynas = {}
# zodziai = trumpas_tekstas.split()
# for zodis in zodziai:
#     zodis = zodis.strip(",.")
#     žodynas[zodis] = žodynas.get(zodis, 0) + 1
# for zodis, pasikartojimai in žodynas.items():
#     if pasikartojimai >=3:
#         print(f"pasikartojantis(-ys) Žodis(-iai) yra: {zodis}, pasikartojo {pasikartojimai} kartų")

# 3. Sukurkite žodyną su studentų duomenimis ir atspausdinkite studentus, kurių vidurkis yra aukščiau 8.0;
# studentai = [
#     {"vardas": "Inga", "pavarde": "Ingaite", "vidurkis": 6.1},
#     {"vardas": "Jurga", "pavarde": "Jurgaite", "vidurkis": 7.1},
#     {"vardas": "Antanas", "pavarde": "Antanaitis", "vidurkis": 8.3},
#     {"vardas": "Linas", "pavarde": "Linaitis", "vidurkis": 9.5},
# ]
# geri_studentai = []
# for studentas in studentai:
#     if studentas["vidurkis"] > 8:
#         geri_studentai.append(studentas)
# print("geri_studentai")
# for studentas in geri_studentai:
#     print(f"vardas: {studentas['vardas']}, Pavarde: {studentas['pavarde']}, Vidurkis: {studentas['vidurkis']}")

# 4. Sukurti žodyną su knygų informacija ir surikiuoti knygas pagal metus ir pavadinimus.

# knygos = [
#     {"pavadinimas": "1984-ieji", "metai":1948},
#     {"pavadinimas": "Placebas", "metai":2023},
#     {"pavadinimas": "Rojus", "metai":1980},
# ]
# for knyga in knygos:
#     print(f"Pavadinimas: {knyga['pavadinimas']}, Metai: {knyga['metai']}")

# Parašykite programą, kuri suskaičiuoja visų sveikujų skaičių nuo 1 iki n ėjimo sumą, kur n yra vartotojo įvestas skaičius.
# Panaudokite "for" ciklą ir "if" sąlygos sakinį, kad tikrintumėte, ar įvestas skaičius yra sveikasis;

# n= int(input("Iveskite sveikaji skaiciu n:"))
# if n <= 0:
#     print("ivestas skaicius turi buti sveikasis")
# else:
#     suma = 0
#     for skaicius in range(1, n+1):
#         suma+= skaicius
#     print(f"sveikuju skaiciu nuo 1 iki {n} suma yra {suma}")

# 2. Sukurkite programą, kurioje vartotojas gali įvesti mokinio pažymį (nuo 1 iki 10). Programa turi grąžinti mokinio vertinimą
# (pvz., "Neužtektinai", "Silpnai", "Vidutiniškai", "Gerai", "Puikiai"). Naudokite "if" sąlygos sakinį;

# pazymys = int(input("iveskite mokinio pazymi nuo 1 iki 10: "))
# if pazymys <= 1 or pazymys <= 2:
#     vertinimas = "Neužtektinai"
# elif pazymys <= 3 or pazymys <= 4:
#     vertinimas = "Silpnai"
# elif pazymys <= 5 or pazymys <= 6:
#     vertinimas = "Vidutiniškai"
# elif pazymys <= 7 or pazymys <= 8:
#     vertinimas = "Gerai"
# elif pazymys <= 9 or pazymys <= 10:
#     vertinimas = "Puikiai"
# else:
#     vertinimas = "ivesties klaida"
#
# print(f"Mokinio vertinimas: {vertinimas}")

# # Vartotojas įveda pažymį
# Tikriname pažymio vertinimą

# pazymys = int(input("Įveskite mokinio pažymį nuo 1 iki 10: "))
# if pazymys >= 9 and pazymys <= 10:
#     vertinimas = "Puikiai"
# elif pazymys >= 7 and pazymys < 9:
#     vertinimas = "Gerai"
# elif pazymys >= 5 and pazymys < 7:
#     vertinimas = "Vidutiniškai"
# elif pazymys >= 4 and pazymys < 5:
#     vertinimas = "Silpnai"
# elif pazymys >= 1 and pazymys < 4:
#     vertinimas = "Neužtektinai"
# else:
#     vertinimas = "Netinkamas pažymys, įveskite pažymį nuo 1 iki 10."
# print(f"Mokinio vertinimas: {vertinimas}")

# 3. Sukurkite programą, kuri leidžia vartotojui įvesti metus. Programa turi patikrinti,
# ar įvesti metai yra keliamieji (dalijasi iš 4) ir atspausdinti atitinkamą pranešimą;

# metai = int(input("iveskite metus:"))
# if metai % 4 == 0:
#     print(f"{metai} yra keliamieji metai")
# else:
#     print("{metai} nera keliamieji metai")

# 4. Turite žodyną, kuriame yra vardai ir amžius. Parašykite programą, kuri peržiūri žodyną ir išrenka tik tas poras,
# kuriose amžius yra didesnis arba lygus 18. Rezultatus patalpinkite naujame žodyne;

# asmenys ={
#      'Rasa': 46,
#      'Daiva': 30,
#      'Jurga': 15,
#      'Joana': 18,
#      'Antanas': 32,
#      'Jurgis': 14,
#      'Domas': 45,
#      'Linas': 37
#      }
# asmenys_naujas = {}
# for vardas, amzius in asmenys.items():
#     if amzius >= 18:
#         asmenys_naujas[vardas] = amzius
# print(asmenys_naujas)

# 5. Leiskite vartotojui įvesti kelias prekes ir jų kainas.
# Sukurkite sąrašą, kuriame prekės yra žodynai, kuriuose yra prekės pavadinimas ir kaina.
# Taip pat paskaičiuokite bendrą visų prekių kainą;

# prekiu_krepselis = []
# while True:
#     preke = input("Nurodyte prekę arba įrašykite žodį baigti")
#     if not preke:
#         break
#     kaina = float(input("Įveskite prekės kainą: "))
#     prekes_info = {'pavadinimas': preke, 'kaina': kaina}
#     prekiu_krepselis.append(prekes_info)
#
# Krepselio_suma = sum((prekes_info['kaina'] for prekes_info in prekiu_krepselis))
# print("prekiu sarasas: ")
# for prekes_info in prekiu_krepselis:
#     print(f"Pavadinimas: {prekes_info['pavadinimas']}, Kaina: {prekes_info['kaina']}")
# print(f"Bendra kaina: {Krepselio_suma}")

# 6. Turite sąrašą žmonių vardų. Sukurkite programą, kuri leidžia vartotojui įvesti vardą ir patikrina, ar jis yra sąraše.
# Jei vardas yra sąraše, programa turi išvesti pranešimą "Vardas yra sąraše," kitu atveju - "Vardo nėra sąraše."

# asmenys = ["Inga", "Jurga", "Jurate", "Antanas", "Jonas"]
# vardas = input("Iveskite varda:")
# if vardas in asmenys:
#     print(f"Vardas {vardas} yra sarase.")
# else:
#     print(f"Vardas {vardas} nera sarase")

# 1. Sukurkite sąrašą temperatūros su temperatūromis. Patikrinkite kiekvieną temperatūrą sąraše
# ir išveskite "šilta" (jei temperatūra virš 20) arba "šalta" (jei temperatūra 20 ar mažiau).

# temperaturos = [15, 20, 22, 25, 28, 30]
# for temperatura in temperaturos:
#     if temperatura > 20:
#         print(f"{temperatura} yra šilta.")
#     else:
#         print(f"{temperatura} yra šalta. ")

# temperaturos = [15, 20, 22, 25, 28, 30]
# for temperatura in temperaturos:
#     if temperatura > 20:
#         print(f"{temperatura} yra šilta.")
#     else:
#         print(f"{temperatura} yra šalta. ")

# 2. Turite žodyną su studentų vardais ir jų pažymiais.
# Parašykite "for" ciklą, kuris išveda kiekvieno studento vardą ir jo pažymį.
#
# studentai = {
#     "Augis": 10,
#     "Rasa": 7,
#     "Daiva": 9,
#     "Antanas": 5
#
# }
# for vardas, pazymys in studentai.items():
#     print(f"Studentas: {vardas}, Pazymys: {pazymys}")

# 3. Sukurkite tuščią sąrašą sarasas ir leiskite vartotojui įvesti skaičius. Naudojant "while" ciklą,
# pridėkite kiekvieną įvestą skaičių prie sąrašo.
# Ciklą nutraukite, kai vartotojas įveda 0.

# sarasas = []
# while True:
#     skaicius = float(input("iveskite skaiciu (N.B.: ivedus 0, ciklas baigsis):"))
#     if skaicius ==0:
#         break
#         sarasas.append(skaicius)
#         print("ivesti skaiciai:")
#         for skaicius in sarasas:
#             print(skaicius)

# 4. Turite žodyną, kuriame saugomi gėrimų pavadinimai ir jų kainos.
# Vartotojas įveda gėrimo pavadinimą, o jūs patikrinkite, ar tokio pavadinimo gėrimas yra žodyne.
# Jei taip, išveskite jo kainą; jei ne, išveskite pranešimą "Gėrimas nerastas".





# jei tik pop, paskutinis nuo galo
# vardai = ['Jonas', 'Petras', 'Marius', 'Laura']
# pirmas_vardas = vardai.pop(0)
# print(pirmas_vardas)


# indeksas parodo kelinta isves: rodys Jonas
#
# vardai = ['Jonas', 'Petras', 'Marius', 'Laura']
# pirmas_vardas = vardai.pop(0)
# print(pirmas_vardas)

# vardai = ['Jonas', 'Petras', 'Marius', 'Laura']
# vardai.insert(1,'Giedrius')
# print(vardai)

# vardai.append('Giedrius')

# vardai.sort()
# print(vardai)

# vardai.sort(reverse=True)
# print(vardai)

# vardai.remove('Laura')
# print(vardai)


# () negalima keisti reiksmiu. naudojami raktai.
# [] galima keisti reiksmes


# vaisiai = ('obuolys', 'kriause', 'bananas', 'braske')
# vaisiai1 = ['obuolys', 'kriause', 'bananas', 'braske']
# vaisiai = {
#     'obuolys'
#     'kriause'
#     'bananas'
#     'braske'
# }

# vaisiai2 = vaisiai[0]
# print(vaisiai2)

# skaiciai = (3.14, 2.71)
# x, y = skaiciai
# print(x)
# print(y)

# vaisiai = ['obuolys', 'kriause', 'bananas', 'braske']
# for indeksas, vaisius in enumerate(vaisiai, start=1):
#     print(f"{indeksas}. {vaisius}")

# open funkcija - rasoma su with
# r -
# w -

# suskaiciavo kiekviena raide ir tarpa

# with open("failo_pav.txt", 'w', encoding='utf-8') as file:
#     content = file.write("kuriame nauja faila")
#     print(content)

# with open("failo_pav.txt", 'w', encoding='utf-8') as file:
#     content = file.read()
#     print(content)

# with open("failo_pav.txt", 'w', encoding='utf-8') as file:
#     content = file.write("\Papildomas tekstas")
#     print(content)

# with open("failo_pav.txt", 'r', encoding='utf-8') as file:
#     content = file.read()
#     print(content)

# with open("failo_pav.txt", 'r', encoding='utf-8') as file:
#     for eilute in file:
#         print(eilute.strip())

# vaisiai = []
# with open("vaisiai.txt", 'r', encoding='utf-8') as file:
#     file.write('obuolys, \nkriause, \nbananas, \nbraske')
#     vaisiai = file.readlines()
#     print(vaisiai)

# Funkcija vartotojo apibrezta struktura. gauna ivesti, vykdo operacijas, grazina
# rezultata. Leidzia strukturizuoti , supaprastina

# def pasisveikinimas(vardas):
#     sveikinimas = f"Sveiki, {vardas}"
#     return sveikinimas
#
# vardas = input("Iveskite savo varda:")
# sveikinimas = pasisveikinimas (vardas)
# print(sveikinimas)

# def ar_lyginis(skaicius):
#     if skaicius % 2 ==0:
#         return True
#     else:
#         return False
# skaicius = 7
# if ar_lyginis(skaicius):
#     print(f"{skaicius} yra lyginis")
# else:
#     print(f"{skaicius} yra nelyginis")

# def suma (a, b):
#     rezultatas = a+b
#     return  rezultatas
#
# x=5
# y=3
# sumos_rezultatas = suma(x, y)
# print(f"{x} + {y} = {sumos_rezultatas}")

# def suma():
#     rezultatas = 5+3
#     return  rezultatas
#
# x=5
# y=3
# sumos_rezultatas = suma()
# print(f"{x} + {y} = {sumos_rezultatas}")

# def pasisveikinimas():
#     sveikinimas = f"Sveiki, Inga"
#     return sveikinimas
#
# if__name__ =="_main_"
#
# ????

# def vidurkis(skaiciai):
#     suma = sum(skaiciai)
#     avg = suma / len(skaiciai)
#     return avg
#
# sarasas = [10,15, 20, 25, 30]
# rezultatas = vidurkis(sarasas)
# print(f"saraso vidurkis:{rezultatas}")

# patikrinti, as skaicius teigiamas, ar neigiamas

# def ar_teigiamas(skaicius):
#     if skaicius >0:
#         return True
#     else:
#         return False
# skaicius = 4
# if ar_teigiamas(skaicius):
#     print(f"{skaicius} yra teigimas")
# else:
#     print(f"{skaicius} yra neigiamas")

# parasyti funkcija, kuri suras max skaiciu sarase

# def didziausias_skaicius(skaicius):
#     didziausias = skaicius[0]
#     for i in skaicius:
#         if i > didziausias:
#             didziausias = i
#     return didziausias
#
# sarasas = [10, 658, 12, -2]
# didziausias = didziausias_skaicius(sarasas)
# print(f"didziausias yra {didziausias}")

# parasyti funkcija, kuri sujungia du sarasus

# def sujungti_sarasai (sarasas_1, sarasas_2):
#     sujungtas_sarasas = sarasas_1+sarasas_2
#     return sujungtas_sarasas
# a_1 = [1, 2, 3]
# a_2 = [4, 5, 6]
# rezultatas = sujungti_sarasai(a_1, a_2)
# print(rezultatas)

# parasyti funkcija, kuri suras didesni skaiciu sarase, nei nurodytas.

# def didesnis(listas, skaicius):
#    didis = [sk_1 for sk_1 in listas if sk_1 >skaicius]
#    return didis
#
# listas = [1, 2, 15, 101, 1005]
# n = 8
# didesni_sk = didesnis(listas, n)
# print(f"sarase skaiciai didesni uz {n}: yra {didesni_sk}")

# 4. Turite žodyną, kuriame saugomi gėrimų pavadinimai ir jų kainos.
# Vartotojas įveda gėrimo pavadinimą, o jūs patikrinkite, ar tokio pavadinimo gėrimas yra žodyne.
# Jei taip, išveskite jo kainą; jei ne, išveskite pranešimą "Gėrimas nerastas".



# namu darbai: 2023-09-08
#
# 1. Parašykite funkciją, kuri priimtų sąrašą studento pažymių ir grąžintų vidurkį;

# def vidurkis(pazymiai):
#     suma_pazymiai = sum(pazymiai)
#     vidurkis = suma_pazymiai/len(pazymiai)
#     return vidurkis
#
# studento_pazymiai = [5, 8, 10, 9, 6]
# rezultatas = vidurkis(studento_pazymiai)
# print("Pazymiu vidurkis:", rezultatas)

# 3. Sukurkite funkciją zodziu_kiekis(tekstas),
# kuri priima tekstą ir grąžina žodžių skaičių tekste. Žodžius galite laikyti atskirtais tarpais;

# def zodziu_kiekis(tekstas):
#     zodziai = tekstas.split()
#     return len(zodziai)
#
# tekstas = "Grazus, siltas ruduo."
# kiekis = zodziu_kiekis(tekstas)
# print("zodziu skaicius tekste:", kiekis)


# 4. NEVEIKIA atsakymas, rodo pozicija nr. 3!!! Sukurkite funkciją didziausias_elementas(sarasas),
# kuri priima sąrašą skaičių ir grąžina didžiausią elementą;

# def didziausias_elementas(sarasas):
#     didziausias = sarasas[0]
#     for skaicius in sarasas:
#         if skaicius > didziausias:
#             didziausias = skaicius
#             return didziausias
#
# skaiciai = [15, 10, 88, 100, 8]
# didziausias = didziausias_elementas(skaiciai)
# print("didziausias elementas sarase:", didziausias)

# 5. Sukurkite funkciją kvadrato_plotas(ilgis),
# kuri priima kvadrato kraštinės ilgį ir grąžina kvadrato plotą.

# def kvadrato_plotas(ilgis):
#     plotas = ilgis **2
#     return plotas
#
# ilgis = float(input("Iveskite kvadrato krastines ilgi:"))
# plotas = kvadrato_plotas(ilgis)
# print("Kvadrato plotas su krastines ilgiu", ilgis, "yra:", plotas)
#
# 6. Sukurkite funkciją sarasas_suma(sarasas), kuri priima sąrašą skaičių ir suskaičiuoja jų sumą.
# Leiskite vartotojui įvesti sąrašą skaičių ir išvesti jų sumą;

# def sarasas_suma(sarasas):
#     suma = sum(sarasas)
#     return suma
#
# ivestas_skaiciu_sarasas = float(input("Iveskite skaiciu sarasa:"))
# sarasas = ivestas_skaiciu_sarasas()
# suma = sarasas_suma(sarasas)
# print("saraso skaiciu suma:", suma)



# 7. Sukurkite funkciją, kuri priimtų skaičių sąrašą ir grąžintų visų sąrašo skaičių sandaugą.
# negeras atsakymas

# def skaiciu_sandauga(sarasas):
#     sandauga = 1
#     for skaicius in sarasas:
#         sandauga *=skaicius
#         return sandauga
#
# skaiciai = [2, 3, 4, 5]
# print("skaiciu saraso sandauga:", sandauga)

# teisingas atsakymas
#
# skaiciai = [1, 2, 3, 4, 5]
# sandauga = 1
# for skaicius in skaiciai:
#     sandauga *=skaicius
#
# print("saraso skaiciu sandauga:", sandauga)

# geras sprendinys:

# def mano_sarasas(sarasas):
#    sandauga = 1
#    for skaicius in sarasas:
#         sandauga *=skaicius
#    return sandauga
# sk_sarasas = [2, 4, 6, 8, 10]
# print('Saraso skaiciu sandauga lygi:',mano_sarasas (sk_sarasas))

#sukuriama klase,
# class Zmogus:
#
# # sukuriamas konstruktorius
#
#     def __init__(self, vardas, amzius):
#         self. vardas = vardas
#         self.amzius = amzius
#
# # kuriami metodai
#     def sveikinimas(self):
#         return f"Sveiki as esu {self.vardas} ir man yra {self.amzius} metu"
#
# # sukuriamas objektas
#
# zmogus1= Zmogus("Jonas", 20)
# zmogus2= Zmogus("Antanas", 45)
# print(zmogus1.sveikinimas())
# print(zmogus2.sveikinimas())

# class Automobilis:
#
#     def __init__(self, marke, modelis):
#         self.marke = marke
#         self.modelis = modelis
#         self.greitis = 0
#     def akseleratorius(self):
#         self.greitis += 10
#
#     def stabdis(self):
#         self.greitis -= 5
#
#     def info(self):
#         return f"{self.marke} {self.modelis}, greitis: {self.greitis} km/h"

# class Automobilis:
#     def __init__(self, marke, modelis):
#             self.marke = marke
#             self.modelis = modelis
#             self.greitis = 0
#
#     def akseleratorius(self):
#             self.greitis += 10
#
#     def stabdis(self):
#             self.greitis -= 5
#
#     def info(self):
#         return f"{self.marke} {self.modelis}, greitis: {self.greitis} km/h"
#
# auto1=Automobilis ('Mazda', '323')
# auto1.akseleratorius()
# auto1.akseleratorius()
# auto1.akseleratorius()
# auto1.stabdis()
# print(auto1.info())

# class Knyga:
#     def __init__(self, pavadinimas, autorius, leidimo_metai):
#         self.pavadinimas = pavadinimas
#         self.autorius = autorius
#         self.leidimo_metai = leidimo_metai
#
#     def info(self):
#         return f"Knygos pavadinimas: {self.pavadinimas}, autorius: {self.autorius}, leidimo metai: {self.leidimo_metai}"
# knyga1 = Knyga ( pavadinimas: "Visi norejo testo", autorius: "studentas", leidimo metai)

# class Knyga:
#     def __init__(self, pavadinimas, autorius, leidimo_metai):
#         self.pavadinimas = pavadinimas
#         self.autorius = autorius
#         self.leidimo_metai = leidimo_metai
#     def info(self):
#         return f"Knygos pavadinimas {self.pavadinimas}, autorius: {self.autorius}, išleidimo metai: {self.leidimo_metai}"
#
# knyga1 = Knyga("'Visi norėjo testo'", "studentas", 2023)
# print(knyga1.info())

# class Preke:
#     def __init__(self, pavadinimas, kaina):
#         self.pavadinimas= pavadinimas
#         self.kaina = kaina
#     def info(self):
#         return f'{self.pavadinimas}: {self.kaina} euru'
# class Krepselis:
#     def __init__(self):
#         self.prekes = []
#
#     def ideti_preke(self, preke):
#         self.prekes.append(preke)
#     def krepselio_info(self):
#         if not self.prekes:
#             print("tokios prekes nera")
#         else:
#             print("krepselio turinys:")
#             for preke in self.prekes:
#                 print(preke.info())
#     def bendra_suma(self):
#         suma = sum(preke.kaina for preke in self.prekes)
#         return suma
#
# krepsys = Krepselis()
# preke1 = Preke('obuolys', 5.56)
# preke2 = Preke('bananas',  2.25)
# preke3 = Preke('vanduo',  1.31)
# preke4 = Preke('kava',  10.55)
#
#
# krepsys.ideti_preke(preke1)
# krepsys.ideti_preke(preke2)
# krepsys.ideti_preke(preke3)
# krepsys.ideti_preke(preke4)
# krepsys.ideti_preke(preke4)
# krepsys.krepselio_info()
#
# print(f'bendra suma: {krepsys.bendra_suma()} euru')

# Sukurkite klasę "Saskaita", kuri turėtų šias savybes ir metodus:
#
#     * saskaitos_nr: sąskaitos numeris.
#     * balansas: sąskaitos balansas (numatytasis pradžioje yra 0).
#     * inesti(suma): metodas, kuris prideda nurodytą sumą prie sąskaitos balanso.
#     * isimti(suma): metodas, kuris sumažina sąskaitos balansą nurodyta suma, jei yra pakankamai lėšų,
# arba išveda pranešimą apie nepakankamą balansą.
#     * informacija(): metodas, kuris grąžina informaciją apie sąskaitą (sąskaitos numeris ir balansas).
#
# Sukurkite bent du objektus pagal šią klasę ir atlikite operacijas, tokiu kaip lėšų įnešimas ir išėmimas, bei gaukite sąskaitos informaciją.

# class Saskaita:
#     def __init__(self, saskaitos_numeris, balansas=0):
#         self.saskaitos_numeris = saskaitos_numeris
#         self.balansas = balansas
#
#     def inesti_suma(self, suma):
#         self.balansas += suma
#         print(f'saskaitos numeris: {self.saskaitos_numeris}, inesta suma: {suma} euru. Naujas balansinis likutis: {self.balansas}')
#
#     def isimti_suma(self, suma):
#         if self.balansas>= suma:
#             self.balansas-= suma
#             print(f'saskaitos numeris: {self.saskaitos_numeris}, isimta suma: {suma} euru. Naujas balansinis likutis: {self.balansas}')
#         else:
#             print(f"nepakankamas balansinis likutis")
#
#     def info(self):
#             return f"saskaitos numeris: {self.saskaitos_numeris}, Balansinis likutis: {self.balansas}"
#
# saskaita1 = Saskaita("LT123456789", 500)
# saskaita2 = Saskaita( "LT101112131415", 1500)
#
#
# saskaita1.info()
# saskaita1.inesti_suma(500)
# saskaita1.isimti_suma(700)
# saskaita2.info()
# saskaita2.inesti_suma(100)
# saskaita2.isimti_suma(5000)

# Sukurkite klasę "Studentas", kuri turėtų šias savybes:
#
#     * vardas: studento vardas.
#     * pazymiai: sąrašas su studento pažymiais.
#
# Sukurkite klasę "Mokytojas", kuri turėtų šias savybes:
#
#     * vardas: mokytojo vardas.
#     * Mokytojo dėstoma tema: mokytojo dėstomas dalykas.
#
# Papildykite "Studentas" klasę metodu vidurkis(), kuris apskaičiuoja studento pažymių vidurkį.
#
# Papildykite "Mokytojas" klasę metodu ivertinimas(studentas, pazymys), kuris prideda studentui pažymį.
#
# Sukurkite objektus pagal "Studentas" ir "Mokytojas" klases,
# pridėkite pažymius ir vykdykite vidurkio apskaičiavimus bei pažymių pridėjimus.

# class Studentas:
#     def __init__(self, studento_vardas):
#         self.studento_vardas = studento_vardas
#         self.pazymiai = []
#
#     def prideti_pazymi(self, pazymys):
#         self.pazymiai.append(pazymys)
#
#     def vidurkis(self):
#         if not self.pazymiai:
#             return 0
#         return sum(self.pazymiai)/len(self.pazymiai)
#
# class Mokytojas:
#     def __init__(self, vardas, destomas_dalykas):
#         self.vardas = vardas
#         self.destomas_dalykas = destomas_dalykas
#
#     def ivertinimas(self, studentas, pazymys):
#         studentas.prideti_pazymi(pazymys)
#
# studentas1 = Studentas ('Petras')
# mokytojas1 = Mokytojas('Jurgis','Informatika')
#
# mokytojas1.ivertinimas('studentas1', '3')
# print(f'{studentas1.studento_vardas}, vidurkis: {studentas1.vidurkis()}')
#

#objekto_pavadinimas = Klases_pavadinimas(klases_savybes)
# geras atsakymas

# class Studentas:
#     def __init__(self, st_vardas):
#         self.st_vardas = st_vardas
#         self.pazymiai = []
#     def prideti_pazymi(self, pazymys):
#         self.pazymiai.append(pazymys)
#     def vidurkis(self):
#         if not self.pazymiai:
#             return 0
#         return sum(self.pazymiai) / len(self.pazymiai)
#
# class Mokytojas:
#     def __init__(self, mokytojo_vardas, destomas_dakykas):
#         self.mokytojo_vardas = mokytojo_vardas
#         self.destomas_dalykas = destomas_dakykas
#     def ivertinimas(self, studentas, pazymys):
#         studentas.prideti_pazymi(pazymys)
#
# studentas1=Studentas('Petras')
# mokytojas1=Mokytojas('Jurgis', 'informatika')
#
# mokytojas1.ivertinimas(studentas1, 3)
#
# print(f'{studentas1.st_vardas}, vidurkis: {studentas1.vidurkis()}')

# sukurkite klase kava, kuri turi savybes: pavadinimas, kaina, talpa.
# parasyti metoda, ar kava tinkama tam puodeliui pagal talpa

# Sukurkite klasę "Kava", kuri turėtų savybes "pavadinimas", "kaina", ir "talpa".
# Parašykite metodą, kuris patikrintų, ar ši kava yra tinkama tam tikram puodeliui, pagal jo talpą.

# class Kava:
#     def __init__(self, pavadinimas, kaina, talpa):
#         self.pavadinimas = pavadinimas
#         self.kaina = kaina
#         self.talpa = talpa
#
#     def ar_tinkama_puodeliui(self, puodelio_talpa):
#         if self.talpa <= puodelio.talpa:
#             return f'{self.pavadinimas} kava tinka puodeliui su talpa {puodelio_talpa} ml'
#         else:
#             return f'{self.pavadinimas} kava netinka puodeliui su talpa {puodelio_talpa} ml'
#
# kava1 = Kava("Latte", 2.50, 300)
# kava2 = Kava("espresso", 3.0, 100)
#
# puodelio_talpa=300
# print(kava1.ar_tinkama_puodeliui(puodelio_talpa))


# class Kava:
#     def __init__(self, pavadinimas, kaina, talpa):
#         self.pavadinimas = pavadinimas
#         self.kaina = kaina
#         self.talpa = talpa
#     def ar_tinkama_puodeliui(self, puodelio_talpa):
#         if self.talpa <= puodelio_talpa:
#             return f'{self.pavadinimas} kava tinka puodeliui su talpa {puodelio_talpa}ml'
#         else:
#             return  f'{self.pavadinimas} kava netelpa {puodelio_talpa}ml'
#
# kava1=Kava('Latte', 2.99, 250)
# puodelio_talpa=200
# print(kava1.ar_tinkama_puodeliui(puodelio_talpa))

# sukurti klase knygynas. savybes: knygos kaip sarasas.
# prideti i sarasa knygu, ieskoti ir atspausdinti visu knygu sarasa.

# class Knygynas:
#     def __init__(self):
#         self.knygos = []
#
#     def prideti_knyga(self, knyga):
#         self.knygos.append(knyga)
#
#     def knygos_paieska(self, pavadinimas):
#         for knyga in self.knygos:
#             if knyga['pavadinimas']== pavadinimas:
#                 return knyga
#
#         return None
#
#     def knygu_sarasas(self):
#         if not self.knygos:
#             print("Knygynas tuscias")
#         else:
#             print("Knygyno knygu sarasas":)
#
#             for knyga in self.knygos:
#                 print(f"Pavadinimas:{knyga['pavadinimas']}, Autorius: {knyga['autorius']}, Metai: {knyga['metai'"]}")
#
# knygynas = Knygynas()
# knygynas.prideti_knyga({'pavadinimas': 'seslis', 'autorius': 'Zemaitis', 'metai':  1981})
# ieskoma_knyga = knygynas.knygos_paieska('seslis')
# if ieskoma_knyga:
#     print(f'rasta knyga:'{ieskoma_knyga["pavadinimas"]}')
# else:
#     print("knyga nerasta")
#     knygynas.knygu_sarasas()

# GERAS VARIANTAS:

# class Knigynas:
#     def __init__(self):
#         self.knygos = []
#     def prideti_knyga(self,knyga):
#         self.knygos.append(knyga)
#
#     def knygos_paieska(self,pavadinimas):
#         for knyga in self.knygos:
#             if knyga['pavadinimas']== pavadinimas:
#                 return knyga
#         return None
#
#     def knygu_sarasas(self):
#         if not self.knygos:
#             print("Knigynas tuscias")
#         else:
#             print('Knigyno knygu sarasas:')
#             for knyga in self.knygos:
#                 print(f"Pavadinimas: {knyga['pavadinimas']}, Autorius: {knyga['autorius']}, Metai: {knyga['metai']}")
#
# knigynas = Knigynas()
# knigynas.prideti_knyga({'pavadinimas': 'seslis', 'autorius': 'Zemaitis', 'metai': 1981})
# knigynas.prideti_knyga({'pavadinimas': 'soslis', 'autorius': 'femaitis', 'metai': 1881})
# ieskoma_knyga = knigynas.knygos_paieska('suslis')
# if ieskoma_knyga:
#     print(f'rasta knyga: {ieskoma_knyga["pavadinimas"]}')
# else:
#     print("knyga nerasta")
# knigynas.knygu_sarasas()
#
# # React
# #
# # Reply
#
#
# Sukurkite klasę "Prekybininkas", kuri turi atributus "vardas" (name) ir "prekės" (items) ( prekių sąrašas).
# Parašykite metodus,
# kurie leidžia pridėti prekes prie prekių sąrašo, pašalinti prekes ir paskaičiuoti prekių bendrą sumą;
#
#
# class Prekybininkas:
#     def __init__(self, name):
#         self.name = name
#         self.prekes = []
#
#     def prideti_preke(self, preke, kiekis=1):
#                 for _ in range(kiekis):
#                     self.prekes.append(preke)
#
#         # for , if NAUDOTI
#     def pasalinti_preke(self, preke, kiekis=1):
#         if preke in self.prekes:
#             for _ in range (kiekis):
#                 self.prekes.remove[preke]
#         else:
#             print("tokios prekes nera")
#
#     def bendra_suma(self):
#         suma=sum(preke[1] for preke in self.prekes)
#         return suma
#
# prekybininkas1 = Prekybininkas("Antanas")
# preke1=("Makaronai, 1.0")
# preke2=("brokolis", 2.5)
# preke3=("sultys", 1.5)
#
# prekybininkas1.prideti_preke(preke1, 10)
# prekybininkas1.prideti_preke(preke2, 5)
# prekybininkas1.prideti_preke(preke3, 3)
# suma=prekybininkas1.bendra_suma()
#
# print(suma)
#
# prekybininkas1.pasalinti_preke(preke1, 3)
# prekybininkas1.pasalinti_preke(preke2, 2)
# prekybininkas1.pasalinti_preke(preke3, 1)
#
# print("prekiu sarasas: ")
# for preke in prekybininkas1.prekes:
#     print(f"{preke[0]}: {preke[1]}")
# print(f"bendra visu prekiu suma:{suma}")

#
# class Prekybininkas:
#     def __init__(self, name):
#         self.name = name
#         self.prekes = []
#     def prideti_preke(self, preke, kiekis=1):
#         for _ in range(kiekis):
#             self.prekes.append(preke)
#     def pasalinti_preke(self, preke, kiekis=1):
#         if preke in self.prekes:
#            for _ in range(kiekis):
#                self.prekes.remove(preke)
#         else:
#             print("tokios prekes nera")
#
#     def prekiu_suma(self):
#         suma=sum(preke[1] for preke in self.prekes)
#         return suma
#
#
# pardavejas=Prekybininkas("Martynas")
# preke1=("kava", 1.0)
# preke2=("sultys", 2.5)
# preke3=("alus", 1.5)
#
# pardavejas.prideti_preke(preke1, 3)
# pardavejas.prideti_preke(preke2)
# pardavejas.prideti_preke(preke3,3)
# suma=pardavejas.prekiu_suma()
#
# print(suma)
#
# pardavejas.pasalinti_preke(preke1, 2)
# pardavejas.pasalinti_preke("preke4")
# suma=pardavejas.prekiu_suma()
#
# print("prekiu sarasas: ")
# for preke in pardavejas.prekes:
#     print(f"{preke[0]}: {preke[1]}")
# print(f"bendra visu prekiu suma:{suma}")
#

# class Darbuotojas:
#     def __init__(self, vardas, pareigos, alga):
#         self.vardas = vardas
#         self.pareigos = pareigos
#         self.alga = alga
#     def pakeisti_alga(self, nauja_alga):
#         self.alga = nauja_alga
#     def pakeisti_pareigas(self, naujos_pareigos):
#         self.pareigos = naujos_pareigos
#
#
# #
# darbuotojas1=Darbuotojas("Jonas", "vairuotojas", 500)
# darbuotojas1.pakeisti_alga(1500)
# darbuotojas1.pakeisti_pareigas("vadybininkas")
#
# print(f"{darbuotojas1.vardas}, pareigos: {darbuotojas1.pareigos}, gaunama alga:{darbuotojas1.alga}")
# Sukurkite klasę "Darbuotojas" (Employee), kuri turi atributus "vardas" (name), "pareigos" (position),
# ir "atlyginimas" (salary). Parašykite metodus, kurie leidžia keisti darbuotojo pareigas ir atlyginimą;
#
# class Darbuotojas:
#     def __init__(self, vardas, pareigos, atlyginimas):
#         self.vardas = vardas
#         self.pareigos = pareigos
#         self.atlyginimas = atlyginimas
#
#     def keisti_pareigas(self, naujos_pareigos):
#         self.pareigos = naujos_pareigos
#
#     def keisti_DU(self, new_DU):
#         self.atlyginimas = new_DU
#
#
# darbuotojas1 = Darbuotojas("Rasa", "Finansininke", 3500)
#
# darbuotojas1.keisti_pareigas("Direktorius")
# darbuotojas1.keisti_DU(5000)
#
# print(f'darbuotojo vardas: {darbuotojas1.vardas}, pareigos: {darbuotojas1.pareigos}, DU: {darbuotojas1.atlyginimas}')
#
# print(f"{darbuotojas1.vardas}, pareigos: {darbuotojas1.keisti_pareigas}, DU: {darbuotojas1.keisti_DU}")

# skaiciuotuvas:

# class Skaiciuotuvas:
#     def add(self, a, b):
#         return a+b
#     def subtract(self, a, b):
#         return a-b
#     def multiply(self, a, b):
#         return a*b
#     def divide(self,a, b):
#         if b ==0:
#             return "dalyba is nulio negalima"
#         else:
#             return a/b
# a=3
# b=2
# a1=Skaiciuotuvas()
# suma=a1.add(a,b)
# skirtumas=a1.subtract(a,b)
# dalyba=a1.multiply(a,b)
# daugyba=a1.divide(a,b)
#
# print(f"{suma}, {skirtumas}, {dalyba}, {daugyba}")



# Objektinis
# Programavimas
# Python
#
#
# class ManoKlase:
#     # kuriame konstruktoriu
#     def __init__(self, savybe1, savybe2):
#         # apibreziame savybes
#         self.savybe1 = savybe1
#         self.savybe2 = savybe2
#
#     # Toliau kuriame metodus, kurie atliks tam tikrus veiksmus
#
#     def metodas_1(self, argumentas):
#         # metodo kodas
#         pass
#
#
# Po
# viso
# to
# kai
# musu
# klase
# yra
# sukurta
# ir
# metodai
# aprasyti
# galime
# pereiti
# prie
# objekto
# kurimo
# ir
# metodo
# panaudojimo;
# # objekto kurimas
# objektas1 = ManoKlase("savybe1_reiksme", "savybe2_reiksme")
#
# # naudojame savo metoda kartu su savo objektu
# # kadangi musu metodas turi papildoma argumenta, mes privalome kviesdami metoda jo viduje parasyti atitinkama reiksme;
# objektas1.metodas_1("argumento_reiksme")
# Tikiuosi
# jog
# dabar
# bus
# aiskiau
# svarbiausia
# sekti
# kas
# ir
# kur
# yra
# rasoma, nes
# kitu
# atveju
# padarysite
# klaidu *Objektinis Programavimas Python
# class ManoKlase:
#     # kuriame konstruktoriu
#     def __init__(self, savybe1, savybe2):
#         # apibreziame savybes
#         self.savybe1 = savybe1
#         self.savybe2 = savybe2
#
#     #Toliau kuriame metodus, kurie atliks tam tikrus veiksmus
#
#     def metodas_1(self, argumentas):
#         # metodo kodas
#         pass
# Po viso to kai musu klase yra sukurta ir metodai aprasyti galime pereiti prie objekto kurimo ir metodo panaudojimo;
# # objekto kurimas
# objektas1 = ManoKlase("savybe1_reiksme", "savybe2_reiksme")
#
# # naudojame savo metoda kartu su savo objektu
# # kadangi musu metodas turi papildoma argumenta, mes privalome kviesdami metoda jo viduje parasyti atitinkama reiksme;
# objektas1.metodas_1("argumento_reiksme")
# Tikiuosi jog dabar bus aiskiau svarbiausia sekti kas ir kur yra rasoma, nes kitu atveju padarysite klaidu *

# Sukurkite klasę "Klase", kuri turės savybę "pavadinimas" ir sąrašą "pamokos" (pamokų pavadinimai ir laikas).
# Sukurkite klasę "Mokykla", kuri turės sąrašą klasių.
# Parašykite metodą, kuris išveda mokyklos tvarkaraštį su visomis pamokomis.
# blogas
# class Klase:
#     def __init__(self, pavadinimas):
#         self.pavadinimas = pavadinimas
#         self.pamokos = []
#
#     def suvesti_pamokas(self, pavadinimas, laikas):
#         self.pamokos.append((pavadinimas, laikas))
#
#     def suvesti_tvarkarasti(self):
#         tvarkarastis = f"Klase: {self.pavadinimas}\n"
#         for pamoka in self.pamokos:
#             pavadinimas, laikas = pamoka
#             tvarkarastis+=f"-{pavadinimas}, laikas: {laikas} \n"
#         return tvarkarastis
# class Mokykla:
#     def __init__(self, pavadinimas):
#         self.pavadinimas = pavadinimas
#         self.klases = []
#
#     def suvesti_klase(self, klase):
#         self.klases.append(klase)
#
#     def tvarkarastis_galutinis(self):
#         galutinis = f"Mokykla: {self.pavadinimas} \n"
#         for klase in self.klases:
#             galutinis +=klase.tvarkarastis()
#         return galutinis
#
#
#
#
# mokykla = Mokykla("Tinginiu pantys")
#
# klase1 = Klase("8", [("Anglu", 9:00), ("Matematika", 9:50)])
# klase1.sukurti_pamoka()
# klase2 = Klase("9", [("Biologija", 9:00), ("Lietuviu", 9:50)])
#
# mokykla.sukurti_klase(klase1)
# mokykla.sukurti_klase(klase2)
# tvarkarastis = mokykla.tvarkarastis_galutinis()
#

# geras variantas Eugenijus
#
# class Klase:
#     def __init__(self, pavadinimas):
#         self.pavadinimas = pavadinimas
#         self.pamokos = []
#
#     def sukurti_pamoka(self, pavadinimas, laikas):
#         self.pamokos.append((pavadinimas, laikas))
#
#     def tvarkarastis(self):
#         tvarkarastis = f"Klase: {self.pavadinimas} \n"
#         for pamoka in self.pamokos:
#             pavadinimas, laikas = pamoka
#             tvarkarastis += f"- {pavadinimas}, laikas: {laikas} \n"
#         return tvarkarastis
#
# class Mokykla:
#     def __init__(self, pavadinimas):
#         self.pavadinimas = pavadinimas
#         self.klases = []
#
#     def sukurti_klase(self, klase):
#         self.klases.append(klase)
#
#     def Tvarkarastis_galutinis(self):
#         galutinis = f"Mokykla: {self.pavadinimas} \n"
#         for klase in self.klases:
#             galutinis += klase.tvarkarastis()
#         return galutinis
#
#
#
# klase1 = Klase("Ziopliu 9A")
# klase1.sukurti_pamoka("Nosiakrap6tis", "8:00-8:45")
# klase1.sukurti_pamoka("Kalbagrauzis", "9:00-9:45")
#
# klase2 = Klase("Smalsučiai gudručiai 1B")
# klase2.sukurti_pamoka("Priešpiečiai", "10:00-10:45")
# klase2.sukurti_pamoka("Kalbagrauzis", "11:00-11:45")
#
# mokykla =Mokykla("Tinginių pantys")
#
# mokykla.sukurti_klase(klase1)
# mokykla.sukurti_klase(klase2)
#
# tvarkarastis = mokykla.Tvarkarastis_galutinis()
#
# print(mokykla.Tvarkarastis_galutinis())

# Sukurkite klasę "Žaislas", kuri turėtų savybes, tokias kaip "pavadinimas" ir "amžiaus rekomendacija".
# Tada sukurkite klasę "Vaikas", kuri turėtų vardą ir amžių. Tada sukurkite klasę "VaikasSuZaislu",
# kuri turėtų šio vaiko objektą ir žaislo objektą.
# Patikrinkite, ar vaiko amžius atitinka žaislo amžiaus rekomendaciją.
#
# class Zaislas:
#     def __init__(self, pavadinimas, amziaus_rekomendacija):
#         self.pavadinimas = pavadinimas
#         self.amziaus_rekomendacija = amziaus_rekomendacija
#
# class Vaikas:
#     def __init__(self, vardas, amzius):
#         self.vardas = vardas
#         self.amzius = amzius
#
# class Vaikassuzaislu:
#     def __init__(self, vaikas, zaislas):
#         self.vaikas = vaikas
#         self.zaislas = zaislas
#
#     def ar_atitinka_rekomendacija(self):
#         return self.vaikas.amzius >= self.zaislas.amziaus_rekomendacija
#
# zaislas1 = Zaislas("Monopolis", 15)
# vaikas1 = Vaikas("Jonas", 16)
#
# vaikas_su_zaislu = Vaikassuzaislu(vaikas1, zaislas1)
#
# if vaikas_su_zaislu.ar_atitinka_rekomendacija():
#     print(f"{vaikas1.vardas} atitinka amziaus rekomendacija zaislui {zaislas1.pavadinimas} ")

# NEGERAS
# class Vaikas:
#     def __init__(self, vardas, amzius):
#         self.vardas = vardas
#         self.amzius = amzius
#
# class Vaikassuzaislu:
#     def __init__(self, vaikas, zaislas):
#         self.vaikas = vaikas
#         self.zaislas = zaislas
#
#     def ar_atitinka_rekomendacija(self):
#         if self.vaikas.amzius >=self.zaislas.amziaus_rekomendacija:
#             return f'{self.vaikas.vardas} gali zaisti su zaislu "{self.zaislas.pavadinimas}" '
#         else:
#             return f'{self.vaikas.vardas} negali zaisti su zaislu: "{self.zaislas.pavadinimas}, del amziaus apribojimo" '
#
# zaislas1 = Zaislas("Monopolis", 15)
# vaikas1 = Vaikas("Jonas", 16)
#
# vaikas_su_zaislu = Vaikassuzaislu(vaikas1, zaislas1)
#
# rezultatas = vaikas_su_zaislu.amziaus_tikrinimas
#
# print(rezultatas)

# GERAS
# class Zaislas:
#     def __init__(self,pavadinimas, amziaus_rekomendacija):
#         self.pavadinimas = pavadinimas
#         self.amziaus_rekomendacija = amziaus_rekomendacija
#
# class Vaikas:
#     def __init__(self, vardas, amzius):
#         self.vardas = vardas
#         self.amzius =amzius
#
# class VaikasSuZaislu:
#     def __init__(self,vaikas, zaislas):
#         self.vaikas = vaikas
#         self.zaislas = zaislas
#     def amziaus_tikrinimas(self):
#         if self.vaikas.amzius >=self.zaislas.amziaus_rekomendacija:
#             return f'{self.vaikas.vardas} gali zaisti su zaislu "{self.zaislas.pavadinimas}" '
#         else:
#             return f'{self.vaikas.vardas} negali zaisti su zaislu "{self.zaislas.pavadinimas}", nes turi paaugti '
#
#
# zaislas1=Zaislas('Lego Betmen', 7)
# zaislas2=Zaislas('burbulai', 15)
# zaislas3=Zaislas('knyga', 8)
#
# vaikas1=Vaikas('Austeja',9)
# vaikas2=Vaikas('Eidvile', 0.5)
# vaikas3=Vaikas('Giedrius', 5)
#
# vaikas_su_zaislu1=VaikasSuZaislu(vaikas1, zaislas2)
#
# rezultatas = vaikas_su_zaislu1.amziaus_tikrinimas()
# print(rezultatas)
#

# Sukurkite programą, kuri leidžia vartotojui valdyti krepšinio komandą.
# Galite kurti klases, pvz., "Komanda", "Žaidėjas", "Treneris".
# Kiekvienas žaidėjas turėtų turėti savo statistiką(taiklumas,pozicija),
# o treneris - instrukcijas ir strategiją(komandos sudeti).
# Programa turi leisti vartotojui pridėti naujus žaidėjus,
# juos treniruoti ir valdyti komandos sudeti.
#
# class Treneris:
#     def __init__(self):
#         self.strategija = "ataka"
#     def keisti_strategija(self,nauja_strategija):
#         self.strategija = nauja_strategija
#
#     def strategijos_info(self):
#         return f'naudojama strategija {self.strategija}'
# class Zaidejas:
#     def __init__(self, pavarde, pozicija):
#         self.pavarde = pavarde
#         self.taiklumas = 30
#         self.pozicija = pozicija
#
#     def upgrade(self):
#         self.taiklumas += 5
#         if self.taiklumas > 100:
#             self.taiklumas = 100
#
#     def zaidejo_info(self):
#         return f'{self.pavarde}, zaidejo pozicija {self.pozicija}, ir jo taiklumas {self.taiklumas}%'
# class Komanda:
#     def __init__(self, pavadinimas):
#         self.komanda =[]
#         self.pavadinimas = pavadinimas
#         self.treneris = Treneris()
#     def prideti_zaideja(self,zaidejas):
#         self.komanda.append(zaidejas)
#
#     def isimti_zaideja(self, zaidejas):
#         if zaidejas in self.komanda:
#             self.komanda.remove(zaidejas)
#     def komandos_informacija(self):
#         print(f'{self.pavadinimas}, komandos zaidejai: ')
#         for zaidejas in self.komanda:
#             print(zaidejas.zaidejo_info())
#     def strategijos_info(self):
#         print (self.treneris.strategijos_info())
#
#     def pasirinkti_treneri(self, treneris):
#         self.komanda.append(treneris)
#
#     def pakeisti_treneri(self, treneris):
#         if treneris in self.komanda:
#             self.komanda.remove(treneris)
#
# komanda=Komanda("Puseles")
# zaidejas1=Zaidejas("Greitas", "puolejas")
# zaidejas2=Zaidejas("didelis", "saugas")
# zaidejas3=Zaidejas("vidutinis", "atsarginis")
#
# komanda.prideti_zaideja(zaidejas1)
# komanda.prideti_zaideja(zaidejas2)
# komanda.prideti_zaideja(zaidejas3)
#
# zaidejas1.upgrade()
# zaidejas1.upgrade()
# zaidejas3.upgrade()
#
# komanda.komandos_informacija()
# komanda.strategijos_info()

# DUOMENU ANALITIKOS IVADAS
# importuojame bibliotekas

import pandas as pd
# "sukuriame sarasa su duomenimis
#
# duomenys = {'vardas': ['Jonas', 'Ieva', 'Petras', 'Ona'],
#             'Amzius': [25, 28, 22, 30]}

# # "sukuriame DataFrame is saraso
#
# df = pd.DataFrame(duomenys)
# print(df)
#
# # filtruoti duomenis pagal amziu
#
# jaunesni = df[df['Amzius'] <25]
# print(jaunesni)
#
# #  skaiciuokite vidutini amziu
# vidutinis_amzius = df['Amzius'].mean()
# print(f"Vidutinis amzius: {vidutinis_amzius}")

# temperaturos = [24.5, 25.2, 23.8, 26.0, 22.5]
# sr = pd.Series(temperaturos)
# print(sr)

# temperaturos = [24.5, 25.2, 23.8, 26.0, 22.5]
# sr = pd.Series(temperaturos)
# serija_rikiavimas = sr.sort_values()
# print(serija_rikiavimas)

# temperaturos = [24.5, 25.2, 23.8, 26.0, 22.5]
# sr = pd.Series(temperaturos)
# serija_rikiavimas = sr.sort_values(ascending=False)
# print(serija_rikiavimas)
#
# temperaturos = [24.5, 25.2, 23.8, 26.0, 22.5]
# sr = pd.Series(temperaturos)
# print(f"pirmas elementas: {sr[0]}")

# kazkas negerai

# duomenys = {'vardas': ['Jonas', 'Ieva', 'Petras', 'Ona'],
#             'Amzius': [25, 28, 22, 30]}
#
# df = pd.DataFrame(duomenys)
# vardai = df['Vardas']
# print("Vardai:")
# print(vardai)
#
# duomenys = {'vardas': ['Jonas', 'Ieva', 'Petras', 'Ona'],
#             'Amzius': [25, 28, 22, 30]}
# df = pd.DataFrame(duomenys)
# #
# df['Lytis'] = ['Vyras', 'Moteris', 'Vyras', 'Moteris']
# print('Atnaujintas dataframe su nauju stulpeliu: ')
# print(df)
#
# import matplotlib.pyplot as plt
# #nurodome asies dydi
# plt.figure(figsize=(8,5))
# plt.bar(df['vardas'], df['Amzius'], color='green')
# plt.xlabel('Vardas')
# plt.ylabel('Amzius')
# plt.title('Amzius pagal vardus')
#
# plt.show()

#pridedame nauja stulpeli savo DataFrame

# df.to_excel('duomenys.xlsx', index=False, engine='openpyxl')
#
# duomenys = {'vardas': ['Jonas', 'Ieva', 'Petras', 'Ona'],
#             'Amzius': [25, 28, 22, 30]}
# df = pd.DataFrame(duomenys)
# #
# df['Lytis'] = ['Vyras', 'Moteris', 'Vyras', 'Moteris']
# print('Atnaujintas dataframe su nauju stulpeliu: ')
# print(df)
# #
# #head # atvaizduoja eiluciu skaiciu (pirmos eilutes)
# df.head()
# # tail - paskutines eilutes
# # df.tail(1)

# data = {'Miestas': ['Vilnius', 'Kaunas', 'Kaunas', 'Vilnius'],
#         'Lytis': ['Vyras', 'Vyras', 'Moteris', 'Vyras'],
#         'Amzius': [25,25,2,30]
#         }
# data1 = pd.DataFrame(data)
# vidutinis_amzius_pagal_miesta = data1.groupby('Miestas') ['Amzius'].mean()
# print(vidutinis_amzius_pagal_miesta)

# data = {
#         'Miestas': ['Vilnius', 'Kaunas', 'Kaunas', 'Vilnius'],
#         'Lytis': ['Vyras', 'Vyras', 'Moteris', 'Vyras'],
#         'Amzius': [25,25,2,30,24]
#         }
# data1 = pd.DataFrame(data)
#
# vidutinis_amzius_pagal_miesta = data1.groupby('Miestas') ['Amzius'].sum()
# print(vidutinis_amzius_pagal_miesta)

# data = {'Miestas': ['Vilnius', 'Kaunas', 'Kaunas', 'Vilnius'],
#         'Lytis': ['Vyras', 'Vyras', 'Moters', 'Vyras'],
#         'Amzius': [25,25,22,30]
#         }
# data1 = pd.DataFrame(data)
# vid_amzius_pagal_miesta = data1.groupby('Miestas') ['Amzius'].mean()
# print(vid_amzius_pagal_miesta)

# Sukurkite Pandas DataFrame(4 miestai ir ju populiacija).
#
# Filtravimas ir paieška:
#
# a. Filtruokite miestus, kurių populiacija yra didesnė nei 200 000 žmonių.
#
# b. Raskite miestą, turintį mažiausią populiaciją.

# data = {'Miestas': ['Vilnius', 'Kaunas', 'Klaipeda', 'Siauliai', 'Panevezys'],
#         'Populiacija': [546155, 298753, 152008, 100653, 89110]}
#
# df = pd.DataFrame(data)
# skaitlingiausi_miestai = df[df['Populiacija'] > 200000]
# print(skaitlingiausi_miestai)
#
# min_miestas = df[df['Populiacija']==df['Populiacija'].min()]
# print(min_miestas)

# Duomenų grupavimas ir agregavimas:
#
# a. Pridėkite stulpelį "Šalis" prie ankstesnio DataFrame, kuriame nurodoma,
# kuri šalis priklauso kiekvienam miestui (pvz., "Lietuva").
#
# b. Grupuokite duomenis pagal "Šalis" stulpelį ir apskaičiuokite
# bendrą populiaciją kiekvienai šaliai.
#
# Duomenų rikiavimas:
#
# Rikiuokite miestus pagal populiaciją mažėjimo tvarka.

# df['Salis'] = 'Lietuva'
# print('Atnaujintas dataframe su salimi: ')
# print(df)
#
# bendra_populiacija = df.groupby('Salis')['Populiacija'].sum()
# print(bendra_populiacija)
#
# miestai_pagal_populiacija = df.sort_values('Populiacija', ascending=False)
# print(miestai_pagal_populiacija)
#
# df = df[df['Miestas']!= 'Siauliai']
# print(df)
# df.loc[df['Miestas'] == 'Kaunas', 'Populiacija'] = 300000
# print(df)


# duomenys = {'Miestas': ['Vilnius', 'Kaunas', 'Klaipeda', 'Plunge'],
#             'Populiacija': [500000, 295000, 152000, 33665]
#             }
# df = pd.DataFrame(duomenys)
# miestai = df['Miestas']
# populiacija = df['Populiacija']
#
# populiacijos_filtravimas = df[df['Populiacija'] > 200000]
# print(populiacijos_filtravimas)
# print(df.min())


# df['Salis'] = ['Lietuva', 'Lietuva', 'Italija', 'Lietuva']
#
# print('Atnaujintas dataframe dsu nauju stulpeliu: ')
# print(df)
#
# Grupavimas = df.groupby('Salis')['Populiacija'].sum()
# print(Grupavimas)
# mazejancia_tvarka = df.sort_values(by='Populiacija')
#
#
# plt.figure(figsize=(8,5))
# plt.bar(df['Miestas'], df['Populiacija'], color='mediumturquoise')
# plt.xlabel('Miestas')
# plt.ylabel('Populiacija')
# plt.title('Populiacija pagal miestu pavadinimus')
# plt.show()


# csv_failo_pavadinimas = 'data-table.csv'
# df = pd.read_csv(csv_failo_pavadinimas)
# print(df.head(5))




