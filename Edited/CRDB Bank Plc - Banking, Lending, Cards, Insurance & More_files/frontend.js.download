(function ($) {
    $(function () {

        /** Trigger Menu stretch */
        if ($(".wpfm-nav-strech-trigger")[0] && ($(".wpfm-nav-strech-trigger").attr('id') == 'right'
            || $(".wpfm-nav-strech-trigger").attr('id') == 'left')) {
            $('.wpfm-nav-strech-trigger').click(function (e) {
                e.preventDefault();
                $('.wpfm-nav-strech-trigger').hide();
                $('ul.wpfm-nav-show-hide').slideToggle(400);
            });
    }

    /** Trigger Menu close */
    if ($(".wpfm-nav-close-trigger")[0] && ($(".wpfm-nav-close-trigger").attr('id') == 'right'
        || $(".wpfm-nav-close-trigger").attr('id') == 'left')) {
        $('.wpfm-nav-close-trigger').click(function (e) {
            e.preventDefault();
            $('.wpfm-nav-strech-trigger').show();
            $('ul.wpfm-nav-show-hide').slideUp(400);
        });
}

/** On hover effect for template 7 */
$(".wpfm-menu-name").hover(function () {
    $(this).find('.wpfm-tootltip-title').css('opacity', '1');
});

         /**
         Add no-touch class to body for mobile touch events 
         Hover toggle for touch activated
         */

         if($('body').find('.wpfm-menu-wrapper').attr('data-disable-double-touch') !== '1'){
            var clickBtn = true;
            if ("ontouchstart" in document.documentElement) {
                /* Add wpfm-touch class to the document html */
                document.documentElement.className += " wpfm-touch";
                var container = $('#wpfm-floating-menu-nav ul li a, #wpfm-floating-menu-nav ul li.wpfm-modal-popup-link a, #wpfm-floating-menu-nav ul li a[href^="#"]');

                /* Prevent First click on menu if touch device */
                $(document).on('click', '#wpfm-floating-menu-nav ul li a, #wpfm-floating-menu-nav ul li.wpfm-modal-popup-link a, #wpfm-floating-menu-nav ul li a[href^="#"]', function (e) {
                    container.not(this).removeClass('wpfm_hover_effect');
                    $(this).toggleClass('wpfm_hover_effect')
                    if($(this).hasClass('wpfm_hover_effect')){
                      e.preventDefault();
                  }else{
                  }
              });


        /**
        * if the target of the click isn't the container nor a descendant of the container
        */
        $(document).mouseup(function (e){
         if (!container.is(e.target) 
          && container.has(e.target).length === 0){
            container.removeClass('wpfm_hover_effect');
    }
});
    }
}

/** Initialize active class for on scroll event */
if ($('.wpfm-floating-wh-wrapper a[href^="#"]').length > 0) {
    $(document).on("scroll", onScroll);
}

/** Inline Navigation Js */
$('.wpfm-floating-wh-wrapper a[href^="#"]').on('click', function (e) {
    e.preventDefault();
    var target = $(this).attr('href');
    if ($(target).length > 0) {
        $('html, body').stop().animate({
            'scrollTop': $(target).offset().top + 1
        }, 900, 'swing', function () {
            $(document).on("scroll", onScroll);
        });
    }
});

/** Add Class on scroll */
//        function onScroll(event){
//        var scrollPos = $(document).scrollTop();
//        $('.wpfm-menu-wrapper a[href^="#"]').each(function () {
//            var currLink = $(this);
//            var refElement = $(currLink.attr("href"));
//            if(refElement != '#' && $(refElement).length > 0){
//            if(refElement.position().top){
//            if (refElement.position().top <= scrollPos && refElement.position().top + refElement.height() > scrollPos){
//                $('.wpfm-menu-wrapper ul li a').removeClass("wpfm-active-nav");
//                currLink.addClass("wpfm-active-nav");
//            }
//            else{
//                currLink.removeClass("wpfm-active-nav");
//                }
//              } 
//            }
//        });
//        }

function onScroll(event) {
    var scrollPos = $(document).scrollTop();
    $('.wpfm-menu-wrapper a[href^="#"]').each(function () {
        var currLink = $(this);
        var refElement = $(currLink.attr("href"));
        var positon_offset_var = $(this).data("pos-offset-var");
        if (positon_offset_var == '1') {
            if (refElement != '#' && $(refElement).length > 0) {
                if (refElement.offset().top) {
                    if (refElement.offset().top <= scrollPos && refElement.offset().top + refElement.height() > scrollPos) {
                        $('.wpfm-menu-wrapper ul li').removeClass("wpfm-active-nav");
                        currLink.parent("li").addClass("wpfm-active-nav");
                    } else {
                        currLink.parent("li").removeClass("wpfm-active-nav");
                    }
                }
            }
        } else {
            if (refElement != '#' && $(refElement).length > 0) {
                if (refElement.position().top) {
                    if (refElement.position().top <= scrollPos && refElement.position().top + refElement.height() > scrollPos) {
                        $('.wpfm-menu-wrapper ul li').removeClass("wpfm-active-nav");
                        currLink.parent("li").addClass("wpfm-active-nav");
                    } else {
                        currLink.parent("li").removeClass("wpfm-active-nav");
                    }
                }
            }
        }

    });
}
}); /** Function ends */
}(jQuery));