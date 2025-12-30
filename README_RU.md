# data-etl-pipeline

## Описание

ETL-конвейер для обработки и трансформации данных используя Python, Pandas, Airflow с Docker и PostgreSQL.

## Особенности

- **ETL класс** для Extract, Transform, Load
- **Docker** для контейнеризации
- **PostgreSQL** для схранения данных
- **Pandas** для обработки данных

## Основное использование

### 1. Построение и запуск

```bash
# Docker Compose запуск
docker-compose up --build
```

### 2. Основной процесс

**Extract** (Extraction):
- Чтение данных из CSV файла

**Transform** (Transformation):
- Удаление дубликатов
- Обработка пропусков
- Клининг данных

**Load** (Loading):
- Сохранение в PostgreSQL

### 3. Пример

```python
from etl_pipeline import ETLPipeline

pipeline = ETLPipeline()
pipeline.run('data/input.csv', 'target_table')
```

## Файлы

- `etl_pipeline.py` - главное приложение
- `docker-compose.yml` - конфигурация Docker
- `Dockerfile` - определение контейнера
- `requirements.txt` - зависимости Python

## Энвайронмент переменные

```bash
DATABASE_URL=postgresql://user:password@localhost:5432/etl_db
LOG_LEVEL=INFO
```

## Лицензия

MIT License
