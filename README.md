# Xush kelibsiz
# Boolean Ma'lumot Turlari

Avtomatlashtirilgan uy vazifalari va testlarni baholash
- Ushbu repozitoriyani fork qiling
- Vazifani hal qiling
- To'g'ri xabar bilan commit qiling
- To'g'ri xabar bilan commit qiling

# Muammolar
## logic01

  Uchta butun son a, b, c berilgan, "b soni a va c orasida" degan bayonotni tekshiring.

**Misol 1:**

```Python
Kirish: a=3 b=4 c=5
Chiqarish: True
```

**Misol 2:**

```Python
Kirish: a=6 b=4 c=5
Chiqarish: False
```

**Misol 3:**

```Python
Kirish: a=6 b=4 c=1
Chiqarish: True
```

**Cheklovlar:**
- -10<sup>18</sup><=num<=10<sup>18</sup>

## logic02

  Ikki butun son a va b berilgan, "a va b sonlarining har biri musbat" degan bayonotni tekshiring.

**Misol 1:**

```Python
Kirish: a=5 b=3
Chiqarish: True
```

**Misol 2:**

```Python
Kirish: a=6 b=-4
Chiqarish: False
```

**Cheklovlar:**
- -10<sup>18</sup><=num<=10<sup>18</sup>

## logic03

  Ikki butun son a va b berilgan, "a va b sonlarining har biri manfiy" degan bayonotni tekshiring.

**Misol 1:**

```Python
Kirish: a=-1 b=-3
Chiqarish: True
```

**Misol 2:**

```Python
Kirish: a=6 b=-4
Chiqarish: False
```

**Cheklovlar:**
- -10<sup>18</sup><=num<=10<sup>18</sup>

## logic04

  Ikki butun son a va b berilgan, "a va b sonlarining har biri juft" degan bayonotni tekshiring.

**Misol 1:**

```Python
Kirish: a=3 b=6
Chiqarish: False
```

**Misol 2:**

```Python
Kirish: a=6 b=4
Chiqarish: True
```

**Cheklovlar:**
- -10<sup>18</sup><=num<=10<sup>18</sup>

## logic05

  Ikki butun son a va b berilgan, "a va b sonlarining har biri toq" degan bayonotni tekshiring.

**Misol 1:**

```Python
Kirish: a=3 b=8
Chiqarish: False
```

**Misol 2:**

```Python
Kirish: a=9 b=1
Chiqarish: True
```

**Cheklovlar:**
- -10<sup>18</sup><=num<=10<sup>18</sup>

## logic06

  Ikki butun son a va b berilgan, "a va b sonlarining kamida biri musbat" degan bayonotni tekshiring.

**Misol 1:**

```Python
Kirish: a=-3 b=8
Chiqarish: True
```

**Misol 2:**

```Python
Kirish: a=-9 b=-1
Chiqarish: False
```

**Cheklovlar:**
- -10<sup>18</sup><=num<=10<sup>18</sup>

## logic07

  Ikki butun son a va b berilgan, "a va b sonlarining kamida biri manfiy" degan bayonotni tekshiring.

**Misol 1:**

```Python
Kirish: a=-3 b=8
Chiqarish: True
```

**Misol 2:**

```Python
Kirish: a=4 b=1
Chiqarish: False
```

**Cheklovlar:**
- -10<sup>18</sup><=num<=10<sup>18</sup>

## logic08

  Ikki butun son a va b berilgan, "a va b sonlarining kamida biri juft" degan bayonotni tekshiring.

**Misol 1:**

```Python
Kirish: a=6 b=3
Chiqarish: True
```

**Misol 2:**

```Python
Kirish: a=7 b=1
Chiqarish: False
```

**Cheklovlar:**
- -10<sup>18</sup><=num<=10<sup>18</sup>

## logic09

  Ikki butun son a va b berilgan, "a va b sonlarining kamida biri toq" degan bayonotni tekshiring.

**Misol 1:**

```Python
Kirish: a=5 b=3
Chiqarish: True
```

**Misol 2:**

```Python
Kirish: a=4 b=9
Chiqarish: True
```

**Cheklovlar:**
- -10<sup>18</sup><=num<=10<sup>18</sup>

## logic10

  Butun son a berilgan, "Son ikki raqamli" degan bayonotni tekshiring.

**Misol 1:**

```Python
Kirish: a=3
Chiqarish: False
```

**Misol 2:**

