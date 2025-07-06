from inference import TTS_RVC
from playsound import playsound

tts = TTS_RVC(rvc_path="src\\rvc", model_path="models\\DenVot.pth", input_directory="input\\")
tts.set_voice("ru-RU-DmitryNeural")
path = tts(text="Привет, мир!", pitch=6)

playsound(path)