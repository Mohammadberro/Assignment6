Ex:3

MyStack = Stack()
message = input("Message:")
string = ''
for x in message:
    if x != '*':
        MyStack.push(x)  # Keep Stacking As Long we Don't encounter '*'
    else:
        x = MyStack.pop()   # If we encounter a '*', we pop adding it to our string
        string += x
while not MyStack.isEmpty():  # The remaining Items are now popped and added to our string.
    x = MyStack.pop()
    string += x
print(string)
