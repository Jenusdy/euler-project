def is_palindrom(n):
    a = str(n)
    b = a[::-1]
    if a == b :
        return True
    return False

def solver():
    palindrom = []
    for i in range(100,999+1):
        for j in range(100,999+1):
            if is_palindrom(i*j):
                palindrom.append(i*j)
    return palindrom

if __name__ == '__main__':
    hasil = max(solver())
    print("Jawaban : {hasil}".format(hasil=hasil))