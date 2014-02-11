get = function(url){
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", url, false);
    xmlhttp.send();
    return xmlhttp.responseText;
}

function generate(name){
    key = get("/seznam-captcha/create/");
    document.getElementById("seznam-captcha-img-"+name).src = "http://captcha.seznam.cz/captcha.getImage?hash="+key;
    document.getElementById("seznam-captcha-key-"+name).value = key;
}

function getCaptchaName(){
    return $('.seznam-captcha-input').attr('name').split('_')[0];
}

$(function(){
    generate(getCaptchaName());
})

