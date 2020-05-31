### Problem
```
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
```

### Solver
```python
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
```

### Output
```
Jawaban : 906609
```