<?php

// Script for the Shocky IRC bot (#shocky on irc.esper.net) by Catlinman
// $args = Contains all arguments passed to the script.
// $ioru = Same as $args but if empty uses the username of the sender.

// Fetches information on Osu players from their user profiles.

$response = file_get_contents("https://osu.ppy.sh/u/$ioru");

if(@explode("</h2>", @explode("<h2>", $response)[1])[0] == "The user you are looking for was not found!") {
    echo "The user you are looking for was not found!";
} else {
    $userid = @explode(";", @explode("var userId = ", $response)[1])[0];
    $country = @explode("'", @explode("flag' title='", $response)[1])[0];

    $osu = file_get_contents("https://osu.ppy.sh/pages/include/profile-general.php?u=$userid&m=0");
    $taiko = file_get_contents("https://osu.ppy.sh/pages/include/profile-general.php?u=$userid&m=1");
    $ctb = file_get_contents("https://osu.ppy.sh/pages/include/profile-general.php?u=$userid&m=2");
    $mania = file_get_contents("https://osu.ppy.sh/pages/include/profile-general.php?u=$userid&m=3");

    $osuranking = @explode("</b>", @explode("Performance</a>: ", $osu)[1])[0];
    $taikoranking = @explode("</b>", @explode("Performance</a>: ", $taiko)[1])[0];
    $ctbranking = @explode("</b>", @explode("Performance</a>: ", $ctb)[1])[0];
    $maniaranking = @explode("</b>", @explode("Performance</a>: ", $mania)[1])[0];

    $osucr = "#". substr(@explode("</span>", @explode("#", @explode("<img class='flag' title=''", $osu)[1])[1])[0], 0, -1);
    $taikocr = "#". substr(@explode("</span>", @explode("#", @explode("<img class='flag' title=''", $taiko)[1])[1])[0], 0, -1);
    $ctbcr = "#". substr(@explode("</span>", @explode("#", @explode("<img class='flag' title=''", $ctb)[1])[1])[0], 0, -1);
    $maniacr = "#". substr(@explode("</span>", @explode("#", @explode("<img class='flag' title=''", $mania)[1])[1])[0], 0, -1);

    if(empty($osuranking)) {
        $osuranking = "n/a";
        $osucr = "n/a";
    }

    if(empty($taikoranking)) {
        $taikoranking = "n/a";
        $taikocr = "n/a";
    }

    if(empty($ctbranking)) {
        $ctbranking = "n/a";
        $ctbcr = "n/a";
    }

    if(empty($maniaranking)) {
        $maniaranking = "n/a";
        $maniacr = "n/a";
    }

    echo "$ioru ($country) | PERFORMANCE | OSU: $osuranking (CR: $osucr) | TAIKO: $taikoranking (CR: $taikocr) | CTB: $ctbranking (CR: $ctbcr) | MANIA: $maniaranking (CR: $maniacr) | PROFILE: https://osu.ppy.sh/u/$ioru";
}
