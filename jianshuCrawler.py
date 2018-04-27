from bs4 import BeautifulSoup
import requests

def get_html(url):
    header ={'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    html=requests.get(url,header).content
    return html

def get_info(html):
    soup = BeautifulSoup(html,'html.parser',from_encoding='utf-8')
    re=soup.body.find('div',attrs={'id':'list-container'})
    note_content=soup.find('ul',attrs={'class':'note-list'})
    print(soup)
    for i in note_content.find_all('li'):
        note_title=i.find('a',attrs={'class':'title'})
        print(note_title+'\n')

def main():
    home_url = "https://www.jianshu.com"
    html=get_html(home_url)
    get_info(html)

if __name__ == '__main__':
    main()
