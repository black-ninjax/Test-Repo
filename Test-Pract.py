temp=int(input("""Select your choice to enter the temperature
in respected degree 1.Farhenheit
2.Celsius : """))
if temp == 1 :
Fa=int(input("Enter the temp in Fahrenheit:"))
C=(Fa-32)*5/9
print(C, "Degrees celsius")
elif temp == 2 :
Ce=int(input("Enter the temp in Celsius : "))
F=(9/5)*Ce+32
print(F," DEGREES FARENHEIT")
else :
print( )
