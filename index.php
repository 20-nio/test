<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>出生情報入力</title>
</head>
<body>
    <h1>出生情報入力</h1>
    <form action="result.php" method="post">
        <label for="birthplace">出生地:</label>
        <input type="text" id="birthplace" name="birthplace" required><br>

        <label for="birthtime">出生時刻:</label>
        <input type="datetime-local" id="birthtime" name="birthtime" required><br>

        <input type="submit" value="送信">
    </form>
</body>
</html>
