# Length of Last Word

<https://leetcode.com/problems/length-of-last-word/description/>

## **最後の単語の長さを求める**

### **問題**

文字列 `s` が **単語とスペース** で構成されています。  
**最後の単語の長さ** を返してください。

- **単語** とは、**スペース以外の文字のみ** で構成される最大部分文字列です。

---

## **例**

### **例 1**

**入力:**  
`s = "Hello World"`  
**出力:**  
`5`  
**説明:**  
最後の単語は `"World"` で、長さは `5` です。

---

### **例 2**

**入力:**  
`s = "   fly me   to   the moon  "`  
**出力:**  
`4`  
**説明:**  
最後の単語は `"moon"` で、長さは `4` です。

---

### **例 3**

**入力:**  
`s = "luffy is still joyboy"`  
**出力:**  
`6`  
**説明:**  
最後の単語は `"joyboy"` で、長さは `6` です。

---

## **制約**

- `1 <= s.length <= 10⁴`
- `s` は **英字とスペース** (`' '`) のみで構成される。
- `s` には **少なくとも1つの単語** が含まれている。
