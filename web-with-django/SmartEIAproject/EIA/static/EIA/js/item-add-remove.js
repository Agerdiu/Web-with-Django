
/**产品表的增加和删除**/
$("#product_add_btn").click(function () {
    // 复制一个样例 加在后面
    var tr = $("#product-table tr").eq(1).clone();
    tr.appendTo(".table");
    var num=$("#total-num").val();//总数
    num=parseInt(num);
    num+=1;
    $("#total-num").val(num);//总数+1
    $("#product-table tr:last td:eq(0)").html(num);
    for(var i=1;i<=4;i++) {
        ss = ".table tr:last td:eq(1) input";
        ss1=ss.substring(0,21);
        ss2=ss.substring(22,ss.length);
        ss=ss1+i+ss2;
        str = $(ss).attr("name");
        str1=str.substring(0,5);
        str2=str.substring(6,str.length);
        str=str1+(num-1)+str2;
        $(ss).attr("name",str);
    }
});

$("#product_remove_btn").click(function () {
    // 复制一个样例 加在后面
    var num=$("#total-num").val();//总数
    num=parseInt(num);
    if(num>1) {
        num -= 1;
        $("#total-num").val(num);//总数-1
        $("#product-table tr:last").remove();
    }

});


/**材料表的增加和删除**/
$("#material_add_btn").click(function () {
    // 复制一个样例 加在后面
    var tr = $("#material-table tr").eq(1).clone();
    tr.appendTo(".table");
    var num=$("#total-num").val();//总数
    num=parseInt(num);
    num+=1;
    $("#total-num").val(num);//总数+1
    $("#material-table tr:last td:eq(0)").html(num);
    for(var i=1;i<=5;i++) {
        ss = ".table tr:last td:eq(1) input";
        ss1=ss.substring(0,21);
        ss2=ss.substring(22,ss.length);
        ss=ss1+i+ss2;
        str = $(ss).attr("name");
        str1=str.substring(0,5);
        str2=str.substring(6,str.length);
        str=str1+(num-1)+str2;
        $(ss).attr("name",str);
    }
});

$("#material_remove_btn").click(function () {
    // 复制一个样例 加在后面
    var num=$("#total-num").val();//总数
    num=parseInt(num);
    if(num>1) {
        num -= 1;
        $("#total-num").val(num);//总数-1
        $("#material-table tr:last").remove();
    }

});

/**设备表的增加和删除**/
$("#equipment_add_btn").click(function () {
    // 复制一个样例 加在后面
    var tr = $("#equipment-table tr").eq(1).clone();
    tr.appendTo(".table");
    var num=$("#total-num").val();//总数
    num=parseInt(num);
    num+=1;
    $("#total-num").val(num);//总数+1
    $("#equipment-table tr:last td:eq(0)").html(num);
    for(var i=1;i<=4;i++) {
        ss = ".table tr:last td:eq(1) input";
        ss1=ss.substring(0,21);
        ss2=ss.substring(22,ss.length);
        ss=ss1+i+ss2;
        str = $(ss).attr("name");
        str1=str.substring(0,5);
        str2=str.substring(6,str.length);
        str=str1+(num-1)+str2;
        $(ss).attr("name",str);
    }
});

$("#equipment_remove_btn").click(function () {
    // 复制一个样例 加在后面
    var num=$("#total-num").val();//总数
    num=parseInt(num);
    if(num>1) {
        num -= 1;
        $("#total-num").val(num);//总数-1
        $("#equipment-table tr:last").remove();
    }

});