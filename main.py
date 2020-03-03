import json
import xml.etree.ElementTree as ET
from collections import Counter


def occurrences_words_json(file_name):
    file = json.load(file_name)
    items = file['rss']['channel']['items']

    words_more_than_six = []

    for news in items:
        description = news['description']
        description = description.split()
        for word in description:
            news_word_count = len(list(word))
            if news_word_count > 6:
                words_more_than_six.append(word.lower())
    print("Чаще всего встречаются слова в JSON: ")
    counter = Counter(words_more_than_six)
    print(counter.most_common(10))

def occurrences_words_xml(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()
    items = root.findall("channel/item")

    words_more_than_six = []

    for item in items:
        description = item.find("description")
        description.text = description.text.split()
        for word in description.text:
            news_word_count = len(list(word))
            if news_word_count > 6:
                words_more_than_six.append(word.lower())
    print("Чаще всего встречаются слова в XML: ")
    counter = Counter(words_more_than_six)
    print(counter.most_common(10))


if __name__ == '__main__':
    with open("newsafr.json", encoding="utf8") as f:
        occurrences_words_json(f)
    with open("newsafr.xml", encoding="utf-8") as f:
        occurrences_words_xml(f)