(function ($) {
    window.console = window.console || function (t) { };
    $(document).ready(function () {
        (function () {
            var self = this,
                that = $('#loading'),
                current = that.find('.current'),
                progress = that.find('.progress'),
                isNeedLoaddng = String(that.css('display')).toLowerCase() === 'block';
            if (!isNeedLoaddng) {
                return onDone();
            }
            preloader({
                lazy: 20,
                onLoading: function (event) {
                    var percentage = event.progressed + '%';
                    current.text(percentage);
                    progress.stop().animate({
                        width: percentage
                    });
                },
                onComplete: function () {
                    that.animate({
                        top: '-100%',
                        opacity: '0'
                    }, {
                        duration: 1800,
                        easing: 'easeInOutBack'
                    });
                    onDone();
                }
            });
        }());

        function onDone() {
            /*onDone star*/
            /*document STAR*/
            h = $(window).height();
            w = $(window).width();

            $winH = $('.winH');
            $winHw = $('.winHw');
            $winHf = $('.winHf');
            $jqimgFill = $('.jqimgFill');
            $jqimgFill_tc = $('.jqimgFill-tc');
            $pro64 = $('.pro64');
            $pro64s = $('.pro64s');
            $pro11 = $('.pro11');
            $pro1 = $('.pro1');
            $body = $('body');
						$body.addClass('in');

            $header = $('#header');
						$header.menu = $('#header .menu > ul > li.pro > ul');
						$header.menu.addClass('in');
                        //加簽下拉
                        $header.menu2 = $('#header .menu > ul > li.subMenu > ul');
                        $header.menu2.addClass('in');

            $navbarToggle = $('.navbar-toggle');
            $banner = $('#banner');
            $homeNews = $('#homeNews');
            $homePro = $('#homePro');
            $proBoxList = $('#proBoxList');

            $searchBox = $('.search-bar');
            $searchBoxBtn = $('#searhc-box-btn');

            $itemMenu = $('.item-menu');
            $menu = $('#header .menu');

            $comparisonBox = $('.comparisonBox');
            $comparisonBoxBtn = $('.comparison');

            resizeCss();
            new WOW().init();


						/*== 列印按鈕  =========================== */
						function varitext(text) {
								text = document
								print(text)
						}
						$('#print-btn').each(function() {
								$('#print-btn').click(function() {
										varitext();
								})
						});

						/* ==========================================================================
						 * select2 下拉選單
						 ==========================================================================*/
						$('.partners-RMA-RS-apply').each(function() {
							$(".js-multiple").select2({
								placeholder: "Please select（You can select more than one product）",
							});
						});

            /*== navigation  =========================== */
            $navbarToggle.click(function () {
                $body.toggleClass('open');
            });

            /*== top  =========================== */
            $(".top").click(function () {
                jQuery("html,body").animate({
                    scrollTop: 0
                }, 1000);
            });

            $(window).scroll(function () {
                if ($(this).scrollTop() > 300) {
                    $('.top').fadeIn("fast");
                } else {
                    $('.top').stop().fadeOut("fast");
                }
            });

            /*== post-bar  =========================== */

            $(".post-bar .bar-btn").click(function(){
                $(".post-bar").addClass('actived');

                useAjax('setCookie','');
            });


						/* ==========================================================================
							* 產品內頁 往下
						==========================================================================*/
						$('#productsInfo').each(function() {
							$('.down1').click(function(){
								$('html,body').animate({scrollTop:$('#Overview').offset().top - 130 }, 800);
							});
						});

						$('#productsInfo').each(function() {
							$('.down2').click(function(){
								$('html,body').animate({scrollTop:$('#Features').offset().top - 130 }, 800);
							});
						});

						$('#productsInfo').each(function() {
							$('.down3').click(function(){
								$('html,body').animate({scrollTop:$('#Specs').offset().top - 130 }, 800);
							});
						});

						$('#productsInfo').each(function() {
							$('.down4').click(function(){
								$('html,body').animate({scrollTop:$('#Resources').offset().top - 130 }, 800);
							});
						});

            /*== banner  =========================== */
            // $banner.each(function() {
            // $(this).find('.slider').slick({
            //   slidesToShow: 1,
            //  slidesToScroll: 1,
            //fade: true,
            // dots: true,
            // arrows: false,
            // autoplay: true,
            // autoplaySpeed: 3000,
            // speed: 1000,
            // });
            //  });

            /*== qa===========================*/
            $('#qa').each(function () {
                $(this).find('.panel-heading a').click(function () {
                    $(this).parents('.panel').toggleClass("active");
                    setTimeout(function () {
                        $("a.collapsed").parents('.panel').removeClass("active");
                    }, 100);
                });
            });

            /*== homeNews  =========================== */
            $homeNews.each(function () {
                $(this).find('.slider').slick({
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    //fade: true,
                    dots: false,
                    arrows: true,
                    autoplay: true,
                    autoplaySpeed: 3000,
                    speed: 1000,
                });
            });

            /*== homePro  =========================== */
            $homePro.each(function () {
                $(this).find('.slider').slick({
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    fade: true,
                    dots: false,
                    arrows: true,
                    autoplay: true,
                    autoplaySpeed: 3000,
                    speed: 500,
                });
            });

            /*== proBoxList  =========================== */
            $proBoxList.each(function () {
                $(this).find('.slider').slick({
                    slidesToShow: 4,
                    slidesToScroll: 1,
                    //fade: true,
                    dots: false,
                    arrows: true,
                    autoplay: true,
                    autoplaySpeed: 3000,
                    speed: 500,
                    responsive: [{
                        breakpoint: 991,
                        settings: {
                            slidesToShow: 3,
                        }
                    }, {
                        breakpoint: 767,
                        settings: {
                            slidesToShow: 2,
                        }
                    }, {
                        breakpoint: 480,
                        settings: {
                            slidesToShow: 1,
                        }
                    }]
                });
            });

            /*== 主體-表頭固定  =========================== */
            // function headerFixed() {
            //h = $(window).height();
            // var $this = $(this);　　
            // var $this_Top = $this.scrollTop();
            // if ($this_Top < 90) {
            //    $subnav.removeClass("fixed");
            //     $footerTop.removeClass("fixed");

            // }　　　　
            // if ($this_Top > 90) {
            //     $subnav.addClass("fixed");
            //     $footerTop.addClass("fixed");
            // }　
            // }
            /*== scroll  =========================== */
            $(window).bind('scroll', function () {
                var $this = $(this);
                var $this_Top = $this.scrollTop();
                if ($this_Top < 75) {
                    $header.removeClass("fixed");
                    //$banner.addClass("mPS2id-target");
                }
                if ($this_Top > 75) {
                    $header.addClass("fixed");
                    //$banner.removeClass("mPS2id-target");
                }
            }).scroll();

						/* ==== dropdown-toggle ====*/
        		 $(".dropdown-toggle").click(function() {
            	$(this).next.$(".dropdown-menu").slideToggle(200);
       		 });

            /* ==========================================================================
            	* 語言 選單開關
            ==========================================================================*/
            $(".lan").click(function () {
                $(".lenList").slideToggle("slow");
            });

						/* ==========================================================================
								[partners-centers] 選單-收合
						==========================================================================*/
						$('.nav-aside-right').each(function() {
							$(".nav-asid-btn").click(function() {
								$(".nav-aside-select").slideToggle();
							});
						});

						/* ==========================================================================
								[investor .subBox] 選單-收合
						==========================================================================*/
						$('.subBox').each(function() {
							$(this).on('click',function(event){
								event.preventDefault();
								$(this).toggleClass('active');
								$(this).next('ul').slideToggle(500);
								})
						});

						$('.subBox2').each(function() {
							$(this).on('click',function(event){
								event.preventDefault();
								$(this).toggleClass('active');
								$(this).next('ul').slideToggle(500);
								})
						});
						/*$('.subBox').each(function() {
							$(this).on('click',function(event){
								event.preventDefault();
								$(this).toggleClass('active');
								$(this).next('ul').slideToggle(500);
								})
						});*/

            /* ==========================================================================
            	* productsTool 按鈕開關
            ==========================================================================*/
            $(".btn-next").click(function () {
                $("#compareOpen").slideToggle("slow");
            });

            /*== searchBox ========================= */
            $searchBox.each(function () {
                $searchBoxBtn.click(function () {
                    $searchBox.toggleClass("active");
                    $searchBoxBtn.toggleClass("active");
                });
            });

            /*== menu ========================= */

            $menu.each(function () {
                var that = $(this),
                    isMobile = function () {
                        return $('html').is('.max-sm-size');
                    };

                // Toggle
                $itemMenu.click(function () {
                    that.toggleClass("active");
                    $itemMenu.toggleClass("active");
                });

                // Close
                $('#header .navigation .close-m').click(function () {
                    $itemMenu.click();
                });

                // 加簽下拉選單
                that.find('> ul > .subMenu').each(function () {
                    var me = $(this),
                        delay = { open: 200, close: 400 },
                        timer = { open: null, close: null },
                        $toggle = me.children('a'),
                        $dropdown = me.children('.dropdown-menu');

                    $toggle.bind({
                        mouseenter: function () {
                            if (!isMobile()) {
                                clearTimeout(timer.close);
                                timer.open = setTimeout(function () {
                                    me.addClass('open');
                                }, delay.open);
                            }
                        },
                        mouseleave: function () {
                            if (!isMobile()) {
                                clearTimeout(timer.open);
                                timer.close = setTimeout(function () {
                                    me.removeClass('open');
                                }, delay.close);
                            }
                        }
                    });

                    $dropdown.bind({
                        mouseenter: function () {
                            $toggle.mouseenter();
                        },
                        mouseleave: function () {
                            $toggle.mouseleave();
                        }
                    });

                    that.find('> ul > li > a').not($toggle).bind({
                        mouseenter: function () {
                            if (!isMobile()) {
                                me.removeClass('open');
                            }
                        },
                    });
                });

                // Product
                that.find('> ul > .pro').each(function () {
                    var me = $(this),
                        delay = { open: 200, close: 400 },
                        timer = { open: null, close: null },
                        $toggle = me.children('a'),
                        $dropdown = me.children('.dropdown-menu');

                    $toggle.bind({
                        mouseenter: function () {
                            if (!isMobile()) {
                                clearTimeout(timer.close);
                                timer.open = setTimeout(function () {
                                    me.addClass('open');
                                }, delay.open);
                            }
                        },
                        mouseleave: function () {
                            if (!isMobile()) {
                                clearTimeout(timer.open);
                                timer.close = setTimeout(function () {
                                    me.removeClass('open');
                                }, delay.close);
                            }
                        }
                    });

                    $dropdown.bind({
                        mouseenter: function () {
                            $toggle.mouseenter();
                        },
                        mouseleave: function () {
                            $toggle.mouseleave();
                        }
                    });

                    that.find('> ul > li > a').not($toggle).bind({
                        mouseenter: function () {
                            if (!isMobile()) {
                                me.removeClass('open');
                            }
                        },
                    });
                });

                // Link
                that.find('a').click(function (event) {
                    var me = $(this);
                    if (!isMobile()) {
                        event.stopPropagation();
                    } else {
                        if (me.is('[data-toggle="dropdown"]')) {
                            event.preventDefault();
                        }
                    }
                });
            });

            /*== supDownload ========================= */
            $('#supDownload').each(function () {
                var that = $(this),
                    isMobile = function () {
                        return $('html').is('.max-sm-size');
                    };

                that.find('.selectBox .nav-pills').click(function () {
                    if ($(event.target).is('.nav-pills')) {
                        var $target = $('#' + $(this).data('target'));
                        $('.proCont').not($target).hide();
                        $target.toggle();
                    }
                });
            });

            $('.mapButton button').bind({
                mouseenter: function () {
                    $('.mapBox .mapPic.' + $(this).data('target')).addClass('hover');
                },
                mouseleave: function () {
                    $('.mapBox .mapPic').removeClass('hover');
                }
            });

            /*== comparisonBox ========================= */
            $comparisonBox.each(function () {
                $comparisonBoxBtn.click(function () {
                    $comparisonBox.toggleClass("active");
                    $comparisonBoxBtn.toggleClass("active");
                });
            });

            /* ==========================================================================
           * slick 廣告 bannerSlick
						==========================================================================*/
            $('.bannerSlick').each(function () {

                $('.slider-for2').slick({
                    autoplay: true,
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    arrows: false,
                    fade: true,
                    dots: true,
                    arrows: false,
                    autoplaySpeed: 3000,
                    speed: 2000,
                    asNavFor: '.slider-nav2'
                });
                $('.slider-nav2').slick({
                    autoplay: true,
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    arrows: false,
                    asNavFor: '.slider-for2',
                    dots: false,
                    autoplaySpeed: 3000,
                    speed: 2000,
                    centerMode: false,
                    focusOnSelect: true
                });
            });

            /* ==========================================================================
           * slick 廣告 proSlick
						==========================================================================*/
            $('.proSlick').each(function () {

                $('.slider-for3').slick({
                    autoplay: true,
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    arrows: true,
                    fade: true,
                    asNavFor: '.slider-nav3'
                });
                $('.slider-nav3').slick({
                    autoplay: true,
                    slidesToShow: 3,
                    slidesToScroll: 1,
                    arrows: false,
                    asNavFor: '.slider-for3',
                    dots: false,
                    centerMode: false,
                    focusOnSelect: true,
                    responsive: [{
                        breakpoint: 991,
                        settings: {
                            slidesToShow: 4
                        }
                    }, {
                        breakpoint: 480,
                        settings: {
                            slidesToShow: 3
                        }
                    }, {
                        breakpoint: 380,
                        settings: {
                            slidesToShow: 2
                        }
                    }

                    ]
                });
            });

            /* ==========================================================================
            	* 產品內頁 往下
            ==========================================================================*/
            $('#productsInfo').each(function () {
                $('#home-banner .down').click(function () {
                    $('html,body').animate({
                        scrollTop: $('#home-link').offset().top - 130
                    }, 800);
                });
            });


            /* ==========================================================================
            	* [Googlemap]
            ==========================================================================*/
            $('#contact').each(function () {
                tinyMapf();
            });

            function tinyMapf() {
                $.fn.tinyMapConfigure({
                    //語系
                    'language': 'en'
                });
                $('.map').tinyMap({
                    'center': ['24.154201', '120.612740'],
                    'zoom': 16,

                    'styles': [ //灰階

                        {
                            "featureType": "administrative",
                            "elementType": "labels.text.fill",
                            "stylers": [{
                                "color": "#444444"
                            }]
                        },

                        {
                            "featureType": "landscape",
                            "elementType": "all",
                            "stylers": [{
                                "color": "#eaeaea"
                            }]
                        },

                        {
                            "featureType": "poi",
                            "elementType": "all",
                            "stylers": [{
                                "saturation": -100
                            }]
                        },

                        {
                            "featureType": "poi",
                            "elementType": "labels.text",
                            "stylers": [{
                                "visibility": "off"
                            }]
                        },

                        {
                            "featureType": "road",
                            "elementType": "all",
                            "stylers": [{
                                "saturation": -100
                            }, {
                                "lightness": 0
                            }]
                        },

                        {
                            "featureType": "road.highway",
                            "elementType": "all",
                            "stylers": [{
                                "visibility": "simplified"
                            }]
                        },

                        {
                            "featureType": "road.arterial",
                            "elementType": "labels.icon",
                            "stylers": [{
                                "visibility": "off"
                            }]
                        },

                        {
                            "featureType": "transit",
                            "elementType": "all",
                            "stylers": [{
                                "visibility": "off"
                            }]
                        },

                        {
                            "featureType": "water",
                            "elementType": "all",
                            "stylers": [{
                                "color": "#dbdbdb"
                            }, {
                                "visibility": "on"
                            }]
                        },

                    ], //灰階 end

                    'marker': [{
                        'addr': ['24.154201', '120.612740'],
                        'text': '1, Creation Rd.3, Hsinchu Science Park, Hsinchu,30077, Taiwan, R.O.C',
                        'css': 'labels',
                        'newLabel': 'Taiwan Corporation',
                        'newLabelCSS': 'labels',
                        // 自訂圖示
                        'icon': {
                            'url': 'styles/images/inco-map.png',
                            'scaledSize': [36, 36]
                        },
                        // 動畫效果
                        'animation': 'DROP'
                    }, {
                        'addr': ['24.154201', '120.612740'],
                        'text': '1, Creation Rd.3, Hsinchu Science Park, Hsinchu,30077, Taiwan, R.O.C',
                        'css': 'labels',
                        'newLabel': 'Taiwan Corporation',
                        'newLabelCSS': 'labels',
                        // 自訂圖示
                        'icon': {
                            'url': '/styles/images/inco-map.png',
                            'scaledSize': [36, 36]
                        },
                        // 動畫效果
                        'animation': 'DROP'
                    }, {
                        'addr': ['24.154201', '120.612740'],
                        'text': '1, Creation Rd.3, Hsinchu Science Park, Hsinchu,30077, Taiwan, R.O.C',
                        'css': 'labels',
                        'newLabel': 'Taiwan Corporation',
                        'newLabelCSS': 'labels',
                        // 自訂圖示
                        'icon': {
                            'url': '/styles/images/inco-map.png',
                            'scaledSize': [36, 36]
                        },
                        // 動畫效果
                        'animation': 'DROP'
                    }]
                });
            }

            /*== 首頁- 多邊形  =========================== */
            $(".index").addClass("keystone");

            /*== scroll  =========================== */
            $(window).bind('scroll', function () {
                //headerFixed();
            }).scroll();


            /* ==========================================================================
                        * resize 螢幕縮放動作
            ==========================================================================*/

            /*螢幕寬高*/

            $(window).resize(function () {
                resizeCss();
                //$jqimgFill.each(function() {

            });

            function resizeCss() {
                h = $(window).height();
                w = $(window).width();
                //});

                /*螢幕寬高*/
                $winHw.each(function () {
                    $(this).css({
                        "height": h,
                        "width": w
                    });
                });

                $winH.each(function () {
                    $(this).css({
                        "height": h,
                    });
                });

                $winHf.each(function () {
                    $(this).css({
                        "min-height": h - $footerH
                    });
                });

                /*判斷螢幕是否旋轉*/
                if (h < w) {
                    $("body").addClass('landscape');
                    $body.removeClass('upright');
                } else {
                    $body.removeClass('landscape');
                    $("body").addClass('upright');
                }

                /*形狀*/
                //$pro64s.each(function() {
                //$(this).find(".list-item .pic").css("height", $(this).find(".list-item:first-child  .pic").width() / 1.63);
                //});

                /*圖片*/
                $pro64.each(function () {
                    $(this).css("height", $(this).width() / 1.63);
                });

                $pro11.each(function () {
                    $(this).css("height", $(this).width() / 1.19);
                });
                $pro1.each(function () {
                    $(this).css("height", $(this).width() / 1);
                });
                $('.pro55').each(function () {
                    $(this).css("height", $(this).width());
                });



                $jqimgFill.focusPoint();
            }
        }
        /* ==========================================================================
            * load
    ==========================================================================*/
        $(window).load(function () {



        });
    });
    /*=============================================================================
    * preloader
    =============================================================================*/
    function preloader(options) {
        var callee = arguments.callee,
            defaultProcess = 'default',
            historyLoaded = [],
            historyFailed = [];
        callee.instances = callee.instances || {};
        if (!$.isPlainObject(options)) {
            var process = String(options) || defaultProcess;
            return callee.instances[process];
        }
        options.process = options.process || defaultProcess;
        return (callee.instances[options.process] = ({
            state: [],
            loaded: [],
            failed: [],
            settings: {
                urls: [],
                onComplete: null,
                onLoading: null,
                workspace: null,
                gather: true,
                lazy: 0
            },
            init: function (options) {
                var self = this;
                $.extend(true, self.settings, options);
                $($.proxy(self.onReady, self));
                return self;
            },
            onReady: function () {
                var self = this;
                if (self.settings.gather) {
                    self.gatherImages(self.settings.workspace);
                }
                self.onStart();
            },
            onStart: function () {
                var self = this,
                    info = {
                        all: self.settings.urls.length,
                        loaded: 0,
                        success: 0,
                        error: 0,
                        progressed: 0
                    },
                    trigger = function (method, args, index) {
                        var eventObject = $.extend({}, args);
                        if (index !== undefined && index !== null) {
                            eventObject.url = self.settings.urls[index];
                        }
                        method && method.call(self, eventObject);
                    };
                if (self.aborted) return;
                trigger(self.settings.onStart, info);
                if (!info.all) {
                    trigger(self.onComplete, info);
                } else {
                    // TODO: Delay?
                    $.each(self.settings.urls, function (index, url) {
                        if (self.aborted) return false;
                        if (historyLoaded[url] || historyFailed[url]) {
                            info.loaded++;
                            historyLoaded[url] && info.success++;
                            historyFailed[url] && info.error++;
                            trigger(self.onLoading, info, index);
                            return true;
                        }
                        var image = new Image(),
                            unbind = function () {
                                image.onload = image.onerror = null;
                            };
                        image.onload = function () {
                            unbind();
                            info.loaded++;
                            info.success++;
                            self.loaded[url] = true;
                            historyLoaded[url] = true;
                            trigger(self.onLoading, info, index);
                        };
                        image.onerror = function () {
                            unbind();
                            info.loaded++;
                            info.error++;
                            self.failed[url] = true;
                            historyFailed[url] = true;
                            trigger(self.onLoading, info, index);
                        };
                        image.src = url;
                    });
                }
            },
            onLoading: function (event) {
                var self = this;
                if (self.aborted) return;
                event.progressed = Math.round((event.loaded / event.all) * 100);

                function loading() {
                    if (self.aborted) return;
                    if (self.settings.onLoading) {
                        self.settings.onLoading.call(self, event);
                    }
                    if (event.loaded === event.all) {
                        self.onComplete.call(self, event);
                    }
                }
                if (!self.settings.lazy) loading();
                else setTimeout(loading, event.loaded * self.settings.lazy);
            },
            onComplete: function (event) {
                var self = this;
                if (self.aborted) return;
                if (self.settings.onComplete) {
                    delete event.url;
                    event.progressed = 100;
                    self.settings.onComplete.call(self, event);
                }
            },
            abort: function () {
                var self = this;
                self.aborted = true;
            },
            gatherImages: function (workspace) {
                var self = this;

                function addUrl(url) {
                    var key = url;
                    if (self.state[key]) return;
                    var url = self.buildUrl(url);
                    self.settings.urls.push(url);
                    self.state[key] = true;
                }
                $(workspace || document).find('*:not(script, link)').each(function () {
                    var element = $(this),
                        background = element.css('backgroundImage'),
                        matches;
                    // TODO: Not support :befor/:after
                    if (background && background.indexOf('url') !== -1) {
                        if ((matches = background.match(/^url\("?([^"]*)"?\)/))) {
                            addUrl(matches[1]);
                        }
                    }
                    if (element.get(0).tagName.toLowerCase() === 'img') {
                        if ((matches = element.attr('data-src'))) {
                            element.attr('src', matches);
                            addUrl(matches);
                        } else if ((matches = element.attr('src'))) {
                            addUrl(matches);
                        }
                    }
                });
            },
            parseCss: function () {
                // TODO...
            },
            buildUrl: function (url, workspace) {
                var self = this,
                    baseUrl = self.baseUrl();
                if (baseUrl && url && !url.match(/^https?:\/\/.+$/i) && !url.match(/^\//)) {
                    url = baseUrl.replace(/\/*$/, '/' + url);
                }
                return url;
            },
            baseUrl: function () {
                var self = this;
                if (arguments.callee.cache) return arguments.callee.cache;
                return (arguments.callee.cache = $('base[href]').attr('href'));
            },
            isLoaded: function (uri) {
                var self = this,
                    url = self.buildUrl(uri);
                return !!self.loaded[url];
            }
        })
            .init(options));
    }
})(jQuery);;

/*=============================================================================
    * 等高
    =============================================================================*/
;
(function ($, window, document, undefined) {
    'use strict';

    var $list = $('.listH'),
        $items = $list.find('.list-item'),
        setHeights = function () {
            $items.css('height', 'auto');

            var perRow = Math.floor($list.width() / $items.width());
            if (perRow == null || perRow < 2) return true;

            for (var i = 0, j = $items.length; i < j; i += perRow) {
                var maxHeight = 0,
                    $row = $items.slice(i, i + perRow);

                $row.each(function () {
                    var itemHeight = parseInt($(this).outerHeight());
                    if (itemHeight > maxHeight) maxHeight = itemHeight;
                });
                $row.css('height', maxHeight);
            }
        };

    setTimeout(function () {
        setHeights();
    }, 400);

    $(window).on('resize', setHeights);
    $list.find('img').on('load', setHeights);


})(jQuery, window, document);
