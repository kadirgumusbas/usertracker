<script setup>
import {computed, onMounted, ref} from "vue"
import {useRoute} from 'vue-router'
import {getRequest} from "@/services/apiService.js";

defineProps({ user: Object })

const userId = computed(() => parseInt())
const profileImage = `https://i.pravatar.cc/150?img=5`

</script>

<template>

  <router-link
      v-if="user"
      :to="`/users/${user.id}/todos`"
      class="bg-white text-black rounded-2xl shadow-md p-4 hover:shadow-lg transition-all duration-300 border">

    <div class="flex items-center mb-6">
      <img :alt="profileImage" :src="profileImage" class="w-24 h-24 rounded-full object-cover"/>
      <div class="mx-7">
        <h2 style="color: #26303E" class="font-semibold text-lg">{{ user.name }}</h2>
        <p style="color: #5C6672" class="text-sm text-gray-600">{{ user.email }}</p>
        <p style="color: #5C6672" class="text-sm text-gray-600">{{ user.phone }}</p>
      </div>
    </div>

    <div class="space-y-4 text-gray-600">
      <div class="flex items-start">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
             stroke-linecap="round" stroke-linejoin="round" width="24" height="24" stroke-width="2">
          <path d="M15 11a3 3 0 1 0 -3.973 2.839"></path>
          <path d="M11.76 21.47a1.991 1.991 0 0 1 -1.173 -.57l-4.244 -4.243a8 8 0 1 1 13.657 -5.588"></path>
          <path
              d="M18 22l3.35 -3.284a2.143 2.143 0 0 0 .005 -3.071a2.242 2.242 0 0 0 -3.129 -.006l-.224 .22l-.223 -.22a2.242 2.242 0 0 0 -3.128 -.006a2.143 2.143 0 0 0 -.006 3.071l3.355 3.296z"></path>
        </svg>
        <div>
          <p style="color: #313E50"><strong>Location</strong></p>
          <span v-if="user.address" style="color: #5C6672">{{ user.address?.street }} / {{ user.address?.city }} <br> {{ user.address?.suite }} </span>
        </div>
      </div>

      <div class="flex items-start">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor"
             stroke-linecap="round" stroke-linejoin="round" width="24" height="24" stroke-width="2">
          <path d="M3 21l18 0"></path>
          <path d="M5 21v-14l8 -4v18"></path>
          <path d="M19 21v-10l-6 -4"></path>
          <path d="M9 9l0 .01"></path>
          <path d="M9 12l0 .01"></path>
          <path d="M9 15l0 .01"></path>
          <path d="M9 18l0 .01"></path>
        </svg>
        <div>
          <p style="color: #313E50"><strong>Company</strong></p>
          <span style="color: #5C6672">{{ user.company?.name }}</span>
        </div>
      </div>

      <div class="flex items-start">
        <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-linecap="round"
            stroke-linejoin="round"
            width="24"
            height="24"
            stroke-width="2"
        >
          <path d="M20.94 13.045a9 9 0 1 0 -8.953 7.955"></path>
          <path d="M3.6 9h16.8"></path>
          <path d="M3.6 15h9.4"></path>
          <path d="M11.5 3a17 17 0 0 0 0 18"></path>
          <path d="M12.5 3a16.991 16.991 0 0 1 2.529 10.294"></path>
          <path d="M16 22l5 -5"></path>
          <path d="M21 21.5v-4.5h-4.5"></path>
        </svg>
        <div>
          <p style="color: #313E50"><strong>Website</strong></p>
          <span style="color: #5C6672">{{ user.website }}</span>
        </div>
      </div>
    </div>
  </router-link>

</template>


