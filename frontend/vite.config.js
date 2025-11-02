import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'
import path from 'path'

export default defineConfig({
  plugins: [svelte()],
  build: {
    outDir: '../pokemon/static/svelte',
    emptyOutDir: true,
    rollupOptions: {
      input: './src/main.js',
      output: {
        entryFileNames: 'pokemon-component.js',
        assetFileNames: 'pokemon-component.[ext]'
      }
    }
  }
})
