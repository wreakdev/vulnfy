import os, requests

def send_discord(vuln_count: int, report_summary: str, report_fpath: str = None):
    webhook = os.getenv("DISCORD_WEBHOOK_URL")
    if not webhook:
        print("[!] Discord Error: Missing DISCORD_WEBHOOK_URL")
        return False
    
    if vuln_count > 0:
        color = 0xFF0000
        text = f"Found {vuln_count} vulnerabilities"
    else:
        color = 0x00FF00
        text = "No vulnerabilities Found"
        
    payload = {
        "username": "Vulnfy - Vulns Scanner",
        "embeds": [
            {
                "title": "🛡️ Security Scan Results",
                "color": color,
                "description": report_summary,
                "fields": [
                    {
                        "name": "Status",
                        "value": text,
                        "inline": False
                    }
                ]
            }
        ]
    }
    
    try:
        resp = requests.post(webhook, json=payload)
        return resp.status_code in [200, 204]
    except Exception as e:
        print(f"[!] Discord Error: {e}")
        return False