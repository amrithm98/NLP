var apiai = require('apiai');
 
var app = apiai("f2b67b34d8824bbfafbde3d2f2a48c8e");
 
var request = app.textRequest('get me a lion eating a goat', {
    sessionId: 'amrithm98'
});
 
request.on('response', function(response) {
    console.log(response);
    response=response.result.parameters
    console.log(response.animals+" actions "+response.actions+" items "+response.items);
});
 
request.on('error', function(error) {
    console.log(error);
});
 
request.end();
