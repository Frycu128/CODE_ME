print("Moje BMI wynosi około", 62//(1.8*1.8))

# BMI = (masa (kg)) / (wzrost (m))²
waga = 62
wzrost = 1.8
BMI = waga / (wzrost ** 2)
BMI_rounded = round(BMI, 2)
print('Moje BMI =', BMI_rounded)

waga = int(input('Jaka jest Twoja waga [kg]'))
wzrost = float(input('Jaki jest Twój wzrost [m]'))

BMI = int(waga/(wzrost**2))
print('Moje BMI=', BMI)

if 12 <= BMI <= 18.5:
    print('Masz niedowagę.')
elif 30 > BMI >= 25:
    print('Masz nadwagę.')
elif 25 > BMI > 18.5:
    print('BMI w normie')
elif BMI >= 30:
    print('To już otyłość..')
else:
    print('Nie żyjesz albo masz same kości :P')
