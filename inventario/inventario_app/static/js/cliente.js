

function main(){
	//alert("hello");
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



$(document).ready(main());