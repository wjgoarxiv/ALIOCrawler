# **ALIOCrawler**
> ::파이썬 기반 ALIO 구직 정보 추출기::

![ALIOCrawler LOGO](./LOGO.png)

<br> 

<a href="https://www.buymeacoffee.com/woojingo" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-red.png" alt="Buy Me A Coffee" style="height: 40px !important;width: 120px !important;" ></a>

## **1. 개요**
[ALIO](https://www.alio.go.kr/)는 한국의 구직 정보를 제공하는 공공기관 경영정보 공개시스템입니다. 특히, 취준생 및 졸업 예정자들이 채용을 위해 수시로 방문하는 사이트이기도 합니다. 다양한 구직 정보를 열람할 수 있다는 데에서 ALIO는 훌륭한 사이트이지만, 구직 정보를 열람하기 위해서는 매번 검색을 해야 한다는 불편함이 있습니다. 이를 해결하기 위해, ALIO의 구직 정보를 추출하여 엑셀 파일 (`.csv` 형태)로 저장하는 프로그램을 개발하였습니다. 구직 정보를 일괄적으로 열람하고 싶은 기관을 터미널에서 입력하세요. 그러면, 해당 기관의 모든 구직 정보를 액셀 파일로 저장할 수 있습니다. 

## **2. 설치 방법** 
설치는 pip를 통해 진행하시면 됩니다. 터미널에 아래와 같이 입력해주세요.
```
$ pip install aliocrawler
```

## **3. 사용 방법**
```
$ aliocrawler [option] [value]
```

### **선택적 인수 목록**
ALIOCrawler는 다음과 같은 선택적 인수를 지원합니다. 터미널에서 `aliocrawler -h`를 입력하면, 아래와 같은 도움말을 볼 수 있습니다.

| 옵션 | 설명 | 디폴트 값 |
|:---:|:---:| :---: |
| `-h`, `--help` | 도움말을 출력합니다. | `.`|
| `-s`, `--search` | 검색하고자 하는 공고기관의 이름을 입력해주세요 (예시: 울산과학기술원). | `울산과학기술원` |
| `-o`, `--output` | 검색 결과를 저장할 파일명을 입력해주세요 (예시: ALIO_output). Output 파일은 CSV 파일 형태로 저장됩니다. | `ALIO_output` |

예를 들어, 
```
aliocrawler -s 한국전력공사 -o 한국전력공사
```
를 입력하면, 한국전력공사의 모든 구직 정보를 `한국전력공사.csv`라는 파일로 저장할 수 있습니다.

## **4. 주요 기능**
* 구직 정보를 엑셀 파일로 일괄 저장합니다.
* 검색어를 입력하여 원하는 기관의 구직 정보를 전부 추출할 수 있습니다.
* 출력 파일명을 입력하여 원하는 파일명으로 저장할 수 있습니다.

## **5. 예시**
* `Examples` 폴더 내에 예시 결과 값들을 올려두었습니다. 활용에 참고해주세요.

## **6. 기여하기**
ALIOCrawler는 오픈소스 프로젝트입니다. 기여하고 싶으신 분은 pull request를 보내주세요. 혹은 [제 메일](mailto:woo_go@yahoo.com)로 연락해주세요.

## **7. 저자**
* [wjgoarxiv](https://www.github.com/wjgoarxiv)

## **8. 라이센스**
* [MIT](https://choosealicense.com/licenses/mit/)
