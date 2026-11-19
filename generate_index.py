# -*- coding: utf-8 -*-
"""
Generates the comprehensive Wikipedia article for 이철현 (Lee Chul-hyun),
modeled after Korean Wikipedia's 장영실 page.
"""

all_books = [
    ("2026. 07.", "초등실과교육탐구(기술, 정보 영역)", "양성원", "저서", "공동", "6인", "academic ai"),
    ("2026. 03.", "2022 초등학교 실과 5 교과서", "㈜미래엔", "교과서", "책임", "10인", "textbook"),
    ("2026. 03.", "2022 초등학교 실과 6 교과서", "㈜미래엔", "교과서", "책임", "10인", "textbook"),
    ("2026. 03.", "2022 초등학교 실과 5 지도서", "㈜미래엔", "지도서", "책임", "10인", "textbook"),
    ("2026. 03.", "2022 초등학교 실과 6 지도서", "㈜미래엔", "지도서", "책임", "10인", "textbook"),
    ("2025. 03.", "2022 고등학교 기술·가정 교과서", "㈜미래엔", "교과서", "책임", "10인", "textbook"),
    ("2025. 03.", "2022 고등학교 기술·가정 지도서", "㈜미래엔", "지도서", "책임", "10인", "textbook"),
    ("2025. 03.", "2022 중학교 기술·가정 1 교과서", "㈜미래엔", "교과서", "책임", "10인", "textbook"),
    ("2025. 03.", "2022 중학교 기술·가정 2 교과서", "㈜미래엔", "교과서", "책임", "10인", "textbook"),
    ("2025. 03.", "2022 중학교 기술·가정 1 지도서", "㈜미래엔", "지도서", "책임", "10인", "textbook"),
    ("2025. 03.", "2022 중학교 기술·가정 2 지도서", "㈜미래엔", "지도서", "책임", "10인", "textbook"),
    ("2024. 02.", "에듀테크와 학교 교육", "지식과감성", "저서", "공동", "10인", "academic ai"),
    ("2024. 01.", "2022 직업계고 전문공통과목 《디지털과 직업생활》", "㈜씨마스", "교과서", "공동", "8인", "textbook ai"),
    ("2021. 06.", "2015 고등학교 인공지능 기초 교과서", "㈜미래엔", "교과서", "책임", "8인", "textbook ai"),
    ("2020. 05.", "목재교육방법론", "산림청", "저서", "책임", "5인", "academic"),
    ("2019. 03.", "2015 초등학교 실과 5 교과서", "㈜미래엔", "교과서", "책임", "10인", "textbook"),
    ("2019. 03.", "2015 초등학교 실과 6 교과서", "㈜미래엔", "교과서", "책임", "10인", "textbook"),
    ("2019. 03.", "2015 초등학교 실과 5 지도서", "㈜미래엔", "지도서", "책임", "10인", "textbook"),
    ("2019. 03.", "2015 초등학교 실과 6 지도서", "㈜미래엔", "지도서", "책임", "10인", "textbook"),
    ("2018. 12.", "과학이 좋아지는 STEAM 융합이 즐겁다: 고등학교 1편", "교육부/한국과학창의재단", "저서", "책임", "10인", "academic"),
    ("2018. 03.", "2015 고등학교 기술·가정 교과서 및 지도서", "㈜미래엔", "교과서", "책임", "10인", "textbook"),
    ("2018. 03.", "2015 중학교 기술·가정 1·2 교과서 및 지도서", "㈜미래엔", "교과서", "공동", "10인", "textbook"),
    ("2018. 02.", "4차 산업혁명시대, 교육", "책과 공간", "저서", "공동", "11인", "academic"),
    ("2018. 01.", "초등실과교육", "양서원", "저서", "공동", "39인", "academic"),
    ("2016. 12.", "엔트리와 함께 하는 어린이 코딩", "㈜미래엔", "저서", "책임", "2인", "academic ai"),
    ("2016. 02.", "소프트웨어 교육의 이해와 실제", "양서원", "저서", "책임", "3인", "academic ai"),
    ("2015. 02.", "실과교육", "양서원", "저서", "공동", "27인", "academic"),
    ("2013. 03.", "교사를 위한 게임 중독 힐링 가이드", "이담북스", "저서", "공동", "2인", "academic"),
    ("2011. 08.", "놀이로 풀어보는 암호세상 step 1", "북스힐 / 이치사이언스", "저서", "공동", "2인", "academic"),
    ("2011. 08.", "놀이로 풀어보는 암호세상 step 2", "북스힐 / 이치사이언스", "저서", "공동", "2인", "academic"),
    ("2007. 03.", "2007 중학교 기술·가정 교과서 및 지도서", "교학사", "교과서", "공동", "10인", "textbook"),
    ("2003. 08.", "실과교육학 이론편 / 내용편", "도서출판 엘리트", "저서", "공동", "7인", "academic"),
    ("2000. 03.", "정보소양인증 워크북", "동아닷컴", "저서", "공동", "4인", "academic"),
    ("2001. 08.", "ICT 교육론", "형설출판사", "저서", "공동", "3인", "academic"),
    ("2002. 01.", "네티켓 교실", "형설출판사", "저서", "공동", "3인", "academic")
]

all_projects = [
    ("2026.10 ~ 2027.09", "2026년 초등학교 방과후 프로그램 공급 사업 (방학 집중형 - 수도권)", "300,000", "한국과학창의재단", "공동연구원"),
    ("2026.07 ~ 2027.06", "2026년 초등 방과후 프로그램 강사 연수 운영 사업", "600,000", "한국과학창의재단", "공동연구원"),
    ("2026.03 ~ 2027.02", "2026년 초등학교 방과후 프로그램 공급 사업 (소외지역 지원형)", "100,000", "한국과학창의재단", "공동연구원"),
    ("2025.12 ~ 2026.05", "인공지능시대 도래에 따른 교육과정 구성 방향 탐색 연구", "60,000", "국가교육위원회", "공동연구원"),
    ("2025.03 ~ 2025.06", "학습활동 데이터 분석 시나리오 연구", "45,000", "㈜ 크롤에이아이", "연구책임자"),
    ("2024.07 ~ 2025.02", "2학기 초1 늘봄교육프로그램 개발 및 운영", "320,000", "한국과학창의재단", "공동연구원"),
    ("2024.03 ~ 2024.08", "초1 늘봄교육프로그램 개발 및 운영", "400,000", "한국과학창의재단", "공동연구원"),
    ("2024.05 ~ 2024.12", "디지털 기반 유치원 운영 지원 자료 개발 연구", "99,000", "경기도교육청", "공동연구원"),
    ("2023.11 ~ 2024.02", "늘봄교육프로그램 개발 및 운영", "500,000", "한국과학창의재단", "공동연구원"),
    ("2023.07 ~ 2024.01", "2022 교육과정 개정에 따른 초등 인공지능교육을 위한 에듀테크 적용 방안", "5,000", "경인교육대학교", "연구책임자"),
    ("2023.05 ~ 2023.10", "학생용 온라인 AI 체험 콘텐츠 기획", "20,000", "네이버 커넥트재단", "연구책임자"),
    ("2022.08 ~ 2022.12", "초등학교 실과 기술 영역 SW와 로봇 관련 AI 교재 개발", "54,500", "네이버 커넥트재단", "공동연구원"),
    ("2022.07 ~ 2023.06", "플립러닝 기반 맞춤형 모듈식 EPL 프로그래밍 수업에서 온라인 소통플랫폼 적용 효과", "25,000", "한국연구재단", "연구책임자"),
    ("2022.06 ~ 2022.12", "2022 개정 교육과정 개발을 위한 의견 수렴 분석", "180,000", "강원도교육청", "공동연구원"),
    ("2022.06 ~ 2022.12", "2022 직업계고 교육과정 개정 각론 시안 개발 연구", "60,000", "한국직업능력연구원", "공동연구원"),
    ("2018.07 ~ 2021.06", "오류유형 분석을 통한 맞춤형 모듈식 EPL 교육프로그램 개발 (1~3차년도)", "60,000", "한국연구재단", "연구책임자"),
    ("2019.03 ~ 2020.12", "인천 인공지능교육 표준안 및 가이드라인 개발", "15,000", "인천광역시교육청", "공동연구원"),
    ("2016.07 ~ 2017.06", "소프트웨어 교육을 위한 컴퓨팅 사고력 기반 실생활 문제해결학습(CT-RLPS) 모형 개발 및 적용", "25,000", "한국연구재단", "연구책임자"),
    ("2016.05 ~ 2016.08", "2015 개정 교육과정에 따른 초등학교 실과 소프트웨어 교육의 방향", "30,000", "네이버 커넥트재단", "공동연구원"),
    ("2015.05 ~ 2015.10", "CS Unplugged 3.1 교안 개발", "17,000", "네이버 커넥트재단", "연구책임자")
]

