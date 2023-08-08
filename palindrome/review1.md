# レビュー1回目

## 

## レビュー対象のソース

```python
 """ 指定されたひらがなの部分の回文判断プログラム """
import re

with open("out.csv", mode='w', encoding="utf-8") as writer:
    print("No,回文の文書,回文(かな),判定", file=writer)
    writer.close()
with open("in.txt",'r+',encoding = 'utf-8') as reader:
    for i, element in enumerate(reader):
        j = i + 1
        atama = str(j) + ","# pylint: disable=C0103
        for word in element.strip().split(' '):
            word = re.sub(r"\（",",",word)
            word1 = re.sub(r"\）",",",word)
            split_string = word.split(",")
            after_comma = split_string[1]
            pailindrome_word = re.sub(r"\）","",after_comma)
            d = reversed(list(pailindrome_word))
            if list(d) == list(pailindrome_word):
                word2 = word1 + "〇"
                wordseikei = atama + word2
                with open("out.csv", mode='a', encoding="utf-8") as writer:
                    print(f"{wordseikei}",file=writer)
                    writer.close()
            else:
                word2 = word1 + "×"
                wordseikei = atama + word2
                with open("out.csv",mode='a',encoding="utf-8") as writer:
                    print(f"{wordseikei}",file=writer)
                    writer.close()
reader.close()
```



## 指摘一覧

- 不要なクローズ

  with句を使ってファイルをオープンする理由はブロックを抜けたときにファイルをクローズすることを保証するためです。なので、close処理は不要です

  

- out.csvの処理に無駄がおおい

  out.csvはヘッダを出すときに1回、入力行ごとにオープン＆クローズを繰り返しており非常に無駄が多い

  一般的にファイルのオープン＆クローズはコストの高い(時間のかかる)処理であり、1回で済むようにするべきである

  

- 文字列の反転処理

  対面で説明した通りスライスを使うのがベスト

  d = palindrome_word[::-1]

  reversedはシーケンスオブジェクトを逆順に変換してくれるわけではない、

  https://docs.python.org/ja/3/library/functions.html#reversed

  要素を逆順にするイテレータを返すだけなので、これを使って逆順の文字列を組み立てようとすると

  ```python
  ''.join(reversed(pailindrome_word))
  ```

  とする必要がある。が、これはそも文字列を反転するような処理で使うものではなく、スライスを使うべきである。

  

- reを使った置換

  reは正規表現のライブラリである。

  (正規表現は非常に強力な処理であり重要な技術要素であるため、研修でも例題を用意する予定である。)

  正規表現は非常に強力な一方、コストが高い処理とされている。

  なので、必要な時は使ったほうがいいが、必要がない場合にわざわざ使う必要もない。

  このソースでは単純に文字の置換を行っているだけなので、わざわざ正規表現を使う必要はなく、単に

  文字列のメソッドreplaceで十分である。

  

- out.csvの文字コード

  説明文には"Excelで見られるように"とあるが、このプログラムで生成されたcsvファイルはExcelでひらくと文字化けする。Excelでcsvファイルが表示できるようにするためには、出力はSJISにする必要がある。

  これは日本でIT系の仕事する場合は基本的な知識となるので覚えておくこと

  

- 無意味なsplit

  ```python
  for word in element.strip().split(' '):
  ```

  この処理はスペースで分割した文字列をループさせる処理である。

  しかし、今回の入力行にスペースは存在しない。

  (しかももしスペースがあった場合は出力がおかしくなる)



## 講評

pythonは非常に簡潔に書くことができ可読性が高い言語である。

しかし、適切なアルゴリズムで書かれていないと、アルゴリズムの悪さがそのまま出てしまうということでもある。

このプログラムは、文字列に対しどのような操作をするのが最も適切かということが全然まとまっていなく、行き当たりばったりのプログラムになっている。

個人の趣味で行うプログラムであればそれでも許されるが、IT業界で仕事としてプログラムを書く場合は、それを実現するための最良のアルゴリズムでプログラムすることを心掛ける必要がある。

そのためには、

- やらなければいけないことがわかったら、その手順を整理する(アルゴリズムを考える)
- 手順がまとまったらプログラムを実装する
- 実装したプログラムを必要に応じてリファクタリングする

という作業を行ってほしい



今回のプログラムの主要部は

1. 文字列を必要な要素に分解する

2. 分解した要素の1つが、文字列を反転させても同じになっている

   (こちらは対面で説明したので省略)

であり、それぞれ適切なアルゴリズムを考えなければいけない

1については、

```
歌歌う（うたうたう）
```

これを

歌歌う

うたうたう

という要素に分解する最良の手順は何か？を考えるのがアルゴリズムである。

であれば、例えば次のようなアルゴリズムにすべきだろう

```
1. 行を"（"で分割する。
　そうすると0番目の要素は、漢字の部分が取り出せる
　1番目の要素は"うたうたう）"になる
2. 1番目の要素の"）"の部分を取り除く
　やり方はいくつかあるが、改行もついているので、最後の1文字だけ取り除く方法ではだめ
```



出力については、csv形式の出力の場合、文字列にカンマを加えていく方法は可読性も悪いのでお勧めできない。

出力する要素を適切に作成し、それをprint文でf-stringで出力する。数が多い場合はjoinでまとめて出力する。

CSVを強く意識しなければいけない場合(データ中に区切り文字が含まれるような場合)はcsvライブラリを使う。

という方法をとるべき。

今回は4項目しかないので、例えばno, text, sentence, resultの4項目であれば

```python
 print(f"{no},{text},{sentence},{result}")
```

で十分である