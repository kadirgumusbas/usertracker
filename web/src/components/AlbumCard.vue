<script setup>
defineProps(['album'])
</script>

<template>
  <router-link
    :to="`albums/${album.id}`"
    class="bg-white text-black rounded-2xl shadow-md p-4 hover:shadow-2xl transition-all duration-300 border flex flex-col"
  >
    <!-- 4 Fotoğraf Alanı -->
    <div class="grid grid-cols-2 grid-rows-2 gap-1 mb-4">
      <img
        v-for="n in 4"
        :key="n"
        :src="`https://picsum.photos/seed/${album.id}-${n}/300/200`"
        class="w-full h-40 object-cover rounded"
        alt="Album photo"
      />
    </div>

    <!-- Başlık -->
    <h2 class="text-md font-semibold text-center text-gray-800">
      {{ album.title.length > 40 ? album.title.slice(0, 40) + '...' : album.title }}
    </h2>
  </router-link>
</template>

<style scoped>
</style>