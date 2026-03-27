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
#pip install termcolor requests

# Run basic reconnaissance
python all_in_one.py -t example.com --recon

# Run subdomain enumeration
python all_in_one.py -t target.com --subdomain

# Run full analysis with scope checking
python all_in_one.py -t example.com --scope-file scope.txt --all

# Generate JSON report
python all_in_one.py -t target.com --all --report json

# Access educational content
python all_in_one.py --education

# Use AI assistant
python all_in_one.py -t example.com --ai-assistant

# DO THIS BEORE DOING SCAN
#chmod +x Allone.py




