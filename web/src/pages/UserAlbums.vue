<script setup>
import AlbumCard from '@/components/AlbumCard.vue'
import {ref, onMounted, computed} from 'vue'
import {useRoute} from 'vue-router'
import {getRequest} from "@/services/apiService.js";

const route = useRoute()
const albums = ref([])
const userId = computed(() => parseInt(route.params.userId))
onMounted(async () => {
  const response = await getRequest('albums', userId.value)
  albums.value = response.data
})

</script>

<template>
  <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
    <AlbumCard v-for="album in albums" :key="album.id" :album="album"/>
  </div>
</template>


