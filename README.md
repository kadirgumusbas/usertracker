# 📦 UserTracker (N2Mobil Staj Projesi - Aşama 3)

Bu proje, N2Mobil firmasındaki staj sürecimde 3 aşamalı olarak geliştirilen **tam kapsamlı bir kullanıcı takip sistemidir**. Kullanıcıların gönderileri, yapılacaklar listesi (Todos), albümleri, fotoğrafları ve yorumları RESTful bir API ile yönetilirken, bu veriler Vue 3 tabanlı modern bir frontend arayüzüyle kullanıcıya sunulmaktadır.

---

## 🚀 Genel Teknolojiler

| Alan     | Teknoloji                     |
|----------|-------------------------------|
| Backend  | Django, Django REST Framework |
| Veritabanı | PostgreSQL, .env yönetimi   |
| Frontend | Vue 3, Pinia, Axios, Tailwind CSS |
| Test / Dokümantasyon | Postman, Git, GitHub |
| Diğer    | LocalStorage, Component Mimarisi, SPA Router |


## ✅ Aşama 1 – Backend (Django API)

- Kullanıcı modeli özelleştirildi (`CustomUser`) ve adres, şirket, konum bilgileri eklendi.
- Modeller arası ilişkiler kuruldu: `Post`, `Comment`, `Album`, `Photo`, `Todo`.
- `ModelViewSet`, `@action`, `router`, `serializer` gibi DRF bileşenleri öğrenildi.
- Admin paneli geliştirildi, filtreler eklendi.
- Veritabanı olarak PostgreSQL kullanıldı.
- Postman ile API testleri yapıldı ve Collection oluşturuldu.

### 🧠 Öğrenilenler

- REST ve RESTful mimarisi
- Django REST Framework (DRF)
- İlişkisel veritabanı yönetimi
- Postman kullanımı
- .env ve hassas veri gizleme

---

## 🖥️ Aşama 2 – Frontend (Vue 3)

- Vue 3 Composition API yapısı kullanılarak SPA mimarisi kuruldu.
- `vue-router` ile dinamik route sistemi tanımlandı.
- `Pinia` ile merkezi state yönetimi sağlandı.
- `Axios` ile API’den veri çekildi.
- `LocalStorage` ile kullanıcı özel verileri kalıcı hale getirildi.
- Komponent tabanlı yapı ile okunabilir ve ölçeklenebilir tasarım yapıldı.
- Tailwind CSS ile modern ve responsive tasarım hazırlandı.

### 🧠 Öğrenilenler

- Vue 3 Composition API
- Pinia vs Vuex farkı, Store yapısı
- Axios ile async/await veri çekme
- LocalStorage ile veri saklama
- Dynamic routing (`/users/:id/posts`)
- Responsive UI tasarımı (Tailwind)
- Reaktif sistem, Proxy yapısı, watch/computed farkları

---

## 📂 Önemli Dosyalar

### API (Backend)
- `api/core/models.py`: Veritabanı modelleri
- `api/core/serializers.py`: DRF serializer’ları
- `api/core/views.py`: Viewset ve custom action’lar
- `api/postman/usertracker_collection.json`: API test koleksiyonu
- `.env`: Veritabanı bilgileri (gizli)

### Web (Frontend)
- `web/src/stores/`: Pinia store dosyaları (örnek: `todoStore.js`)
- `web/src/components/`: Parçalanmış Vue bileşenleri
- `web/src/pages/`: Sayfa-temelli komponentler (`UserTodos.vue` gibi)
- `web/src/router/index.js`: Vue Router tanımları
- `web/src/assets/style.css`: Global stil ve scrollbar özelleştirmesi

---

## 🧪 Örnek Kullanım

### Sunucu Başlatmak (Backend)

```bash
cd api/
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver

Geliştirme Sunucusu (Frontend)
bash
Kopyala
Düzenle
cd web/
npm install
npm run dev
```
📌 Proje Durumu

 Aşama 1 – Backend: Tamamlandı

 Aşama 2 – Frontend Tasarımı: Tamamlandı

 Aşama 3 – API Entegrasyonu ve State Yönetimi: Tamamlandı

👨‍💻 Geliştirici
Kadir Gümüşbaş
Stajyer Yazılım Geliştirici @ N2Mobil
📧 akadirgumusbas@gmail.com

Staj süresince REST API, Vue 3, Pinia gibi teknolojileri öğrenerek ve gerçek dünya problemleri çözerek yazılım geliştirme deneyimimi ileri taşıdım.
Mentorüm Uğurcan Usta yönlendirmeleri ile kod kalitesi, okunabilirlik ve proje yapısı konusunda da gelişme kaydettim ✅
