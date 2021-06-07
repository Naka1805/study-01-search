import pandas as pd
import csv

### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
#sourceリストをDataframeに変換しそれをcsv化する
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]
name_df = pd.DataFrame({'name':source})
print(name_df)
print(type(name_df))
name_df.to_csv("kimetu.csv")

#csvを読み込んでそれをリストに変換する
name_df = pd.read_csv('kimetu.csv')
name_list = list(name_df['name'])

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く
    if word in name_list:
        print("{}が見つかりました".format(word))

    #入力したものがリストに存在しなければリストに追加する
    else:
        print("{}が見つかりませんでした".format(word))
        name_list.append(word)
        print(name_list)

#リストをDataframeに変換後csv化する
if __name__ == "__main__":
    search()
    name_df = pd.DataFrame({'name':name_list})
    print(name_df)
    name_df.to_csv("kimetu.csv")
