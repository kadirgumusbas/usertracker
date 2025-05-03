import {defineStore} from 'pinia'
import {getRequest} from '@/services/apiService.js'

const request = 'todos'

export const useTodoStore = defineStore('todo', {
    state: () => ({
        todos: [],
    }),
    actions: {
        async fetchTodos(userId) {
            const response = await getRequest(request, userId)
            this.todos = response.data
            localStorage.setItem(`todos_user_${userId}`, JSON.stringify(this.todos)) // ilk parametre key ikinci parametre değer stringify yazıya çeviriyor
        },
        async getTodos(userId) {
            const storedTodos = localStorage.getItem(`todos_user_${userId}`)
            console.log(storedTodos)
            if (storedTodos) {
                this.todos = JSON.parse(storedTodos)
            } else {
                await this.fetchTodos(userId)
            }
        },
        setTodos(id) {
            console.log("set todos")
            const todo = this.todos.find(todo => todo.id === id)
            if (todo) {
                console.log("settodosif")
                todo.completed = !todo.completed
                localStorage.setItem(`todos_user_${todo.user}`, JSON.stringify(this.todos))
            }
        }
    }
})