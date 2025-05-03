<script setup>

import Navbar from "@/components/Navbar.vue";
import {useRoute} from "vue-router";
import {computed, ref} from "vue";

const route = useRoute()
const userId = computed(() => route.params.userId || '')
const isHomePage = computed(() => {
  return route.path === '/users' || route.path === '/users/'
})
const isAlbumDetail = computed(() => {
  return route.path.includes('/albums/') && route.params.albumId
})
const mainContent = ref(null)

const scrollToTop = () => {
  if (mainContent.value) {
    mainContent.value.scrollTo({
      top: 0,
      behavior: 'smooth'
    })
  }
}

</script>

<template>
  <div class="flex h-screen">
    <!-- Sol Sabit Navbar -->
    <Navbar/>

    <div class="flex flex-col flex-grow bg-white">
      <div v-if="isHomePage" class="m-6">
        <router-link to="/users" aria-label="Go to All Users">
          <span class="text-black font-bold text-2xl" @click="scrollToTop">All Users</span>
        </router-link>
      </div>
      <div v-else-if="isAlbumDetail" class="m-6">
        <router-link :to="`/users/${userId}/albums`" aria-label="Go to Albums">
          <div class="flex items-center">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="black"
                 stroke-linecap="round" stroke-linejoin="round" width="24" height="24" stroke-width="2">
              <path d="M12 8l-4 4l4 4"></path>
              <path d="M16 12h-8"></path>
              <path d="M12 3c7.2 0 9 1.8 9 9s-1.8 9 -9 9s-9 -1.8 -9 -9s1.8 -9 9 -9z"></path>
            </svg>
            <span class="text-black ml-4 font-bold">Go Albums</span>
          </div>
        </router-link>
      </div>
      <div v-else class="m-6">
        <router-link to="/users">
          <div class="flex items-center">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="black"
                 stroke-linecap="round" stroke-linejoin="round" width="24" height="24" stroke-width="2">
              <path d="M12 8l-4 4l4 4"></path>
              <path d="M16 12h-8"></path>
              <path d="M12 3c7.2 0 9 1.8 9 9s-1.8 9 -9 9s-9 -1.8 -9 -9s1.8 -9 9 -9z"></path>
            </svg>
            <span class="text-black ml-4 font-bold">Go Home</span>
          </div>
        </router-link>
      </div>
      <main ref="mainContent" class="flex-grow overflow-auto">
        <router-view/>
      </main>
    </div>
  </div>
</template>


<style scoped>

</style>