let initialEvent = () => {
    initialCommentFormClose();
    article_id = localStorage.getItem("article_id")
    getArticleData();
    getArticleMessage();
    setClickCommentEvent();
    setPostNewAnswerEvent();
    updateArticleView();
    console.log(is_authenticated);
}
addLoadEvent(initialEvent);

let updateArticleView = () => {
    article_id = localStorage.getItem("article_id")
    console.log(article_id)
    $.ajax({
        type: "post",
        url: "http://"+ Config.ip_address + Config.port + "/sonic/forum/putArticleViews/",
        data:{article_id:article_id,},
        dataType: "json",
        success: function(data){
            // location.replace("http://"+ Config.ip_address + Config.port + "/sonic/accton/forum");
        },
    })
}

let initialCommentFormClose = () => {
    $(".comment-form").hide();
}

let setClickMessageAwesomeEvent = function(){
    article_id = $("#article_id").text()
    $(".awesome-button").click(function(){
        if(!is_authenticated){
            location.href = "http://"+ Config.ip_address + Config.port + "/accounts/login"
            return;
        }
        if($(this).parent().find(".bad-button path").css("fill") === "rgb(255, 0, 0)"){
        }
        else if($(this).find("path").css("fill") === "rgb(115, 135, 156)"){
            $(this).find("path").css("fill","red")
            $.ajax({
                type: "post",
                url: "http://"+ Config.ip_address + Config.port + "/sonic/forum/putMessageAwesome/",
                data:{article_id:article_id,message_id:$(this).next().text(),},
                dataType: "json",
                success: function(data){
                    location.replace("http://"+ Config.ip_address + Config.port + "/sonic/accton/forum");
                },
            })
            awesome_number = $(this).parent().find("#awesome_number").text()
            $(this).parent().find("#awesome_number").text(Number(awesome_number)+1)
        }
        else{
            $(this).find("path").css("fill","rgb(115, 135, 156)")
            $.ajax({
                type: "post",
                url: "http://"+ Config.ip_address + Config.port + "/sonic/forum/deleteMessageAwesome/",
                data:{article_id:article_id,message_id:$(this).next().text(),},
                dataType: "json",
                success: function(data, status){
                    console.log(status)
                    console.log(data)
                },
            })
            awesome_number = $(this).parent().find("#awesome_number").text()
            $(this).parent().find("#awesome_number").text(Number(awesome_number)-1)
        }
    });
}


let setClickMessageBadEvent = function(){
    $(".bad-button").click(function(){
        if(!is_authenticated){
            location.href = "http://"+ Config.ip_address + Config.port + "/accounts/login"
            return;
        }
        if($(this).parent().find(".awesome-button path").css("fill") === "rgb(255, 0, 0)"){
        }
        else if($(this).find("path").css("fill") === "rgb(115, 135, 156)"){
            $(this).find("path").css("fill","red")
            $.ajax({
                type: "post",
                url: "http://"+ Config.ip_address + Config.port + "/sonic/forum/putMessageBad/",
                data:{article_id:article_id,message_id:$(this).parent().find("#message_id").text(),},
                dataType: "json",
                success: function(data, status){
                    console.log(status)
                    console.log(data)
                },
            })
            awesome_number = $(this).parent().find("#awesome_number").text()
            $(this).parent().find("#awesome_number").text(Number(awesome_number)-1)
        }
        else{
            $(this).find("path").css("fill","rgb(115, 135, 156)")
            $.ajax({
                type: "post",
                url: "http://"+ Config.ip_address + Config.port + "/sonic/forum/deleteMessageBad/",
                data:{article_id:article_id,message_id:$(this).parent().find("#message_id").text(),},
                dataType: "json",
                success: function(data, status){
                    console.log(status)
                    console.log(data)
                },
            })
            awesome_number = $(this).parent().find("#awesome_number").text()
            $(this).parent().find("#awesome_number").text(Number(awesome_number)+1)
        }
    });
}

let setPostNewAnswerEvent = function(){
    $("#send").click(function(){
        if(!is_authenticated){
            location.href = "http://"+ Config.ip_address + Config.port + "/accounts/login"
            return;
        }
        article_id = $("#article_id").text()
        message_id = "NULL"
        content = $(this).parent().find("#message_content").val()
        $.ajax({
            type: "post",
            url: "http://"+ Config.ip_address + Config.port + "/sonic/forum/postNewReply/",
            data:{article_id:article_id,message_id:message_id,content:content },
            dataType: "json",
            success: function(data, status){
                console.log(status)
                getArticleMessage();
            },
        })
        $(this).parent().find("#message_content").val("");
    });
}

let setPostNewReplyEvent = function(){
    $(".send-reply").click(function(){
        if(!is_authenticated){
            location.href = "http://"+ Config.ip_address + Config.port + "/accounts/login"
            return;
        }
        article_id = $("#article_id").text()
        message_id = $(this).parent().parent().parent().find("#message_id").text()
        content = ($(this).parent().parent().parent().find("#message_content").val())
        $.ajax({
            type: "post",
            url: "http://"+ Config.ip_address + Config.port + "/sonic/forum/postNewReply/",
            data:{article_id:article_id,message_id:message_id,content:content},
            dataType: "json",
            success: function(data, status){
                console.log(status)
                getArticleMessage();
            },
        })
         $(this).parent().parent().parent().find("#message_content").val("");
    });
}


