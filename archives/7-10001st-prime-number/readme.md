### Problem
```
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
```

### Solver 
```python
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
```
### Output
```
Jawaban : 104743
```