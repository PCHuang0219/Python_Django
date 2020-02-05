let submit_click_event = () =>{
    $("#submit").click(function(){
        postArticle();
    });
} 

addLoadEvent(submit_click_event);

let postArticle = function(){
    article_title = document.getElementById("article_title").value;
    article_content = document.getElementById("article_content").value;
    article_tag = document.getElementById("article_tag").value;
    split_list = article_tag.split("#")
    tag_list = []
    if(article_title == ""){
        alert("title cannot be empty!")
        return;
    }
    if(article_content == ""){
        alert("content cannot be empty!")
        return;
    }
    split_list.forEach(element => {
        if(element != ""){
            tag_list.push(element);
        }
    });
    $.ajax({
        type: "post",
        url: window.location.origin + "/sonic/forum/postNewArticle/",
        data:{"article_title" : article_title,"article_content" : article_content,"article_tag" : tag_list,},
        dataType: "json",
        success: function(data){
            location.replace(window.location.origin + "/sonic/accton/forum");
        },
    })
}