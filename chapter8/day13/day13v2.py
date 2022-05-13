# 练习8-8
def make_album(singer, album, songs=1):
    music_album = {"singerName": singer, "albumName": album, "songCount": songs}
    return music_album


# 下面开始循环部分，并且提供退出途径
while True:
    singer_name = input("输入专辑的歌手名字：（填写过程中可随时退出，若要退出，输入q即可！）\n")
    if singer_name.lower() == "q":
        break
    album_name = input("输入专辑的名字：\n")
    if album_name.lower() == "q":
        break
    song_count = input("专辑内有几首歌呢？（默认一首）\n")
    if song_count == "q":
        break
    # 用户输入了回车，就是默认情况，判断条件不是"\n"而是""也就是空值
    elif song_count == "":
        song_count = 1
    # 如果上面的条件都没退出循环，下来把收集到的值添加到字典中
    music = make_album(singer_name, album_name, song_count)
    print(music)
