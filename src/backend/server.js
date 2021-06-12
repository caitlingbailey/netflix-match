var express = require('express');
var bodyParser = require('body-parser');
var app = express();


app.get("/", (req, res) => {
   res.sendFile(__dirname + "../frontend/index.html");
});


































module.exports = app;