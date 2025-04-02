"# Automated_Animal_prediction" 


# Automated Animal Prediction

This project uses a Convolutional Neural Network (CNN) to predict whether an image is of a cat or a dog. The project includes a Flask web application that allows users to upload images and get predictions.

## Project Structure

.
Additional Notes:
The predict_pipeline.py script assumes the existence of a load_object utility function to load the saved model and preprocessor.
The train_pipeline.py script includes the steps to build, compile, train, and save the CNN model and preprocessor.
The paths for saving and loading models and preprocessors are configurable and can be adjusted as per your directory structure. Ensure that directories like artifacts exist in your project.


## Setup and Installation

### Prerequisites

- Docker
- Python 3.8 or higher

### Steps to Run the Project

1. **Clone the repository:**
    ```bash
    git clone https://github.com/mahi865/Automated_Animal_prediction.git
    cd Automated_Animal_prediction
    ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask application:**
    ```bash
    python app.py
    ```
   The application will be available at `http://0.0.0.0:5000`.

### Steps to Run the Project with Docker

1. **Build the Docker image:**
    ```bash
    docker build -t automated_animal_prediction .
    ```

2. **Run the Docker container:**
    ```bash
    docker run -p 5000:5000 automated_animal_prediction
    ```
   The application will be available at `http://0.0.0.0:5000`.

## Usage

1. Open the application in your browser at `http://0.0.0.0:5000`.
2. Upload an image of a cat or dog.
3. The application will display the prediction result.

## Project Dependencies

- Flask
- TensorFlow
- Keras
- NumPy
- Pandas
- Werkzeug
- AWS CLI
- FFmpeg
- libsm6
- libxext6

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.






############################################################################################################################









# Automated Animal Prediction

This project uses a Convolutional Neural Network (CNN) to predict whether an image is of a cat or a dog. The project includes a Flask web application that allows users to upload images and get predictions.

## Project Structure

```
Automated_Animal_prediction/
├── Dockerfile
├── README.md
├── app.py
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── exception.py
│   ├── logger.py
│   ├── pipeline/
│   │   ├── __init__.py
│   │   ├── predict_pipeline.py
│   ├── utils.py
├── templates/
│   ├── index.html
│   ├── home.html
└── uploads/
```

## Setup and Installation

### Prerequisites

- Docker
- Python 3.8 or higher
- AWS CLI

### Local Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/mahi865/Automated_Animal_prediction.git
    cd Automated_Animal_prediction
    ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask application:**
    ```bash
    python app.py
    ```
   The application will be available at `http://0.0.0.0:5000`.

### Docker Setup

#### Building the Docker Image

1. **Build the Docker image:**
    ```bash
    docker build -t automated_animal_prediction .
    ```

2. **Run the Docker container:**
    ```bash
    docker run -p 5000:5000 automated_animal_prediction
    ```
   The application will be available at `http://0.0.0.0:5000`.

#### Docker Setup in EC2

Optional:
```bash
sudo apt-get update -y
sudo apt-get upgrade
```

Required:
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

### Configure EC2 as Self-Hosted Runner

1. Go to your GitHub repository.
2. Navigate to **Settings** > **Actions** > **Runners**.
3. Click **New self-hosted runner** and follow the instructions to set up the runner on your EC2 instance.

### Setup GitHub Secrets

1. Go to your GitHub repository.
2. Navigate to **Settings** > **Secrets** and click **New repository secret**.
3. Add the following secrets:
    - `AWS_ACCESS_KEY_ID`
    - `AWS_SECRET_ACCESS_KEY`
    - `AWS_REGION` (e.g., `us-east-1`)
    - `AWS_ECR_LOGIN_URI` (e.g., `566373416292.dkr.ecr.ap-south-1.amazonaws.com`)
    - `ECR_REPOSITORY_NAME` (e.g., `simple-app`)

## Usage

1. Open the application in your browser at `http://0.0.0.0:5000`.
2. Upload an image of a cat or dog.
3. The application will display the prediction result.

## Project Dependencies

- Flask
- TensorFlow
- Keras
- NumPy
- Pandas
- Werkzeug
- AWS CLI
- FFmpeg
- libsm6
- libxext6

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


```

This `README.md` provides comprehensive instructions for setting up, running, and contributing to the project, both locally and using Docker. It also includes details for configuring an EC2 instance as a self-hosted GitHub Actions runner and setting up GitHub secrets.