```Python
Kirish: a=12
Chiqarish: True
```

**Cheklovlar:**
- -10<sup>18</sup><=num<=10<sup>18</sup>

## logic11

  Butun son a berilgan, "Son uch raqamli" degan bayonotni tekshiring.

**Misol 1:**

```Python
Kirish: a=3
Chiqarish: False
```

**Misol 2:**

```Python
Kirish: a=12
Chiqarish: False
```

**Misol 2:**

```Python
Kirish: a=123
Chiqarish: True
```

**Cheklovlar:**
- -10<sup>18</sup><=num<=10<sup>18</sup>

## logic12

  Ikki raqamli butun son a berilgan, "Sonning barcha raqamlari teng" degan bayonotni tekshiring.

**Misol 1:**

```Python
Kirish: a=32
Chiqarish: False
```

**Misol 2:**

```Python
Kirish: a=22
Chiqarish: True
```

**Cheklovlar:**
- -10<sup>18</sup><=num<=10<sup>18</sup>

## logic13

  Ikki raqamli butun son a berilgan, "Sonning barcha raqamlarining yig'indisi juft" degan bayonotni tekshiring.

**Misol 1:**

```Python
Kirish: a=45
Chiqarish: False
```

**Misol 2:**

```Python
Kirish: a=35
Chiqarish: True
```

**Cheklovlar:**
- -10<sup>18</sup><=num<=10<sup>18</sup>

## logic14

  Ikki raqamli butun son a berilgan, "Sonning barcha raqamlarining yig'indisi toq" degan bayonotni tekshiring.

**Misol 1:**

```Python
Kirish: a=45
Chiqarish: True
```

**Misol 2:**

```Python
Kirish: a=35
Chiqarish: False
```

**Cheklovlar:**
- -10<sup>18</sup><=num<=10<sup>18</sup>

## logic15

  Uch raqamli butun son a berilgan, "Sonning barcha raqamlarining yig'indisi toq" degan bayonotni tekshiring.

**Misol 1:**

```Python
Kirish: a=152
Chiqarish: False
```

**Misol 2:**

```Python
Kirish: a=335
Chiqarish: True
```

**Cheklovlar:**
- -10<sup>18</sup><=a<=10<sup>18</sup>

## logic16

  Butun son a berilgan, "Son besh raqamli" degan bayonotni tekshiring.

**Misol 1:**

```Python
Kirish: a=15234
Chiqarish: True
```

**Misol 2:**

```Python
Kirish: a=763
Chiqarish: False
```

**Cheklovlar:**
- -10<sup>18</sup><=a<=10<sup>18</sup>

Here is the Uzbek translation for the logic problems you provided:

---

## logic17

Besh raqamli butun son `a` berilgan, "Raqamlarning hammasi o'sish tartibida" degan gapni tekshiring.

**Misol 1:**

```Python
Input: a=75421
Output: True
```

**Misol 2:**

```Python
Input: a=13763
Output: False
```

**Cheklovlar:**
- -10<sup>18</sup><=a<=10<sup>18</sup>

## logic18

Besh raqamli butun son `a` berilgan, "Raqamlarning hammasi kamayish tartibida" degan gapni tekshiring.

**Misol 1:**

```Python
Input: a=75421
Output: False
```

**Misol 2:**

```Python
Input: a=12347
Output: True
```

**Cheklovlar:**
- -10<sup>18</sup><=a<=10<sup>18</sup>

## logic19

Butun son `x` berilgan, `x` palindrom bo'lsa, ya'ni orqaga va oldinga qaraganda bir xil o'qilsa, `True` qaytaring.

**Misol 1:**

```Python
Input: x=121
Output: True
```

**Misol 2:**

```Python
Input: x=10
Output: False
```

**Misol 3:**

```Python
Input: x=11
Output: True
```

**Cheklovlar:**
- 9 < x < 1000

## logic20

Birlar va nolardan iborat bo'lgan son berilgan (son birlar bilan boshlanadi). Agar birlar soni nolardan ko'p bo'lsa, `True`, aks holda `False` qaytarilsin. `n` besh raqamli son.

**Misol 1:**

```Python
Input: n=1100
Output: False
```

**Misol 2:**

```Python
Input: n=10011
Output: True
```

**Cheklovlar:**
- 0 < n < 100000

---

**Eslatma:**
- Boshqa yechimlarni nusxalamang yoki hech qanday yechimni olib tashlamang.
