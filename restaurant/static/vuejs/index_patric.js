Vue.component('card_items',{
    delimiters:["${","}"],
    template:`
    <div class="col-4">
        <a href="#" class="thumb-menu">
            <img class="img-fluid img-cover" :src='item.image' />
            <h6>`+" ${item.description}  "+` </h6>
        </a>
    </div>
    `,
    props:['item']
})
Vue.component('working',{
    delimiters:["${","}"],
    template:`
    <li class="d-flex justify-content-between"><span>`+"${item.day}"+`</span><span> `+"${item.openHours} " +` - `+"${item.closeHours} " +` </span></li>
    `,
    props:['item']
})
var principal= new Vue({ 
    el: '#pri',
    data: {
        exemple:'pentest extemple ',
        message: 'You Pentest this page on ' + new Date().toLocaleString(),
        logoUrl:null,
        headerText:null,
        movieUrl:null,
        imageTesti:null,
        imageResrvation:null,
        foorTerText:null,
        newsLaterText:null,
        sladerImage:[],
        myImg1:'',
        myImg2:'',
        myImg3:'',
        aboutImg:'',
        aboutHeader:'',
        aboutImg:'',
        aboutDescription:'',
        imagesSpecialiste:[],
        workingH:[],
        info:[],
    },
    delimiters: ["${", "}"],
    mounted(){
        this.get_allFront(),
        this.get_menu(),
        this.get_about(),
        this.get_specialiste(),
        this.get_workingHours()
    },
    methods: {

        get_allFront:function(){
            axios.get('http://127.0.0.1:8000/config/allfront/')
            .then(response => {
                // console.log(response.data[0]),
                this.logoUrl=response.data[0].logo,
                this.headerText=response.data[0].headerText,
                this.movieUrl=response.data[0].movieInto,
                this.imageTesti=response.data[0].imageTesti,
                this.imageResrvation=response.data[0].imageReservations,
                this.foorTerText=response.data[0].footText,
                this.newsLaterText=response.data[0].newsletterText
                this.movieUrl=this.movieUrl.replace("watch", "/embed/");
                console.log(response.data[0].logo)
                console.log(this.logoUrl+'\n'+ this.headerText +'\n'+this.movieUrl+'\n'+this.imageTesti+'\n'+this.imageResrvation+'\n'+this.foorTerText+'\n'+this.newsLaterText)
            })
            .catch((err) => {   
                console.log(err);
            })
        },
        get_menu:function(){
            axios.get('http://127.0.0.1:8000/menuapi/')
            .then(response=>{
                
                for (i=0;i <3 ;i++){
                    this.sladerImage.push(response.data[i]);
                }
                this.myImg3=this.sladerImage[0].image
                this.myImg1=this.sladerImage[1].image
                this.myImg2=this.sladerImage[2].image
                Console.log('Slide image'+this.sladerImage)
            })
            .catch((err)=>{
                console.log(err)
            })
        },
        get_about:function(){
            axios.get('http://127.0.0.1:8000/config/about/')
            .then(response=>{
               this.aboutHeader=response.data[0].headerText
               this.aboutImg=response.data[0].image
               this.aboutDescription=response.data[0].description
            })
            .catch((err)=>{
                console.log(err)
            })
        },
        get_specialiste:function(){
            axios.get('http://127.0.0.1:8000/specialapi/')
            .then(response=>{
                
                for(i=0;i<3;i++){
                    this.imagesSpecialiste.push(response.data[i]);
                }
            })
            .catch(err=>{
                console.log(err)
            })
        },
        get_workingHours:function(){
            axios.get('http://127.0.0.1:8000/config/works/')
            .then(response=>{
                for(i=0;i<7;i++){
                    this.workingH.push(response.data[i])
                }
            })
            .catch(err=>{
                console.log(err)
            })
        },
        get_info:function(){
            axios.get('http://127.0.0.1:8000/config/info/')
            .then(response=>{
                // this.info=response.data
                console.log(response)
            })
            .catch(err=>{
                console.log(err)
            })
        }
        
        
    },  
            
});

        