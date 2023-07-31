""" 指定された英語文章の英単語をカウントするプログラム """
from collections import defaultdict
import re
import sys

def main(argv):
    """ 指定された英語文章の英単語をカウントする """
    if len(argv) < 2:
        sys.exit(f"usage: {argv[0]} infile")

    words = defaultdict(int)
    with open(argv[1], encoding="UTF-8") as reader:
        for line in reader:
            for word in line.strip().split(' '):
                word = re.sub('[.,!?]', '', word).lower()
                words[word] += 1

    for key, value in sorted(words.items(), key = lambda x:-x[1]):
        if value >= 3:
            print(f"{value:2d},{key}")

if __name__ == "__main__":
    main(sys.argv)
