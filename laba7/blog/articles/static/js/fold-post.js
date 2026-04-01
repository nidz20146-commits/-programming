document.addEventListener('DOMContentLoaded', function() {
    var foldBtns = document.getElementsByClassName("fold-button");
    
    for (var i = 0; i < foldBtns.length; i++) {
        foldBtns[i].addEventListener("click", function(e) {
            var post = e.target.closest('.one-post');
            
            if (post.classList.contains('folded')) {
                e.target.innerHTML = "свернуть";
                post.classList.remove('folded');
            } else {
                e.target.innerHTML = "развернуть";
                post.classList.add('folded');
            }
        });
    }
});