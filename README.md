# 🛰️ SubDNS-UI

**SubDNS-UI** is a powerful and elegant **Subdomain + DNS Enumeration Tool** built with Python and Streamlit. It helps you discover active subdomains and gather DNS records (A, MX, TXT, CNAME, etc.) — with real-time display and Markdown report generation.

> 🚀 Created by [Rajkumar Kumawat](https://www.linkedin.com/in/rajkumarkumawat.workup) | © 2025

---

## 🌟 Features

- 🔍 Brute-force **Subdomain Enumeration**
- 🌐 DNS Record Resolution: `A`, `MX`, `TXT`, `CNAME`, `SOA`, `AAAA`
- 🧠 Multithreaded for fast subdomain checks
- 📄 Generates clean **Markdown Reports**
- 🎨 Clean and responsive **Streamlit UI**
- ☁️ Download report directly from the browser
- 🛡️ Ideal for Recon, Bug Bounties, Red Teaming

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Rjkumarkumawat/subdns-ui.git
cd subdns-ui
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit requests dnspython
```

### 3. Run the Tool

```bash
streamlit run app.py
```

---

## 🧾 Folder Structure

```
subdns-ui/
├── app.py                 # Streamlit UI
├── unified_enum.py        # Backend logic for recon
├── subdomains.txt         # Wordlist for brute-force
├── reports/               # Markdown reports will be saved here
└── README.md
```

---

## ⚙️ Sample Wordlist (`subdomains.txt`)

```text
www
mail
ftp
dev
api
admin
test
vpn
cdn
blog
```

You can replace it with your own custom list for deeper enumeration.

---

## 📄 Sample Output

Markdown report saved in `reports/` folder:

```markdown
# Recon Report for `example.com`
_Generated on 2025-07-24 20:10:12_

## 🛰️ Discovered Subdomains
- http://www.example.com
- http://mail.example.com

## 🌐 DNS Records

### A Records
- 93.184.216.34

### MX Records
- aspmx.l.google.com.

### TXT Records
- v=spf1 include:_spf.google.com ~all
```

---

## 👨‍💻 Author

**Rajkumar Kumawat**

- 💼 [LinkedIn](https://www.linkedin.com/in/rajkumar-kumawat-66072b199/)
- ✍️ [Medium](https://medium.com/@rajkumarkumawat.workup)
- 🛠️ [GitHub](https://github.com/Rjkumarkumawat/)

---

## 📜 License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## ⭐ Star This Project!

If you find this project helpful, consider giving it a ⭐ on GitHub to show support and help others discover it.
