import{e as p,o as u,b as f,a as e,t as a,f as d,g as l,v as n,F as h,j as r}from"./index.a6cde548.js";const b={class:"container mb-5"},_={class:"row"},g={class:"col-md-3"},y={class:"d-flex flex-column p-4 py-6 align-items-center text-center img_container"},v=["src"],w={class:"font-weight-bold"},S={class:"text-black-50"},F={class:"text-black-50"},I={class:"col-md-5 border-right"},P={class:"p-3"},k=e("div",{class:"d-flex justify-content-between align-items-center mb-3"},[e("h4",{class:"text-right"},"Edit Profile")],-1),T={class:"row mt-3"},D={class:"col-md-6"},U=e("label",null,"Name",-1),V={class:"col-md-6"},C=e("label",null,"Surname",-1),j={class:"col-md-6"},O=e("label",null,"DOB",-1),$=e("div",{class:"col-md-6"},[e("label",null,"Password")],-1),B=e("div",{class:"row mt-6"},null,-1),N=e("div",{class:"mt-3"},[e("button",{class:"btn btn-primary profile-button",type:"submit"}," Save Profile ")],-1),E=e("button",{class:"btn btn-primary profile-button",type:"submit"},"Upload Image",-1),H={class:"container align-items-center mt-5"},R={class:"row"},X=e("h4",null,"Add Items",-1),A={class:"row mt-2"},J={class:"col-md-3 mb-5"},M={class:"col-md-3 mb-5"},G=e("label",{for:"item"},"Item end date",-1),q={class:"col-md-6"},z=e("div",{class:"d-flex justify-content-between align-items-center mt-3"},[e("button",{type:"submit",class:"btn btn-primary mb-5 btn-sm"},"Submit Item")],-1),K={data(){return{details:this.get_details(),name:"",surname:"",dob:"",file:"",title:"",price:"",end_date:"",item_image:"",description:"",$refs:{file:{files:[]},itemFile:{files:[]}}}},methods:{async get_details(){const t=await(await fetch("http://localhost:8000/bidder/api/profile/",{method:"GET",credentials:"include",mode:"cors",referrerPolicy:"no-referrer"})).json();this.details=t},async updateImg(){console.log("string");const i=new FormData;i.append("file",this.file);const t=new Headers([["X-CSRFToken",r("csrftoken")]]),o=await(await fetch("http://localhost:8000/bidder/api/profile/",{method:"POST",credentials:"include",mode:"cors",referrerPolicy:"no-referrer",headers:t,body:i})).json();this.details.image_name=o.image},async uploadFile(){this.file=this.$refs.file.files[0]},async edit(){const i=Date.parse(this.dob),t=new Headers([["X-CSRFToken",r("csrftoken")]]);await fetch("http://localhost:8000/bidder/api/profile/",{method:"PUT",credentials:"include",mode:"cors",referrerPolicy:"no-referrer",headers:t,body:JSON.stringify({name:this.name,surname:this.surname,date_of_birth:i})})},async item(){let i=new Date(this.end_date).getTime();const t=new Headers([["X-CSRFToken",r("csrftoken")]]),m=(await(await fetch("http://localhost:8000/bidder/api/profile/",{method:"POST",credentials:"include",mode:"cors",referrerPolicy:"no-referrer",headers:t,body:JSON.stringify({title:this.title,price:this.price,final_date:i,description:this.description})})).json()).id;console.log(m);const c=new FormData;c.append("file",this.item_image),await fetch(`http://localhost:8000/bidder/api/profile/${m}`,{method:"POST",credentials:"include",mode:"cors",referrerPolicy:"no-referrer",headers:t,body:c})},async uploadItemImg(){this.item_image=this.$refs.itemFile.files[0]}}},Q=p({...K,__name:"index",setup(i){return(t,s)=>(u(),f(h,null,[e("div",b,[e("div",_,[e("div",g,[e("div",y,[e("img",{class:"img-fluid",src:`http://localhost:8000/static/${t.details.image_name}`},null,8,v),e("span",w,a(t.details.name),1),e("span",S,a(t.details.surname),1),e("span",null,[e("span",F,a(t.details.email),1)])])]),e("div",I,[e("form",{class:"form-outline",onSubmit:s[5]||(s[5]=d((...o)=>t.edit&&t.edit(...o),["prevent"]))},[e("div",P,[k,e("div",T,[e("div",D,[U,l(e("input",{type:"text",class:"form-control","onUpdate:modelValue":s[0]||(s[0]=o=>t.name=o),placeholder:"first name"},null,512),[[n,t.name]])]),e("div",V,[C,l(e("input",{type:"text",class:"form-control","onUpdate:modelValue":s[1]||(s[1]=o=>t.surname=o),placeholder:"surname"},null,512),[[n,t.surname]])]),e("div",j,[O,l(e("input",{type:"date",class:"form-control","onUpdate:modelValue":s[2]||(s[2]=o=>t.dob=o),placeholder:"date of birth"},null,512),[[n,t.dob]])]),$]),B,N]),e("form",{onSubmit:s[4]||(s[4]=d((...o)=>t.updateImg&&t.updateImg(...o),["prevent"]))},[e("input",{type:"file",ref:"file",onChange:s[3]||(s[3]=(...o)=>t.uploadFile&&t.uploadFile(...o))},null,544),E],32)],32)])])]),e("form",{class:"form-outline",onSubmit:s[11]||(s[11]=d((...o)=>t.item&&t.item(...o),["prevent"]))},[e("div",H,[e("div",R,[X,e("div",A,[e("div",J,[l(e("input",{type:"text","onUpdate:modelValue":s[6]||(s[6]=o=>t.title=o),class:"form-control",placeholder:"title"},null,512),[[n,t.title]])]),e("div",M,[l(e("input",{type:"text","onUpdate:modelValue":s[7]||(s[7]=o=>t.price=o),class:"form-control",placeholder:"starting price"},null,512),[[n,t.price]])]),e("div",null,[G,l(e("input",{type:"datetime-local","onUpdate:modelValue":s[8]||(s[8]=o=>t.end_date=o),id:"item",name:"birthday"},null,512),[[n,t.end_date]])]),e("div",null,[e("input",{type:"file",ref:"itemFile",onChange:s[9]||(s[9]=(...o)=>t.uploadItemImg&&t.uploadItemImg(...o))},null,544)])]),e("div",q,[l(e("textarea",{class:"form-control","onUpdate:modelValue":s[10]||(s[10]=o=>t.description=o),placeholder:"Add description",rows:"3"},null,512),[[n,t.description]])]),z])])],32)],64))}});export{Q as default};
