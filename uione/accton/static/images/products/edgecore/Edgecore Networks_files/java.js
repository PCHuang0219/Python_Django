


//AJAX動作
function useAjax(ACT , needVal){
	
	$.ajax({
		type: 'POST',
		url: 'ajax.php',
		data: {Func:ACT,Val:encodeURI(needVal)},
		dataType:'json',
		beforeSend:function(){

			if(ACT == 'requestForm' || ACT == 'contact'){
				setLoadPlayer( '' , '' , '');
			}
		},
		success:function(json){
			

			//回傳判斷
			switch(ACT)
			{
                case 'setCookie':

                    break;
				case 'getModel':
					if(json.re == '1'){
						$('#title4_'+json.no).val(json.model);
						$('#buy_date_'+json.no).val(json.date);
					}
				break;
					
				case 'getModel2':
					if(json.re == '1'){
						$('#title4_'+json.no).html(json.html);
						
						if(json.num > 0){
							$('#no_'+json.no).parent().find("span").hide(); 
						}else{
							$('#no_'+json.no).parent().find("span").show(); 
						}
					}
				break;	
					
				case 'getExpiryDate':
					if(json.re == '1'){
						//alert(json.no);
						$('#expiry_date_'+json.no).val(json.date);
						//$('#expiry_date_1').value('aa');
						//$('#buy_date_'+json.no).val(json.date);
					}
				break;
					
					
				case 'chkNo':
					
					return json.re;
					
					if(json.re = '1'){
		   				return "* This serial number has been registered"
					}
				break;
				
				case 'delRepair':
					if(json.re == '1'){
						window.location.reload();
					}
				break;
				
				
				case 'getInvestor':
					$('.partners-title').html(json.title);
					$('.info').html(json.desc);
					$('#path_title').html(json.title);
				break;
				
				case "chkLogin":

					if(json.re == '1'){
						//window.location.href='member.php';
						window.location.reload();
					}else if(json.re == '2'){
						alert('帳號密碼錯誤!');
						$('#loginBtn').attr('disabled',false);
						$('#passwd').val('');
						$('#VerificationCode2').val('');
						$('#rand-img').click();
					}else{
						alert('Verification code error!');
						$('#loginBtn').attr('disabled',false);
						$('#passwd').val('');
						$('#VerificationCode2').val('');
						$('#rand-img').click();
					}
					
					//return false;


					break;
				
				case 'getProList':
					//$('input[name=product_class]').val().indexOf($(this).val()) == -1
					console.log(json.sql);
					if(json.num7 == 0){
						alert('No Data!!'); return false;
					}else{
						$('.proList').html(json.re);
						
						
						$('#num').html(json.num+' product(s) found.');
						$("#compareOpen").slideDown("slow");
						
						var valuelist = ''; 
						
						$('input[name=comparison]').change(function() {
							if (this.checked) {
								valuelist += $(this).val() + ',';
							}else{
								valuelist = valuelist.replace($(this).val()+',','');
							}
							
							
							if($('input[name=comparison]:checked').length >4){
								alert('Only choose a maximum of four!!');
								
								$('#inquiryBtn').attr('disabled',true);
								
								/*$('#inquiryBtn').click(function(){
									alert('Only choose a maximum of four!!');
								})*/
								
								
								
							}else{
								$('#inquiryBtn').attr('disabled',false);
								
								$('#inquiryBtn').click(function(){
									useAjax('compare',valuelist);
								})
								
							}
						});
					}
					
				break;
				
				case 'getProList2':
					//alert(json.re);
					$('#Condition').html(json.re);
					//console.log(json.sql);
				break;
				
				case 'compare':
					//alert(json.re);
					window.location.href='products-inquiry.php';
				break;
				
				case 'addCompare':
					//alert(json.re);
					
					$('.selectWord').html('You have selected '+json.num+' products');
					
				break;
				
				case 'delComparison':
					//alert(json.re);
					//window.location.href='products-inquiry.php';
					//$('#proList').html(json.re);
					useAjax('getComparison','en');
				break;
				
				case 'getComparison':
					//alert(json.re);
					//window.location.href='products-inquiry.php';
					$('#proList').html(json.re);
				break;
				
				case 'getProduct':
					//alert(json.re);
					//console.log(json.sql);
					$('#up_cls').html(json.re);
					$('#up_cls').show(1000);
					if(json.id > 0){
						useAjax('getDownloadList',json.id );
						$('#up_cls > option:nth-child(2)').attr('selected','selected');
					}else{
						$('#result').hide(1000);	
					}
				break;
				
				case 'getDownloadList':
					$('#result > div.container.md > div > table > tbody').html(json.re);
					$('#p_url').attr('href',json.url);
					$('#p_url').html(json.title);
					$('#p_url2').attr('href',json.url);
					
					$('#p_pic').html('<img src="_upload/images/'+json.pic+'" alt="">');
					
					$('#result').show(1000);
				break;
				
				case 'contact':
					if(json.re == '1'){
						alert("send success!!");
						window.location.href="contactInquiry.php";
					}else{
						alert('Verification code error!!');
						$('#VerificationCode').val('');
						$('#rand-img').click();
					}
				break;
				
				case 'requestForm':
					if(json.re == '1'){
						alert("send success!!");
						window.location.href="supRequest.php";
					}else{
						alert('Verification code error!!');
						$('#VerificationCode').val('');
						$('#rand-img').click();
					}
				break;
				
				case 'logOut':
					window.location.href='index.php';
				break;
				
				case 'resourcesDW':
					$('#qty_'+json.id).html(json.re);
				break;
				
				case 'forgetPW':
					if(json.re == '1'){
						//$('#forgetBtn').click();
						window.location.href='member-forgoted.php';
					}else{
						//alert(json.msg);
						$('#msg').html(json.msg);
						$('#VerificationCode').val('');
						$('#rand-img').click();
					}
					
				break;
				
				case 'report':
					if(json.re == '1'){
						window.location.href='partners-message-reported.php?cls='+json.cls+'&id='+json.id;
					}
				break;

			}

			//setLoadPlayer( 'none' , '' , '');
			if(ACT == 'requestForm' || ACT == 'contact'){
				$.unblockUI();
			}

		},
		complete:function(){ //生成分頁條

		},
		error:function(){
			//alert("讀取錯誤!");
		}
	});
}


