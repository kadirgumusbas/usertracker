<script setup>
import {useRoute} from 'vue-router'
import {computed, onMounted, ref} from 'vue'
import {getRequest} from "@/services/apiService.js";

const route = useRoute()
const users = ref([])  // Reaktif bir kullanıcı listesi
const userId = computed(() => parseInt(route.params.userId))

const selectedUser = computed(() =>
    users.value.find(user => user.id === userId.value)
)
const isHomePage = computed(() => {
  return route.path === '/users' || route.path === '/users/'
})

const profileImage = `https://i.pravatar.cc/150?img=5`

onMounted(async () => {
  const response = await getRequest('users')
  users.value = response.data
})
</script>

<template>
  <aside
      class="h-screen w-[250px] bg-gray-100 text-black  flex-shrink-0 overflow-y-auto flex flex-col justify-between border-r border-gray-300">
    <!-- ÜST KISIM -->
    <div>
      <template v-if="isHomePage">
        <div class="my-10 h-10">
          <router-link
              :to="'/users'"
              class="flex items-center gap-3 py-1 px-4 transition-all text-sm font-medium text-purple-600 bg-white"
              :class="route.path.includes('/users') ? 'bg-white border-l-4 border-purple-600':''">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                 stroke-linecap="round" stroke-linejoin="round" width="24" height="24" stroke-width="2">
              <path d="M9 7m-4 0a4 4 0 1 0 8 0a4 4 0 1 0 -8 0"></path>
              <path d="M3 21v-2a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4v2"></path>
              <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
              <path d="M21 21v-2a4 4 0 0 0 -3 -3.85"></path>
            </svg>
            <span>Users</span>
          </router-link>
        </div>
      </template>
      <template v-else>
        <div class="space-y-8">
          <!-- Kullanıcı Bilgisi -->
          <div class="flex items-center gap-4 m-4 ">
            <img
                :src="profileImage"
                alt="Avatar"
                class="w-12 h-12 rounded-full object-cover"
            />
            <div>
              <h2 class="text-sm font-semibold">{{ selectedUser?.name }}</h2>
              <p class="text-xs text-gray-500">{{ selectedUser?.email }}</p>
            </div>
          </div>
          <div class="border-t border-gray-300 w-50 m-4"></div>


          <!-- Menü Butonları -->
          <nav class="space-y-2">
            <div>
              <router-link
                  :to="`/users/${userId}/todos`"
                  class="flex items-center gap-3 px-8 py-1.5 transition-all text-sm font-medium text-purple-600 hover:bg-white"
                  :class="route.path.includes('/todos') ? 'bg-white border-l-4 border-purple-600' : ''">
                <!-- icon -->
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                     stroke-linecap="round" stroke-linejoin="round" width="24" height="24" stroke-width="2">
                  <path d="M9 5h-2a2 2 0 0 0 -2 2v12a2 2 0 0 0 2 2h10a2 2 0 0 0 2 -2v-12a2 2 0 0 0 -2 -2h-2"></path>
                  <path d="M9 3m0 2a2 2 0 0 1 2 -2h2a2 2 0 0 1 2 2v0a2 2 0 0 1 -2 2h-2a2 2 0 0 1 -2 -2z"></path>
                  <path d="M9 14h.01"></path>
                  <path d="M9 17h.01"></path>
                  <path d="M12 16l1 1l3 -3"></path>
                </svg>
                <span>Todos</span>
              </router-link>
            </div>
            <div>
              <router-link
                  :to="`/users/${userId}/posts`"
                  class="flex items-center gap-3 px-8 py-1.5 transition-all text-sm font-medium text-purple-600 hover:bg-white"
                  :class="route.path.includes('/posts') ? 'bg-white border-l-4 border-purple-600' : ''">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                     stroke-linecap="round" stroke-linejoin="round" width="24" height="24" stroke-width="2">
                  <path
                      d="M6 4h11a2 2 0 0 1 2 2v12a2 2 0 0 1 -2 2h-11a1 1 0 0 1 -1 -1v-14a1 1 0 0 1 1 -1m3 0v18"></path>
                  <path d="M13 8l2 0"></path>
                  <path d="M13 12l2 0"></path>
                </svg>
                <span>Posts</span>
              </router-link>
            </div>
            <div>
              <router-link
                  :to="`/users/${userId}/albums`"
                  class="flex items-center gap-3 px-8 py-1.5 transition-all text-sm font-medium text-purple-600 hover:bg-white"
                  :class="route.path.includes('/albums') ? 'bg-white border-l-4 border-purple-600' : ''">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                     stroke-linecap="round" stroke-linejoin="round" width="24" height="24" stroke-width="2">
                  <path d="M15 8h.01"></path>
                  <path d="M11.5 21h-5.5a3 3 0 0 1 -3 -3v-12a3 3 0 0 1 3 -3h12a3 3 0 0 1 3 3v5"></path>
                  <path d="M3 16l5 -5c.928 -.893 2.072 -.893 3 0l1.5 1.5"></path>
                  <path
                      d="M18 22l3.35 -3.284a2.143 2.143 0 0 0 .005 -3.071a2.242 2.242 0 0 0 -3.129 -.006l-.224 .22l-.223 -.22a2.242 2.242 0 0 0 -3.128 -.006a2.143 2.143 0 0 0 -.006 3.071l3.355 3.296z"></path>
                </svg>
                <span>Albums</span>
              </router-link>
            </div>
          </nav>
        </div>
      </template>
    </div>
    <!-- ALT SABİT KISIM -->
    <div class="flex items-center gap-1 font-bold m-4 border-t w-30 h-16 border-gray-300">
      <img src="@/assets/n2.png" alt="logo" class="w-10 h-10 m-1 ml-6"/>
      <span style="color: #485B69; font-size: 25px; text-align: center">N2Mobil</span>
    </div>
  </aside>
</template>

<style scoped>
</style>
