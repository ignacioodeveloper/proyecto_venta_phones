

// google map API
// inicializar map 
function initMap() {
    
  // latitud de smartphonestore
  // av andres bello 2425
  const ubicacion_tienda = { lat: -33.41754, lng: -70.60557 };
  

  // centrar y dar zoom al mapa
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 15,
    center: ubicacion_tienda,
  });
  // markador y posisionamiento 
  const marker = new google.maps.Marker({
    position: ubicacion_tienda,
    map: map,
  });
}






$(document).ready(function(){
  $('.responsive').slick({
    dots: true,
    infinite: true,
    speed: 300,
    slidesToShow: 4,
    slidesToScroll: 4,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3,
          infinite: true,
          dots: true
        }
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
    ]
  });
});







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
    const imagery_el = document.querySelector('.imagery');
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
        imagery_el.style.backgroundColor = this.dataset.colour;
      });
    }
  }