books_html_rows = ""
for b in all_books:
    role_str = f"<b>{b[4]}</b>" if b[4] == "책임" else b[4]
    books_html_rows += f'''
              <tr data-category="{b[6]}">
                <td class="text-center nowrap">{b[0]}</td>
                <td><b>{b[1]}</b></td>
                <td>{b[2]}</td>
                <td class="text-center">{b[3]}</td>
                <td class="text-center">{role_str}</td>
                <td class="text-center nowrap">{b[5]}</td>
              </tr>'''

projects_html_rows = ""
for p in all_projects:
    role_str = f"<b>{p[4]}</b>" if p[4] == "연구책임자" else p[4]
    projects_html_rows += f'''
              <tr>
                <td class="text-center nowrap">{p[0]}</td>
                <td><b>{p[1]}</b></td>
                <td class="text-right nowrap">{p[2]}천 원</td>
                <td>{p[3]}</td>
                <td class="text-center nowrap">{role_str}</td>
              </tr>'''

full_html = f'''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>이철현 - 위키백과, 우리 모두의 백과사전</title>
  <link rel="stylesheet" href="css/style.css">
  <link rel="icon" href="assets/wikipedia-logo.svg" type="image/svg+xml">
</head>
<body>

  <!-- 1. TOP HEADER (Wikipedia Vector 2022 Navigation) -->
  <header class="wiki-header">
    <div class="header-left">
      <button class="btn-icon" id="mobile-menu-btn" title="주 메뉴" aria-label="주 메뉴">
        <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M3 5h14a1 1 0 010 2H3a1 1 0 010-2zm0 4h14a1 1 0 010 2H3a1 1 0 010-2zm0 4h14a1 1 0 010 2H3a1 1 0 010-2z" clip-rule="evenodd"/>
        </svg>
      </button>
      <a href="index.html" class="wiki-brand" title="위키백과 대문으로 가기">
        <img src="assets/wikipedia-logo.svg" alt="위키백과 로고">
      </a>
    </div>

    <div class="header-center">
      <div class="search-box">
        <svg class="search-icon" width="16" height="16" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd"/>
        </svg>
        <input type="text" id="wiki-search-input" placeholder="위키백과 검색 (예: 개요, 교과서, 늘봄학교, 연구과제, 논문...)" autocomplete="off">
        <div id="search-dropdown" class="search-dropdown"></div>
      </div>
    </div>

    <div class="header-right">
      <button class="nav-text-btn" id="theme-toggle-btn" title="야간 모드 전환">
        🌙 <span>야간 모드</span>
      </button>
      <button class="nav-text-btn" id="font-size-btn" title="글자 크기 조절">
        <span style="font-weight:bold;">A<sup>±</sup></span> <span>글자크기</span>
      </button>
      <a href="#" class="nav-text-btn edit-trigger" title="새 계정 만들기">계정 만들기</a>
      <a href="#" class="nav-text-btn edit-trigger" title="로그인">로그인</a>
    </div>
  </header>

  <!-- 2. WIKIPEDIA BODY CONTAINER -->
  <div class="wiki-container">

    <!-- LEFT STICKY TABLE OF CONTENTS -->
    <aside class="wiki-sidebar">
      <div class="toc-header">
        <span class="toc-title">목차</span>
        <button class="toc-toggle" id="toc-toggle">숨기기</button>
      </div>
      <ul class="toc-list" id="toc-list">
        <li class="toc-item">
          <a href="#개요" class="toc-link active"><span class="toc-number">1</span> 개요</a>
        </li>
        <li class="toc-item">
          <a href="#생애_및_학력" class="toc-link"><span class="toc-number">2</span> 생애 및 학력</a>
          <ul class="toc-sublist">
            <li><a href="#학업_및_초기_연구" class="toc-link"><span class="toc-number">2.1</span> 학업 및 초기 연구</a></li>
            <li><a href="#석박사_학위논문" class="toc-link"><span class="toc-number">2.2</span> 석·박사 학위논문</a></li>
          </ul>
        </li>
        <li class="toc-item">
          <a href="#주요_경력_및_보직" class="toc-link"><span class="toc-number">3</span> 주요 경력 및 보직</a>
          <ul class="toc-sublist">
            <li><a href="#교수_임용_및_교내_보직" class="toc-link"><span class="toc-number">3.1</span> 교수 임용 및 교내 주요 보직</a></li>
            <li><a href="#해외_방문연구_및_대외활동" class="toc-link"><span class="toc-number">3.2</span> 해외 방문연구 및 정부 자문</a></li>
            <li><a href="#학회_활동_및_리더십" class="toc-link"><span class="toc-number">3.3</span> 학술단체 리더십</a></li>
          </ul>
        </li>
        <li class="toc-item">
          <a href="#연구_및_교육과정_개발_업적" class="toc-link"><span class="toc-number">4</span> 연구 및 교육과정 개발 업적</a>
          <ul class="toc-sublist">
            <li><a href="#국가_교육과정_및_교과서_개발" class="toc-link"><span class="toc-number">4.1</span> 국가 교육과정 및 표준 교과서 편찬</a></li>
            <li><a href="#인공지능_및_소프트웨어_교육_연구" class="toc-link"><span class="toc-number">4.2</span> AI 및 SW 교육 패러다임 선도</a></li>
            <li><a href="#늘봄학교_및_국가_교육사업" class="toc-link"><span class="toc-number">4.3</span> 초등 늘봄학교 및 방과후 교육 프로그램</a></li>
            <li><a href="#주요_연구과제_수행_실적" class="toc-link"><span class="toc-number">4.4</span> 주요 연구과제(사업) 수행 실적</a></li>
            <li><a href="#STEAM_융합인재교육_체계화" class="toc-link"><span class="toc-number">4.5</span> STEAM·로봇·발명 교육 체계화</a></li>
          </ul>
        </li>
        <li class="toc-item">
          <a href="#저역서_목록" class="toc-link"><span class="toc-number">5</span> 저역서 목록</a>
        </li>
        <li class="toc-item">
          <a href="#주요_학술논문" class="toc-link"><span class="toc-number">6</span> 주요 학술논문</a>
        </li>
        <li class="toc-item">
          <a href="#학술대회_발표_및_기조강연" class="toc-link"><span class="toc-number">7</span> 학술대회 발표 및 기조강연</a>
        </li>
        <li class="toc-item">
          <a href="#수상_내역" class="toc-link"><span class="toc-number">8</span> 수상 내역</a>
        </li>
        <li class="toc-item">
          <a href="#평가_및_영향" class="toc-link"><span class="toc-number">9</span> 평가 및 영향</a>
        </li>
        <li class="toc-item">
          <a href="#같이_보기" class="toc-link"><span class="toc-number">10</span> 같이 보기</a>
        </li>
        <li class="toc-item">
          <a href="#각주" class="toc-link"><span class="toc-number">11</span> 각주</a>
        </li>
        <li class="toc-item">
          <a href="#바깥_고리" class="toc-link"><span class="toc-number">12</span> 바깥 고리</a>
        </li>
      </ul>
    </aside>

    <!-- MAIN ARTICLE CONTENT -->
    <main class="wiki-main">
      
      <!-- Article Header & Tabs -->
      <div class="article-header">
        <div class="article-toolbar">
          <div class="tab-group">
            <button class="wiki-tab active">문서</button>
            <button class="wiki-tab edit-trigger">토론</button>
          </div>
          <div class="tab-group">
            <button class="wiki-tab active">읽기</button>
            <button class="wiki-tab edit-trigger">편집</button>
            <button class="wiki-tab edit-trigger">역사 보기</button>
            <button class="wiki-tab" title="이 문서를 주시 목록에 추가">★</button>
            <button class="wiki-tab edit-trigger">도구 ▾</button>
          </div>
        </div>

        <div class="page-title-row">
          <h1 class="page-title">이철현</h1>
          <button class="page-lang-btn">
            🌐 <span>0개 언어</span> ▾
          </button>
        </div>
        <div class="site-sub">위키백과, 우리 모두의 백과사전.</div>
      </div>

      <!-- Hatnote Notice -->
      <div class="hatnote">
        이 문서는 대한민국의 컴퓨터교육학자이자 경인교육대학교 교수인 이철현에 관한 것입니다. 조선 전기의 과학자 장영실에 대해서는 <a href="https://ko.wikipedia.org/wiki/%EC%9E%A5%EC%98%81%EC%8B%A4" target="_blank" rel="noopener">장영실</a> 문서를 참고하십시오.
      </div>

      <!-- ARTICLE BODY & INFOBOX -->
      <article class="wiki-content">

        <!-- INFOBOX (인물 정보 상자) -->
        <table class="infobox biography vcard">
          <thead>
            <tr>
              <th colspan="2" class="infobox-title">이철현</th>
            </tr>
            <tr>
              <td colspan="2" class="infobox-subtitle">李哲賢 | Lee, Chul Hyun</td>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td colspan="2" class="infobox-image-cell">
                <div class="infobox-portrait-wrap">
                  <img id="portrait-img" src="assets/professor-portrait.svg" alt="이철현 교수 초상">
                </div>
                <div class="infobox-photo-actions">
                  <button type="button" class="photo-change-btn" id="photo-change-btn" title="사진 업로드 / 교체">📷 사진 변경</button>
                  <input type="file" id="photo-upload-input" accept="image/*" style="display:none;">
                </div>
                <div class="infobox-caption">경인교육대학교 생활과학교육과 교수<br>전 학습자중심교과교육학회 회장</div>
              </td>
            </tr>
            <tr>
              <th scope="row">출생</th>
              <td>1971년 2월 24일 (55세)<br><span class="flagicon">🇰🇷</span> 대한민국</td>
            </tr>
            <tr>
              <th scope="row">국적</th>
              <td>대한민국</td>
            </tr>
            <tr>
              <th scope="row">학력</th>
              <td>
                <a href="#학업_및_초기_연구">한국교원대학교</a> 수학교육 (교육학사, 1993)<br>
                한국교원대학교 컴퓨터교육 (교육학석사, 1995)<br>
                한국교원대학교 컴퓨터교육 (교육학박사 Ph.D., 2002)
              </td>
            </tr>
            <tr>
              <th scope="row">지도교수</th>
              <td>이태욱</td>
            </tr>
            <tr>
              <th scope="row">직업</th>
              <td>교육학자, 대학교수</td>
            </tr>
            <tr>
              <th scope="row">소속</th>
              <td>
                <a href="https://www.gin.ac.kr" target="_blank" rel="noopener">경인교육대학교</a> 생활과학교육과 교수
              </td>
            </tr>
            <tr>
              <th scope="row">주요 보직</th>
              <td>
                경인교육대학교 연구처장·산학협력단장<br>
                창의·인성교육연구소 소장<br>
                발명교육센터 센터장<br>
                로봇창의교육센터 센터장<br>
                융합인재교육대학원 전공주임 (전)
              </td>
            </tr>
            <tr>
              <th scope="row">학회 활동</th>
              <td>
                <a href="http://www.kalci.net" target="_blank" rel="noopener">학습자중심교과교육학회</a> 제12대 회장<br>
                <a href="http://www.koraie.org" target="_blank" rel="noopener">한국인공지능교육학회</a> 부회장·기획이사<br>
                한국공학교육학회 편집위원<br>
                한국실과교육학회 이사<br>
                실과교육연구학회 이사
              </td>
            </tr>
            <tr>
              <th scope="row">전문 분야</th>
              <td>
                컴퓨터교육, 인공지능(AI) 교육, 초등 실과 및 기술·가정 교육, STEAM 융합교육, 발명·로봇교육
              </td>
            </tr>
            <tr>
              <th scope="row">대표 저작</th>
              <td>
                2022 개정 초등 실과 5·6 교과서 집필책임<br>
                2022 개정 중·고교 기술·가정 교과서 집필책임<br>
                2015 고등학교 인공지능 기초 교과서 집필책임<br>
                《초등실과교육탐구》, 《에듀테크와 학교 교육》
              </td>
            </tr>
            <tr>
              <th scope="row">상훈</th>
              <td>
                부총리 겸 교육부장관상 (2023)<br>
                경인교육대학교 대학원 강의우수교수상 (2023)<br>
                사단법인 한국발명교육학회 우수논문상 (2012)
              </td>
            </tr>
            <tr>
              <th scope="row">웹사이트 / 연락</th>
              <td>
                <a href="mailto:leesleek@gin.ac.kr">leesleek@gin.ac.kr</a><br>
                (연구실) 031-470-6285
              </td>
            </tr>
          </tbody>
        </table>

        <!-- LEAD PARAGRAPHS -->
        <p>
          <b>이철현</b>(李哲賢, 1971년 2월 24일 ~ )은 대한민국의 컴퓨터교육학자이자 대학교수이다.<sup id="cite_ref-1" class="reference"><a href="#cite_note-1">[1]</a></sup> 현재 <a href="https://www.gin.ac.kr" target="_blank" rel="noopener">경인교육대학교</a> 생활과학교육과 교수로 재직 중이다.<sup id="cite_ref-2" class="reference"><a href="#cite_note-2">[2]</a></sup>
        </p>

        <p>
          대한민국 초·중·고등학교의 정보·컴퓨터 교육 및 인공지능(AI) 교육과정 수립과 국가 검정·인정 표준 교과서 편찬을 주도해 온 대표적인 학자이다. <a href="#">2015 개정 교육과정</a> 및 <a href="#">2022 개정 교육과정</a>에서 초등학교 실과(5·6학년)와 중학교 및 고등학교 기술·가정 교과서, 그리고 대한민국 최초의 정규 고등학교 <b>《인공지능 기초》</b> 교과서의 대표 집필책임자를 역임하였다.<sup id="cite_ref-3" class="reference"><a href="#cite_note-3">[3]</a></sup><sup id="cite_ref-4" class="reference"><a href="#cite_note-4">[4]</a></sup>
        </p>

        <p>
          또한 국가교육위원회, 한국과학창의재단, 교육부, 한국교육학술정보원(KERIS) 등과 긴밀히 협력하여 초등 늘봄학교 프로그램 개발·운영, 인공지능 교육과정 표준 모형 수립, 컴퓨팅 사고력(Computational Thinking) 기반 교수학습 모형(CT-RLPS) 구축에 중추적 역할을 수행하였다.<sup id="cite_ref-5" class="reference"><a href="#cite_note-5">[5]</a></sup> 학계에서는 <a href="http://www.kalci.net" target="_blank" rel="noopener">학습자중심교과교육학회</a> 제12대 회장을 역임하였으며, <a href="http://www.koraie.org" target="_blank" rel="noopener">한국인공지능교육학회</a> 부회장 및 기획이사로 활동하고 있다.<sup id="cite_ref-6" class="reference"><a href="#cite_note-6">[6]</a></sup>
        </p>

        <!-- SECTION 1: 개요 -->
        <h2 id="개요" class="wiki-heading-2">
          <span>1 개요</span>
          <span class="heading-edit edit-trigger">[편집]</span>
        </h2>
        <p>
          이철현은 1990년대 초 컴퓨터교육학 연구가 태동하던 시기부터 학문적 연구를 시작하여, 컴퓨터 및 정보 교육이 단순한 기능 습득을 넘어 미래 세대의 핵심 소양인 문제해결력과 <b>컴퓨팅 사고력(Computational Thinking)</b>, 나아가 <b>인공지능 문해력(AI Literacy)</b>으로 확장되는 전 과정을 이끈 교육학자이다.
        </p>
        <p>
          조선 전기 <a href="https://ko.wikipedia.org/wiki/%EC%9E%A5%EC%98%81%EC%8B%A4" target="_blank" rel="noopener">장영실</a>이 자격루와 앙부일구, 측우기 등을 개발하여 국가의 과학기술 표준 기구를 세우고 백성들의 생활 편의를 도모했던 것과 같이, 이철현은 대한민국 초·중등 공교육 현장에 표준화된 소프트웨어(SW) 및 인공지능(AI) 교육과정, 국정·검정 교과서, 맞춤형 모듈식 교육 프로그램 및 늘봄학교 교재를 설계·보급하여 국가 표준 교육 기틀을 정립한 인물로 평가받는다.<sup id="cite_ref-7" class="reference"><a href="#cite_note-7">[7]</a></sup>
        </p>

        <div class="quotebox">
          <div class="quotebox-quote">
            "인공지능과 생성형 AI의 시대에는 단순한 코드 작성을 가르치는 차원을 넘어, 인간 중심의 가치관과 컴퓨팅 사고력을 기반으로 실생활 문제를 창의적으로 해결할 수 있는 역량을 길러주는 것이 미래 공교육의 본질적 사명이다."
          </div>
          <div class="quotebox-author">— 이철현, 《디지털 인공지능 시대 교육&연구 5.0》 기조강연 (2024) 중</div>
        </div>

        <!-- SECTION 2: 생애 및 학력 -->
        <h2 id="생애_및_학력" class="wiki-heading-2">
          <span>2 생애 및 학력</span>
          <span class="heading-edit edit-trigger">[편집]</span>
        </h2>

        <h3 id="학업_및_초기_연구" class="wiki-heading-3">2.1 학업 및 초기 연구</h3>
        <p>
          이철현은 1971년 2월 24일 태어났다. 1989년 대한민국 교원 양성의 중심 고등교육기관인 <a href="https://ko.wikipedia.org/wiki/%ED%95%9C%EA%B5%AD%EA%B5%90%EC%9B%90%EB%8C%80%ED%95%99%EA%B5%90" target="_blank" rel="noopener">한국교원대학교</a> 수학교육과에 입학하여 1993년 2월 교육학사 학위를 취득함과 동시에 교육부 중등학교 정교사(2급) 자격을 취득하였다.<sup id="cite_ref-8" class="reference"><a href="#cite_note-8">[8]</a></sup>
        </p>
        <p>
          수학교육을 전공하며 논리적 사고와 컴퓨터 기술의 교육적 접목에 주목한 그는 한국교원대학교 대학원 컴퓨터교육전공으로 진학하여 대한민국 컴퓨터교육학의 원로인 이태욱 교수의 지도 아래 1995년 2월 교육학석사 학위를 취득하였다. 이어 박사과정에 진학하여 2002년 2월 교육학박사(Ph.D.) 학위를 취득하였다.
        </p>

        <h3 id="석박사_학위논문" class="wiki-heading-3">2.2 석·박사 학위논문</h3>
        <ul>
          <li><b>석사학위논문 (1995. 2.)</b>: 《물리적 시뮬레이션을 위한 과학교과용 저작 도구의 설계 및 구현》<sup id="cite_ref-9" class="reference"><a href="#cite_note-9">[9]</a></sup> — 당시 초기 컴퓨터 기반 교육(CBI) 환경에서 과학교과 교수학습을 위한 저작도구 구조를 제안하였다.</li>
          <li><b>박사학위논문 (2002. 2.)</b>: 《인터넷 기반의 문제 해결 학습을 위한 ICT-EUS와 지원 시스템 개발》<sup id="cite_ref-10" class="reference"><a href="#cite_note-10">[10]</a></sup> — 인터넷 초기 통신 기반 학습 환경에서 자기주도적 문제해결학습을 지원하는 시스템 아키텍처를 규명하여 학술적 주목을 받았다.</li>
        </ul>

        <!-- SECTION 3: 주요 경력 및 보직 -->
        <h2 id="주요_경력_및_보직" class="wiki-heading-2">
          <span>3 주요 경력 및 보직</span>
          <span class="heading-edit edit-trigger">[편집]</span>
        </h2>

        <h3 id="교수_임용_및_교내_보직" class="wiki-heading-3">3.1 교수 임용 및 교내 주요 보직</h3>
        <p>
          박사과정 수료 및 학위 취득 전후인 1999년부터 2003년까지 청주대학교 등 5개 대학에서 시간강사로 출강하였으며, 한국교원대학교 특별연구원 및 두뇌한국 21(BK21) Post-Doc.(박사후연구원) 과정을 거쳤다. 2003년 3월 경인교육대학교 생활과학교육과 교수로 임용되어 현재까지 교원 양성 및 대학원 연구에 헌신하고 있다.<sup id="cite_ref-1" class="reference"><a href="#cite_note-1">[1]</a></sup>
        </p>
        <p>
          경인교육대학교 재직 기간 동안 연구와 행정 역량을 두루 인정받아 다음과 같은 주요 교내 보직을 역임하였다:
        </p>
        <ul>
          <li><b>경인교육대학교 연구처장 / 산학협력단장</b> (2019.03 ~ 현재): 대학의 종합 연구 기획, 산학연 협력 과제 유치 및 국책 교육사업 총괄.</li>
          <li><b>창의·인성교육연구소 소장</b> (2012.03 ~ 현재): 융합적 창의성 및 인성 함양 교수학습 프로그램 연구.</li>
          <li><b>발명교육센터 센터장</b> (2012.09 ~ 현재): 초·중등 발명 인재 발굴 및 발명 영재 교육과정 운영.</li>
          <li><b>로봇창의교육센터 센터장</b> (2013.09 ~ 현재): 로봇 활용 교육 및 피지컬 컴퓨팅 교육 연구.</li>
          <li><b>STEAM교육센터 센터장</b> (2012.09 ~ 2015.02): 융합인재교육 모델 개발 및 확산.</li>
          <li><b>융합인재교육대학원 전공주임</b> (2012.03 ~ 2017.02): 현직 교사 대상 융합교육 전문 석사과정 주관.</li>
          <li><b>멘토링센터 / 미디어센터 소장 및 커리어개발센터 소장</b> (2011 ~ 2015): 예비교사 역량 강화 및 진로지도 총괄.</li>
        </ul>

        <h3 id="해외_방문연구_및_대외활동" class="wiki-heading-3">3.2 해외 방문연구 및 정부 자문</h3>
        <p>
          2009년 12월부터 2011년 2월까지 미국 캔자스 주에 위치한 명문 공립대학인 <b><a href="https://ko.wikipedia.org/wiki/%EC%BA%94%EC%9E%90%EC%8A%A4_%EB%8C%80%ED%95%99%EA%B5%90" target="_blank" rel="noopener">캔자스 대학교</a>(University of Kansas)</b>에서 방문교수(Visiting Professor)로 체류하며 미국의 STEM 교육 및 교육용 소프트웨어 연구 동향을 심층 분석하였다.<sup id="cite_ref-1" class="reference"><a href="#cite_note-1">[1]</a></sup>
        </p>
        <p>
          또한 국가 교육 정책 발전에 참여하여 2005년부터 <a href="https://ko.wikipedia.org/wiki/%ED%95%9C%EA%B5%AD%EA%B5%90%EC%9C%A1%ED%95%99%EC%88%A0%EC%A0%95%EB%B3%B4%EC%9B%90" target="_blank" rel="noopener">한국교육학술정보원(KERIS)</a> 원격연수원 평가위원으로 활동하고 있으며, <a href="https://ko.wikipedia.org/wiki/%ED%95%9C%EA%B5%AD%EA%B5%90%EC%9C%A1%EA%B3%BC%EC%A0%95%ED%8F%89%EA%B0%80%EC%9B%90" target="_blank" rel="noopener">한국교육과정평가원</a> 대학수학능력시험 프로그래밍 관련 교과 출제 및 검토위원(2005~2007)을 역임하였다. 2020년부터는 <a href="https://connect.or.kr" target="_blank" rel="noopener">네이버 커넥트재단</a> 초중등 SW교육 자문단 자문위원으로 참여하며 공교육과 민간 플랫폼의 협력을 이끌고 있다.<sup id="cite_ref-11" class="reference"><a href="#cite_note-11">[11]</a></sup>
        </p>

        <h3 id="학회_활동_및_리더십" class="wiki-heading-3">3.3 학술단체 리더십</h3>
        <p>
          학회 활동에서도 탁월한 리더십을 발휘하여 국내 대표 교육 학술단체들의 발전에 공헌하였다:
        </p>
        <ul>
          <li><b><a href="http://www.kalci.net" target="_blank" rel="noopener">학습자중심교과교육학회</a> 제12대 회장 (2021.01.01 ~ 2022.12.31)</b>: 전국 단위 교과교육 학자들의 학문 공동체를 대표하여 학술지 발행 및 학술대회를 성공적으로 이끌었으며, 부회장 및 학술위원장(2017.03 ~ 현재)을 맡고 있다.</li>
          <li><b><a href="http://www.koraie.org" target="_blank" rel="noopener">한국인공지능교육학회</a> 부회장 및 기획이사 (2020.01 ~ 현재)</b>: AI 교육 전문 학회 창립 및 정착에 기여하며 학술 교류를 견인하고 있다.</li>
          <li><b>한국공학교육학회 편집위원 (2017.01 ~ 현재)</b>: 공학교육 연구 논문의 질적 향상에 기여.</li>
          <li><b>한국실과교육학회 이사 (2015.03 ~ 현재)</b> 및 <b>실과교육연구학회 이사 (2003.03 ~ 현재)</b>.</li>
        </ul>

        <!-- SECTION 4: 연구 및 교육과정 개발 업적 -->
        <h2 id="연구_및_교육과정_개발_업적" class="wiki-heading-2">
          <span>4 연구 및 교육과정 개발 업적</span>
          <span class="heading-edit edit-trigger">[편집]</span>
        </h2>

        <h3 id="국가_교육과정_및_교과서_개발" class="wiki-heading-3">4.1 국가 교육과정 개발 및 표준 교과서 편찬</h3>
        <p>
          이철현은 대한민국 공교육 교과서 집필사에서 독보적인 족적을 남긴 학자이다. 2007 개정 교육과정 당시 초등 실과 및 중학 기술·가정 교과서의 정보영역 집필진으로 참여한 것을 시작으로, 2015 개정 및 2022 개정 교육과정에 이르기까지 초·중·고 교과서의 대표 집필책임자를 역임하였다.<sup id="cite_ref-3" class="reference"><a href="#cite_note-3">[3]</a></sup>
        </p>
        <ul>
          <li><b>2022 개정 교육과정 초등학교 실과 5·6학년 교과서 및 지도서 (미래엔, 2026 발행 예정)</b>: 집필책임자로서 초등학생의 디지털 기초 소양과 인공지능 윤리, 기초 알고리즘 단원을 혁신적으로 구성하였다.</li>
          <li><b>2022 개정 중학교 기술·가정 1·2 교과서 및 지도서 (미래엔, 2025 발행)</b>: 중등 단계의 기술적 문제 해결과 소프트웨어 융합 역량을 강화하였다.</li>
          <li><b>2022 개정 고등학교 기술·가정 교과서 및 지도서 (미래엔, 2025 발행)</b>: 공학적 설계와 디지털 전환 역량을 체계화하였다.</li>
          <li><b>2015 개정 고등학교 《인공지능 기초》 교과서 (미래엔, 2021)</b>: 대한민국 일반계·특목고 정규 과목으로 신설된 《인공지능 기초》 교과서의 집필책임자로서 고등학생 수준에 맞춘 기계학습, 딥러닝, 데이터 과학 및 인공지능 윤리의 기틀을 마련하였다.<sup id="cite_ref-4" class="reference"><a href="#cite_note-4">[4]</a></sup></li>
          <li><b>2022 개정 직업계고 전문공통과목 《디지털과 직업생활》 (씨마스, 2024)</b>: 직업계고 학생들을 위한 현장 중심 디지털 역량 교재를 개발하였다.</li>
        </ul>

        <h3 id="인공지능_및_소프트웨어_교육_연구" class="wiki-heading-3">4.2 인공지능(AI) 및 소프트웨어(SW) 교육 패러다임 선도</h3>
        <p>
          단순한 교재 집필에 머무르지 않고, 교육 현장에 적용 가능한 실증적 교수학습 모델을 직접 창안하였다.
        </p>
        <ul>
          <li><b>컴퓨팅 사고력 기반 실생활 문제해결학습(CT-RLPS) 모형</b>: 한국연구재단의 지원을 받아 개발한 독자적 교수학습 모형으로, 학습자가 일상생활의 문제를 발견하고 이를 분해, 추상화, 알고리즘 설계를 거쳐 프로그램으로 구현하는 일련의 과정을 정립하였다.<sup id="cite_ref-12" class="reference"><a href="#cite_note-12">[12]</a></sup></li>
          <li><b>모듈식 EPL(Educational Programming Language) 맞춤형 교육 프로그램</b>: 한국연구재단 3개년 연구과제를 통해 초등 예비교사 및 초등학생의 프로그래밍 오류 유형을 체계적으로 분류하고, 플립러닝(Flipped Learning) 기반 맞춤형 학습 모듈을 개발하여 보급하였다.<sup id="cite_ref-13" class="reference"><a href="#cite_note-13">[13]</a></sup></li>
          <li><b>생성형 AI 시대 초·중등 프로그래밍 교육의 방향</b>: 2026년 한국실과교육학회지에 게재된 단독 연구논문을 통해 대규모 언어 모델(LLM)과 AI 에이전트가 코딩 교육에 미치는 영향을 분석하고, 프롬프트 엔지니어링과 AI 협업 역량을 포함한 새로운 프로그래밍 교육 패러다임을 주창하였다.<sup id="cite_ref-14" class="reference"><a href="#cite_note-14">[14]</a></sup></li>
          <li><b>국제 기준 역량 분석</b>: 유네스코(UNESCO, 2024) AI 역량 체계에 기반하여 대한민국 초등교사들의 인공지능 교육 요구도를 분석하고 정책적 제언을 제시하였다.<sup id="cite_ref-15" class="reference"><a href="#cite_note-15">[15]</a></sup></li>
        </ul>

        <h3 id="늘봄학교_및_국가_교육사업" class="wiki-heading-3">4.3 초등 늘봄학교 및 방과후 교육 프로그램</h3>
        <p>
          교육부와 한국과학창의재단이 국가 중점 과제로 추진하는 초등 <b>늘봄학교</b>의 성공적 안착을 위하여 다수의 대형 연구사업을 수행하였다:
        </p>
        <ul>
          <li><b>2024~2025 초1 늘봄교육프로그램 개발 및 운영</b>: 한국과학창의재단 국책과제(총 사업비 12억 원 이상 규모)의 핵심 연구진으로 참여하여, 초등학교 1학년 신입생들의 학교 적응과 창의력 신장을 위한 디지털·신체놀이·융합 활동 프로그램을 설계하고 전국 시도교육청에 보급하였다.<sup id="cite_ref-5" class="reference"><a href="#cite_note-5">[5]</a></sup></li>
          <li><b>초등 방과후 프로그램 강사 연수 운영 사업</b>: 2026년 6억 원 규모의 강사 전문성 향상 연수 과정을 총괄 기획하였다.</li>
          <li><b>방과후 프로그램 공급 사업 (수도권 방학집중형 및 소외지역 지원형)</b>: 도서벽지 및 교육 소외지역 학생들에게 양질의 디지털·SW 교육 기회를 제공하기 위한 지원 체계를 구축하였다.</li>
        </ul>

        <!-- SUBSECTION 4.4: 주요 연구과제 수행 실적 -->
        <h3 id="주요_연구과제_수행_실적" class="wiki-heading-3">4.4 주요 연구과제(사업) 수행 실적</h3>
        <p>국가 공공기관, 교육부, 한국연구재단, 한국과학창의재단 및 교육청과 함께 수행한 대표적인 연구과제 목록이다.<sup id="cite_ref-5" class="reference"><a href="#cite_note-5">[5]</a></sup></p>

        <div class="table-wrap">
          <table class="wikitable">
            <thead>
              <tr>
                <th style="width: 15%;">연구 기간</th>
                <th style="width: 42%;">연구 과제명</th>
                <th style="width: 13%;">연구비</th>
                <th style="width: 18%;">지원 기관</th>
                <th style="width: 12%;">역할</th>
              </tr>
            </thead>
            <tbody>
              {projects_html_rows}
            </tbody>
          </table>
        </div>

        <h3 id="STEAM_융합인재교육_체계화" class="wiki-heading-3">4.5 STEAM·로봇·발명 교육 체계화</h3>
        <p>
          경인교육대학교 발명교육센터장 및 로봇창의교육센터장으로서 피지컬 컴퓨팅, 엔트리(Entry), 아두이노(Arduino), 마이크로비트(micro:bit), 3D 프린터 및 메이커 교육을 초등 교육과정과 연계한 실천적 연구를 주도하였다. 2018년 교육부 및 한국과학창의재단의 《과학이 좋아지는 STEAM 융합이 즐겁다》 고등학교편을 책임 집필하였으며, 미래직업 연계형 메이커 문화 확산에 기여하였다.<sup id="cite_ref-16" class="reference"><a href="#cite_note-16">[16]</a></sup>
        </p>

        <!-- SECTION 5: 저역서 목록 -->
        <h2 id="저역서_목록" class="wiki-heading-2">
          <span>5 저역서 목록</span>
          <span class="heading-edit edit-trigger">[편집]</span>
        </h2>
        <p>이철현 교수가 집필 책임 또는 공동 저술한 35종 이상의 주요 교과서, 지도서 및 학술 저서 목록이다.<sup id="cite_ref-3" class="reference"><a href="#cite_note-3">[3]</a></sup></p>

        <div class="table-filter-bar">
          <span style="font-weight:bold; font-size:0.85rem; margin-right:4px;">분류 필터:</span>
          <button class="filter-chip active" data-filter="all">전체 보기 (35종)</button>
          <button class="filter-chip" data-filter="textbook">교과서 / 지도서</button>
          <button class="filter-chip" data-filter="academic">학술서 / 단행본</button>
          <button class="filter-chip" data-filter="ai">AI / SW 교육</button>
        </div>

        <div class="table-wrap">
          <table class="wikitable sortable" id="books-table">
            <thead>
              <tr>
                <th style="width: 10%;">발행연월</th>
                <th style="width: 38%;">저역서명</th>
                <th style="width: 20%;">발행처</th>
                <th style="width: 12%;">구분</th>
                <th style="width: 10%;">역할</th>
                <th style="width: 10%;">저자 수</th>
              </tr>
            </thead>
            <tbody>
              {books_html_rows}
            </tbody>
          </table>
        </div>

        <!-- SECTION 6: 주요 학술논문 -->
        <h2 id="주요_학술논문" class="wiki-heading-2">
          <span>6 주요 학술논문</span>
          <span class="heading-edit edit-trigger">[편집]</span>
        </h2>
        <p>한국연구재단 등재학술지(KCI) 및 국제 학술지에 게재된 대표 연구논문 선별 목록이다.<sup id="cite_ref-17" class="reference"><a href="#cite_note-17">[17]</a></sup></p>

        <div class="table-wrap">
          <table class="wikitable">
            <thead>
              <tr>
                <th style="width: 12%;">게재일자</th>
                <th style="width: 45%;">논문 제목</th>
                <th style="width: 25%;">게재 학술지</th>
                <th style="width: 10%;">역할</th>
                <th style="width: 8%;">저자</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="text-center nowrap">2026. 09.</td>
                <td>인공지능교육 교육과정 표준 모형(안) 개발 연구</td>
                <td>《교육과정연구》 44(3)</td>
                <td class="text-center">공동저자</td>
                <td class="text-center nowrap">11인</td>
              </tr>
              <tr>
                <td class="text-center nowrap">2026. 09.</td>
                <td>블록 기반 프로그래밍 교육에 AI 에이전트 적용 가능성 탐색</td>
                <td>《한국실과교육학회지》 39(3)</td>
                <td class="text-center">교신저자</td>
                <td class="text-center nowrap">2인</td>
              </tr>
              <tr>
                <td class="text-center nowrap">2026. 09.</td>
                <td><b>생성형 AI 시대, 초·중등 프로그래밍 교육의 방향</b></td>
                <td>《한국실과교육학회지》 39(3)</td>
                <td class="text-center"><b>책임자</b></td>
                <td class="text-center nowrap">단독</td>
              </tr>
              <tr>
                <td class="text-center nowrap">2026. 08.</td>
                <td>교육대학교 대학원생의 생성형 AI 활용 양상과 사용 빈도 영향 요인</td>
                <td>《홀리스틱융합교육연구》 30(3)</td>
                <td class="text-center">교신저자</td>
                <td class="text-center nowrap">3인</td>
              </tr>
              <tr>
                <td class="text-center nowrap">2026. 03.</td>
                <td>UNESCO(2024) 역량 체계에 기반한 초등교사의 AI 교육을 위한 교육요구도 분석</td>
                <td>《인공지능연구 논문지》 7(1)</td>
                <td class="text-center">교신저자</td>
                <td class="text-center nowrap">2인</td>
              </tr>
              <tr>
                <td class="text-center nowrap">2025. 12.</td>
                <td>2022 개정 실과 교과서 정보영역 비교 분석</td>
                <td>《한국실과교육학회지》 38(4)</td>
                <td class="text-center">교신저자</td>
                <td class="text-center nowrap">2인</td>
              </tr>
              <tr>
                <td class="text-center nowrap">2025. 12.</td>
                <td>2022 개정 초등학교 교육과정의 디지털·인공지능 관련 내용 분석</td>
                <td>《인공지능연구 논문지》 6(3)</td>
                <td class="text-center"><b>책임자</b></td>
                <td class="text-center nowrap">단독</td>
              </tr>
              <tr>
                <td class="text-center nowrap">2025. 03.</td>
                <td>실과교과 에듀테크 활용을 위한 체제적 교수 설계 모형 (TUEPA_ADDIE) 개발</td>
                <td>《한국실과교육학회지》 38(1)</td>
                <td class="text-center"><b>책임자</b></td>
                <td class="text-center nowrap">단독</td>
              </tr>
              <tr>
                <td class="text-center nowrap">2024. 03.</td>
                <td>플립러닝 기반 맞춤형 모듈식 EPL 프로그래밍 수업에서 온라인 소통플랫폼 적용 효과</td>
                <td>《한국실과교육학회지》 37(1)</td>
                <td class="text-center"><b>책임자</b></td>
                <td class="text-center nowrap">단독</td>
              </tr>
              <tr>
                <td class="text-center nowrap">2023. 09.</td>
                <td>2022 실과 교육과정 개정에 따른 정보 영역의 내용 구성과 교과서 개발 전략</td>
                <td>《한국실과교육학회지》 36(3)</td>
                <td class="text-center"><b>책임자</b></td>
                <td class="text-center nowrap">단독</td>
              </tr>
              <tr>
                <td class="text-center nowrap">2021. 12.</td>
                <td>인공지능 시대의 역량에 기초한 실과 정보교육과정 내용 체계 탐색</td>
                <td>《교육논총》 41(4)</td>
                <td class="text-center"><b>책임자</b></td>
                <td class="text-center nowrap">단독</td>
              </tr>
              <tr>
                <td class="text-center nowrap">2017. 09.</td>
                <td>소프트웨어교육을 위한 컴퓨팅 사고력 기반 실생활 문제해결(CT-RLPS)모형 개발</td>
                <td>《한국실과교육학회지》 30(3)</td>
                <td class="text-center"><b>책임자</b></td>
                <td class="text-center nowrap">단독</td>
              </tr>
              <tr>
                <td class="text-center nowrap">2016. 06.</td>
                <td>Effects of robot for teaching geometry to fourth graders</td>
                <td>《IJISME》 24(2)</td>
                <td class="text-center">공동저자</td>
                <td class="text-center nowrap">국제</td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- SECTION 7: 학술대회 발표 및 기조강연 -->
        <h2 id="학술대회_발표_및_기조강연" class="wiki-heading-2">
          <span>7 학술대회 발표 및 기조강연</span>
          <span class="heading-edit edit-trigger">[편집]</span>
        </h2>
        <ul>
          <li><b>기조강연 (2024. 11. 16.)</b>: 〈디지털 인공지능 시대 교육&연구 5.0〉 — 제54회 학습자중심교과교육학회 동계학술대회 (이화여자대학교).<sup id="cite_ref-18" class="reference"><a href="#cite_note-18">[18]</a></sup></li>
          <li><b>단독 발표 (2026. 08. 06.)</b>: 〈생성형 AI 시대 초중등 프로그래밍 교육의 방향〉 — 2026년 한국실과교육학회 하계학술대회 (부산교육대학교).</li>
          <li><b>단독 발표 (2025. 01. 09.)</b>: 〈AIX시대, 실과 교과의 에듀테크 활용 방안 탐색〉 — 2024 (사)한국실과교육학회 동계학술대회 (광주교육대학교).</li>
          <li><b>단독 발표 (2023. 08. 03.)</b>: 〈실과 교과서 내용 구성과 교과서 개발 전략: 정보 분야〉 — 2023년 한국실과교육학회 하계학술대회 (부산교육대학교).</li>
          <li><b>공동 발표 (2023. 11. 18.)</b>: 〈중학교 교사의 인공지능 활용 교육에 대한 인식 조사〉 — 제52회 학습자중심교과교육학회 추계학술대회 (서울교육대학교).</li>
        </ul>

        <!-- SECTION 8: 수상 내역 -->
        <h2 id="수상_내역" class="wiki-heading-2">
          <span>8 수상 내역</span>
          <span class="heading-edit edit-trigger">[편집]</span>
        </h2>
        <div class="table-wrap">
          <table class="wikitable">
            <thead>
              <tr>
                <th style="width: 15%;">연도</th>
                <th style="width: 45%;">수상명</th>
                <th style="width: 40%;">수여 기관 및 사유</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="text-center nowrap"><b>2023년</b></td>
                <td><b>부총리 겸 교육부장관 표창 (우수교수)</b></td>
                <td>대한민국 교육부 (초·중등 교육과정 및 교원 양성 공로)<sup id="cite_ref-19" class="reference"><a href="#cite_note-19">[19]</a></sup></td>
              </tr>
              <tr>
                <td class="text-center nowrap"><b>2023년</b></td>
                <td><b>경인교육대학교 대학원 강의우수교수상</b></td>
                <td>경인교육대학교 (대학원 연구 및 지도 우수 교원)</td>
              </tr>
              <tr>
                <td class="text-center nowrap"><b>2012년</b></td>
                <td><b>사단법인 한국발명교육학회 우수논문상</b></td>
                <td>사단법인 한국발명교육학회 (발명 및 융합교육 학술 발전 공로)</td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- SECTION 9: 평가 및 영향 -->
        <h2 id="평가_및_영향" class="wiki-heading-2">
          <span>9 평가 및 영향</span>
          <span class="heading-edit edit-trigger">[편집]</span>
        </h2>
        <p>
          이철현은 대한민국 정보·컴퓨터 교육 분야에서 이론적 학술 연구와 초·중등 학교 현장의 실제 교육과정·교과서 개발을 결합시킨 대표적인 학자로 평가받는다. 2000년대 초 ICT 교육론 및 네티켓 교실 교재 개발에서부터, 2010년대 피지컬 컴퓨팅과 엔트리 기반 코딩 교육, 2020년대 인공지능 기초 및 생성형 AI 교육에 이르기까지 대한민국의 기술 발전에 발맞추어 학교 교육의 체질 개선을 선제적으로 이끌어왔다.<sup id="cite_ref-7" class="reference"><a href="#cite_note-7">[7]</a></sup>
        </p>
        <p>
          특히 경인교육대학교의 수많은 초등 예비교사들을 양성하고, 현직 교사 대상의 직무연수 및 늘봄학교 강사 연수를 총괄함으로써 초등 공교육의 디지털 전환(DX)을 실질적으로 안착시켰다는 평가를 얻고 있다.
        </p>

        <!-- SECTION 10: 같이 보기 -->
        <h2 id="같이_보기" class="wiki-heading-2">
          <span>10 같이 보기</span>
          <span class="heading-edit edit-trigger">[편집]</span>
        </h2>
        <ul>
          <li><a href="https://ko.wikipedia.org/wiki/%EA%B2%BD%EC%9D%B8%EA%B5%90%EC%9C%A1%EB%8C%80%ED%95%99%EA%B5%90" target="_blank" rel="noopener">경인교육대학교</a></li>
          <li><a href="https://ko.wikipedia.org/wiki/%ED%95%9C%EA%B5%AD%EA%B5%90%EC%9C%A1%EB%8C%80%ED%95%99%EA%B5%90" target="_blank" rel="noopener">한국교원대학교</a></li>
          <li><a href="#">컴퓨팅 사고력</a></li>
          <li><a href="#">인공지능 교육</a></li>
          <li><a href="#">늘봄학교</a></li>
          <li><a href="#">2022 개정 교육과정</a></li>
          <li><a href="https://ko.wikipedia.org/wiki/%EC%9E%A5%EC%98%81%EC%8B%A4" target="_blank" rel="noopener">장영실</a> (조선 과학기술 표준을 정립한 선구자)</li>
        </ul>

        <!-- SECTION 11: 각주 -->
        <h2 id="각주" class="wiki-heading-2">
          <span>11 각주</span>
          <span class="heading-edit edit-trigger">[편집]</span>
        </h2>
        <ol class="references-list">
          <li id="cite_note-1">
            <span class="mw-cite-backlink"><a href="#cite_ref-1">↑</a></span>
            경인교육대학교 교수진 소개 - 생활과학교육과 이철현 교수 프로필 및 공식 인적사항.
          </li>
          <li id="cite_note-2">
            <span class="mw-cite-backlink"><a href="#cite_ref-2">↑</a></span>
            경인교육대학교 연구처 및 산학협력단 공식 기구표 (2019-2026).
          </li>
          <li id="cite_note-3">
            <span class="mw-cite-backlink"><a href="#cite_ref-3">↑</a></span>
            한국교과서연구재단 교과용도서 검정·인정 공고 및 ㈜미래엔 교과서 발행 목록 (2015, 2022 개정 실과·기술가정).
          </li>
          <li id="cite_note-4">
            <span class="mw-cite-backlink"><a href="#cite_ref-4">↑</a></span>
            이철현 외 7인, 《고등학교 인공지능 기초》 교과서, 미래엔, 2021년 6월.
          </li>
          <li id="cite_note-5">
            <span class="mw-cite-backlink"><a href="#cite_ref-5">↑</a></span>
            한국과학창의재단, 〈초1 늘봄교육프로그램 개발 및 운영 사업 결과보고서〉, 2024.
          </li>
          <li id="cite_note-6">
            <span class="mw-cite-backlink"><a href="#cite_ref-6">↑</a></span>
            학습자중심교과교육학회 임원 명단 (제12대 회장 이철현) 및 한국인공지능교육학회 임원 명단 (부회장).
          </li>
          <li id="cite_note-7">
            <span class="mw-cite-backlink"><a href="#cite_ref-7">↑</a></span>
            교육부 및 한국과학창의재단, 〈초·중등 SW·AI 교육 종합 발전방안 연구보고서〉.
          </li>
          <li id="cite_note-8">
            <span class="mw-cite-backlink"><a href="#cite_ref-8">↑</a></span>
            한국교원대학교 학위수여대장 및 교육부 교원자격검정령에 따른 중등학교 정교사(2급) 자격증 (1993. 2).
          </li>
          <li id="cite_note-9">
            <span class="mw-cite-backlink"><a href="#cite_ref-9">↑</a></span>
            이철현, 〈물리적 시뮬레이션을 위한 과학교과용 저작 도구의 설계 및 구현〉, 한국교원대학교 대학원 석사학위논문, 1995.
          </li>
          <li id="cite_note-10">
            <span class="mw-cite-backlink"><a href="#cite_ref-10">↑</a></span>
            이철현, 〈인터넷 기반의 문제 해결 학습을 위한 ICT-EUS와 지원 시스템 개발〉, 한국교원대학교 대학원 박사학위논문, 2002.
          </li>
          <li id="cite_note-11">
            <span class="mw-cite-backlink"><a href="#cite_ref-11">↑</a></span>
            네이버 커넥트재단, 소프트웨어 교육 플랫폼 엔트리(Entry) 자문위원단 명단 (2020~2026).
          </li>
          <li id="cite_note-12">
            <span class="mw-cite-backlink"><a href="#cite_ref-12">↑</a></span>
            이철현, 〈소프트웨어교육을 위한 컴퓨팅 사고력 기반 실생활 문제해결(CT-RLPS)모형 개발〉, 《한국실과교육학회지》, 30(3), 2017.
          </li>
          <li id="cite_note-13">
            <span class="mw-cite-backlink"><a href="#cite_ref-13">↑</a></span>
            한국연구재단 개인기초연구지원사업 과제 보고서, 〈오류유형 분석을 통한 맞춤형 모듈식 EPL 교육프로그램 개발〉, 2018-2021.
          </li>
          <li id="cite_note-14">
            <span class="mw-cite-backlink"><a href="#cite_ref-14">↑</a></span>
            이철현, 〈생성형 AI 시대, 초·중등 프로그래밍 교육의 방향〉, 《한국실과교육학회지》, 39(3), 155-189쪽, 2026.
          </li>
          <li id="cite_note-15">
            <span class="mw-cite-backlink"><a href="#cite_ref-15">↑</a></span>
            이철현 외, 〈UNESCO(2024) 역량 체계에 기반한 초등교사의 AI 교육을 위한 교육요구도 분석〉, 《인공지능연구 논문지》, 7(1), 2026.
          </li>
          <li id="cite_note-16">
            <span class="mw-cite-backlink"><a href="#cite_ref-16">↑</a></span>
            교육부·한국과학창의재단, 《과학이 좋아지는 STEAM 융합이 즐겁다: 고등학교 1편》, 2018.
          </li>
          <li id="cite_note-17">
            <span class="mw-cite-backlink"><a href="#cite_ref-17">↑</a></span>
            한국학술지인용색인(KCI) 연구자 업적 정보 - 이철현 교수 게재 논문 목록 (한국연구재단).
          </li>
          <li id="cite_note-18">
            <span class="mw-cite-backlink"><a href="#cite_ref-18">↑</a></span>
            학습자중심교과교육학회 제54회 동계학술대회 자료집, 이화여자대학교, 2024년 11월 16일.
          </li>
          <li id="cite_note-19">
            <span class="mw-cite-backlink"><a href="#cite_ref-19">↑</a></span>
            교육부 제42회 스승의 날 유공교원 정부포상 및 교육부장관 표창 대상자 명단, 2023.
          </li>
        </ol>

        <!-- SECTION 12: 바깥 고리 -->
        <h2 id="바깥_고리" class="wiki-heading-2">
          <span>12 바깥 고리</span>
          <span class="heading-edit edit-trigger">[편집]</span>
        </h2>
        <ul>
          <li><a href="https://www.gin.ac.kr" target="_blank" rel="noopener">경인교육대학교 공식 홈페이지</a></li>
          <li><a href="http://www.kalci.net" target="_blank" rel="noopener">학습자중심교과교육학회 공식 웹사이트</a></li>
          <li><a href="http://www.koraie.org" target="_blank" rel="noopener">한국인공지능교육학회 공식 웹사이트</a></li>
          <li><a href="https://www.kci.go.kr" target="_blank" rel="noopener">한국학술지인용색인(KCI) 연구자 정보 - 이철현</a></li>
          <li><a href="https://connect.or.kr" target="_blank" rel="noopener">네이버 커넥트재단 소프트웨어 교육</a></li>
          <li><a href="https://ko.wikipedia.org/wiki/%EC%9E%A5%EC%98%81%EC%8B%A4" target="_blank" rel="noopener">위키백과 "장영실" 문서 (원문 모티브)</a></li>
        </ul>

        <!-- NAVBOX (둘러보기 상자) -->
        <div class="navbox">
          <div class="navbox-title">
            경인교육대학교 연구처장 및 학술단체 리더십
            <button class="navbox-toggle" id="navbox-toggle-btn">[접기]</button>
          </div>
          <table class="navbox-table" id="navbox-body">
            <tbody>
              <tr>
                <th scope="row" class="navbox-group">소속 대학</th>
                <td class="navbox-list">
                  <a href="https://www.gin.ac.kr" target="_blank" rel="noopener">경인교육대학교</a>
                  <a href="#">생활과학교육과</a>
                  <a href="#">창의·인성교육연구소</a>
                  <a href="#">발명교육센터</a>
                  <a href="#">로봇창의교육센터</a>
                  <a href="#">융합인재교육대학원</a>
                </td>
              </tr>
              <tr>
                <th scope="row" class="navbox-group">학회 회장 및 임원</th>
                <td class="navbox-list">
                  <a href="http://www.kalci.net" target="_blank" rel="noopener">학습자중심교과교육학회 (전 회장/부회장)</a>
                  <a href="http://www.koraie.org" target="_blank" rel="noopener">한국인공지능교육학회 (부회장·기획이사)</a>
                  <a href="#">한국공학교육학회 (편집위원)</a>
                  <a href="#">한국실과교육학회 (이사)</a>
                  <a href="#">실과교육연구학회 (이사)</a>
                </td>
              </tr>
              <tr>
                <th scope="row" class="navbox-group">국가 교육과정 및 정책</th>
                <td class="navbox-list">
                  <a href="#">2022 개정 교육과정</a>
                  <a href="#">2015 개정 교육과정</a>
                  <a href="#">초등 늘봄학교</a>
                  <a href="#">고등학교 인공지능 기초</a>
                  <a href="#">초등 실과 정보영역</a>
                  <a href="#">컴퓨팅 사고력(CT-RLPS)</a>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- CATEGORIES BOX (분류) -->
        <div id="catlinks" class="catlinks">
          <span class="catlinks-title">분류:</span>
          <ul>
            <li><a href="#">1971년 출생</a></li>
            <li><a href="#">살아있는 사람</a></li>
            <li><a href="#">한국교원대학교 동문</a></li>
            <li><a href="#">경인교육대학교 교수</a></li>
            <li><a href="#">대한민국의 교육학자</a></li>
            <li><a href="#">컴퓨터 교육학자</a></li>
            <li><a href="#">인공지능 교육학자</a></li>
            <li><a href="#">2022 개정 교육과정 참여자</a></li>
            <li><a href="#">대한민국 교육부장관 표창 수훈자</a></li>
          </ul>
        </div>

      </article>
    </main>
  </div>

  <!-- 3. WIKIPEDIA FOOTER -->
  <footer class="wiki-footer">
    <div class="footer-content">
      <div class="footer-info">
        이 문서는 2026년 11월 19일 (목) 11:28에 마지막으로 편집되었습니다.<br>
        모든 문서는 <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.ko" target="_blank" rel="noopener">크리에이티브 커먼즈 저작자표시-동일조건변경허락 4.0</a>에 따라 사용할 수 있으며, 추가적인 조건이 적용될 수 있습니다. 자세한 내용은 <a href="#">이용 약관</a>을 참고하십시오.
      </div>
      <div class="footer-places">
        <a href="#">개인정보처리방침</a>
        <a href="#">위키백과 소개</a>
        <a href="#">면책 조항</a>
        <a href="#">행동 강령</a>
        <a href="#">개발자</a>
        <a href="#">통계</a>
        <a href="#">쿠키 정책</a>
        <a href="#">모바일 보기</a>
      </div>
    </div>
  </footer>

  <!-- 4. WIKITEXT EDIT MODAL SIMULATOR -->
  <div class="modal-overlay" id="edit-modal">
    <div class="wiki-modal">
      <div class="modal-header">
        <div class="modal-title">위키백과 문서 편집 — 이철현 (위키텍스트 편집기)</div>
        <button class="btn-icon" id="modal-close-btn" title="닫기">✕</button>
      </div>
      <div class="modal-body">
        <div style="font-size:0.85rem; color:var(--wiki-text-muted);">
          위키텍스트(마크업) 문법을 자유롭게 수정해 볼 수 있습니다. 변경사항은 현재 브라우저 세션에 반영됩니다.
        </div>
        <textarea class="wikitext-editor" id="wikitext-content" spellcheck="false"></textarea>
      </div>
      <div class="modal-footer">
        <button class="btn-secondary" id="modal-cancel-btn">취소</button>
        <button class="btn-primary" id="modal-save-btn">변경사항 저장</button>
      </div>
    </div>
  </div>

  <!-- Scripts -->
  <script src="js/app.js"></script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print('Updated index.html written successfully.')
