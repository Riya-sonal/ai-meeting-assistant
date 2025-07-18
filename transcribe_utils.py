import whisper

model = whisper.load_model("base")

def transcribe(file_path):
    result = model.transcribe(file_path)
    return result['text']
