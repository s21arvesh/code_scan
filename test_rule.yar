rule SuspiciousEval
{
    strings:
        $eval = "eval("
        $exec = "exec("

    condition:
        $eval or $exec
}
