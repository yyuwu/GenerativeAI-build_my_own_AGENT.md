# -*- coding: utf-8 -*-
"""
Logic Wiki - Single File HTML Generator (Home Page & Frosted Orange Edition)
============================================================================
1. 新增極具設計感之「首頁 (Home Page)」：
   - 畫面中央「邏輯」巨幅設計感大字樣 (Hero Typography)。
   - 簡約懸浮中央搜尋列 (Spotlight Search)，支援即時模糊檢索與卡片式結果預覽。
   - 快速入口與知識庫核心統計 (56 篇文獻 · 11 個章節 · 18 條規則 · 55 條定理)。
2. 左上角 LOGIC WIKI 標誌統一採用首頁風格字樣（「邏輯 LOGIC // WIKI」），
   點擊隨時一鍵滑順返回首頁。
3. 右側目錄側邊欄：亮橘色細線條邊框 + 高透光毛玻璃 + 3px 微米級磨砂質感。
4. 常駐右上角固定三槓按鈕 (position: fixed)，原地開關絕不跑位。
5. 全站字體纖細、無表情符號、雙向連結瞬間跳轉、數學公式離線預編譯。
"""

import os
import re
import json
import yaml
from pathlib import Path
import markdown_it

def slugify(text: str) -> str:
    s = text.strip()
    s = re.sub(r'[^\w\u4e00-\u9fff\-]', '-', s)
    s = re.sub(r'-+', '-', s)
    return s.strip('-')

# 1. 離線 LaTeX 數學公式預先編譯器
MATH_REPLACEMENTS = [
    # 邏輯連接詞與運算子
    (r'\\supset', '⊃'),
    (r'\\equiv', '≡'),
    (r'\\sim', '∼'),
    (r'\\neg', '¬'),
    (r'\\land', '∧'),
    (r'\\lor', '∨'),
    (r'\\cdot', '·'),
    (r'\\bullet', '•'),
    (r'\\rightarrow', '→'),
    (r'\\to', '→'),
    (r'\\leftarrow', '←'),
    (r'\\leftrightarrow', '↔'),
    (r'\\implies', '⟹'),
    (r'\\iff', '⟺'),
    # 量詞與後設邏輯符號
    (r'\\forall', '∀'),
    (r'\\exists', '∃'),
    (r'\\vdash', '⊢'),
    (r'\\vDash', '⊨'),
    (r'\\models', '⊨'),
    (r'\\bot', '⊥'),
    (r'\\top', '⊤'),
    # 集合與關係符號
    (r'\\neq', '≠'),
    (r'\\le', '≤'),
    (r'\\ge', '≥'),
    (r'\\in', '∈'),
    (r'\\notin', '∉'),
    (r'\\subset', '⊂'),
    (r'\\subseteq', '⊆'),
    (r'\\supset', '⊃'),
    (r'\\supseteq', '⊇'),
    (r'\\cup', '∪'),
    (r'\\cap', '∩'),
    (r'\\emptyset', '∅'),
    (r'\\varnothing', '∅'),
    (r'\\times', '×'),
    (r'\\dots', '…'),
    (r'\\cdots', '⋯'),
    # 希臘字母
    (r'\\alpha', 'α'),
    (r'\\beta', 'β'),
    (r'\\gamma', 'γ'),
    (r'\\Gamma', 'Γ'),
    (r'\\phi', 'ϕ'),
    (r'\\psi', 'ψ'),
    (r'\\Delta', 'Δ'),
    (r'\\lambda', 'λ'),
    # 格式清理
    (r'\\{', '{'),
    (r'\\}', '}'),
    (r'\\,', ' '),
    (r'\\;', ' '),
    (r'\\:', ' '),
    (r'\\quad', '   '),
    (r'\\qquad', '      '),
    (r'\\text\{([^}]+)\}', r'\1'),
    (r'\\mathrm\{([^}]+)\}', r'\1'),
    (r'\\mathbf\{([^}]+)\}', r'<b>\1</b>'),
    (r'\\mathit\{([^}]+)\}', r'<i>\1</i>'),
    (r'\\mathcal\{([^}]+)\}', r'<i>\1</i>'),
    # 上下标
    (r'_\{([^}]+)\}', r'<sub>\1</sub>'),
    (r'_([0-9a-zA-Zα-ωΑ-Ω])', r'<sub>\1</sub>'),
    (r'\^\{([^}]+)\}', r'<sup>\1</sup>'),
    (r'\^([0-9a-zA-Zα-ωΑ-Ω])', r'<sup>\1</sup>'),
]

def prerender_math(text: str) -> str:
    def replace_block_math(match):
        latex = match.group(1).strip()
        rendered = latex
        for pattern, repl in MATH_REPLACEMENTS:
            rendered = re.sub(pattern, repl, rendered)
        rendered = rendered.replace(r'\\', '<br>')
        return f'\n\n<div class="logic-math-block" data-raw="{latex}">{rendered}</div>\n\n'

    text = re.sub(r'\$\$(.*?)\$\$', replace_block_math, text, flags=re.DOTALL)

    def replace_inline_math(match):
        latex = match.group(1).strip()
        rendered = latex
        for pattern, repl in MATH_REPLACEMENTS:
            rendered = re.sub(pattern, repl, rendered)
        return f'<span class="logic-math-inline" data-raw="{latex}">{rendered}</span>'

    text = re.sub(r'(?<!\$)\$([^\$\n]+?)\$(?!\$)', replace_inline_math, text)
    return text

# 2. Markdown 解析器初始化
md_engine = markdown_it.MarkdownIt("commonmark").enable("table").enable("strikethrough")

