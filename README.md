# AutoPent – Automated Penetration Testing Framework

## Overview

**AutoPent** is a **one of its kind, AI-powered penetration testing framework** designed to automate the complete security testing lifecycle.
It combines **reconnaissance, vulnerability scanning, exploitation, privilege escalation, AI-driven analysis, and automated reporting** into a single integrated platform.

Unlike traditional tools, AutoPent leverages **LLM (LLaMA 3.1)** to provide intelligent recommendations, generate remediation steps, and analyze vulnerabilities dynamically.

---

## Key Features

* **Automated Reconnaissance** – Domain, subdomain, and service discovery.
* **Vulnerability Scanning** – Automated scans using Nmap, OpenVAS, and custom scripts.
* **Exploitation Engine** – Metasploit-based automated exploitation with controlled payloads.
* **Privilege Escalation** – Post-exploitation privilege escalation & persistence detection.
* **AI Security Analysis** – LLaMA 3.1 for intelligent vulnerability assessment & mitigation strategies.
* **Automated Reports** – Professional, compliance-ready PDF/HTML reports.
* **Interactive GUI** – PyQt5-based dashboard for intuitive control and monitoring.

---

## The AutoPent Advantage: A New Paradigm in Security

# Key Features of AutoPent

AutoPent is a first-of-its-kind framework that redefines automated offensive security. 

* **First-of-its-Kind Framework:**
    It introduces a new category of security tooling by bridging the gap between static scanning and dynamic, intelligent analysis.

* **True End-to-End Integration:**
    AutoPent is a single, seamless framework that manages the entire offensive security workflow, including:
    * Reconnaissance
    * Multi-layered scanning
    * Automated exploitation
    * Privilege escalation
    * AI-driven reporting

* **AI-Powered Decision Making:**
    It is the first open-source framework to use a Large Language Model (LLaMA 3.1) at its core. This allows it to:
    * **Understand** vulnerabilities in context.
    * Prioritize risks intelligently.
    * Generate actionable remediation strategies.

* **From Data to Intelligence:**
    The AI engine processes raw scan data and correlates findings to transform security "noise" into a clear, prioritized list of exploitable threats.

* **Unified Command Center:**
    It features an intuitive PyQt5 GUI that acts as a single dashboard for managing complex penetration tests, making advanced security accessible without juggling multiple command-line tools.

---

## Tech Stack

* **Languages:** Python 3.11
* **Frameworks:** PyQt5, Flask (for backend APIs)
* **Libraries:**

  * Recon: `scapy`, `sublist3r`, `shodan`
  * Scanning: `nmap`, `openvas_lib`
  * Exploitation: `msfrpc`, `pwntools`
  * AI/ML: `transformers`, `llama-index`, `langchain`
  * Reporting: `reportlab`, `jinja2`, `pdfkit`
* **Databases:** SQLite for session & scan data
* **AI Model:** **LLaMA 3.1** for contextual security insights

---

## Methodology

1. **Reconnaissance** → Automated target mapping
2. **Vulnerability Scanning** → Weakness identification
3. **Exploitation & Privilege Escalation** → Automated attack simulation
4. **AI Analysis** → Risk evaluation & patch recommendation
5. **Reporting** → Compliance-ready documentation

---

## Why AutoPent?

| Feature                     | Existing Tools | AutoPent      |
| --------------------------- | -------------- | ------------- |
| Recon & Scanning            | ✔              | ✔             |
| Exploitation                | Limited        | ✔ Automated   |
| Privilege Escalation        | Manual         | ✔ Automated   |
| AI-Driven Security Insights | ❌              | ✔ (LLaMA 3.1) |
| Integrated GUI              | ❌              | ✔             |
| End-to-End Automation       | ❌              | ✔             |

---

## Getting Started

Follow these steps to get a local copy up and running.

### Prerequisites

*   Python 3.x
*   External tools like `nmap`, `nikto`, and `sqlmap` should be installed and available in your system's PATH.

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/Abhinavmehra2004/CyberShield-Hakathon-Autopenters-.git
    ```

2.  **Navigate to the source code directory:**
    ```sh
    cd CyberShield-Hakathon-Autopenters-/SourceCode
    ```

3.  **Create and activate a virtual environment (recommended):**
    ```sh
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

4.  **Install the required Python packages:**
    ```sh
    pip install -r requirements.txt
    ```

---

## Usage

1.  **Run the application from the `SourceCode` directory:**
    ```sh
    python autopent.py
    ```

2.  **Enter the target URL** in the input field (e.g., `http://example.com`).

3.  **Click the "Start Security Test" button** to begin the automated penetration test.

4.  The progress will be displayed in the text area. Once the test is complete, you can **download the final report** using the "Download Report" button.

---

## Use Cases

* **Cyber Forensics & Incident Response**
* **Enterprise Security Audits**
* **Government & Law Enforcement Cyber Operations**
* **Education & Training in Ethical Hacking**

---

## Disclaimer

AutoPent is developed **strictly for ethical and authorized penetration testing**.
Unauthorized usage against systems without explicit permission is **illegal** and punishable under **Indian IT Act (2000/2008 amendments)** and global cybercrime laws.

---

## Future Scope

* [ ] Cloud Infrastructure Security Module
* [ ] Real-time Threat Intelligence Integration
* [ ] Mobile App Pentesting Support
* [ ] Multi-user Collaboration Dashboard

---

## Contributors

* **Abhinav Mehra (23BCY10015)**
* **Himanshu Gaur (23BCY10127)**
* **Tanya Bharti (23BCE11555)**
* **Rananjay Singh Chauhan (23BAI10080)**
