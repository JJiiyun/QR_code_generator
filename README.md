# QR 코드 생성기 프로젝트

## 📌 프로젝트 개요
기존 클라우드 컴퓨팅 과목의 프로젝트로 구현한 간단한 웹 애플리케이션(https://github.com/JJiiyun/QR_code_generator/tree/main/previous_project) 에서 더 나아가, \
URL과 사용자 지정 제목을 기반으로 고품질 QR 코드를 생성하도록 생성 기록 관리와 다양한 내보내기 기능을 제공합니다.

<img width="1488" alt="image" src="https://github.com/user-attachments/assets/eab685b0-e513-4c5e-8d50-467eaf572b2f" />
<img width="1483" alt="image" src="https://github.com/user-attachments/assets/630c331d-4179-4354-a4da-52ea06b1a820" />


## ✨ 주요 기능
### 핵심 기능
- **이중 입력 시스템**  
  ✔️ 사용자 지정 제목 + URL 조합 입력  
  ✔️ 실시간 URL 유효성 검증

### 생성 옵션
- **3단계 크기 선택**  
  `기본(300px)` | `큰(450px)` | `고화질(600px)`

### 기록 관리
- **인텔리전트 히스토리**  
  ✔️ 생성일자 기준 자동 정렬  
  ✔️ 썸네일 + 제목 + URL 조합 표시  
  ✔️ 컨텍스트 액션(다운로드/삭제)

### UI/UX
- **다이내믹 테마**  
  라이트/다크 모드 실시간 전환
- **인터랙티브 디자인**  
  ✔️ 호버 애니메이션  
  ✔️ 로딩 인디케이터  
  ✔️ 모바일 최적화

## 🛠 기술 스택
**Backend**  
`Python 3.10` | `Flask 2.3` | `qrcode 7.4` | `Pillow 10.0`

**Frontend**  
`HTML5` | `CSS3 Grid/Flex` | `Vanilla JS`  
`Font Awesome 5` | `Poppins Font`

## 📥 설치 & 실행
```bash
# 의존성 설치
pip install flask qrcode[pil]

# 서버 실행 (개발 모드)
FLASK_ENV=development flask run --port 5001
