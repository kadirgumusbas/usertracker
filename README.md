# 📦 UserTracker (N2Mobil Staj Projesi - Aşama 3)

Bu proje, N2Mobil firmasındaki staj sürecimde 3 aşamalı olarak geliştirilen **tam kapsamlı bir kullanıcı takip sistemidir**. Kullanıcıların gönderileri, yapılacaklar listesi (Todos), albümleri, fotoğrafları ve yorumları RESTful bir API ile yönetilirken, bu veriler Vue 3 tabanlı modern bir frontend arayüzüyle kullanıcıya sunulmaktadır.

![HomePage](https://github.com/user-attachments/assets/e4feb81a-5fd3-4b7d-83ae-02ea9f216f7c)
![TodoPage](https://github.com/user-attachments/assets/b1ec857c-ae50-4cfe-8a6c-5b4f9f61bef6)
![PostPage](https://github.com/user-attachments/assets/925c79dd-48d2-40a5-b3bc-0125e17d30ec)
![PostCommentPage](https://github.com/user-attachments/assets/3749ad91-a453-4662-a70d-ebd4e64d2a93)
![AlbumPage](https://github.com/user-attachments/assets/9796c4b0-6d01-41c1-bb23-2e0e9f2e95c2)
![PhotoPage](https://github.com/user-attachments/assets/6bddc628-3e7f-4c32-8a38-d2f31f9d38d3)







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
