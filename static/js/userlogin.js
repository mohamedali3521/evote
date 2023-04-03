function uservalidation()
      {
        let aadhar=document.forms["login"]["aadharno"].value;
        if(aadhar=="")
        {
          alert("Enter aadhar number");

        }
        else if(aadhar.length==12)
        {

        }
        else{
          alert("please enter valid aadhar number ");

        }
        let password=document.forms["login"]["pwd"].value;
        if(password=="")
        {
          alert("Please enter your password");

        }
        
      }