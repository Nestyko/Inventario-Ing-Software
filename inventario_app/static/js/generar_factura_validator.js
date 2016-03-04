$("#cliente").bootstrapValidator({
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
                 }
            }
        }
     }
});