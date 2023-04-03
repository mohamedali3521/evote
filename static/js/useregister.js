function registration()
       {
        // var aadhar = document.getElementById("aadhar").value;
        
        let aadhar=document.forms["regi"]["aadhar"].value;
        // let adharcardTwelveDigit = /^\d{12}$/;
        if(aadhar=="")
        {
        alert("aadhar must be filled out");
        }
        else if(aadhar.length==12) 
        {
        
        }
        else{
            alert("Enter valid aadhar number");
        }
        let uname=document.forms["regi"]["username"].value;
        var a=/^[a-zA-Z]+$/;
        if(username=="")
        {
            alert("Enter Your Name");
        }
        else if(username.match(a))
        {
        }
        else
        {
            alert("enter valid name");
        }
        let age=document.forms["regi"]["age"].value;
        if(age=="")
        {
            alert("Enter the age");
        }
        else if(age>17)
        {
        }
        else
        {
            alert("Age must be greater than or equal to 18 for vote");
        }
        let pnum=document.forms["regi"]["phoneno"].value;
        var phnNum =  /^\d{10}$/;
        if(phoneno=="")
        {
            alert("Enter the mobile number");
        }
        else if(phoneno.match(phnNum))
        {
        }
        else{
            alert("Enter the valid mobile number");
        }
        let pwrd=document.forms["regi"]["password"].value;
        var pass = /^[a-zA-Z0-9!@#$%.&,]{8,16}$/;
        if(pwrd=="")
        {
            alert("Password must be filled out");
        }
        else if(password.match(pass))
        {
        }
        else
        {
            alert("Password contain alphanumeric values and special characters");
        }
    }
