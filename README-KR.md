# test_cicd_01

Databricks Asset Bundle을 활용한 CI/CD 테스트 프로젝트입니다. 이 프로젝트는 Databricks 환경에서 Python 모듈과 노트북을 효율적으로 관리하고 배포하기 위한 구조와 유틸리티를 제공합니다.

> 📖 **English Documentation**: [README.md](./README.md)

## 프로젝트 구조

```
test_cicd_01/
├── src/                          # 소스 코드
│   ├── test_cicd_01/            # 메인 패키지
│   │   ├── main.py              # Spark 기반 메인 애플리케이션
│   │   └── __init__.py          # 패키지 초기화 (v0.0.1)
│   ├── module/                  # 공통 모듈
│   │   ├── path_manager.py      # 경로 관리 유틸리티
│   │   └── util.py              # 기본 유틸리티 함수
│   ├── foo/                     # 예제 모듈
│   │   └── bar.py               # 리소스 파일 읽기 예제
│   ├── main.ipynb               # 메인 노트북 (모듈 사용 예제)
│   └── set_notebook_paths.ipynb # 노트북 경로 설정 유틸리티
├── resources/                   # 리소스 파일
│   ├── test_cicd_01.job.yml    # Databricks Job 정의
│   └── foo/bar.yml             # 예제 설정 파일
├── tests/                       # 테스트 코드
│   ├── foo/test_read_resource.py
│   └── module/test_path_manager.py
├── config/                      # 설정 파일 디렉토리
├── databricks.yml              # Databricks Bundle 설정
└── setup.py                    # Python 패키지 설정
```

## 주요 기능

### 1. 경로 관리 시스템 (PathResolver)
- **싱글톤 패턴**으로 구현된 경로 관리 클래스
- Databricks 환경에서 Bundle 내 다양한 디렉토리에 대한 절대 경로 제공
- 지원 경로: `resources`, `config`, `tests`

```python
from module.path_manager import PathResolver

paths = PathResolver()
print(paths.resources)  # 리소스 디렉토리 경로
print(paths.config)     # 설정 디렉토리 경로
print(paths.tests)      # 테스트 디렉토리 경로
```

### 2. 노트북 경로 설정
- `set_notebook_paths.ipynb`: Databricks 노트북에서 Python 모듈을 import할 수 있도록 sys.path 자동 설정
- Bundle 이름 기반 동적 경로 구성

### 3. 리소스 파일 관리
- YAML 설정 파일 읽기 예제
- 경로 관리자를 통한 안전한 파일 접근

```python
from foo.bar import parse_bar
content = parse_bar()  # resources/foo/bar.yml 파일 읽기
```

## 시작하기

### 1. 환경 설정

Databricks CLI 설치:
```bash
pip install databricks-cli
```

Databricks 워크스페이스 인증:
```bash
databricks configure
```

### 2. 개발 환경 배포

개발 환경에 배포:
```bash
databricks bundle deploy --target dev
```

프로덕션 환경에 배포:
```bash
databricks bundle deploy --target prod
```

### 3. Job 실행

배포된 Job 실행:
```bash
databricks bundle run
```

### 4. 로컬 개발

개발 의존성 설치:
```bash
pip install -r requirements-dev.txt
```

테스트 실행:
```bash
pytest
```

## 테스트

프로젝트에는 다음과 같은 테스트가 포함되어 있습니다:

- **경로 관리자 테스트**: PathResolver 클래스의 정상 동작 확인
- **리소스 파일 읽기 테스트**: YAML 파일 읽기 기능 검증

```bash
# 모든 테스트 실행
pytest

# 특정 테스트 실행
pytest tests/module/test_path_manager.py
pytest tests/foo/test_read_resource.py
```

## 개발 도구

- **Databricks Connect**: 로컬 IDE에서 Databricks 클러스터에 연결
- **Visual Studio Code Extension**: Databricks 개발 환경 통합
- **pytest**: 단위 테스트 프레임워크

## CI/CD 설정

이 프로젝트는 Databricks Asset Bundle을 사용하여 CI/CD 파이프라인을 구성합니다:

- **Git 연동**: GitHub 리포지토리 기반 소스 관리
- **자동 배포**: Bundle을 통한 개발/프로덕션 환경 분리
- **Job 스케줄링**: 워크플로우 자동 실행 지원

