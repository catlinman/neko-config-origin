<?php

// Script for the Shocky IRC bot (#shocky on irc.esper.net) by Catlinman
// $args = Contains all arguments passed to the script
// $ioru = Same as $args but if empty uses the username of the sender

// Basic bitly link shortening script.

if(!$args) {
    echo "Missing required URL argument!";
    exit();
}

$token = "a3a75bea2e87347f66a3d41bafd61ea073e63c90";
$url = "https://api-ssl.bitly.com/v3/shorten?access_token=$token&longUrl=$args";
$response = file_get_contents($url);

$json = json_decode($response, true);
$data = $json["data"];

if(isset($data["url"])) {
    echo $data["url"];

} else {
    $status = $json["status_code"];
    $txt = $json["status_txt"];
    echo "Error: $status | $txt";
}
