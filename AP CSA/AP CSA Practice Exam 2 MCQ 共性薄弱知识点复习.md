# AP CSA Practice Exam 2 MCQ — 共性薄弱知识点复习

> 全班通用复习材料，聚焦高频错题和易错知识点

---

## 📋 考试数据概览

- **总分：** 42分（40道单选题 + 2道双选题）
- **班级平均得分率：** ~84%
- **以下知识点错误率超过 25%，需要重点复习**

---

## 🔴 最高优先级：全班共性薄弱点

---

### 1. 类型转换 `(double)` 的优先级（错误率 ~75%）

**对应题目：** Q3

**题目回顾：**
```
Which of the following expressions evaluates to 3.5?
(A) (double) 2 / 4 + 3
(B) (double) 2 / (4 + 3)
(C) (double) (2 / 4) + 3
(D) (double) (2 / 4 + 3)
```

**正确答案：A**

**为什么很多人会选 C？**

```java
// ❌ 选项 C: (double) (2 / 4) + 3
//    步骤1: 括号内先算 → 2 / 4 = 0（整数除法！小数被截断！）
//    步骤2: (double)(0) = 0.0
//    步骤3: 0.0 + 3 = 3.0 ❌

// ✅ 选项 A: (double) 2 / 4 + 3
//    步骤1: (double) 2 = 2.0
//    步骤2: 2.0 / 4 = 0.5（double除法，保留小数）
//    步骤3: 0.5 + 3 = 3.5 ✅
```

**核心规则：**

| 写法 | 执行顺序 | 结果 |
|------|---------|------|
| `(double) (2 / 4)` | 先算括号内的整数除法 `2/4=0`，再转double | `0.0` |
| `(double) 2 / 4` | 先转 `2.0`，再做double除法 | `0.5` |
| `(double) (2 / 4 + 3)` | 先算括号内 `0 + 3 = 3`，再转double | `3.0` |

**记忆口诀：**
> **`(double)` 只影响紧邻的下一个值！**
> **括号内的整数运算先算完，结果已经是 int，再转 double！**

**练习题（务必手写）：**

```java
(double) 5 / 2          // = 2.5  还是  2.0 ?
(double) (5 / 2)        // = ?
5 / (double) 2          // = ?
(int) 7.8 + 2           // = ?
(int) (7.8 + 2)         // = ?
(double) 3 + 4 / 2      // = ?
(double) (3 + 4) / 2    // = ?
```

<details>
<summary>点击查看答案</summary>

```
(double) 5 / 2       → 2.5    (2.0 / 2 = 2.5)
(double) (5 / 2)     → 2.0    (5/2=2, 再转double)
5 / (double) 2       → 2.5    (5 / 2.0 = 2.5)
(int) 7.8 + 2        → 9      (7 + 2 = 9)
(int) (7.8 + 2)      → 9      (9.8 → 9)
(double) 3 + 4 / 2   → 5.0    (3.0 + 2 = 5.0)
(double) (3 + 4) / 2 → 3.5    (7.0 / 2 = 3.5)
```

</details>

---

### 2. 开源代码 vs 闭源代码（错误率 ~62%）

**对应题目：** Q13

**考点：** Computing Innovations — 伦理与社会影响（APCSA考纲必考内容）

**核心概念：**

| | 开源 (Open Source) | 闭源 (Closed/Proprietary) |
|--|-------------------|--------------------------|
| **代码可见性** | 任何人都能看到源代码 | 源代码不公开 |
| **修改权限** | 允许他人修改、分发 | 不允许他人修改 |
| **使用场景** | 希望协作、共享、社区改进 | 保护知识产权、商业利益 |
| **例子** | Linux, Apache | Windows, Photoshop |

**易错点：**

> ❌ "当程序员想确保只有他们自己可以修改代码时" → 这是**闭源**的场景！

> ✅ "当程序员希望其他程序员能修改代码并纳入他们自己的程序时" → 这才是**开源**！

**相关知识点扩展：**

**Q21: 提高系统可靠性 (System Reliability)**
- 方法：冗余(redundancy)、错误处理(error handling)、测试(testing)
- 不是：减少功能、限制用户访问

**记忆清单：**
- 开源 = 共享、协作、允许修改、社区驱动
- 闭源 = 保护、控制、商业保密
- 可靠性 = 冗余备份 + 错误处理 + 充分测试
- 隐私 = 数据最小化 + 用户知情同意

---

### 3. `static` 变量：属于类，不属于对象（错误率 ~37%）

**对应题目：** Q25

**核心规则（一句话记住）：**

> **`static` 变量属于类，所有对象共享同一个！**

**示例：**

