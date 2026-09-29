#!/usr/bin/env python3

def mendel(k: int, m: int, n: int) -> float:
    total: int = (k + m + n) * (k + m + n - 1)
    
    p1 = (m * (m - 1)) / total
    p2 = (2 * (m * n)) / total
    p3 = (n * (n - 1)) / total
    
    p_rec = (p1 * 0.25) + (p2 * 0.50) + (p3 * 1)
    p_dom = 1 - p_rec
    
    return round(p_dom, 5)


if __name__ == "__main__":
    k: int = 24
    m: int = 21
    n: int = 16
    
    result: float = mendel(k, m, n)
    print(result)