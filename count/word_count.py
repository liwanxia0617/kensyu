""" word count 英単語をカウント数するプログラム """
import sys
import re


def main(argv):
    """ word count実体 """
    if len(argv) < 2:
        sys.exit(f"usage:{argv[0]} infile")

    path = argv[1]
    words = {}
    with open(path, encoding="UTF-8") as reader:
        for line in reader:
            line = re.sub('[?,!.]', '', line).lower().strip().split(' ')
            for word in line:
                if word in words:
                    words[word] += 1
                else:
                    words[word] = 0

    for key, value in sorted(words.items(), key=lambda x: -x[1]):
        if value > 2:
            print(f"{value:2d},{key}")


if __name__ == "__main__":
    main(sys.argv)
