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
