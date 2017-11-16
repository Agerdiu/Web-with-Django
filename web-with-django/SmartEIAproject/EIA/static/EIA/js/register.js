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

    //校验公司名称
    var environmentAssessmentCompany=$("#reg_environmentAssessmentCompany_input").val();
    var regenvironmentAssessmentCompany=/^[\u4e00-\u9fa5]{2,20}$/;
    if(!regenvironmentAssessmentCompany.test(environmentAssessmentCompany)){
        show_validate_msg("#reg_Name_input","error","请输入正确公司名称");
        return false;
    }else{
        show_validate_msg("#reg_Name_input","success","");
    }
    //校验姓名
    var first_name=$("#reg_Name_input").val();
    var regfirst_name=/^[\u4e00-\u9fa5]{2,20}$/;
    if(!regfirst_name.test(first_name)){
        show_validate_msg("#reg_Name_input","error","请输入合法姓名");
        return false;
    }else{
        show_validate_msg("#reg_Name_input","success","");
    }

        //校验手机号
    var tel=$("#reg_tel_input").val();
    var regTel=/^[1][3,4,5,7,8][0-9]{9}$/;
    if(!regTel.test(tel)){
        show_validate_msg("#reg_tel_input","error","请输入正确手机号码");
        return false;
    }else{
        show_validate_msg("#reg_tel_input","success","");
    }

        //校验邮箱
    var email=$("#reg_email_input").val();
    var regEmail=/^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/;
    if(!regEmail.test(email)){
        show_validate_msg("#reg_email_input","error","请输入正确email");
        return false;
    }else{
        show_validate_msg("#reg_email_input","success","");
    }

    //校验密码
    var password=$("#reg_password_input").val();
    var regPassword=/^[a-z0-9_-]{6,18}$/;
    if(!regPassword.test(password)){
        show_validate_msg("#reg_password_input","error","请输入6-16位数字，字母，下划线的组合");
        return false;
    }else{
        show_validate_msg("#reg_password_input","success","");
    }

    return true;
}




/*********模态框注册按钮*********/
$("#register_btn").click(function () {
if(!validate_adds_form()){
        return false;
    }
    $("#register_form").submit();
});