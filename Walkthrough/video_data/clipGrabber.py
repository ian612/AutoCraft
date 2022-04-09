import random
import math
from pathlib import Path
from moviepy.editor import *
import os

# Folders
fullVideoFolder = 'fullVideos/'
clipFolder = 'clips/'
if not os.path.exists(clipFolder):
    os.makedirs(clipFolder)

# Video file extension
videoExt = '.mp4'

# Data that sets up the captions file
captionFileName = 'captions.txt'
captionHeader = '# StarCraft II Video Description Captions\n#\n# Generated Manually by Ian Bennett\n# Using the same format as the Microsoft Research Video Description Dataset\n\n'

# Choose a consistent value if we run the clip segmenter more than once
random.seed(0)

# Dataset clip information
clipMinInterval = 5
numClips = 25
clipLength = 10
captionsPerClip = 6

# Get full video names
videos = os.listdir(fullVideoFolder)
print(videos)

# Create the captions file
#Path(clipFolder).mkdir(parents=True, exist_ok=True)
f = open(captionFileName, 'w')
f.write(captionHeader)

for videoName in videos:
    if videoName.endswith(videoExt):
        
        video = VideoFileClip(fullVideoFolder+videoName)
        totalDuration = video.duration
        
        clipPositions = [clipMinInterval * x for x in random.sample(range(math.floor((totalDuration-clipLength)/clipMinInterval)), numClips)]
        clipPositions = sorted(clipPositions)
        print(clipPositions)
        
        for clipPos in clipPositions:
            print(clipPos)
            # Parse small clips
            smolClip = video.subclip(clipPos, clipPos+clipLength)
            
            # Create a name for that
            clipName = videoName[:-len(videoExt)] + '_' + str(clipPos) + '_' + str(clipPos+clipLength)
            
            # write mp4 video files to disk
            smolClip.write_videofile(clipFolder + clipName + videoExt, fps=30, audio=False)
            
            for ct in range(0,captionsPerClip):
                f.write(clipName + ' \n')
        
        video.close()

f.close()