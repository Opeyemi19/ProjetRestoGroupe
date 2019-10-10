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

                                                                                                            Vue.component('working_hours', {
                                                                                                                template: "#working-hours",
                                                                                                                delimiters : ["${","}"],
                                                                                                            });
Vue.component('banner_field', {
template: "#banner-field",
delimiters : ["${","}"],
});


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
    el: '#sessionabout',
    
    data: {
        specialdis: [

        ],
        menuis : [

        ],
        about : [

        ],
        
        
    },
    delimiters: ["${", "}"],
    mounted(){
        this.getspecialdish()
        this.getmenuis()
        this.getaboutinfos()
       
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

        getmenuis: function(){
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
        // getallteami: function(){
        //     axios.get('http://127.0.0.1:8000/personnel/teamapi/')
        //     .then(response => {
        //         console.log(response.data)
        //         this.teamis   = response.data
                
        //     })
        //     .catch((err) => {
        //         console.log(err);
        //     })

           
        // },

        // getpostei: function(){
        //     axios.get('http://127.0.0.1:8000/personnel/posteapi/')
        //     .then(response => {
        //         console.log(response.data)
        //         this.posteis  = response.data
                
                
        //     })
        //     .catch((err) => {
        //         console.log(err);
        //     })
        
        // },
        
        
                   
    },
        
});


                                                                                {/* create app for get special dish      */}
                                                                                var app = new Vue({
                                                                                    el: '#workinghours',
                                                                                    
                                                                                    data: {
                                                                                        
                                                                                        workinghours :[

                                                                                        ],
                                                                                       
                                                                                    },
                                                                                    delimiters: ["${", "}"],
                                                                                    mounted(){
                                                                                        this.getworkinghours()
                                                                                    },
                                                                                    methods: {
                                                                                                
                                                                                        // hello: function () {
                                                                                        //     console.log('Hello')
                                                                                        // },

                                                                                       
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

                                                                                {/* create app for get special dish      */}
                                                                                var app = new Vue({
                                                                                    el: '#header',
                                                                                    
                                                                                    data: {
                                                                                        
                                                                                        allfront : [

                                                                                        ],

                                                                                    },
                                                                                    delimiters: ["${", "}"],
                                                                                    mounted(){
                                                                                        
                                                                                        this.getallfront()
                                                                                    },
                                                                                    methods: {
                                                                                                
                                                                                        // hello: function () {
                                                                                        //     console.log('Hello')
                                                                                        // },

                                                                                       
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
    el: '#bann',
    
    data: {
        
        banners : [

        ],

    },
    delimiters: ["${", "}"],
    mounted(){
        
        this.getbanner()
    },
    methods: {
                
        // hello: function () {
        //     console.log('Hello')
        // },

       
        getbanner: function(){
            axios.get('http://127.0.0.1:8000/config/bannerapi/')
                .then(response => {
                    console.log(response.data)
                    this.banners=response.data;
                })
                .catch((err) => {
                    console.log(err);
                })
        },
        
        
    },
        
});

                                                                                                var app = new Vue({
                                                                                                    el: '#sessionmenu',
                                                                                                    data: {
                                                                                                        categos : [],
                                                                                                    },
                                                                                                    delimiters: ["${", "}"],
                                                                                                    mounted(){
                                                                                                        this.getcategos()
                                                                                                    },
                                                                                                    methods: {
                                                                                                        getcategos: function(){
                                                                                                            axios.get('http://127.0.0.1:8000/categorieapi/')
                                                                                                            .then(response => {
                                                                                                                // console.log(response.data)
                                                                                                                this.categos  = response.data
                                                                                                                
                                                                                                            })
                                                                                                            .catch((err) => {
                                                                                                                console.log(err);
                                                                                                            })
                                                                                                        }
                                                                                                                        
                                                                                                    },
                                                                                                            
                                                                                                });
var app = new Vue({
    el: '#today',
    data: {
        categos : [],
        today :'today'.toLowerCase()
    },
    delimiters: ["${", "}"],
    mounted(){
        this.getcategos()
        this.gettoday()
    },
    methods: {
        getcategos: function(){
            axios.get('http://127.0.0.1:8000/categorieapi/')
            .then(response => {
                // console.log(response.data)
                this.categos  = response.data
                
            })
            .catch((err) => {
                console.log(err);
            })
        },

        gettoday: function(){
            var ladate=new Date()
            var tab_jour=new Array("dimanche", "lundi", "mardi", "mercredi", "Jeudi", "vendredi", "samedi");
            this.today = tab_jour[ladate.getDay()]
            console.log(this.today)
        }
                        
    },
            
});

                                                                                    {/* create app for get special dish      */}
                                                                                    var app = new Vue({
                                                                                        el: '#sessionspd',
                                                                                        
                                                                                        data: {
                                                                                            spdishs: [

                                                                                            ],
                                                                                            repas : [

                                                                                            ],
                                                                                            
                                                                                        },
                                                                                        delimiters: ["${", "}"],
                                                                                        mounted(){
                                                                                            this.getrepas()
                                                                                            this.getspdish()
                                                                                        },
                                                                                        methods: {
                                                                                                    
                                                                                            // hello: function () {
                                                                                            //     console.log('Hello')
                                                                                            // },

                                                                                            getspdish: function(){
                                                                                                axios.get('http://127.0.0.1:8000/specialapi/')
                                                                                                    .then(response => {
                                                                                                        console.log(response.data)
                                                                                                        this.spdishs=response.data;


                                                                                                    })
                                                                                                    .catch((err) => {
                                                                                                        console.log(err);
                                                                                                    })
                                                                                            },

                                                                                            getrepas: function(){
                                                                                                axios.get('http://127.0.0.1:8000/menuapi/')
                                                                                                    .then(response => {
                                                                                                        console.log(response.data)
                                                                                                        this.repas=response.data;

                                                                                                    })
                                                                                                    .catch((err) => {
                                                                                                        console.log(err);
                                                                                                    })
                                                                                            }
                                                                                                            
                                                                                        },
                                                                                            
                                                                                    });

var app = new Vue({
    el: '#sessionteam',
    data: {
        members:[],
        occupations:[],
    },
    delimiters: ["${", "}"],
    mounted(){
        this.getmembers()
        this.getoccupations()
    },
    methods: {
        getmembers: function(){
            axios.get('http://127.0.0.1:8000/personnel/teamapi/')
            .then(response => {
                this.members   = response.data
                // console.log(response.data)
                
            })
            .catch((err) => {
                console.log(err);
            })

            
        },

        getoccupations: function(){
            axios.get('http://127.0.0.1:8000/personnel/posteapi/')
            .then(response => {
                this.occupations  = response.data
                console.log(response.data)
                
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
                                                                                            
                                                                                            footerinfos :[

                                                                                            ],
                                                                                            aboutinfooter :[

                                                                                            ],
                                                                                            socialnetwork :[

                                                                                            ],
                                                                                            
                                                                                        
                                                                                        },
                                                                                        delimiters: ["${", "}"],
                                                                                        mounted(){
                                                                                            this.getfooterinfos()
                                                                                            this.getsocialnetwork()
                                                                                            this.getaboutinfooter()
                                                                                        },
                                                                                        methods: {
                                                                                                    
                                                                                            // hello: function () {
                                                                                            //     console.log('Hello')
                                                                                            // },

                                                                                        
                                                                                            getfooterinfos: function(){
                                                                                                axios.get('http://127.0.0.1:8000/config/allfront/')
                                                                                                    .then(response => {
                                                                                                        console.log(response.data)
                                                                                                        this.footerinfos=response.data;
                                                                                                    })
                                                                                                    .catch((err) => {
                                                                                                        console.log(err);
                                                                                                    })
                                                                                            },    
                                                                                            getsocialnetwork: function(){
                                                                                                axios.get('http://127.0.0.1:8000/config/info/')
                                                                                                    .then(response => {
                                                                                                        console.log(response.data)
                                                                                                        this.socialnetwork=response.data;
                                                                                                    })
                                                                                                    .catch((err) => {
                                                                                                        console.log(err);
                                                                                                    })
                                                                                            },    
                                                                                            getaboutinfooter: function(){
                                                                                                axios.get('http://127.0.0.1:8000/config/about/')
                                                                                                    .then(response => {
                                                                                                        console.log(response.data)
                                                                                                        this.aboutinfooter=response.data;
                                                                                                    })
                                                                                                    .catch((err) => {
                                                                                                        console.log(err);
                                                                                                    })
                                                                                            },                  
                                                                                        },
                                                                                            
                                                                                    });