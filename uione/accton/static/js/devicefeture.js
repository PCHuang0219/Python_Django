let initLoadFunction = function(){
    getTestPlanTable([])

}


let filter = function(){
    var list = '';
    var ul ='';
    for(var x=0;x<odata.length;x++)
                {
                    var dname=odata[x];

                    ul += '<li><input type="checkbox" id="'+ dname['test'] +
                            '" value="'+dname['test']+
                            '" name="check_device">'+
                            '<label for="'+ 
                            dname['test'] +
                            '">'+dname['test']+'</label></li>';

                    if(x%6==0 && x!=0){
                        list += '<ul>' + ul +'</ul>';

                        ul='';
                    }
                    
                }
                $("#filtercondition").append(list);
                return runCondition();

}

let getTestPlanTable = function(device){
    $.ajax({
        type: "get",
        url: window.location.origin + "/sonic/devicefeture/table",
        data:{},
        dataType: "json",
        success: function(data, status){
            //console.log(data,status)
            $(".table tbody").empty();
            let html = "";
            let title = "";
            odata = data['data'];
            var a = Object.keys(odata[1]);
            $(".table thead").empty();
            $(".table tbody").empty();
            $("#filtercondition").empty();
           // console.log(device.length)
            
            if(device.length<1){
                for(var i=0;i <a.length;i++)
                {
                    topic = a[i];
                   // console.log(topic)
                    let content ="";
                    for(var j=0;j<odata.length;j++)
                    {   
                        var element =[];
                       
                        element = odata[j];
                        //element = element[0];
                        //console.log(odata[j])
                        if(topic!='test')
                            {
                            content += "<td>" + element[topic] + "</td>" ;
                            }
                        else{
                            title += "<th>" + element[topic] +"</th>";
                        }
                    }
                    if(topic =='test' | topic =='_id')
                        {
                            continue;
                        }
                    html += "<tr>" + "<td>" + a[i] + "</td>" + content +"</tr>";
                } 
                title = "<tr><td></td>" + title + "</tr>";
                $(".table thead").append(title);
                $(".table tbody").append(html);
            }
            else{
                let result = [];
                for(let g=0;g<device.length;g++)
                    {
                        result.push(odata.filter(item => item.test == device[g]))
                    }
                for(var i=0;i <a.length;i++)
                {
                    topic = a[i];
                    let content ="";
                  //  console.log(result.length)
                    for(var j=0;j<result.length;j++)
                    {   
                        element =result[j];
                        element = element[0];
        
                        if(topic!='test')
                            {
                            content += "<td>" + element[topic] + "</td>" ;
                            }
                        else{
                            title += "<th>" + element[topic] +"</th>";
                        }
                    }
                    if(topic =='test' | topic =='_id')
                        {
                            continue;
                        }
                    html += "<tr>" + "<td>" + a[i] + "</td>" + content +"</tr>";
                } 
                title = "<tr><td>" + title + "</tr>";
                $(".table thead").append(title);
                $(".table tbody").append(html);
            }

            filter();

           
            
            // select value
            

        },
    })
    localStorage.clear();
    
}

// let createFilterCondition = function(){
//     $("#addViewsCondition").click(function(){
//         console.log('ININDER')
//         html = '<div class="col-xs-12"> \
//                     <div class="col-xs-6"> \
//                         Condition<span class="red">*</span>：<br> \
//                         <select class="col-xs-6"> \
//                             <option>Device</option> \
//                         </select> \
//                     </div> \
//                     <div class="col-xs-6"> \
//                         Value<span class="red">*</span>：<br> \
//                         <select class="col-xs-8"> \
//                         </select> \
//                         <a class="btn btn-primary deleteCondition">Delete</a> \
//                     </div> \
//                 </div>'
//         $("#filtercondition").append(html)
//         deleteCondition()
//         //selectCondition()
//     })
// }
// let selectCondition = function(){

//         condition = 'test';
//         value_selection = $(this).next().children('select')
//         console.log(condition)
//             $.ajax({
//                 type:'get',
//                 data:{data:condition},
//                 dataType:'json',
//                 url: window.location.origin + "/sonic/devicefeture/table",
//                 success:function(data){
//                     console.log(condition)
//                     data = data["data"]
//                     console.log(data)
//                     html = '<select class="col-xs-8">'
//                     for ( var i=0 ; i < data.length ; i++){
//                         html += "<option>" + data[i] + "</option>"
//                     }

//                     html += '</select>'
//                     value_selection.replaceWith(html)
//                 }
//             })
        
       
// }



// let deleteCondition = function(){
//     $(".deleteCondition").click(function(){
//         if ($(this).parent().parent().parent().children().length != 1){
//             $(this).parent().parent().remove()
//         }
//     })
// }


// let dateAdd = function (startDate,days) {
//     startDate = new Date(startDate);
//     startDate = +startDate + days * 1000 * 60 * 60 * 24;
//     startDate = new Date(startDate);
//     var nextStartDate = startDate.getFullYear() + "-" + (startDate.getMonth() + 1) + "-" + startDate.getDate();
//     return nextStartDate;
// }

let runCondition = function(){
    $("#updateTRRViews").click(function(){
        var checkbox = new Array();
        $('input:checkbox:checked[name="check_device"]').each(function(i){checkbox[i]=this.value});
       // console.log(checkbox)
        $('#c').attr('class','modal');
        $('.modal-backdrop').remove();
        $('#c').css("display","none");
        getTestPlanTable(checkbox);
       // location.href = window.location.origin + "/sonic/devicefeture"
    })
}

/*
let ConvertMutilValueToMongoDB = function(html,key,value_list){
    if (value_list.length >0){
        if (html.indexOf('"') != -1){
            html += ','
        }
        if (value_list.length == 1){
            if (!value_list[0]){
                value_list[0] = ""
            }
            if (!key.includes('time')){
                html += '"' + key + '":"' + value_list[0] + '"'
            }
            else{
                if (value_list[0][0] == '≡'){
                    date = value_list[0][1]
                    nextDate = dateAdd(value_list[0][1], 1)
                    html += '"' + key + '":{"$lte":ISODate("' + nextDate + '"),"$gte":ISODate("' + date + '")}'
                }
                if (value_list[0][0] == '≤'){
                    html += '"' + key + '":{"$lte":ISODate("' + value_list[0][1] + '")}'
                }
                if (value_list[0][0] == '≥'){
                    html += '"' + key + '":{"$gte":ISODate("' + value_list[0][1] + '")}'
                }
            }
        }
        else {
            if (!key.includes('time')){
                buff = "["
            }
            for(var i=0 ; i < value_list.length ; i++){
                if ( i>0 ){
                    buff += ','
                }
                if (!value_list[i]){
                    value_list[i] = ""
                }
                if (!key.includes('time')){
                    buff += '"' + value_list[i]  + '"' 
                }
                else{
                    if (value_list[0][0] == '≡'){
                        buff += '"' + key + '":"ISODate(' + value_list[0][1] + ')"'
                    }
                    if (value_list[0][0] == '≤'){
                        buff += '"' + key + '":{"$lte":"ISODate(' + value_list[0][1] + ')"}'
                    }
                    if (value_list[0][0] == '≥'){
                        buff += '"' + key + '":{"$gte":"ISODate(' + value_list[0][1] + ')"}'
                    }
                     
                }
            }
            if (!key.includes('time')){
                buff += "]"
                html += '"' + key + '":{"$in":' + buff + "}"
            }
            else{
                html += '"' + key + '":{' + buff + "}"
            }
        }
        return html
    }
    return html
}
*/
addLoadEvent(initLoadFunction);