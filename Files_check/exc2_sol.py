def exc2_sol(x):
    n=x
    import math
    digits = (int)(math.log10(n))
    n = (int)(n / pow(10, digits))
    first =n;

    last = (x % 10)
    ans = str(first)+ ""+str(last)
    return int(ans)

