var cliente = $("#cliente").bootstrapValidator({
     feedbackIcons: {
         valid: 'glyphicon glyphicon-ok',
         invalid: 'glyphicon glyphicon-remove',
         validating: 'glyphicon glyphicon-refresh'
     },
     fields: {
        cedula:{
            validators: {
                notEmpty:{
                    message: 'Cedula es requerida'
                },
                regexp: {
                     regexp: /^[0-9]+$/,
                     message: 'Campo cedula solo puede contener numeros'
                 },
                callback: {
                    message: 'Cliente no registrado',
                    callback: function(value, validator, $field){
                        valid = false;
                        $.ajax({
                            method: 'get',
                            url: domain_url + '/api/cliente/' + value,
                            async: false,
                            success: function(data){
                                console.log(data.nombre + " " + data.apellido);
                                valid = true;
                                cliente_nombre = $('#cliente-nombre');
                                cliente_nombre.html(data.nombre + " " + data.apellido);
                                if(cliente_nombre.parents('.row').nextAll().is(':hidden')){
                                    cliente_nombre.parents('.row').nextAll().slideDown(500);
                                }
                            },
                            error: function(){
                                valid = false;
                                cliente_nombre = $('#cliente-nombre');
                                cliente_nombre.html("");
                                if(cliente_nombre.parents('.row').nextAll().is(':visible')){
                                    cliente_nombre.parents('.row').nextAll().slideUp(500);
                                }
                            }
                        });
                        return valid;
                    }
                }
            }
        }

     }
});

$('#productoForm').bootstrapValidator({
    feedbackIcons: {
         valid: 'glyphicon glyphicon-ok',
         invalid: 'glyphicon glyphicon-remove',
         validating: 'glyphicon glyphicon-refresh'
    },
    fields:{
        producto_codigo_input:{
            validators: {
                regexp: {
                     regexp: /^[0-9]+$/,
                     message: 'Solo puede contener numeros'
                },
                notEmpty:{
                    message: 'Campo requerido'
                }
                
            }
        },
        producto_nombre_input:{
            validators: {
                notEmpty:{
                    message: 'Campo requerido'
                }
            }
        }
    }
})

function only_one_input(){
    $('input:radio').on('change', function() {
        $('input:radio').each(function(){
            if($(this).is(':checked')){
                input = $(this).parents('.form-group').children('input');
                input.removeAttr("disabled");
                input.focus();
            }else{
                input = $(this).parents('.form-group').children('input');
                input.attr("disabled", true);


            }
        });
        
    });
    $('input:radio').first().attr('checked', 'true');
    $('input:radio').trigger("change");
}

only_one_input();