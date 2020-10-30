                                    /*Strike-through*/  

$("ul").on("click", "li", function(){
    $(this).toggleClass("completed");
});
                                    /*Delete To-do*/

$("ul").on("click", "span", function(event){
    $(this).parent().slideUp(500, function(){
        $(this).remove();
    });
    event.stopPropagation();
});

$("input").keypress(function(event){
    if(event.which === 13 && $(this).val()!==""){
        console.log("Enter");
        var todoText=$(this).val();
        $(this).val("");
        $("ul").append("<li><span><i class='fa fa-trash'></i></span> "+ todoText +"</li>");
    }
        
});
$(".fa-plus-square").click(function(){
    $("input").fadeToggle("slow");
})
