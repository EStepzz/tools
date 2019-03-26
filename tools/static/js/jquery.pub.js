//(document).ready(function(){
$(function () {
   $("btn btn-default").submit(function () {
    var ips = $('#basic-ip').val()
    var addr = $('#basic-ip').val()
    var licenseInfo = $('.exampleInputFile').val()
    $.ajax({
        type:'post',
        url:'/license',
        data:{'ips':ips,
            "path":addr,
            "info":license_info
        },
        dataType:"json",
        success:function (msg) {
            if (msg.success){
                alert("提交成功")
            }
            else{
                alert("异常请检查")
            }
        }
    })
   } ,
       function f_check_IP() {
        var ip = document.getElementById('basic-ip').value;
        var re = /^(\d+)\.(\d+)\.(\d+)\.(\d+)$/;
        if (re.test(ip)) {
            if (RegExp.$1 < 256 && RegExp.$2 < 256 && RegExp.$3 < 256 && RegExp.$4 < 256)
                return true;
        }
        alert("IP有误！");
        return false;
    }
});
})



// $("#apply_form").submit(function (){
//     parent.layer.close(index);
//     $.ajax({
//         async:false,
//         type:"POST",
//         url:'${pageContent.request.contextPath}/license',
//         data:$("apply_form").serialize(),
//         dataType:"text",
//         success:function () {
//             alert("请求成功")
//         },
//         error:function () {
//             alert("请检查参数")
//         }
//     })
//     }
// )
    
