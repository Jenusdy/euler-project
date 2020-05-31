### Problem
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

### Solver
```python
def find_factor(n):
    factor = []
    for i in range(1,int(n**0.5)+1): # Upper limit sqrt(n) mempercepat proses
        if n % i == 0 :
            factor.append(i)
    return factor

def factor_prime(factor):
    prime = []
    for i in factor:
        counter = 0
        for j in range(1,i+1):
            if i % j == 0:
                counter+=1
        if counter == 2 :
            prime.append(i)
    return prime

def solver(n):
    factor = factor_prime(find_factor(n))
    return factor

if __name__ == '__main__':
    hasil = max(solver(600851475143))
    print("Jawaban : {hasil}".format(hasil=hasil))
```

### Output
```
Jawaban : 6857
```