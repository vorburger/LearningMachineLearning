import{d as a,z as i,o as l,b as c,f as d,h as u}from"../modules/vue-CZkfEai8.js";function s(e){return e.startsWith("/")?"/LearningMachineLearning/prez/sli.dev/dist/"+e.slice(1):e}function p(e,o=!1,n="cover"){const t=e&&(e[0]==="#"||e.startsWith("rgb")),r={background:t?e:void 0,color:e&&!t?"white":void 0,backgroundImage:t?void 0:e?o?`linear-gradient(#0005, #0008), url(${s(e)})`:`url("${s(e)}")`:void 0,backgroundRepeat:"no-repeat",backgroundPosition:"center",backgroundSize:n};return r.background||delete r.background,r}const g=a({__name:"image",props:{image:{type:String},backgroundSize:{type:String,default:"cover"}},setup(e){const o=e,n=i(()=>p(o.image,!1,o.backgroundSize));return(t,r)=>(l(),c("div",{class:"slidev-layout w-full h-full",style:u(n.value)},[d(t.$slots,"default")],4))}});export{g as _};
