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

function refresh_table(productos){
    //clear table before inserting data
    tbody = $('#table-body');
    tbody.find('tr').remove();
    //cehck if theres is more than one product
    if (productos.length > 1){
        for ( var producto of productos){
            console.log(producto);
            row = $('<tr></tr>');
            tbody.append(row);
            row.append('<td>' + producto.codigo + '</td>');
            row.append('<td>' + producto.nombre + '</td>');
            row.append('<td>' + producto.precio_venta + '</td>');
        }
    }else{
        row = $('<tr></tr>');
            tbody.append(row);
            row.append('<td>' + productos.codigo + '</td>');
            row.append('<td>' + productos.nombre + '</td>');
            row.append('<td>' + productos.precio_venta + '</td>');
    }

}

var main = function(){
    only_one_input();

    $('#submit-btn').click(function(event){
        event.preventDefault();
        var data_aux = {};
        var info = $('input:radio:checked').parents('.form-group').children('input').val();
        if($('input:radio:checked').attr('id') === 'codigo-option'){
            //var data_aux = {codigo : info};
            data_aux.codigo = info;
        }else{
            //var data_aux = {nombre : info};
            data_aux.nombre = info;
        }
        console.log(data_aux);
        $.ajax({
            url: 'http://localhost:8000/api/productos',
            data: data_aux,
            success: function(response){
                refresh_table(response);
            },
            error: function(response){
                console.log(reponse);
            }
            });
    });
}


$(document).ready(main);
