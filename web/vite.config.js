import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src') // ✅ BU SATIR GEREKLİ @ dediğimizde ./src arasın diye
    }
  }
})
