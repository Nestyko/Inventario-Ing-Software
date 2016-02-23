
function calcular_total(){
    cantidad = $('#cantidad').val();
    precio = $('#precio_unitario').val();
    iva = precio * cantidad * 0.12;
    total = (precio * cantidad) + iva;
    $('#iva').val(iva);
    $('#total').val(total);
}

function update_table(producto){
    $('#descripcion').val(producto.descripcion);
    $('#precio_unitario').val(producto.precio_venta);
    calcular_total();
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
    var producto_btn = $('#buscar-producto-btn');
    alert('revisar generar_factura.js para ver tareas por hacer');
    producto_btn.click(function(event){
        event.preventDefault();
        codigo = $('#codigo-producto').val();
        console.log(domain_url);
        console.log(codigo);
        //validar que el codigo sea numerico y que no sea nulo
        $.ajax({
            url : domain_url + '/api/productos',
            data: {codigo: codigo},
            method: 'get',
            success: function(producto){
                console.log(producto);
                update_table(producto);
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
