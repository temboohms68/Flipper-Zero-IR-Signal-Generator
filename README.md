# IR Signal Generator for Flipper Zero

[English](#english) | [Türkçe](#türkçe)

---

<a name="english"></a>
## 🇬🇧 English

### Description
This is a simple **IR Signal Generator** application designed for the **Flipper Zero**. It allows you to generate continuous infrared signals at a configurable frequency.

**Disclaimer:** This application is for **educational and testing purposes only**. Do not use it to disrupt legitimate communications or services. The author is not responsible for any misuse.

### Features
- **Adjustable Frequency:** Change the signal frequency (default: 38kHz) using Left/Right buttons.
- **Toggle Generation:** Start and stop signal generation with the OK button.
- **Visual Feedback:** Screen indicates when signal generation is active.

### How to Build
1. Clone this repository into your Flipper Zero firmware's `applications_user` directory.
2. Build the firmware or just this application using `fbt`.
   ```bash
   ./fbt fap_ir_signal_generator
   ```

### Controls
- **OK Button:** Start / Stop Generation
- **Left / Right:** Decrease / Increase Frequency (Steps of 1kHz)
- **Back:** Exit Application

---

<a name="türkçe"></a>
## 🇹🇷 Türkçe

### Açıklama
Bu, **Flipper Zero** için tasarlanmış basit bir **Kızılötesi (IR) Sinyal Üretici** uygulamasıdır. Ayarlanabilir bir frekansta sürekli IR ışığı yayarak sinyal üretmenizi sağlar.

**Yasal Uyarı:** Bu uygulama yalnızca **eğitim ve test amaçlıdır**. Meşru iletişimleri veya hizmetleri aksatmak için kullanmayınız. Yazar, herhangi bir kötüye kullanımdan sorumlu değildir.

### Özellikler
- **Ayarlanabilir Frekans:** Sol/Sağ tuşlarını kullanarak sinyal frekansını değiştirebilirsiniz (Varsayılan: 38kHz).
- **Üretimi Aç/Kapat:** OK tuşu ile sinyal üretimini başlatıp durdurabilirsiniz.
- **Görsel Geri Bildirim:** Üretim aktif olduğunda ekranda belirtilir.

### Nasıl Derlenir (Build)
1. Bu depoyu Flipper Zero yazılımınızın `applications_user` dizinine klonlayın.
2. Yazılımı veya sadece bu uygulamayı `fbt` kullanarak derleyin.
   ```bash
   ./fbt fap_ir_signal_generator
   ```

### Kontroller
- **OK Tuşu:** Sinyal Üretimini Başlat / Durdur
- **Sol / Sağ:** Frekansı Azalt / Artır (1kHz'lik adımlarla)
- **Geri:** Uygulamadan Çık
