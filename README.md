# pvalue_inspector

This `README.md` was created using my package [README_genie](https://github.com/browshanravan/README_genie).

A Streamlit-based application for performing two-sample statistical significance tests (t-tests and Mann-Whitney U) on data stored in CSV files.

---

## About This Project

**pvalue_inspector** provides an interactive web UI where users can upload a CSV file, select two columns of interest, specify assumptions about variance and distribution, and instantly compute:

- Standard (Student’s) t-test  
- Welch’s t-test  
- Mann-Whitney U test  

Results include the test name, p-value, and a simple null-hypothesis decision (Reject/Accept at α=0.05).

---

## Project Description

This tool is ideal for:

- Quick, exploratory hypothesis testing  
- Teaching/demoing basic inferential statistics  
- Lightweight, no-code statistical analysis  

Key features:

- Automatic handling of equal/unequal sample sizes (drops NaNs when needed)  
- Choice of parametric (t-tests) or non-parametric (Mann-Whitney U) methods  
- Streamlined, three-step workflow: upload → select columns → choose test  
- Runs entirely in the browser via Streamlit—no web-dev expertise required  

---

## Getting Started

### Prerequisites

- Python 3.10+  
- pip  

> Optionally, use the included Dev Container (VS Code + Docker) to spin up a ready-to-code environment.

### Installation

1. Clone the repository  
   ```bash
   git clone https://github.com/behzadrowshanravan/pvalue_inspector.git
   cd pvalue_inspector
   ```

2. Install Python dependencies  
   ```bash
   pip install -r requirements.txt
   ```

### Dev Container Setup (VS Code)

1. Open this folder in VS Code.  
2. Allow the “Dev Container” prompt to rebuild.  
3. A container with Python 3.10 and all tools will be provisioned automatically.

---

## Quickstart

Option 1: Run the helper script  
```bash
sh app.sh
```
This will install dependencies and launch the app on `localhost:8501`.

Option 2: Manual launch  
```bash
pip install -r requirements.txt
streamlit run main.py --server.port 8501
```

Then open your browser at:  
```
http://localhost:8501
```

---

## Usage

1. **Upload a CSV**  
2. **Select two columns** from the dropdown  
3. If **no missing values**, choose:
   - “Are you assuming equal population variance?”  
   - “Are you assuming equal population distribution?”  
4. Select one of:
   - **Standard t-test** (equal variance)  
   - **Welch’s t-test** (unequal variance)  
   - **Mann-Whitney U** (non-parametric or unequal lengths)  
5. View test statistic, p-value, and a “Rejected”/“Accepted” null-hypothesis outcome.

---

## Project Structure

```
.
├── app.sh                      # Install & launch script
├── main.py                     # Streamlit application
├── requirements.txt            # Python dependencies
├── LICENSE                     # MIT License
├── .streamlit/config.toml      # Streamlit UI/server config
├── .devcontainer/              # VS Code Dev Container config
│   ├── Dockerfile
│   └── devcontainer.json
└── pvalue_inspector/           # Python package
    └── src/
        └── utils.py            # CSV‐reading utility
```

---

## Contributing

Contributions, issues and feature requests are welcome. Feel free to fork the repository and submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.