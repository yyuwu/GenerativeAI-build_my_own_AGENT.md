# -*- coding: utf-8 -*-
"""
Logic Wiki - Title to File ID / Anchor Mapping Generator
========================================================
掃描 wiki/ 下的所有 Markdown 檔案，解析 Frontmatter 與內文章節標題，
產出標準化「標題 ↔ 檔案 ID / 錨點」對照表與雙向連結查詢字典 (Lookup Index)。
"""

import os
import re
import json
import yaml
from pathlib import Path

CATEGORY_NAMES = {
    "overviews": "宏觀綜述",
    "concepts": "核心概念",
    "rules": "推論與等值規則",
    "methods": "證明與判定方法",
    "exercises": "習題與考題解析",
    "fallacies": "邏輯謬誤"
}

def slugify(text: str) -> str:
    """生成 URL 安全、乾淨且唯一的標識符 (保留繁體中文與英數連字符號)"""
    s = text.strip()
    s = re.sub(r'[^\w\u4e00-\u9fff\-]', '-', s)
    s = re.sub(r'-+', '-', s)
    return s.strip('-')

def build_mapping(wiki_root: str = "wiki"):
    wiki_path = Path(wiki_root)
    files = sorted(list(wiki_path.glob("**/*.md")))

    documents = []
    lookup_index = {}

    for f in files:
        rel_path = f.relative_to(wiki_path).as_posix()
        cat = f.parent.name
        base_name = f.stem
        
        content = f.read_text(encoding="utf-8")
        fm = {}
        body = content
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                try:
                    fm = yaml.safe_load(parts[1]) or {}
                    body = parts[2]
                except Exception as e:
                    print(f"[Warning] YAML 解析失敗 {f}: {e}")

        title = fm.get("title", base_name)
        aliases = fm.get("aliases", [])
        if isinstance(aliases, str):
            aliases = [aliases]
        elif not isinstance(aliases, list):
            aliases = []

        tags = fm.get("tags", [])
        if isinstance(tags, str):
            tags = [tags]
        elif not isinstance(tags, list):
            tags = []

        file_id = f"{cat}_{slugify(base_name)}"
        page_anchor = f"#{file_id}"

        # 擷取文章內的所有標題與子錨點
        headings = []
        for line in body.splitlines():
            m = re.match(r'^(#{1,4})\s+(.+)$', line)
            if m:
                level = len(m.group(1))
                h_text = m.group(2).strip()
                # 去除可能的行內 markdown 格式
                clean_h_text = re.sub(r'[*_`$\[\]]', '', h_text)
                h_anchor_suffix = slugify(clean_h_text)
                sub_anchor = f"{file_id}__{h_anchor_suffix}"
                headings.append({
                    "level": level,
                    "raw_text": h_text,
                    "clean_text": clean_h_text,
                    "anchor": f"#{sub_anchor}",
                    "sub_id": sub_anchor
                })

        doc_meta = {
            "file_id": file_id,
            "anchor": page_anchor,
            "category": cat,
            "category_name": CATEGORY_NAMES.get(cat, cat),
            "file_path": f"wiki/{rel_path}",
            "base_name": base_name,
            "title": title,
            "aliases": aliases,
            "tags": tags,
            "headings_count": len(headings),
            "headings": headings
        }
        documents.append(doc_meta)

        # 登錄至 lookup_index (所有可能的 Wikilink 命中目標)
        keys_to_register = [
            base_name,
            f"{base_name}.md",
            title,
            f"wiki/{rel_path}",
            f"{rel_path}"
        ]
        for a in aliases:
            if a and str(a).strip():
                keys_to_register.append(str(a).strip())

        target_info = {
            "file_id": file_id,
            "anchor": page_anchor,
            "title": title,
            "category": cat,
            "category_name": CATEGORY_NAMES.get(cat, cat)
        }

        for k in keys_to_register:
            # 優先保留精確 base_name 映射，若已有則記錄
            if k not in lookup_index:
                lookup_index[k] = target_info

    # 輸出 JSON
    output_data = {
        "generated_at": "2026-11-17",
        "total_documents": len(documents),
        "categories": CATEGORY_NAMES,
        "documents": documents,
        "lookup_index": lookup_index
    }

    out_json = Path("scripts/title_anchor_map.json")
    with open(out_json, "w", encoding="utf-8") as jf:
        json.dump(output_data, jf, ensure_ascii=False, indent=2)

    # 產出人類可讀的 Markdown 對照表報告
    md_lines = [
        "# 邏輯學 Wiki：標題 ↔ 檔案 ID / 錨點對照表 (Title-Anchor Map)",
        "",
        "> 本表由轉換程式自動掃描 `wiki/` 產生，作為 Single-Page HTML 網頁導航、雙向連結解析與路由映射之標準核心對照表。",
        f"> **收錄文章總數**：{len(documents)} 篇 | **涵蓋分類**：6 大模組",
        "",
        "---",
        ""
    ]

    for cat_key, cat_name in CATEGORY_NAMES.items():
        cat_docs = [d for d in documents if d["category"] == cat_key]
        if not cat_docs:
            continue
        md_lines.append(f"## {cat_name} (`{cat_key}`, 共 {len(cat_docs)} 篇)")
        md_lines.append("")
        md_lines.append("| 標題 (Title) | 檔案 ID (file_id) | 網頁錨點 (Anchor) | 別名 (Aliases) | 子標題數 |")
        md_lines.append("| :--- | :--- | :--- | :--- | :---: |")
        for d in cat_docs:
            alias_str = ", ".join(d["aliases"]) if d["aliases"] else "-"
            md_lines.append(f"| **{d['title']}** | `{d['file_id']}` | `{d['anchor']}` | {alias_str} | {d['headings_count']} |")
        md_lines.append("")

    out_md = Path("scripts/title_anchor_map.md")
    out_md.write_text("\n".join(md_lines), encoding="utf-8")

    print(f"成功生成對照表！")
    print(f"JSON 檔案已儲存至: {out_json} (大小: {out_json.stat().st_size} bytes)")
    print(f"Markdown 文件已儲存至: {out_md}")
    return output_data

if __name__ == "__main__":
    build_mapping()
