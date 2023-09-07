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

