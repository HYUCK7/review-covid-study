from urllib.request import urlopen

from bs4 import BeautifulSoup


class Crawl:
    @staticmethod
    def crawling(soup, tag, cls_nm) -> []:
        ls = soup.find_all(tag, {'class': cls_nm})
        ls = [i.get_text() for i in ls]
        return ls

    def print_music_list(self, soup) -> None:
        artists = soup.find_all('p', {'class': 'artist'})
        artists = [i.get_text() for i in artists]
        print(''.join(i for i in artists))

        titles = soup.find_all('p', {'class': 'artist'})
        titles = [i.get_text() for i in titles]
        print(''.join(i for i in titles))

    @staticmethod
    def dict1(ls1, ls2) -> {}:
        dict = {}
        for i in range(0, len(ls1)):
            dict[ls1[i]] = ls2[i]
        print(dict)
        return dict

    @staticmethod
    def dict2(ls1, ls2) -> {}:
        dict = {}
        for i, j in enumerate(ls1):
            dict[ls1[i]] = ls2[i]
        print(dict)
        return dict
    
    def zip(self) -> None:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml')
        ls1 = self.crawling(soup, 'p', 'title')
        ls2 = self.crawling(soup, 'p', 'artist')
        # self.dict1(ls1, ls2) -> 사용 시 dict 리턴타입으로
        # self.dict2(ls1, ls2)
        dict = {}
        for i, j in zip(ls1, ls2):
            dict[i] = j
        print(dict)

