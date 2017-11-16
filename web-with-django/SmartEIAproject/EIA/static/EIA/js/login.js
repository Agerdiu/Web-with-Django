



/**根据输入校验进行DOM操作*/
function  show_validate_msg(ele,status,msg) {
    $(ele).parent().removeClass("has-success has-error");
    $(ele).next("span").text("");
    if(status=="success"){
        $(ele).parent().addClass("has-success");
        $(ele).next("span").text(msg);
    }else if(status=="error"){
        $(ele).parent().addClass("has-error");
        $(ele).next("span").text(msg);
    }
}

/********校验表单数据***********/
function validate_adds_form() {
    //邮箱
    var email=$("#login_email_input").val();
    var regemail=/^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/;
    if(!regemail.test(email)){
        show_validate_msg("#login_email_input","error","请输入正确邮箱");
        return false;
    }else{
        show_validate_msg("#login_email_input","success","");
    }

    //校验密码
    var password=$("#login_password_input").val();
    var regpassword=/^[a-z0-9_-]{6,18}$/;
    if(!regpassword.test(password)){
        show_validate_msg("#login_password_input","error","请输入6-16位数字，字母，下划线的组合");
        return false;
    }else{
        show_validate_msg("#login_password_input","success","");
    }

    return true;
}


/*****登陆按钮*******/
$("#login_btn").click(function () {
    if(!validate_adds_form()){
        return false;
    }
    $("#login_form").submit();
});