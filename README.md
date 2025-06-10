# 🔐 Gelişmiş Güvenli Dosya Aktarım Sistemi (Advanced Secure File Transfer System)

Bu proje, istemci-sunucu mimarisi ile çalışan, AES-128 ve RSA-2048 şifreleme algoritmalarını kullanan, IP başlığı üzerinde manuel işlem yapılabilen ve saldırı simülasyonları ile test edilen gelişmiş bir güvenli dosya aktarım sistemidir.

---

## 📦 Özellikler

- 🧠 AES-128 (EAX mod) ile simetrik veri şifreleme
- 🔑 RSA-2048 ile AES anahtarının güvenli iletimi
- ✅ SHA-256 hash ile dosya bütünlüğü kontrolü
- 🧱 Dosya parçalayıp TCP ile gönderim (Fragmentation & Reassembly)
- 🌐 IP başlığı (TTL, ID, checksum) manipülasyonu (Scapy)
- 🧪 UDP packet injection simülasyonu
- 📊 iPerf3 ile ağ bant genişliği testi
- ⚠️ `tc` komutu ile yapay paket kaybı simülasyonu
- 🖥️ Tkinter ile kullanıcı dostu GUI

---

## 🗂️ Proje Yapısı

```
├── client.py            # İstemci: dosya şifreleme & gönderme
├── server.py            # Sunucu: çözümleme & doğrulama
├── crypto_utils.py      # AES & RSA işlemleri
├── ip_utils.py          # IP başlığı düzenleme (Scapy)
├── inject_packet.py     # UDP packet injection
├── gui.py               # Grafik arayüz (Tkinter)
```

---

## ⚙️ Kurulum

1. Python 3.12 kurulu olmalı.
2. Aşağıdaki kütüphaneleri yükle:

```bash
pip install pycryptodome scapy
```

---

## 🚀 Çalıştırma

1. Sunucuyu başlat:

```bash
python server.py
```

2. GUI arayüzünü çalıştır:

```bash
python gui.py
```

3. Alternatif olarak komut satırı istemcisi:

```bash
python client.py
```

---

## 🧪 Testler & Gözlemler

- ✅ RTT (Ping) Testi → Ortalama 0.42 ms
- ✅ iPerf3 Testi → 1.10 GB, 941 Mbps
- ✅ Paket kaybı (%5) sonrası şifreli veri tespiti: “MAC check failed”
- ✅ Wireshark ile şifreli veri gözlemlenebilir ancak içerik okunamaz
- ✅ Inject edilen UDP paketleri algılanıp işlenmedi

---

## 🔐 Güvenlik Detayları

- **AES-EAX** ile gizlilik ve bütünlük birlikte sağlanır.
- **RSA-2048**, yalnızca AES anahtarını şifrelemek için kullanılır.
- **SHA-256**, dosya bütünlüğünü istemci ve sunucu tarafında doğrular.
- **Wireshark** testleri, trafiğin şifrelendiğini göstermektedir.

---

## 🎯 Saldırı Simülasyonları

- `inject_packet.py`: UDP sahte paket gönderimi
- Wireshark üzerinden bu paketlerin reddedildiği gözlemlenir
- AES-EAX MAC kontrolü başarısız olunca veri işlenmez

---

## 📸 Ekran Görüntüleri

- Dosya gönderim arayüzü (Tkinter)
- Sunucuda çözümleme çıktısı
- Wireshark ekran görüntüleri
- iPerf3 performans ekranı

---

## 🎬 Demo Videosu

📺 [YouTube'da İzle](https://www.youtube.com/watch?v=KWYasapdn3M)

---

## 📄 Proje Raporu

📎 [Final Raporunu Görüntüle (PDF)](https://github.com/AleksDulda/Advanced-Secure-File-Transfer-System/blob/main/Final_Raporu.pdf))

---
