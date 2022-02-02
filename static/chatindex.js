$(document).ready(function()
{

    $("#myform").submit(function(event)
    {
        var msg = $("#msg").val()
        console.log(msg)
        const url = "/"
        var request_headers = {
            method: "POST",
            body: JSON.stringify(`{"my message": ${msg}}`)
        }
        var response = fetch(url, request_headers)
        response.then(function(resp){
            resp.json().then(function(data){$("#response").text(data["message"]);})
        });
        return false;  // Stops Page from refreshing
    })
}) 

/*
.then() basically waits for the response from the server side and then runs the function
defined inside it. Since Javascript allows us to make functions on spot as similar to lambda
in python, we just create a function which takes resp as argument in the first .then()
which will give us the server response and then get the json data using .then() on json()
yeah man, javascript is a fked up language if you think about it. yet makes it convinient
*/