자세한 내용은 [Databricks Asset Bundles 문서](https://docs.databricks.com/dev-tools/bundles/index.html)를 참조하세요.

## 프로젝트 구성 요소

### 핵심 모듈

#### PathResolver (`src/module/path_manager.py`)
```python
class PathResolver:
    """
    싱글톤 패턴으로 구현된 경로 관리 클래스
    Databricks Bundle 환경에서 안전한 파일 경로 접근을 제공
    """
    
    @property
    def resources(self):
        """리소스 디렉토리 경로 반환"""
        
    @property  
    def config(self):
        """설정 디렉토리 경로 반환"""
        
    @property
    def tests(self):
        """테스트 디렉토리 경로 반환"""
```

#### Spark 유틸리티 (`src/test_cicd_01/main.py`)
```python
def get_spark() -> SparkSession:
    """
    Databricks Connect 또는 표준 Spark 세션 생성
    로컬 개발과 클러스터 환경을 모두 지원
    """

def get_taxis(spark: SparkSession) -> DataFrame:
    """
    NYC Taxi 샘플 데이터 로드
    """
```

### 노트북 구성

#### 메인 노트북 (`src/main.ipynb`)
- 경로 설정 노트북 실행
- 모듈 import 및 사용 예제
- PathResolver 사용법 데모
- 리소스 파일 읽기 예제

#### 경로 설정 노트북 (`src/set_notebook_paths.ipynb`)
- Bundle 이름 기반 동적 경로 구성
- sys.path 자동 설정
- 노트북 환경에서의 모듈 import 지원

### 테스트 구성

#### 단위 테스트
- `tests/module/test_path_manager.py`: PathResolver 기능 테스트
- `tests/foo/test_read_resource.py`: 리소스 파일 읽기 테스트

#### 테스트 실행 환경
- pytest 기반 테스트 프레임워크
- `pytest.ini`를 통한 테스트 경로 및 Python 경로 설정
- 개발 의존성은 `requirements-dev.txt`에 정의

### Bundle 설정

#### Databricks Bundle (`databricks.yml`)
- 개발/프로덕션 환경 분리
- Git 기반 소스 관리 설정
- Job 및 리소스 정의 포함

#### Job 정의 (`resources/test_cicd_01.job.yml`)
- 노트북 기반 작업 정의
- 큐 활성화 설정
- 워크스페이스 소스 사용

## 사용 사례

### 1. 로컬 개발 환경에서 테스트
```bash
# 의존성 설치
pip install -r requirements-dev.txt

# 테스트 실행
pytest -v

# 특정 모듈 테스트
pytest tests/module/ -v
```

### 2. Databricks 노트북에서 모듈 사용
```python
# 노트북 첫 번째 셀에서 실행
%run ./set_notebook_paths

# 이후 셀에서 모듈 import 가능
from module.path_manager import PathResolver
from foo.bar import parse_bar
```

### 3. Bundle 배포 및 실행
```bash
# 개발 환경 배포
databricks bundle deploy --target dev

# Job 실행
databricks bundle run test_cicd_01_job

# 배포 상태 확인
databricks bundle validate
```

## 확장 가능성

이 프로젝트는 다음과 같은 방향으로 확장할 수 있습니다:

1. **추가 데이터 소스 연동**: Delta Lake, 외부 데이터베이스 등
2. **MLflow 통합**: 모델 학습 및 배포 파이프라인
3. **DLT 파이프라인**: Delta Live Tables를 활용한 데이터 파이프라인
4. **모니터링 및 알림**: Job 실행 상태 모니터링
5. **보안 강화**: Secret 관리, 접근 권한 제어

## 문제 해결

### 일반적인 문제들

#### 1. 모듈 import 오류
```python
# 해결방법: 노트북에서 경로 설정 실행
%run ./set_notebook_paths
```

#### 2. 리소스 파일 접근 오류
```python
# PathResolver 사용 권장
from module.path_manager import PathResolver
paths = PathResolver()
config_path = paths.resources / 'config.yml'
```

#### 3. Bundle 배포 실패
```bash
# 설정 검증
databricks bundle validate

# 인증 상태 확인
databricks auth profiles
```

## 기여하기

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.
