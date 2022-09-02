# 機能概要
csvファイルに従ってmp3ファイルを分割するプログラム

例）

用意するデータ：

・audioSplit/filename.mp3

・audioSplit/input.csv
>  内容
>
> 00:00,【AAA】 aaaaaa
>
> 10:33,【AAA】 bbbbbb
>
> 30:37,【AAA】 cccccc
>
> 50:00,【BBB】 aaaaaa
>
> 1:01:50,【BBB】 bbbbbb
> 


出力結果：

    audioSplit/filename~~
            　├──【AAA】 aaaaaa.mp3
            　├──【AAA】 bbbbbb.mp3
            　├──【AAA】 cccccc.mp3
            　├──【BBB】 aaaaaa.mp3
            　└──【BBB】 bbbbbb.mp3


## 使用の準備

※はじめにpythonのツールをインストールしてください
1. 実行するPython環境に必要なパッケージをインストール。
    > pip install pydub

2. ffmpegコマンドを利用できるように以下からダウンロードしたファイルにパスを通す

    https://ffmpeg.org/download.html


## 使い方

1. 以下の情報でcsvファイルを作成

        1列目：hh:yy:mmまたはyy:mmフォーマットでチャプターの開始時間を記入
        MP3に存在しない時間は指定しないでください。

        2列目：分割したMP3のタイトル
        \などフォルダに使用してはいけない文字を使用しないでください。

2. audioSplitフォルダにmp3ファイルの配置

    *ファイル名は出力先のフォルダ名になります。
    すでにaudioSplitフォルダ内に存在するフォルダ名は使用しないでください。
    
    *すでにaudioSplitフォルダ内に別のMP3ファイルがある場合は削除してください。

3. コマンドを実行

    audioSplitディレクトリに移動
    > cd audioSplit

    run.pyを実行
    > python run.py

4. [END!!]と表示されたら完了です。

## おことわり
　個人用に数時間程度で作成したため、コンパイルや品質保証もまったくないです。

　pydubで対応しているファイル形式であれば

    16行目43行目51行目の書き換え＋[mp3]の置換

を行えば他のファイル形式にも応用可能かと思います。

このソースを利用して問題が発生した場合、自己責任でお願いします。
