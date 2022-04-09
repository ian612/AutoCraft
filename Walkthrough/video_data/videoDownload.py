import pytube
import os

# URLs of videos that make up the dataset
urls = ['https://www.youtube.com/watch?v=Eg-jIWWemeQ', 'https://www.youtube.com/watch?v=K1bQuMnMqKY', 'https://www.youtube.com/watch?v=jOgmyYJJ0Is', 'https://www.youtube.com/watch?v=k8oUc2K8nKs', 'https://www.youtube.com/watch?v=tccZgx9HqXo']

# Select options for files to download
videoRes = '480p'
audioRes = '160kbps'
videoFileType = 'mp4'
audioType = 'audio'
language = 'en'

# Folder stuff
outFolder = 'fullVideos/'
if not os.path.exists(outFolder):
    os.makedirs(outFolder)

# Download loop
for url in urls:
    yt = pytube.YouTube(url)
    fname = url.split("=",1)[1]+'.'+videoFileType

    #Title of video
    print('Title: ',yt.title)

    #Number of views of video
    print('Number of views: ',yt.views)

    #Length of the video
    print('Length of video: ',yt.length,'seconds')

    #Description of video
    # print('Description: ',yt.description)

    #Rating
    # print('Ratings: ',yt.rating)

    # Get the video, audio, and captions files
    video = yt.streams.filter(res = videoRes, file_extension = videoFileType).first()
    # audio = yt.streams.filter(abr = audioRes, type = audioType).first()
    # caption = yt.captions.get_by_language_code(language)

    # Print to verify
    print(video)
    # print(caption)
    # print(audio)

    # Download video and audio files
    video.download(output_path=outFolder, filename=fname)
    #audio.download()