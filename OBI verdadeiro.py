P = int(input())
D = int(input())
B = int(input())

total_pontos = (P * 1) + (D * 2) + (B * 3)

if total_pontos >= 150:
    print("B")
elif total_pontos >= 120:
    print("D")
elif total_pontos >= 100:
    print("P")
