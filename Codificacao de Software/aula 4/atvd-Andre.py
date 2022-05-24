import random
for x in range(50):
    num = random.randint(1, 99)
    if num<12:
        print(f"A pessoa é uma criança! (idade: {num})")
    elif num>=12 and num<18:
        print(f"A pessoa é um adolescente! (idade: {num})")
    elif num>=18 and num<60:
        print(f"A pessoa é um adulto! (idade: {num})")
    elif num>=60 and num<76:
        print(f"A pessoa é um idoso! (idade: {num})")
    elif num>=76:
        print(f"A pessoa é um idoso que ultrapassou a expectativa de vida do Brasil! (idade: {num})")
