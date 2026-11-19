// Wikipedia Interactive Logic for 이철현 Wikipedia Article

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initFontSize();
  initTOC();
  initSearch();
  initRefTooltips();
  initTableFilter();
  initEditModal();
  initPhotoUploader();
  initNavboxToggle();
  initMobileMenu();
});

// 1. Theme Management (Light / Dark)
function initTheme() {
  const themeBtn = document.getElementById('theme-toggle-btn');
  const savedTheme = localStorage.getItem('wiki_theme') || 'light';
  applyTheme(savedTheme);

  if (themeBtn) {
    themeBtn.addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
      const next = current === 'dark' ? 'light' : 'dark';
      applyTheme(next);
      localStorage.setItem('wiki_theme', next);
    });
  }
}

function applyTheme(theme) {
  if (theme === 'dark') {
    document.documentElement.setAttribute('data-theme', 'dark');
    const themeBtn = document.getElementById('theme-toggle-btn');
    if (themeBtn) themeBtn.innerHTML = '☀️ <span>주간 모드</span>';
  } else {
    document.documentElement.removeAttribute('data-theme');
    const themeBtn = document.getElementById('theme-toggle-btn');
    if (themeBtn) themeBtn.innerHTML = '🌙 <span>야간 모드</span>';
  }
}

// 2. Font Size Adjustment
function initFontSize() {
  const fontBtn = document.getElementById('font-size-btn');
  const sizes = ['font-md', 'font-lg', 'font-sm'];
  let currentIdx = 0;

  const savedSize = localStorage.getItem('wiki_fontsize') || 'font-md';
  document.documentElement.className = savedSize;
  currentIdx = sizes.indexOf(savedSize) !== -1 ? sizes.indexOf(savedSize) : 0;

  if (fontBtn) {
    fontBtn.addEventListener('click', () => {
      currentIdx = (currentIdx + 1) % sizes.length;
      const nextSize = sizes[currentIdx];
      document.documentElement.className = nextSize;
      localStorage.setItem('wiki_fontsize', nextSize);
    });
  }
}

// 3. Table of Contents & Scrollspy
function initTOC() {
  const tocLinks = document.querySelectorAll('.toc-link');
  const sections = document.querySelectorAll('.wiki-heading-2, .wiki-heading-3');
  const tocToggle = document.getElementById('toc-toggle');
  const tocList = document.getElementById('toc-list');

  if (tocToggle && tocList) {
    tocToggle.addEventListener('click', () => {
      if (tocList.style.display === 'none') {
        tocList.style.display = 'block';
        tocToggle.textContent = '숨기기';
      } else {
        tocList.style.display = 'none';
        tocToggle.textContent = '보이기';
      }
    });
  }

  // Smooth scroll
  tocLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      const targetId = link.getAttribute('href').substring(1);
      const targetEl = document.getElementById(targetId);
      if (targetEl) {
        const offset = 70; // Header height + padding
        const bodyRect = document.body.getBoundingClientRect().top;
        const elementRect = targetEl.getBoundingClientRect().top;
        const elementPosition = elementRect - bodyRect;
        const offsetPosition = elementPosition - offset;

        window.scrollTo({
          top: offsetPosition,
          behavior: 'smooth'
        });

        // Close mobile drawer if open
        const sidebar = document.querySelector('.wiki-sidebar');
        if (sidebar && sidebar.classList.contains('mobile-open')) {
          sidebar.classList.remove('mobile-open');
        }
      }
    });
  });

  // IntersectionObserver for active section highlighting
  const observerOptions = {
    root: null,
    rootMargin: '-80px 0px -70% 0px',
    threshold: 0
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.id;
        tocLinks.forEach(l => {
          if (l.getAttribute('href') === `#${id}`) {
            l.classList.add('active');
          } else {
            l.classList.remove('active');
          }
        });
      }
    });
  }, observerOptions);

  sections.forEach(sec => {
    if (sec.id) observer.observe(sec);
  });
}

