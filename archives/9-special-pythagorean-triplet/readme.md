### Problem 
```
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
```
### Solution
```python
def solver(n):
    for a in range(1,1000):
        for b in range(a,1000):
            c = 1000 - a - b
            if a < b and b < c and a**2 + b**2 == c**2:
                return a*b*c

if __name__ == '__main__':
    hasil = solver(1000)
    print("Jawaban : {hasil}".format(hasil=hasil))
```

### Output
```
Jawaban : 31875000
```