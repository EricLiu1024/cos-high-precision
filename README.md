# cos-high-precision

A high‑precision cosine digit extractor based on Python’s `decimal` module and the Taylor series expansion.  
This project computes the **n‑th digit after the decimal point** of `cos(a)` with controllable precision.

---

## 📌 Overview

This repository provides a precise implementation for evaluating the cosine function and retrieving a specific decimal digit.  
By combining Python’s arbitrary‑precision arithmetic with a carefully controlled Taylor expansion, the method avoids floating‑point errors and ensures stable accuracy.

---

## 🧠 Mathematical Background

The cosine function is computed using its Taylor series:



\[
\cos(a) = \sum_{k=0}^{\infty} \frac{(-1)^k a^{2k}}{(2k)!}
\]



The algorithm:

- Sets precision to `n + 50` digits to ensure numerical safety  
- Iteratively evaluates each term  
- Stops when the term becomes smaller than \(10^{-(n+5)}\)  
- Extracts the n‑th digit after the decimal point

---

## 🚀 Usage

Run the script:

```bash
python src/cos_digit.py
