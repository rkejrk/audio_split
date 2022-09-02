import csv
from pydub import AudioSegment
import os
import glob

# フォルダの絶対パス
root = os.path.dirname(os.path.abspath(__file__))
# mp3ファイルを検出
mp3_path = glob.glob(os.path.join(root, "*.mp3"))
# 出力先作成
save_folder = mp3_path[0].rstrip('.mp3')
print(save_folder)    
os.mkdir(save_folder)

# mp3ファイルの読み込み
sound = AudioSegment.from_file(mp3_path[0], format="mp3")
# csv読み込み
with open(os.path.join(root, "input.csv"), encoding="utf-8") as f:
    reader = csv.reader(f)
    # mp3 書き出し
    last_time: int = 0
    title: str = "タイトル"
    count:int = 0

    for line in reader:
        if len(line) >= 2:
            # 終了  時間
            time = line[0].split(':')
            finish_time = 0;

            if len(time) == 2:
                finish_time = (int(time[0])*60 + int(time[1])) * 1000
            elif len(time) == 3:
                finish_time = (int(time[0])*3600 + int(time[1])*60 + int(time[2])) * 1000

            # 0-0秒にならないように設定
            if finish_time != last_time:
                path:str = os.path.join(save_folder,"{}_{}.mp3")
                # audioclip\output\
                print(line[0],path.format(count, title))
                # last_time～finish_timeを抽出
                sound1 = sound[last_time:finish_time]
                sound1.export(path.format(count,title), format="mp3")

            # 次の情報
            last_time = finish_time
            title = line[1]
            count += 1
        
    sound1 = sound[last_time:]
    sound1.export(
        os.path.join(save_folder,"{}_{}.mp3").format(count,title), 
        format="mp3"
        )
    
    print("END!!")
