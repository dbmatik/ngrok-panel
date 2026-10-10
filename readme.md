<div align="center">

# 🚀 Ngrok Panel Pro

**A Modern Web Dashboard for Local Ngrok Management**  
*Yerel Ngrok Yönetimi İçin Modern Web Arayüzü*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?logo=python&logoColor=white)](https://www.python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0-lightgrey.svg?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[English](#english) • [Türkçe](#türkçe)

<img src="https://via.placeholder.com/800x450.png?text=✨+Insert+Dashboard+Screenshot+Here+✨" alt="Ngrok Panel Dashboard" width="100%">

</div>

---

<h2 id="english">🇬🇧 English</h2>

Tired of using the terminal for Ngrok? **Ngrok Panel Pro** is a lightweight, local web dashboard that allows you to manage your HTTP, TCP, and TLS tunnels with a single click. It features an auto-installer, auth-token management, and a beautiful UI.

### ✨ Features
*   **Zero-Config Auto Install:** Automatically detects your OS and downloads Ngrok if it's not installed.
*   **Multi-Protocol Support:** Expose HTTP, HTTPS, TCP, and TLS endpoints.
*   **Bilingual & Themed:** Built-in English/Turkish languages and Light/Dark mode toggles with memory.
*   **One-Click Copy:** Grabs the generated public IP/URL directly from the Ngrok local API.
*   **No Terminal Needed:** Everything runs in the background.

### 📸 Screenshots
| Light Mode | Dark Mode |
| :---: | :---: |
| <img src="https://via.placeholder.com/400x250.png?text=Light+Mode+Screenshot" alt="Light Mode"> | <img src="https://via.placeholder.com/400x250.png?text=Dark+Mode+Screenshot" alt="Dark Mode"> |

### 🛠️ Installation & Quick Start

1. **Clone or Download the Repository:**
   ```bash
   git clone https://github.com/dbmatik/ngrok-panel.git
   cd ngrok-panel
   ```

2. **Run the Application:**
   *   **Windows:** Double-click the `start.bat` file.
   *   **Mac / Linux:** Open your terminal and run:
       ```bash
       bash start.sh
       ```
   *The script will automatically create a virtual environment, install Flask, and open the dashboard in your default browser at `http://127.0.0.1:5000`.*

### 📖 How to Use
1. **Setup:** If Ngrok is not installed, the panel will prompt you to click "Auto Install".
2. **Authentication:** Paste your Ngrok Auth Token (from your Ngrok dashboard) and click "Save".
3. **Forward a Port:** Enter a Project Name, select the Protocol (HTTP, TCP, TLS), enter the Port number (e.g., `8000` or `25565`), and click "Add".
4. **Go Live:** Click the **Start** button next to your rule. The public URL will appear instantly. Click the copy icon to share it!

---

<h2 id="türkçe">🇹🇷 Türkçe</h2>

Ngrok için sürekli terminal kullanmaktan sıkıldınız mı? **Ngrok Panel Pro**, HTTP, TCP ve TLS tünellerinizi tek bir tıklamayla yönetmenizi sağlayan hafif ve yerel bir web arayüzüdür. Otomatik kurulum, token yönetimi ve modern bir tasarıma sahiptir.

### ✨ Özellikler
*   **Otomatik Kurulum:** İşletim sisteminizi algılar ve Ngrok yüklü değilse arka planda otomatik olarak indirir.
*   **Çoklu Protokol Desteği:** HTTP, HTTPS, TCP ve TLS portlarını dışarı açın.
*   **Çift Dil & Tema:** Dahili Türkçe/İngilizce dil seçeneği ve hafızalı Gece/Gündüz modu.
*   **Tek Tıkla Kopyalama:** Ngrok'un atadığı public IP/URL adresini yerel API'den otomatik çeker ve kopyalamanızı sağlar.
*   **Terminal Gerekmez:** Tüm işlemler arka planda sessizce yürütülür.

### 📸 Ekran Görüntüleri
| Gündüz Modu | Gece Modu |
| :---: | :---: |
| <img src="https://via.placeholder.com/400x250.png?text=Gunduz+Modu+Gorseli" alt="Gündüz Modu"> | <img src="https://via.placeholder.com/400x250.png?text=Gece+Modu+Gorseli" alt="Gece Modu"> |

### 🛠️ Kurulum ve Başlangıç

1. **Projeyi İndirin (Clone):**
   ```bash
   git clone https://github.com/dbmatik/ngrok-panel.git
   cd ngrok-panel
   ```

2. **Uygulamayı Çalıştırın:**
   *   **Windows:** Klasördeki `start.bat` dosyasına çift tıklayın.
   *   **Mac / Linux:** Terminali açın ve şu komutu girin:
       ```bash
       bash start.sh
       ```
   *Bu komutlar otomatik olarak sanal bir Python ortamı oluşturur, Flask kütüphanesini kurar ve `http://127.0.0.1:5000` adresinde paneli tarayıcınızda açar.*

### 📖 Nasıl Kullanılır?
1. **Kurulum:** Sisteminizde Ngrok yoksa, panel size "Otomatik Kur" butonu sunacaktır, tıklayın.
2. **Kimlik Doğrulama:** Ngrok web sitesinden aldığınız "Auth Token" kodunu yapıştırın ve "Kaydet"e basın.
3. **Port Yönlendirme:** Bir "Proje Adı" girin, Protokolü seçin (Örn: web için HTTP, oyun sunucuları için TCP) ve Port numarasını (Örn: `8000` veya `25565`) yazıp "Ekle"ye tıklayın.
4. **Bağlantıyı Başlat:** Eklediğiniz kuralın yanındaki **Başlat** butonuna basın. Ngrok URL'i saniyeler içinde ekrana gelecektir. Yanındaki kopyala butonunu kullanarak arkadaşlarınızla paylaşabilirsiniz!

---

<div align="center">
  <i>dbmatik</i>
</div>