# app.py

import streamlit as st
from unified_enum import enumerate_subdomains, enumerate_dns, generate_markdown
import os

# ----------------------------
# 🌟 Page Config & Styling
# ----------------------------
st.set_page_config(
    page_title="SubDNS-UI - Recon Scanner",
    page_icon="🛰️",
    layout="centered",
)

st.markdown("""
    <style>
    .big-title {
        font-size: 40px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
        margin-top: -30px;
    }
    .subtext {
        text-align: center;
        font-size: 18px;
        color: #777777;
    }
    .footer {
        font-size: 14px;
        text-align: center;
        margin-top: 50px;
        color: gray;
    }
    .stButton>button {
        background-color: #1E88E5;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5em 2em;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# 🛰️ Header
# ----------------------------
st.markdown('<div class="big-title">🛰️ SubDNS-UI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext">Advanced Subdomain & DNS Enumerator with Reporting</div>', unsafe_allow_html=True)
st.markdown("---")

# ----------------------------
# 🚀 User Input
# ----------------------------
domain = st.text_input("🌐 Enter Domain (e.g., `example.com`)")

if st.button("🚀 Start Recon") and domain:
    st.info("🔍 Enumerating subdomains...")
    subs = enumerate_subdomains(domain)

    if subs:
        st.success(f"✅ Found {len(subs)} active subdomain(s):")
        st.code("\n".join([f"http://{s}" for s in subs]), language="bash")
    else:
        st.warning("❌ No active subdomains found.")

    st.info("🌐 Resolving DNS records...")
    records = enumerate_dns(domain)

    st.success("✅ DNS Enumeration Complete.")
    st.markdown("### 🌐 DNS Records Found:")

    for record_type, values in records.items():
        with st.expander(f"🔎 {record_type} Records ({len(values)})"):
            if values:
                for v in values:
                    st.markdown(f"- `{v}`")
            else:
                st.markdown("*No records found*")

    st.info("📝 Generating Markdown report...")
    report_path = generate_markdown(domain)

    st.success("🎉 Report generated successfully!")

    with open(report_path, 'r') as file:
        st.download_button(
            label="📄 Download Markdown Report",
            data=file.read(),
            file_name=f"{domain}.md",
            mime="text/markdown"
        )

elif domain == "":
    st.warning("⚠️ Please enter a valid domain.")

# ----------------------------
# 📢 Footer Credit
# ----------------------------
st.markdown("""
    <div class="footer">
        🚀 Created by <strong>Rajkumar Kumawat</strong> | Tool: <em>SubDNS-UI</em> | &copy; 2025<br>
        Connect on <a href="https://www.linkedin.com/in/rajkumar-kumawat-66072b199/" target="_blank">LinkedIn</a> or read tutorials on <a href="https://medium.com/@rajkumarkumawat.workup" target="_blank">Medium</a>
    </div>
""", unsafe_allow_html=True)

