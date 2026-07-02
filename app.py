from flask import Flask, render_template, request, send_file
from detector.waf_engine import detect_attack

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():

    result = None

    total_attacks = 0
    abusive_requests = 0
    safe_requests = 0
    critical_attacks = 0

    attack_summary = {
        "XSS": 0,
        "SQL Injection": 0,
        "Directory Traversal": 0,
        "Command Injection": 0,
        "LFI": 0
    }

    # Handle user input
    if request.method == 'POST':

        user_input = request.form['payload']
        user_ip = request.remote_addr

        result = detect_attack(user_input, user_ip)

        if result["status"] == "Blocked":
            total_attacks += 1

        elif result["status"] == "Abusive":
            abusive_requests += 1

        else:
            safe_requests += 1

    # Read attack logs
    try:

        with open('logs/attack_logs.txt', 'r') as file:

            logs = file.readlines()

            total_attacks = len(logs)

            for log in logs:

                if "XSS" in log:
                    attack_summary["XSS"] += 1

                elif "SQL Injection" in log:
                    attack_summary["SQL Injection"] += 1
                    critical_attacks += 1

                elif "Directory Traversal" in log:
                    attack_summary["Directory Traversal"] += 1

                elif "Command Injection" in log:
                    attack_summary["Command Injection"] += 1

                elif "LFI" in log:
                    attack_summary["LFI"] += 1

    except:
        logs = []

    # Latest first
    logs.reverse()

    # Structured logs for dashboard
    structured_logs = []

    for log in logs:

        if log.strip() == "":
            continue

        parts = log.split("|")

        if len(parts) >= 4:

            structured_logs.append({
                "timestamp": parts[0].strip(),
                "ip": parts[1].strip(),
                "type": parts[2].strip(),
                "payload": parts[3].strip()
            })

    return render_template(
        'index.html',
        result=result,
        logs=logs,
        total_attacks=total_attacks,
        abusive_requests=abusive_requests,
        safe_requests=safe_requests,
        critical_attacks=critical_attacks,
        attack_summary=attack_summary,
        structured_logs=structured_logs,
        latest_attack=result["attack_type"] if result else "None",
        system_health="Protected"
    )


@app.route('/download-report')
def download_report():

    try:
        with open('logs/attack_logs.txt', 'r') as logs:
            log_data = logs.read()

    except:
        log_data = "No logs available."

    report_path = "reports/security_report.txt"

    with open(report_path, "w") as report:

        report.write("SENTINELSHIELD SECURITY REPORT\n")
        report.write("=" * 50 + "\n\n")
        report.write(log_data)

    return send_file(report_path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)