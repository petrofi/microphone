import speech_recognition as sr
import sys

def sesten_metne():
    print("-" * 40)
    print(" 🎙️ Sesli Asistan (Speech to Text)")
    print("-" * 40)
    
    r = sr.Recognizer()

    # Dili seçme
    print("\nLütfen konuşacağınız dili seçin:")
    print("1 - Türkçe (tr-TR)")
    print("2 - İngilizce (en-US)")
    print("3 - Rusça (ru-RU)")
    
    secim = input("\nSeçiminiz (1/2/3): ")

    dil_haritasi = {
        '1': 'tr-TR',
        '2': 'en-US',
        '3': 'ru-RU'
    }

    if secim not in dil_haritasi:
        print("❌ Hata: Geçersiz seçim. Programdan çıkılıyor.")
        sys.exit(1)

    secilen_dil = dil_haritasi[secim]

    # Mikrofonu dinleme
    try:
        with sr.Microphone() as source:
            print("\n✅ Ortam gürültüsü ayarlanıyor, lütfen bekleyin...")
            r.adjust_for_ambient_noise(source, duration=1)
            print("🎙️ Lütfen konuşun...")
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
    except Exception as e:
        print(f"❌ Mikrofon erişim hatası: {e}")
        print("Lütfen mikrofonunuzun bağlı ve yetkili olduğundan emin olun.")
        sys.exit(1)

    # API ile dönüştürme
    try:
        print("\n⏳ İşleniyor...")
        text = r.recognize_google(audio, language=secilen_dil)
        print("=" * 40)
        print(f"🗣️ Söylediğiniz metin: \n\n{text}")
        print("=" * 40)
    except sr.UnknownValueError:
        print("❌ Hata: Ne dediğinizi tam olarak anlayamadım. Lütfen daha net konuşmayı deneyin.")
    except sr.RequestError as e:
        print(f"❌ Hata: Google Speech Recognition servisine ulaşılamıyor.\nDetay: {e}")
    except Exception as e:
        print(f"❌ Beklenmeyen bir hata oluştu: {e}")

if __name__ == "__main__":
    sesten_metne()
