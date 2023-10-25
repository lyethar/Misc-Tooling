function DecodeBase64($base64String) {
    return [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($base64String))
}

# Example usage:
$encodedString = "WwBOAGUAdAAuAFMAZQByAHYA..."
$decodedString = DecodeBase64 $encodedString
Write-Output $decodedString
