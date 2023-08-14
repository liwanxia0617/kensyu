'''回文判断'''
with open("in.txt", "r", encoding="utf-8") as reader, open("out.csv", "w", encoding="utf-8") as writer:
    for n, line in enumerate(reader):
        n += 1
        kannji, kana = line.strip().replace("（", ":").replace("）", "").split(":")
        if kana == kana[::-1]:
            result = "〇"
        else:
            result = "×"
        print(f"{n},{kannji},{kana},{result}", file=writer)
