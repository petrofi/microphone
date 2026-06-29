# 🎙️ Python ile Sesten Metne Dönüştürücü (Speech-to-Text)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![SpeechRecognition](https://img.shields.io/badge/Library-SpeechRecognition-green)
![License](https://img.shields.io/badge/License-MIT-blueviolet)

Bilgisayarınızın mikrofonunu kullanarak sesinizi dinleyen ve bunu metne çeviren basit, modüler bir Python uygulaması. **Google Web Speech API** altyapısını kullanır.

## ✨ Özellikler
- **Çoklu Dil Desteği:** Türkçe, İngilizce ve Rusça seçenekleri.
- **Akıllı Dinleme:** Ortam gürültüsünü (ambient noise) otomatik olarak temizler.
- **Hata Yönetimi:** Mikrofon erişim sorunları veya API bağlantı hatalarını düzgünce ele alır.

## 🚀 Kurulum

1. Depoyu bilgisayarınıza klonlayın:
```bash
git clone https://github.com/HACKTRI1X/microphone.git
cd microphone
```

2. Gerekli kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt
```

> **Not:** Windows kullanıcılarının mikrofon erişimi için `PyAudio` kütüphanesini kurması gerekmektedir. Eğer `pip install PyAudio` hata verirse, resmi dokümantasyona göz atabilirsiniz.

## 💡 Kullanım

Programı çalıştırdığınızda size hangi dili kullanmak istediğinizi soracaktır:

```bash
python microphone.py
```
