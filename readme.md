## jinja prettier 이슈일때

플러그인 설치

1. Django Baptiste Darthenay
2. Unibeautify - Universal Formatter

[project경로]/.vscode/settings.json

```
{
  "files.associations": {
    "**/*.html": "html",
    "**/templates/*/*.html": "django-html",
    "**/templates/*": "django-html",
    "**/requirements{/**,*}.{txt,in}": "pip-requirements"
  },
  "unibeautify.enabled": true,
  "[django-html]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "Glavin001.unibeautify-vscode"
  }
}
```

## FASTAPI 환경 설정  
0. python -m venv .venv  
-> 가상환경 잡아줌  
1. requirements.txt 생성  
```
fastapi
uvicorn

sqlalchemy
mysqlclient #db 접속 용도
alembic #migration 용도

python-dotenv #env파일 경로 
PyJWT   
```
2. pip install -r .\requirements.txt  

## DB 설정  
1. sqlalchemy  
```
SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://root:0000@localhost:3306/test2"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
        
Base.metadata.create_all(bind=engine)
```

## 테이블 스키마 선언    
```
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20),index=True)
    def __init__(self,**data):
      super(User,self).__init__(**data)
```
-> super **data를 사용하면 init 일일이 선언 해주지 않아도 됨  
실사용 예)    
```
class UserCreate(BaseModel):
  name:str

@app.post("/create")
def read_root(userInfo:UserCreate,db: Session = Depends(get_db)):
  user = User(**userInfo.dict())
```
-> body로 들어오는 데이터에 **dict()를 사용하여 바로 파라미터화 시킬 수 있음  

## 마이그레이션  
-> DB 스키마 변경 사항 적용을 위해서 필수  
```
alembic init ./migration
alembic revision --autogenerate -m "Initial"
alembic upgrade head
```

## env 파일 사용  
```
from dotenv import load_dotenv
import jwt,os

load_dotenv(dotenv_path=".env") #기본이 .env파일인데 변경을 원할때는 dotenv 모듈 설치후 
JWT_SECRET = os.getenv("secret","secret")
JWT_ALGORITHM = os.getenv("secret","HS256")

jwt.encode({'id':user.id,'name':user.name}, JWT_SECRET, algorithm=JWT_ALGORITHM)
userInfo = jwt.decode(token,JWT_SECRET, algorithms=[JWT_ALGORITHM])
```

## CRUD 문법  
```
user = db.query(User).get(userInfo['id']) # id인 경우 get사용 가능
db.delete(user)
db.commit

user = User(**userInfo.dict())
id = db.add(user)
db.commit()
print(user['id']) #커밋 후, 삽입된 정보(id)를 받아서 사용 가능
```

## env 파일 사용  
```
from dotenv import load_dotenv
import jwt,os

load_dotenv(dotenv_path=".env") #기본이 .env파일인데 변경을 원할때는 dotenv 모듈 설치후 
JWT_SECRET = os.getenv("secret","secret")
JWT_ALGORITHM = os.getenv("secret","HS256")

jwt.encode({'id':user.id,'name':user.name}, JWT_SECRET, algorithm=JWT_ALGORITHM)
userInfo = jwt.decode(token,JWT_SECRET, algorithms=[JWT_ALGORITHM])
```

## jwt bearer token 인증  
```
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBasicCredentials, HTTPBearer
import jwt,os
JWT_SECRET = os.getenv("secret","secret")
JWT_ALGORITHM = os.getenv("secret","HS256")

security = HTTPBearer()

async def check_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    token = credentials.credentials
    userInfo = jwt.decode(token,JWT_SECRET, algorithms=[JWT_ALGORITHM])
    print(userInfo)
    print(token)
    try:
      if not userInfo:
        raise HTTPException(status_code=403, detail="Invalid authorization code.")
      return userInfo
    except e:  # catches any exception
        raise HTTPException(
            status_code=401,
            detail=str(e))
```
실사용 예)  
```
@app.delete("/resign")
def read_root(user=Depends(check_current_user)):
  print(user["id"])
```
