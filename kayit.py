import speech_recognition as ses_tanima
sesi_tani= ses_tanima.Recognizer()
with ses_tanima.AudioFile('antoncehov.wav') as kaynak:
    ses_metni= sesi_tani.listen(kaynak)
    try:
        text=sesi_tani.recognize_google(ses_metni, language="tr-TR")
        print(text)
    except:
        print("bir hata var.")
