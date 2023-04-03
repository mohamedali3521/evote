function confirmsubmission()
                {
                    
                    if (confirm("Are you sure,you want to vote this candidate?"))
                    {
                    // If the user confirms, redirect to the specified URL
                    window.location.href = "thanks.html";
                    } 
                    else {
                    // If the user cancels, do nothing
                    return false;
                            }
            }