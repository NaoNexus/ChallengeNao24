<!DOCTYPE html>
<html lang="it">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Homepage</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" integrity="sha512-z9b+7oG5fWeAOeVG2HEoaFPiFjsxxhMbDSFOx6YLLEpAt52D74BlN/C2BZJKPXyBBo5HcAc2rZSXtITc8Unw/A==" crossorigin="anonymous" />
    <style>
        body {
            background-color: #A8D0F0;
            color: #FFF8F8;
            font-family: 'Arial', sans-serif;
            text-align: center;
            margin: 0;
            padding: 0;
        }

        h1 {
            color: #0A0A0A;
            font-size: 150px;
            text-align: center;
            margin: 20px 0;
            font-family: 'Times New Roman', serif;
        }

        .home-link {
            position: absolute;
            top: 10px;
            left: 10px;
            font-size: 20px;
            color: #FFF8F8;
            text-decoration: none;
        }

        .menu {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }

        .menu button,
        .menu select {
            flex: 1;
            background-color: #FFF8F8;
            color: #0A0A0A;
            border: none;
            padding: 15px;
            margin: 0 10px;
            font-size: 18px;
            font-weight: bold;
            text-transform: uppercase;
            cursor: pointer;
            border-radius: 10px;
            transition: background-color 0.3s ease;
        }

        .menu select {
            width: 80px;
            text-align: center; 
        }

        .menu button:hover,
        .menu select:hover {
            background-color: #FF7370;
        }

        .logo-link {
            position: absolute;
            top: 10px;
            left: 10px;
            width: 70px;
            height: 70px;
        }
    </style>
</head>

<body>
    <a href="file:///C:/Users/edoar/Desktop/nao_webapp/codici%20webapp/templates/index.html" class="logo-link"><img src="C:\Users\edoar\Desktop\codici webapp\templates\logo.png" alt="Logo" width="100%" height="100%"></a>
    <h1>Swarovski</h1>
    <div class="menu">
        <select onchange="window.location.href=this.value">
            <option value="" disabled selected hidden>Prodotto</option>
            <option value="http://127.0.0.1:5000/pagina1">Pagina 1</option>
            <option value="http://127.0.0.1:5000/pagina2">Pagina 2</option>
        </select>
        <button onclick="window.location.href='http://127.0.0.1:5000/bilancio'">Vendite</button>
        <button onclick="window.location.href='http://127.0.0.1:5000/utenti'">Utenti</button>
    </div>
    <div class="menu">
        <button onclick="window.location.href='http://127.0.0.1:5000/carrelli'">Carrelli</button>
        <button onclick="window.location.href='http://127.0.0.1:5000/scaffale'">Scaffale</button>
        <button onclick="window.location.href='http://127.0.0.1:5000/magazzino'">Magazzino</button>
    </div>
    <div class="menu">
        <button onclick="window.location.href='http://127.0.0.1:5000/api'">API</button>
        <button onclick="window.location.href='http://127.0.0.1:5000/services'">Services</button>
    </div>
</body>

</html>
