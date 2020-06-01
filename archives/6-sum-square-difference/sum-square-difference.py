def sum_square(n):
    a = 0
    b = 0
    for i in range(1,n+1):
        a += i**2
        b += i
    return a,b

def solver(n):
    a,b = sum_square(n)
    b = b ** 2
    return b-a

if __name__ == '__main__':
    hasil = solver(100)
    print("Jawaban : {hasil}".format(hasil=hasil))