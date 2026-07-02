attack_patterns = {

    "SQL Injection": [
        "SELECT",
        "UNION",
        "DROP TABLE",
        "--",
        "' OR '1'='1"
    ],

    "XSS": [
        "<script>",
        "javascript:",
        "onerror="
    ],

    "Directory Traversal": [
        "../",
        "..\\"
    ],

    "LFI": [
        "/etc/passwd",
        "boot.ini",
        "/proc/self/environ",
        "win.ini"
    ],

    "Command Injection": [
        "; ls",
        "; cat",
        "&&",
        "|"
    ]
}