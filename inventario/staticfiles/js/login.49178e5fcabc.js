var main = function(){
	//alert('hello');

	var showerror = function(){
		row = $('.error-row');
		if (row.find('p').text() !== ''){
			row.removeClass('hidden');
			setTimeout(function(){
				row.slideUp(500);
			}, 5000)
		}

	}
	login_btn = $('#login-btn');
	login_form = $('#login-form');

	login_form.on('change', function(){
		empty = false;
		$('input').each(function(){
			if($(this).val() === ""){
				empty = true;
			}
		});
		if (empty){
			login_btn.addClass('disabled');
		}else{
			login_btn.removeClass('disabled');
		}
	});

	$('input').keypress(function(e) {
	    if(e.which == 13) {
	        login_form.submit();
	    }
	});

	login_form.trigger('change');
	showerror();

}

$(document).ready(main());
