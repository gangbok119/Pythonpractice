'''
while문 내에 try 구문에서 input을 이용해 숫자값을 입력받음
입력받는 숫자값에 해당하는 l[index]를 참조하고, IndexError일 경우 다시 숫자값 입력
IndexError가 나지 않으면 while문 종료
'''
l = ['abcd']


while True:
    try:
        index=input('숫자를 입력하세요: ')
        print('입력한 숫자: {}'.format(index))
        print(l[index])
    except IndexError as IE:
        import Traceback
        print('IndexError!')
        print(Traceback.format_exc())
    else:
        break




'''
1. 정규표현식으로 검사했을 때 패턴이 없을 경우 발생할 NotMatchedException을 사용자 정의
    1-1. Exception을 상속
    1-2. __init__ 메소드에서 패턴문자열과 소스문자열을 매개변수로 사용
    1-3. __str__ 메소드는 __init__에서 받은 "패턴문자열"이 "소스문자열"에 없음을 출력
2. 패턴문자열과 소스문자열을 매개변수로 갖는 search_from_source함수를 정의
    만약 re.search로 소스문자열에서 패턴을 검색했을 때 MatchObject를 찾지 못하면,
    raise NotMatchedException(패턴문자열, 소스문자열)을 발생시킴

3. try-except 구문에서 위 함수를 실행, 예외를 발생시키고 except 구문에서 해당 예외를 받을
    수 있도록 구현
'''
import re
# 패턴과 소스를 생성자 매개변수로 갖는 Exception 클래스 정의
class NotMatchedException(Exception):
    def __init__(self,pattern, source):
        pass
    #print(obj)했을 때 출력될 내용
    def __str__(self):
        return 'Pattern "{}" is not matched in source "{}"'.format(self.Pattern,self.source)
#패턴과 소스매개변수를 받아 re.search로 소스에서 패턴을 검색, 찾지 못하면 NotMatchedException 발생
def search_from_source(p,s):
        m = re.search(p, s)
        if not m:
            raise NotMatchedException(p,s)
        return m

source_string = 'Lux, the Lady of Luminosity'

pattern_string = r'L\w{5}\b'

try:
    result = search_from_source(pattern_string, source_string)
    print('result')
except NotMatchedException as e:
    print(e)

print('Search Result:', result)
