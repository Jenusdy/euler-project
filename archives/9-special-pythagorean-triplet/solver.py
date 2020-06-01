def solver(n):
    for a in range(1,1000):
        for b in range(a,1000):
            c = 1000 - a - b
            if a < b and b < c and a**2 + b**2 == c**2:
                return a*b*c

if __name__ == '__main__':
    hasil = solver(1000)
    print("Jawaban : {hasil}".format(hasil=hasil))