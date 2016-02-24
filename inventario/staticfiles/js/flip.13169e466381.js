var main = function(){
	$('.btn-for-flipping').click(function(){
		$(this).parents('.flip-container').toggleClass('flip');
	});
}






$(document).ready(main);