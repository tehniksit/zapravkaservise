$('.popup .close_window, .overlay').load(function (){
$('.popup, .overlay').css({'opacity': 0, 'visibility': 'hidden'});
});

$(window).load(function (e){
$('.popup, .overlay').css({'opacity': 1, 'visibility': 'visible'});
e.preventDefault();
alert('hel');
});


/*
window.onload = function () {
    document.querySelector('#show_count').onclick = function () {
        ajaxGet();
    }
    
};

function ajaxGet() {
    var request = new XMLHttpRequest();
    
    request.onreadystatechange = function () {
        //noinspection JSAnnotator
        if(request.readyState === 4) {
            document.querySelector('#cont_count').innerHTML = request.responseText;
        }

        
    };


    request.open('GET', 'ajax/more/');
    request.send();
    
    
}*/

/* AJAX GET
$('#show_count').click(function(){

    $.ajax({
        type: "GET",
        url: "ajax/more/",
        success: function(data) {
            $('#cont_count');
    }
    });

});
*/
