//ほかのメニューを閉じるスクリプト
$(function (){
    $("details").click(function () {
        console.log("hello")
        $(this).nextAll().removeAttr("open")
        $(this).prevAll().removeAttr("open")
    });
});
//hambergerメニューのスクリプト
$(function () {
    $("#hamberger").click(function () {
        $(this).toggleClass('active');

        if ($(this).hasClass('active')) {
            $(".div1").addClass('active');
        } else {
            $(".div1").removeClass('active');
        }
    });
});
//
