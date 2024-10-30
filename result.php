<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $birthplace = $_POST['birthplace'];
    $birthtime = $_POST['birthtime'];

    // Pythonスクリプトを呼び出す
    $command = escapeshellcmd("python3 test.py \"$birthplace\" \"$birthtime\"");
    $output = shell_exec($command);

    // 結果を表示
    echo "<h1>計算結果</h1>";
    echo "<p>出生地: " . htmlspecialchars($birthplace) . "</p>";
    echo "<p>出生時刻: " . htmlspecialchars($birthtime) . "</p>";
    echo "<p>黄経: " . htmlspecialchars($output) . "</p>";
} else {
    echo "不正なリクエストです。";
}
?>
