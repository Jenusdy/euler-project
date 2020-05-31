def solver():
    n = 19*2
    while(True):
        counter = 0
        for i in range(1,20+1):
            if n % i == 0:
                counter += 1
        if counter == 20 :
            return n
            break
        else :
            n += 19 # Mempercepat proses, kelipatan bilangan prima terbesar

if __name__ == '__main__':
    hasil = solver()
    print("Jawaban : {hasil}".format(hasil=hasil))