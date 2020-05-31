def fibbonanci(n):
    pertama = 1
    kedua = 2

    if n == 1 :
        return pertama
    elif n == 2 :
        return kedua
    elif n > 2 :
        temp = 0
        for i in range(n-2):
            temp = pertama + kedua
            pertama = kedua
            kedua = temp
        return temp

def solver():
    i = 1
    total = 0
    while(fibbonanci(i)<4000000):
        temp = fibbonanci(i)
        if temp % 2 == 0 :
            total += temp
        i+=1
    return total

if __name__ == '__main__':
    hasil = solver()
    print("Jawaban : %d" % hasil)