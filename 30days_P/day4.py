# print("I'm learning Python")
# print("Days\tTopics\tExercises")
# print("Day 1\t3\t5")
# print("Day 2\t3\t5")
# print("This is a backslash symbol \\")

name = "Cris"
email = "cc@cc.com"

string_chain = "I am %s and my email is %s" %(name, email)
print(string_chain)

name2 = "Salemm"
email2 = "ss@ss.com"
string_chain2 = "I am {} and my email is {}".format(name2, email2)
print(string_chain2)

x= 8
y = 7

print("{} / {} = {:.4f}".format(x,y,x/y))

print(f"My name is {name}")