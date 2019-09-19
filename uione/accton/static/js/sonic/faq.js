// function expandQuestion(){
//     var title=$(this).attr("value");
//     console.log($(this));
// }
let expandQuestion=function(){
    $(".collapse_all").click(function(){
    var q = "#"+$(this).attr("value");
    $(this).attr("style","display:none")
    $(q).attr("style","display:block");
})
    $(".model").click(function(){
    var q = "#"+$(this).attr("value");
    if ($(q).attr("style")=="display:none"){
    $(q).attr("style","display:block");}
    else{
    $(q).attr("style","display:none");
    }  
})
}

let changoUpDownIcon=function(){
    $("a").click(function(){
        var icon_status = $(this).children().children().children().attr("class");
        if (icon_status == "fa fa-angle-up" ){
            $(this).children().children().children().attr("class","fa fa-angle-down");
        }
        else{
            $(this).children().children().children().attr("class","fa fa-angle-up");
        }
    })
}
addLoadEvent(expandQuestion);
addLoadEvent(changoUpDownIcon);
