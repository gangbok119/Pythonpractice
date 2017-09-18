import re

f = open('sample.txt','rt')
source = f.read()

re.compile(r'.*', re.DOTALL) #- .과 개행문자를 포함해서 검색
# <td class="title">내용</td>까지의 목록들을 정규표현식으로 찾기
p=re.compile(r'(<td.*?class="title">)(.*?)(</td>)',re.DOTALL)

# 꺾쇠 사이의 공백을 없애기
# re.sub
# group 사용.
result - re.findall(p,source)
for index, item in enumerate(s):
    print('== index %s ==' % index

    # ><사이의 공백을 모두 없앰
    cur_strip_item = re.sub(r'>\s*?<', '><', item, flags=re.DOTALL)
    print(cur_strip_item)

#a태그 내부의 내용을 출력.

    cur_title = re.sub(r'.*?<a.*?(.*?)</a>.*',r'\g<1>', cur_strip_item)
    print(cur_title)



def find_tag(tag_name, class_name, source):
    p = re.compile('r<{tag_name} class="{class_name}".*?>.*?</{tag_name}>'.format(tag_name=tag_name,class_name=class_name))
    return 
