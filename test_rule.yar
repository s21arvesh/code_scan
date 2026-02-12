rule Hardcoded_AWS_Key
{
  strings:
    $a = /AKIA[0-9A-Z]{16}/
  condition:
    $a
}
