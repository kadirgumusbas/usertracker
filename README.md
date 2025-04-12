# 📦 UserTracker Backend (N2Mobil Staj Projesi - Aşama 1)

Bu proje, **N2Mobil** firması tarafından verilen 3 aşamalı proje kapsamında geliştirilen **Backend API** uygulamasıdır.  
Projede kullanıcıların; gönderileri, yorumları, albümleri, fotoğrafları ve yapılacak işleri (todos) gibi içerikleri RESTful bir yapıyla yönetebilmesi amaçlanmıştır.

## 🚀 Tamamlanan Teknolojiler ve Yetenekler

Bu aşamada **backend geliştirmesi** başarıyla tamamlanmıştır ve aşağıdaki teknolojiler kullanılmıştır:

- ⚙️ **Django** (backend web framework)
- 🧱 **Django REST Framework** (API geliştirme)
- 🗃️ **PostgreSQL** (gerçek veritabanı bağlantısı)
- 📬 **Postman** (API testleri ve dökümantasyonu)

---

## 🔍 Bu Aşamada Öğrendiklerim

- ✅ REST ve RESTful API mimarisinin temelleri
- ✅ Django REST Framework ile `ModelViewSet`, `@action`, `router`, `serializer`, `perform_create`, `get_queryset` gibi yapılar
- ✅ `CustomUser` modeli oluşturarak kullanıcı modelini genişletme (adres, şirket, konum vb.)
- ✅ `OneToOne` ve `ForeignKey` gibi ilişkilerle modeller arası bağlantı kurma
- ✅ Admin panelinde gelişmiş görüntüleme ve filtreleme işlemleri
- ✅ Postman ile API testleri yapma ve Collection oluşturma
- ✅ SQLite yerine **PostgreSQL** kullanarak gerçek veritabanı bağlantısı kurma
- ✅ `.env` dosyası ile hassas bilgileri gizleme

---

## 🧱 Kullanılan Modeller (Özet)

- **User (CustomUser)**: `name`, `phone`, `website`, `address`, `company`
- **Post / Comment**: Gönderi ve yorum sistemi
- **Album / Photo**: Albüm ve görsel yönetimi
- **Todo**: Kullanıcılara ait yapılacaklar listesi

---

## 📂 Proje Yapısı

bash
usertracker/
├── core/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── admin.py
│   └── ...
├── postman/
│   └── usertracker_collection.json
├── manage.py
├── requirements.txt
└── README.md

⚙️ Kurulum
git clone https://github.com/kullaniciadi/usertracker-backend.git
cd usertracker-backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

.env dosyası oluştur:
DB_NAME=usertracker
DB_USER=postgres
DB_PASS=postgres

Veritabanı migrasyonları:
python manage.py makemigrations
python manage.py migrate

Geliştirme sunucusunu başlat:
python manage.py runserver

🔗 Postman Collection
Tüm API endpoint'leriyle birlikte hazır olan Postman Collection dosyasını postman/usertracker_collection.json yolundan içe aktararak test edebilirsiniz.

📌 Sonraki Aşama
Bu backend yapısı, Vue 3 ile geliştirilecek olan Frontend (Aşama 2) ile entegre edilecek ve daha sonra projede tam bir kullanıcı arayüzü ile bütünleştirilecektir.

🧑‍💻 Geliştirici
Kadir [@kadirgumusbas]
Stajyer Yazılım Geliştirici – N2Mobil
Proje süresi boyunca mentorluk, öğrenme ve pratik arasında denge kurarak temel backend yapı taşlarını oturtmayı başardım ✅
