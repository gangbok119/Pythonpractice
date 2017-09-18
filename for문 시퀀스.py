>실습 - zip 없이 두 시퀀스 동시에 순회하기


fruits = ['apple', 'banana', 'melon']
colors = ['red', 'yellow', 'green', 'purple']

index = 0

for fruit in fruits:
        print(fruit, colors[index])
        print('fruit(%s), color(%s)' % (fruit, colors[index]))
        index +=1


print(zip(fruits, colors)) - zip object

range(0, 10) - 0부터 10 미만까지

> 실습 리스트 컴프리헨션 - 짝수 항목만 리스트화 하기

[item for item in range(1,6) if item%2 == 0]

[표현식 for 항목 in iterable객체 조건문]

실습
1. for문을 2개 중첩하여 0,0 -> 6,3까지 출력

for item1 in range(0,7):
    for item2 in range(0,4):
        print('(%d, %d)' % (item1, item2))
2. 리스트 컴프리헨션으로 위 항목 생성

['(%d, %d)' % (item1, item2) for item1 in range(0,7) for item2 in range(0,4)]
#문자열로 리스트

l2 = [(x,y) for x in range(7) for y in range(4)]
#튜플로 리스트

3. 1, 2번의 반복문에서 1번은 튜플의 첫 번째 항목이 짝수일때만 출력하도록,

 2번은 첫 번째 항복이 짝수일때만 리스트의 원소로 추가

for item1 in range(0,7):
    for item2 in range(0,4):
        if item1%2==0:
            print(item1,item2)

l= [(item1, item2) for item1 in range(0,7) for item2 in range(0,4) if item1%2==0]


 4. 1000에서 2000까지 숫자 중, 홀수의 합을 구해본다.
result = 0
for i in range(1000, 2001):
    if i%2==1:
        result+=i

print(result)

#컴프리헨션과 내장함수 sum 이용

result= sum([x for x in range(1000,2001) if x % 2 ==1])
print(result)
#sum - iterable 내의 값을 모두 더해주는 내장함수

#더 효율적인 방법으로 step 사용

result = sum([x for x in range(1001,2000,2)])
print(result)


 5.
gugu=[item1*item2 for item1 in range(2,10) for item2 in range(1,10)]
index = 0

for x in range(2,10):
    for y range(1,10):
        print('%d X %d = %d'(x,y,gugu[index]))
        index+=1

#기초적인 방법
l = ['%d x %d = %d' % (x, y, x*y) for x in range(2,10) for y in range(1,10)]


# 현재 출력중인 결과가 구구단 중 '몇'단에 해당하는지의 index
gugu_index = 2
# 전체 구구단 결과 리스트 중 몇 번째를 순회하고 있는지의 index
list_index = 0
for item in l:
    #전체 구구단 리스트의 아이템 중 9번째마다 실행
    if list_index % 9 ==0:
        print('== %s단 ==' % gugu_index)
        # 한 번 '몇'단인지 출혁 후에는 다음 단의 index를 저장
        gugu_index += 1
    # 전체 구구단 결과 리스트 중 몇 번째를 순회하는 중인지 업데이트
    list_index += 1
    # 전체 구구단 결과 중 현재 순회중인 item을 출력
    print(item)


# enumerate 내장함수 사용, index를 생략
for list_index, item in enumerate(l):
    if list_index % 9 ==0:
        print('== %단 ==' % gugu_index)
        gugu_index += 1
    print(item)

#dict를 사용해서 gugu_index를 구구단 자료구조내에 포함
#for 문으로 순회 시, 각 리스트의 항목이 dict가 되도록 한다.
# 각 dict는 자신이 '몇단'인지의 정보와 9개의 결과 리스트를 갖는다.
/*
gugu_iist =

for i in range(2,10):
    {'title':'%d단'(% i),'items':['%d x %d = %d' % (i,y,i*y) for y in range(1,10)] }
*/

# 정답

gugu_list = [ {'title':'%d단' % (x), 'items':['%d x %d = %d' % (x, y, x*y) for y in range(1,10)] } for x in range(2,10)]

print(gugu_list)


for gugu in gugu_list:
    print(gugu['title'])
    for item in gugu['items']:
        print(item)
    print('')

 6.
list79=sorted(list(set([result for x in range(1,99) if x%7==0 or x%9==0])))

result = []
for x in range(1,100):
    if x % 7 == 0 or x % 9 == 0:
        result.append(x)

print(result)

bool(None)
bool(0)
bool([])
bool('')

l = []
if not l:
    print('empty list')


def print_string(x):
    print(x)
    print(type(x))
def print_int(x):
    print(x)
    print(type(x))

def print_type(func):
    def inner_func(*args **kwargs):
        for arg in args:
            print('args type:', type(args))
        return f(*args)
    return inner_func
