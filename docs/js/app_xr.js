

// sticky menu
document.addEventListener("DOMContentLoaded", function(){
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
          document.getElementById('navbar_top').classList.add('fixed-top');
          // add padding top to show content behind navbar
          navbar_height = document.querySelector('.navbar').offsetHeight;
          document.body.style.paddingTop = navbar_height + 'px';
        } else {
          document.getElementById('navbar_top').classList.remove('fixed-top');
           // remove padding top from body
          document.body.style.paddingTop = '0';
        } 
    });
  }); 











  
  // menu iphone xr
  window.onload = function () {
    const colour_btn_els = document.querySelectorAll('.colores_iphone .colour');
    const almacenamiento_btn_els = document.querySelectorAll('.almacenamiento .size');
    const imagen_color_xr = document.querySelector('.imagery');
    const image_el = document.querySelector('.imagery .image');

    for (let i = 0; i < almacenamiento_btn_els.length; i++) {
      let btn = almacenamiento_btn_els[i];
  
      btn.addEventListener('click', function () {
        document.querySelector('.almacenamiento .size.selected').classList.remove('selected');
        this.classList.add('selected');
      });
    }
  
  
    for (let i = 0; i < colour_btn_els.length; i++) {
      let btn = colour_btn_els[i];
  
      btn.addEventListener('click', function () {
        document.querySelector('.colores_iphone .colour.selected').classList.remove('selected');
        this.classList.add('selected');
        image_el.src = "photos/iphone/iphone_xr/iphone_xr_" + this.dataset.name + '.png';
        imagen_color_xr.style.backgroundColor = this.dataset.colour;
      });
    }
  }