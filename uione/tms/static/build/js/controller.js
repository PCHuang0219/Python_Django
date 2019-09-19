jQuery(function() {

        jQuery('.components_controller').click(function() {

                var block = jQuery(this).val();

		console.log(block);


                if(jQuery(this).prop('checked')) {

                        jQuery('.'+block).show();
                } else {

                        jQuery('.'+block).hide();
                }
        });
       
	jQuery('.system_controller').click(function() {

		var block = jQuery(this).val();

		console.log(block);

		if(jQuery(this).prop('checked')) {

			jQuery('.'+block).show();
		} else {

			jQuery('.'+block).hide();
		}
	});
});
