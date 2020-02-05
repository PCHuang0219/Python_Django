let document_list = [];

let expandTable = function() {
    $(".presentationTitle").click(function(){
        var target= "#"+$(this).attr("value");
        var status= $(target).attr("style");
        if ( status == "display:none"){
            $(target).attr("style","display:block");}
        else {
            $(target).attr("style","display:none");
        }
    })
}

let getDocumentList = async function(){
    result = await $.get(window.location.origin + "/sonic/data/documentList/",
    {
    },
    function(data, status){
        data = data["documentList"]
        document_list = data
    });
}

let showDocument = function() {
    $(".showDoc").click(function(){
        var title = $(this).parent().parent().children().first().text();
        var html = "" ;
        html += '<html><head></head><body>';
        for(let i = 0; i < document_list.length; i++){
            if ( document_list[i]["title"] == title ){
                html += '<object data="/static/'+document_list[i]["path"]+'/'+document_list[i]["filename"]+'" type="application/pdf" width="1195" height="2000">';
            }
        }
        html += '</object></body></html>';
        var newWindow = window.open('url','_blank',config='width=1195')
        if (!newWindow) return false ;
        newWindow.document.write(html);
        return newWindow;
    })
}

let updatePresentationTable = async function(){
    let sort_name='';
    let sub_sort_name='';
    let result = await getDocumentList();
    let html = "";

    sub_sort_name = document_list[0]["sub_sort"]
    sort_name = document_list[0]["sort"]
    html += '<h1 style="color:#20304b;text-align: center;padding:20px">Presentations</h1>';
    html = addInitialHtml(html,sort_name,0);
    html = addSubItemInitial(html,sub_sort_name)
    for (let i=0 ; i<document_list.length ; i++){
        if(sort_name == document_list[i]["sort"]){
            if(sub_sort_name == document_list[i]["sub_sort"]){
                html = addContent(html,document_list[i]);
            }
            else{
                sub_sort_name = document_list[i]["sub_sort"]
                html = addSubItemEnd(html)
                html = addSubItemInitial(html,sub_sort_name)
                html = addContent(html,document_list[i]);
            }
        }
        else{
            sort_name = document_list[i]["sort"]
            sub_sort_name = document_list[i]["sub_sort"]
            html = addSubItemEnd(html)
            html += '</div></div>'

            html = addInitialHtml(html,sort_name,i);
            html = addSubItemInitial(html,sub_sort_name);
            html = addContent(html,document_list[i]);
        }

    }
    html = addSubItemEnd(html)
    html += '</div></div>'

    $("#presentations").empty();
    $("#presentations").append(html);
    expandTable();
    showDocument();
}

let addContent = function(html,content){
    html +=
    '<tr> \
        <td data-th="Release Series">'+content["title"]+'</td> \
        <td data-th="Initial Release Date">04/30/2019<br>(Scheduled)</td> \
        <td data-th="Overview"><i class="fa fa-eye showDoc">click</i></td> \
        <td data-th="Download"> \
            <a href="/static/'+content["path"]+'/'+content["filename"]+'"><span aria-hidden="true" class="glyphicon glyphicon-download-alt"></span></a> \
        </td> \
    </tr>'
    return html
}

let addSubItemInitial = function(html,sub_sort_name){
    html += '<h3 style="color:#20304b;text-align:center;">'+sub_sort_name+'</h3>'
    html += '<div class="x_panel">';
    html += '<table class="table table-hover presentationTable"> \
                <tbody> \
                    <tr class="tr-only-hide"> \
                        <td>Release Series</td> \
                        <td>Initial Release Date</td> \
                        <td>Overview</td> \
                        <td>Download</td> \
                    </tr>'
    return html
}

let addSubItemEnd = function(html){
    html += '</tbody></table></div>'
    return html
}

let addInitialHtml = (html,sort_name,index) => {
    html += '<div class="presentationTitle" value="'+index+'"><h3>'+sort_name+'</h3></div>';
    html += '<div id="'+index+'" style="display:none">';
    html += '<div class="x_panel">';
    return html;
}

addLoadEvent(expandTable);
addLoadEvent(showDocument);
addLoadEvent(updatePresentationTable);