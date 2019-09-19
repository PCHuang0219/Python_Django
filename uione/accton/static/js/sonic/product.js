let clickPictureBigger = function(){
    $(".img-thumbnail").click(function(){
        var src_buffer = $('#bigger_picture').attr('src');
        $('#bigger_picture').attr('src', $(this).attr('src'));
        $(this).attr('src',src_buffer);
    });
}

let download_SONiC_image = function(){
    $("#SONiC_Image_Downloads").click(function(){
        location.href = "http://210.63.221.19:8888/SONiC/Common/sonic-broadcom.bin" ;
    })
}

$(document).on('ready', function () {
    $('.slider-for').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        asNavFor: '.slider-nav'
    });
    $('.slider-nav').slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        asNavFor: '.slider-for',
        dots: true,
        centerMode: true,
        focusOnSelect: true
    });
});
addLoadEvent(download_SONiC_image);
addLoadEvent(clickPictureBigger);