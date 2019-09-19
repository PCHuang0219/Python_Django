let clickArticle = () => {
    $(".article").click(function(){
        article_id =$(this).children(":first").text() 
        console.log(article_id)
        localStorage.setItem("article_id",article_id);
        location.href = "http://" + Config.ip_address + Config.port +"/sonic/accton/forum/showArticle";
    });
}

let setPageNavigationNextFocusOut = () => {
    $("#previous>a").blur();
    $("#next>a").blur(); 
}

const setInitialPageButtonDisableView = async () => {
    const article_total_number = await getArticleTotalNumber();
    let page_middle_number = 2
    updatePagePreviousButtonView(checkIsInitPagination(page_middle_number));
    updatePageNextButtonView(checkIsLastPageNumber(page_middle_number,article_total_number));
}

let setClickPageNavigationEvent = () => {
    $(".page-selector li").click(async function(){
        label_name = $(this).children('a').children('span').eq(1).text()
        const article_total_number = await getArticleTotalNumber();
        article_total_page_number = getTotalPageNumber(article_total_number);
        //pagination eq index: 0 1 2 3 4 
        const MIDDLE_PAGE_INDEX = 2
        if(label_name == "Previous"){
            let page_middle_number = parseInt($(".page-selector li").children('a').eq(MIDDLE_PAGE_INDEX).text());
            updatePageNavigationView(page_middle_number-3,article_total_page_number);
            // $(".page-selector li").children('a').eq(1).focus();
        }
        else if(label_name == "Next"){
            let page_middle_number = parseInt($(".page-selector li").children('a').eq(MIDDLE_PAGE_INDEX).text());
            updatePageNavigationView(page_middle_number+3,article_total_page_number);
            // $(".page-selector li").children('a').eq(3).focus();
        }
        else{
            let page_number = parseInt($(this).text()) 
            getArticle(page_number);
            $(this).focus();
        }
        let page_middle_number = parseInt($(".page-selector li").children('a').eq(MIDDLE_PAGE_INDEX).text());
        setPageNavigationNextFocusOut();
        updatePagePreviousButtonView(checkIsInitPagination(page_middle_number));
        updatePageNextButtonView(checkIsLastPageNumber(page_middle_number,article_total_number));
    });
}

let updatePageNextButtonView = (is_disable) => {
    if(is_disable){
        document.getElementById('next').style.pointerEvents = 'none';
        $("#next").addClass("disabled");
    }
    else{
        document.getElementById('next').style.pointerEvents = 'auto';
        $("#next").removeClass("disabled");
    }
}

let updatePagePreviousButtonView = (is_disable) => {
    if(is_disable){
        document.getElementById('previous').style.pointerEvents = 'none';
        $("#previous").addClass("disabled");
    }
    else{
        document.getElementById('previous').style.pointerEvents = 'auto';
        $("#previous").removeClass("disabled");
    }
}

let checkIsInitPagination = (page_middle_number) => {
    return (page_middle_number <= 2) ? true : false;
}

let checkIsLastPageNumber = (page_middle_number,article_total_number) => {
    return (page_middle_number + 2 > getTotalPageNumber(article_total_number)) ? true : false;
}

let getTotalPageNumber = (article_total_number) =>{
    auto_add =  ((article_total_number%10) > 0) ? 1 : 0;
    article_total_page_number = parseInt(article_total_number/10) + auto_add
    return article_total_page_number;
}

let updatePageNavigationView = (page_number,article_total_page_number) =>{
    if(page_number <= 1 || article_total_page_number <= 3){
        $(".page-selector li").children('a').eq(1).text(1);
        $(".page-selector li").children('a').eq(2).text(2);
        $(".page-selector li").children('a').eq(3).text(3);
    }
    else if(page_number >= article_total_page_number){
        $(".page-selector li").children('a').eq(1).text(article_total_page_number-2);
        $(".page-selector li").children('a').eq(2).text(article_total_page_number-1);
        $(".page-selector li").children('a').eq(3).text(article_total_page_number);
    }
    else{
        $(".page-selector li").children('a').eq(1).text(page_number-1);
        $(".page-selector li").children('a').eq(2).text(page_number);
        $(".page-selector li").children('a').eq(3).text(page_number+1);
    }
}

const getArticleTotalNumber = async function(){
    const getResult = await Promise.resolve($.get("http://"+ Config.ip_address + Config.port + "/sonic/forum/getArticleListLength/",));
    article_total_number = getResult["article_total_number"]
    return article_total_number;
}

let getArticle = (page_number = 1) => {
    $.ajax({
        type: "get",
        url: "http://"+ Config.ip_address + Config.port + "/sonic/forum/getArticleList/",
        data:{page_number:page_number,},
        dataType: "json",
        success: function(data){
            showArticleByTopBar(data);
        showArticle(data);
        clickArticle();
        },
    })
}

