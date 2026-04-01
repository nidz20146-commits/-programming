$(document).ready(function(){
    $('.one-post').hover(
        function(event){
            $(event.currentTarget).find('.one-post-shadow').animate({opacity: '0.1'}, 300);
        },
        function(event){
            $(event.currentTarget).find('.one-post-shadow').animate({opacity: '0'}, 300);
        }
    );
    
    $('.header img').hover(
        function(){
            $(this).stop().animate({width: '+=20px'}, 200);
        },
        function(){
            $(this).stop().animate({width: '-=20px'}, 200);
        }
    );
});