# 🌐 UserTracker Frontend (N2Mobil Staj Projesi - Aşama 2)

Bu proje, **N2Mobil firması** tarafından verilen 3 aşamalı projenin ikinci adımı olan **Frontend uygulamasıdır**.  
Amaç, Vue 3 ile kullanıcıların gönderileri, yorumları, albümleri ve yapılacaklarını kullanıcı arayüzüyle takip edebilmesini sağlamaktır.

---

## 🚀 Kullanılan Teknolojiler ve Yetenekler

| Teknoloji      | Açıklama                                            |
|----------------|-----------------------------------------------------|
| ⚙️ Vue 3       | Modern, reaktif frontend framework                  | 
| 🌿 Pinia       | Global state yönetimi (Vuex'in modern alternatifi) |
| 🔗 Vue Router  | Sayfalar arası yönlendirme (SPA mimarisi)           |
| 🔮 Axios       | API ile veri alışverişi                             |
| 🎨 TailwindCSS | Utility-first modern CSS framework                  |
| 💾 localStorage| Kalıcı kullanıcı etkileşimleri (checkbox kayıt vb.) |



## 📌 Öğrenilen ve Uygulanan Kavramlar

- ✅ Vue 3 Composition API ile component yapıları
- ✅ Vue Router ile dinamik route kullanımı (örneğin `/users/:userId/albums`)
- ✅ `ref`, `reactive`, `computed`, `watch` gibi reaktif yapılar
- ✅ `v-for`, `v-if`, `@click`, `:class` gibi Vue direktifleri
- ✅ Modal yapısı, layout yönetimi, grid sistemleri
- ✅ Axios ile API'den veri çekme, filtreleme, hata yakalama
- ✅ localStorage ile checkbox kayıtları (her userId için farklı saklama)
- ✅ `Pinia` ile tüm uygulamada state yönetimi (örnek: todos)

---

## 🛠️ Kurulum

```bash
git clone https://github.com/kullaniciadi/usertracker-frontend.git
cd usertracker-frontend
npm install
npm run dev
Uygulama localhost:5173 adresinde çalışır. (Vite üzerinden)

🧠 Öne Çıkan Özellikler
📁 AlbumCard.vue: İçinde 4 sabit resim olan kart yapısı, tıklanabilir bağlantı

📝 UserTodos.vue: Her kullanıcı için localStorage ile yönetilen yapılacaklar listesi

💬 UserPosts.vue: Dinamik modal ile post detay ve yorum gösterimi

📸 AlbumDetail.vue: Her albüm için sabit ama farklı picsum.photos görselleri

👨‍💻 Geliştirici
Kadir Gümüşbaş
Stajyer Yazılım Geliştirici – N2Mobil
Bu aşamada Vue 3 ekosistemine hakimiyet kazanarak modern SPA geliştirme konusunda ciddi bir yetkinlik kazandım ✅

