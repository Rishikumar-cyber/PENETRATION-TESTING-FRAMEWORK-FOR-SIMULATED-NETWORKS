# PENETRATION-TESTING-FRAMEWORK-FOR-SIMULATED-NETWORKS

## Overview
This project is a *Penetration Testing Framework* designed for simulated network environments. It is implemented on *Windows* and leverages *Streamlit* to provide an interactive and user-friendly interface for executing various penetration testing modules, including custom and automated exploits.

## Features
- Comprehensive penetration testing modules  
- Custom exploit scripts tailored for the Windows environment  
- Automation support for repetitive testing tasks  
- Interactive web UI powered by Streamlit (running at localhost:8502)  
- Modular design to easily extend with new exploits  

## Installation

### Prerequisites
- Windows OS  
- Python 3.8 or higher  
- [Streamlit](https://streamlit.io/)  
- Required Python packages (listed in requirements.txt)  

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Rishikumar-cyber/penetration-testing-framework.git
   cd penetration-testing-framework
   ```
2. Install dependencies:
   ``` bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage
- Launch the app with Streamlit.  
- Use the sidebar or buttons to navigate through the modules.  
- Select any exploit or scan, and execute it in one click.  
- Results and logs are displayed on the interface in real-time.

## Screenshots

### Nmap Scanning Result
![Nmap Output](screenshots/nmap_result.png)

### Exploit Interface
![Exploit Interface](screenshots/exploit_interface.png)

### Final Project Report (UI Preview)
![Report Screenshot](screenshots/final_report_ui.png)



## Project Info
This project was developed as part of a final-year major project (2021–2025) titled:  
*"Design and Implementation of a Penetration Testing Framework for Simulated Networks"*.

## License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
