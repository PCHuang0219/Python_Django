let platform_list = []
const SELECT_VENDOR = 4 ;
const SELECT_ASIC = 3 ;
const SELECT_BAND = 2 ;
const SELECT_MODEL = 1 ;

let dropdown_button_click = function(){
    $("#vendor_choose li a").click(function(){
        $(this).parent().parent().prev().text($(this).text());
        $("#switch_asic_choose").children().text("Switch ASIC");
        $("#band_choose").children().text("Band Width");
        $("#model_choose").children().text("Switch SKU");
        $("#configuration_choose").children().text("Port Config");
        $(this).parent().parent().prev().append('<span class="caret"></span>');
        $(this).parent().parent().prev().val($(this).text());
        vendor_text = $("#vendor_choose > button").text(); 
        data_list = changeProductList(vendor_text);
        changeDropDownView(data_list,SELECT_VENDOR);
        changeProductView(data_list);
    });

    $("#switch_asic_choose li a").click(function(){
        $(this).parent().parent().prev().text($(this).text());
        $("#band_choose").children().text("Band Width");
        $("#model_choose").children().text("Switch SKU");
        $("#configuration_choose").children().text("Port Config");
        $(this).parent().parent().prev().append('<span class="caret"></span>');
        $(this).parent().parent().prev().val($(this).text());
        vendor_text = $("#vendor_choose > button").text(); 
        switch_asic_text = $("#switch_asic_choose > button").text();
        data_list = changeProductList(vendor_text,switch_asic_text);
        changeDropDownView(data_list,SELECT_ASIC);
        changeProductView(data_list);
    });

    $("#band_choose li a").click(function(){
        $(this).parent().parent().prev().text($(this).text());
        $("#model_choose").children().text("Switch SKU");
        $("#configuration_choose").children().text("Port Config");
        $(this).parent().parent().prev().append('<span class="caret"></span>');
        $(this).parent().parent().prev().val($(this).text());
        vendor_text = $("#vendor_choose > button").text(); 
        switch_asic_text = $("#switch_asic_choose > button").text(); 
        band_text = $("#band_choose > button").text();
        data_list = changeProductList(vendor_text,switch_asic_text,band_text);
        changeDropDownView(data_list,SELECT_BAND);
        changeProductView(data_list);
    });

    $("#model_choose li a").click(function(){
        $(this).parent().parent().prev().text($(this).text());
        $("#configuration_choose").children().text("Port Config");
        $(this).parent().parent().prev().append('<span class="caret"></span>');
        $(this).parent().parent().prev().val($(this).text());
        vendor_text = $("#vendor_choose > button").text(); 
        switch_asic_text = $("#switch_asic_choose > button").text(); 
        band_text = $("#band_choose > button").text();
        model_text = $('#model_choose > button').text();
        data_list = changeProductList(vendor_text,switch_asic_text,band_text,model_text);
        changeDropDownView(data_list,SELECT_MODEL);
        changeProductView(data_list);
    });

    $("#configuration_choose li a").click(function(){
        $(this).parent().parent().prev().text($(this).text());
        $(this).parent().parent().prev().append('<span class="caret"></span>');
        $(this).parent().parent().prev().val($(this).text());
        vendor_text = $("#vendor_choose > button").text(); 
        switch_asic_text = $("#switch_asic_choose > button").text(); 
        band_text = $("#band_choose > button").text();
        model_text = $("#model_choose > button").text();
        port_text = $("#configuration_choose > button").text();
        data_list = changeProductList(vendor_text,switch_asic_text,band_text,model_text,port_text);
        changeDropDownView(data_list,SELECT_VENDOR);
        changeProductView(data_list);
    });
}
let changeProductList = function(vendor_text="Select All",switch_asic_text="Select All",band_text="Select All",model_text="Select All",port_text="Select All"){
    let data_list = [] ;
    if (vendor_text=="ASIC Vendor"){vendor_text="Select All";}
    if (switch_asic_text=="Switch ASIC"){switch_asic_text="Select All";}
    if (band_text=="Band Width"){band_text="Select All";}
    if (model_text=="Switch SKU"){model_text="Select All";}
    if (port_text=="Port Config"){port_text="Select All";}
    for (let i=0;i < platform_list.length;i++){
        if ( (platform_list[i]["ASIC_Vendor"] == vendor_text || vendor_text == "Select All") &&
             (platform_list[i]["Switch_ASIC"] == switch_asic_text || switch_asic_text == "Select All") &&
             (platform_list[i]["Bandwith"] == band_text || band_text == "Select All") &&
             (platform_list[i]["Switch_SKU"] == model_text || model_text == "Select All") &&
             (platform_list[i]["Port_Configuration"] == port_text || port_text == "Select All")){
                data_list.push(platform_list[i]);
            }
        }            
    return data_list;
}

