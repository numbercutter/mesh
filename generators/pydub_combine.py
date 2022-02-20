from pydub import AudioSegment
import random
import glob

sounds = glob.glob("./audio/*")
segments = {}
segment_list = []
for i in range(len(sounds)):
    segments[sounds[i]] = AudioSegment.from_file(sounds[i], format="wav")

print(range(len(segments.values())))
print(segments.values())
for i in range(len(segments.values())):
    combined = segments[0].append(segments[i])
# sound1 6 dB louder
#louder = sound1 + 6

print(combined)
print(segments.values())
print(sounds[0])
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