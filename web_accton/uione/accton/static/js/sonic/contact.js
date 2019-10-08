let submit=function(){
    $("#submit").click(function(){
        const first_name = document.getElementById("first_name").value;
        const last_name =  document.getElementById("last_name").value;
        const companys =  document.getElementById("companys").value;
        const job_title =  document.getElementById("job_title").value;
        const country =  document.getElementById("country").value;
        const address =  document.getElementById("addresss").value;
        const email =  document.getElementById("email").value;
        const phone =  document.getElementById("tel2").value;
        const description = document.getElementById("description").value;
        var radios = document.getElementsByName("sex");
        for (var i=0 ; i<radios.length ; i++){
            if (radios[i].checked){
                var gender = radios[i].value;
            }
        }
        if (first_name == ''){alert("Please input your first_name");}
        else if (last_name == ''){alert("Please input your last_name");}
        else if (companys == ''){alert("Please input your companys");}
        else if (job_title == ''){alert("Please input your job_title");}
        else if (gender == ''){alert("Please input your gender");}
        else if (country == ''){alert("Please input your country");}
        else if (email == ''){alert("Please input your email");}
        else if (phone == ''){alert("Please input your telephone");}
        else if (description == ''){
            alert("Please input your description");
        };
    })
}

let clear=function(){
    $("#clear").click(function(){
        $("#first_name").val("");
        $("#last_name").val("");
        $("#companys").val("");
        $("#sex").val("");
        $("#job_title").val("");
        $("#country").val("");
        $("#addresss").val("");
        $("#email").val("");
        $("#tel2").val("");
        $("#description").val("");
    })
}

addLoadEvent(submit);
addLoadEvent(clear);