Back-end Challenge

In the PHP file, write a program to perform a GET request on the route

https://coderbyte.com/api/challenges/json/age-counting which contains a data key and the value is a string which contains items in the format: key-STRING, age INTEGER. Your goal is to count how many items exist that have an age equal to or greater than 50, and print this final value.

Example Input

{"data":"key=IAfpK, age=58, key=WNVdi, age=64, key=jp9zt, age=47")

Example Output

2

My Solution :-

<?php 

  $ch = curl_init('https://coderbyte.com/api/challenges/json/age-counting');
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HEADER, 0);
  $data = curl_exec($ch);
  curl_close($ch);

  $response = json_decode($data, true);
  $dataString = $response['data'];

  $count = 0;
  $items = explode(',', $dataString);

  foreach ($items as $item){
    $item = trim($item);
    if(strpos($item, 'age=') !== false){
      $age = (int) str_replace('age=', '', $item);

      if($age >=50){
         $count++;
      }
    }
  }
  
  echo $count;

?>