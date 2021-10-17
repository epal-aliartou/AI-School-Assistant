var payload=msg.payload;
var topic=msg.topic;

function checktime(time)
{
    var error_flag=false;
   var a=time.split(":"); 
   node.log(a)
   if(a.length <2)
     error_flag=true;
   if(parseInt(a[0])>23)
     error_flag=true;
   if(parseInt(a[1])>=60)
     error_flag=true;
    if(parseInt(a[2])>=60)
     error_flag=true;

return error_flag;  
}
if (topic=="on_time")
{
  flow.set("on_time",msg.payload);
  
    
}
if (topic=="off_time")
 
{
     flow.set("off_time",msg.payload);

}
if (topic=="submit")
 
{
  var on_time= flow.get("on_time");
  var off_time= flow.get("off_time");
  var error_flag=false;
  if(checktime(on_time)) //ok
    error_flag=true;
  if(checktime(off_time)) //ok
    error_flag=true;
  


  if(!error_flag)
  {
      newpayload={};
      newpayload.ontime=on_time;
      newpayload.offtime=off_time;
      msg.payload=newpayload;
;
   return[msg,null];
}
else
{
    var msg1={};
    msg1.payload="error time not set";
   return [null,msg1]; 
}
}