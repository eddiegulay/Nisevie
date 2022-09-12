jQuery(document).ready(function ($) {
    "use strict";
    var windowSize = $(window).width();
    l18W();

    $(window).load(function() {
        l18W();
        if($('html').hasClass('stm-site-preloader')){
            $('html').addClass('stm-site-loaded');

            setTimeout(function(){
                $('html').removeClass('stm-site-preloader stm-site-loaded');
            }, 250);

            $(window).bind('onbeforeunload', function(e) {
                $('html').addClass('stm-site-preloader stm-after-hidden');
            });

            if( $('a[href^=mailto], a[href^=skype], a[href^=tel]').on('click', function(e) {
                setTimeout(function(){
                    $('html').removeClass('stm-site-preloader stm-site-loaded');
                });
            }));
        }
    });

    $(window).resize(function(){
        l18W();
        stm_stretch_column();
        full_height_columns();
    });

    $.fn.is_on_screen = function(){
        var win = $(window);
        var viewport = {
            top : win.scrollTop(),
            left : win.scrollLeft()
        };
        viewport.right = viewport.left + win.width();
        viewport.bottom = viewport.top + win.height();

        var bounds = this.offset();
        bounds.right = bounds.left + this.outerWidth();
        bounds.bottom = bounds.top + this.outerHeight();

        return (!(viewport.right < bounds.left || viewport.left > bounds.right || viewport.bottom < bounds.top || viewport.top > bounds.bottom));
    };

    $(".stm-register-form form").submit(function (e) {
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: ajaxurl,
            dataType: 'json',
            context: this,
            data: $(this).serialize() + '&action=stm_custom_register',
            beforeSend: function(){
                $(this).find('input').removeClass('form-error');
                $('.stm-validation-message').empty();
            },
            success: function (data) {

                for(var err in data.errors){
                    $(this).find('input[name=' + err + ']').addClass('form-error');
                }

                if(data.message) {
                    var message = $('<div class="stm-message-ajax-validation heading-font">' + data.message + '</div>').hide();

                    $(this).find('.stm-validation-message').append(message);
                    message.slideDown('fast');
                }
            }
        });
    });

    $(document).on("click", ".load_more_btn", function(e){
        e.preventDefault();
        var page = $(this).attr("data-page");
        var load_by = $(this).attr("data-load");
        var filter = $(this).attr("data-filter");
        var category = $(this).attr('data-category');
        $.ajax({
            url: ajaxurl,
            type: "POST",
            dataType: "json",
            data: "&page=" + page + "&load_by=" + load_by + "&category=" + category +  "&filter=" + filter + "&action=stm_ajax_load_events",
            context: this,
            beforeSend: function (data) {
                $(this).parent().addClass("event_posts_loading");
            },
            success: function (data) {
                $(this).parent().removeClass("event_posts_loading");
                $(".stm_events_modern_list ").append(data.html);
                $(this).attr("data-page", data.new_page);
                if(!data.load_more) {
                    $(this).remove();
                }
            }
        });
    });

    $('.scroll_to_event_form').click(function(e) {
        event.preventDefault();
        $('html,body').animate({ scrollTop: $(this.hash).offset().top}, 500);
    });

    $('.show_popup').on('click', function(e){
        $(this).parents().find('#video').addClass('video_popup_box')
    });

    stm_stretch_column();

    function stm_stretch_column() {
        $('.wpb_column[data-stretch]').each(function () {
            var stretch = $(this).data('stretch');
            var xPos = $(this).offset().left;
            var wW = $(window).width();
            var xW = $(this).width();

            var value = wW - (xW + xPos);
            if (stretch == 'left') {
                value = xPos;
            }

            $(this).find('.vc_column-inner').css('width', xW + value + 'px');
            $(this).find('.vc_column-inner').css('margin-' + stretch, '-' + value + 'px');
        });
    };

    //Full height
    full_height_columns();
    function full_height_columns() {

        $(".full_height_columns").each(function () {
            var full_height_columns = $(this).find(".wpb_column:first").height();
            $(this).find("iframe").css("height", full_height_columns);
        });
    };

    stm_ajax_add_event_member();

    function stm_ajax_add_event_member() {
        $("#event-members-form").on("submit", function (event) {
            event.preventDefault();

            var $this = $(this),
                eventID = parseInt($($this).find('input[name="event_member_id"]').val()),
                addedEvents = localStorage.getItem('addedEvents'),
                eventAdded = false;

            if (addedEvents) {
                addedEvents = JSON.parse(addedEvents);
                eventAdded = $.inArray(eventID, addedEvents) > -1;
            }
            if (!eventAdded) {
                $.ajax({
                    url: ajaxurl,
                    type: "POST",
                    dataType: "json",
                    context: this,
                    data: $(this).serialize() + "&action=stm_ajax_add_event_member",
                    beforeSend: function () {
                        $(".alert-modal").remove();
                        $(this).closest("form").find("input").removeClass("form-error");
                        $(this).closest("form").find(".stm-ajax-loader").addClass("loading");
                    },
                    success: function (data) {
                        $(this).closest("form").find(".stm-ajax-loader").removeClass("loading");

                        $(this).closest("form").find(".event-members-box").append('<div class="alert-modal alert alert-' + data.status + ' text-left">' + data.response + '</div>')
                        for (var key in data.errors) {
                            $('#event-members-form input[name="' + key + '"]').addClass("form-error");
                        }
                        if (!$('#event-members-form input[name="' + key + '"]').hasClass('form-error')) {
                            $(".event-members-box-table .event-attended-count").text(parseInt($(".event-members-box-table .event-attended-count").text()) + 1);
                            $(".event-attended-count.event-new-count").text(parseInt($(".event-attended-count.event-new-count").text()) + 1);
                            if (addedEvents) {
                                addedEvents.push(eventID);
                            } else {
                                addedEvents = [eventID];
                            }
                            localStorage.setItem('addedEvents', JSON.stringify(addedEvents));
                            $($this).find(".form__notice_success").fadeIn(300);
                        }
                        $("#event-members-form button").addClass("disabled").prop('disabled', true);
                    },
                    complete: function (data) {
                        $("#event-members-form")[0].reset();
                    }
                });
                $(this).closest("form").find(".form-error").live("hover", function () {
                    $(this).removeClass("form-error");
                });
            } else {
                $($this).find(".form__notice_information").fadeIn(300);
            }
            return false;
        });
    }

    $(".event_terms_conditions #event_terms_conditions").on("click", function(e){
        if($(this).is(':checked')){
            $("#event-members-form button").removeClass("disabled").prop('disabled', false);
        } else {
            $("#event-members-form button").addClass("disabled").prop('disabled', true);
        }
    });

    $(".event_joining .show_event_list_form").on("click", function(e){
        var eventItemValId = $(this).parents(".item").find(".event-item-id").val();
        $(".stm_events_classic #event-members-form .event_member_id").val(eventItemValId);
        $(".stm_events_list_form").show();
        $(this).parents(".item").find(".event-attended-count").addClass("event-new-count");
    });
    $(".notice__hide").on("click", function(e){
        $(".stm_events_list_form").hide();
        $("#event-members-form")[0].reset();
        $("#event-members-form .alert-modal").hide();
        $("#event-members-form .form__notice_information").hide();
        $(".stm_events_classic .item").find(".event-attended-count").removeClass("event-new-count");
    });

    $(".events_lessons_box .event_lesson_tabs:first-child").addClass("active");
    $('.events_lessons_box .event_lesson_tabs a').each(function(e){
        if( $(this).parent().hasClass("active")) {
            $($(this).attr('href')).show();
        }
    });
    $('.events_lessons_box .event_lesson_tabs a').click(function(e){
        $(this).parents(".events_lessons_box").find(".event_lesson_info").hide();
        $(this).parents(".events_lessons_box").find(".event_lesson_tabs").removeClass("active");
        $(this).parent().addClass("active");
        $($(this).attr("href")).show();
        return false;
    });

    $(document).on("click", ".js-open-search-box", function() {
        $(this).closest(".header_search").toggleClass("active");
        return false;
    });

    if( $(".wpb_revslider_element").length && $('body').hasClass("header_style_7") ) {
        $(".wpb_revslider_element").closest(".vc_row-no-padding").addClass("stm-revslider-wrapper");
    }

    $(document).on("click", "body", function(e) {
        if( ! $(e.target).closest(".header_search").length ) {
            $(".header_search").removeClass("active");

        }
    });

    $("body .wpb_video_widget .wpb_wrapper .wpb_video_wrapper .play_video").live('click', function () {
        $(this).parent().find('iframe').attr( 'src', $(this).parent().find('iframe').attr( 'src' ) + '?autoplay=1').delay();
        $(this).hide();
        $(this).parent().find('img').hide();
        $(this).parent().find('.video').show();
        return false;
    });

    $(".staff_read_more").live('click', function () {
        $(this).closest('.stm_staff_2').find('.full_description').slideToggle(150);
        return false;
    });

    $("select:not(.stm_not_select2)").each(function() {
        if( ! $(this).closest(".gfield").hasClass("stm_not_select2") ) {
            $(this).select2({width: '100%', minimumResultsForSearch: '-1'});
        }
    });
    if( $("#rating").length ){
        $("#rating").select2( 'destroy' );
    }

    if( $("#demos_switcher").length ) {
        $("#demos_switcher").select2("destroy");

        $("#demos_switcher").select2({
            templateResult: demosItemTemplate,
            width: '100%',
            minimumResultsForSearch: '-1'
        });

    }

    if( $('body').hasClass('customizer_page') ) {
        $(".customizer_page .ui-tabs").remove();
    }

    $('#menu_toggle').live('click', function () {
        $(this).toggleClass('open');
        $('.mobile_header .top_nav_mobile').slideToggle(300);
        return false;
    });
    $('#menu_toggle_button').live('click', function () {
        $(this).toggleClass('open');
        $('.header_side').each(function(){
            if(! $(this).hasClass('show') ) {
                $(this).addClass('show');
                if($('body').hasClass('rtl')) {
                    $(this).animate({right: "0"}, 300);
                }else {
                    $(this).animate({left: "0"}, 300);
                }
            }else {
                $(this).removeClass('show');
                if($('body').hasClass('rtl')) {
                    $(this).animate({right: "-100%"}, 600);
                }else{
                    $(this).animate({left: "-100%"}, 600);
                }
            }
        });

        return false;
    });

    $(".mobile_header .top_nav_mobile .main_menu_nav > li.menu-item-has-children > a").after('<span class="arrow"><i></i></span>');
    $(".mobile_header .top_nav_mobile .main_menu_nav > li.menu-item-has-children > .sub-menu > .menu-item-has-children > a").after('<span class="arrow"><i class="fa fa-chevron-down"></i></span>');

    $(".mobile_header .top_nav_mobile .main_menu_nav > li.menu-item-has-children .arrow").live('click', function () {
        $(this).toggleClass('active');
        $(this).closest('li').find('> ul').slideToggle(300);
    });

    $(".mobile_header .top_nav_mobile .main_menu_nav > li.menu-item-has-children > a").live('click', function () {
        if( $(this).attr('href') == '#' ){
            $(this).closest('li').find('ul').slideToggle(300);
            $(this).closest('li').find('.arrow').toggleClass('active');
        }
    });

    // Quantity actions
    $('.quantity_actions span').on('click', function() {
        var quantityContainer = $(this).closest('.quantity'),
            quantityInput = quantityContainer.find('.qty'),
            quantityVal = quantityInput.attr('value');

		$('.shop_table.cart .button').removeAttr("disabled")

        if( $(this).hasClass('plus') ) {
            quantityInput.attr('value', parseInt(quantityVal) + 1);
        } else if( $(this).hasClass('minus') ) {
            if( quantityVal > 1 ) {
                quantityInput.attr('value', parseInt(quantityVal) - 1);
            }
        }
    });

    // Stiky Header
	var headerHeight = $("#header").height();
    var headerTop = $(".header_top").height();
    var topBar = $(".top_bar").height();

    $("#header .top_nav, #header .header_top").affix({
        offset: {
            top: headerHeight
        }
    });

    $("#menu_toggle_button").affix({
        offset: {
            top: topBar
        }
    });

    $(window).scroll(function(){
        if( $(".sticky_menu .header_top, .sticky_menu .top_nav").hasClass('affix') ) {
            $("#header").css("paddingBottom", headerTop);
        } else {
            $("#header").css("paddingBottom", 0);
        }
    });

    $(".top_bar_info_switcher .active").on('click', function () {

        if( $(".top_bar_info_switcher ul").is(':visible') ){
            $(".top_bar_info_switcher ul").slideUp(100);
        }else{
            $(".top_bar_info_switcher ul").slideDown(100);
        }

        return false;
    });

    $(".top_bar_info_switcher a").on('click', function () {
        var id = $(this).attr('href');
        var title = $(this).text();
        $(".top_bar_info").hide();
        $(id).show();
        $(".top_bar_info_switcher .active span").text(title);
        $(".top_bar_info_switcher ul").slideUp(100);
        return false;
    });

    if(! /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ){
        stm_animate_block();
    }else{
        $(".stm_animation").css('opacity', 1);
    }

    jQuery(window).scroll(function(){
        if(! /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ){
            stm_animate_block();
        }else{
            $(".stm_animation").css('opacity', 1);
        }
    });

	$('.single-product .product-type-variable table.variations select').live("change", function() {
		$(this).parent().find('.select2-selection__rendered').text($(this).find('option[value="'+ $(this).val() +'"]').text());
	});

    /*Adds*/
    if(typeof($.fancybox) !== 'undefined') {
        $('.stm_fancy-iframe').fancybox({
            type: 'iframe',
            padding: 0,
            maxWidth: '800px',
            width: '100%',
            fitToView: false,
            beforeLoad: function () {
                var url = $(this.element).data('url');
                this.href = url;
            }
        });

        $('.stm_fancybox').fancybox({
            fitToView	: false,
            padding     : 30,
            maxWidth    : '500px',
            autoSize	: true,
            closeClick	: false,
            openEffect	: 'none',
            closeEffect	: 'none'
        });
    }

    $('[data-scroll-to]').on('click', function(e){
        var url = $(this).attr('data-scroll-to');
        if(typeof(url) !== 'undefined') {
            var url_parsed = url.split('#');
            if(typeof(url_parsed[1]) !== 'undefined' && $('#' + url_parsed[1]).length > 0) {
                $('html, body').stop().animate({
                    scrollTop: $('#' + url_parsed[1]).offset().top
                }, 700);
            } else {
                window.location.href = url;
            }
        }
    });

    if($('body').hasClass('site_layout_19')) {
        $('.top_nav li a').on('click', function (e) {
            e.preventDefault();
            var url = $(this).attr('href');
            if (typeof(url) !== 'undefined') {
                var url_parsed = url.split('#');
                if (typeof(url_parsed[1]) !== 'undefined' && $('#' + url_parsed[1]).length > 0) {
                    $('html, body').stop().animate({
                        scrollTop: $('#' + url_parsed[1]).offset().top - 50
                    }, 700);
                } else {
                    window.location.href = url;
                }
            }
        });
    }

    $('.stm_top_bar_l13-search button').click(function(e){
        var $wr = $(this).closest('.stm_top_bar_l13-search');
        if($wr.hasClass('active')) {
            if($wr.find('input').val() == '') {
                e.preventDefault();
                $wr.removeClass('active active-focus');
            }
        } else {
            e.preventDefault();
            $wr.addClass('active active-focus');
            setTimeout(function(){
                $wr.find('input').focus();
            }, 300);
        }
    })

    $('body').click(function(e) {
        if ($(e.target).closest('.stm_top_bar_l13-search').length === 0) {
            var $wr = $('.stm_top_bar_l13-search');
            $wr.find('input').focusout();
            $wr.removeClass('active active-focus');
        }
    });

});