# 3. 章節架構定義
CHAPTER_STRUCTURE = {
    "lectures": {
        "title": "講義",
        "code": "LECTURES",
        "chapters": [
            {
                "id": "lec_ch01",
                "title": "第一章：導論與論證基礎",
                "file_ids": [
                    "overviews_邏輯學知識體系地圖",
                    "concepts_論證與陳述句",
                    "concepts_演繹與歸納",
                    "concepts_有效性與健全性",
                    "concepts_一致性與有效性檢測",
                    "concepts_發現脈絡與證成脈絡"
                ]
            },
            {
                "id": "lec_ch02",
                "title": "第二章：語句邏輯與符號化",
                "file_ids": [
                    "concepts_真值函應與邏輯連接詞",
                    "concepts_語句形式與取代實例",
                    "concepts_自然語言翻譯與充要條件",
                    "concepts_實質條件句的哲學爭論與證成",
                    "concepts_使用與提及_Use_and_Mention"
                ]
            },
            {
                "id": "lec_ch03",
                "title": "第三章：真值表法",
                "file_ids": [
                    "methods_真值表判定法",
                    "concepts_恆真句_矛盾句與適真句"
                ]
            },
            {
                "id": "lec_ch04",
                "title": "第四章：自然演繹法 (18 條規則)",
                "file_ids": [
                    "methods_自然演繹法_Natural_Deduction",
                    "methods_引進與消去規則系統",
                    "rules_假言推理_Modus_Ponens",
                    "rules_否定後項_Modus_Tollens",
                    "rules_選言三段論_Disjunctive_Syllogism",
                    "rules_假言三段論_Hypothetical_Syllogism",
                    "rules_簡化律與連言律_Simp_and_Conj",
                    "rules_附加律與兩難推論_Add_and_CD",
                    "rules_笛摩根定律_DeMorgans_Laws",
                    "rules_實質蘊涵律與異質換位_Impl_and_Contra",
                    "rules_分配律與結合律_Dist_and_Assoc",
                    "rules_輸出入律與重言律_Exp_and_Taut",
                    "rules_實質等值律_Material_Equivalence"
                ]
            },
            {
                "id": "lec_ch05",
                "title": "第五章：條件證法、間接證法與後設邏輯",
                "file_ids": [
                    "methods_條件證明法_Conditional_Proof",
                    "methods_間接證明法_Indirect_Proof",
                    "concepts_後設邏輯_健全性與完備性"
                ]
            },
            {
                "id": "lec_ch07",
                "title": "第七章：述詞邏輯的符號化",
                "file_ids": [
                    "concepts_個體_述詞與量詞",
                    "concepts_對當方陣與範恩圖",
                    "concepts_展開式與有數量化",
                    "concepts_自然語言否定深層語意_部分否定與雙重否定"
                ]
            },
            {
                "id": "lec_ch08",
                "title": "第八章：述詞邏輯語意學",
                "file_ids": [
                    "concepts_述詞邏輯語意學與無效性證明"
                ]
            },
            {
                "id": "lec_ch09",
                "title": "第九章：述詞邏輯的演繹證明",
                "file_ids": [
                    "methods_述詞邏輯演繹證明法",
                    "rules_量詞推論四規則_UI_UG_EI_EG",
                    "rules_量詞否定規則_QN"
                ]
            },
            {
                "id": "lec_ch10",
                "title": "第十章：關係述詞、多重量詞與定理群",
                "file_ids": [
                    "overviews_述詞邏輯55條定理總覽與分類",
                    "rules_量詞前綴移入移出定理_Q17_Q18"
                ]
            },
            {
                "id": "lec_ch11",
                "title": "第十一章：等同與確定描述詞",
                "file_ids": [
                    "concepts_等同與確定描述詞",
                    "rules_等同規則與反身律_ID_and_IR"
                ]
            },
            {
                "id": "lec_fallacies",
                "title": "補充專題與邏輯謬誤",
                "file_ids": [
                    "fallacies_肯定後項的謬誤"
                ]
            }
        ]
    },
    "exercises": {
        "title": "習題",
        "code": "EXERCISES",
        "chapters": [
            {
                "id": "ex_ch01",
                "title": "第一章習題：導論與論證辨析",
                "file_ids": [
                    "exercises_ex_ch01_有效性與健全性觀念辨析"
                ]
            },
            {
                "id": "ex_ch02",
                "title": "第二章習題：符號化與真值函應",
                "file_ids": [
                    "exercises_ex_ch02_語句符號化與真值函應判準",
                    "exercises_ex_ch02_自然語言符號化Ex2-6實戰"
                ]
            },
            {
                "id": "ex_ch03",
                "title": "第三章習題：真值表與反例構造",
                "file_ids": [
                    "exercises_ex_ch03_真值表與短真值表反例技巧"
                ]
            },
            {
                "id": "ex_ch04",
                "title": "第四章習題：18 條規則自然演繹推導",
                "file_ids": [
                    "exercises_ex_ch04_自然演繹法18條規則經典推導",
                    "exercises_ex_001_基本演繹推導與有效性判定"
                ]
            },
            {
                "id": "ex_ch05",
                "title": "第五章習題：條件證法與間接證法",
                "file_ids": [
                    "exercises_ex_ch05_條件證法與間接證法進階演練"
                ]
            },
            {
                "id": "ex_ch07",
                "title": "第七章習題：述詞符號化與量詞陷阱",
                "file_ids": [
                    "exercises_ex_ch07_述詞邏輯符號化與量詞陷阱"
                ]
            },
            {
                "id": "ex_ch08",
                "title": "第八章習題：述詞語意學與反例模型",
                "file_ids": [
                    "exercises_ex_ch08_述詞邏輯語意學與反例模型構造"
                ]
            },
            {
                "id": "ex_ch09",
                "title": "第九章習題：一元述詞證明與易錯限制",
                "file_ids": [
                    "exercises_ex_ch09_一元述詞演繹證明與易錯限制",
                    "exercises_ex_002_述詞邏輯演繹推導與量詞規則限制"
                ]
            },
            {
                "id": "ex_ch10",
                "title": "第十章習題：關係述詞與多重量詞證明",
                "file_ids": [
                    "exercises_ex_ch10_關係述詞多重量詞推導與定理證明"
                ]
            },
            {
                "id": "ex_exams",
                "title": "綜合小考與期中考詳解",
                "file_ids": [
                    "exercises_quiz_語句邏輯小考精華與考點全解",
                    "exercises_exam_期中考精華詳解與觀念避坑"
                ]
            }
        ]
    },
    "projects": {
        "title": "專案",
        "code": "PROJECTS",
        "chapters": [
            {
                "id": "proj_studies",
                "title": "主題研究與專題簡報",
                "file_ids": [
                    "project_material_implication"
                ]
            }
        ]
    }
}

