

$("#formulario_contacto").validate({
    rules:{

        nombre: {
            required : true,
            minlength: 3,
            maxlength: 30

        },

        apellido: {
            required : true,
            minlength: 2,
            maxlength: 30

        },

        email: {
            required : true,
            email: true

        },



        donde_conocio: {
            required: true
        },

        mensaje: {
            required: true,
            minlength: 15,
            maxlength: 200
        }

            

    }

})



$("#enviar").click(function() {
    alert("Mensaje Enviado con Exito")

    
    // recogemos datos
    let nombre = $("#nombre").val()
    let apellido = $("#apellido").val()
    let email = $("#email").val()
    let donde_conocio = $("donde_conocio").val()
    let mensaje = $("#mensaje").val()
    let anuncio_email = $("#anuncio_email").is(":checked")

    console.log(nombre)

})
