
email = input("Email manzilini kiriting: ")


if "@" in email:
    
    at_index = email.index("@")
    if "." in email[at_index:]:
        
        if " " not in email:
            print("Email manzili to'g'ri")
        else:
            print("Email manzili noto'g'ri")
    else:
        print("Email manzili noto'g'ri")
else:
    print("Email manzili noto'g'ri")
