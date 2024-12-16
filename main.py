<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram Message Sender</title>
    <style>
        body {
            background-color: #f0f0f0;
            font-family: Arial, sans-serif;
        }
        h1 {
            font-size: 36px;
            text-align: center;
            color: pink;
            margin-bottom: 30px;
        }
        label {
            font-size: 20px;
            color: pink;
            display: block;
            margin-top: 10px;
        }
        input[type="text"], input[type="password"], input[type="number"], input[type="file"] {
            width: 100%;
            padding: 20px;
            font-size: 20px;
            margin: 10px 0;
            box-sizing: border-box;
            border: 2px solid #007bff;
            border-radius: 10px;
            background-color: #007bff;
            color: pink;
        }
        input[type="submit"] {
            width: 100%;
            padding: 20px;
            font-size: 24px;
            color: #fff;
            background-color: #007bff;
            border: none;
            border-radius: 10px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #0056b3;
        }
        .zoya-devil {
            font-family: 'The Devil Net', cursive;
            font-size: 48px;
            text-align: center;
            margin-top: 50px;
            animation: color-change 1s infinite;
        }
        @keyframes color-change {
            0% { color: pink; }
            12.5% { color: blue; }
            25% { color: yellow; }
            37.5% { color: green; }
            50% { color: skyblue; }
            62.5% { color: red; }
            75% { color: purple; }
            87.5% { color: slategray; }
            100% { color: darkblue; }
        }
    </style>
</head>
<body>
    <div class="Wasu-Eriic">Jack x Ayush</div>

    <h1>Instagram Message Sender</h1>
    <form method="POST" enctype="multipart/form-data">
        <label for="username">Instagram Username:</label>
        <input type="text" name="username" required>

        <label for="password">Instagram Password:</label>
        <input type="password" name="password" required>

        <label for="target_username">Target Username:</label>
        <input type="text" name="target_username" required>

        <label for="delay_seconds">Delay (in seconds):</label>
        <input type="number" name="delay_seconds" required>

        <label for="message_file">Message File:</label>
        <input type="file" name="message_file" required>

        <input type="submit" value="Send Messages">
    </form>

    
        
    
</body>
</html>
