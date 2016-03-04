


function calcular_total(){
    cantidad = $('#cantidad').val();
    precio = $('#precio_unitario').val();
    iva = precio * cantidad * 0.12;
    total = (precio * cantidad) + iva;
    $('#iva').val(iva);
    $('#total').val(total);
}

function add_quantity_and_button(row){
    row.append('<td> <input type="number" min=1 value=1 /> </td>');
    row.append('<td> <button class="btn btn-card teal-green agregar_producto_btn">Agregar</button></td>');
}

function refresh_table(productos){
    //clear table before inserting data
    tbody = $('#table-body');
    tbody.find('tr').remove();
    //cehck if theres is more than one product
    for ( var producto of productos){
            console.log(producto);
            row = $('<tr></tr>');
            tbody.append(row);
            row.append('<td>' + producto.codigo + '</td>');
            row.append('<td> <a href=\"{% url \"producto_detail\" ' + producto.codigo + '%}\">' + producto.nombre + '</a></td>');
            row.append('<td>' + producto.precio_venta + ' Bs</td>');
            add_quantity_and_button(row);
        }
    

}

//TODO: (POR HACER)
//Validar que la cantidad no exceda el maximo del producto buscado
//Validar que el codigo sea un numero
//Agregar el nombre del producto en la tabla
//Quitar descuento y cambiar todos los imputs por otro elemento no modificable(ej: parrafos, span)
//IVA y Total tienen que ser calculados
//Luego de agregar un cliente no se debe poder agregar otro.
//Agragar un boton de agregar producto, puede esta debajo de cantidad y debe estar desabilitado si el producto no se ha encontrado


var main = function(){
    
    cliente_nombre = $('#cliente-nombre');
    cliente_nombre.change(function(){
        if(cliente_nombre.html() === ''){
            cliente_nombre.parents('.row').nextAll().slideUp(500);
        }else{
            cliente_nombre.parents('.row').nextAll().slideDown(500);
        }
    });
    cliente_nombre.trigger('change');
    

    var producto_btn = $('#buscar-producto-btn');
    //alert('revisar generar_factura.js para ver tareas por hacer');
    producto_btn.click(function(event){
        event.preventDefault();
        codigo = $('producto_codigo_input').val();
        console.log(domain_url);
        console.log(codigo);
        //validar que el codigo sea numerico y que no sea nulo
        $.ajax({
            url : domain_url + '/api/productos',
            data: {codigo: codigo},
            method: 'get',
            success: function(data){
                console.log(data);
                refresh_table(data);
            },
            error: function(data){
                console.log('error');
                alert('producto, no encontrado');
            }
            

        });

    });

    $('#cantidad').on('change', calcular_total);
}





$(document).ready(main);
