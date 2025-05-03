<script setup>
import {ref, onMounted} from 'vue'
import UserCard from '@/components/UserCard.vue'
import {getRequest} from '@/services/apiService.js'

const users = ref([])

onMounted(async () => {
  const response = await getRequest('users')
  users.value = response.data
})

</script>


<template>
  <div v-if ="users.length">
    <div class="grid sm:grid-cols-2 md:grid-cols-3 gap-6 bg-white">
      <UserCard v-for="user in users" :key="user.id" :user="user"/>
    </div>
  </div>
</template>


<style scoped>

</style>