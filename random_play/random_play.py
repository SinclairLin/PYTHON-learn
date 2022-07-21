import random, os
music_dir = 'C:/Users/Sinclair/Desktop/python/PYTHON-learn/random_play/music'
songs = os.listdir(music_dir)
song = random.randint(0,len(songs))
print(songs[song])  ## Prints The Song Name
os.startfile(os.path.join(music_dir, songs[0]))
