let changeDropdownValue = function(){
    $(".dropdown-menu li a").click(function(){
        $(this).parents(".dropdown").find('.btn').html($(this).text() + '<span class="caret"></span>');
        $(this).parents(".dropdown").find('.btn').val($(this).data('value'));
     });
}

let executeCondition = function(){
    $("#executeCondition").click(function(){
        project  = $("#project button").text()
        topology = $("#topology button").text()
        if (topology != 'Data Center Core'){
            displaySelectorToSelectModel()
        }
        else{
            $.ajax({
                type: 'get',
                dataType: 'json',
                url: window.location.origin + '/test/get/topoConfig/',
                data: {'project': project, 'topo': topology},
                success:function(data){
                    displayTopoConfig(data['data'])
                }
            })
        }
    })
}

let displaySelectorToSelectModel = function(){
    $.ajax({
        type: 'get',
        url: window.location.origin + '/test/get/topoModel/',
        success:function(data){
            data = data['data']
            html = '<div style="float: left;margin: 10px;">Model : ' +
                '<div class="dropdown" id="model" style="display:inline">' +
                    '<button aria-expanded="true" aria-haspopup="true" class="btn btn-default dropdown-toggle" data-toggle="dropdown" id="dropdownMenu1" style="min-width:150px;text-align:right" type="button">' + data[0] + '<span class="caret"></span></button>' +
                    '<ul aria-labelledby="dropdownMenu1" class="dropdown-menu" id="DUTList" style="min-width:150px;text-align:right">'
            data.forEach(element => {
                html += '<li><a>' + element + '</a></li>'
            })
            html += '</ul></div>' +
                    '<a class="btn btn-primary" id="getModelConfig" role="button" style="float:right; margin-left:15px;" type="button">Select</a></div>'
            $("#displayConfig").empty()
            $("#displayConfig").append(html)
            getModelConfig()
        }

    })
}

let getModelConfig = function(){
    $("#getModelConfig").click(function(){
        model = $("#model button").text()
        $.ajax({
            type: 'get',
            url: window.location.origin + '/test/get/modelConfig/',
            data:{model: model},
            success: function(data){
                data = data['model']
                html = '<div class="level col-md-12">' + 
                            '<div class="level_content"><img src="/static/images/products/forSupportList/' + data.toLowerCase() + '_overview.png" style="max-width: 200px;"> ' +
                                '<p>Model : ' + data + '</p>' +
                                '<p>Software Version: ' +
                                    '<select>' +
                                        '<option>2018-10</option>' +
                                        '<option>2019-04</option>' +
                                        '<option>2019-11</option>' +
                                    '</select>' + 
                                '</p>' +
                             '</div>' +
                        '</div>'
                $("#displayConfig").empty()
                $("#displayConfig").append(html)
            }
        })
    })
}

let displayTopoConfig = function(data){
    if (data['topo'] != 'Data Center Core'){
        html = ''
    }
    else{
        html = ''
        level_1 = data['level_1'].split(', ')
        level_2 = data['level_2'].split(', ')
        level_3 = data['level_3'].split(', ')
        level_4 = data['level_4'].split(', ')
        level_5 = data['level_5'].split(', ')
        level_list = [level_1, level_2, level_3, level_4, level_5]
        level_list.forEach(element => {
            if (element[0] != ""){
                html +='<div class="level col-md-12">'
                element.forEach(element =>{
                    model_number = element.toLowerCase()
                    html += '<div class="level_content"><img src="/static/images/products/forSupportList/' + model_number + '_overview.png" style="max-width: 200px;"> ' +
                                '<p>Model : ' + element + '</p>' +
                                '<p>Software Version: ' +
                                    '<select>' +
                                        '<option>2018-10</option>' +
                                        '<option>2019-04</option>' +
                                        '<option>2019-11</option>' +
                                    '</select>' + 
                                '</p>' +
                            '</div>'
                })
                html += '</div>'
            }
            
        });
    }
    $("#displayConfig").empty()
    $("#displayConfig").append(html)
}

function ValidateNumber(obj){
    // 清除"数字"和"."以外的字符
    obj.value = obj.value.replace(/[^\d.]/g,"");
    // 验证第一个字符是数字
    obj.value = obj.value.replace(/^\./g,"");
    // 只保留第一个, 清除多余的
    obj.value = obj.value.replace(/\.{2,}/g,".");
    obj.value = obj.value.replace(".","$#$").replace(/\./g,"").replace("$#$",".");
    // 只能输入两个小数
    obj.value = obj.value.replace(/^(\-)*(\d+)\.(\d\d).*$/,'$1$2.$3');
}


let initialLoadFunction = function(){
    changeDropdownValue();
    executeCondition();

}

addLoadEvent(initialLoadFunction);