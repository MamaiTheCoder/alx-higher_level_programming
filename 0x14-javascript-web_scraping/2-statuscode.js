#!/usr/bin/node

// Display the status code of a GET request.
const request = require('request');

request(process.argv[2], function (_err, res) {
  console.log('Code: ', res.statusCode);
});
