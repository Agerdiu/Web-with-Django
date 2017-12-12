/***Products表**/

/*****提交按钮*******/
$("#login_btn").click(function () {
    if(!validate_adds_form()){
        return false;
    }
    $("#login_form").submit();
});