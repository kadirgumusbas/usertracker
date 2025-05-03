<script setup>
import {ref, onMounted, watch} from 'vue'
import {useRoute} from 'vue-router'
import {getRequest} from '@/services/apiService.js'


const route = useRoute()
const userId = parseInt(route.params.userId)
const selectedPost = ref(null)
const posts = ref([])
const comments = ref([])


onMounted(async () => {
  const response = await getRequest('posts', userId)
  posts.value = response.data
})

const formatBody = (text, id = 0) => {
  if (id === 0) {
    text = text.length > 100 ? text.slice(0, 150) + '...' : text
  }
  return text.replace(/\\/g, '\n').replace(/\n/g, '<br>')
}

const openModal = (post) => {
  selectedPost.value = post
}
const closeModal = () => {
  selectedPost.value = null
}

watch(selectedPost, async () => {
  if (selectedPost.value) {
    const response = await getRequest('comments', selectedPost.value.id)
    comments.value = response.data
  }
})


</script>

<template>
  <div class="p-6 space-y-6">
    <div
        v-for="post in posts"
        :key="post.id"
        class="bg-white shadow rounded-lg p-4 relative border border-gray-200 h-44 transition-transform duration-200 hover:scale-[1.02] hover:translate-x-1 hover:shadow-md"
    >
      <h2 class="text-lg font-semibold text-gray-800 mb-2">
        {{ post.title.length > 20 ? post.title.slice(0, 20) + '...' : post.title }}
      </h2>
      <p class="text-gray-700" v-html="formatBody(post.body)"></p>
      <div
          @click="openModal(post)"
          class="absolute bottom-4 right-4 text-black font-medium hover:underline flex items-center gap-1 cursor-pointer"
      >
        <span class="text-purple-600 cursor-pointer hover:underline flex items-center gap-1">
          See More</span>
        <!-- Icon buraya eklenecek -->
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="purple"
             stroke-linecap="round" stroke-linejoin="round" width="24" height="24" stroke-width="2">
          <path d="M12 16l4 -4l-4 -4"></path>
          <path d="M8 12h8"></path>
          <path d="M12 3c7.2 0 9 1.8 9 9s-1.8 9 -9 9s-9 -1.8 -9 -9s1.8 -9 9 -9z"></path>
        </svg>
      </div>
    </div>
  </div>
  <div v-if="selectedPost"
       class="fixed inset-0 bg-black bg-opacity-40 backdrop-blur-sm flex justify-center items-center z-50">
    <div class="bg-white w-[90%] max-w-5xl h-[80vh] rounded-3xl shadow-lg relative p-6 flex gap-6 overflow-hidden">

      <!-- Kapatma ikonu -->
      <button
          @click="closeModal"
          class="absolute top-4 right-4 p-1 text-black hover:text-black transition-colors"
          style="background: transparent; border: none;"
      >
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
             fill="none" stroke="currentColor"
             stroke-linecap="round" stroke-linejoin="round"
             width="24" height="24" stroke-width="2">
          <path d="M10 10l4 4m0 -4l-4 4"></path>
          <path d="M12 3c7.2 0 9 1.8 9 9s-1.8 9 -9 9s-9 -1.8 -9 -9s1.8 -9 9 -9z"></path>
        </svg>
      </button>

      <!-- Sol: Post içeriği -->
      <div class="w-1/2 overflow-y-auto pr-4">
        <h2 class=" text-2xl font-bold text-black mb-4 ">{{ selectedPost.title }}</h2>
        <p class="text-gray-700 whitespace-pre-line ml-6 mt-8" v-html="formatBody(selectedPost.body,1)"></p>
      </div>

      <!-- Sağ: Yorumlar (gelecek) -->
      <div class="custom-scroll w-1/2 overflow-y-auto pl-4 border-l border-gray-200 space-y-6 h-full mt-6">
        <h2 class="text-xl font-bold mb-4 text-black">Comments</h2>

        <div v-for="comment in comments" :key="comment.id" class="flex items-start gap-4">
          <!-- Avatar -->
          <img
              :src="`https://i.pravatar.cc/150?img=${(comment.id % 70) + 1}`"
              class="w-12 h-12 rounded-full object-cover"
              alt="User avatar"
          />

          <!-- Comment içeriği -->
          <div>
            <p class="font-semibold text-black text-sm">{{ comment.email }}</p>
            <p class="text-gray-700 text-sm whitespace-pre-line" v-html="formatBody(comment.body,1)"></p>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<style scoped>
/* Scrollbar genişliği */
::-webkit-scrollbar {
  width: 6px;
}

/* Scrollbar arka planı (track) */
::-webkit-scrollbar-track {
  background: #f1f1f1;
}

/* Scrollbar kaydırma kolu (thumb) */
::-webkit-scrollbar-thumb {
  background-color: #4d4d53; /* gri tonu */
  border-radius: 6px;
}
</style>
