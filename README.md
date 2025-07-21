# Backend-Exercise
# 📄 PubMed Paper Fetcher CLI

This is a Python CLI tool to fetch PubMed research papers by query and identify non-academic (company-affiliated) authors. It outputs results in a CSV file.

## 🚀 Features
- Search PubMed using custom queries
- Detect non-academic authors
- Export data to CSV
- Uses Python, Typer, and Poetry

## 🛠️ Setup Instructions
1. Clone this repo:
   git clone https://github.com/HarshitaKuppannagari/Backend-Exercise
   cd Backend-Exercise

2. Install dependencies:
   poetry install

## 🧪 Run the Tool
   poetry run get-papers-list fetch "your query here" -f output.csv

Example:
   poetry run get-papers-list fetch "covid vaccine" -f output.csv

## 📁 Output Columns
- PubMed ID  
- Title  
- Publication Date  
- Non-academic Author(s)  
- Company Affiliation(s)  
- Corresponding Author Email  

## 📂 Project Structure
src/
└── get_papers_list/
    ├── cli.py
    ├── pubmed.py
    └── utils.py

## 👩‍💻 Author
Harshita Kuppannagari  
GitHub: https://github.com/HarshitaKuppannagari

## 📄 License
MIT
