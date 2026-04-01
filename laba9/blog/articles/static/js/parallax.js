$(document).ready(function(){
    var scrolled = 0;
    var $parallaxElements = $('.icons-for-parallax img');
    var $logo = $('.header .logo');
    var logoStartTop = 15;
    
    // Плавный параллакс с ограничением
    $(window).scroll(function() {
        scrolled = $(window).scrollTop();
        
        // Ограничиваем максимальное смещение
        var maxScroll = 300;
        var limitedScroll = Math.min(scrolled, maxScroll);
        
        // Параллакс для иконок
        for (var i = 0; i < $parallaxElements.length; i++){
            var yPosition = limitedScroll * 0.1 * (i + 1);
            $parallaxElements.eq(i).css({ 
                top: yPosition,
                opacity: 1 - (limitedScroll / 1000) * (i + 0.5)
            });
        }
        
        // Параллакс для логотипа (очень плавный)
        var logoOffset = limitedScroll * 0.03;
        $logo.css({ 
            top: logoStartTop + logoOffset,
            opacity: 1 - (limitedScroll / 2000)
        });
    });
});