//調整讀取條位置
function setLoadPlayer( view , left , top)
{


	if(view == 'none')
	{
		$.unblockUI();
	}
	else
	{
		$.blockUI({ css: {
			border: 'none',
			padding: '15px',
			backgroundColor: '#000',
			'-webkit-border-radius': '10px',
			'-moz-border-radius': '10px',
			opacity: .5,
			color: '#fff'
		} });

	}

}

function useAjax2(ACT , Forms){
	var fd = new FormData(document.getElementById(Forms));
	fd.append( 'Func', ACT );
	
	
	$.ajax({
		type: "POST",
		//url: "ajax2.php",
		url: "ajax2.php",
		//data:fd,
		processData: false,
		contentType: false,
		data:fd,
		enctype: 'multipart/form-data',
		dataType:'json',
		
		success: function(json){
			//alert( "Data Saved: " + json.re );
			switch(ACT){
				
				case 'addRMA':
					if(json.re == '1'){
						window.location.href='partners-RMA-registered.php';
					}
				break;
					
				case 'addRMA2':
					if(json.re == '1'){
						window.location.href='partners-RMA-RS-applyout.php';
					}
				break;	
					
				case 'select_repair':
					if(json.re == '1'){
						window.location.href='partners-RMA-RS-applyout.php';
					}
				break;
					
				case 'addREPAIR':
					if(json.re == '1'){
						window.location.href='partners-RMA-RS-applyed.php';
					}
				break;
					
					
				case 'chkLogin':
						if(json.re == 'errCode'){
							//alert('Verification code error!!');
							$('#msg').html('Verification code error!!');
							$('#passwd').val('');
							$('#VerificationCode').val('');
							$('#reload-img').click();
						}else if(json.re == '0'){
							//alert('Check your account and password!!');
							$('#msg').html('Check your account and password!!');
							$('#VerificationCode').val('');
							$('#passwd').val('');
							$('#reload-img').click();
						}else{
							window.location.href='partners-centers.php';
						}
				break;
				
				case 'memberAdd':
					if(json.re == 'errCode'){
						$('#msg').html('Verification code error!!');
						$('#rand-img').click();
						$('#VerificationCode').val('');
					}else{	
						window.location.href='member-registered.php';
					}
				break;
				
				case 'memberEdit':
					$('#msg').html('Modify success!!');
					//window.location.href='partners-profile.php';
				break;
				
				case 'changPW':
					if(json.re == '0'){
						$('#msg').html('Current password error!!');
					}else{
						$('#msg').html('Modify success!!');
					}
				break;
				
				case 'coopAdd':
					window.location.href='partners-project-registrationed.php';
				break;
				
				case 'appAdd':
					window.location.href='partners-coop-registrationed.php';
				break;
				
				case 'appEdit':
					window.location.href='partners-coop-uploaded.php';
				break;
				
				case 'mes':
					if(json.re == '1'){
						window.location.href='partners-message-mesed.php?cls='+json.cls;
					}
				break;
				
				
					
			}
		}
	});

}


