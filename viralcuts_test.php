<?php
// Set the URL of the endpoint where you want to make the POST request
$endpointUrl = "https://datawb.com/viralcuts.php"; // Replace with the actual URL

// Data to be sent in the POST request
$data = array(
    'video' => 'https://www.youtube.com/watch?v=QRy4JJNTAiA'
);

// Initialize cURL session
$ch = curl_init();

// Set cURL options
curl_setopt($ch, CURLOPT_URL, $endpointUrl);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

// Execute the cURL session and fetch the result
$result = curl_exec($ch);

// Check for cURL errors
if (curl_errno($ch)) {
    echo 'cURL Error: ' . curl_error($ch);
}

// Close cURL session
curl_close($ch);

// Echo the result
echo $result;
