$(document).ready(function(){
	$('#education').carouFredSel({
		responsive: true,
		width: '100%',
		pagination: "#education-pager",
		auto: false,
		scroll: 1,
		items: {
			width: 400,
		//	height: '30%',	//	optionally resize item-height
			visible: {
				min: 1,
				max: 1
			}
		}
	});
});

	$(document).ready(function(){
		// hide #back-top first
		$("#back-top").hide();		
		// fade in #back-top
		$(function () {
			$(window).scroll(function () {
				if ($(this).scrollTop() > 100) {
					$('#back-top').fadeIn();
				} else {
					$('#back-top').fadeOut();
				}
			});	
			// scroll body to 0px on click
			$('#back-top a').click(function () {
				$('body,html').animate({
					scrollTop: 0
				}, 800);
				return false;
			});
		});	
	});
$(document).ready(function(){
	$('#work-expeirence').carouFredSel({
		responsive: true,
		width: '100%',
		pagination: "#expeirence-pager",
		auto: false,
		scroll: 1,
		items: {
			width: 400,
		//	height: '30%',	//	optionally resize item-height
			visible: {
				min: 1,
				max: 1
			}
		}
	});
});
$(document).ready(function(){
 	$("#tab-container").easytabs({
		animate: true,
		updateHash		: false,
		transitionIn		:'slideDown',
		transitionOut		:'slideUp',
		animationSpeed	:600,
	});

});

$(document).ready(function() {
	$("a[rel^='prettyPhoto']").prettyPhoto({
		opacity:0.80,
		//default_width:500,
		//default_height:344,
		theme:'dark_rounded',
		hideflash:false,
		modal:false
	});
});

$(document).ready(function() {  
	$('.portfolio-img').each(function() {
		$(this).hover(
			function() {
				$(this).stop().animate({ opacity: 0.5 }, 400);
			},
		   function() {
			   $(this).stop().animate({ opacity: 1.0 }, 400);
	   })
	});
});

	$(document).ready(function(){
		$("#contact_form").validate({
			meta: "validate",
			submitHandler: function (form) {
				$('#contact_form').hide();
				$('#sucessmessage').append("<h4 class='form_thanks'>Thanks! Our Team will get in touch in next 24 hours</h4>");
				return false;
				form.submit();
			},
			/* */
			rules: {
				name: "required",
				
				lastname: "required",
				// simple rule, converted to {required:true}
				email: { // compound rule
					required: true,
					email: true
				},
				subject: {
					required: true,
				},
				comment: {
					required: true
				}
			},
			messages: {
				name: "Please enter your name.",
				lastname: "Please enter your last name.",
				email: {
					required: "Please enter email.",
					email: "Please enter valid email"
				},
				subject: "Please enter a subject.",
				comment: "Please enter a comment."
			},
		}); /*========================================*/
	});