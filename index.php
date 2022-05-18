<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="styl8.css">
    <title>Nasz sklep internetowy</title>
</head>
<body>
<div id="menu">
    <a href="index.php">Glowna</a>
    <a href="procesory.html">Procesory</a>
    <a href="ram.html">RAM</a>
    <a href="grafika.html">Grafika</a>
</div>
<div id="logo">
    <h2>Podzespoly komputerowe</h2>
</div>
<div id="glowny">
    <h1>Dzisiejsze promocje</h1>
    <table>
        <tr>
            <th>NUMER</th>
            <th>NAZWA PODZESPOLU</th>
            <th>OPIS</th>
            <th>CENA</th>
        </tr>
    </table>
</div>
<div class="stopka">
    <img src="scalak.jpg" alt="promocje na procesory">
</div>
<div class="stopka">
    <h4>Nasz sklep internetowy</h4>
    <p>Wsplopracujemy z hurtownia
        <a href="http://edata.pl/" target="_blank">edata</a>
    </p>
</div>
<div class="stopka">
    <p>zadzwon: 601 602 603</p>
</div>
<div class="stopka">
    <p>Strone wykonal: TEB</p>
</div>

<?php
function skrypt(){
    $conn  =  mysqli_connect("localhost", "root", "", "baza");
    $sql  = SELECT id,nazwa,opis, cena from podzespoly WHERE cena<1000;
    $res  =  mysqli _query($conn, $sql);

    while($row  = mysqli_fetch_assoc($res)){
        echo "<tr>";
        echo "<td>".$row["id"]."</td>";
        echo "<td>".$row["nazwa"]."</td>";
        echo "<td>".$row["opis"]."</td>";
        echo "<td class='doPrawej'>".$row["cena"]."</td>";
        echo "</tr>";
    }
    mysqli_close($conn);
}
?>
</body>
</html>