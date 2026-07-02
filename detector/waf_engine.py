from rules.attack_signatures import attack_patterns
from datetime import datetime

# Track attacks by IP
ip_attack_count = {}


def log_attack(ip_address, attack_type, payload):

    with open("logs/attack_logs.txt", "a") as file:

        timestamp = datetime.now()

        log_entry = (
            f"[{timestamp}] "
            f"IP: {ip_address} | "
            f"ATTACK DETECTED | "
            f"Type: {attack_type} | "
            f"Payload: {payload}\n"
        )

        file.write(log_entry)


def detect_attack(user_input, ip_address):

    user_input = user_input.lower()

    if ip_address not in ip_attack_count:
        ip_attack_count[ip_address] = 0

    attack_type = None
    matched_pattern = None

    # ---------------- LFI ----------------

    for pattern in attack_patterns["LFI"]:

        if pattern.lower() in user_input:

            attack_type = "LFI"
            matched_pattern = pattern
            break

    # ---------- Directory Traversal ----------

    if attack_type is None:

        for pattern in attack_patterns["Directory Traversal"]:

            if pattern.lower() in user_input:

                attack_type = "Directory Traversal"
                matched_pattern = pattern
                break

    # ---------- SQL Injection ----------

    if attack_type is None:

        for pattern in attack_patterns["SQL Injection"]:

            if pattern.lower() in user_input:

                attack_type = "SQL Injection"
                matched_pattern = pattern
                break

    # ---------- XSS ----------

    if attack_type is None:

        for pattern in attack_patterns["XSS"]:

            if pattern.lower() in user_input:

                attack_type = "XSS"
                matched_pattern = pattern
                break

    # ---------- Command Injection ----------

    if attack_type is None:

        for pattern in attack_patterns["Command Injection"]:

            if pattern.lower() in user_input:

                attack_type = "Command Injection"
                matched_pattern = pattern
                break

    # ---------- Attack Found ----------

    if attack_type:

        ip_attack_count[ip_address] += 1

        log_attack(ip_address, attack_type, user_input)

        if ip_attack_count[ip_address] >= 5:

            return {
                "status": "Abusive",
                "attack_type": attack_type,
                "matched_pattern": matched_pattern,
                "severity": "Critical"
            }

        return {
            "status": "Blocked",
            "attack_type": attack_type,
            "matched_pattern": matched_pattern,
            "severity": "High"
        }

    # ---------- Safe ----------

    return {
        "status": "Safe",
        "attack_type": None,
        "matched_pattern": None,
        "severity": "Low"
    }