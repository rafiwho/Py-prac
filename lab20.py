class MediaFile:
    def __init__(self, file_name, file_size, random):
        self.file_name = file_name
        self.file_size = file_size
        self.random = random

    def play(self):
        print(f'Now playing the media file "{self.file_name}"...')

    def update(self, string=None):
        if string!=None:
            if isinstance(string,int):
                self.file_size = string
            elif '.' in string:
                self.file_name = string
            else:
                self.random = string
        else: 
            pass


class AudioFile(MediaFile):
    def __init__(self, file_name, file_size, duration):
        super().__init__(file_name, file_size, "")
        self.random = duration

    def display(self):
        print(f'File Name: {self.file_name}')
        print(f'File Size: {self.file_size} MB')
        print(f'Duration: {self.random}')


class VideoFile(MediaFile):
    def __init__(self, file_name, file_size, resolution):
        super().__init__(file_name, file_size, "")
        self.random = resolution

    def display(self):
        print(f'File Name: {self.file_name}')
        print(f'File Size: {self.file_size} MB')
        print(f'Resolution: {self.random}')


audio_file = AudioFile("song.mp3", 5, "3:42")
video_file = VideoFile("movie.mp4", 150, "4k")

audio_file.play()
video_file.play()

print("\nDetails of Audio File:")
audio_file.display()
print("Details of Video File:")
video_file.display()

audio_file.update('2:1')
video_file.update('3k')
video_file.update(25)
video_file.update()

print("\nUpdate occurred in audio file.")
print("Details of Audio File:")
audio_file.display()

print("\nUpdate occurred in the video file.")
print("Details of Video File:")
video_file.display()
