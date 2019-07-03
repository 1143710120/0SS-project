	$(document).ready(function(){
	 $(".tabs").slide({ trigger: "click" });

});
function delete_department(id){
			$.post(
			'/delete_department/',{
				"id" : id
				},
			function (data){
				if(data) {
                    alert('删除成功')
                    top.location.reload()
                }
			});
}
function edit_department(id) {
	var text = prompt("请输入更改后的数据", "院系名称+院系描述+备注"); //将输入的内容赋给变量
	if (text == "院系名称+院系描述+备注") {
		alert('您没有做出任何更改')
    }
	else {
        var edit_args = text.split('+');
        if (text)//如果返回的有内容
        {
            if (edit_args.length == 3) {
                var department_name = edit_args[0];
                var message= edit_args[1]
                var remark = edit_args[2]
                $.post('/edit_department/', {
                    'id': id,
                    'department_name': department_name,
                    'message':message,
                    'remark': remark
                }, function (data) {
                    if (data) {
                        alert('修改成功')
                        top.location.reload()
                    }
                });
            } else {
                alert('您输入的内容格式不对，或者缺少必须内容')
            }
        } else {
            alert('你没有输入任何内容')
        }
    }

}

