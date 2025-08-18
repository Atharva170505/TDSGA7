---
marp: true
title: Product Documentation Presentation
paginate: true
theme: custom
author: 24f1001859@ds.study.iitm.ac.in
style: |
  /* Custom theme overrides */
  section { font-family: "Segoe UI", sans-serif; }
  h1, h2, h3 { color: #0a84ff; }
  footer { font-size: 0.7em; color: #555; }
---

# Product Documentation  
**Author:** 24f1001859@ds.study.iitm.ac.in  

---

# Why Marp?  

- **Markdown-based** → ideal for version control.  
- **Exportable** → generate PDF, PPTX, HTML easily.  
- **Customizable** → themes, directives, CSS.

<!-- _footer: "Confidential — For internal stakeholders only" -->

---

# Algorithmic Complexity  

Typical example (**merge sort**):

$$
T(n) = 2T\left(\frac{n}{2}\right) + O(n) \\
\implies T(n) = O(n \log n)
$$

---

![bg cover](https://raw.githubusercontent.com/marp-team/marp-core/master/logo.svg)

# 🌄 Background Image Slide  
This slide uses Marp's native syntax for a proper background image.

---

# Custom Styling with Directives  

- `paginate: true` for page numbers.  
- Inline CSS via `style:` in frontmatter.  
- Use `![bg ...](...)` for slide backgrounds.  
- Use math via LaTeX in $$...$$ blocks.  
- Example directive:  

<!-- _class: lead -->

---

# Contact  
📧 24f1001859@ds.study.iitm.ac.in  
Slides powered by **Marp Markdown**
