$('#registrationForm').bootstrapValidator({
	 feedbackIcons: {
		 valid: 'glyphicon glyphicon-ok',
		 invalid: 'glyphicon glyphicon-remove',
		 validating: 'glyphicon glyphicon-refresh'
	 },
	 fields: {
	 	cedula:{
	 		validators:{
	 			notEmpty:{
	 				message: 'Cedula es requerida'
	 			},
	 			regexp: {
					 regexp: /^[0-9]+$/,
					 message: 'Campo cedula solo puede contener numeros'
				 }
	 		}
	 	},
		 nombre: {
			 validators: {
				 notEmpty: {
					 message: 'El nombre es requerido'
				 }
			 }
		 },
		 apellido: {
			 validators: {
				 notEmpty: {
					 message: 'El apellido es requerido'
				 }
			 }
		 },
		 email: {
			 validators: {
				 notEmpty: {
					 message: 'El correo es requerido y no puede estar vacio'
				 },
				 emailAddress: {
					 message: 'El correo electronico no es valido'
				 }
			 }
		 },
		 password: {
			 validators: {
				 notEmpty: {
					 message: 'El password es requerido y no puede ser vacio'
				 },
				 stringLength: {
					 min: 8,
					 message: 'El password debe contener al menos 8 caracteres'
				 },
				 regexp: {
					 regexp: /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{8,}$/,
					 message: 'Debe contener al menos 8 caracteres compuestos de letras (al menos una mayuscula y minuscula) y numeros'
				 }
	
				 
			 }
		 },
		 repeat_password: {
		 	validators:{
		 		notEmpty: {
		 			message: 'Repita la constraseña por favor'
		 		},
		 		callback:{
		 			message: 'Contraseñas no coinciden',
		 			callback: function(value, validator, $field){
		 				if(value == $('#password').val()){
		 					return {valid:false,
		 						message: ' Contraseñas no coinciden'}
		 				}
		 			}
		 		}
		 	}
		 },
		 telefono: {
			 message: 'El teléfono no es valido',
			 validators: {
				 notEmpty: {
					 message: 'El teléfono es requerido y no puede ser vacio'
				 },
				 regexp: {
					 regexp: /^[0-9]+$/,
					 message: 'El teléfono solo puede contener números'
				 }
			 }
		 },
		username:{
		 	message: 'El usuario es requerido',
		 	validators:{
		 		notEmpty:{
		 			message: 'No puede estar vacío el campo de usuario'
		 		}

		 	}
		 }
	 }
});
