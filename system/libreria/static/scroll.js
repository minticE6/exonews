window.addEventListener("scroll", function(){
    var header = document.querySelector(".home-section")
    header.classList.toggle("abajo",this.window.scrollY>0);
})