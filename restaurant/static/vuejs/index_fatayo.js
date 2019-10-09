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




var jour_reservation = new Vue({
    el: '#reserve_formulair',
    data: {
        form: {
            nom: '',
            email: '',
            phone: '',
            jour: '',
            heure: '',
            nbre_reservation: '',

        },
        jour_reserv: [],
        heure_reserv: [],
        person_reserv: [],
        message_reservation:[],
    },
    delimiters: ["${", "}"],
    mounted(){
        this.reservatio_jou(),
        this.reservatio_heure(),
        this.reservatio_person(),
        this.fin_reservation()

    },
    methods: {
        
        reservatio_jou: function(){

            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = 'X-CSRFToken'

            const path = `http://127.0.0.1:8000/reservet/jourapi/`

            axios.get(path)
            .then(response => {
                console.log(response.data)
                this.jour_reserv  = response.data
                
            })
            .catch((err) => {
                console.log(err);
            })
        },
         
        reservatio_heure: function(){

            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = 'X-CSRFToken'

            const path = `http://127.0.0.1:8000/reservet/heureapi/`

            axios.get(path)
            .then(response => {
                console.log(response.data)
                this.heure_reserv  = response.data
                
            })
            .catch((err) => {
                console.log(error);
            })
        },

        reservatio_person: function(){

            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = 'X-CSRFToken'

            const path = `http://127.0.0.1:8000/reservet/personapi/`

            axios.get(path)
            .then(response => {
                console.log(response.data)
                this.person_reserv  = response.data
                
            })
            .catch((error) => {
                console.log(error);
            })
        },

        onSubmit(evt){
            evt.preventDefault()

            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = 'X-CSRFToken'

            const path = `http://127.0.0.1:8000/reservet/reservationapi/`
                
            axios.post(path, this.form)
            .then(response => { 
                // console.log(response) 
                this.form.nom = response.data.nom
                this.form.email = response.data.email
                this.form.phone = response.data.phone
                this.form.jour = response.data.jour
                this.form.heure = response.data.heure
                this.form.nbre_reservation = response.data.nbre_reservation  
                
                swal("Reservation executee avec succes!", "", "success");

                this.form.nom = ''
                this.form.email = ''
                this.form.phone = ''
                this.form.jour = ''
                this.form.heure = ''
                this.form.nbre_reservation = ''

            })
            .catch(error => {
                console.log(error.response)
            });
        },

        fin_reservation: function(){

            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = 'X-CSRFToken'

            const path = `http://127.0.0.1:8000/reservet/messageresvationapi/`

            axios.get(path)
            .then(response => {
                // console.log(response.data[0].status)
                this.message_reservation = response.data[0].status
            })
            .catch((error) => {
                console.log(error);
            })
        },

    },
            
});
