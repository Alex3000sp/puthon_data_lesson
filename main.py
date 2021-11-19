#Task 1
s1 = input("Enter string s1: ")
s2 = input("Enter string s2: ")
equal = s1 == s2
print(f'''s1 is: {s1} 
          s1 lnegth = {len(s1)}
          s2 is: {s2} 
          s2 lnegth = {len(s2)}
          s1 first symbol is: {s1[0]}
          s2 last symbol is: {s2[-1]}
          s1 equals s2 - {equal}
          s2 include s1? - {s2 in s1}
          s1 include s2? - {s1 in s2}
''')
#Task 2
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
print(f"Result of division without remainder: {((a**2 + b**2)/(3 * b - 4))//((4 * c**5)/6)}")
print(f"The remainder of division: {((a**2 + b**2)/(3 * b - 4))%((4 * c**5)/6)}")
