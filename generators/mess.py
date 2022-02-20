from pydub import AudioSegment
import random
import glob

sounds = glob.glob("./audio/*")
#print(sounds)
segment_list = []
for i in range(len(sounds)):
    segment_list.append(AudioSegment.from_file(sounds[i], format="wav"))

random.shuffle(segment_list)

#print(segment_list)
for i in range(len(segment_list)):
    if i == 0:
        combined = segment_list[0].append(segment_list[i], crossfade=30)
    if i >= 1:
        combined = combined.append(segment_list[i], crossfade=30)
        print(combined)

file_handle = combined.export("./audio/jam5.wav", format="wav")