```java
public class Counter {
    public static int count = 0;  // static变量
    public int id;                 // 非static变量（实例变量）
    
    public Counter(int i) {
        id = i;
        count++;    // 所有Counter对象共用同一个count
    }
}

Counter c1 = new Counter(1);
Counter c2 = new Counter(2);
Counter c3 = new Counter(3);
// c1.id = 1, c2.id = 2, c3.id = 3（各自不同）
// Counter.count = 3（只有一个，所有对象共享）
```

**常见考题陷阱：**
- 一个对象修改了 static 变量，另一个对象能看到变化
- static 方法不能访问非 static 的实例变量（因为没有"this"对象）

---

### 4. 循环执行次数的比较（错误率 ~37%）

**对应题目：** Q22

**常见循环模板对比：**

```java
// 循环A: 执行 n 次
for (int i = 0; i < n; i++) { }

// 循环B: 执行 n 次
for (int i = 1; i <= n; i++) { }

// 循环C: 执行 n-1 次
for (int i = 1; i < n; i++) { }

// 循环D: 执行 n/2 次（i每次加2）
for (int i = 0; i < n; i += 2) { }
```

**检查方法：**
> 代入小数字，列出来看！

比如 `for(int i=0; i<4; i++)`：
- i=0 ✅, i=1 ✅, i=2 ✅, i=3 ✅, i=4 ❌(不执行)
- 共执行 **4** 次

比如 `for(int i=1; i<=4; i++)`：
- i=1 ✅, i=2 ✅, i=3 ✅, i=4 ✅, i=5 ❌
- 共执行 **4** 次

**虽然执行次数可能相同，但 i 的取值范围不同，注意题目问的是什么！**

---

## 🟡 中高优先级：多选题共性错误

---

### 5. 排序算法的 Trace（Insertion/Selection Sort）

**对应题目：** Q40, Q41

**考试要求：** 能给定初始数组，写出排序过程中每轮的结果。

**Insertion Sort（插入排序）模板：**

```java
for (int i = 1; i < data.length; i++) {
    int temp = data[i];
    int j = i - 1;
    while (j >= 0 && data[j] > temp) {
        data[j + 1] = data[j];
        j--;
    }
    data[j + 1] = temp;
}
```

**Trace 方法（务必动手写）：**

以 `{6, 3, 2, 5, 4, 1}` 为例：

```
初始: [6, 3, 2, 5, 4, 1]
i=1:  temp=3, 和6比较→[3, 6, 2, 5, 4, 1]
i=2:  temp=2, 和6,3比较→[2, 3, 6, 5, 4, 1]
i=3:  temp=5, 和6比较→[2, 3, 5, 6, 4, 1]
```

**每轮结束后，前 i+1 个元素是有序的！**

---

### 6. 递归方法跟踪

**对应题目：** Q37, Q42

**跟踪方法：画调用树**

```java
public static void stars(int n) {
    if (n > 0) {
        System.out.print("*");
        stars(n - 1);
        System.out.print("*");
    }
}
```

**跟踪 `stars(3)`：**

```
stars(3)
├── print "*"
├── stars(2)
│   ├── print "*"
│   ├── stars(1)
│   │   ├── print "*"
│   │   ├── stars(0) → base case, 什么也不做
│   │   └── print "*"
│   └── print "*"
└── print "*"

输出: ****** (6个星)
```

**关键点：**
- 先找到 **base case**（递归终止条件）
- 每次递归调用，参数必须向 base case 靠近
- 注意递归调用前后的语句都会执行

---

### 7. 文件扫描 Scanner

**对应题目：** Q29

**常用方法：**

```java
Scanner in = new Scanner(new File("data.txt"));

while (in.hasNext()) {      // 是否还有下一个token？
    String word = in.next(); // 读一个String
    int num = in.nextInt();  // 读一个int
    double d = in.nextDouble(); // 读一个double
}
```

**陷阱：**
- `nextInt()` 不会消费行末的换行符，如果后面跟 `nextLine()` 要注意
- `hasNext()` 判断是否还有任何token，`hasNextInt()` 判断下一个token是否是整数

---

### 8. 2D 数组：行 vs 列

**对应题目：** Q28, Q35, Q39

**关键区分：**

```java
// 遍历行
for (int r = 0; r < grid.length; r++) { ... }

// 遍历列（固定某一行）
for (int c = 0; c < grid[r].length; c++) { ... }

// 遍历"第x列的所有元素"
for (int r = 0; r < grid.length; r++) {
    // grid[r][x] 就是第x列的第r个元素
}
```

**记忆：**
> `grid[r][c]` — 第一个索引是 **行(row)**，第二个是 **列(col)**
> `grid.length` = 行数
> `grid[r].length` = 第 r 行的列数

