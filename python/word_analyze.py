# -*- coding: UTF-8 -*- 
# @author hezhang
# @date   2016/9/5 
# @time   19:40:20
# @brief  listparse paractice
import jieba
import requests
from bs4 import BeautifulSoup


def extract_text(url):
    """Extract html content."""
    page_source = requests.get(url).content
    bs_source = BeautifulSoup(page_source)
    report_text = bs_source.find_all('p')

    text = ''

    for p in report_text:
        text += p.get_text()
        text += '\n'

    return text

def word_frequency(text):
    from collections import Counter

    words = [word for word in jieba.cut(text, cut_all=True) if len(word) >= 2]
    c = Counter(words)

    for word_freq in c.most_common(10):
        word, freq = word_freq
        print(word)
        print(freq)


# url_2016 = 'http://www.gov.cn/guowuyuan/2016-03/05/content_5049372.htm'
url_2016 = 'http://www.noahweb.net/mail/2/Project.htm'
text_2016 = extract_text(url_2016)
word_frequency(text_2016)




