<?php
header('Access-Control-Allow-Origin: ' . $_SERVER['HTTP_ORIGIN']);
header('Access-Control-Allow-Methods: GET, POST');
header('Access-Control-Allow-Headers: Content-Type');
$url = "http://127.0.0.1:5070/generate";
$ch = curl_init($url);

// Prepare the POST data
$post_data = array();
// $post_data['file'] = new CURLFile($image_path, $_FILES['file']['type'], $_FILES['file']['name']);
foreach ($_POST as $key => $value) {
    $post_data[$key] = $value;
}

curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, $post_data);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
curl_setopt($ch, CURLOPT_HEADER, 1);
$response = curl_exec($ch);

$header_size = curl_getinfo($ch, CURLINFO_HEADER_SIZE);
$header = substr($response, 0, $header_size);
$body = substr($response, $header_size);
$data = json_decode($body, true);
// $data['font-size'] = 140;
// $data['font-family'] = 'Impact';
echo json_encode($data);
curl_close($ch);
// print_r($response);

// add data to database
