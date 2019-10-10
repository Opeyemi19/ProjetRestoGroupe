// create component for display special dish
Vue.component('special-dish', {
    template: "#special-dish",
    delimiters : ["${","}"],
});

                                                                                                            Vue.component('speciald_about', {
                                                                                                                template: "#speciald-about",
                                                                                                                delimiters : ["${","}"],
                                                                                                            });

Vue.component('about_index', {
    template: "#about-index",
    delimiters : ["${","}"],
});

                                                                                                            // Vue.component('working_hours', {
                                                                                                            //     template: "#working-hours",
                                                                                                            //     delimiters : ["${","}"],
                                                                                                            // });
{/* create app about for get and display about infos */}
var app = new Vue({
    el: '#about',
    
    data: {
        infos: [

        ],
        specialdishinfos : [

        ],
        menus : [

        ]
    },
    delimiters: ["${", "}"],
    mounted(){
        this.getspdinfos()
        this.getspdinfosa()
        this.getmenusa()
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
        },
        getspdinfosa: function(){
            axios.get('http://127.0.0.1:8000/specialapi/')
                .then(response => {
                    console.log(response.data)
                    this.specialdishinfos=response.data;


                })
                .catch((err) => {
                    console.log(err);
                })
        },

        getmenusa: function(){
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

                                                                                {/* create app for get special dish      */}
                                                                                var app = new Vue({
                                                                                    el: '#specialdish',
                                                                                    
                                                                                    data: {
                                                                                        specialdishinfos: [

                                                                                        ],
                                                                                        menus : [

                                                                                        ],
                                                                                        counter:0
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



{/* create app for get special dish      */}
var app = new Vue({
    el: '#index',
    
    data: {
        specialdis: [

        ],
        menuis : [

        ],
        about : [

        ],
        allfront : [

        ]
    },
    delimiters: ["${", "}"],
    mounted(){
        this.getspecialdish()
        this.getmenusi()
        this.getaboutinfos()
        this.getallfront()
    },
    methods: {
                
        // hello: function () {
        //     console.log('Hello')
        // },

        getspecialdish: function(){
            axios.get('http://127.0.0.1:8000/specialapi/')
                .then(response => {
                    console.log(response.data)
                    this.specialdis=response.data;
                })
                .catch((err) => {
                    console.log(err);
                })
        },

        getmenusi: function(){
            axios.get('http://127.0.0.1:8000/menuapi/')
                .then(response => {
                    console.log(response.data)
                    this.menuis=response.data;

                })
                .catch((err) => {
                    console.log(err);
                })
        },
        getaboutinfos: function(){
            axios.get('http://127.0.0.1:8000/config/about/')
                .then(response => {
                    console.log(response.data)
                    this.about=response.data;
                })
                .catch((err) => {
                    console.log(err);
                })
        },
        getallfront: function(){
            axios.get('http://127.0.0.1:8000/config/allfront/')
                .then(response => {
                    console.log(response.data)
                    this.allfront=response.data;
                })
                .catch((err) => {
                    console.log(err);
                })
        },
        
                   
    },
        
});


                                                                                {/* create app for get special dish      */}
                                                                                var app = new Vue({
                                                                                    el: '#footerinfos',
                                                                                    
                                                                                    data: {
                                                                                        footerinfos: [

                                                                                        ],
                                                                                        workinghours :[

                                                                                        ],
                                                                                       
                                                                                    },
                                                                                    delimiters: ["${", "}"],
                                                                                    mounted(){
                                                                                        this.getfooterinfos()
                                                                                        this.getworkinghours()
                                                                                    },
                                                                                    methods: {
                                                                                                
                                                                                        // hello: function () {
                                                                                        //     console.log('Hello')
                                                                                        // },

                                                                                        getfooterinfos: function(){
                                                                                            axios.get('http://127.0.0.1:8000/config/about/')
                                                                                                .then(response => {
                                                                                                    console.log(response.data)
                                                                                                    this.footerinfos=response.data;
                                                                                                })
                                                                                                .catch((err) => {
                                                                                                    console.log(err);
                                                                                                })
                                                                                        },
                                                                                        getworkinghours: function(){
                                                                                            axios.get('http://127.0.0.1:8000/config/works/')
                                                                                                .then(response => {
                                                                                                    console.log(response.data)
                                                                                                    this.workinghours=response.data;
                                                                                                })
                                                                                                .catch((err) => {
                                                                                                    console.log(err);
                                                                                                })
                                                                                        },                  
                                                                                    },
                                                                                        
                                                                                });
{/* create app for get special dish      */}
var app = new Vue({
    el: '#logo',
    
    data: {
        header : [

        ]
    },
    delimiters: ["${", "}"],
    mounted(){
        this.getlogo()
    },
    methods: {
                
        // hello: function () {
        //     console.log('Hello')
        // },
        getlogo: function(){
            axios.get('http://127.0.0.1:8000/config/allfront/')
                .then(response => {
                    console.log(response.data)
                    this.header=response.data;
                })
                .catch((err) => {
                    console.log(err);
                })
        },
        
                   
    },
        
});                                                                              