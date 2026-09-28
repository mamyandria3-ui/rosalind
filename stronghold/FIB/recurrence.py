#!/usr/bin/env python3

def recurrence(n: int, k: int) -> int:
    if n > 40 or k > 5:
        raise ValueError("n must be <= 40 and k must be <= 5")
    if n <= 2:
        return 1
    return recurrence(n - 1, k) + k * recurrence(n - 2, k)
    
if __name__ == "__main__":
    try:
        result = recurrence(28, 2)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")