## -*- coding: windows-1251 -*-

alph = ['АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя ']
def encoder(tex, key, a, b):
    num = 1
    f = 0
    i = 0
    j = 0
    numb = 0
    stroka = tex
    result = ''
    sch = 0
    size = len(tex)
    while(size > a*b):
        num +=1
        size -= a*b
    for numb in range(num):
        if(len(tex) - sch < a*b):
            sr = len(tex) - sch
            stroka = tex[sch:sch+sr:1]
        else:
            stroka = tex[sch:sch+a*b:1]

        p = len(text)//len(key)

        mas = [[0 for x in range(b)] for y in range(a)]

        i = 0
        j = 0

        for x in stroka:
            mas[i][j] = x

            j = j+1
            if j%len(key) == 0:
                j=0
                i=i+1

        for numb in key:
        
            for i in range(a):
                if(mas[i][int(numb)-1] != 0):
                    result = result + mas[i][int(numb)-1]

        sch +=a*b
    return(result)
        

def decoder(tex, key, a, b):
    num = 1
    f = 0
    i = 0
    j = 0
    numb = 0
    stroka = tex
    res = ''
    rеs = tex
    sch = 0
    size = len(tex)
    while(size > a*b):
        num +=1
        size -= a*b
    
    for numb in range(num):
        if(len(tex) - sch < a*b):
            sr = len(tex) - sch
            stroka = tex[sch:sch+sr:1]
        else:
            stroka = tex[sch:sch+a*b:1]

        p = len(text)//len(key)

        mas = [[0 for x in range(b)] for y in range(a)]
        mas1 = [[0 for x in range(b)] for y in range(a)]
    
        for x in stroka:
            mas[i][j] = x
            j = j+1
            if j%len(key) == 0:
                j=0
                i=i+1

        rev_key = key[::-1]

        i = 0

        for numb in key:
                j = 0
                while j < b:
                    mas1[1][int(numb)-1] = mas[1][1]
                    j +=1
                i+=1
   
        sch +=a*b
        i = 0
        j = 0
        for i in range(a):
            for j in range(b):
                if(mas1[i][j] != 0):
                    res = res + mas1[i][j]
                    

        #res = res.join(ele for sub in mas1 for ele in sub)
        i = 0
        j = 0
    

    return(rеs)
     


text = input ("Текст для шифрования: ")

a = int(input("Введите количество строк таблицы:"))

b = int(input("Введите количество столбцов таблицы:"))


k = input("Введите ключ шифрования: ")

result = ''
res = ''

result = encoder(text, k, a, b)

print("Зашифрованное сообщение: ", result)

res = decoder(text, k, a, b)
print("Расшифрованное сообщение: ", res)
