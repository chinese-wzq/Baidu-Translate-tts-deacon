import urllib.request,os
from urllib.parse import quote

import parse

print("使用百度翻译tts接口实现的自动朗读脚本\n当前版本:demo v0.1\n\t折腾，才是社会进步的原动力！\n")
def download_reporthook(blocknum,blocksize,totalsize):
    if blocknum==0:
        print("下载开始~")
        return 0
    print("\r当前下载进度："+ '%.2f'%((blocknum*blocksize)/totalsize)+"\t\t\t\t\t\t",end="")
    return 0
def download_file(url:str,fileplace:str):
    urllib.request.urlretrieve(url,fileplace,reporthook=download_reporthook)
    return fileplace
text=""
while not os.path.isfile(text):
    text=input("请将输出字幕文件\033[1;0;41m拖到\033[0m这里来(请确保文件存在哦)：")
folder=""
while not os.path.isdir(folder):
    folder=input("请将输出文件夹\033[1;0;41m拖到\033[0m这里来(请确保文件夹存在哦)：")
print("-"*20)
print("正在读取字幕文件中......")
file=open(text,"r+",encoding="UTF-8")
lines=file.readlines()
print("读取字幕文件成功，正在关闭文件......")
file.close()
print("成功关闭字幕文件。")
for i in range(len(lines)):
    print("\n准备下载第\033[1;0;41m"+str(i)+"\033[0m行，本行内容为：\033[1;33;42m"+lines[i]+"\033[0m")
    download_file("https://fanyi.baidu.com/gettts?lan=zh&text="+quote(lines[i])+"&spd="+str(len(lines[i]))+"&source=web",folder+"/"+str(i)+".mp3")
print("下载完成，文件都放文件夹里面了哦~\n百度娘字幕朗读工具\tby WZQ|13905069")