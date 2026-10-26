# 우리 스몰웨딩 가이드

가족만 모여 드리는 작은 예배를 준비하는 앱이에요. 스몰웨딩 후기 11편을 정리했고, 인원·예식일·지역·예산을 넣으면 맞는 장소와 예상 총액, 날짜별 할 일을 골라 줘요.

- 웹 주소: https://wedding.totocos.workers.dev (Cloudflare Workers)
- claude.ai 버전: https://claude.ai/artifact/SAbXKDmzDqcu48ZDZkxZ6A

## 구성

- `src/guide.html`: 페이지 본문. claude.ai 아티팩트와 웹 버전이 같이 쓰는 원본이에요.
- `scripts/build.py`: `src/guide.html`을 홈 화면 앱용 문서로 감싸 `public/index.html`을 만들어요.
- `scripts/make_icons.py`: `public/icons`의 앱 아이콘을 그려요.
- `public/`: Cloudflare Workers가 그대로 올리는 정적 파일이에요. 매니페스트와 오프라인용 `sw.js`가 들어 있어요.
- `wrangler.jsonc`: Worker 이름(`wedding`)과 정적 파일 폴더 설정이에요.

## 고치고 다시 올리기

```sh
python3 scripts/build.py
```

`src/guide.html`을 고친 뒤 위 명령으로 `public/index.html`을 다시 만들고 커밋해서 푸시하면, Cloudflare가 연결된 브랜치를 자동으로 다시 배포해요. 웹 버전의 체크리스트는 각 기기 브라우저에만 저장돼요.
