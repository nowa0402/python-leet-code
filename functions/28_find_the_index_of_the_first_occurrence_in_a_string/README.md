# Find the Index of the First Occurrence in a String

## **部分文字列の検索**

### **問題**

2 つの文字列 `needle`（検索対象） と `haystack`（元の文字列）が与えられます。  
`haystack` 内で **最初に `needle` が出現するインデックス** を返してください。  
`needle` が `haystack` に含まれていない場合は `-1` を返してください。

---

## **例**

### **例 1**

**入力:**  
`haystack = "sadbutsad", needle = "sad"`  
**出力:**  
`0`  
**説明:**  
`"sad"` はインデックス `0` と `6` に現れますが、最初の出現位置 `0` を返します。

---

### **例 2**

**入力:**  
`haystack = "leetcode", needle = "leeto"`  
**出力:**  
`-1`  
**説明:**  
`"leeto"` は `"leetcode"` に含まれていないため、`-1` を返します。

---

## **制約**

- `1 <= haystack.length, needle.length <= 10⁴`
- `haystack` と `needle` は **小文字の英字** のみで構成される。
