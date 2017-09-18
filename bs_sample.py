from bs4 import BeautifulSoup

f = open('sample.txt','rt')
source = f.read()
soup = BeautifulSoup(source, 'lxml')

soup_beauti=soup.prettify() #일부분만 가져와도 자동으로 태그를 삽입해서 보정.

soup_a=soup.findAll('a')

for name in soup_a:
    print(name.get_text())
