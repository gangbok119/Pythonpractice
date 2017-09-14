#1. 매개변수로 문자열을 받고, 해당 문자열이 `red`면 `apple`을, `yellow`면 `banana`를, `green`이면 `melon`을, 어떤 경우도 아닐 경우 `I don't know`를 리턴하는 함수를 정의하고, 사용하여 `result`변수에 결과를 할당하고 `print`해본다.

def print_fruit(s):
    if s =='red':
        return 'apple'
    elif s =='yellow':
        return 'banana'
    elif s =='green':
        return 'melon'
    else:
        return 'I don\'t know'
result = print_fruit('red')
print(result)
#2. 1번에서 작성한 함수에 `docstring`을 작성하여 함수에 대한 설명을 달아보고, `help(함수명)`으로 해당 설명을 출력해본다.

def print_fruit(s):
    '''
    parameter = string
    You can get back fruit matching color
    red = apple, yellow = banana, green = melon
    if parameter do not matches this color, you can't get back fruit
    '''
    if s =='red':
        return 'apple'
    elif s =='yellow':
        return 'banana'
    elif s =='green':
        return 'melon'
    else:
        return 'I don\'t know'

    help(print_fruit)

#2. 한 개 또는 두 개의 숫자 인자를 전달받아, 하나가 오면 제곱, 두개를 받으면 두 수의 곱을 반환해주는 함수를 정의하고 사용해본다.

def mul(*args):
  if len(args) ==1:
    return args[0] ** 2
  elif len(args) ==2:
    return args[0] * args[1]
  else:
      print('1개나 2개의 숫자를 입력하세요')

mul(2)
mul(2,4)

#3. 두 개의 숫자를 인자로 받아 합과 차를 튜플을 이용해 동시에 반환하는 함수를 정의하고 사용해본다.

def addandminus(x,y):
    if x>y:
        return (x+y,x-y)
    else:
        return (x+y,y-x)


#4. 위치인자 묶음을 매개변수로 가지며, 위치인자가 몇 개 전달되었는지를 print하고 개수를 리턴해주는 함수를 정의하고 사용해본다.

def args_number(func):
    def inner_func(*args):
        print('위치인자의 개수는? :{}'.fomat(len(args)))
        return len(args)
    return inner_func()

args_number(addandminus(2,4))

#5. 람다함수와 리스트 컴프리헨션을 사용해 한 줄로 구구단의 결과를 갖는 리스트를 생성해본다.


f=lambda x,y : '{} x {} = {}'.format(x,y,x*y)
[f for x in range(2,10),for y in range(1,10)]
