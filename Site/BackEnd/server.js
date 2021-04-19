const mysql = require("mysql2");
const express = require("express");
const bodyParser = require("body-parser");
const dbConfig = require("./app/config/db.config")

const app = express();
const urlencodedParser = bodyParser.urlencoded({ extended: false });

const pool = mysql.createPool({
    connectionLimit: 5,
    host: dbConfig.HOST,
    port: dbConfig.PORT,
    user: dbConfig.USER,
    database: dbConfig.DB,
    password: dbConfig.PASSWORD
});

app.use(function(req,res,next){
    res.header("Access-Control-Allow-Origin", "*"); 
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

app.get("/", function (req, res,next) {
    pool.query("SELECT * FROM `GOST_TYPES`", function (err, data) {
        if (err) return console.log(err);
        console.log(data);
        res.json(data)
    });
});

app.get("/:GOST", function (req, res,next) {
    const GOST = req.params.GOST;
    var queryStr = "SELECT * FROM `" + GOST + "`";
    pool.query(queryStr, function (err, data) {
        if (err) return console.log(err);
        console.log(data);
        res.json(data);
    });
});

app.get("/:GOST/:TYPE", function (req, res) {
    const GOST = req.params.GOST;
    const TYPE = req.params.TYPE;
    var queryStr = "SELECT * FROM `" + GOST + "` WHERE GOST = " + TYPE;
    pool.query(queryStr, function (err, data) {
        if (err) return console.log(err);
        console.log(data);
        res.json(data);
    });
});

app.listen(3000, function () {
    console.log("Сервер ожидает подключения...");
});