let getPlatformList = function(){
    $.ajax({
        type: "get",
        url: window.location.origin + "/sonic/data/platformList/",
        data:{},
        dataType: "json",
        success: function(data, status){
            data = data["platformList"]
            platform_list = data
            changeDropDownView(platform_list,SELECT_VENDOR);
            dropdown_button_click();
        },
    })
}

let changeProductView = function(data_list){
    $("#switch_info").empty();
    let html = '';
    for(let i = 0; i < data_list.length; i++){
        html += 
        '<div class="col-xs-6 col-sm-3 devices"> \
        <a href="'+window.location.origin+'/sonic/products/'+data_list[i]["Bandwith"]+'/'+data_list[i]["Switch_SKU"]+'"> \
        <div class="thumbnail"> \
        <img src="../../../static/'+data_list[i]["image"]+'"> \
        <div class="caption"> \
            <h4>'+data_list[i]["Switch_Vendor"]+'</h4> \
                <p>'+data_list[i]["Bandwith"]+'</p> \
                <p>'+data_list[i]["Switch_SKU"]+'</p> \
                <p>'+data_list[i]["ASIC_Vendor"]+'</p> \
                <p>'+data_list[i]["Switch_ASIC"]+'</p> \
                <p>'+data_list[i]["Port_Configuration"]+'</p> \
            </div> \
        </div> \
        </a> \
        </div>';
    }
    $("#switch_info").append(html);
    dropdown_button_click();
}


let changeDropDownView = function(data_list,CHANGE_ITEM){
    if (CHANGE_ITEM > 0 ){
        $("#configuration_choose ul").empty();
        unique = [...new Set(data_list.map(item => item.Port_Configuration))];
        for(let i = 0; i < unique.length; i++){
            $("#configuration_choose ul").append('<li><a>'+unique[i]+'</a></li>')
        }}
    if (CHANGE_ITEM > 1 ){
        $("#model_choose ul").empty();
        unique = [...new Set(data_list.map(item => item.Switch_SKU))];
        for(let i = 0; i < unique.length; i++){
            $("#model_choose ul").append('<li><a>'+unique[i]+'</a></li>')
        }
        $("#model_choose ul").append('<li><a>Select All</a></li>')}
    if (CHANGE_ITEM > 2 ){
        $("#band_choose ul").empty();
        unique = [...new Set(data_list.map(item => item.Bandwith))];
        for(let i = 0; i < unique.length; i++){
            $("#band_choose ul").append('<li><a>'+unique[i]+'</a></li>')
        }
        $("#band_choose ul").append('<li><a>Select All</a></li>')}
    if (CHANGE_ITEM > 3 ){
        $("#switch_asic_choose ul").empty();
        unique = [...new Set(data_list.map(item => item.Switch_ASIC))];
        for(let i = 0; i < unique.length; i++){
            $("#switch_asic_choose ul").append('<li><a>'+unique[i]+'</a></li>')
        }
        $("#switch_asic_choose ul").append('<li><a>Select All</a></li>')}   
    $("#vendor_choose ul").empty();
    unique = [...new Set(data_list.map(item => item.ASIC_Vendor))];
    for(let i = 0; i < unique.length; i++){
        $("#vendor_choose ul").append('<li><a>'+unique[i]+'</a></li>')
    }
}
addLoadEvent(getPlatformList);
addLoadEvent(dropdown_button_click);