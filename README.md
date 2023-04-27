# Streamlit Python to LaTeX Code Formatter

Streamlit Python to LaTeX Code Formatter is a web application that downloads Python code from a repository and formats it in LaTeX. It allows users to input a URL to a repository containing Python code and generates a formatted LaTeX document that includes the downloaded code.

## Features

- Input a URL to a repository containing Python code
- Download and format Python code in LaTeX
- Preview and download the generated LaTeX document

## Project Structure

```
├── Dockerfile
├── docker-compose.yml
├── docker_compose_build.sh
├── docker_compose_run.sh
└── src
    ├── app.py
    ├── latex_head.tex
    ├── latex_tail.tex
    ├── requirements.txt
    └── run_streamlit.sh
```


## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Running the application

1. Clone the repository:

```
git clone https://github.com/NorSoulx/streamlit_py2latex.git
cd streamlit_py2latex
```

2. Build the Docker image:

```
bash ./docker_compose_build.sh
```


3. Run the Docker container:

```
bash ./docker_compose_run.sh
```

4. Open your web browser and navigate to http://localhost:8501.


<img width="788" alt="py2latex" src="https://user-images.githubusercontent.com/4839848/235004016-432b1200-1330-46d8-992f-282d4f034a6d.png">