// 4. Live Search with Dropdown
function initSearch() {
  const searchInput = document.getElementById('wiki-search-input');
  const dropdown = document.getElementById('search-dropdown');

  const searchableSections = [
    { title: '개요 (Overview)', id: '개요', badge: '문서' },
    { title: '생애 및 학력', id: '생애_및_학력', badge: '생애' },
    { title: '한국교원대학교 학·석·박사', id: '학업_및_초기_연구', badge: '학력' },
    { title: '경인교육대학교 교수 임용', id: '교수_임용_및_교내_보직', badge: '경력' },
    { title: '미국 캔자스 대학교(KU) 방문교수', id: '해외_방문연구_및_대외활동', badge: '경력' },
    { title: '학습자중심교과교육학회 회장', id: '학회_활동_및_리더십', badge: '학회' },
    { title: '한국인공지능교육학회 부회장', id: '학회_활동_및_리더십', badge: '학회' },
    { title: '2022 개정 초등 실과 교과서', id: '국가_교육과정_및_교과서_개발', badge: '교과서' },
    { title: '2022 개정 중·고교 기술가정 교과서', id: '국가_교육과정_및_교과서_개발', badge: '교과서' },
    { title: '고등학교 인공지능 기초 교과서', id: '국가_교육과정_및_교과서_개발', badge: '교과서' },
    { title: '초등 늘봄학교 프로그램 개발', id: '늘봄학교_및_국가_교육사업', badge: '연구과제' },
    { title: '생성형 AI 시대 프로그래밍 교육', id: '인공지능_및_소프트웨어_교육_연구', badge: '논문' },
    { title: '컴퓨팅 사고력 실생활 문제해결(CT-RLPS)', id: '인공지능_및_소프트웨어_교육_연구', badge: '연구' },
    { title: '모듈식 EPL 교수학습 모델', id: '인공지능_및_소프트웨어_교육_연구', badge: '연구' },
    { title: 'STEAM 융합인재교육 및 발명·로봇', id: 'STEAM_융합인재교육_체계화', badge: '연구' },
    { title: '저서 및 교과서 목록', id: '저역서_목록', badge: '저서' },
    { title: '주요 학술논문 목록', id: '주요_학술논문', badge: '논문' },
    { title: '학술대회 발표 및 기조강연', id: '학술대회_발표_및_기조강연', badge: '학술' },
    { title: '부총리 겸 교육부장관상', id: '수상_내역', badge: '수상' },
    { title: '각주 및 참고문헌', id: '각주', badge: '참고' }
  ];

  if (searchInput && dropdown) {
    searchInput.addEventListener('input', (e) => {
      const q = e.target.value.trim().toLowerCase();
      if (!q) {
        dropdown.classList.remove('active');
        return;
      }

      const matches = searchableSections.filter(s => 
        s.title.toLowerCase().includes(q) || s.badge.toLowerCase().includes(q)
      );

      if (matches.length > 0) {
        dropdown.innerHTML = matches.map(m => `
          <div class="search-item" data-target="${m.id}">
            <span class="search-item-title">${m.title}</span>
            <span class="search-item-badge">${m.badge}</span>
          </div>
        `).join('');
        dropdown.classList.add('active');
      } else {
        dropdown.innerHTML = `<div class="search-item" style="color:var(--wiki-text-muted);">일치하는 항목이 없습니다.</div>`;
        dropdown.classList.add('active');
      }
    });

    dropdown.addEventListener('click', (e) => {
      const item = e.target.closest('.search-item');
      if (item && item.dataset.target) {
        const targetId = item.dataset.target;
        const el = document.getElementById(targetId);
        if (el) {
          dropdown.classList.remove('active');
          searchInput.value = '';
          const offset = 70;
          const bodyRect = document.body.getBoundingClientRect().top;
          const elementRect = el.getBoundingClientRect().top;
          const offsetPosition = elementRect - bodyRect - offset;
          window.scrollTo({ top: offsetPosition, behavior: 'smooth' });

          // Flash highlight
          el.style.transition = 'background-color 0.5s';
          el.style.backgroundColor = 'var(--wiki-highlight)';
          setTimeout(() => {
            el.style.backgroundColor = '';
          }, 1500);
        }
      }
    });

    document.addEventListener('click', (e) => {
      if (!searchInput.contains(e.target) && !dropdown.contains(e.target)) {
        dropdown.classList.remove('active');
      }
    });

    searchInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        const first = dropdown.querySelector('.search-item');
        if (first) first.click();
      }
    });
  }
}

