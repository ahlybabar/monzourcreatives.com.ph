<?php
/**
 * Monzour Creatives — Contact Form Handler (PHPMailer + Native Fallback)
 * Delivers inquiries to monzourcreatives@gmail.com and returns JSON.
 */

declare(strict_types=1);

header('Content-Type: application/json; charset=UTF-8');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['ok' => false, 'error' => 'Method not allowed.']);
    exit;
}

// Honeypot check to silently drop automated spam bots
$honeypot = trim((string)($_POST['website'] ?? ''));
if ($honeypot !== '') {
    echo json_encode(['ok' => true, 'message' => 'Thanks for reaching out!']);
    exit;
}

// Sanitize helper (strips CR/LF to prevent header injection)
$cleanHeader = static function (string $value): string {
    return trim(str_replace(["\r", "\n"], ' ', $value));
};

$firstName = $cleanHeader((string)($_POST['first_name'] ?? ''));
$lastName  = $cleanHeader((string)($_POST['last_name'] ?? ''));
$email     = $cleanHeader((string)($_POST['email'] ?? ''));
$business  = $cleanHeader((string)($_POST['business_name'] ?? ''));
$phone     = $cleanHeader((string)($_POST['phone'] ?? ''));
$service   = $cleanHeader((string)($_POST['service'] ?? 'General Inquiry'));
$message   = trim((string)($_POST['message'] ?? ''));

if ($firstName === '' || $lastName === '' || $message === '' || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    http_response_code(422);
    echo json_encode([
        'ok'    => false,
        'error' => 'Please complete your name, a valid email address, and your message.',
    ]);
    exit;
}

$configPath = __DIR__ . '/mail-config.php';
$config = file_exists($configPath) ? require $configPath : [];

$recipientEmail = $config['recipient_email'] ?? 'monzourcreatives@gmail.com';
$recipientName  = $config['recipient_name'] ?? 'Monzour Creatives';
$smtpHost       = $config['smtp_host'] ?? 'smtp.gmail.com';
$smtpPort       = (int)($config['smtp_port'] ?? 587);
$smtpEncryption = $config['smtp_encryption'] ?? 'tls';
$smtpUser       = $config['smtp_username'] ?? $recipientEmail;
$smtpPass       = (string)($config['smtp_password'] ?? '');

$fullName = trim($firstName . ' ' . $lastName);
$subject  = "New Portfolio Inquiry: {$service} — {$fullName}";

$esc = static fn(string $v): string => htmlspecialchars($v, ENT_QUOTES, 'UTF-8');

$htmlBody = '
<div style="font-family: -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif; color: #181A20; max-width: 600px; line-height: 1.6;">
  <h2 style="margin: 0 0 12px; color: #D95B38;">New Client Inquiry — Monzour Creatives</h2>
  <table style="width: 100%; border-collapse: collapse; margin-bottom: 16px;">
    <tr><td style="padding: 6px 0; font-weight: 600; width: 130px;">Name:</td><td>' . $esc($fullName) . '</td></tr>
    <tr><td style="padding: 6px 0; font-weight: 600;">Email:</td><td><a href="mailto:' . $esc($email) . '">' . $esc($email) . '</a></td></tr>
    <tr><td style="padding: 6px 0; font-weight: 600;">Business:</td><td>' . $esc($business !== '' ? $business : 'Not provided') . '</td></tr>
    <tr><td style="padding: 6px 0; font-weight: 600;">Phone:</td><td>' . $esc($phone !== '' ? $phone : 'Not provided') . '</td></tr>
    <tr><td style="padding: 6px 0; font-weight: 600;">Service:</td><td>' . $esc($service !== '' ? $service : 'General Inquiry') . '</td></tr>
  </table>
  <div style="padding: 14px 16px; background: #F6F5F1; border-left: 3px solid #D95B38; border-radius: 6px;">
    <strong>Message:</strong><br>' . nl2br($esc($message)) . '
  </div>
</div>';

$plainBody = "New Client Inquiry — Monzour Creatives\n"
    . "=====================================\n"
    . "Name:     {$fullName}\n"
    . "Email:    {$email}\n"
    . "Business: " . ($business !== '' ? $business : 'Not provided') . "\n"
    . "Phone:    " . ($phone !== '' ? $phone : 'Not provided') . "\n"
    . "Service:  " . ($service !== '' ? $service : 'General Inquiry') . "\n\n"
    . "Message:\n{$message}\n";

$autoloadPath = __DIR__ . '/vendor/autoload.php';

// Primary path: PHPMailer via Gmail SMTP when App Password is configured
if (file_exists($autoloadPath) && $smtpPass !== '') {
    require_once $autoloadPath;

    try {
        $mail = new \PHPMailer\PHPMailer\PHPMailer(true);
        $mail->isSMTP();
        $mail->Host       = $smtpHost;
        $mail->SMTPAuth   = true;
        $mail->Username   = $smtpUser;
        $mail->Password   = $smtpPass;
        $mail->SMTPSecure = $smtpEncryption === 'ssl'
            ? \PHPMailer\PHPMailer\PHPMailer::ENCRYPTION_SMTPS
            : \PHPMailer\PHPMailer\PHPMailer::ENCRYPTION_STARTTLS;
        $mail->Port       = $smtpPort;
        $mail->CharSet    = 'UTF-8';

        $mail->setFrom($smtpUser, $recipientName);
        $mail->addAddress($recipientEmail, $recipientName);
        $mail->addReplyTo($email, $fullName);

        $mail->isHTML(true);
        $mail->Subject = $subject;
        $mail->Body    = $htmlBody;
        $mail->AltBody = $plainBody;

        $mail->send();
        echo json_encode([
            'ok'      => true,
            'message' => 'Message sent! I will reply within 24 hours.',
        ]);
        exit;
    } catch (\Throwable $e) {
        http_response_code(500);
        echo json_encode([
            'ok'    => false,
            'error' => 'Could not deliver via SMTP right now. Please email monzourcreatives@gmail.com directly.',
        ]);
        exit;
    }
}

// Secondary path: native PHP mail() when hosted on a server with sendmail configured
$headers = [
    'MIME-Version: 1.0',
    'Content-Type: text/plain; charset=UTF-8',
    "From: {$recipientName} <{$recipientEmail}>",
    "Reply-To: {$fullName} <{$email}>",
    'X-Mailer: PHP/' . PHP_VERSION,
];

$sent = @mail($recipientEmail, $subject, $plainBody, implode("\r\n", $headers));
if ($sent) {
    echo json_encode([
        'ok'      => true,
        'message' => 'Message sent! I will reply within 24 hours.',
    ]);
    exit;
}

// Clear actionable message if local XAMPP has neither SMTP password nor sendmail set up
http_response_code(503);
echo json_encode([
    'ok'             => false,
    'needs_smtp_key' => ($smtpPass === ''),
    'error'          => 'Mail server is not configured yet (add your Gmail App Password in mail-config.php).',
]);
