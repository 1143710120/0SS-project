	$(document).ready(function(){
	 $(".tabs").slide({ trigger: "click" });

});
function delete_teacher(id){
			$.post(
			'/delete_teacher/',{
				"id" : id
				},
			function (data){
				if(data) {
                    alert('删除成功')
                    top.location.reload()
                }
			});
}
function edit_teacher(id) {
	var text = prompt("请输入更改后的数据", "教师姓名+教师性别+教师年龄+教师身份+教师院系"); //将输入的内容赋给变量
	if (text == "教师姓名+教师性别+教师年龄+教师身份+教师院系") {
		alert('您没有做出任何更改')
    }
	else {
        var edit_args = text.split('+');
        print()
        if (text)//如果返回的有内容
        {
            if (edit_args.length == 5) {
                var name = edit_args[0];
                var sex = edit_args[1]
                var age = edit_args[2]
                var identity = edit_args[3]
                var department_name = edit_args[4]
                $.post('/edit_teacher/', {
                    'id': id,
                    'name': name,
                    'sex': sex,
                    'age': age,
                    'identity': identity,
                    'department_name': department_name
                }, function (data) {
                    if (data.msg == 'wrong') {
                        alert('院系不存在')
                        top.location.reload()
                    }else{
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