// 5. Reference Tooltip Popover (Wikipedia Reference Previews)
function initRefTooltips() {
  const refLinks = document.querySelectorAll('sup.reference a');
  let tooltip = document.createElement('div');
  tooltip.className = 'ref-tooltip';
  document.body.appendChild(tooltip);

  let hideTimeout;

  refLinks.forEach(link => {
    link.addEventListener('mouseenter', (e) => {
      clearTimeout(hideTimeout);
      const refId = link.getAttribute('href').substring(1);
      const refTarget = document.getElementById(refId);
      if (refTarget) {
        // Clone text without backlink arrow
        let clone = refTarget.cloneNode(true);
        const backlink = clone.querySelector('.mw-cite-backlink');
        if (backlink) backlink.remove();

        tooltip.innerHTML = `<strong>참고문헌 [${link.textContent.replace(/[\[\]]/g, '')}]</strong><br>${clone.innerHTML}`;
        
        const rect = link.getBoundingClientRect();
        tooltip.style.left = `${Math.min(window.innerWidth - 380, Math.max(10, rect.left - 20))}px`;
        tooltip.style.top = `${rect.bottom + window.scrollY + 8}px`;
        tooltip.style.display = 'block';
      }
    });

    link.addEventListener('mouseleave', () => {
      hideTimeout = setTimeout(() => {
        tooltip.style.display = 'none';
      }, 300);
    });
  });

  tooltip.addEventListener('mouseenter', () => {
    clearTimeout(hideTimeout);
  });

  tooltip.addEventListener('mouseleave', () => {
    tooltip.style.display = 'none';
  });
}

// 6. Table Filter Chips for Books & Textbooks
function initTableFilter() {
  const filterBtns = document.querySelectorAll('.filter-chip');
  const bookRows = document.querySelectorAll('#books-table tbody tr');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const cat = btn.dataset.filter;

      bookRows.forEach(row => {
        if (cat === 'all') {
          row.style.display = '';
        } else {
          const rowCat = row.dataset.category;
          if (rowCat && rowCat.includes(cat)) {
            row.style.display = '';
          } else {
            row.style.display = 'none';
          }
        }
      });
    });
  });
}

