import os

# Metasploit RPC Configuration
METASPLOIT_RPC_HOST = os.getenv("METASPLOIT_RPC_HOST", "127.0.0.1")
METASPLOIT_RPC_PORT = int(os.getenv("METASPLOIT_RPC_PORT", 55552))
METASPLOIT_RPC_PASS = os.getenv("METASPLOIT_RPC_PASS", "abhinav2004")

# Attack Machine Details
LHOST = os.getenv("LHOST", "172.25.162.99")
LPORT = int(os.getenv("LPORT", 4444))  # Reverse shell listener port

# API Keys for Reconnaissance
SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")
BINARYEDGE_API_KEY = os.getenv("BINARYEDGE_API_KEY")
ONYPHE_API_KEY = os.getenv("ONYPHE_API_KEY")

# File Paths for Privilege Escalation Scripts
LINPEAS_PATH = os.getenv("LINPEAS_PATH", "/app/scripts/linpeas.sh")
WINPEAS_PATH = os.getenv("WINPEAS_PATH", "/app/scripts/winPEASany.exe")

# AI Model Path (LLaMA)
LLAMA_MODEL_PATH = os.getenv("DEEPSEEK_MODEL_PATH", "/app/models/blobs/sha256-ff82381e2bea77d91c1b824c7afb83f6fb73e9f7de9dda631bcdbca564aa5435")

# Haiku API Configuration
HAIKU_API_KEY = os.getenv("HAIKU_API_KEY")
HAIKU_API_URL = os.getenv("HAIKU_API_URL", "https://api.haikuscanner.com/v1/scan")

print("all is working")