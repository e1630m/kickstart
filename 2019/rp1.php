<?php

function solve($a, $b) {
    $m = ($a + $b) / 2;
    printf("%d\n", $m);
    fscanf(STDIN, "%s", $s);
    if (strcmp($s, "CORRECT") == 0)
        return;
    else if (strcmp($s, "TOO_SMALL") == 0)
        $a = $m + 1;
    else
        $b = $m - 1;
    solve($a, $b);
}

fscanf(STDIN, "%d", $t);
for ($ks = 0; $ks < $t; $ks++) {
    fscanf(STDIN, "%d %d", $a, $b);
    fscanf(STDIN, "%d", $n);
    solve($a + 1, $b);
}
?>