// 7. Wikitext Edit Modal Simulator
function initEditModal() {
  const editBtns = document.querySelectorAll('.edit-trigger');
  const modal = document.getElementById('edit-modal');
  const closeBtn = document.getElementById('modal-close-btn');
  const cancelBtn = document.getElementById('modal-cancel-btn');
  const saveBtn = document.getElementById('modal-save-btn');
  const editor = document.getElementById('wikitext-content');

  const defaultWikitext = `{{인물 정보
| 이름 = 이철현
| 원어명 = 李哲賢 / Lee Chul Hyun
| 출생일 = {{출생일과 나이|1971|2|24}}
| 출생지 = 대한민국
| 국적 = 대한민국
| 학력 = 
* 한국교원대학교 수학교육과 (교육학사, 1993)
* 한국교원대학교 대학원 컴퓨터교육전공 (교육학석사, 1995)
* 한국교원대학교 대학원 컴퓨터교육전공 (교육학박사 Ph.D., 2002)
| 지도교수 = 이태욱
| 직업 = 대학교수, 교육학자
| 소속 = [[경인교육대학교]] 생활과학교육과 교수
| 주요 경력 = 
* 경인교육대학교 연구처장 / 산학협력단장 (2019~현재)
* 학습자중심교과교육학회 회장 (2021~2022)
* 한국인공지능교육학회 부회장 (2020~현재)
* 경인교육대학교 창의·인성교육연구소 소장 (2012~현재)
* 경인교육대학교 발명교육센터·로봇창의교육센터장
| 전문분야 = 컴퓨터교육, 인공지능(AI) 교육, 초등실과 및 기술가정 교육, STEAM 융합교육
| 주요 저서 = 
* 2022 개정 초등학교 실과 5·6 교과서 집필책임
* 2022 개정 중·고교 기술가정 교과서 집필책임
* 2015 고등학교 인공지능 기초 교과서 집필책임
| 상훈 = 
* 부총리 겸 교육부장관 표창 (우수교수, 2023)
* 경인교대 대학원 강의우수교수상 (2023)
}}

'''이철현'''(李哲賢, [[1971년]] [[2월 24일]] ~ )은 대한민국의 교육학자이자 교수이다. 현재 [[경인교육대학교]] 생활과학교육과 교수로 재직 중이다. 

대한민국 초·중등 정보 및 인공지능(AI) 교육과정 수립과 표준 교과서 편찬을 주도해 온 대표적인 학자이다. [[2015 개정 교육과정]] 및 [[2022 개정 교육과정]]에서 초등학교 실과, 중·고등학교 기술·가정, 고등학교 《인공지능 기초》 교과서의 대표 집필책임자를 역임하였다.

== 개요 ==
이철현 교수는 컴퓨터교육 및 인공지능 교육 분야의 석학으로, 대한민국 초·중등 교육 현장의 정보 교육 내실화와 융합인재교육(STEAM) 보급에 기여하였다...`;

  if (editor) {
    editor.value = defaultWikitext;
  }

  editBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      if (modal) modal.classList.add('active');
    });
  });

  const closeModal = () => {
    if (modal) modal.classList.remove('active');
  };

  if (closeBtn) closeBtn.addEventListener('click', closeModal);
  if (cancelBtn) cancelBtn.addEventListener('click', closeModal);
  if (saveBtn) {
    saveBtn.addEventListener('click', () => {
      alert('위키 편집 내용이 브라우저 세션에 임시 반영되었습니다.');
      closeModal();
    });
  }

  // Escape key closes modal
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal && modal.classList.contains('active')) {
      closeModal();
    }
  });
}

// 8. Custom Profile Photo Uploader
function initPhotoUploader() {
  const photoInput = document.getElementById('photo-upload-input');
  const photoBtn = document.getElementById('photo-change-btn');
  const portraitImg = document.getElementById('portrait-img');

  const savedPhoto = localStorage.getItem('wiki_user_photo');
  if (savedPhoto && portraitImg) {
    portraitImg.src = savedPhoto;
    portraitImg.style.objectFit = 'cover';
  }

  if (photoBtn && photoInput) {
    photoBtn.addEventListener('click', () => {
      photoInput.click();
    });

    photoInput.addEventListener('change', (e) => {
      const file = e.target.files[0];
      if (file && portraitImg) {
        const reader = new FileReader();
        reader.onload = (event) => {
          portraitImg.src = event.target.result;
          portraitImg.style.objectFit = 'cover';
          try {
            localStorage.setItem('wiki_user_photo', event.target.result);
          } catch(err) {
            console.warn('LocalStorage quota exceeded', err);
          }
        };
        reader.readAsDataURL(file);
      }
    });
  }
}

// 9. Navbox Collapsible Toggle
function initNavboxToggle() {
  const navboxToggle = document.getElementById('navbox-toggle-btn');
  const navboxBody = document.getElementById('navbox-body');

  if (navboxToggle && navboxBody) {
    navboxToggle.addEventListener('click', () => {
      if (navboxBody.style.display === 'none') {
        navboxBody.style.display = '';
        navboxToggle.textContent = '[접기]';
      } else {
        navboxBody.style.display = 'none';
        navboxToggle.textContent = '[펼치기]';
      }
    });
  }
}

// 10. Mobile Menu Hamburger
function initMobileMenu() {
  const menuBtn = document.getElementById('mobile-menu-btn');
  const sidebar = document.querySelector('.wiki-sidebar');

  if (menuBtn && sidebar) {
    menuBtn.addEventListener('click', () => {
      sidebar.classList.toggle('mobile-open');
    });
  }
}
