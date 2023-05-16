window.onscroll = function(){
    if (document.documentElement.scrollTop > 1){
        document.querySelector('.arriba-container')
        .classList.add('show');
    }else{
        document.querySelector('.arriba-container')
        .classList.remove('show');
    }
}

document.querySelector('.arriba-container').addEventListener('click',()=>{
    window.scrollTo({
        top:0,
        bahavior: 'smooth'
    })
})