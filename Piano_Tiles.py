import pafy

audio_path = "D:/Music"
url_input = input("Enter the URL: ")
url = url_input

video = pafy.new(url)
bestaudio = video.getbestaudio()
bestaudio.download(filepath=audio_path)