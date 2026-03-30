# lists
# num = [x for x in range(50)] list comprehension liste elemanlarını loopla yazdırdık
num = [1, 2, 3, 4]
num.append(5)
num.insert(5, 6) # bu 5.indekse 6 yı ekle demek yani num[5] 6. elemanı 6 yap diyor
num[len(num):] = [7]   
# python da listeler list[başlangıç:bitiş] şeklinde olur burda da eleman sayısı kadar indeks gelip en son terime  7 ekledik
for number in num:
    print(number)