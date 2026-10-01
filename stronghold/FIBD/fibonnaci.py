#!/usr/bin/env python3

def fibonnaci(n: int, m: int) -> int:
    if n > 100 or m > 20:
        raise ValueError("n must be at most 100 and m must be at most 20")

    age: list[int] =  [0] * m
    age[0] = 1

    for i in range(2, n + 1):
        birth: int = 0
        for element in age[1:]:
            birth += element

        for j in range(m - 1, 0, -1):
            age[j] = age[j - 1]
            
        age[0] = birth
    
    result: int = 0
    for x in range(0, m):
        result += age[x]

    return result


if __name__ == "__main__":
    try:
        result = fibonnaci(80, 18)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
