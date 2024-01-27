import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer


root= Tk()
root.geometry("516x700+340+10")
root.title("Аудиоплеер")
root.config(bg='#0f0f0f')
root.resizable(False, False)
mixer.init()

def addMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        print(songs)
        # указываем, что из выбранной папки нужно загружать файлы .mp3
        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)

# определяем функцию воспроизведения загруженной музыки
def playMusic():
    music_name = Playlist.get(ACTIVE)
    print(music_name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()

# добавляем фрейм для элементов интерфейса
lower_frm = Frame(root, bg="#000000", width=516, height=200)
lower_frm.place(x=0, y=00)

# указываем количество кадров в гифке
frmcount = 32
# указываем путь к файлу гифки — она лежит в одной папке с файлом проекта .py
frms = [PhotoImage(file= os.path.join(os.path.dirname(__file__), 'animation.gif'), format='gif -index %i' % i) for i in range(frmcount)]
# определяем функцию обновления гифки
def update(ind):
    frame = frms[ind]
    ind += 1
    if ind == frmcount:
        ind = 0
    lbl.config(image=frame)
    root.after(40, update, ind)

# указываем расположение гифки в окне интерфейса
lbl = Label(root)
lbl.place(x=0, y=0)
root.after(0, update, 0)

# добавляем меню с кнопками
menu = PhotoImage(file= os.path.join(os.path.dirname(__file__), 'menu.png'))
# указываем размер
lb_menu = Label(root, image=menu, width=516, height=120)
# указываем координаты расположения
lb_menu.place(x=0, y=580)

# добавляем фрейм для кнопок
frm_music = Frame(root, bd=2, relief=RIDGE, width=516, height=120)
frm_music.place(x=0, y=580)

# добавляем кнопку воспроизведения и указываем её функцию
btn_play = PhotoImage(file= os.path.join(os.path.dirname(__file__), 'play.png'))
btn_p = Button(root, image=btn_play, bg='#0f0f0f', height=50, width=50, command=playMusic)
btn_p.place(x=225, y=516)

# добавляем кнопку остановки воспроизведения и указываем её функцию
btn_stop = PhotoImage(file= os.path.join(os.path.dirname(__file__), 'stop.png'))
btn_s = Button(root, image=btn_stop, bg='#0f0f0f', height=50, width=50, command=mixer.music.stop)
btn_s.place(x=140, y=516)

# добавляем кнопку паузы и указываем её функцию
btn_pause = PhotoImage(file= os.path.join(os.path.dirname(__file__), 'pause.png'))
btn_ps = Button(root, image=btn_pause, bg='#0f0f0f', height=50, width=50, command=mixer.music.pause)
btn_ps.place(x=310, y=516)

# добавляем кнопку выбора папки с музыкой
btn_browse = Button(root, text="Выбрать папку с музыкой", font=('Arial,bold', 15), fg="Black", bg="#FFFFFF", width=48, command=addMusic)
btn_browse.place(x=0, y=572)

# настраиваем отображение плейлиста
Scroll = Scrollbar(frm_music)
Playlist = Listbox(frm_music, width=100, font=('Arial,bold', 15), bg='#0f0f0f', fg='#00ff00', selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=RIGHT, fill=BOTH)

# запускаем окно плеера
root.mainloop()