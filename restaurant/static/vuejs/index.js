var app = new Vue({
    el: '#app',
    data: {
        message: 'You loaded this page on ' + new Date().toLocaleString(),
    },
    delimiters: ["${", "}"],
    mounted(){
        this.hello()
    },
    methods: {
        reverseMessage: function () {
            this.message = this.message.split('').reverse().join('')
        },
                
        hello: function () {
            console.log('Hello')
        },
                        
    },
            
});
        