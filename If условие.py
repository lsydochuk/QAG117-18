# If условие (a > b "Свершилось!", a < b "Да ну!", a = b "А если так?", потом a + v, b - v и заново сравнить)

a = int(input(""))
b = int(input(""))
v = int(input(""))

if a > b:
    print("Свершилось!")
elif a < b:
    print("Да ну!")
else:
    print("А если так?")
    a = a + v
    b = b - v
    if a > b:
       print("Свершилось!")
    elif a < b:
       print("Да ну!")