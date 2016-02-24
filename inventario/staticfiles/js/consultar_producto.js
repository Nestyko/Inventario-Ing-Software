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

var main = function(){
    only_one_input();

    $('#submit-btn').click(function(event){
        event.preventDefault();
        info = $('input:radio:checked').parents('.form-group').children('input').val();
        if($('input:radio:checked').attr('id') === 'codigo-option'){
            data = {'codigo' : info};
        }else{
            data = {'nombre' : info}
        }
        $.ajax({
            url: domain_url +'api/productos',
            method: 'GET',
            data: data,
            success: function(response){
                alert(response);
            },
            error: function(response){
                alert(reponse);
            }
            });
    });
}


$(document).ready(main);
