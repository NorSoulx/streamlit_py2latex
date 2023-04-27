# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt into the container at /app
COPY src/requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Install TeX Live for pdflatex
RUN apt-get update && apt-get install -y texlive-latex-base texlive-latex-extra texlive-fonts-recommended poppler-utils

# Make port 8501 available to the world outside this container
EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["/bin/bash"]
CMD ["run_streamlit.sh"]
