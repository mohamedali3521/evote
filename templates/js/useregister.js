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
        let uname=document.forms["regi"]["uname"].value;
        var a=/^[a-zA-Z]+$/;
        if(uname=="")
        {
            alert("Enter Your Name");
        }
        else if(uname.match(a))
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
        let pnum=document.forms["regi"]["pnum"].value;
        var phnNum =  /^\d{10}$/;
        if(pnum=="")
        {
            alert("Enter the mobile number");
        }
        else if(pnum.match(phnNum))
        {
        }
        else{
            alert("Enter the valid mobile number");
        }
        let pwrd=document.forms["regi"]["pwrd"].value;
        var password = /^[a-zA-Z0-9!@#$%.&,]{8,16}$/;
        if(pwrd=="")
        {
            alert("Password must be filled out");
        }
        else if(pwrd.match(password))
        {
        }
        else
        {
            alert("Password contain alphanumeric values and special characters");
        }
    }
