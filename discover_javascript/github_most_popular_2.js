var https = require('https');

var options = {
    hostname: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
    headers: {
	'User-Agent': 'Holberton_School',
	'Authorization': 'token 576bcef0e6a9e47b7bbb47385326d42a630bfff6'
    }
};

var printOut = function (jsonString) {
    console.log(typeof jsonString);
    console.log(jsonString);
}

var req = https.request(options, function(res) {
    streamToString(res,printOut)    
    });

req.end();

function streamToString(stream, cb) {
  const chunks = [];
  stream.on('data', (chunk) => {
    chunks.push(chunk);
  });
  stream.on('end', () => {
    cb(chunks.join(''));
  });
}

req.on('error', function(e) {
    console.error(e);
});