def generate_html():
    map_path = Path("scripts/title_anchor_map.json")
    if not map_path.exists():
        raise FileNotFoundError("請先執行 scripts/build_title_anchor_map.py 產生對照表！")
    
    with open(map_path, "r", encoding="utf-8") as f:
        map_data = json.load(f)

    lookup_index = map_data["lookup_index"]
    doc_meta_dict = {d["file_id"]: d for d in map_data["documents"]}

    # 1. 建立首頁 Home Page 虛擬頁面
    home_doc = {
        "file_id": "home",
        "anchor": "#home",
        "category": "home",
        "category_name": "首頁",
        "file_path": "index.md",
        "base_name": "home",
        "title": "邏輯學知識庫首頁",
        "aliases": ["首頁", "Home", "邏輯"],
        "tags": ["知識地圖", "導航中心", "哲學邏輯"],
        "headings_count": 0,
        "headings": []
    }
    doc_meta_dict["home"] = home_doc
    lookup_index["home"] = {
        "file_id": "home",
        "anchor": "#home",
        "title": "首頁",
        "category": "home",
        "category_name": "首頁"
    }

    # 2. 動態掃描 notes/ 目錄，自動掛載所有主題研究與專案簡報 (Data-Driven Projects)
    notes_dir = Path("notes")
    project_file_ids = []
    if notes_dir.exists():
        for note_file in sorted(notes_dir.glob("*.md")):
            raw_content = note_file.read_text(encoding="utf-8")
            fm = {}
            if raw_content.startswith("---"):
                parts = raw_content.split("---", 2)
                if len(parts) >= 3:
                    try:
                        fm = yaml.safe_load(parts[1]) or {}
                    except Exception:
                        pass
            
            clean_stem = slugify(note_file.stem)
            file_id = fm.get("file_id", f"project_{clean_stem}")
            title = fm.get("title", note_file.stem)
            raw_aliases = fm.get("aliases", [])
            if isinstance(raw_aliases, str):
                raw_aliases = [raw_aliases]
            aliases = list(set([note_file.stem, title] + raw_aliases))
            tags = fm.get("tags", ["主題研究", "專案簡報"])
            
            proj_doc = {
                "file_id": file_id,
                "anchor": f"#{file_id}",
                "category": "projects",
                "category_name": "專案",
                "file_path": str(note_file).replace("\\", "/"),
                "base_name": clean_stem,
                "title": title,
                "aliases": aliases,
                "tags": tags,
                "headings_count": 0,
                "headings": []
            }
            doc_meta_dict[file_id] = proj_doc
            lookup_index[file_id] = {
                "file_id": file_id,
                "anchor": f"#{file_id}",
                "title": title,
                "category": "projects",
                "category_name": "專案"
            }
            for al in aliases:
                lookup_index[al] = lookup_index[file_id]
            project_file_ids.append(file_id)

    CHAPTER_STRUCTURE["projects"]["chapters"][0]["file_ids"] = project_file_ids

    # 讀取並轉換所有 Markdown 檔案
    rendered_articles = {}

    # 產生首頁 (Home Page) 內容 HTML
    home_html = """
    <div class="home-container">
        <div class="home-hero">
            <div class="home-kicker">PHILOSOPHY & FORMAL REASONING</div>
            <h1 class="home-title">邏輯</h1>
            <div class="home-subtitle">SYMBOLIC LOGIC // KNOWLEDGE BASE</div>
            
            <div class="home-search-container">
                <div class="home-search-input-wrap">
                    <input type="text" id="homeSearchInput" class="home-search-input" placeholder="檢索 56 篇講義、推論規則、章節或習題..." oninput="handleHomeSearch(this.value)">
                </div>
                <div class="home-search-dropdown hidden" id="homeSearchDropdown"></div>
            </div>

            <div class="home-quick-tags">
                <span class="quick-tag-label">快速進入</span>
                <span class="quick-tag-sep">/</span>
                <a href="#overviews_邏輯學知識體系地圖" class="home-tag-btn" onclick="navigateTo('overviews_邏輯學知識體系地圖'); return false;">知識地圖</a>
                <a href="#methods_自然演繹法_Natural_Deduction" class="home-tag-btn" onclick="navigateTo('methods_自然演繹法_Natural_Deduction'); return false;">18 條規則</a>
                <a href="#methods_真值表判定法" class="home-tag-btn" onclick="navigateTo('methods_真值表判定法'); return false;">真值表法</a>
                <a href="#overviews_述詞邏輯55條定理總覽與分類" class="home-tag-btn" onclick="navigateTo('overviews_述詞邏輯55條定理總覽與分類'); return false;">55 條定理</a>
                <a href="#exercises_quiz_語句邏輯小考精華與考點全解" class="home-tag-btn" onclick="navigateTo('exercises_quiz_語句邏輯小考精華與考點全解'); return false;">小考考點全解</a>
                <a href="#exercises_exam_期中考精華詳解與觀念避坑" class="home-tag-btn" onclick="navigateTo('exercises_exam_期中考精華詳解與觀念避坑'); return false;">期中考解答</a>
            </div>
        </div>
    </div>
    """
    rendered_articles["home"] = {
        "meta": home_doc,
        "html": home_html
    }

    for doc_id, doc_info in doc_meta_dict.items():
        if doc_id == "home":
            continue

        file_path = Path(doc_info["file_path"])
        if not file_path.exists():
            continue

        raw_md = file_path.read_text(encoding="utf-8")
        body_md = raw_md
        fm_meta = {}
        if raw_md.startswith("---"):
            parts = raw_md.split("---", 2)
            if len(parts) >= 3:
                try:
                    fm_meta = yaml.safe_load(parts[1]) or {}
                except Exception:
                    pass
                body_md = parts[2].strip()

        math_processed_md = prerender_math(body_md)

        def replace_wikilink(m):
            link_content = m.group(1).strip()
            if "|" in link_content:
                target, label = link_content.split("|", 1)
                target = target.strip()
                label = label.strip()
            else:
                target = link_content
                label = link_content

            sub_anchor = ""
            if "#" in target:
                target_base, sub_anchor = target.split("#", 1)
                target_base = target_base.strip()
                sub_anchor = sub_anchor.strip()
            else:
                target_base = target

            if target_base.startswith("raw/"):
                return f'<code class="raw-ref">{label}</code>'

            found = lookup_index.get(target_base)
            if found:
                target_file_id = found["file_id"]
                sub_id_arg = ""
                if sub_anchor:
                    clean_sub = slugify(sub_anchor)
                    sub_id_arg = f"{target_file_id}__{clean_sub}"
                
                href_attr = f"#{sub_id_arg if sub_id_arg else target_file_id}"
                onclick_js = f"navigateTo('{target_file_id}', '{sub_id_arg}'); return false;"
                return f'<a href="{href_attr}" class="wikilink" onclick="{onclick_js}" data-target="{target_file_id}">{label}</a>'
            else:
                return f'<span class="wikilink-unresolved">{label}</span>'

        wikilink_processed_md = re.sub(r'\[\[(.*?)\]\]', replace_wikilink, math_processed_md)
        article_html = md_engine.render(wikilink_processed_md)

        def inject_heading_ids(m):
            tag = m.group(1)
            h_text = m.group(2)
            clean_text = re.sub(r'<[^>]+>', '', h_text).strip()
            clean_text = re.sub(r'[*_`$\[\]]', '', clean_text)
            sub_id = f"{doc_id}__{slugify(clean_text)}"
            return f'<{tag} id="{sub_id}">{h_text}</{tag}>'

        article_html = re.sub(r'<(h[1-4])>(.*?)</\1>', inject_heading_ids, article_html)

        article_html = re.sub(r'<blockquote>', '<blockquote class="callout-box">', article_html)
        article_html = re.sub(r'<table>', '<div class="table-wrapper"><table>', article_html)
        article_html = re.sub(r'</table>', '</table></div>', article_html)

        # 自動檢查 Frontmatter 是否宣告了簡報 (Data-Driven Presentation Embed)
        pres_cfg = fm_meta.get("presentation")
        if pres_cfg and pres_cfg.get("enabled", True):
            pres_path = pres_cfg.get("path", "presentation/index.html")
            pres_height = pres_cfg.get("height", "660px")
            pres_title = pres_cfg.get("title", f"{doc_info['title']} 簡報")
            embed_html = f"""
            <div class="presentation-embed" style="margin: 0.5rem 0 2.8rem 0; width: 100%;">
                <iframe src="{pres_path}" style="width: 100%; height: {pres_height}; border: none; display: block;" title="{pres_title}"></iframe>
            </div>
            """
            article_html = embed_html + article_html

        rendered_articles[doc_id] = {
            "meta": doc_info,
            "html": article_html
        }

    # 4. 生成側邊欄導航 HTML
    sidebar_html = []
    
    for sec_key, sec_data in CHAPTER_STRUCTURE.items():
        sec_title = sec_data["title"]
        sec_code = sec_data["code"]
        chapters = sec_data["chapters"]
        total_items = sum(len(ch["file_ids"]) for ch in chapters)

        sidebar_html.append(f"""
        <div class="sidebar-section" data-section="{sec_key}">
            <div class="section-header" onclick="toggleSection('{sec_key}')">
                <div class="section-title">
                    <span class="section-name">{sec_title}</span>
                    <span class="section-code">{sec_code}</span>
                </div>
                <div class="section-meta">
                    <span class="badge-count">{total_items}</span>
                    <span class="arrow-toggle" id="arrow-{sec_key}">-</span>
                </div>
            </div>
            <div class="section-content" id="content-{sec_key}">
        """)

        for ch in chapters:
            ch_id = ch["id"]
            ch_title = ch["title"]
            file_ids = ch["file_ids"]

            sidebar_html.append(f"""
                <div class="chapter-group" data-chapter="{ch_id}">
                    <div class="chapter-header" onclick="toggleChapter('{ch_id}')">
                        <span class="chapter-arrow" id="arrow-ch-{ch_id}">+</span>
                        <span class="chapter-title">{ch_title}</span>
                        <span class="chapter-count">({len(file_ids)})</span>
                    </div>
                    <ul class="chapter-list collapsed" id="list-{ch_id}">
            """)

            for fid in file_ids:
                doc = rendered_articles.get(fid)
                if not doc:
                    continue
                d_meta = doc["meta"]
                item_title = d_meta["title"]
                item_anchor = d_meta["anchor"]
                sidebar_html.append(f"""
                        <li class="nav-item" id="nav-item-{fid}" onclick="navigateTo('{fid}');">
                            <a href="{item_anchor}" class="nav-link" onclick="event.preventDefault(); navigateTo('{fid}');">
                                <span class="nav-dash">—</span>
                                <span class="nav-text">{item_title}</span>
                            </a>
                        </li>
                """)

            sidebar_html.append("""
                    </ul>
                </div>
            """)

        sidebar_html.append("""
            </div>
        </div>
        """)

    sidebar_full_html = "\n".join(sidebar_html)

    # 5. 生成所有文章內容 HTML (包含首頁)
    articles_html = []
    for doc_id, doc_data in rendered_articles.items():
        meta = doc_data["meta"]
        html_body = doc_data["html"]
        cat_name = meta.get("category_name", meta.get("category", ""))
        tags_html = "".join([f'<span class="meta-tag">#{t}</span>' for t in meta.get("tags", [])])
        
        if doc_id == "home":
            articles_html.append(f"""
            <article class="wiki-article hidden" id="article-home" data-file-id="home">
                {html_body}
            </article>
            """)
        else:
            articles_html.append(f"""
            <article class="wiki-article hidden" id="article-{doc_id}" data-file-id="{doc_id}">
                <div class="article-header-card">
                    <div class="article-breadcrumb">
                        <span class="crumb-cat">{cat_name}</span>
                        <span class="crumb-sep">/</span>
                        <span class="crumb-title">{meta['title']}</span>
                    </div>
                    <h1 class="article-main-title">{meta['title']}</h1>
                    <div class="article-metadata-row">
                        <div class="tags-container">{tags_html}</div>
                        <div class="file-path-badge">{meta['file_path']}</div>
                    </div>
                </div>
                <div class="article-content markdown-body">
                    {html_body}
                </div>
                <div class="article-footer-nav">
                    <button class="footer-btn prev-btn" onclick="navigateAdjacent(-1)">上一篇</button>
                    <button class="footer-btn top-btn" onclick="document.getElementById('mainPane').scrollTo({{top: 0, behavior: 'smooth'}})">置頂</button>
                    <button class="footer-btn next-btn" onclick="navigateAdjacent(1)">下一篇</button>
                </div>
            </article>
            """)

    articles_full_html = "\n".join(articles_html)

    # 搜尋索引 JSON (供前端首頁即時下拉檢索使用)
    search_catalog = []
    for d in map_data["documents"]:
        search_catalog.append({
            "file_id": d["file_id"],
            "title": d["title"],
            "category_name": d.get("category_name", ""),
            "aliases": d.get("aliases", []),
            "tags": d.get("tags", [])
        })

    # 6. 整合完整 HTML 樣板
    full_page_html = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>邏輯 (Logic) // 哲學課堂與習題知識庫</title>
    <style>
        :root {{
            --bg-page: #ffffff;
            --bg-subtle: #fafafa;
            --bg-hover: rgba(255, 115, 0, 0.05);
            --text-main: #171717;
            --text-secondary: #525252;
            --text-muted: #8c8c8c;
            --text-faint: #b3b3b3;
            --line-border: #e5e5e5;
            --line-light: #eeeeee;
            --line-dark: #262626;

            /* 亮橘色核心變數 (Bright Orange Lines & Accents) */
            --accent-orange: #ff7300;
            --accent-orange-deep: #e65c00;
            --line-orange: #ff7300;
            --line-orange-soft: rgba(255, 115, 0, 0.28);
            --line-orange-glow: rgba(255, 115, 0, 0.12);

            /* 藍紫色字樣與反白 (Blue-Purple / Indigo Accent for Wikilinks & Highlights) */
            --accent-purple: #5c56d6;
            --accent-purple-deep: #4338ca;
            --line-purple-soft: rgba(92, 86, 214, 0.38);
            --bg-purple-highlight: rgba(92, 86, 214, 0.12);
            --selection-purple: rgba(92, 86, 214, 0.22);

            --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang TC", "Noto Sans TC", "Hiragino Sans GB", "Microsoft JhengHei", Roboto, sans-serif;
            --font-mono: "JetBrains Mono", Menlo, Consolas, "Fira Code", monospace;
            --sidebar-width: 320px;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: var(--font-sans);
            background-color: var(--bg-page);
            color: var(--text-main);
            font-weight: 350;
            letter-spacing: 0.015em;
            line-height: 1.7;
            display: flex;
            flex-direction: row;
            height: 100vh;
            width: 100vw;
            overflow: hidden;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }}

        /* 右上角固定三槓按鈕 */
        .fixed-sidebar-toggle {{
            position: fixed;
            top: 10px;
            right: 18px;
            z-index: 1000;
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid var(--line-orange);
            border-radius: 3px;
            width: 36px;
            height: 34px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 3.5px;
            cursor: pointer;
            box-shadow: 0 1px 6px var(--line-orange-glow);
            transition: all 0.2s ease;
        }}

        .fixed-sidebar-toggle:hover {{
            border-color: var(--accent-orange-deep);
            background: #ffffff;
            box-shadow: 0 0 10px rgba(255, 115, 0, 0.28);
            transform: scale(1.02);
        }}

        .hamburger-bar {{
            width: 16px;
            height: 1.6px;
            background-color: var(--accent-orange);
            border-radius: 1px;
            transition: all 0.2s ease;
        }}

        /* 左側主畫面區 */
        main.wiki-main {{
            flex: 1;
            height: 100vh;
            overflow-y: auto;
            background: var(--bg-page);
            display: flex;
            flex-direction: column;
            position: relative;
            min-width: 0;
            transition: width 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        }}

        /* 頂部操作列 */
        .top-navbar {{
            position: sticky;
            top: 0;
            background: rgba(255, 255, 255, 0.96);
            backdrop-filter: blur(8px);
            border-bottom: 1px solid var(--line-border);
            padding: 0.65rem 4.5rem 0.65rem 2.2rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            z-index: 50;
            gap: 1.2rem;
        }}

        .nav-left {{
            display: flex;
            align-items: center;
            gap: 0.85rem;
            min-width: 0;
        }}

        /* 
           【左上角 Logo 標誌】
           採用與主頁大字一致的風格：漢字「邏輯」＋ 亮橘英文標識，點擊可隨時滑順返回首頁
        */
        .brand-link {{
            display: flex;
            align-items: baseline;
            gap: 0.45rem;
            text-decoration: none;
            color: var(--text-main);
            padding: 0.15rem 0.5rem;
            border-radius: 3px;
            border: 1px solid transparent;
            cursor: pointer;
            transition: all 0.15s ease;
            white-space: nowrap;
        }}

        .brand-link:hover {{
            border-color: var(--line-orange-soft);
            background: rgba(255, 115, 0, 0.05);
        }}

        .brand-kanji {{
            font-size: 1.05rem;
            font-weight: 500;
            letter-spacing: 0.08em;
            color: var(--text-main);
        }}

        .brand-latin {{
            font-family: var(--font-mono);
            font-size: 0.68rem;
            letter-spacing: 0.06em;
            color: var(--accent-orange);
            font-weight: 500;
        }}

        .crumb-sep {{
            color: var(--text-faint);
            font-size: 0.8rem;
        }}

        .current-indicator {{
            font-size: 0.85rem;
            font-weight: 450;
            color: var(--text-secondary);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}

        /* 
           【全新主頁 (Home View) 風格樣式】
           簡約、留白、巨大字樣、極簡懸浮搜尋列
        */
        .home-container {{
            min-height: calc(100vh - 120px);
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 2rem 1rem 4rem 1rem;
        }}

        .home-hero {{
            width: 100%;
            max-width: 680px;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
        }}

        .home-kicker {{
            font-family: var(--font-mono);
            font-size: 0.76rem;
            letter-spacing: 0.2em;
            color: var(--accent-orange);
            margin-bottom: 0.8rem;
            font-weight: 500;
        }}

        /* 「邏輯」超大設計感標題 */
        .home-title {{
            font-size: 4.6rem;
            font-weight: 300;
            letter-spacing: 0.18em;
            color: var(--text-main);
            margin-bottom: 0.35rem;
            line-height: 1.1;
            padding-left: 0.18em; /* 補齊 letter-spacing 右偏 */
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.02);
        }}

        .home-subtitle {{
            font-family: var(--font-mono);
            font-size: 0.72rem;
            letter-spacing: 0.15em;
            color: var(--text-muted);
            margin-bottom: 2.8rem;
        }}

        /* 簡約懸浮中央搜尋框 */
        .home-search-container {{
            width: 100%;
            position: relative;
            margin-bottom: 2rem;
        }}

        .home-search-input-wrap {{
            width: 100%;
            position: relative;
        }}

        .home-search-input {{
            width: 100%;
            background: #ffffff;
            border: 1px solid var(--line-border);
            border-radius: 4px;
            padding: 0.95rem 1.4rem;
            font-size: 1.02rem;
            font-family: var(--font-sans);
            font-weight: 350;
            color: var(--text-main);
            outline: none;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03);
            transition: all 0.2s ease;
        }}

        .home-search-input:focus {{
            border-color: var(--line-orange);
            box-shadow: 0 6px 24px var(--line-orange-glow), 0 0 0 2px rgba(255, 115, 0, 0.1);
        }}

        .home-search-input::placeholder {{
            color: var(--text-faint);
            font-weight: 300;
            font-size: 0.94rem;
        }}

        /* 首頁搜尋即時下拉清單 */
        .home-search-dropdown {{
            position: absolute;
            top: calc(100% + 6px);
            left: 0;
            right: 0;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid var(--line-orange-soft);
            border-radius: 4px;
            max-height: 320px;
            overflow-y: auto;
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.06);
            z-index: 200;
            text-align: left;
        }}

        .home-search-dropdown.hidden {{
            display: none;
        }}

        .home-search-item {{
            padding: 0.75rem 1.2rem;
            border-bottom: 1px solid rgba(0, 0, 0, 0.04);
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: space-between;
            transition: all 0.15s ease;
        }}

        .home-search-item:last-child {{
            border-bottom: none;
        }}

        .home-search-item:hover {{
            background: rgba(255, 115, 0, 0.06);
        }}

        .search-item-left {{
            display: flex;
            align-items: center;
            gap: 0.6rem;
        }}

        .search-item-cat {{
            font-family: var(--font-mono);
            font-size: 0.68rem;
            color: var(--accent-orange);
            border: 1px solid var(--line-orange-soft);
            padding: 0.05rem 0.35rem;
            border-radius: 2px;
            white-space: nowrap;
        }}

        .search-item-title {{
            font-size: 0.92rem;
            color: var(--text-main);
            font-weight: 450;
        }}

        /* 快速入口標籤 */
        .home-quick-tags {{
            display: flex;
            align-items: center;
            justify-content: center;
            flex-wrap: wrap;
            gap: 0.45rem;
            margin-bottom: 0.5rem;
        }}

        .quick-tag-label {{
            font-size: 0.78rem;
            color: var(--text-muted);
            letter-spacing: 0.05em;
        }}

        .quick-tag-sep {{
            color: var(--text-faint);
            font-size: 0.75rem;
            margin-right: 0.2rem;
        }}

        .home-tag-btn {{
            font-size: 0.8rem;
            color: var(--text-secondary);
            text-decoration: none;
            border: 1px solid var(--line-border);
            padding: 0.25rem 0.65rem;
            border-radius: 2px;
            transition: all 0.15s ease;
        }}

        .home-tag-btn:hover {{
            border-color: var(--line-orange);
            color: var(--accent-orange);
            background: rgba(255, 115, 0, 0.04);
        }}

        /* 
           右側目錄側邊欄 (Frosted Glass & Bright Orange Border & Matte Texture)
        */
        aside.wiki-sidebar {{
            width: var(--sidebar-width);
            min-width: var(--sidebar-width);
            max-width: var(--sidebar-width);
            background: rgba(255, 255, 255, 0.78);
            backdrop-filter: blur(20px) saturate(180%);
            -webkit-backdrop-filter: blur(20px) saturate(180%);
            color: var(--text-secondary);
            display: flex;
            flex-direction: column;
            border-left: 1px solid var(--line-orange);
            border-right: none;
            box-shadow: -2px 0 16px rgba(255, 115, 0, 0.06), inset 1px 0 0 rgba(255, 255, 255, 0.6);
            height: 100vh;
            overflow: hidden;
            user-select: none;
            position: relative;
            transition: width 0.22s cubic-bezier(0.16, 1, 0.3, 1),
                        min-width 0.22s cubic-bezier(0.16, 1, 0.3, 1),
                        max-width 0.22s cubic-bezier(0.16, 1, 0.3, 1),
                        border-left-color 0.2s ease,
                        opacity 0.18s ease;
            z-index: 100;
        }}

        /* 磨砂微顆粒純 CSS 紋理遮罩 */
        aside.wiki-sidebar::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-image: radial-gradient(rgba(0, 0, 0, 0.038) 1px, transparent 0);
            background-size: 3px 3px;
            opacity: 0.8;
            pointer-events: none;
            z-index: 1;
        }}

        .sidebar-brand, .sidebar-search, .sidebar-nav-scroll {{
            position: relative;
            z-index: 2;
        }}

        /* 側欄收折後的狀態 */
        body.sidebar-collapsed aside.wiki-sidebar {{
            width: 0 !important;
            min-width: 0 !important;
            max-width: 0 !important;
            border-left-color: transparent !important;
            opacity: 0;
            pointer-events: none;
        }}

        .sidebar-brand {{
            padding: 1rem 4.5rem 0.85rem 1.4rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid var(--line-orange-soft);
            min-height: 52px;
        }}

        .brand-title {{
            font-size: 0.95rem;
            font-weight: 500;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            color: var(--text-main);
            white-space: nowrap;
        }}

        .brand-count {{
            font-family: var(--font-mono);
            font-size: 0.72rem;
            color: var(--accent-orange);
            border: 1px solid var(--line-orange-soft);
            background: rgba(255, 115, 0, 0.06);
            padding: 0.08rem 0.4rem;
            border-radius: 2px;
            white-space: nowrap;
        }}

        /* 搜尋列 */
        .sidebar-search {{
            padding: 0.8rem 1.4rem;
            border-bottom: 1px solid var(--line-orange-soft);
        }}

        .search-box {{
            width: 100%;
            background: rgba(255, 255, 255, 0.65);
            border: 1px solid var(--line-orange-soft);
            border-radius: 2px;
            padding: 0.42rem 0.7rem;
            color: var(--text-main);
            font-family: var(--font-sans);
            font-size: 0.84rem;
            font-weight: 350;
            outline: none;
            transition: all 0.15s ease;
        }}

        .search-box:focus {{
            border-color: var(--line-orange);
            background: rgba(255, 255, 255, 0.9);
            box-shadow: 0 0 0 2px var(--line-orange-glow);
        }}

        .search-box::placeholder {{
            color: var(--text-faint);
            font-weight: 300;
        }}

        .sidebar-quick-tools {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-top: 0.6rem;
            padding-top: 0.5rem;
            border-top: 1px dashed var(--line-orange-soft);
        }}

        .tools-label {{
            font-size: 0.72rem;
            font-family: var(--font-mono);
            letter-spacing: 0.08em;
            color: var(--text-muted);
            text-transform: uppercase;
        }}

        .tools-btn-group {{
            display: flex;
            align-items: center;
            gap: 0.35rem;
        }}

        .sidebar-tool-btn {{
            background: rgba(255, 255, 255, 0.85);
            border: 1px solid var(--line-orange);
            color: var(--accent-orange-deep);
            font-size: 0.74rem;
            font-family: var(--font-sans);
            font-weight: 350;
            padding: 0.16rem 0.52rem;
            border-radius: 3px;
            cursor: pointer;
            box-shadow: 0 1px 6px var(--line-orange-glow);
            transition: all 0.2s ease;
        }}

        .sidebar-tool-btn:hover {{
            border-color: var(--accent-orange-deep);
            color: var(--accent-orange-deep);
            background: #ffffff;
            box-shadow: 0 0 10px rgba(255, 115, 0, 0.28);
            transform: scale(1.02);
        }}

        .tool-sep {{
            color: var(--line-orange-soft);
            font-size: 0.72rem;
        }}

        /* 側欄導航清單 */
        .sidebar-nav-scroll {{
            flex: 1;
            overflow-y: auto;
            padding: 0.6rem 0;
            min-width: var(--sidebar-width);
        }}

        .sidebar-nav-scroll::-webkit-scrollbar {{
            width: 4px;
        }}

        .sidebar-nav-scroll::-webkit-scrollbar-thumb {{
            background: var(--line-orange-soft);
            border-radius: 2px;
        }}

        /* 三大主要分類 Section */
        .sidebar-section {{
            margin-bottom: 0.25rem;
        }}

        .section-header {{
            padding: 0.65rem 1.4rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            cursor: pointer;
            border-bottom: 1px solid rgba(255, 115, 0, 0.15);
            transition: background 0.15s;
        }}

        .section-header:hover {{
            background: var(--bg-hover);
        }}

        .section-title {{
            display: flex;
            align-items: baseline;
            gap: 0.5rem;
            white-space: nowrap;
        }}

        .section-name {{
            font-size: 0.88rem;
            font-weight: 500;
            color: var(--text-main);
            letter-spacing: 0.02em;
        }}

        .section-code {{
            font-family: var(--font-mono);
            font-size: 0.65rem;
            color: var(--accent-orange);
            letter-spacing: 0.05em;
            opacity: 0.85;
        }}

        .section-meta {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .badge-count {{
            font-family: var(--font-mono);
            font-size: 0.72rem;
            color: var(--text-muted);
        }}

        .arrow-toggle {{
            font-family: var(--font-mono);
            font-size: 0.8rem;
            color: var(--accent-orange);
            width: 12px;
            text-align: center;
            font-weight: 500;
        }}

        .section-content {{
            transition: max-height 0.2s ease;
        }}

        .section-content.collapsed {{
            display: none;
        }}

        /* 章節 Chapter Group */
        .chapter-group {{
            margin: 0.1rem 0;
        }}

        .chapter-header {{
            padding: 0.4rem 1.4rem 0.4rem 1.8rem;
            display: flex;
            align-items: center;
            gap: 0.4rem;
            font-size: 0.82rem;
            font-weight: 450;
            color: var(--text-secondary);
            cursor: pointer;
            transition: all 0.15s;
            white-space: nowrap;
        }}

        .chapter-header:hover {{
            color: var(--text-main);
            background: var(--bg-hover);
        }}

        .chapter-arrow {{
            font-family: var(--font-mono);
            font-size: 0.8rem;
            color: var(--accent-orange);
            width: 12px;
            display: inline-block;
            font-weight: 500;
        }}

        .chapter-title {{
            flex: 1;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}

        .chapter-count {{
            font-family: var(--font-mono);
            font-size: 0.7rem;
            color: var(--text-faint);
        }}

        .chapter-list {{
            list-style: none;
            padding-left: 2.5rem;
            margin: 0.1rem 0 0.4rem 0;
        }}

        .chapter-list.collapsed {{
            display: none;
        }}

        /* 單篇項目 */
        .nav-item {{
            margin: 0.05rem 0;
        }}

        .nav-link {{
            display: flex;
            align-items: baseline;
            gap: 0.4rem;
            padding: 0.28rem 0.6rem 0.28rem 0;
            color: var(--text-secondary);
            text-decoration: none;
            font-size: 0.81rem;
            font-weight: 350;
            line-height: 1.4;
            transition: all 0.15s;
            border-left: 1px solid transparent;
            padding-left: 0.5rem;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}

        .nav-link:hover {{
            color: var(--text-main);
            border-left-color: var(--line-orange-soft);
            background: var(--bg-hover);
        }}

        .nav-item.active .nav-link {{
            color: var(--accent-orange-deep);
            font-weight: 500;
            border-left-color: var(--accent-orange);
            background: rgba(255, 115, 0, 0.07);
        }}

        .nav-dash {{
            font-family: var(--font-mono);
            font-size: 0.65rem;
            color: var(--text-faint);
        }}

        .nav-item.active .nav-dash {{
            color: var(--accent-orange);
        }}

        /* 文章容器 */
        .article-viewport {{
            flex: 1;
            padding: 2.5rem 3.5rem 5rem 3.5rem;
            max-width: 900px;
            margin: 0 auto;
            width: 100%;
        }}

        .wiki-article {{
            display: block;
            animation: fadeIn 0.12s ease-out;
        }}

        .wiki-article.hidden {{
            display: none !important;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; }}
            to {{ opacity: 1; }}
        }}

        /* 文章標頭卡片 */
        .article-header-card {{
            border-bottom: 1px solid var(--line-border);
            padding-bottom: 1.5rem;
            margin-bottom: 2.2rem;
        }}

        .article-breadcrumb {{
            font-size: 0.78rem;
            color: var(--text-muted);
            margin-bottom: 0.6rem;
            display: flex;
            align-items: center;
            gap: 0.45rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}

        .crumb-cat {{
            color: var(--accent-orange-deep);
            font-weight: 500;
        }}

        .crumb-sep {{
            color: var(--text-faint);
        }}

        .article-main-title {{
            font-size: 1.75rem;
            font-weight: 500;
            color: var(--text-main);
            margin-bottom: 0.9rem;
            line-height: 1.35;
            letter-spacing: -0.01em;
        }}

        .article-metadata-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 0.8rem;
            padding-top: 0.6rem;
            border-top: 1px solid var(--line-light);
        }}

        .tags-container {{
            display: flex;
            gap: 0.4rem;
            flex-wrap: wrap;
        }}

        .meta-tag {{
            font-size: 0.72rem;
            font-family: var(--font-mono);
            border: 1px solid var(--line-border);
            color: var(--text-muted);
            padding: 0.05rem 0.45rem;
            border-radius: 2px;
        }}

        .file-path-badge {{
            font-size: 0.72rem;
            color: var(--text-faint);
            font-family: var(--font-mono);
        }}

        /* Markdown 正文排版 */
        .markdown-body {{
            font-size: 0.98rem;
            color: var(--text-main);
            line-height: 1.85;
            font-weight: 350;
        }}

        .markdown-body h1, .markdown-body h2, .markdown-body h3, .markdown-body h4 {{
            color: var(--text-main);
            margin-top: 2.2rem;
            margin-bottom: 0.8rem;
            font-weight: 500;
            line-height: 1.4;
            scroll-margin-top: 4.5rem;
        }}

        .markdown-body h1 {{ font-size: 1.45rem; border-bottom: 1px solid var(--line-border); padding-bottom: 0.35rem; }}
        .markdown-body h2 {{ font-size: 1.25rem; border-bottom: 1px solid var(--line-light); padding-bottom: 0.3rem; }}
        .markdown-body h3 {{ font-size: 1.05rem; font-weight: 500; }}
        .markdown-body h4 {{ font-size: 0.95rem; font-weight: 500; }}

        .markdown-body p {{
            margin-bottom: 1.1rem;
        }}

        .markdown-body ul, .markdown-body ol {{
            margin-bottom: 1.2rem;
            padding-left: 1.5rem;
        }}

        .markdown-body li {{
            margin-bottom: 0.35rem;
        }}

        .markdown-body hr {{
            border: none;
            border-top: 1px solid var(--line-light);
            margin: 2.5rem 0;
        }}

        /* 雙向連結 (Wikilinks 底線字樣：預設與反白採用藍紫色調) */
        a.wikilink {{
            color: #171717;
            text-decoration: underline;
            text-decoration-thickness: 1px;
            text-underline-offset: 3.5px;
            text-decoration-color: var(--line-purple-soft);
            font-weight: 450;
            cursor: pointer;
            padding: 0 0.15rem;
            border-radius: 2px;
            transition: all 0.15s ease;
        }}

        a.wikilink:hover {{
            color: var(--accent-purple-deep);
            text-decoration-color: var(--accent-purple);
            background-color: var(--bg-purple-highlight);
        }}

        /* 瀏覽器選取反白與底線字樣反白 */
        a.wikilink::selection {{
            background-color: var(--selection-purple);
            color: var(--accent-purple-deep);
        }}

        ::selection {{
            background-color: var(--selection-purple);
            color: #1e1b4b;
        }}

        .wikilink-unresolved {{
            color: var(--text-muted);
            text-decoration: underline dotted var(--line-border);
        }}

        .raw-ref {{
            font-family: var(--font-mono);
            border: 1px solid var(--line-light);
            color: var(--text-muted);
            padding: 0.05rem 0.35rem;
            border-radius: 2px;
            font-size: 0.82em;
        }}

        /* 離線預先編譯數學公式 */
        .logic-math-inline {{
            display: inline-block;
            font-family: "Cambria Math", "Times New Roman", "KaTeX_Math", Georgia, serif;
            font-size: 1.05em;
            color: var(--text-main);
            padding: 0 0.15em;
            font-style: italic;
        }}

        .logic-math-inline b, .logic-math-inline i {{
            font-style: normal;
        }}

        .logic-math-block {{
            border-top: 1px solid var(--line-border);
            border-bottom: 1px solid var(--line-border);
            background: var(--bg-subtle);
            padding: 0.85rem 1.2rem;
            margin: 1.4rem 0;
            font-family: "Cambria Math", "Times New Roman", "KaTeX_Math", Georgia, serif;
            font-size: 1.1em;
            overflow-x: auto;
            text-align: center;
        }}

        /* 表格排版 */
        .table-wrapper {{
            overflow-x: auto;
            margin: 1.4rem 0;
            border: 1px solid var(--line-border);
            border-radius: 2px;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.88rem;
            font-weight: 350;
        }}

        th, td {{
            padding: 0.6rem 0.85rem;
            border: 1px solid var(--line-light);
            text-align: left;
        }}

        th {{
            background: var(--bg-subtle);
            font-weight: 500;
            color: var(--text-main);
            border-bottom: 1px solid var(--line-border);
        }}

        tr:nth-child(even) {{
            background: #fdfdfd;
        }}

        /* 代碼塊與證明 */
        pre {{
            background: #171717;
            color: #fafafa;
            padding: 1rem 1.25rem;
            border-radius: 2px;
            overflow-x: auto;
            font-family: var(--font-mono);
            font-size: 0.84rem;
            font-weight: 350;
            line-height: 1.55;
            margin: 1.4rem 0;
            border: 1px solid #333;
        }}

        code {{
            font-family: var(--font-mono);
            font-size: 0.86em;
            background: var(--bg-subtle);
            border: 1px solid var(--line-border);
            color: #171717;
            padding: 0.08rem 0.35rem;
            border-radius: 2px;
        }}

        pre code {{
            background: transparent;
            border: none;
            color: inherit;
            padding: 0;
        }}

        .callout-box {{
            border-left: 2px solid var(--accent-orange);
            background: rgba(255, 115, 0, 0.03);
            padding: 0.75rem 1.2rem;
            margin: 1.4rem 0;
            color: var(--text-secondary);
            font-size: 0.94rem;
        }}

        /* 專案卡片 */
        .project-hero {{
            border-bottom: 1px solid var(--line-border);
            padding-bottom: 1.6rem;
            margin-bottom: 2rem;
        }}

        .hero-code {{
            font-family: var(--font-mono);
            font-size: 0.72rem;
            color: var(--accent-orange);
            letter-spacing: 0.08em;
            margin-bottom: 0.4rem;
        }}

        .project-hero h2 {{
            font-size: 1.55rem;
            font-weight: 500;
            margin-bottom: 0.4rem;
            border: none !important;
            padding: 0 !important;
        }}

        .project-hero .subtitle {{
            color: var(--text-secondary);
            font-size: 0.95rem;
        }}

        .project-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 1.25rem;
            margin-bottom: 2rem;
        }}

        .project-card {{
            border: 1px solid var(--line-border);
            padding: 1.3rem;
            border-radius: 2px;
            transition: all 0.15s ease;
        }}

        .project-card:hover {{
            border-color: var(--line-orange);
            box-shadow: 0 2px 8px var(--line-orange-glow);
        }}

        .card-meta {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 0.6rem;
        }}

        .project-badge {{
            font-family: var(--font-mono);
            font-size: 0.68rem;
            border: 1px solid var(--line-orange-soft);
            color: var(--accent-orange);
            background: rgba(255, 115, 0, 0.05);
            padding: 0.05rem 0.35rem;
        }}

        .project-code {{
            font-family: var(--font-mono);
            font-size: 0.68rem;
            color: var(--text-faint);
        }}

        .project-card h3 {{
            font-size: 1.05rem;
            font-weight: 500;
            margin-bottom: 0.5rem;
            color: var(--text-main);
        }}

        .project-card p {{
            font-size: 0.86rem;
            color: var(--text-secondary);
            line-height: 1.6;
            margin-bottom: 0.9rem;
        }}

        .project-features {{
            font-size: 0.8rem;
            color: var(--text-muted);
            padding-left: 1.1rem;
        }}

        .project-footer-note {{
            border: 1px solid var(--line-orange-soft);
            padding: 1rem 1.3rem;
            font-size: 0.86rem;
            color: var(--text-secondary);
            background: rgba(255, 115, 0, 0.03);
        }}

        .note-title {{
            font-weight: 500;
            color: var(--accent-orange-deep);
            margin-bottom: 0.2rem;
            font-size: 0.88rem;
        }}

        .article-footer-nav {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 3.5rem;
            padding-top: 1.5rem;
            border-top: 1px solid var(--line-border);
        }}

        .footer-btn {{
            background: transparent;
            border: 1px solid var(--line-border);
            padding: 0.42rem 1rem;
            border-radius: 2px;
            font-family: var(--font-sans);
            font-size: 0.82rem;
            cursor: pointer;
            color: var(--text-secondary);
            transition: all 0.15s;
        }}

        .footer-btn:hover {{
            border-color: var(--line-orange);
            color: var(--accent-orange);
        }}
    </style>
