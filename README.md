[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/yoHXt_g5)
# 프로젝트 이름

스포츠 규칙 및 규정 관련 QA Engine

<br>

## 프로젝트 소개

- 이 프로젝트는 다양한 스포츠 종목에 대한 규칙과 규정을 효율적으로 제공하는 QA engine입니다. 
- 사용자는 이 엔진을 통해 특정한 스포츠에 대한 질문을 할때 PDF에서 수집된 문서를 기반으로 관련 규칙과 규정을 즉각적으로 제공하는 것을 목표로 합니다. 

## 팀원 구성

<div align="center">

| **팀장** | **팀원 1** | **팀원 2** | **팀원 3** | **팀원 4** |
| :------: |  :------: | :------: | :------: | :------: |
|[<img src="https://avatars.githubusercontent.com/u/156163982?v=4" height=150 width=150> <br/> @Juha Lee](https://github.com/jl3725) |[<img src="https://avatars.githubusercontent.com/u/156163982?v=4" height=150 width=150> <br/> @hannakhw](https://github.com/hannakhw) |[<img src="https://avatars.githubusercontent.com/u/156163982?v=4" height=150 width=150> <br/> @moon-dotcom](https://github.com/moon-dotcom) |[<img src="https://avatars.githubusercontent.com/u/156163982?v=4" height=150 width=150> <br/> @Github](https://github.com/) |[<img src="https://avatars.githubusercontent.com/u/156163982?v=4" height=150 width=150> <br/> @Github](https://github.com/) |
</div>

<br>

## 1. 개발 환경

- 주 언어 : python
- 버전 및 이슈관리 : 3.11.9
- 협업 툴 : Github

<br>

## 2. 채택한 개발 기술과 브랜치 전략

### LangChain
- LangChain
  - LLM(대형 언어 모델)을 사용하여 애플리케이션 생성을 단순화하도록 설계된 프레임워크. 프롬프트를 인식하고 관련된 내용을 벡터스토어에서 찾아 LLM에 전달하여 전문적인 답변을 할 수 있게 만듭니다. 

- OS
  -  사용자의 환경 변수로 지정된 API_key를 가져오고, 외부에 노출되지 않도록 보안성을 강화합니다.

- ChatUpstage(LLM)
  - Upstage의 solar-embedding-1-large-passage 모델을 사용하여 질의응답 모델을 구성합니다. 

- RecursiveCharacterTextSplitter
  - 일반적인 텍스트에 범용적으로 사용할 수 있는 텍스트 분할기로, 문자 목록을 매개변수로 받아 동작합니다. 

- Chroma
  - 임베딩한 데이터를 Chroma에 로드하고 쿼리합니다. 질문을 하면 Chroma 벡터 스토어에서 유사도 검색을 하고 검색 결과 중 가장 유사한 문서를 출력합니다. 

- PyMuPDFLoader
  - 랭체인에서 제공하는 패키지로, pdf 파일을 로드하여 테스트 스플리터에 전달한다. 

### 브랜치전략 
    
- 브랜치 전략
  - Git-flow 전략을 기반으로 팀장의 main 브랜치와 각 팀원의 보조 브랜치를 운용했습니다.
  - main, master, hyowon 브랜치로 나누어 개발을 하였습니다.
    - **main** 브랜치는 각 팀원의 브랜치를 최종 머지하는 브랜치이자 팀장 Juha Lee의 브랜치 입니다.
    - **master** 브랜치는 팀원 moon-dotcom의 브랜치 입니다.
    - **hyowon** 브랜치는 팀원 hannakhw의 브랜치 입니다.

### 브랜치전략 
    
- 브랜치 전략
  - Git-flow 전략을 기반으로 팀장의 main 브랜치와 각 팀원의 보조 브랜치를 운용했습니다.
  - main, master, hyowon 브랜치로 나누어 개발을 하였습니다.
    - **main** 브랜치는 각 팀원의 브랜치를 최종 머지하는 브랜치이자 팀장 Juha Lee의 브랜치 입니다.
    - **master** 브랜치는 팀원 moon-dotcom의 브랜치 입니다.
    - **hyowon** 브랜치는 팀원 hannakhw의 브랜치 입니다.
  - 개인별 모듈 작업은 팀원별로 각자 가지고 있는 브랜치에서 작업했습니다. 모듈 개발이 끝나면 main 브랜치에 merge하고, merge 후에는 모든 팀원이 함께 pull하여 동기화를 마쳤습니다.

<br>

## 3. 프로젝트 구조
```
├── README.md
├── data
     ├── 올림픽예선시리즈 스포츠클라이밍_ 필수 정보.pdf
├── main.py
├── llm_api.py
├── file_loader.py
├── txt_splitter.py
├── vectorstore.py
├── retriever.py
├── prompt.py
└── conversational_rag.py
...

```

<br>

## 4. 역할 분담

### 팀원 Juha Lee
- **역할**
    - 프로젝트를 진행하며 맡은 역할 작성
- **기능**
    - 프로젝트를 진행하며 개발한 기능 작성
<br>

### 팀원 hannakhw
- **역할**
    - 프로젝트를 진행하며 맡은 역할 작성
- **기능**
    - 프로젝트를 진행하며 개발한 기능 작성
<br>

### 팀원 moon-dotcom
- **역할**
    - langchain pipline에서 문서를 로드, 스플릿하여 vectorstore에 전달
- **기능**
    - QA할 문서를 로드
    - RecursiveCharacterTextSplitter을 사용하여 chunk_size=1500, chunk_overlap=50으로 스플릿
<br>

## 5. 개발 기간 및 작업 관리

### 개발 기간
- 전체 개발 기간 : 2024-08-12 ~ 2024-08-19
- 계획 수립 및 역할 분담 : 2024-08-13
- 기능 구현 : 2024-08-13 ~ 2024-08-16
- 오류 테스트 및 발표 준비 : 2024-08-16
  
<br>

### 작업 관리
<예시>

- 아래와 같은 오류가 발생했습니다.

```python
C:\Users\yong\AppData\Local\Programs\Python\Python311\Lib\site-packages\langchain_core\_api\deprecation.py:117: LangChainDeprecationWarning: The class `langchain_community.llms.openai.OpenAI` was deprecated in langchain-community 0.0.10 and will be removed in 0.2.0. An updated version of the class exists in the langchain-openai package and should be used instead. To use it run `pip install -U langchain-openai` and import as `from langchain_openai import OpenAI`.
  warn_deprecated(
```

### 설명

- langchain_community.llms.openai.OpenAI는 langchain-community 0.0.10에서 deprecate되었으며 0.2.0에서 제거될 예정입니다.
- 업데이트된 버전의 클래스가 langchain-openai 패키지에 있으며 이것을 사용해야 합니다.


### 해결

- 명령 프롬프트(또는 터미널)에서 다음 명령을 실행해 langchain-openai 패키지를 설치합니다.

```python
pip install -U langchain-openai
```

- 아래와 같이 import문 변경하면 해결됩니다.
```python
from langchain_openai import OpenAI
```


<br>

## 5. 프로젝트 후기

### 팀원 1
프로젝트 후기 작성

### 팀원 2
프로젝트 후기 작성
<br>

