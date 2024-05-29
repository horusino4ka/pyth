##e=(input("введите количество сторон"))
##if e=="3":
##    print("треугольник")
##elif e=="4":
##    print("квадрат")
##elif e=="5":
##    print("пятиугольник")
##else:
##    print("стороны указаны неверно")
##

##e=(input("введите номер мясяца"))
##if e=="1":
##    print("январь")
##elif e=="2":
##    print("февраль")
##elif e=="3":
##    print("март")
##elif e=="4":
##    print("апрель")
##elif e=="5":
##    print("май")
##elif e=="6":
##    print("Июнь")
##elif e=="7":
##    print("Июль")
##elif e=="8":
##    print("Август")
##elif e=="9":
##    print("сентябрь")
##elif e==10:
##    print("Октябрь")
##elif e==11:
##    print("ноябрь")
##else:
##    print("Декабрь")

e=(input("введите номер мясяца"))
if e=="1" or e=="2" or e=="12":
    print("Зима")
elif e=="4" or e=="6" or e=="5":
    print("Весна")
elif e=="6" or e=="7" or e=="8":
    print("Лето")
elif e=="9" or e=="10" or e=="11":
    print("Осень")
