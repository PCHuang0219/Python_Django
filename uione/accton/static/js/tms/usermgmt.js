let getAccountList=function(){
    $.ajax({
        type: "get",
        url: window.location.origin + "/tmsadmin/AccountList/",
        data:{},
        dataType: "json",
        success: function(data, status){
            account_list = data["status"];
            getUserType(account_list);
        },
    })
}

let getUserType=function(account_list){
    $.ajax({
        type: "get",
        url: window.location.origin + "/tmsadmin/getUserTypeTable/",
        data:{},
        dataType: "json",
        success: function(data, status){
            user_type_list = data["data"];
            showAccount(account_list,user_type_list);
            showUserList(account_list);
        },
    })
}

let showAccount=function(account_list,user_type_list){
    var html = '<tr> \
                    <th>User Type</th> \
                    <th>User Name</th> \
                    <th>First_Name</th> \
                    <th>Email</th> \
                    <th>Last Login</th> \
                    <th>Joined Date</th> \
                </tr>';
    user_type_name = '' ;
    for (var i=0 ; i<account_list.length ; i++){
        for (var x=0 ; x<user_type_list.length ; x++){
            if ( user_type_list[x]["user_id"] == account_list[i]["id"] ){
                user_type = user_type_list[x]["user_type_id"];
                if ( user_type == "9"){ user_type_name = "TMS_Project Viewer"}
                if ( user_type == "8"){ user_type_name = "TMS_Project Mananger"}
                if ( user_type == "7"){ user_type_name = "TMS_Admin"}
                if ( user_type == "6"){ user_type_name = "Channel_Partners"}
                if ( user_type == "5"){ user_type_name = "Reseller"}
                if ( user_type == "4"){ user_type_name = "Lab_Master"}
                if ( user_type == "3"){ user_type_name = "Lab-Controller"}
                if ( user_type == "2"){ user_type_name = "Subscriber"}
                if ( user_type == "1"){ user_type_name = "General User"}
            }
        }
        if (user_type_name == ""){
            user_type_name = "General User";
        }
        html += '<tr> \
					<td data-th="User Type">'+user_type_name+'</td> \
                    <td data-th="User Name">'+account_list[i]["username"]+'</td> \
                    <td data-th="First_Name">'+account_list[i]["first_name"]+'</td> \
                    <td data-th="Email">'+account_list[i]["email"]+'</td> \
                    <td data-th="Last Login">'+account_list[i]["last_login"]+'</td> \
                    <td data-th="Joined Date">'+account_list[i]["date_joined"].substring(0,10)+'</td> \
                </tr>'
                user_type_name = '';
        
    }
    $("#account_content").empty();
    $("#account_content").append(html);
}

let showUserList=function(account_list){
    var html = '';
    for (var i=0 ; i<account_list.length ; i++){
        html += '<option value="'+account_list[i]["id"]+'">'+account_list[i]["username"]+'</option>';
    }
    $("#selectUserName").append(html);
    $("#showAllAccount").append(html);
    modifyUserType();
    deleteAccount();
}

let modifyUserType=function(){
    $("#changeUserType").click(function(){
        $.ajax({
            type: "post",
            url: window.location.origin + "/tmsadmin/updateUserPriority/",
            data:{user_id:$("#selectUserName").val(),user_type_id:$("#selectUserType").val(),},
            dataType: "json",
            success: function(data, status){
                window.location = window.location.origin + "/tmsadmin/usermgmt";
            },
        })
    })
}

let deleteAccount=function(){
    $("#deleteAccount").click(function(){
    var del_user_id = $("select[name='delete']").val();
        $.ajax({
            type: "post",
            url: window.location.origin + "/tmsadmin/deleteAccount/",
            data:{user_id:del_user_id},
            dataType: "json",
            success: function(data, status){
                window.location = window.location.origin + "/tmsadmin/usermgmt";
            },
        })
    })   
}
addLoadEvent(getAccountList);