# FastAPI Backend Development

This repository comprehensively covers the backend development process using FastAPI. It focuses on building APIs, data validation, CRUD operations, authentication, and asynchronous programming. Additionally, it provides a guide for deploying the application in a production environment using Docker and Google Cloud.

## Project Features

- **Creating APIs with FastAPI**  
- **Asynchronous programming**  
- **Data validation with Pydantic**  
- **CRUD operations**  
- **Authentication with JWT**  
- **Database integration (SQLite & Alembic)**  
- **Containerization with Docker**  
- **Deployment with Google Cloud**

## Getting Started

### Requirements

The following software must be installed for the project to run:

- Python 3.9+
- Docker (optional, for deployment)

### Installation

Follow these steps to get the project running on your local environment:

1. Clone this repository:
    ```bash
    git clone https://github.com/your-repo-name.git
    cd your-repo-name
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Start the application:
    ```bash
    uvicorn main:app --reload
    ```

### Deployment

You can easily deploy the application using Docker. Build and run your Docker image with the following commands:

1. Build the Docker image:
    ```bash
    docker build -t fastapi-backend .
    ```

2. Start the Docker container:
    ```bash
    docker run -d -p 8000:8000 fastapi-backend
    ```

## Contributing

If you would like to contribute to this project, please create a branch from the `main` branch before submitting a pull request. Your contributions will greatly help improve the project.

---

# FastAPI Backend Geliştirme

Bu repository, FastAPI kullanarak backend geliştirme sürecini kapsamlı bir şekilde ele almaktadır. API oluşturma, veri doğrulama, CRUD işlemleri, kimlik doğrulama ve asenkron programlama gibi konulara odaklanır. Ayrıca, Docker ve Google Cloud üzerinde uygulamanın üretim ortamında dağıtımına dair bir rehber sunar.

## Proje Özellikleri

- **FastAPI ile API oluşturma**  
- **Asenkron programlama**  
- **Pydantic ile veri doğrulama**  
- **CRUD işlemleri**  
- **JWT ile kimlik doğrulama**  
- **Veritabanı entegrasyonu (SQLite & Alembic)**  
- **Docker ile konteynerizasyon**  
- **Google Cloud ile dağıtım**

## Başlangıç

### Gereksinimler

Projenin çalışabilmesi için aşağıdaki yazılımlar yüklü olmalıdır:

- Python 3.9+
- Docker (isteğe bağlı, dağıtım için)

### Kurulum

Projenin yerel ortamınızda çalıştırılması için aşağıdaki adımları izleyin:

1. Bu repoyu klonlayın:
    ```bash
    git clone https://github.com/your-repo-name.git
    cd your-repo-name
    ```

2. Gerekli paketleri yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

3. Uygulamayı başlatın:
    ```bash
    uvicorn main:app --reload
    ```

### Dağıtım

Docker kullanarak uygulamanızı kolayca dağıtabilirsiniz. Aşağıdaki komut ile Docker imajınızı oluşturun ve çalıştırın:

1. Docker imajını oluşturun:
    ```bash
    docker build -t fastapi-backend .
    ```

2. Docker konteynerini başlatın:
    ```bash
    docker run -d -p 8000:8000 fastapi-backend
    ```

## Katkı

Eğer bu projeye katkıda bulunmak isterseniz, lütfen bir pull request göndermeden önce `main` dalından bir branch oluşturun. Katkılarınız, projenin gelişmesine büyük katkı sağlayacaktır.
