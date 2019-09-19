let addInputButton = function(){
    $("#select_file").click(function() {
        var input = $(document.createElement("input"));
        input.attr("id", "select_image");
        input.change(function(){
        });
        input.attr("type", "file");
        input.attr("accept", ".bin");
        input.trigger("click"); // opening dialog
        return false; // avoiding navigation
    });
}

let submitTestCase = function(){
    let value_list =  []
    $('#imageCase input[type="checkbox"]:checked').each(function(){
        let image_dir = $.trim($(this).parent().parent().parent().clone().children().remove().end().text());	//get the text of element);
        let image_name = $(this).parent().text()
        value_list.push(image_dir+"/"+image_name)
    });
    if(value_list.length > 1)
    {
        alert("only allow choose one Image!");
        value_list = []
        return;
    }
    localStorage.setItem("image_path",value_list);
    localStorage.setItem("change_page","1");
    // location.href = document.referrer;
    location.href = "http://" + Config.ip_address + Config.port + "/test/"
}

let getImageTable = function(){
    $.ajax({
        type: "get",
        url: "http://"+ Config.ip_address + Config.port + "/test/image/imageTable/",
        data:{},
        dataType: "json",
        success: function(data, status){
            let html = ""
            $("#imageCase").empty();
            data = data["image_table"]
            // console.log(data)
            let last_num = 0
            for(var i = 0; i < data.length;i++)
            {
                if(i == 0 || data[i]["server_name"] != data[i-1]["server_name"])
                {
                    // console.log("all")
                    html = addAll(html,data,i);
                }
                else if(data[i]["chip_company_name"] != data[i-1]["chip_company_name"])
                {
                    // console.log("company_name")
                    html = addCompany(html,data,i);
                }
                else if(data[i]["build_type"] != data[i-1]["build_type"])
                {
                    // console.log("build type")
                    html = addBuildType(html,data,i);
                }
                else
                {
                    // console.log("name")
                    html = addBuildNumber(html,data,i);
                }
            }
            html += "</ul>" + "</li>" + "</ul>" + "</li>" + "</ul>" +"</li>" + "</ul>"
            // console.log(html);
            $("#imageCase").append(html);
        },
    })
}

let addFinalTag = function(html,now_num,last_num){
    for(var y = 0; y < Math.abs(last_num - now_num);y++)
    {
        html += "</ul>" + "</li>" 
    }
    return html;
}

let addAll = function(html,data,i){
    if(i != 0)
    {
        html += "</ul>" + "</li>" + "</ul>" + "</li>" + "</ul>" + "</li>" + "</ul>" + "</li>" 
    }
    html += "<ul>" + 
    "<li style='color: crimson'>" + data[i]["server_name"] + 
    "<ul>" + 
            "<li style='color:brown'>" + data[i]["chip_company_name"] + 
            "<ul>" + 
                    "<li style='color: black'>" + data[i]["build_type"] + 
                    "<ul>" + 
                            "<label style='color: blueviolet'><input type='checkbox'>" + data[i]["build_number"] + "</label><br>"
    return html;
}

let addCompany = function(html,data,i){
    html += "</ul>" + "</li>" + "</ul>" + "</li>"  + 
            "<li style='color:brown'>" + data[i]["chip_company_name"] + 
            "<ul>" + 
                    "<li style='color: black'>" + data[i]["build_type"] + 
                    "<ul>" + 
                            "<label style='color: blueviolet'><input type='checkbox'>" + data[i]["build_number"] + "</label><br>"
    return html;

}

let addBuildType = function(html,data,i){
    html += "</ul>" + "</li>" + 
            "<li style='color: black'>" + data[i]["build_type"] + 
            "<ul>" + 
                "<label style='color: blueviolet'><input type='checkbox'>" + data[i]["build_number"] + "</label><br>" 
    return html;

}

let addBuildNumber = function(html,data,i){
    html += "<label style='color: blueviolet'><input type='checkbox'>" + data[i]["build_number"] + "</label><br>"
    return html;
}

addLoadEvent(getImageTable);
addLoadEvent(addInputButton);