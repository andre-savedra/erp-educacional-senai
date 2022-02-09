export default {
    // Global page headers: https://go.nuxtjs.dev/config-head
    ssr: false,
    head: {
        title: 'FIAP',
        htmlAttrs: {
            lang: 'pt_br'
        },
        meta: [
            { charset: 'utf-8' },
            { name: 'viewport', content: 'width=device-width, initial-scale=1' },
            { hid: 'description', name: 'description', content: '' },
            { name: 'format-detection', content: 'telephone=no' }
        ],
        link: [
            { rel: 'icon', type: 'image/x-icon', href: '/favicon.png' },
            { rel: 'stylesheet', type: 'text/css', href: 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css' },
        ]
    },

    // Global CSS: https://go.nuxtjs.dev/config-css
    css: [
        '@/layouts/css/primeflex.min.css',
        '@/layouts/scss/generalStyle.scss'
    ],

    dir: {

    },

    // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
    plugins: [],

    // Auto import components: https://go.nuxtjs.dev/config-components
    components: true,

    // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
    buildModules: [],

    primevue: {
        theme: 'saga-blue',
        ripple: true,
        components: [
            'Button', 'Chart', 'ProgressBar', 'Knob'
        ]
    },

    // Modules: https://go.nuxtjs.dev/config-modules
    modules: [
        // https://go.nuxtjs.dev/axios
        '@nuxtjs/axios',
        'primevue/nuxt',
    ],

    // Axios module configuration: https://go.nuxtjs.dev/config-axios
    axios: {},

    // Build Configuration: https://go.nuxtjs.dev/config-build
    build: {
        loaders: {
            sass: {
                implementation: require('sass'),
            },
            scss: {
                implementation: require('sass'),
            },
        },
    }
}