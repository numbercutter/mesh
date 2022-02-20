from pydub import AudioSegment
sound1 = AudioSegment.from_file("./audio/j.wav", format="wav")
sound2 = AudioSegment.from_file("./audio/q.wav", format="wav")

# sound1 6 dB louder
louder = sound1 + 6


# sound1, with sound2 appended (use louder instead of sound1 to append the louder version)
combined = sound1 + sound2

# simple export
file_handle = combined.export("./audio/output.wav", format="wav")

"""
sound1 = AudioSegment.from_file("1.wav", format="wav")
sound2 = AudioSegment.from_file("2.wav", format="wav")

# sound1 6 dB louder
louder = sound1 + 6

# Overlay sound2 over sound1 at position 0  (use louder instead of sound1 to use the louder version)
overlay = sound1.overlay(sound2, position=0)


# simple export
file_handle = overlay.export("output.mp3", format="mp3")
"""