import requests, datetime, re
from bs4 import BeautifulSoup

db = {}
def dic(key): #keyword 입력받아, 검색 결과 list return
    get = requests.get("https://dic.daum.net/search.do?q=" + key)
    soup = BeautifulSoup(get.text, "html.parser")
    eng = soup.select_one('div[data-tiara-layer="word eng"]')
    div = eng.select_one('div[class="cleanword_type kuek_type"]')
    ul = div.select_one('ul[class="list_search"]')
    li = ul.select('span[class="txt_search"]')
    
    return li

def slt(li): #list 입력 받아서, 모든 항목 출력, 선택한 번호의 string 출력
    a = 0
    for i in li:
        a += 1
        print(str(a) + ". " + i.get_text(), end="   ")
    
    print(f"//총 {a}개 결과 탐색")
    n = int(input())
    return li[n-1].get_text()

P = ""
while 1:
    A = input()
    if A == "exit":
        break
    P = A
    db[P] = slt(dic(P))
    print(f"{P}(을)를 {db[P]}(으)로 저장\n")

for i in db.keys():
    print(f'{i}   {db[i]}')
    


# now = datetime.datetime.now()
# f = open(f"./cache/{now.year%100:02d}{now.month:02d}{now.day:02d}_{now.hour:02d}{now.minute:02d}{now.second:02d}_{key}.html", "w")
# f.write(str(text))
# f.close()
