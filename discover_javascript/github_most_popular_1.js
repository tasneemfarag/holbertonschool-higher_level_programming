var https = require('https');

var options = {
    hostname: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
    headers: {
	'User-Agent': 'Holberton_School',
	'Authorization': 'token d2739b7e46416f82a729a383721859a753fe6416'
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