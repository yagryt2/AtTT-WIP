import requests

file_path = 'D:/Sublime Text/projects/py/recordToSend1.mp3'  # Add the Path of your audio file 
headers = {
    'Authorization': f'Bearer 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',
}

files = {
    'file': open(file_path, 'rb'),
    'model': (None, 'whisper-1'),
}

response = requests.post('https://api.openai.com/v1/audio/transcriptions', headers=headers, files=files)

print(response.text)