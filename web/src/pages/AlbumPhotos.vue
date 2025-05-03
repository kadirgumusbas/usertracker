<script setup>
import {useRoute} from 'vue-router'
import {ref} from 'vue'

const route = useRoute()
const albumId = parseInt(route.params.albumId)
const photos = ref([])

// 10 fotoğrafı picsumdan üretme
for (let i = 1; i <= 10; i++) {
  photos.value.push({
    id: i,
    url: `https://picsum.photos/seed/${albumId}-${i}/600/400`,
    title: `Photo ${i}`
  })
}
</script>

<template>
  <div class="p-8">
    <h1 class="text-2xl font-bold mb-6 text-center text-black">Album Photos</h1>

    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
      <div
        v-for="photo in photos"
        :key="photo.id"
        class="bg-white p-3 shadow rounded-lg flex flex-col items-center hover:shadow-lg transition"
      >
        <img :src="photo.url" :alt="photo.title" class="w-full h-52 object-fill rounded mb-4" />
        <p class="text-sm text-gray-700 text-center truncate">{{ photo.title }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
</style>
