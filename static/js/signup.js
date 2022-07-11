let phoneRegex = /^[(]?[\+]?[0-9]{3}[)]?[-\s]?[0-9]{3}[-\s]?[0-9]{4,6}$/im;

function check_phone(){
    let user_phn = document.getElementById("user_phn_no");
    let err_phn = document.getElementById("error-msg-phone");

    if (user_phn.value.match(phoneRegex)){
        err_phn.style.display = "none";
        user_phn.style.border = "2px solid lightgreen"
    }

    else if(user_phn.value == ""){
        user_phn.style.border= "2px solid red"
        err_phn.style.display = 'none'
    }
    
    else{
        user_phn.style.border= "2px solid red";
        err_phn.style.display = 'block'
    }
    
};

let mailRegex = /^[a-zA-Z][a-zA-Z0-9\-\_\.]+@[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}$/;

function check_mail(){
    user_mail = document.getElementById("user_mail");
    err_msg = document.getElementById("error-msg-mail");

    if (user_mail.value.match(mailRegex)){
        err_msg.style.display = "none";
        user_mail.style.border = "2px solid lightgreen";
    }

    else if(user_mail.value == ""){
        user_mail.style.border= "2px solid red";
        err_msg.style.display = 'none';
    }
    
    else{
        user_mail.style.border= "2px solid red";
        err_msg.style.display = 'block';
    }
    
};

function show_Password(){
    let pswd = document.getElementById("user_pswd");
    let re_pswd=document.getElementById("user_repswd");
    // console.log("SHOW PASSWORD IS WORKING!");
    if (pswd.getAttribute('type') === "password"){
        pswd.setAttribute('type',"text")
        re_pswd.setAttribute('type',"text")
    }
    else if  (pswd.getAttribute('type') === "text"){
        pswd.setAttribute('type',"password")
        re_pswd.setAttribute('type',"password")
    }
};

let pswd_regex = /[a-zA-Z][a-zA-Z0-9\-\_\.]+@[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}$/;
function check_pswd(){
    let pswd = document.getElementById("user_pswd");
    let re_pswd = document.getElementById("user_repswd");
    let error_pswd = document.getElementById("error-msg-pswd");
    validate_pswd(pswd.value)
    

    if (pswd.value === re_pswd.value){
        pswd.style.border = "2px solid lightgreen";
        re_pswd.style.border = "2px solid lightgreen";
        error_pswd.style.display = "none";
    }
    else if (pswd.value !== re_pswd.value){
        pswd.style.border = "2px solid red";
        re_pswd.style.border = "2px solid red";
        error_pswd.style.display = "block";
    }
}


function validate_pswd(pswd){
    let str ="Your password should ";

    
    let validation_msg = document.getElementById("validate-msg-pswd");
    

    if (pswd.length < 8) {
        str = str.concat(",be at least 8 characters");
         
    }
    else{
        str = str.replace(",be at least 8 characters","");
    }
    if (pswd.search(/[a-z]/i) < 0) {
        str = str.concat(",contain at least one letter");
        
    }
    else{
        str = str.replace(",contain at least one letter","");
    }
    if (pswd.search(/[0-9]/) < 0) {
        str = str.concat(",contain at least one digit");
        
    }
    else{
        str = str.replace(",contain at least one digit","");
    }
    if (pswd.search(/[!@#$%^&*()]/) < 0) {
        str = str.concat(",contain at least one specialcharacter.");
        
    }
    else{
        str = str.replace(",contain at least one specialcharacter.","");
    }
    
    validation_msg.innerHTML = str

    if (str.length <= 19 ){
        validation_msg.innerHTML = "";
        validation_msg.style.display = "none"
    }
    else{
        validation_msg.style.display = "block"
    }
}



function required(){
    let mail = document.getElementById("user_mail").value;
    let phone = document.getElementById("user_phone").value;
 
    if (mail === "" && phone === "" ){
        alert("Please enter your phone number or email")
        return false
    }
    else if (mail === "" && phone !== "" ){
        return true
    }
    else if (mail !== "" && phone === "" ){
        return true
    }
}