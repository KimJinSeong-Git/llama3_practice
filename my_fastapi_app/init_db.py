# 데이터베이스를 초기화하는 Python 스크립트를 만듭니다. 이를 예로 들어 `init_db.py`로 저장하세요.
from app.database import Base, engine
from app.models import example

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Tables created.")
