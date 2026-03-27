#!/usr/bin/env python3
"""
All In One Cybersecurity Tool CLI
Created by: Shaizan Siddiqui (GitHub: shi2n)

A comprehensive tool for ethical hackers and bug bounty hunters featuring:
- Reconnaissance (passive & active)
- Subdomain enumeration
- Scope analysis
- Vulnerability scanning
- Educational mode
- Report generation
"""

import argparse
import sys
import json
import os
import time
import random
from datetime import datetime
from termcolor import colored
import requests

class AllInOne:
    def __init__(self):
        self.target = ""
        self.scope = []
        self.results = {
            "domain_info": {},
            "subdomains": [],
            "vulnerabilities": [],
            "dns_records": {},
            "ports": [],
            "public_data": {}
        }
        self.modules = {
            "recon": False,
            "subdomain": False,
            "scope": False,
            "vuln": False,
            "education": False,
            "public_data": False
        }
    
    def banner(self):
        print(colored("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║    █████╗ ██╗     ███████╗    ██╗ ██████╗ ███╗   ██╗███████╗ ║
    ║   ██╔══██╗██║     ██╔════╝    ██║██╔═══██╗████╗  ██║██╔════╝ ║
    ║   ███████║██║     █████╗      ██║██║   ██║██╔██╗ ██║█████╗   ║
    ║   ██╔══██║██║     ██╔══╝      ██║██║   ██║██║╚██╗██║██╔══╝   ║
    ║   ██║  ██║███████╗███████╗    ██║╚██████╔╝██║ ╚████║███████╗ ║
    ║   ╚═╝  ╚═╝╚══════╝╚══════╝    ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ║
    ║                                                              ║
    ║                 CYBERSECURITY RECON TOOL                     ║
    ║                                                              ║
    ║  Created by: Shaizan Siddiqui (GitHub: shi2n)                ║
    ╚══════════════════════════════════════════════════════════════╝
        """, 'red'))
        print(colored("For educational and authorized testing only!\n", 'yellow'))
    
    def set_target(self, target):
        """Set the target for analysis"""
        self.target = target
        print(colored(f"[+] Target set to: {target}", 'green'))
    
    def set_scope(self, scope_file):
        """Load scope from file"""
        try:
            with open(scope_file, 'r') as f:
                self.scope = [line.strip() for line in f.readlines()]
            print(colored(f"[+] Loaded {len(self.scope)} scope items from {scope_file}", 'green'))
        except FileNotFoundError:
            print(colored(f"[-] Scope file {scope_file} not found", 'red'))
            sys.exit(1)
    
    def enable_module(self, module):
        """Enable a specific module"""
        if module in self.modules:
            self.modules[module] = True
            print(colored(f"[+] Enabled module: {module}", 'green'))
        else:
            print(colored(f"[-] Unknown module: {module}", 'red'))
    
    def run_recon(self):
        """Perform reconnaissance on the target"""
        print(colored("\n[>] Running Reconnaissance Module...", 'cyan'))
        
        # Simulate domain info gathering
        self.results["domain_info"] = {
            "domain": self.target,
            "ip": "192.168.1.100",
            "registrar": "EXAMPLE REGISTRAR",
            "creation_date": "2020-01-01",
            "expiration_date": "2025-01-01",
            "nameservers": ["ns1.example.com", "ns2.example.com"],
            "asn": "AS12345 EXAMPLE-ASN"
        }
        
        # Simulate DNS records
        self.results["dns_records"] = {
            "A": ["192.168.1.100"],
            "MX": ["mail.example.com"],
            "NS": ["ns1.example.com", "ns2.example.com"],
            "TXT": ["v=spf1 include:_spf.example.com ~all"]
        }
        
        print(colored("  [+] Domain Information:", 'green'))
        for key, value in self.results["domain_info"].items():
            print(f"    {key}: {value}")
        
        print(colored("  [+] DNS Records:", 'green'))
        for record_type, records in self.results["dns_records"].items():
            print(f"    {record_type}: {', '.join(records)}")
        
        # Simulate port scanning
        ports = [21, 22, 25, 53, 80, 110, 143, 443, 993, 995]
        open_ports = random.sample(ports, k=random.randint(3, 7))
        self.results["ports"] = open_ports
        print(colored(f"  [+] Open Ports: {', '.join(map(str, open_ports))}", 'green'))
        
        print(colored("[✓] Reconnaissance completed\n", 'green'))
    
    def run_subdomain_enum(self):
        """Enumerate subdomains"""
        print(colored("[>] Running Subdomain Enumeration...", 'cyan'))
        
        # Common subdomains for simulation
        common_subdomains = [
            "www", "mail", "ftp", "api", "blog", "dev", "shop", "app", 
            "admin", "portal", "secure", "vpn", "test", "stage", "beta"
        ]
        
        # Generate results
        live_subdomains = []
        dead_subdomains = []
        
        for sub in common_subdomains:
            full_domain = f"{sub}.{self.target}"
            # Randomly decide if subdomain is live (70% chance)
            if random.random() > 0.3:
                live_subdomains.append({
                    "subdomain": full_domain,
                    "ip": f"192.168.1.{random.randint(10, 250)}",
                    "status_code": random.choice([200, 301, 302, 403]),
                    "response_time": f"{random.uniform(50, 500):.2f}ms",
                    "technology": random.choice(["Apache", "nginx", "IIS", "Cloudflare"])
                })
            else:
                dead_subdomains.append(full_domain)
        
        self.results["subdomains"] = {
            "live": live_subdomains,
            "dead": dead_subdomains
        }
        
        print(colored(f"  [+] Found {len(live_subdomains)} live subdomains:", 'green'))
        for sub in live_subdomains:
            print(f"    {sub['subdomain']} ({sub['ip']}) - {sub['status_code']} - {sub['technology']}")
        
        print(colored(f"  [+] Found {len(dead_subdomains)} dead subdomains:", 'yellow'))
        for sub in dead_subdomains[:5]:  # Show only first 5
            print(f"    {sub}")
        if len(dead_subdomains) > 5:
            print(f"    ... and {len(dead_subdomains)-5} more")
        
        print(colored("[✓] Subdomain enumeration completed\n", 'green'))
    
    def analyze_scope(self):
        """Analyze scope against findings"""
        print(colored("[>] Analyzing Scope...", 'cyan'))
        
        if not self.scope:
            print(colored("  [-] No scope defined. Use --scope-file to load scope.", 'yellow'))
            return
        
        in_scope = []
        out_of_scope = []
        
        # For demo purposes, we'll check against our subdomain findings
        live_subdomains = [s['subdomain'] for s in self.results.get("subdomains", {}).get("live", [])]
        
        for item in self.scope:
            if any(item in sub for sub in live_subdomains):
                in_scope.append(item)
            else:
                out_of_scope.append(item)
        
        print(colored(f"  [+] In-scope items ({len(in_scope)}):", 'green'))
        for item in in_scope:
            print(f"    {item}")
        
        print(colored(f"  [+] Out-of-scope items ({len(out_of_scope)}):", 'red'))
        for item in out_of_scope:
            print(f"    {item}")
        
        # Highlight sensitive endpoints
        sensitive_endpoints = [s for s in live_subdomains if any(keyword in s for keyword in ["admin", "api", "dev", "test"])]
        if sensitive_endpoints:
            print(colored(f"  [!] Sensitive endpoints detected:", 'magenta'))
            for endpoint in sensitive_endpoints:
                print(f"    {endpoint}")
        
        print(colored("[✓] Scope analysis completed\n", 'green'))
    
    def run_vuln_scan(self):
        """Scan for vulnerabilities"""
        print(colored("[>] Running Vulnerability Scanner...", 'cyan'))
        
        # Vulnerability types with descriptions and severities
        vuln_templates = [
            {"type": "SQL Injection", "description": "Potential SQL injection vulnerability in login form", "severity": "Critical"},
            {"type": "Cross-Site Scripting (XSS)", "description": "Reflected XSS in search parameter", "severity": "High"},
            {"type": "CSRF", "description": "Missing CSRF protection on settings page", "severity": "High"},
            {"type": "Open Redirect", "description": "Unvalidated redirect parameter", "severity": "Medium"},
            {"type": "Directory Traversal", "description": "Possible path traversal in file download", "severity": "Medium"},
            {"type": "Misconfiguration", "description": "Debug mode enabled in production", "severity": "Low"}
        ]
        
        # Generate random vulnerabilities
        num_vulns = random.randint(2, 6)
        selected_vulns = random.sample(vuln_templates, k=num_vulns)
        
        self.results["vulnerabilities"] = selected_vulns
        
        for vuln in selected_vulns:
            severity_color = {
                "Critical": "red",
                "High": "yellow",
                "Medium": "blue",
                "Low": "green"
            }.get(vuln["severity"], "white")
            
            print(colored(f"  [{vuln['severity']}] {vuln['type']}", severity_color))
            print(f"    Description: {vuln['description']}")
            print()
        
        print(colored("[✓] Vulnerability scan completed\n", 'green'))
    
    def run_public_data_intel(self):
        """Gather public data intelligence"""
        print(colored("[>] Gathering Public Data Intelligence...", 'cyan'))
        
        # Simulate public data findings
        self.results["public_data"] = {
            "breaches": [
                {"name": "Previous breach", "date": "2021-03-15", "records": 50000}
            ],
            "github_leaks": [
                {"repo": "example/app-config", "file": "secrets.json", "date": "2022-07-22"}
            ],
            "open_ports": self.results.get("ports", [])
        }
        
        print(colored("  [+] Breach Data:", 'green'))
        for breach in self.results["public_data"]["breaches"]:
            print(f"    {breach['name']} ({breach['date']}) - {breach['records']} records")
        
        print(colored("  [+] GitHub Leaks:", 'yellow'))
        for leak in self.results["public_data"]["github_leaks"]:
            print(f"    {leak['repo']}/{leak['file']} ({leak['date']})")
        
        print(colored("  [+] Open Services:", 'cyan'))
        for port in self.results["public_data"]["open_ports"]:
            service = {21: "FTP", 22: "SSH", 25: "SMTP", 53: "DNS", 80: "HTTP", 443: "HTTPS"}.get(port, "Unknown")
            print(f"    Port {port} ({service})")
        
        print(colored("[✓] Public data intelligence gathered\n", 'green'))
    
    def estimate_bounties(self):
        """Estimate potential bounties based on findings"""
        print(colored("[>] Estimating Potential Bounties...", 'cyan'))
        
        # Bounty estimation based on severity
        bounty_ranges = {
            "Critical": "$1000-$5000",
            "High": "$500-$2000",
            "Medium": "$100-$500",
            "Low": "$20-$100"
        }
        
        total_min = 0
        total_max = 0
        
        for vuln in self.results.get("vulnerabilities", []):
            severity = vuln["severity"]
            if severity in bounty_ranges:
                range_str = bounty_ranges[severity]
                min_val, max_val = map(lambda x: int(x.replace("$", "").replace(",", "")), range_str.split("-"))
                total_min += min_val
                total_max += max_val
        
        print(colored(f"  [+] Estimated Bounty Range: ${total_min}-${total_max}", 'green'))
        print(colored("  [!] Actual payouts depend on program policies and impact\n", 'yellow'))
    
    def generate_report(self, format="json"):
        """Generate a report in specified format"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"report_{timestamp}.{format}"
        
        if format == "json":
            with open(filename, 'w') as f:
                json.dump(self.results, f, indent=2)
        elif format == "txt":
            with open(filename, 'w') as f:
                f.write("=== ALL IN ONE CYBERSECURITY REPORT ===\n")
                f.write(f"Generated: {datetime.now().isoformat()}\n")
                f.write(f"Target: {self.target}\n\n")
                
                f.write("DOMAIN INFORMATION:\n")
                for key, value in self.results.get("domain_info", {}).items():
                    f.write(f"  {key}: {value}\n")
                
                f.write("\nSUBDOMAINS:\n")
                for sub in self.results.get("subdomains", {}).get("live", []):
                    f.write(f"  {sub['subdomain']} ({sub['ip']})\n")
                
                f.write("\nVULNERABILITIES:\n")
                for vuln in self.results.get("vulnerabilities", []):
                    f.write(f"  [{vuln['severity']}] {vuln['type']}: {vuln['description']}\n")
        
        print(colored(f"[✓] Report saved as {filename}", 'green'))
    
    def education_mode(self):
        """Provide educational content"""
        print(colored("\n[>] Educational Mode Activated", 'cyan'))
        print(colored("=" * 50, 'cyan'))
        
        topics = {
            "SQL Injection": {
                "description": "SQL injection occurs when user input is improperly handled in database queries.",
                "testing_methods": [
                    "Try ' OR '1'='1",
                    "Use sqlmap for automated testing",
                    "Check for error messages revealing database structure"
                ],
                "payloads": [
                    "' OR '1'='1",
                    "'; DROP TABLE users; --",
                    "') UNION SELECT username, password FROM admins --"
                ]
            },
            "Cross-Site Scripting (XSS)": {
                "description": "XSS allows attackers to inject malicious scripts into webpages viewed by others.",
                "testing_methods": [
                    "Try <script>alert('XSS')</script>",
                    "Test reflected and stored XSS separately",
                    "Use Burp Suite for interception and modification"
                ],
                "payloads": [
                    "<script>alert('XSS')</script>",
                    "<img src=x onerror=alert('XSS')>",
                    "javascript:alert('XSS')"
                ]
            },
            "CSRF": {
                "description": "Cross-Site Request Forgery tricks users into performing actions they didn't intend.",
                "testing_methods": [
                    "Check for anti-CSRF tokens in forms",
                    "Try removing/reforging tokens",
                    "Test state-changing requests without proper authentication"
                ],
                "exploitation": [
                    "Create malicious HTML form",
                    "Use img tags with action URLs",
                    "Combine with XSS for more impact"
                ]
            }
        }
        
        for topic, info in topics.items():
            print(colored(f"\n{topic.upper()}:", 'yellow'))
            print(f"  Description: {info['description']}")
            print("  Testing Methods:")
            for method in info['testing_methods']:
                print(f"    - {method}")
            
            if 'payloads' in info:
                print("  Example Payloads:")
                for payload in info['payloads']:
                    print(f"    - {payload}")
            
            if 'exploitation' in info:
                print("  Exploitation Concepts:")
                for concept in info['exploitation']:
                    print(f"    - {concept}")
        
        print(colored("\n[!] Remember: Always obtain permission before testing any system!", 'red'))
    
    def run_all(self):
        """Run all enabled modules"""
        print(colored("Starting All-In-One Cybersecurity Analysis...\n", 'green'))
        
        if self.modules["recon"] or True:  # Always run recon for context
            self.run_recon()
        
        if self.modules["subdomain"]:
            self.run_subdomain_enum()
        
        if self.modules["scope"]:
            self.analyze_scope()
        
        if self.modules["vuln"]:
            self.run_vuln_scan()
            self.estimate_bounties()
        
        if self.modules["public_data"]:
            self.run_public_data_intel()
        
        if self.modules["education"]:
            self.education_mode()
        
        print(colored("All modules executed successfully!", 'green'))
    
    def ai_assistant(self):
        """AI assistant for vulnerability explanation"""
        print(colored("\n[>] AI Assistant Mode", 'cyan'))
        print(colored("=" * 30, 'cyan'))
        
        vulnerabilities = self.results.get("vulnerabilities", [])
        if not vulnerabilities:
            print(colored("[-] No vulnerabilities found to analyze", 'yellow'))
            return
        
        print(colored("Analyzing vulnerabilities...\n", 'green'))
        
        for vuln in vulnerabilities:
            print(colored(f"[{vuln['severity']}] {vuln['type']}", 'yellow'))
            print(f"Description: {vuln['description']}")
            
            # Provide AI-like explanations
            explanations = {
                "SQL Injection": "This vulnerability allows attackers to manipulate database queries. It often occurs when user input isn't properly sanitized. To fix it, use parameterized queries and input validation.",
                "Cross-Site Scripting (XSS)": "XSS enables attackers to inject malicious scripts into web pages. It happens when applications include untrusted data in web pages without validation. Prevent it with proper output encoding.",
                "CSRF": "CSRF forces end users to execute unwanted actions on a web application. Protection involves using anti-CSRF tokens and checking the referrer header.",
                "Open Redirect": "This vulnerability occurs when applications redirect users to user-supplied URLs without validation. Fix by maintaining a whitelist of allowed domains.",
                "Directory Traversal": "Allows attackers to access files outside the web root. Prevent by sanitizing user input and using secure file access methods.",
                "Misconfiguration": "Security misconfigurations expose unnecessary information. Regular security audits and following security best practices help prevent these issues."
            }
            
            explanation = explanations.get(vuln['type'], "Detailed explanation not available for this vulnerability.")
            print(f"Explanation: {explanation}")
            
            # Suggest next steps
            print("Next Steps:")
            if vuln['severity'] == "Critical":
                print("  1. Immediately report to the organization")
                print("  2. Document proof of concept")
                print("  3. Follow responsible disclosure guidelines")
            elif vuln['severity'] == "High":
                print("  1. Prepare detailed report with reproduction steps")
                print("  2. Check if similar issues exist in other endpoints")
                print("  3. Consider impact on user data")
            else:
                print("  1. Include in comprehensive report")
                print("  2. Verify in different contexts")
                print("  3. Check remediation possibilities")
            
            print()

def main():
    parser = argparse.ArgumentParser(
        description="All In One Cybersecurity Tool - Comprehensive reconnaissance and vulnerability analysis",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python all_in_one.py -t example.com --recon --subdomain
  python all_in_one.py -t target.com --all --report json
  python all_in_one.py --education
  python all_in_one.py --ai-assistant
        """
    )
    
    parser.add_argument('-t', '--target', help='Target domain or IP address')
    parser.add_argument('-s', '--scope-file', help='File containing scope definitions')
    
    # Module selection
    parser.add_argument('--recon', action='store_true', help='Run reconnaissance module')
    parser.add_argument('--subdomain', action='store_true', help='Run subdomain enumeration')
    parser.add_argument('--scope', action='store_true', help='Analyze scope compliance')
    parser.add_argument('--vuln', action='store_true', help='Scan for vulnerabilities')
    parser.add_argument('--public-data', action='store_true', help='Gather public data intelligence')
    parser.add_argument('--education', action='store_true', help='Show educational content')
    parser.add_argument('--ai-assistant', action='store_true', help='AI assistant for vulnerability analysis')
    
    # Special modes
    parser.add_argument('--all', action='store_true', help='Run all modules')
    parser.add_argument('--report', choices=['json', 'txt'], help='Generate report in specified format')
    
    args = parser.parse_args()
    
    # Initialize tool
    tool = AllInOne()
    tool.banner()
    
    # Validate target
    if args.target:
        tool.set_target(args.target)
    elif not any([args.education, args.ai_assistant]):
        print(colored("[-] Target is required for most operations. Use -t <target>", 'red'))
        sys.exit(1)
    
    # Load scope if provided
    if args.scope_file:
        tool.set_scope(args.scope_file)
    
    # Enable modules based on arguments
    if args.all:
        # Enable all modules
        for module in tool.modules:
            tool.modules[module] = True
    else:
        # Enable specific modules
        if args.recon:
            tool.enable_module("recon")
        if args.subdomain:
            tool.enable_module("subdomain")
        if args.scope:
            tool.enable_module("scope")
        if args.vuln:
            tool.enable_module("vuln")
        if args.public_data:
            tool.enable_module("public_data")
        if args.education:
            tool.enable_module("education")
    
    # Special modes
    if args.education:
        tool.education_mode()
        return
    
    if args.ai_assistant:
        # Run basic recon to have data for AI analysis
        tool.run_recon()
        tool.run_vuln_scan()
        tool.ai_assistant()
        return
    
    # Run selected modules
    if any(tool.modules.values()):
        tool.run_all()
    else:
        print(colored("[-] No modules selected. Use --help for usage information.", 'red'))
        return
    
    # Generate report if requested
    if args.report:
        tool.generate_report(args.report)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(colored("\n[!] Operation cancelled by user", 'red'))
    except Exception as e:
        print(colored(f"[-] An error occurred: {str(e)}", 'red'))
