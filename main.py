import requests
from bs4 import BeautifulSoup

URL = "http://www.stj.or.kr/bbs/board.php?bo_table=branch&page={}&"
print("지역", "회사명", "택시 수", "주소", "연락처", "채용공고", "채용공고 조회수", sep=" | ")

page = 0
while True:
    page += 1
    webpage = requests.get(URL.format(page))
    soup = BeautifulSoup(webpage.content, "html.parser")

    # 테이블 리스트 존재 확인
    table_lists = soup.find_all("li", {"class": "list-item"})
    if len(table_lists) == 0:
        break

    # 지역
    areas_with_markup = soup.find_all("div", {"class": "wr-category"})
    areas = []

    for area in areas_with_markup:
        areas.append(area.text.strip())

    # 택시회사
    companies_with_markup = soup.find_all("div", {"class": "wr-subject"})
    companies = []

    for company in companies_with_markup:
        companies.append(company.text.strip())

    # 택시 수
    taxis = []
    for link in links:
        taxi_webpage = requests.get(link)
        taxi_soup = BeautifulSoup(taxi_webpage.content, "html.parser")
        taxi = taxi_soup.find("div", {"class": "col-sm-4 col-xs-3 en font-16"})
        taxis.append(taxi.text.strip())

    # 주소
    addresses_with_markup = soup.find_all("div", {"class": "wr-wr_1 hidden-xs"})
    addresses = []

    for address in addresses_with_markup:
        addresses.append(address.text.strip())

    # 연락처
    contacts_with_markup = soup.find_all("div", {"class": "wr-wr_2 hidden-xs"})
    contacts = []

    for contact in contacts_with_markup:
        contacts.append(contact.text.strip())

    # 채용 공고
    invitations = soup.find_all("a", {"onclick": "view_modal(this.href); return false;"})
    links = []
    for link in invitations:
        children = link['href']
        links.append(children)

    # 채용 공고 조회수
    hits_with_markup = soup.find_all("div", {"class": "wr-hit hidden-xs"})
    hits = []
    for hit in hits_with_markup:
        hits.append(hit.text.strip())

    # 출력
    for number in range(0, len(areas)):
        print(areas[number], companies[number], taxis[number], addresses[number], contacts[number],
              links[number], hits[number], sep=' | ')