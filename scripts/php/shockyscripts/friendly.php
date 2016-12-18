<?php

// Script for the Shocky IRC bot (#shocky on irc.esper.net) by Catlinman
// $args = Contains all arguments passed to the script.
// $ioru = Same as $args but if empty uses the username of the sender.

// Allows you to check if a user is friendly or not. Very crucial.

$options = array(
    "$ioru is friendly.",
    "$ioru is friendly but also holding a gun behind his back.",
    "$ioru is friendly with the world.",
    "$ioru is friendly but feels like murdering someone.",
    "$ioru is friendly and wants to marry.",
    "I AM FRIENDLY DON'T SHOOT!",
    "$ioru killed my friendly cat.",
    "$ioru is friendly. He's selling two cans of dog food in the church.",
    "$ioru is friendly but who can you really trust these days.",
    "$ioru probably ate your best friend who was friendly.",
    "$ioru seems to be shouting \"don't shoot\". He must be friendly.",
    "$ioru is wearing a friendly dress. Enough said.",
    "$ioru is friendly. Wait, I lied.",
    "$ioru has noticed his right earlobe is friendly.",
    "$ioru can only be friendly if everyone is friendly.",
    "$ioru feels a strange urge to take out is friendly anger.",
    "$ioru spotted a trout. It was friendly."
);

echo $options[rand(0, count($options) - 1)];
