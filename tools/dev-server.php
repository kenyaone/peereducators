<?php
/**
 * Local preview router for Peer Educator.
 *
 * Emulates the Apache config in setup/install-peereducator.sh so the app can
 * be run without root:
 *
 *   php -S 127.0.0.1:8080 -t . tools/dev-server.php
 *
 * This is a PREVIEW ONLY. The real deployment uses Apache + the aliases in
 * conf-available/peereducator.conf. Anything relying on .htaccess, mod_rewrite
 * or Apache-level access control is approximated here, not reproduced.
 */

$root = dirname(__DIR__);
$base = '/peereducator';

$uri = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH) ?: '/';
$uri = rawurldecode($uri);

// Convenience: land on the app from the server root.
if ($uri === '/' || $uri === '') {
    header('Location: ' . $base . '/');
    exit;
}
if ($uri === $base) {
    header('Location: ' . $base . '/');
    exit;
}
if (strpos($uri, $base . '/') !== 0) {
    http_response_code(404);
    echo "Not part of the Peer Educator app. Try $base/";
    exit;
}

$path = substr($uri, strlen($base) + 1);   // "", "admin/dashboard", "css/style.css" ...

// ── static file helper ────────────────────────────────────────────────
function serve(string $file): bool {
    if (!is_file($file)) return false;
    $ext = strtolower(pathinfo($file, PATHINFO_EXTENSION));
    $types = [
        'html' => 'text/html; charset=UTF-8', 'htm' => 'text/html; charset=UTF-8',
        'css' => 'text/css', 'js' => 'application/javascript',
        'json' => 'application/json', 'webmanifest' => 'application/manifest+json',
        'png' => 'image/png', 'jpg' => 'image/jpeg', 'jpeg' => 'image/jpeg',
        'gif' => 'image/gif', 'svg' => 'image/svg+xml', 'ico' => 'image/x-icon',
        'pdf' => 'application/pdf', 'mp4' => 'video/mp4', 'webm' => 'video/webm',
        'woff' => 'font/woff', 'woff2' => 'font/woff2', 'ttf' => 'font/ttf',
    ];
    header('Content-Type: ' . ($types[$ext] ?? 'application/octet-stream'));
    header('Content-Length: ' . filesize($file));
    readfile($file);
    return true;
}

// ── deny what Apache denies ───────────────────────────────────────────
// includes/ is blocked, and data/ is blocked except data/uploads/.
if (preg_match('#^includes(/|$)#', $path)
    || (preg_match('#^data/#', $path) && !preg_match('#^data/uploads/#', $path))) {
    http_response_code(403);
    echo 'Forbidden';
    exit;
}

// ── Alias /peereducator/uploads and /peereducator/data/uploads ────────
if (preg_match('#^(?:data/)?uploads/(.+)$#', $path, $m)) {
    if (serve($root . '/data/uploads/' . $m[1])) exit;
    http_response_code(404); echo 'Upload not found'; exit;
}

// ── Alias /peereducator/admin and /peereducator/datapost ──────────────
foreach (['admin', 'datapost'] as $area) {
    if ($path === $area || strpos($path, $area . '/') === 0) {
        $rest = ltrim(substr($path, strlen($area)), '/');
        if ($rest !== '' && serve($root . '/' . $area . '/' . $rest)) exit;
        // .htaccess: RewriteBase /peereducator/<area>/ -> index.php?p=$1
        if ($rest !== '' && $rest !== 'index.php') {
            $_GET['p'] = $rest;
            $_REQUEST['p'] = $rest;
        }
        $_SERVER['SCRIPT_NAME']     = $base . '/' . $area . '/index.php';
        $_SERVER['SCRIPT_FILENAME'] = $root . '/' . $area . '/index.php';
        require $root . '/' . $area . '/index.php';
        exit;
    }
}

// ── Everything else is the public site ────────────────────────────────
if ($path !== '' && serve($root . '/public/' . $path)) exit;

// .htaccess: RewriteBase /peereducator/ -> index.php?p=$1
if ($path !== '' && $path !== 'index.php' && !isset($_GET['p'])) {
    $_GET['p'] = $path;
    $_REQUEST['p'] = $path;
}
$_SERVER['SCRIPT_NAME']     = $base . '/index.php';
$_SERVER['SCRIPT_FILENAME'] = $root . '/public/index.php';
require $root . '/public/index.php';
