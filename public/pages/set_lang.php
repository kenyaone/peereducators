<?php
require_once __DIR__ . '/../../includes/config.php';
if (session_status() === PHP_SESSION_NONE) session_start();
$lang = ($_GET['lang'] ?? 'en') === 'sw' ? 'sw' : 'en';
$_SESSION['peer_lang'] = $lang;
header('Location: ' . ($_SERVER['HTTP_REFERER'] ?? '/peereducator/'));
exit;
