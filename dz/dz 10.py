age1=int(input())
age2=int(input())
age3=int(input())
age4=int(input())
if age1*12+age2<age3*12+age4:
    print("первый человек старше")
elif age1*12+age2>age3*12+age4:
    print("второй человек старше")
else:
    print("их возраст равен")
    