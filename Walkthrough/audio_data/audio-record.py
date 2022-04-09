import pyaudio
import pyAudioDspTools
import wave
import os

# Define text file with sentences
sentence_file = 'sentences.txt'
sentences = []

for line in open(sentence_file):
    line = line.strip('\n')
    sentences.append(line)

# Ensuring the sentences have been properly loaded.
print(len(sentences), 'sentences loaded') # 100
#print(sentences[0:20])
#print(sentences[-1])

# Define audio extension
ext = '.wav'

# Define audio recording device
chunk = 1024
FORMAT = pyaudio.paInt16
channels = 1
sample_rate = 48000
record_time = 4 		# time in seconds

# Define folder for saving audio files
folder = 'files_'+str(int(sample_rate/1000))+'kHz/'
if not os.path.exists(folder):
    os.makedirs(folder)

# Allow the user to start at a sentence number other than 0
start_number = int(input('Enter a sentence number to start with (0 = beginning): '))

for ct in range(start_number,100):
	fname = folder+str(ct)+ext
	print('Now recording',fname)
	
	# Display the desired sentence
	print('Sentence is "', sentences[ct], '"')
	
	# Recording Loop
	done = 0
	while not done:
		
		# User prompt to begin recording
		input('Press Enter to begin recording.')
		
		# Record Audio
		p = pyaudio.PyAudio()
		stream = p.open(format=FORMAT,
						channels=channels,
						rate=sample_rate,
						input=True,
						output=True,
						frames_per_buffer=chunk)
		frames = []
		print("Recording...")
		for i in range(int(sample_rate / chunk * record_time)):
			data = stream.read(chunk)
			# if you want to hear your voice while recording
			# stream.write(data)
			frames.append(data)
		print("Finished recording.")
		stream.stop_stream()
		stream.close()
		p.terminate()
		
		# Save the audio file
		wf = wave.open(fname, "wb")
		wf.setnchannels(channels)
		wf.setsampwidth(p.get_sample_size(FORMAT))
		wf.setframerate(sample_rate)
		wf.writeframes(b"".join(frames))
		wf.close
		
		done = int(input('Enter 1 to continue, 0 to rerecord: '))

print('Files are done, all stored in', folder)