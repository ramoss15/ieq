var request,request_hovercard,searchbarselected;$(document).ready(function(){$('.tipsy1').tipsy({gravity:'nw',fade:true,live:true});$("#fullscreendarktabclose").click(function(){$("#fullscreendark").hide();});$("#fullscreenlighttabclose").click(function(){$("#fullscreenlight").hide();});$("#topbarinnerrighttopbox5").hover(function(){$("#topbarinnerdropdownrides").stop().show();var right5=$("#topbarinnerrighttopbox1").width()+$("#topbarinnerrighttopbox4").width()-($("#topbarinnerrighttopbox5").width()/4);$("#topbarinnerdropdownrides").css('right',right5);},function(){$("#topbarinnerdropdownrides").stop().hide();});$("#topbarinnerdropdownrides").hover(function(){$("#topbarinnerrighttopbox5").addClass("hovered1");$("#topbarinnerdropdownrides").stop().show();},function(){$("#topbarinnerrighttopbox5").removeClass("hovered1");$("#topbarinnerdropdownrides").stop().hide();});$("#topbarinnerrighttopbox4").hover(function(){$("#topbarinnerdropdownpools").stop().show();var right5=$("#topbarinnerrighttopbox1").width()-($("#topbarinnerrighttopbox4").width()/4);$("#topbarinnerdropdownpools").css('right',right5);},function(){$("#topbarinnerdropdownpools").stop().hide();});$("#topbarinnerdropdownpools").hover(function(){$("#topbarinnerrighttopbox4").addClass("hovered1");$("#topbarinnerdropdownpools").stop().show();},function(){$("#topbarinnerrighttopbox4").removeClass("hovered1");$("#topbarinnerdropdownpools").stop().hide();});$("#topbarinnerrighttopbox3").hover(function(){$("#topbarinnerdropdownnotices").stop().show();var right5=$("#topbarinnerrighttopbox2").width()+$("#topbarinnerrighttopbox5").width()+$("#topbarinnerrighttopbox1").width()+$("#topbarinnerrighttopbox4").width()-($("#topbarinnerdropdownnotices").width()-$("#topbarinnerrighttopbox3").width())/2;$("#topbarinnerdropdownnotices").css('right',right5);},function(){$("#topbarinnerdropdownnotices").stop().hide();});$("#topbarinnerdropdownnotices").hover(function(){$("#topbarinnerrighttopbox3").addClass("hovered1");$("#topbarinnerdropdownnotices").stop().show();},function(){$("#topbarinnerrighttopbox3").removeClass("hovered1");$("#topbarinnerdropdownnotices").stop().hide();});$("#topbarinnerrighttopbox2").hover(function(){$("#topbarinnerdropdownmessages").stop().show();var right5=$("#topbarinnerrighttopbox5").width()+$("#topbarinnerrighttopbox1").width()+$("#topbarinnerrighttopbox4").width()-($("#topbarinnerdropdownmessages").width()-$("#topbarinnerrighttopbox2").width())/2;$("#topbarinnerdropdownmessages").css('right',right5);},function(){$("#topbarinnerdropdownmessages").stop().hide();});$("#topbarinnerdropdownmessages").hover(function(){$("#topbarinnerrighttopbox2").addClass("hovered1");$("#topbarinnerdropdownmessages").stop().show();},function(){$("#topbarinnerrighttopbox2").removeClass("hovered1");$("#topbarinnerdropdownmessages").stop().hide();});$("#topbarinnerrighttopbox1").hover(function(){$("#topbarinnerdropdownuser").stop().show();},function(){$("#topbarinnerdropdownuser").stop().hide();});$("#topbarinnerdropdownuser").hover(function(){$("#topbarinnerrighttopbox1").addClass("hovered1");$("#topbarinnerdropdownuser").stop().show();},function(){$("#topbarinnerrighttopbox1").removeClass("hovered1");$("#topbarinnerdropdownuser").stop().hide();});$("#topbarinnerrighttopbox7").hover(function(e){if($("#searchbigbardropdown").css('display')=='none'){$("#topbarsearchimglight").stop().hide();$("#topbarsearchimgbright").stop().show();}},function(){if($("#searchbigbardropdown").css('display')=='none'){$("#topbarsearchimgbright").stop().hide();$("#topbarsearchimglight").stop().show();}});$("#topbarinnerrighttopbox7").click(function(e){$(this).addClass("topbarinnerrighttopbox7clicked");$("#topbarinnerrighttopbox891011").stop().show();$("#topbarsearchimglight").stop().hide();$("#topbarsearchimgbright").stop().show();e.stopPropagation();});$(document).click(function(){$("#topbarinnerrighttopbox891011").stop().hide();$("#topbarinnerrighttopbox7").removeClass("topbarinnerrighttopbox7clicked");$("#topbarsearchimgbright").stop().hide();$("#topbarsearchimglight").stop().show();});$('#topbarinnerrighttopbox891011').click(function(event){if($("#topbarinnerrighttopbox891011").css('display')!='none'){event.stopPropagation();}});$("#topbarinnerrighttopbox891011").click(function(event){if($("#topbarinnerrighttopbox891011").css('display')!='none'){event.stopPropagation();}});$('#topbar').click(function(event){});
$(".hovercarduserlink").live('mouseover',function(){that=$(this);$(".hovercarduserbottomright").html('');if(((that.offset().top+that.height()+$(".hovercarduser").height())<$(document).height())&&(that.offset().left+that.width()+$(".hovercarduser").width())<$(document).width())
{$(".hovercarduser").css('top',that.offset().top+that.height()-5).css('left',that.offset().left+5).stop().show();}
if(((that.offset().top+that.height()+$(".hovercarduser").height())>=$(document).height())&&(that.offset().left+that.width()+$(".hovercarduser").width())>=$(document).width())
{$(".hovercarduser").css('top',that.offset().top-$(".hovercarduser").height()+5).css('left',that.offset().left+10).stop().show();}
if(((that.offset().top+that.height()+$(".hovercarduser").height())>=$(document).height())&&(that.offset().left+that.width()+$(".hovercarduser").width())<$(document).width())
{$(".hovercarduser").css('top',that.offset().top-$(".hovercarduser").height()+5).css('left',that.offset().left-10).stop().show();}
if(((that.offset().top+that.height()+$(".hovercarduser").height())<$(document).height())&&(that.offset().left+that.width()+$(".hovercarduser").width())>=$(document).width())
{$(".hovercarduser").css('top',that.offset().top+that.height()-5).css('left',that.offset().left+5).stop().show();}
if(request_hovercard){request_hovercard.abort();}
request_hovercard=$.post("https://winwinride.com/ajax/hovercard/user",{id:that.attr('data-id')},function(data){$(".hovercarduserbottomright").html('').append(data);});});$(".hovercarduserlink").live('mouseout',function(){that=$(this);$(".hovercarduser").stop().hide();});$(".hovercarduser").live('mouseover',function(){that=$(this);that.stop().show();});$(".hovercarduser").live('mouseout',function(){that=$(this);that.stop().hide();});$(".hovercardplacelink").live('mouseover',function(){that=$(this);$(".hovercarduserbottomright").html('');if(((that.offset().top+that.height()+$(".hovercardplace").height())<$(document).height())&&(that.offset().left+that.width()+$(".hovercardplace").width())<$(document).width())
{$(".hovercardplace").css('top',that.offset().top+that.height()-5).css('left',that.offset().left+5).stop().show();}
if(((that.offset().top+that.height()+$(".hovercardplace").height())>=$(document).height())&&(that.offset().left+that.width()+$(".hovercardplace").width())>=$(document).width())
{$(".hovercardplace").css('top',that.offset().top-$(".hovercardplace").height()+5).css('left',that.offset().left+10).stop().show();}
if(((that.offset().top+that.height()+$(".hovercardplace").height())>=$(document).height())&&(that.offset().left+that.width()+$(".hovercardplace").width())<$(document).width())
{$(".hovercardplace").css('top',that.offset().top-$(".hovercardplace").height()+5).css('left',that.offset().left-10).stop().show();}
if(((that.offset().top+that.height()+$(".hovercardplace").height())<$(document).height())&&(that.offset().left+that.width()+$(".hovercardplace").width())>=$(document).width())
{$(".hovercardplace").css('top',that.offset().top+that.height()-5).css('left',that.offset().left+5).stop().show();}
if(request_hovercard){request_hovercard.abort();}
request_hovercard=$.post("https://winwinride.com/ajax/hovercard/place",{id:that.attr('data-id')},function(data){$(".hovercardplacebottomright").html('').append(data);});});$(".hovercardplacelink").live('mouseout',function(){that=$(this);$(".hovercardplace").stop().hide();});$(".hovercardplace").live('mouseover',function(){that=$(this);that.stop().show();});$(".hovercardplace").live('mouseout',function(){that=$(this);that.stop().hide();});$(".suggestionclose").live('click',function(){var that=$(this);var that1;var id1,id2;var counter=0;that.parents().eq(9).each(function(){that1=$(this);if(counter==0){id1=that1.attr('data-id');}
else{id2=that1.attr('data-id');}
counter=counter+1;});request=$.post("https://winwinride.com/ajax/network/suggestion/delete",{id:that.attr('data-id'),id1:id1,id2:id2},function(data){if(data){that.parents().eq(9).append(data);}});});$(".connectbtn.subbtnblue").live('mouseover',function(){if($(this).attr("value")=="Connected"){$(this).stop().removeClass("subbtnblue").addClass("subbtnred").prop('value','Remove');}});$(".connectbtn.subbtnred").live('mouseout',function(){if($(this).attr("value")=="Remove"){$(this).removeClass("subbtnred").addClass("subbtnblue").prop('value','Connected');}});$(".connectbtn").live('click',function(){var that=$(this);if($(this).attr("value")=="Connect"){request=$.post("https://winwinride.com/ajax/network/connect",{username:$(this).attr('data-connect')},function(data){if(data.result=="success"){that.removeClass("subbtngreen").addClass("subbtnblue").prop('value','Connected');}});}
if(($(this).attr("value")=="Remove")||($(this).attr("value")=="Connected")){request=$.post("https://winwinride.com/ajax/network/remove",{username:$(this).attr('data-connect')},function(data){if(data.result=="success"){that.removeClass("subbtnred").addClass("subbtngreen").prop('value','Connect');}});}});$(".connectbtntag.subbtnblue").live('mouseover',function(){if($(this).attr("value")=="Connected"){$(this).stop().removeClass("subbtnblue").addClass("subbtnred").prop('value','Remove');}});$(".connectbtntag.subbtnred").live('mouseout',function(){if($(this).attr("value")=="Remove"){$(this).removeClass("subbtnred").addClass("subbtnblue").prop('value','Connected');}});$(".connectbtntag").live('click',function(){var that=$(this);if($(this).attr("value")=="Connect"){request=$.post("https://winwinride.com/ajax/network/connect",{username:$(this).attr('data-connect')},function(data){if(data.result=="success"){that.removeClass("subbtngreen").addClass("subbtnblue").prop('value','Connected');}});}
if(($(this).attr("value")=="Remove")||($(this).attr("value")=="Connected")){request=$.post("https://winwinride.com/ajax/network/remove",{username:$(this).attr('data-connect')},function(data){if(data.result=="success"){that.removeClass("subbtnred").addClass("subbtngreen").prop('value','Connect');}});}});$(".fullscreenpopupcloseimg").live('click',function(){$("#fullscreenpopupcontentmain").html('');$("#fullscreenpopup").stop().hide();});$(".checkinpost").live('click',function(){
$(this).val('WORKING');var popup=$("#fullscreenpopupcontentmain");$("#fullscreenpopup").show();var request1=$.post('https://winwinride.com/ajax/checkin',{id:'checkin'},function(data){popup.html('').append(data);popup.css('left',(($(window).width()-popup.width())/2));popup.css('top',((($(window).height()-60)-popup.height())/2));});});$(".ridepost").live('click',function(){$(this).parents().eq(2).stop().hide();
var popup=$("#fullscreenpopupcontentmain");$("#fullscreenpopup").show();var request1=$.post('https://winwinride.com/ajax/ride',{id:'post_ride'},function(data){popup.html('').append(data);popup.css('left',(($(window).width()-popup.width())/2));popup.css('top',((($(window).height()-60)-popup.height())/2));});});$(".rideofferpost").live('click',function(){$(this).parents().eq(2).stop().hide();
var popup=$("#fullscreenpopupcontentmain");$("#fullscreenpopup").show();var request1=$.post('https://winwinride.com/ajax/ride',{id:'offer'},function(data){popup.html('').append(data);popup.css('left',(($(window).width()-popup.width())/2));popup.css('top',((($(window).height()-60)-popup.height())/2));});});$(".rideofferpost1").live('click',function(){
var popup=$("#fullscreenpopupcontentmain");$("#fullscreenpopup").show();var request1=$.post('https://winwinride.com/ajax/ride',{id:'offer'},function(data){popup.html('').append(data);popup.css('left',(($(window).width()-popup.width())/2));popup.css('top',((($(window).height()-60)-popup.height())/2));});});$(".ridequerypost").live('click',function(){$(this).parents().eq(2).stop().hide();
var popup=$("#fullscreenpopupcontentmain");$("#fullscreenpopup").show();var request1=$.post('https://winwinride.com/ajax/ride',{id:'query'},function(data){popup.html('').append(data);popup.css('left',(($(window).width()-popup.width())/2));popup.css('top',((($(window).height()-60)-popup.height())/2));});});$(".ridequerypost1").live('click',function(){
var popup=$("#fullscreenpopupcontentmain");$("#fullscreenpopup").show();var request1=$.post('https://winwinride.com/ajax/ride',{id:'query'},function(data){popup.html('').append(data);popup.css('left',(($(window).width()-popup.width())/2));popup.css('top',((($(window).height()-60)-popup.height())/2));});});$(".rideofferresponse1").live('click',function(){
var popup=$("#fullscreenpopupcontentmain");$("#fullscreenpopup").show();var request1=$.post('https://winwinride.com/ajax/ride',{object_id:$(this).attr('data-rideoffer-id'),id:'offerresponse'},function(data){popup.html('').append(data);popup.css('left',(($(window).width()-popup.width())/2));popup.css('top',((($(window).height()-60)-popup.height())/2));});});$(".ridequeryresponse1").live('click',function(){
var popup=$("#fullscreenpopupcontentmain");$("#fullscreenpopup").show();var request1=$.post('https://winwinride.com/ajax/ride',{object_id:$(this).attr('data-ridequery-id'),id:'queryresponse'},function(data){popup.html('').append(data);popup.css('left',(($(window).width()-popup.width())/2));popup.css('top',((($(window).height()-60)-popup.height())/2));});});$(".rideofferschedule1").live('click',function(){
var popup=$("#fullscreenpopupcontentmain");$("#fullscreenpopup").show();var request1=$.post('https://winwinride.com/ajax/ride',{object_id:$(this).attr('data-rideoffer-id'),id:'offerschedule'},function(data){popup.html('').append(data);popup.css('left',(($(window).width()-popup.width())/2));popup.css('top',((($(window).height()-60)-popup.height())/2));});});$(".ridequeryschedule1").live('click',function(){
var popup=$("#fullscreenpopupcontentmain");$("#fullscreenpopup").show();var request1=$.post('https://winwinride.com/ajax/ride',{object_id:$(this).attr('data-ridequery-id'),id:'queryschedule'},function(data){popup.html('').append(data);popup.css('left',(($(window).width()-popup.width())/2));popup.css('top',((($(window).height()-60)-popup.height())/2));});});$(".poolpost").live('click',function(){$(this).parents().eq(2).stop().hide();
var popup=$("#fullscreenpopupcontentmain");$("#fullscreenpopup").show();var request1=$.post('https://winwinride.com/ajax/pool',{id:'post_pool'},function(data){popup.html('').append(data);popup.css('left',(($(window).width()-popup.width())/2));popup.css('top',((($(window).height()-60)-popup.height())/2));});});$(".poolcreatepost").live('click',function(){$(this).parents().eq(2).stop().hide();
var popup=$("#fullscreenpopupcontentmain");$("#fullscreenpopup").show();var request1=$.post('https://winwinride.com/ajax/pool',{id:'create'},function(data){popup.html('').append(data);popup.css('left',(($(window).width()-popup.width())/2));popup.css('top',((($(window).height()-60)-popup.height())/2));});});$(".poolcreatepost1").live('click',function(){
var popup=$("#fullscreenpopupcontentmain");$("#fullscreenpopup").show();var request1=$.post('https://winwinride.com/ajax/pool',{id:'create'},function(data){popup.html('').append(data);popup.css('left',(($(window).width()-popup.width())/2));popup.css('top',((($(window).height()-60)-popup.height())/2));});});$(".poolinvitepost").live('click',function(){$(this).parents().eq(2).stop().hide();
var popup=$("#fullscreenpopupcontentmain");$("#fullscreenpopup").show();var request1=$.post('https://winwinride.com/ajax/pool',{id:'invite'},function(data){popup.html('').append(data);popup.css('left',(($(window).width()-popup.width())/2));popup.css('top',((($(window).height()-60)-popup.height())/2));});});$(".poolinvitepost1").live('click',function(){
var popup=$("#fullscreenpopupcontentmain");$("#fullscreenpopup").show();var request1=$.post('https://winwinride.com/ajax/pool',{id:'invite'},function(data){popup.html('').append(data);popup.css('left',(($(window).width()-popup.width())/2));popup.css('top',((($(window).height()-60)-popup.height())/2));});});$(".poolrequestpost").live('click',function(){$(this).parents().eq(2).stop().hide();
var popup=$("#fullscreenpopupcontentmain");$("#fullscreenpopup").show();var request1=$.post('https://winwinride.com/ajax/pool',{id:'request'},function(data){popup.html('').append(data);popup.css('left',(($(window).width()-popup.width())/2));popup.css('top',((($(window).height()-60)-popup.height())/2));});});$(".poolrequestpost1").live('click',function(){
var popup=$("#fullscreenpopupcontentmain");$("#fullscreenpopup").show();var request1=$.post('https://winwinride.com/ajax/pool',{id:'request'},function(data){popup.html('').append(data);popup.css('left',(($(window).width()-popup.width())/2));popup.css('top',((($(window).height()-60)-popup.height())/2));});});$(".poolinviteresponse1").live('click',function(){
var popup=$("#fullscreenpopupcontentmain");$("#fullscreenpopup").show();var request1=$.post('https://winwinride.com/ajax/pool',{object_id:$(this).attr('data-poolinvite-id'),id:'inviteresponse'},function(data){popup.html('').append(data);popup.css('left',(($(window).width()-popup.width())/2));popup.css('top',((($(window).height()-60)-popup.height())/2));});});$(".poolrequestresponse1").live('click',function(){
var popup=$("#fullscreenpopupcontentmain");$("#fullscreenpopup").show();var request1=$.post('https://winwinride.com/ajax/pool',{object_id:$(this).attr('data-poolrequest-id'),id:'requestresponse'},function(data){popup.html('').append(data);popup.css('left',(($(window).width()-popup.width())/2));popup.css('top',((($(window).height()-60)-popup.height())/2));});});$(".composemessageinbox").live('click',function(){
var popup=$("#fullscreenpopupcontentmain");$("#fullscreenpopup").show();var request1=$.post('https://winwinride.com/messages/ajax/compose',{inbox:'inbox',},function(data){popup.html('').append(data);popup.css('left',(($(window).width()-popup.width())/2));popup.css('top',((($(window).height()-60)-popup.height())/2));});});$(".composemessagetrash").live('click',function(){
var popup=$("#fullscreenpopupcontentmain");$("#fullscreenpopup").show();var request1=$.post('https://winwinride.com/messages/ajax/compose',{inbox:'trash',},function(data){popup.html('').append(data);popup.css('left',(($(window).width()-popup.width())/2));popup.css('top',((($(window).height()-60)-popup.height())/2));});});$(".composemessagerideoq").live('click',function(){
var that=$(this);var popup=$("#fullscreenpopupcontentmain");$("#fullscreenpopup").show();var request1=$.post('https://winwinride.com/messages/ajax/compose',{inbox:'no',rideoq:'yes',recipient:that.attr('data-recipient'),},function(data){popup.html('').append(data);popup.css('left',(($(window).width()-popup.width())/2));popup.css('top',((($(window).height()-60)-popup.height())/2));});});$(".composemessage").live('click',function(){
var that=$(this);var popup=$("#fullscreenpopupcontentmain");$("#fullscreenpopup").show();var request1=$.post('https://winwinride.com/messages/ajax/compose',{inbox:'no',recipient:that.attr('data-recipient'),},function(data){popup.html('').append(data);popup.css('left',(($(window).width()-popup.width())/2));popup.css('top',((($(window).height()-60)-popup.height())/2));});});$(".sendinforequest").live('click',function(){
var that=$(this);var popup=$("#fullscreenpopupcontentmain");$("#fullscreenpopup").show();var request1=$.post('https://winwinride.com/ajax/inforequest/send_inforequest',{id:that.attr('data-recipient'),type:that.attr('data-type'),},function(data){popup.html('').append(data);popup.css('left',(($(window).width()-popup.width())/2));popup.css('top',((($(window).height()-60)-popup.height())/2));});});$(".write_reco").live('click',function(){
var that=$(this);var popup=$("#fullscreenpopupcontentmain");$("#fullscreenpopup").show();var request1=$.post('https://winwinride.com/ajax/write_reco',{user_id:that.attr('data-user-id'),},function(data){popup.html('').append(data);popup.css('left',(($(window).width()-popup.width())/2));popup.css('top',((($(window).height()-60)-popup.height())/2));});});});$(document).ready(function(){$('#fullscreenlighttabclose').tipsy({gravity:'ne',fade:true});$('#fullscreendarktabclose').tipsy({gravity:'ne',fade:true});});$(document).ready(function(){});var request;$(document).ready(function(){$("#bottombaremailbtn").click(function(){var that;var that1=$(this);var values=new Array();var counter=0;that=$(this);var email=$("#bottombaremail");if(($.trim(email.val())!='')&&email.val().length<=250&&email.val().indexOf('.')!=-1&&email.val().indexOf('@')!=-1&&email.val().indexOf('@')!=(email.val().length-1)&&email.val().lastIndexOf('@')<email.val().lastIndexOf('.')){that1.val('...');request=$.post("https://winwinride.com/ajax/save_newsletter_email",{email:email.val()},function(data){that1.val(':-)');email.val("");});}
else{}});$("#bottombaremail").keyup(function(){$("#bottombaremailbtn").val('GO');if(request){request.abort();}});$("#bottombaremail").change(function(){$("#bottombaremailbtn").val('GO');if(request){request.abort();}});});