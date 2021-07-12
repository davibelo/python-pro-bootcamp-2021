# declaring variables type
age: int
name: str

age = 12
name = "Davi Belo"

# specifing data types previously, 
# helps when you call the function
# because the IDE understands what to expect
# after the "->" is the return of the function
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

print(police_check(12))
print(police_check(19))

if police_check(19):
    print("You may pass")
else: 
    print("Pay a fine")
