var menu = new Vue({
    el: '#menu',
    data: {
        cate : [],
    },
    delimiters: ["${", "}"],
    mounted(){
        this.categorie()
    },
    methods: {
        categorie: function(){
            axios.get('http://127.0.0.1:8000/categorieapi/')
            .then(response => {
                // console.log(response.data)
                this.cate  = response.data
                
            })
            .catch((err) => {
                console.log(err);
            })
        }
                        
    },
            
});

var team = new Vue({
    el: '#team',
    data: {
       teams:[],
       postes:[],
    },
    delimiters: ["${", "}"],
    mounted(){
        this.allteam()
        this.poste()
    },
    methods: {
        allteam: function(){
            axios.get('http://127.0.0.1:8000/personnel/teamapi/')
            .then(response => {
                this.teams   = response.data
                // console.log(response.data)
                
            })
            .catch((err) => {
                console.log(err);
            })

           
        },

        poste: function(){
            axios.get('http://127.0.0.1:8000/personnel/posteapi/')
            .then(response => {
                this.postes  = response.data
                console.log(response.data)
                
            })
            .catch((err) => {
                console.log(err);
            })
        
        },
    },       
});
        

//