function stm_animate_block(){
    jQuery('.stm_animation').each(function(){
        if(jQuery(this).attr('data-animate')) {
            var animation_blocks = jQuery(this).children('*');
            var animationName = jQuery(this).attr('data-animate'),
                animationDuration = jQuery(this).attr('data-animation-duration') + 's',
                animationDelay = jQuery(this).attr('data-animation-delay');
            var style = 'opacity:1;-webkit-animation-delay:'+animationDelay+'s;-webkit-animation-duration:'+animationDuration+'; -moz-animation-delay:'+animationDelay+'s;-moz-animation-duration:'+animationDuration+'; animation-delay:'+animationDelay+'s;';
            var container_style = 'opacity:1;-webkit-transition-delay: '+(animationDelay)+'s; -moz-transition-delay: '+(animationDelay)+'s; transition-delay: '+(animationDelay)+'s;';
            if (isAppear(jQuery(this))) {
                jQuery(this).attr( 'style', container_style );
                jQuery.each( animation_blocks, function(index,value){
                    jQuery(this).attr('style', style);
                    jQuery(this).addClass('animated').addClass(animationName);
                });
            }
        }
    });
}

function isAppear(id) {
    var window_scroll = jQuery(window).scrollTop();
    var window_height = jQuery(window).height();

    if (jQuery(id).hasClass('stm_viewport')) {
        var start_effect = jQuery(id).data('viewport_position');
    }

    if (typeof(start_effect) === 'undefined' || start_effect == '') {
        var percentage = 2;
    }else {
        var percentage = 100 - start_effect;
    }
    var element_top = jQuery(id).offset().top;
    var position = element_top - window_scroll;

    var cut = window_height - (window_height * (percentage / 100));
    if (position <= cut) {
        return true;
    }else {
        return false;
    }
}

function demosItemTemplate(state) {
    if (!state.id) { return state.text; }
    var $state = jQuery(
        '<span class="'+ state.element.value +'"> ' + state.text + '</span>'
    );
    return $state;
}

function l18W() {
    var $ = jQuery;
    if($('body').hasClass('site_layout_18')) {
        var contentW = $('#fullpage').outerWidth();
        var contentArea = $('.content-area').outerWidth();
        var fullWleft = contentW/2;

        var marginArea = (contentW - contentArea) / 2;
        //$('.stm_bg_right').css('width', contentW + 'px');
        $('.stm_fullwidth_left').css({
            'width' : fullWleft + 'px'
        });

        $('.stm_fullwidth_content').css({
            'width' : contentW + 'px',
            'margin-right' : '-' + marginArea + 'px'
        })

    }
}