let postCommand = function(){
    command = document.getElementById("command").value;
    $.post(window.location.origin + "/network/command/",
    {
        command: command
    },function(data, status){
        $("#log").empty();
        console.log(data)
        let html = ""
        data = data["log"]
        for(var i = 0; i < data.length;i++)
        {
            html += "<div>" + data[i] +" "+ "</div>"
        }
        $("#log").append(html);
    });
};