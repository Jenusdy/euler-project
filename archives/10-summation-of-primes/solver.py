def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solver(n):
    total = 0
    angka = 2
    while True:
        if is_prime(angka):
            total+=angka
        angka+=1
        if angka == n :
            print("Jawaban : {hasil}".format(hasil=total))
            break

if __name__ == '__main__':
    solver(2000000)