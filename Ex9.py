'''fath_playlist = input('Введите плей-лист отца: ').split(',')
fath_playlist.reverse()
print('Плей-лист мамы:')
print('\n'.join(fath_playlist), '\n')'''

fath_playlist = []
print('Введите плей-лист отца: ')
for i in range(5):
    music = input()
    fath_playlist.append(music)

mam_playlist = fath_playlist[::-1]

print('\nПлей-лист мамы:')
for music in mam_playlist:
    print(music)