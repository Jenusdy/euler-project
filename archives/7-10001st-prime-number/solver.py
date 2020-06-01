def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solver(n):
    awal = 2
    prima = 0
    while True:
        if is_prime(awal):
            prima+=1
        if prima == n :
            print("Jawaban : {prima}".format(prima=awal))
            break
        awal += 1

if __name__ == '__main__':
    solver(10001)