---

### 9. `indexOf` 和 `substring` 的配合

**对应题目：** Q4, Q26, Q31

**`substring` 的两种形式：**

```java
String s = "ABCDEF";
s.substring(1, 3);  // → "BC"  (从1开始到3之前，即索引1,2)
s.substring(4);     // → "EF"  (从4开始到末尾)
```

**`indexOf` 的返回值：**

```java
String s = "banana";
s.indexOf("na");     // → 2（第一次出现的位置）
s.indexOf("z");      // → -1（不存在时返回-1）
```

---

### 10. Mutator (Setter) 方法的正确写法

**对应题目：** Q6

**正确模板：**

```java
public void setXxx(Type newValue) {
    this.xxx = newValue;  // 参数赋值给实例变量
}
```

**常见错误：**

```java
// ❌ 参数和实例变量写反了
public void setA(int newA) {
    newA = myA;   // 把myA的值赋给参数（毫无意义）
}

// ❌ private方法，外部无法调用
private void setA(int newA) {
    myA = newA;
}
```

**三要素：** public、void、参数值赋给实例变量

---

## ✅ 考前检查清单（做每道题时问自己）

### 看到类型转换题：
- [ ] `(double)` 影响的是紧邻的下一个值，还是括号内整体？
- [ ] 括号内有没有整数除法（会截断小数）？

### 看到循环题：
- [ ] 代入 n=3 或 n=4，列出每次 i 的值
- [ ] 注意 `i < n` 和 `i <= n` 的区别
- [ ] 注意 `i++` 和 `i += 2` 的区别

### 看到 static 题：
- [ ] 这个变量是 static 吗？是则所有对象共享

### 看到递归题：
- [ ] Base case 是什么？参数什么时候到达 base case？
- [ ] 画调用树，注意递归前后的语句都会执行

### 看到排序题：
- [ ] 是 Insertion Sort 还是 Selection Sort？
- [ ] 动手写出每轮后的数组状态

### 看到伦理/影响题：
- [ ] 开源 = 共享协作允许修改
- [ ] 闭源 = 保护控制限制修改
- [ ] 可靠性 = 冗余 + 错误处理 + 测试

---

## 📝 针对性练习题

### 练习 1: 类型转换
```java
(int) 9.7 / 2          // = ?
(int) (9.7 / 2)        // = ?
(double) 1 / 2 + 1 / 2 // = ?
(double) (1 / 2 + 1 / 2) // = ?
```

### 练习 2: static 变量
```java
public class Counter {
    public static int total = 0;
    public int id;
    public Counter(int i) { id = i; total++; }
}
// 执行:
Counter a = new Counter(1);
Counter b = new Counter(2);
// a.id = ?  b.id = ?  Counter.total = ?
```

### 练习 3: 循环次数
```java
for (int i = 0; i < 5; i++)      // 执行几次？
for (int i = 1; i <= 5; i++)     // 执行几次？
for (int i = 0; i < 10; i += 3)  // i 分别取什么值？
```

### 练习 4: 递归跟踪
```java
public static int mystery(int n) {
    if (n <= 1) return 1;
    return n + mystery(n - 1);
}
// mystery(4) = ?
```

<details>
<summary>点击查看答案</summary>

**练习1：**
```
(int) 9.7 / 2          → 4      (9/2=4)
(int) (9.7 / 2)        → 4      (4.85→4)
(double) 1 / 2 + 1 / 2 → 0.0    (0.5 + 0 = 0.5? 不对！)
// 等等：1/2=0, 所以 0.5 + 0 = 0.5? 不对！
// (double)1 / 2 = 0.5
// 1 / 2 = 0（整数除法）
// 0.5 + 0 = 0.5 ✅
(double) (1 / 2 + 1 / 2) → 1.0  (0+0=0, 再转double)
```

**练习2：**
```
a.id = 1, b.id = 2, Counter.total = 2
// 注意：如果后面再执行 new Counter(3)，total 会变成 3
// 但 a.id 始终是 1（不会被改变）
```

**练习3：**
```
0,1,2,3,4   → 5次
1,2,3,4,5   → 5次
0,3,6,9     → 4次（i=12时不满足<10）
```

**练习4：**
```
mystery(4) = 4 + mystery(3)
           = 4 + (3 + mystery(2))
           = 4 + 3 + (2 + mystery(1))
           = 4 + 3 + 2 + 1
           = 10
```

</details>

---

> **最后提醒：** 这些错题不是"马虎"，是概念漏洞。每道错题都要做到：能说出正确答案为什么对，自己的错误选项为什么错，才算真正掌握。
