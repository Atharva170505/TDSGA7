---
marp: true
title: Product Documentation Presentation
author: Atharva Thakre
theme: default
paginate: true
---

<!-- _class: lead -->

# Product Documentation with Marp

**Author:** Atharva Thakre  
**Email:** 24f1001859@ds.study.iitm.ac.in

---

<!-- _backgroundColor: #123456 -->
<!-- _color: white -->

# Why Marp?

- Write once, present anywhere  
- Version control friendly  
- Export to PDF, PPTX, HTML  
- Great for technical + product documentation  

---

<!-- Background image -->
![bg cover](images/background.jpg)

# Product Overview

Our system is designed to be:  
- Scalable  
- Maintainable  
- Easy to integrate  

---

# Custom Theme Example

<style>
section {
  background: #fdf6e3;
  color: #657b83;
}
h1 {
  color: #d33682;
}
blockquote {
  font-style: italic;
}
</style>

> “Good documentation is the backbone of great software.”

---

# Algorithmic Complexity

Marp supports math with KaTeX:

- Inline: $O(n \log n)$
- Block:

$$
T(n) = T\left(\frac{n}{2}\right) + O(n) \implies O(n \log n)
$$

---

# Code Example

```java
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, Marp!");
    }
}