let showArticle=function(data_list){
    $("#article_list").empty();   
    let html = "";
    // console.log(data_list)
    data_list.forEach((element) =>{
        html +=   
        '<div class="col-sm-12 col-xs-12 article"> \
            <div style="display:none">'+element["id"]+'</div> \
            <div class="col-sm-2 col-xs-2 user-info"> \
                <img src=data:image/jpeg;base64,'+element["personal_image"].split("'")[1]+' style="width:60%" > \
                <p class="user-name"> '+element["user__first_name"] + element["user__last_name"]+' </p> \
            </div> \
            <div class="col-sm-8 col-xs-8 titile"> \
                <h3>'+element["title"]+'</h3> \
                <p>'+element["content"].substring(0,100)+'...</p> \
            </div> \
            <div class="col-sm-2 col-xs-2 post-info"> \
                <div class="comments"> \
                    <div class="commentbg"> \
                        <div class="mark"></div>'+
                        element["reply_number"]+
                    '</div> \
                </div> \
                <div class="views"> \
                    <i class="fa fa-eye show">'+
                        element["view_number"]+
                    '</i> \
                </div> \
                <div class="fa fa-clock-o show">'+
                        element["time"]+
                '</div> \
            </div> \
        </div>'
    })
    $("#article_list").append(html);
    clickArticle();
}

let getAllTagName=function(){
    $.ajax({
        type: "get",
        url: "http://"+ Config.ip_address + Config.port + "/sonic/forum/getAllTagName/",
        dataType: "json",
        success: function(data){
            data = data["status"];
            showTag(data);
        },
    })
}

let showTag=function(data_list){
    var html = '';
    var page_number=1;
    data_list.forEach((element) => {
        html+='<li class="list-group-item" value="'+element["tag_name"]+'">'+element["tag_name"]+'<span class="badge">'+element["count"]+'</span></li>'
    })
    $("#tag_sort").empty();
    $("#tag_sort").append(html);
    showSelectTagArticle(page_number);
}

let showSelectTagArticle=function(page_number = 1){
    $(".list-group-item").click(function(){
        var tag_name = $(this).attr("value");
        $.ajax({
            type: "get",
            url: "http://"+ Config.ip_address + Config.port + "/sonic/forum/getArticleList/",
            data:{page_number:page_number,tag_name:tag_name,},
            dataType: "json",
            success: function(data){
                var html = '' ;
               for( var i=0 ; i < data.length ; i++){
                    element = data[i]
                    var date = element["article__time"].substring(0,10);
                    var time = element["article__time"].substring(11,19);
                    html +=
                    '<div class="col-sm-12 col-xs-12 article"> \
                        <div style="display:none">'+element["article__id"]+'</div> \
                        <div class="col-sm-2 col-xs-2 user-info"> \
                            <img src=data:image/jpeg;base64,'+element["personal_image"].split("'")[1]+' style="width:60%" > \
                            <p class="user-name"> '+element["article__user__first_name"] + element["article__user__last_name"]+' </p> \
                        </div> \
                        <div class="col-sm-8 col-xs-8 titile"> \
                            <h3>'+element["article__title"]+'</h3> \
                            <p>'+element["article__content"].substring(0,100)+'...</p> \
                        </div> \
                        <div class="col-sm-2 col-xs-2 post-info"> \
                            <div class="comments"> \
                                <div class="commentbg"> \
                                    <div class="mark"></div>'+
                                    element["article__awesome_number"]+
                                '</div> \
                            </div> \
                            <div class="views"> \
                                <i class="fa fa-eye show">'+
                                    element["article__view_number"]+
                                '</i> \
                            </div> \
                            <div class="fa fa-clock-o show">'+
                                date+'<br>'+time+
                            '</div> \
                        </div> \
                    </div>'
                }
                $("#article_list").empty();   
                $("#article_list").append(html);
                clickArticle();
            },
        })
    })
}

let showArticleByTopBar=function(data_list){
    $(".topbar-link").click(function(){
        key = $(this).text();
        if (key == "Popular"){bubble_sort(data_list,"view_number");}
        if (key == "Unanswered"){findNoneElement(data_list,"reply_number");}
        /*if (key == "Popular"){bubble_sort(data_list,"view_number");}
        if (key == "Popular"){bubble_sort(data_list,"view_number");}*/
    })
}

let findNoneElement=function(data_list,key){
    var data = new Array();
    var index=0;
    data_list.forEach((element) =>{
        if ( element[key] == "0" )
        {
            data[index]=element;
            index++;
        }
    })
    showArticle(data);
}
let bubble_sort=function(data_list,element){
    for (let i=0 ; i< data_list.length ; i++){
        for (let j=0 ; j< data_list.length-1 ; j++)  {
            if ( data_list[j][element] < data_list[j + 1][element] )
            {
                let buff = data_list[j];
                data_list[j] = data_list[j+1] ;
                data_list[j + 1] = buff;
            }
        }
    }
    showArticle(data_list);
}

let showArticleNumber = async function(){
    total = await getArticleTotalNumber()
    if ( total > 1000){
        a = total / 1000 
        b = total % 1000
        total = String(a)+","+String(b)
    }
    html = total + ' questions'
    $("#forum_total_number").empty()
    $("#forum_total_number").append(html)
}

let initial = () =>{
    showArticleNumber();
    getArticle();
    getAllTagName();
    setClickPageNavigationEvent();
    setPageNavigationNextFocusOut();
    getArticleTotalNumber();
    setInitialPageButtonDisableView();
} 
addLoadEvent(initial);





