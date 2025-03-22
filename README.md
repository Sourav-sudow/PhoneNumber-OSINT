# 📞 PhoneNumber-OSINT

![GitHub Repo Stars](https://img.shields.io/github/stars/Sourav-sudow/PhoneNumber-OSINT?style=social)
![GitHub Forks](https://img.shields.io/github/forks/Sourav-sudow/PhoneNumber-OSINT?style=social)
![GitHub License](https://img.shields.io/github/license/Sourav-sudow/PhoneNumber-OSINT)

## 🔍 About
**PhoneNumber-OSINT** is a simple Python tool to fetch phone number details using the `phonenumbers` library. This tool helps you retrieve details such as:
- 🌍 Country of the phone number
- 📡 Carrier (Network Provider)
- ⏰ Time zone associated with the number

## 🚀 Features
✅ Easy to use
✅ Lightweight & Fast
✅ Uses `phonenumbers` library for accuracy
✅ Supports multiple countries

## 📦 Installation
Make sure you have **Python 3.6+** installed. Then, clone the repository and install dependencies:
```bash
# Clone this repository
git clone https://github.com/Sourav-sudow/PhoneNumber-OSINT.git
cd PhoneNumber-OSINT

# Install required dependencies
pip install -r requirements.txt
```

## 🛠 Usage
Run the script and enter a phone number with the country code (e.g., `+91XXXXXXXXXX` for India):
```bash
python phone_info.py
```
### 📌 Example Output:
```
🔍 Enter phone number (with country code, e.g., +91XXXXXXXXXX): +14158586273
📞 Phone Number Information:
🌍 Country: United States
📡 Carrier: AT&T Wireless
⏰ Time Zone: America/Los_Angeles
```

## 📜 Requirements
This project requires:
- `phonenumbers` (Phone number parsing & validation)

Install it manually if needed:
```bash
pip install phonenumbers
```

## 💡 How It Works
1. Parses the phone number using `phonenumbers.parse()`
2. Extracts country, carrier, and time zone information
3. Displays the details in an easy-to-read format

## 🎯 Contributing
Contributions are welcome! Feel free to fork, improve, and submit a pull request. 🔥

## 📄 License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## 🤝 Connect with Me
💼 **GitHub**: [Sourav-sudow](https://github.com/Sourav-sudow)


