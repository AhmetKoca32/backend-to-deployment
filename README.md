# FastAPI Backend Development

Bu repo, FastAPI kullanarak backend geliştirme sürecini kapsamlı bir şekilde ele almaktadır. API oluşturma, veri doğrulama, CRUD işlemleri, kimlik doğrulama, asenkron programlama gibi konulara odaklanır. Ayrıca, Docker ve Google Cloud üzerinde dağıtım yaparak uygulamanın üretim ortamında çalıştırılmasına dair rehber sunar.

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

- Python 3.7+
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

## Lisans

Bu proje MIT lisansı ile lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakabilirsiniz.
