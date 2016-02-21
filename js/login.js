var main = function(){
	//alert('hello');
	login_btn = $('#login-btn');
	login_btn.click(function(event){
		username = $('#usuario').val();
		password = $('#password').val();
		//alert(password);
		if(username === 'jose' && password === 'jose'){
			window.loaction.href = './index.html';
		}else{
			event.preventDefault();
			error = $('#login-error');
			error.text("Usuario no registrado, prueba con usuario: jose, clave:jose");
			error.parents('.row').removeClass("hidden");
			setTimeout(function(){$('#login-error').parents('.row').fadeOut(500)}, 5000);
		}
	});

	$('input').keypress(function(e) {
	    if(e.which == 13) {
	        login_btn.trigger('click');
	    }
	});

	

}

$(document).ready(main);