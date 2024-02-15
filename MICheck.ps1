# Define the header to include the Metadata:true requirement
$headers = @{
    Metadata = 'true'
}

# Define the URL for the request
$url = "http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https%3A%2F%2Fmanagement.azure.com%2F"

# Use Invoke-RestMethod to make the request
$response = Invoke-RestMethod -Uri $url -Headers $headers -Method Get -NoProxy

# The response object will contain the OAuth2 token and other data in a parsed form
# To access the access_token, you can simply refer to it like this:
$token = $response.access_token

# Output the token to the console
Write-Output $token
