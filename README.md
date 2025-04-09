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






############################################################################################################







To set up CI/CD for your project using GitHub Actions, you need to create a GitHub Actions workflow file. This file will define the steps to build, test, and deploy your application.

Here's a step-by-step guide to create a CI/CD pipeline for your project:

### Step 1: Create a GitHub Actions Workflow File

1. In your repository, navigate to the `.github/workflows` directory. If it doesn't exist, create it.
2. Inside the `.github/workflows` directory, create a new file named `ci-cd.yml`.

### Step 2: Define the Workflow

Add the following content to the `ci-cd.yml` file:

```yaml
name: CI/CD Pipeline

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.8

    - name: Install dependencies
      run: |
        python -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt

    - name: Lint with flake8
      run: |
        pip install flake8
        flake8 .

    - name: Run tests
      run: |
        source venv/bin/activate
        python -m unittest discover

  docker:
    needs: build
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Log in to Amazon ECR
      id: login-ecr
      uses: aws-actions/amazon-ecr-login@v1
      with:
        region: ${{ secrets.AWS_REGION }}

    - name: Build, tag, and push Docker image
      env:
        ECR_REGISTRY: ${{ steps.login-ecr.outputs.registry }}
        ECR_REPOSITORY: ${{ secrets.ECR_REPOSITORY_NAME }}
        IMAGE_TAG: latest
      run: |
        docker build -t $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG .
        docker push $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG

  deploy:
    needs: docker
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Deploy to AWS ECS
      uses: aws-actions/amazon-ecs-deploy-task-definition@v1
      with:
        task-definition: ecs-task-def.json
        service: my-ecs-service
        cluster: my-ecs-cluster
        container-name: my-container
        image: ${{ steps.login-ecr.outputs.registry }}/${{ secrets.ECR_REPOSITORY_NAME }}:latest
      env:
        AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
        AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        AWS_REGION: ${{ secrets.AWS_REGION }}
```

### Step 3: Define Secrets

You need to set up the following secrets in your GitHub repository:

1. Navigate to your repository on GitHub.
2. Go to **Settings** > **Secrets and variables** > **Actions**.
3. Add the following secrets:
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `AWS_REGION` (e.g., `us-east-1`)
   - `AWS_ECR_LOGIN_URI` (e.g., `566373416292.dkr.ecr.ap-south-1.amazonaws.com`)
   - `ECR_REPOSITORY_NAME` (e.g., `simple-app`)

### Step 4: Create ECS Task Definition

Create an `ecs-task-def.json` file in the root of your repository with the following content:

```json
{
  "family": "my-ecs-task",
  "networkMode": "awsvpc",
  "executionRoleArn": "arn:aws:iam::<aws_account_id>:role/ecsTaskExecutionRole",
  "containerDefinitions": [
    {
      "name": "my-container",
      "image": "<aws_account_id>.dkr.ecr.<region>.amazonaws.com/<repository>:latest",
      "essential": true,
      "memory": 512,
      "cpu": 256,
      "portMappings": [
        {
          "containerPort": 5000,
          "hostPort": 5000
        }
      ]
    }
  ],
  "requiresCompatibilities": [
    "FARGATE"
  ],
  "cpu": "256",
  "memory": "512"
}
```

### Step 5: Push Changes

Commit and push the changes to your repository. The GitHub Actions workflow will automatically run on every push to the `main` branch and on every pull request targeting the `main` branch.

### Summary

- **ci-cd.yml**: Defines the GitHub Actions workflow for building, testing, and deploying the application.
- **Secrets**: Stores sensitive information securely in GitHub.
- **ecs-task-def.json**: Defines the ECS task for deploying the Docker container.

This should set up a complete CI/CD pipeline for your project using GitHub Actions.


#########################################################################################################################33

Updated Information

Based on the files and information retrieved from your repository, here is an analysis of the project and tools used, followed by a proposed architecture diagram.

---

### **Project Overview**
The "Automated Animal Prediction" project uses a Convolutional Neural Network (CNN) to predict whether an image is of a cat or a dog. It includes:
- **Flask Web Application:** For interacting with users where images can be uploaded for prediction.
- **Machine Learning Model:** A CNN for binary classification (cat vs. dog), trained using TensorFlow/Keras.
- **AWS Infrastructure:** Terraform scripts for provisioning AWS resources, including EC2 instances.
- **Data Preprocessing:** Tools and scripts for handling datasets and preparing input for the model.
- **Docker Integration:** Docker setup for containerizing and deploying the application.
- **GitHub Actions:** CI/CD pipeline for automating the build, test, and deployment process.

---

### **Architecture Diagram**

The architecture can be structured into the following key layers:

```plaintext
               +-----------------------------------+
               |       User Interface (Web)       |
               |   (Flask Application in EC2)     |
               +-----------------------------------+
                               |
                               v
               +-----------------------------------+
               | Machine Learning Model (CNN)      |
               |  (TensorFlow/Keras, Preprocessor) |
               +-----------------------------------+
                               |
                               v
               +-----------------------------------+
               |   Data Preprocessing Layer        |
               | (Training and Testing datasets)   |
               +-----------------------------------+
                               |
                               v
               +-----------------------------------+
               |          AWS Infrastructure       |
               |   (Terraform: EC2, S3, IAM, etc.) |
               +-----------------------------------+
                               |
                               v
               +-----------------------------------+
               |         CI/CD Pipeline            |
               |  (GitHub Actions, Docker, ECS)    |
               +-----------------------------------+
```

---

### **Components Explained**

1. **User Interface (Web)**:
   - Built with Flask (`app.py`).
   - Provides endpoints for uploading images and displaying predictions.
   - Renders templates such as `index.html` and handles file uploads.

2. **Machine Learning Model**:
   - A CNN, defined and trained via TensorFlow/Keras (`train_pipeline.py`).
   - Handles predictions through the `PredictPipeline` class in `predict_pipeline.py`.
   - Preprocessor (e.g., StandardScaler) is used for transforming input data.

3. **Data Preprocessing**:
   - Scripts like `training_cnn.py` and `making_single_prediction.py` handle training and prediction tasks.
   - Preprocessing includes rescaling images and data augmentation.

4. **AWS Infrastructure**:
   - Terraform is used to provision resources:
     - `main.tf`: Defines EC2 instances.
     - `variables.tf` and `outputs.tf`: Handle configuration.
   - Resources like S3 buckets can store datasets and model artifacts.

5. **CI/CD Pipeline**:
   - GitHub Actions workflow (`ci-cd.yml`) automates build, test, and deployment tasks.
   - Docker is used for containerizing the application.
   - ECS (Elastic Container Service) can be used for deploying Docker containers.

---

### **Next Steps**
1. **Validation**: Ensure all Terraform configurations are deployed and that the Flask app is running on the provisioned EC2 instance.
2. **Enhancements**: Use S3 for storing datasets and model artifacts to ensure scalability.
3. **Monitoring**: Add logging and monitoring for the web app and AWS resources.
4. **Testing**: Validate the CI/CD pipeline for automated updates on code push.
