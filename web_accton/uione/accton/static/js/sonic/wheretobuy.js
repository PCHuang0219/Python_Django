let changeArea = function (){
    $("#chooseArea li").click(function(){
        var value = $(this).attr("value");
        $("#chooseArea li").attr("class","");
        $(this).attr("class","active");
        showContent(value);
    })
}

let showContent = function(value){
    area = "#"+value;
    $("#asia").attr("style","display:none;");
    $("#emea").attr("style","display:none;");
    $("#n-america").attr("style","display:none;");
    $("#l-america").attr("style","display:none;");
    $("#rc").attr("style","display:none;");
    $(area).attr("style","display:block;");
}

let getClientAreaFromIP = function(){
  $.ajax({
    url: 'http://ip-api.com/json/'+returnCitySN["cip"],
    type: 'POST',
    dataType: 'json',
    success:function(data) {
      area = data.timezone.split("/")[0]
      if ( area != ''){
        if (area == "Asia"){
          selection = "#asia"
          select_content = "#area1"
        }
        else if (area == "America"){
          selection = "#n-america"
          select_content = "#area3"
        }
        else if (area == "Europe"){
          selection = "#emea"
          select_content = "#area2"
        }
        else if (area == "Africa"){
          selection = "#emea"
          select_content = "#area2"
        }
        else if (area == "Australia"){
          selection = "#rc"
          select_content = "#area5"
        }
        else{
          selection = "#n-america"
          select_content = "#area3"
        }
        showInitContent(selection,select_content)
      }
      else{
        getClientAreaFromBrowser();
      }
    }
  });
}

let getClientAreaFromBrowser = function(){
  if(userLang == "zh-TW" || userLang =="zh" || userLang =="ja"){
    selection="#asia"
    select_content="#area1";
  }
  else if(userLang == "en-US" ||userLang == "fr" || userLang =="en" || userLang =="en-GB"){
    selection="#emea"
    select_content="#area2";
  }
  else if(userLang == "us"){
    selection="#n-america"
    select_content="#area3";
  }
  else if(userLang == "pt-BR" || userLang =="es-PE"){
    selection="#l-america"
    select_content="#area4";
  }
  else if(userLang == "ru" || userLang =="uk"){
    selection="#rc"
    select_content="#area5";
  }
  else{
    selection = "#n-america"
    select_content = "#area3"
  }
  showInitContent(selection,select_content)
}

let showInitContent = function(area,area_content){
    $(area).attr("style","display:block;");
    $("#chooseArea li").attr("class","");
    $(area_content).attr("class","active");
}

let getPartnersData = function(){
  $.ajax({
    type: "get",
    url: "http://" + Config.ip_address + Config.port + "/sonic/get/partnersData/",
    data:{},
    dataType: "json",
    success: function(data, status){
      data_list = data["data"]
      distributor_html = ''
      reseller_html = ''
      pre_sort = ''
      for (var i=0 ; i <data_list.length ; i++){
        data = data_list[i]
        sort = data["sort"]
        type = data["type"]
        if ( pre_sort != sort ){
          append_html_to_web(pre_sort,distributor_html,reseller_html)
          pre_sort = sort;
          distributor_html = '';
          reseller_html = '' ;
        }
        if (pre_sort == sort){
          if (type == 'distributor'){
            distributor_html = writer_html(distributor_html,data)
          }
          else{
            reseller_html = writer_html(reseller_html,data)
          }
        }
      }
      append_html_to_web(pre_sort,distributor_html,reseller_html);
    },
  })
}

let append_html_to_web = function(sort,distributor_html,reseller_html){
  if ( sort == ''){
    return
  }
  else if (sort == "ASIA PACIFIC"){
      selection = "#asia"
  } 
  else if (sort == "EMEA"){
    selection = "#emea"
  }
  else if (sort == "NORTH AMERICA"){
    selection = "#n-america"
  }
  else if (sort == "LATIN AMERICA"){
    selection = "#l-america"
  }
  else if (sort == "RUSSIA AND CIS"){
    selection = "#rc"
  }
  distributor_selection = $(selection).children(".distributor").children(".distributor_data")
  reseller_selection = $(selection).children(".SI").children(".reseller_data")
  distributor_selection.empty()
  distributor_selection.append(distributor_html)
  reseller_selection.empty()
  reseller_selection.append(reseller_html)
}

let writer_html = function(html,data){
  if ( data["img_path"] != 'images/partners/no_pic'){
    html += '<div class="card col-md-3 col-sm-4 col-xs-12"> \
            <div class="panel panel-primary"> \
              <div class="panel-heading"> \
                ' + data["country"] + ' \
              </div> \
              <div class="panel-body"> \
                <div class="partner_img"> \
                  <img src="/static/' + data["img_path"] + '" style="height:100%;"> \
                </div> \
                ' + data["company"] + '<br> \
                ' + data["address"] + '<br> \
                ' + data["telephone"] + '<br> \
                ' + data["fax"] + '<br> \
                <a href="'+ data["company_link"] + '">' + data["company_link"] + '</a><br> \
              </div> \
            </div> \
          </div>'
  }
  else{
    html += '<div class="card col-md-3 col-sm-4 col-xs-12"> \
            <div class="panel panel-primary"> \
              <div class="panel-heading"> \
                ' + data["country"] + ' \
              </div> \
              <div class="panel-body"> \
                <div class="partner_img"> \
                </div> \
                ' + data["company"] + '<br> \
                ' + data["address"] + '<br> \
                ' + data["telephone"] + '<br> \
                ' + data["fax"] + '<br> \
                <a href="'+ data["company_link"] + '">' + data["company_link"] + '</a><br> \
              </div> \
            </div> \
          </div>'
  }
  
  return html
}

let InitLoadFunction = function(){
  changeArea();
  showInitContent();
  getPartnersData();
  getClientAreaFromIP();
}

addLoadEvent(InitLoadFunction);