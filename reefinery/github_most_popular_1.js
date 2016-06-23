var https = require('https');

var options = {
   hostname: 'api.github.com',
   path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
   headers: {
      'User-Agent': 'Holberton_School',
      'Authorization': 'token aa9bb6a760f8f03c4351818ef6fb4cc0e27583eb'
   }
}  

var req = https.request(options, function(res) {
  console.log(res.statusCode);
  res.on('data', function(d) {
    process.stdout.write(d);
  });
});
req.end();

req.on('error', function(e) {
  console.error(e);
});
