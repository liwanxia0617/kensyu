""" 指定されたひらがなの部分の回文判断プログラム """
with open("in.txt","r",encoding="utf-8") as reader,open("out.csv","w",encoding="utf-8") as writer:
    for no,line in enumerate(reader):
        no = no + 1
        text, sentence = line.strip().replace("）", "").split("（")
        if sentence == sentence[::-1]:
            result = "〇"  # pylint: disable=C0103
        else:
            result = "×"  # pylint: disable=C0103
        print(f"{no},{text},{sentence},{result}",file=writer)  # pylint: disable=C0304