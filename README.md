# 🇹🇷 SauceDemo Pytest Otomasyon Projesi

Bu proje, popüler bir e-ticaret sitesi olan [SauceDemo](https://www.saucedemo.com/) üzerindeki temel kullanıcı akışlarını (Giriş yapma, Ürün ekleme/silme, Sepet kontrolü) otomatikleştirmek için geliştirilmiştir. Proje, endüstri standardı olan **Page Object Model (POM)** tasarım desenini ve **Pytest** test çatısını kullanır.

## ⚙️ Kurulum Talimatları

Projenin çalışması için Python 3.8+ ve aşağıdaki kütüphaneler gereklidir.


--------------------1. Sanal Ortam (venv) Oluşturma ve Aktifleştirme----------------------------------

Proje bağımlılıklarını izole etmek için sanal ortamı kullanın:

```bash
# Sanal ortamı oluşturun
python -m venv venv

# Sanal ortamı aktifleştirin (Windows/PowerShell)
.\venv\Scripts\Activate

-------------------2. Bağımlılıkları Kurma-----------------------

Gerekli tüm Python kütüphanelerini kurun:

Bash

pip install selenium pytest pytest-html


----------------------------3. Testleri Çalıştırma-------------------------


 

Bash 

pytest

***

HTML Raporu Oluşturma
Test sonuçlarını görsel, paylaşılabilir bir HTML raporu olarak kaydetmek için:

Bash

pytest --html=report.html --self-contained-html
⚠️ Önemli Not: Manuel Tıklama Gereksinimi
Bu projenin en büyük zorluğu, Chrome tarayıcısının otomasyon sırasında otomatik olarak kapatılamayan inatçı bir Google güvenlik pop-up'ı tetiklemesidir. Bu teknik olarak aşılamaz bir engel olduğundan, test akışı bu engeli geçebilmek için manuel müdahale gerektirir.

Manuel Müdahale Süreci:
Test başladığında ve pop-up ekranda belirdiğinde, akış 10 saniye süreyle duraklayacaktır.

Hemen pop-up üzerindeki "Tamam" veya "Okey" butonuna elle tıklayın.

Otomasyon, 10 saniyelik süre dolduktan sonra müdahalenize bakmaksızın otomatik olarak devam edecek ve tamamlanacaktır. (Testin tamamlanması yaklaşık 30 sn kadar sürebilir)

Test tamamlandıktan sonra ana dizinde 'report.html' adında dosya oluşacaktır.Dosyanın üstüne sağ tık -> 'Open with live server' veya 'Canlı sunucuyla aç' seçeneğini seçin(Genellikle ilk seçenek olur) ve test raporlarını HTML formatında görüntüleyin




🇺🇸 SauceDemo Pytest Automation Project
This project is a Python Pytest automation suite developed to test core user flows (Login, Adding/Removing items, Cart validation) on the popular e-commerce website SauceDemo. The project uses the industry-standard Page Object Model (POM) design pattern and the Pytest framework.

⚙️ Installation Instructions
The project requires Python 3.8+ and the following libraries.

--------------------1. Create and Activate Virtual Environment (venv)------------------
Use a virtual environment to isolate project dependencies:

Bash

# Create the virtual environment
python -m venv venv

# Activate the virtual environment (Windows/PowerShell)
.\venv\Scripts\Activate


------------------------------------2. Install Dependencies-------------------
Install all required Python libraries:

Bash

pip install selenium pytest pytest-html


-------------------------------------- Running the Tests---------------------------
Bash

pytest


***
Generate HTML Report
To save test results as a visual, shareable HTML report:

Bash

pytest --html=report.html --self-contained-html
⚠️ Important Note: Manual Click Required
The main challenge for this project is a persistent Google security pop-up that is triggered in the Chrome browser during automation and cannot be programmatically dismissed. Since this is a technical barrier, the test flow requires manual intervention to proceed.

Manual Intervention Process:
When the test starts and the pop-up appears, the execution flow will pause for 10 seconds.

Immediately manually click the "OK" button on the pop-up.

The automation will continue and complete automatically after the 10-second period expires, regardless of your intervention. (The test may take approximately 30 seconds to complete.)

After test complete, a file named 'report.html' folder well be created in main directory. Right-click and select 'Open with live server' option and wiew test reports in HTML format