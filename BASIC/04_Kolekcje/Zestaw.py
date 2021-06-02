# 1.  Utwórz dowolną krotkę, w której elementy mogą się powtarzać. Przekształć ją w set.
kr_tuple = ('dasdsa', 'asdsad', 'asdsa', 'asdsa')
print(set(kr_tuple))

# 2. Utwórz listę L_test = [1, 2, 3, 4], krotkę T_test = (1, 2, 3, 4) oraz set S_test = {1, 2, 3, 4}.
# Jakie metody dostępne dla typu list nie będą działać dla typów tuple i set?
L_test = [1, 2, 3, 4]  # ze sprawdzonych metod dla list działają wszystkie jak poniżej.
print(L_test)

L_test.append(2)
print(L_test)
L_test.extend("5")
print(L_test)
L_test.insert(5, 6)
print(L_test)
L_test.remove(1)
print(L_test)
print(L_test.index(3))
print(L_test.count(2))
print(L_test.pop())
L_test.reverse()
print(L_test)

print('*'*20)

T_test = (1, 2, 3, 4)  # ze sprawdzonych metod dla listy, w przypadku krotki działają metody jak poniżej.
print(T_test)

print(T_test.index(3))
print(T_test.count(2))

print('*'*20)

S_test = {1, 2, 3, 4}  # ze sprawdzonych metod dla listy, w przypadku set'u działają metody jak poniżej.
print(S_test)

S_test.remove(1)
print(S_test)
print(S_test.pop())

# 3. Utwórz 2 krotki. Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z pierwszej krotki,
# a oraz nieparzystych elementów z drugiej. Przekształć powstałą listę w set.
tuple1 = ('aaaaa', 'bbbbb', 'ccccc', 'ddddd')
tuple2 = ('aaaaa', 'f', 'ccccc', 'p')
list1 = list(tuple1[0::2])
list2 = list(tuple2[1::2])
set_all = set(list1 + list2)
print(set_all)

# 4. Napisz skrypt, który podaną listę podzieli na 3 równe listy i odwraca każdą z tych.
fulllist = input('Wpisz kilka pozycji listy rozdielonych przecinkiem:')
fulllist = fulllist.split(',')
listlong = len(fulllist)
partlong = len(fulllist)//3
part1 = fulllist[0:partlong]
part2 = fulllist[partlong:partlong*2]
part3 = fulllist[partlong*2:listlong]
part1.reverse()
part2.reverse()
part3.reverse()

print(part1, part2, part3)

# 5. Porównaj zachowanie discard() vs remove() dla typu set.
S_test = {1, 2, 3, 4}
S_test.discard(0)
print(S_test)

S_test.remove(0)
print(S_test)

# różnica polega na tym że jeśli spróbojemy usunąć element set'u który w nim nie występuje za pomocą funcji discard
# to nic się nie stanie a przy metodzie remove wyskoczy błąd.
