
# hi()

if 5 < 2:
    print('5 is indeed greater than 2')
else:
    print('5 is not greater than 2')


myname = 'hazar'
if myname == 'hazar':
  print('YES')
elif myname == 'bob':
  print('WHAT?')
else:
    print('NO')

volume = 10
print(volume)
if volume<20 or volume>80:
  volume = 50
  print('BETTER')
print(volume)


print('------------------')
def hi():
  print('Hello')
  print("How's you?")
# hi()
def hay(name):
    if name == 'Ola':
        print('Hi Ola!')
    elif name == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')
hay('yui')
print('------------------')


# def hoo(personal):
def hoo():
  # print('Hi ' + personal + '!')
  print('PAINT hohoho')

people = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']

# hoo("Rachel")
for personal in people:
  # hoo(personal)
  hoo()
  print('Hi ' + personal + '!')
