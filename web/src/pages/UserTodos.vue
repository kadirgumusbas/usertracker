<script setup>

import {onMounted, watch, computed} from 'vue'
import {useRoute} from 'vue-router'
import {useTodoStore} from '@/stores/todoStore.js'

const route = useRoute()
const userId = computed(() => parseInt(route.params.userId))
const todoService = useTodoStore()

onMounted(async () => {
  await loadTodos()
})

watch(userId, async () => {
  await loadTodos()
})

async function loadTodos() {
  await todoService.getTodos(userId.value)
  if (todoService.todos.length === 0) {
    await todoService.fetchTodos(userId.value)
  }
}

</script>

<template>
  <div class="p-6 ml-5 mt-5">
    <ul class="space-y-3">
      <li
          v-for="todo in todoService.todos"
          :key="todo.id"
          class="transition-transform duration-200 hover:scale-[1.02] hover:translate-x-1 hover:shadow-md"
      >
        <label
            class="flex items-center gap-3 p-3 border border-gray-200 rounded-md cursor-pointer w-full"
        >
          <input
              type="checkbox"
              :checked="todo.completed"
              @change="todoService.setTodos(todo.id)"
              class="w-5 h-5 appearance-none border-2 border-black rounded checked:bg-purple-600 checked:border-purple-600 checked:after:content-['✔'] checked:after:text-white checked:after:flex checked:after:justify-center checked:after:items-center checked:after:h-full checked:after:w-full"
          />
          <span class="text-black">{{ todo.title }}</span>
        </label>
      </li>
    </ul>
  </div>
</template>

<style scoped>

</style>