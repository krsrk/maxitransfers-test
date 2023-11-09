export default defineNuxtConfig({
    devtools: {enabled: false},
    imports: {
        dirs: ['@/src/stores'],
    },
    modules: [
        [
            '@pinia/nuxt',
            {
                autoImports: ['defineStore', 'acceptHMRUpdate']
            }
        ],
    ],
    css: [
        '@/node_modules/vuetify/lib/styles/main.sass',
        '@mdi/font/css/materialdesignicons.min.css',
    ],
    build: {
        transpile: ['vuetify'],
    },
})
