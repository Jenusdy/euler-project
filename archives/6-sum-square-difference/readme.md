### Problem
```
The sum of the squares of the first ten natural numbers is,

1^2+2^2+...+10^2=385
The square of the sum of the first ten natural numbers is,

(1+2+...+10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
```

### Solver
```python
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
```

### Output
```
Jawaban : 25164150
```