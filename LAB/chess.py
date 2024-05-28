def is_val(x, y, p, q):
    if p > 8 or q > 'H':
        return False
    if x == p or y == q:
        return True
    else:
        return False

def solve():
    x = int(input())
    y = input()
    p = int(input())
    q = input()
    if is_val(x, y, p, q):
        print("Valid")
    else:
        print("Invalid")

solve()
