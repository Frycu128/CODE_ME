# 1.   Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny.
# Załóżmy, że spalanie na 100km wynosi 6,4 l, trasa to 120km, litr benzyny kosztuje 5,04 zł.
mileage_per_100 = float(6.4)
distance = int(120)
cost = float(5.04)
print()
fuel = float((distance*mileage_per_100)/100)
print('Koszty wyprawy wyniosły ' , round(fuel*cost,2) , 'zł')
print('*'*100)
print()

# 2.	Zmodyfikuj skrypt tak, by przyjmował wartości od użytkownika.
distance = float(input('Jaki pokonano dystans? '))
mileage_per_100 = float(input('Jakie było średnie spalanie na 100 km? '))
cost = float(input('Jaką cene za jeden litr paliwa przyjąć do obliczeń? '))
fuel = float((distance*mileage_per_100)/100)
print('Koszty wyprawy wyniosły' , round(fuel*cost,2) , 'zł')
print('*'*100)
print()
