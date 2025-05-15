function ChangePage(value){
    if(value=='signup'){
        document.getElementById('mlog').style.display='none'
        document.getElementById('mSignup').style.display='block'
        document.getElementById('mforgetpass').style.display='none'
    }
    if(value=='login'){
        document.getElementById('mlog').style.display='block'
        document.getElementById('mSignup').style.display='none'
        document.getElementById('mforgetpass').style.display='none'
    }
    if(value=='forgetpass'){
        document.getElementById('mlog').style.display='none'
        document.getElementById('mSignup').style.display='none'
        document.getElementById('mforgetpass').style.display='block'
    }
}