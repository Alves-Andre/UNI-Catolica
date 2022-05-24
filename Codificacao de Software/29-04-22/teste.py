posi = [['x',1,'o'],['o','x','o']]
for x in posi:
    for y in x:
        if str(y) in '123456789':
            print("\nJogo  NAO terminado!")
        else:
            print("\nJogo terminado!")