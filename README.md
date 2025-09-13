# AutoPent – Automated Penetration Testing Framework

## Overview

**AutoPent** is an **AI-powered penetration testing framework** designed to automate the complete security testing lifecycle.
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

AutoPent isn't just another security tool; it is a **first-of-its-kind framework** that fundamentally redefines automated offensive security. It bridges the critical gap between static scanning and dynamic, intelligent analysis, creating a new category of security tooling.

*   **True End-to-End Integration:** While most tools focus on one phase (like scanning or reporting), AutoPent is the only framework that seamlessly integrates the entire workflow: from initial reconnaissance and multi-layered scanning to automated exploitation, privilege escalation, and AI-driven reporting.

*   **AI-Powered Decision Making:** This is what makes AutoPent truly unique. It is the first open-source framework to embed a powerful Large Language Model (**LLaMA 3.1**) at its core. It doesn't just find vulnerabilities; it *understands* them in context, prioritizes risks, and generates actionable remediation strategies that go far beyond static rule-based outputs.

*   **From Data Overload to Actionable Intelligence:** Traditional tools produce thousands of lines of output, leaving the analysis to the user. AutoPent’s AI engine processes this raw data, correlates findings from different modules, and delivers a prioritized list of credible, exploitable threats. It transforms noise into clear, actionable intelligence.

*   **A Unified Command Center:** By integrating a powerful backend with an intuitive **PyQt5 GUI**, AutoPent provides a single, unified dashboard for orchestrating complex penetration tests. This makes advanced security testing accessible without forcing users to master a dozen different command-line tools and manually manage their outputs.

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

## Roadmap

* [ ] Cloud Infrastructure Security Module
* [ ] Real-time Threat Intelligence Integration
* [ ] Mobile App Pentesting Support
* [ ] Multi-user Collaboration Dashboard

---

## Contributors

* **Abhinav Mehra** – Project Lead & Developer
* **Himanshu Gaur**
* **Tanya Bharti**
* **Rananjay Singh Chauhan**
* Metaversity Club @ VIT Bhopal