function getlanguage() {
  var userLang = navigator.language || navigator.userLanguage; 
    //userLang = "ru";
    //alert ("Thlanguage is: " + userLang);
    if(userLang == "zh-TW" || userLang =="zh" || userLang =="ja"){
    window.open("https://www.edge-core.com/whereInfo.php?cls=1")
  }
  else if(userLang == "en-US" ||userLang == "fr" || userLang =="en"){
    window.open("https://www.edge-core.com/whereInfo.php?cls=2")
  }
  else if(userLang == "us"){
    window.open("https://www.edge-core.com/whereInfo.php?cls=3")
  }
  else if(userLang == "pt-BR" || userLang =="es-PE"){
    window.open("https://www.edge-core.com/whereInfo.php?cls=4")
  }
  else if(userLang == "ru" || userLang =="uk"){
    window.open("https://www.edge-core.com/whereInfo.php?cls=5")
  }
}
/*
$(".list-group-item").mouseover(function() {
  var title = "#"+$(this).attr("value");
  $(".sub-title").hide();
  $(title).show();
})

$(".sub-title").mouseover(function() {
  var title = "#"+$(this).attr("id");
  $(title).show();
  $(title).mouseleave(function() {
    $(title).hide();
  })
})*/