console.log("Loading up...")

$(window).on("load", function() {

$("button.visit").click(function() {
    window.location.href= "/";
    return false;
})

$("button.reset").click(function() {
    window.location.href = "/destroy_session"
    return false;
})

})