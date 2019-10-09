var app = new Vue({
    el: '#appfatayo',
    data: {
        form: {
            nom: '',
            email: '',
            sujet: '',
            message: '',

        }
    },
    delimiters: ["${", "}"],
    mounted(){
        // this.getContact()
    },
    methods: {
        // Pour faire le POST vers notre API
        onSubmit(evt){
            evt.preventDefault()

            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = 'X-CSRFToken'

            const path = `http://127.0.0.1:8000/contact/contactapi/`
                
            axios.post(path, this.form)
            .then(response => { 
                // console.log(response) 
                this.form.nom = response.data.nom
                this.form.email = response.data.email
                this.form.sujet = response.data.sujet
                this.form.message = response.data.message  
                
                swal("Merci!", "Votre formulaire contact a ete soumis avec succes!", "success");

                this.form.nom = ''
                this.form.email = ''
                this.form.sujet = ''
                this.form.message = ''

            })
            .catch(error => {
                console.log(error.response)
            });
        },


            // Pour Afficher les elements a partir de notre API

        // getContact: function (){
        //     const path = `http://127.0.0.1:8000/contact/contactapi/6/`
            
        //     axios.get(path)
        //     .then((reponse) => {
        //         this.form.name = reponse.data.nom
        //         this.form.email = reponse.data.email
        //         this.form.sujet = reponse.data.sujet
        //         this.form.message = reponse.data.message
        //     })
        //     .catch((error) => {
        //         console.log(error)
        //     })
        // }

    },
            
});







var appnewletter = new Vue({
    el: '#appfatayonewletter',
    data: {
        form: {
            email: '',
        }
    },
    delimiters: ["${", "}"],
    mounted(){

    },
    methods: {
        onSubmit(evt){
            evt.preventDefault()

            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = 'X-CSRFToken'

            const path = `http://127.0.0.1:8000/contact/newslletterapi/`
                
            axios.post(path, this.form)
            .then(response => { 

                this.form.email = response.data.email                
                swal("Merci d'avoir souscrire au Newsletter", "", "success");

                this.form.email = ''

            })
            .catch(error => {
                console.log(error.response.data)
            });
        },

    },
            
});


