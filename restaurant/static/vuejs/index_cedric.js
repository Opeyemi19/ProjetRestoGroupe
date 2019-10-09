// create component for display special dish
Vue.component('special-dish', {
    template: "#special-dish",
    delimiters : ["${","}"],
});

{/* create app about for get and display about infos */}
var app = new Vue({
    el: '#about',
    
    data: {
        infos: [

        ]
    },
    delimiters: ["${", "}"],
    mounted(){
        this.getspdinfos()
    },
    methods: {
                
        // hello: function () {
        //     console.log('Hello')
        // },

        getspdinfos: function(){
            axios.get('http://127.0.0.1:8000/config/about/')
                .then(response => {
                    console.log(response.data)
                    this.infos=response.data;

                })
                .catch((err) => {
                    console.log(err);
                })
        }
                        
    },

});

{/* create app for get special dish      */}
var app = new Vue({
    el: '#specialdish',
    
    data: {
        specialdishinfos: [

        ],
        menus : [

        ],
    },
    delimiters: ["${", "}"],
    mounted(){
        this.getinfos()
        this.getmenus()
    },
    methods: {
                
        // hello: function () {
        //     console.log('Hello')
        // },

        getinfos: function(){
            axios.get('http://127.0.0.1:8000/specialapi/')
                .then(response => {
                    console.log(response.data)
                    this.specialdishinfos=response.data;

                })
                .catch((err) => {
                    console.log(err);
                })
        },

        getmenus: function(){
            axios.get('http://127.0.0.1:8000/menuapi/')
                .then(response => {
                    console.log(response.data)
                    this.menus=response.data;

                })
                .catch((err) => {
                    console.log(err);
                })
        }
                        
    },
        
});


    