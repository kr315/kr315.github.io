<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST["name"];
    $email = $_POST["email"];
    $message = $_POST["message"];
    
    $to = "tomasz@lumistone.pl";
    
    $subject = "Wiadomość ze strony WWW Lumi Stone";
    
    $headers = "From: $email\r\n";
    $headers .= "Reply-To: $email\r\n";
    $headers .= "MIME-Version: 1.0\r\n";
    $headers .= "Content-Type: text/html; charset=UTF-8\r\n";
    
    $message = "<html><body>";
    $message .= "<p><strong>Imię:</strong> $name</p>";
    $message .= "<p><strong>Email:</strong> $email</p>";
    $message .= "<p><strong>Telefon:</strong> $phone</p>";
    $message .= "<p><strong>Wiadomość:</strong><br>$message</p>";
    $message .= "</body></html>";
    
    $success = mail($to, $subject, $message, $headers, "-f tomasz@lumistone.pl");
    
    if ($success) {
        header("Location: sent.html");
        exit;
    } else {
        header("Location: error.html");
        exit;
    }
}
?>