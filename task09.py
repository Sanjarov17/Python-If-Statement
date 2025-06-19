
a = int(input("1-tomon uzunligini kiriting: "))
b = int(input("2-tomon uzunligini kiriting: "))
c = int(input("3-tomon uzunligini kiriting: "))


if a == b and b == c:
    print("Teng tomonli uchburchak")
else:
    if a == b or b == c or a == c:
        print("Teng yonli uchburchak")
    else:
        print("Turli tomonli uchburchak")
