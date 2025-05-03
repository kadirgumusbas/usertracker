import {createRouter, createWebHistory} from 'vue-router'
import HomeView from '@/pages/HomeView.vue'
import UserTodos from '@/pages/UserTodos.vue'
import UserAlbums from "@/pages/UserAlbums.vue"
import UserPosts from "@/pages/UserPosts.vue"
import AlbumPhotos from "@/pages/AlbumPhotos.vue"

const routes = [
    {
        path: '/users',
        name: 'Home',
        component: HomeView
    },
    {
        path: '/',
        redirect: '/users',  //  Ana dizine girilince otomatik /usersa yonlendir
    },
    {
        path: '/users/:userId/todos',
        name: 'UserTodos',
        component: UserTodos
    },
    {
        path: '/users/:userId/albums',
        name: 'UserAlbums',
        component: UserAlbums
    },
    {
        path: '/users/:userId/posts',
        name: 'UserPosts',
        component: UserPosts
    },
    {
        path: '/users/:userId/albums/:albumId',
        name: 'AlbumPhotos',
        component: AlbumPhotos
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
