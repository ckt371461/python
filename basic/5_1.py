song='''When an eel grabs your arm,
And it causes great harm,
That's - a moray'''
splits_in_song=song.split()
song_replace_prefix_m_with_M=''
for split in splits_in_song:
    if split[0]=='m':
        split=split.capitalize()
    song_replace_prefix_m_with_M+=split+' '
print(song_replace_prefix_m_with_M)