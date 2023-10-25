function DecodeBase64($base64String) {
    return [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($base64String))
}

if ($args.Count -ne 1) {
    Write-Error "Please provide a single Base64 encoded string as an argument."
    exit 1
}

$decodedString = DecodeBase64 $args[0]
Write-Output $decodedString