</head>
<body>

    <!-- 常駐右上角固定三槓按鈕 (亮橘色細線) -->
    <button class="fixed-sidebar-toggle" id="fixedSidebarToggleBtn" onclick="toggleSidebar()" title="切換目錄側欄" aria-label="切換目錄側欄">
        <span class="hamburger-bar"></span>
        <span class="hamburger-bar"></span>
        <span class="hamburger-bar"></span>
    </button>

    <!-- 左側主畫面區 -->
    <main class="wiki-main" id="mainPane">
        <header class="top-navbar">
            <div class="nav-left">
                <!-- 左上角「邏輯」主題風格標誌，點擊可一鍵返回首頁 -->
                <a href="#home" class="brand-link" onclick="navigateTo('home'); return false;" title="回到邏輯首頁">
                    <span class="brand-kanji">邏輯</span>
                    <span class="brand-latin">LOGIC // WIKI</span>
                </a>
                <span class="crumb-sep">/</span>
                <span class="current-indicator" id="currentArticleTitle">首頁 // 概覽</span>
            </div>
        </header>

        <div class="article-viewport">
            {articles_full_html}
        </div>
    </main>

    <!-- 右側目錄欄 (毛玻璃透明質感 + 磨砂微顆粒 + 亮橘色細線邊框) -->
    <aside class="wiki-sidebar" id="sidebar">
        <div class="sidebar-brand">
            <span class="brand-title">目錄導航</span>
            <span class="brand-count">56 篇</span>
        </div>

        <div class="sidebar-search">
            <input type="text" id="searchInput" class="search-box" placeholder="搜尋講義、習題、概念..." oninput="handleSearch()">
            <div class="sidebar-quick-tools">
                <span class="tools-label">架構層級</span>
                <div class="tools-btn-group">
                    <button class="sidebar-tool-btn" onclick="expandAllSections()" title="展開所有分類與章節">展開全部</button>
                    <span class="tool-sep">/</span>
                    <button class="sidebar-tool-btn" onclick="collapseAllSections()" title="收起所有分類與章節">收起全部</button>
                </div>
            </div>
        </div>

        <div class="sidebar-nav-scroll" id="sidebarNav">
            {sidebar_full_html}
        </div>
    </aside>

    <!-- 前端互動控制腳本 -->
    <script>
        const ARTICLE_ORDER = {json.dumps([fid for sec in CHAPTER_STRUCTURE.values() for ch in sec["chapters"] for fid in ch["file_ids"]], ensure_ascii=False)};
        const SEARCH_CATALOG = {json.dumps(search_catalog, ensure_ascii=False)};
        let currentArticleId = "home";

        function toggleSection(secKey) {{
            const content = document.getElementById("content-" + secKey);
            const arrow = document.getElementById("arrow-" + secKey);
            if (!content || !arrow) return;
            if (content.classList.contains("collapsed")) {{
                content.classList.remove("collapsed");
                arrow.innerText = "-";
            }} else {{
                content.classList.add("collapsed");
                arrow.innerText = "+";
            }}
        }}

        function toggleChapter(chId) {{
            const list = document.getElementById("list-" + chId);
            const arrow = document.getElementById("arrow-ch-" + chId);
            if (!list || !arrow) return;
            if (list.classList.contains("collapsed")) {{
                list.classList.remove("collapsed");
                arrow.innerText = "-";
            }} else {{
                list.classList.add("collapsed");
                arrow.innerText = "+";
            }}
        }}

        function expandAllSections() {{
            document.querySelectorAll(".section-content").forEach(el => el.classList.remove("collapsed"));
            document.querySelectorAll(".arrow-toggle").forEach(el => el.innerText = "-");
            document.querySelectorAll(".chapter-list").forEach(el => el.classList.remove("collapsed"));
            document.querySelectorAll(".chapter-arrow").forEach(el => el.innerText = "-");
        }}

        function collapseAllSections() {{
            document.querySelectorAll(".section-content").forEach(el => el.classList.add("collapsed"));
            document.querySelectorAll(".arrow-toggle").forEach(el => el.innerText = "+");
            document.querySelectorAll(".chapter-list").forEach(el => el.classList.add("collapsed"));
            document.querySelectorAll(".chapter-arrow").forEach(el => el.innerText = "+");
        }}

        // 4. 文章切換導航核心 (支援首頁 home 與任意文章)
        function navigateTo(fileId, subHeadingId) {{
            if (!fileId) fileId = "home";
            
            document.querySelectorAll(".wiki-article").forEach(art => art.classList.add("hidden"));
            document.querySelectorAll(".nav-item").forEach(item => item.classList.remove("active"));

            const targetArticle = document.getElementById("article-" + fileId);
            if (targetArticle) {{
                targetArticle.classList.remove("hidden");
                currentArticleId = fileId;

                // 更新頂部指示器
                const titleIndicator = document.getElementById("currentArticleTitle");
                if (fileId === "home") {{
                    titleIndicator.innerText = "首頁 // 概覽";
                }} else {{
                    const titleEl = targetArticle.querySelector(".article-main-title");
                    if (titleEl) {{
                        titleIndicator.innerText = titleEl.innerText;
                    }}
                }}

                // 高亮對應側欄項目 (首頁不需在側欄高亮)
                const navItem = document.getElementById("nav-item-" + fileId);
                if (navItem) {{
                    navItem.classList.add("active");
                    
                    const parentChapterList = navItem.closest(".chapter-list");
                    if (parentChapterList) {{
                        parentChapterList.classList.remove("collapsed");
                        const chGroup = navItem.closest(".chapter-group");
                        if (chGroup) {{
                            const arrow = chGroup.querySelector(".chapter-arrow");
                            if (arrow) arrow.innerText = "-";
                        }}
                    }}

                    const parentSectionContent = navItem.closest(".section-content");
                    if (parentSectionContent) {{
                        parentSectionContent.classList.remove("collapsed");
                        const secEl = navItem.closest(".sidebar-section");
                        if (secEl) {{
                            const secArrow = secEl.querySelector(".arrow-toggle");
                            if (secArrow) secArrow.innerText = "-";
                        }}
                    }}

                    navItem.scrollIntoView({{ block: "nearest", behavior: "smooth" }});
                }}

                if (subHeadingId) {{
                    setTimeout(() => {{
                        const subEl = document.getElementById(subHeadingId);
                        if (subEl) {{
                            subEl.scrollIntoView({{ behavior: "smooth", block: "start" }});
                        }} else {{
                            document.getElementById("mainPane").scrollTo({{ top: 0, behavior: "smooth" }});
                        }}
                    }}, 60);
                }} else {{
                    document.getElementById("mainPane").scrollTo({{ top: 0, behavior: "smooth" }});
                }}

                const hashValue = subHeadingId ? subHeadingId : fileId;
                history.pushState(null, "", "#" + hashValue);
            }}
        }}

        function navigateAdjacent(delta) {{
            const curIdx = ARTICLE_ORDER.indexOf(currentArticleId);
            if (curIdx === -1) {{
                navigateTo(ARTICLE_ORDER[0]);
                return;
            }}
            let nextIdx = curIdx + delta;
            if (nextIdx >= 0 && nextIdx < ARTICLE_ORDER.length) {{
                navigateTo(ARTICLE_ORDER[nextIdx]);
            }}
        }}

        // 側欄即時搜尋
        function handleSearch() {{
            const query = document.getElementById("searchInput").value.trim().toLowerCase();
            const navItems = document.querySelectorAll(".nav-item");
            const chapterGroups = document.querySelectorAll(".chapter-group");
            const sections = document.querySelectorAll(".sidebar-section");

            if (!query) {{
                navItems.forEach(el => el.style.display = "");
                chapterGroups.forEach(el => el.style.display = "");
                sections.forEach(el => el.style.display = "");
                return;
            }}

            expandAllSections();
            navItems.forEach(item => {{
                const text = item.innerText.toLowerCase();
                if (text.includes(query)) {{
                    item.style.display = "";
                }} else {{
                    item.style.display = "none";
                }}
            }});

            chapterGroups.forEach(ch => {{
                const visibleItems = ch.querySelectorAll(".nav-item:not([style*='display: none'])");
                if (visibleItems.length > 0) {{
                    ch.style.display = "";
                }} else {{
                    ch.style.display = "none";
                }}
            }});

            sections.forEach(sec => {{
                const visibleChapters = sec.querySelectorAll(".chapter-group:not([style*='display: none'])");
                if (visibleChapters.length > 0) {{
                    sec.style.display = "";
                }} else {{
                    sec.style.display = "none";
                }}
            }});
        }}

        // 首頁中央即時搜尋與下拉選單
        function handleHomeSearch(val) {{
            const q = val.trim().toLowerCase();
            const dropdown = document.getElementById("homeSearchDropdown");
            if (!q) {{
                dropdown.innerHTML = "";
                dropdown.classList.add("hidden");
                return;
            }}

            const matches = SEARCH_CATALOG.filter(item => {{
                if (item.title.toLowerCase().includes(q)) return true;
                if (item.aliases.some(a => a.toLowerCase().includes(q))) return true;
                if (item.tags.some(t => t.toLowerCase().includes(q))) return true;
                return false;
            }}).slice(0, 8); // 最多呈現 8 筆

            if (matches.length === 0) {{
                dropdown.innerHTML = '<div style="padding: 0.8rem 1.2rem; font-size: 0.86rem; color: #888;">查無相關文獻，請嘗試其他關鍵字</div>';
                dropdown.classList.remove("hidden");
                return;
            }}

            let html = "";
            matches.forEach(m => {{
                html += `
                <div class="home-search-item" onclick="navigateTo('${{m.file_id}}'); document.getElementById('homeSearchDropdown').classList.add('hidden');">
                    <div class="search-item-left">
                        <span class="search-item-cat">${{m.category_name}}</span>
                        <span class="search-item-title">${{m.title}}</span>
                    </div>
                    <span style="font-size: 0.72rem; color: #999; font-family: var(--font-mono);">${{m.file_id}}</span>
                </div>
                `;
            }});

            dropdown.innerHTML = html;
            dropdown.classList.remove("hidden");
        }}

        function toggleSidebar() {{
            document.body.classList.toggle("sidebar-collapsed");
        }}

        function handleHashRouting() {{
            const rawHash = window.location.hash.replace("#", "");
            if (!rawHash || rawHash === "home") {{
                navigateTo("home");
                return;
            }}
            let targetFileId = rawHash;
            let subHeadingId = "";
            if (rawHash.includes("__")) {{
                const parts = rawHash.split("__");
                targetFileId = parts[0];
                subHeadingId = rawHash;
            }}

            if (document.getElementById("article-" + targetFileId)) {{
                navigateTo(targetFileId, subHeadingId);
            }} else {{
                navigateTo("home");
            }}
        }}

        window.addEventListener("DOMContentLoaded", () => {{
            handleHashRouting();

            window.addEventListener("hashchange", handleHashRouting);
            window.addEventListener("popstate", handleHashRouting);

            document.addEventListener("click", (e) => {{
                const link = e.target.closest("a.wikilink");
                if (link) {{
                    const href = link.getAttribute("href");
                    if (href && href.startsWith("#")) {{
                        e.preventDefault();
                        const rawTarget = href.replace(/^#/, "");
                        const parts = rawTarget.split("__");
                        const fileId = parts[0];
                        const subId = parts.length > 1 ? rawTarget : "";
                        navigateTo(fileId, subId);
                    }}
                }}
            }});

            // 點擊頁面其他地方關閉首頁搜尋下拉選單
            document.addEventListener("click", (e) => {{
                const dropdown = document.getElementById("homeSearchDropdown");
                const searchWrap = document.querySelector(".home-search-container");
                if (dropdown && !searchWrap.contains(e.target)) {{
                    dropdown.classList.add("hidden");
                }}
            }});
        }});
    </script>
</body>
</html>
"""

    out_file = Path("logic_wiki.html")
    out_file.write_text(full_page_html, encoding="utf-8")
    print(f"成功更新單一檔案網頁（首頁 + 亮橘細線磨砂版）！")
    print(f"檔案位置: {out_file} (大小: {out_file.stat().st_size} bytes)")

if __name__ == "__main__":
    generate_html()
