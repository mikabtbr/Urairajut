def urai(kata):                                 # membuat fungsi urai dengan parameter kata
    for i in range(len(kata)):                  # membuat loop dengan range panjang dari parameter kata
        for j in range(i):                      # membuat loop dalam loop dengan range i
            print(kata[j],end='')               # print hasil sesuai dengan index  dan memisahkan antar hasil loop dengan ''.
    return kata                                 # memanggil fungsi rajut
# iterasi pertama yaitu : saat i di range 0 kondisi belum berjalan karna j pada range i=0
# iterasi kedua : saat i =1 , maka j = 0 (range(1)), print index 0 pada kata >'C'
# iterasi ketiga : saat i =2 dan j = 0, print index ke 0 lagi, yaitu 'C'
# iterasi keempat : saat i =2 dan j =1 , print index ke 1 , yaitu 'o' >> CCo
# dan seterusnya

print(urai('Code'))
print(urai('Python'))
print(urai('Purwadhika'))


def rajut(words):                            # membuat fungsi dengan nama rajut dengan parameter words
    first = words[0]                         # buat variabel dengan assign sebagai huruf pertama dari words
    new = words.split(first)                 # kemudian membuat variabel baru dengan nama new, konversi ke list baru dengan memisahkan string pada parameter words, terhadap huruf pertama
    result = first + new[-1]                 # membuat variabel baru dengan nama result, dengan menggabungkan huruf pertama + words di index terakhir pada list
    return result                            # memanggil fungsi rajut


print(rajut('CCoCodCode'))  #CCoCodCode >> akan di split menjadi ['', '', 'o', 'od', 'ode', 'ode'], sehingga di index[::-1] adalah kata 'ode'.
# huruf pertama + index terakhir pada list = C + ode = Code
print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))