```sh
<!-- xss.html -->
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <script type="text/javascript">
    var name;
    if(location.hash == '#welcome'){
      name = "AAA"
    }
    document.write(`hello ${name}`)
    </script>
  </head>
  <body>
    HELLO abc
  </body>
</html>
```
จากโค้ดสามารถ xss injection จากบรรทัด document.write(`hello ${name}`) วิธีการคือ
1. เข้าเว็บ(ถ้าให้ดีก็ของตัวเอง) ไปยัง console
2. พิมพ์ window.name = "<i m g s r c = x   o n e r r o r = a l r e t (1)>" // xss payload ทั่วไป     <-- จงใจเขียนผิด 
3. และ window.location = "http://127.0.0.1/xss.html"

เพราะว่า จากข้อ 2 เป็นการเซต name ตัวเดียวกัน และ window.name เป็น global var ทั้ง 2 แท็บของเบาว์เซอร์เห็นเป็นตัวเดียวกัน <br>
และ xss.html จะรับ value จากข้อ 2 ไป execute

โค้ดจาก : https://www.youtube.com/watch?v=L1RvK1443Yw&ab_channel=LiveOverflow
อยากเขียนเก็บเอาไว้
