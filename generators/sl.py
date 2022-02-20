from pydub import AudioSegment
import glob

sounds = glob.glob("./audio/*")
sound = AudioSegment.from_file(sounds[0], format="wav")
slices = sound[::50000]
print(slices)


for i, chunk in enumerate(sound[::100]):
  with open("sound-%s.wav" % i, "wb") as f:
    chunk.export(f, format="wav")