let getArticleData = () => {
    let article_id = localStorage.getItem("article_id")
    $.ajax({
        type: "get",
        url: "http://"+ Config.ip_address + Config.port + "/sonic/forum/getArticle/",
        data:{article_id:article_id,},
        dataType: "json",
        success: function(data, status){
            console.log(data)
            console.log(data["data"])
            data = data["data"]
            updateArticleInfoView(data);
            updateArticleContentView(data["content"]);
            updateArticleTagView(data["tag"])
            updateJudgeMessageView(article_id);
            updateAuthorInfoView(data);
        },
    })
}

let getArticleMessage = () => {
    let article_id = localStorage.getItem("article_id")
    $.ajax({
        type: "get",
        url: "http://"+ Config.ip_address + Config.port + "/sonic/forum/getArticleMessage/",
        data:{article_id:article_id,},
        dataType: "json",
        success: function(data, status){
            data = data["data"]
            let answer_num = updateReplyView(data);
            $("#answer-number").text(answer_num + " Answers")
        },
    })
}

let updateArticleInfoView = (data) =>{
    $("#article_content").empty()
    $("#article_id").text(data["id"])
    $("#article_title").text(data["title"])
}

let updateAuthorInfoView = (data) =>{
    $("#ask-time").text(data["time"])
    $("#asker img").attr("src","data:image/jpeg;base64," + data["author_personal_image"].split("'")[1])
    $("#asker-name").text(data["author_first_name"] + data["author_last_name"])
}


let updateArticleContentView = (content) => {
    let html = ""
    content.split("\n").forEach((element) => {
        html += '<p>'+element+'</p>';
    });
    $("#article_content").append(html)
}

let updateJudgeMessageView = (article_id) => {
    $.ajax({
        type: "get",
        url: "http://"+ Config.ip_address + Config.port + "/sonic/forum/getJudgeMessage/",
        data:{article_id:article_id,},
        dataType: "json",
        success: function(data, status){
            for(var i=0 ; i <data.length ; i++){
                element = data[i]
                $('#'+element["judge_type"]+'-'+element["message_id"]).find("path").css("fill","rgb(255, 0, 0)")
            }
        },
    })
}

let updateArticleTagView = (tag_list) => {
    let html = ""
    tag_list.forEach((element) => {
        html += '<a>'+element["tag_name"]+'</a>'
    });
    $("#tag-list").append(html);  
};

let updateReplyView = (message_list) => {
    let answer_num = 0;
    $("#message-list").empty()
    message_list.forEach((element) => {
        let html = "";
        if(element["main_message_id"])
        {
            html += 
            '<div class="col-1 col-sm-1"> \
            </div> \
            <div class="col-11 col-sm-11"> \
                <div class="reply-awesome"> \
                    <span>'+element["awesome_number"]+'</span> \
                </div> \
                <div class="reply-message-content"> \
                    <div class="content"> \
                        <span>'+element["content"]+' – <a>'+element["first_name"] + element["last_name"]+'</a><span class="reply-date"> '+element["time"]+'</span></span> \
                    </div> \
                </div> \
            </div>'
            $('#reply-'+element["main_message_id"]).append(html);  
        }
        else{
            answer_num += 1
            html += 
            '<div class="row message"> \
                <div class="col-12 col-sm-12"> \
                    <div class="col-1 col-sm-1 awesome" > \
                        <button class="awesome-button" id=awesome-'+element["id"]+'> \
                            <svg aria-hidden="true" class="svg-icon m0 iconArrowUpLg" width="12" height="12" viewBox="0 0 36 36"><path d="M2 26h32L18 10 2 26z"></path></svg> \
                        </button> \
                        <div id="message_id" style="display:None">'+element["id"]+'</div> \
                        <div id="awesome_number">'+element["awesome_number"]+'-'+element["bad_number"]+'</div> \
                        <button class="bad-button" id=bad-'+element["id"]+'> \
                            <svg aria-hidden="true" class="svg-icon m0 iconArrowDownLg" width="12" height="12" viewBox="0 0 36 36"><path d="M2 10h32L18 26 2 10z"></path></svg> \
                        </button> \
                    </div> \
                    <div class="col-11 col-sm-11 message-content"> \
                        <div class="content">'
            
            element["content"].split("\n").forEach((element) => {
                html += '<p>'+element+'</p>';
            });
            html += '</div> \
                        <div> \
                            <div class="time col-12 col-sm-12"> \
                                <div>'+element["time"]+'</div> \
                            </div> \
                            <div class="replier"> \
                                <img width="40" height="40" src=data:image/jpeg;base64,'+element["personal_image"].split("'")[1]+'></img> \
                                <div>'+element["first_name"] + element["last_name"]+'</div> \
                            </div> \
                        </div> \
                    </div> \
                </div> \
                <div class="row reply" id=reply-'+element["id"]+'> \
                </div> \
                <div class="col-xs-1"></div> \
                <div class="col-xs-11"> \
                    <div class="add-comment"> \
                        add a comment \
                    </div> \
                    <div class="comment-form"> \
                        <form> \
                            <textarea class="form-control" id="message_content" rows="2"></textarea> \
                        </form> \
                        <button type="button" class="btn btn-primary btn-sm send-reply">SEND</button> \
                    </div> \
                </div> \
            </div>'
           $("#message-list").append(html);  
        }
    });
    initialCommentFormClose();
    setClickCommentEvent();
    setPostNewReplyEvent();
    setClickMessageAwesomeEvent();
    setClickMessageBadEvent();
    return answer_num;
}

let setClickCommentEvent = function(){
    $(".add-comment").click(function(){
        if($(this).next().is(":hidden")){
            $(this).next().show();
        }
        else{
            $(this).next().hide();
        }
    });
}

