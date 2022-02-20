from pydub import AudioSegment
import random
import glob

sounds = glob.glob("./audio/*")
#print(sounds)
segment_list = []
for i in range(len(sounds)):
    segment_list.append(AudioSegment.from_file(sounds[i], format="wav"))

#print(segment_list)
for i in range(len(segment_list)):
    if i == 0:
        combined = segment_list[0].append(segment_list[i])
    if i >= 1:
        combined = combined.append(segment_list[i])
        print(combined)

file_handle = combined.export("./audio/jam.wav", format="wav")
# sound1 6 dB louder
#louder = sound1 + 6

# sound1, with sound2 appended (use louder instead of sound1 to append the louder version)
#combined = sound1 + sound2
#combined = sound1.append(sound2)

# simple export
"""file_handle = combined.export("./audio/output333.wav", format="wav")

print(type(combined)) 
  
#  To find frame rate of song/file
print(combined.frame_rate)   
  
# To know about channels of file
print(combined.channels) 
  
# Find the number of bytes per sample 
print(combined.sample_width ) 
  
  
# Find Maximum amplitude 
print(combined.max)
  
# To know length of audio file
print(len(combined))"""
"""sound1 = AudioSegment.from_file("./audio/j.wav", format="wav")
sound2 = AudioSegment.from_file("./audio/q.wav", format="wav")

# sound1 6 dB louder
louder = sound1 + 6

# Overlay sound2 over sound1 at position 0  (use louder instead of sound1 to use the louder version)
overlay = sound1.overlay(sound2, position=0)


# simple export
file_handle = overlay.export("output444.wav", format="wav")
"""