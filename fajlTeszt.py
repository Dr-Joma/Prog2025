

try:
    with open ("F1-2024dec1.csv",encoding="utf-8") as fajl:
        f = fajl.read()
    
        n = 4 / 0
    
        print(f)
        print(n)

except Exception as ex:
    print("ezer van baj mo: {ex}")
except FileNotFoundError:
    print("hiva a fajl nyitas kozbe")
except ZeroDivisionError:
    print("me osz noulaval")


print("END")