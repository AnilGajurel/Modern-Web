  function validateForm(){
    var pwd=document.forms["validregister"]["userpassword"].value;
    var cpwd=document.forms["validregister"]["usercpassword"].value;
    var fname=document.forms["validregister"]["userfname"].value;
    var lname=document.forms["validregister"]["userlname"].value;
    var email=document.forms["validregister"]["useremail"].value;
    if(pwd!=cpwd)
    {
      alert("password not match");
      return false;
    }
    else if(fname==null || fname=="" ){
      alert("please fill the first name text field");
      return false;
    }
    else if(lname==null || lname==""){
      alert("please fill the last name text field");
      return false;
    }
    else if(pwd.length<8){
      alert("please must be at least 8 characters long");
      return false;
    }
    else if(cpwd.length<8){
      alert("please must be at least 8 character long");
      return false;
    }
    else if(email==null || email==""){
      alert("email cant be blank");
      return false;
    }
}

















