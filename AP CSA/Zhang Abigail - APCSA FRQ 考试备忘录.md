# Zhang Abigail - APCSA FRQ 考试备忘录

> 基于 Practice Exam 2 FRQ 的答卷分析

---

## 📊 总体表现概览

| 题目 | 满分 | 预估得分 | 核心问题 |
|------|------|----------|----------|
| Q1 RobotMover 构造函数 | 4 | 0 | 基础语法完全混乱 |
| Q2 countOccurrences | 3 | 0 | String方法、循环逻辑完全错误 |
| Q3 LapTracker 完整类 | 7 | 0 | 类结构、方法嵌套、概念混乱 |
| Q4 playerWithClosestScore | 5 | 0 | ArrayList、算法、返回值全错 |
| Q5 countOrderedRows | 6 | 0 | 数组访问、比较逻辑、返回值 |
| **总计** | **25** | **0** | **Java基础概念亟需重建** |

---

## 🚨 诊断：当前处于"概念混乱期"

你的代码显示出对以下最基础概念的混淆：

1. **变量声明** 和 **参数使用** 分不清
2. **类结构** 和 **方法嵌套** 概念不清
3. **String/数组/ArrayList** 三种数据结构的语法完全混用
4. **方法调用** 和 **对象访问** 语法错误

**这不是细节错误，是需要重建知识框架的问题。**

---

## 🔧 第一优先级：重建Java基础骨架

### 1. 变量声明 vs 参数使用（Q1致命错误）

**你的错误代码：**
```java
public RobotMover(int numMoves){
    int numMoves = Math.Random() * (numMoves+1);  // ❌ 灾难性错误！
```

**问题分析：**
- `int numMoves` 在参数列表中已经存在了
- 你在方法体内又声明了同名变量，造成"变量遮蔽"
- `Math.Random()` 大写R错误，且没有类型转换

**你必须记住的规则：**
```java
public RobotMover(int numMoves) {  // ← 参数已经在括号里声明了
    // 不需要再声明 int numMoves！
    // 直接使用 numMoves 即可
    
    this.moveSequence = "";  // 实例变量需要 this. 或直接用名称
    
    for (int i = 0; i < numMoves; i++) {  // ✅ 循环变量i才需要声明
        // ...
    }
}
```

**黄金法则：**
> 参数已经"自带声明"，进方法就能直接用，**绝对不要**在方法内再写 `int 参数名`！

---

### 2. Math.random() 的正确用法（Q1）

**你的错误：**
```java
Math.Random() * (numMoves+1)  // ❌ Random大写，且无意义
```

**正确模板（必须背下来）：**
```java
// 生成 [0, n) 范围的整数：0, 1, 2, ..., n-1
int randomNum = (int)(Math.random() * n);

// 本题：4个方向，生成 0, 1, 2, 3
int dir = (int)(Math.random() * 4);

// 注意括号位置！先乘后转！
```

**常见错误对照：**
| 错误 | 正确 |
|------|------|
| `Math.Random()` | `Math.random()` |
| `(int)Math.random() * 4` | `(int)(Math.random() * 4)` |
| `Math.random() * 4`（没转int）| `(int)(Math.random() * 4)` |

---

### 3. 类结构：绝对不能方法嵌套方法！（Q3致命错误）

**你的错误代码（完全错误的结构）：**
```java
public class LapTracker{
    private times;  // ❌ 缺类型
    
    public LapTracker(int times){
        int count = 0;
        
        public int addLaps(int num){  // ❌❌❌ 在构造函数里定义方法！
            // ...
        }  // 这是Java语法的绝对禁区！
    }
}
```

**正确的类骨架（必须刻进DNA）：**
```java
public class 类名 {
    // 1. 实例变量（在类里面，方法外面）
    private int var1;
    private String var2;
    
    // 2. 构造函数（和类同名，无返回类型）
    public 类名(参数) {
        this.var1 = 初始值;
    }
    
    // 3. 普通方法（有返回类型，不能嵌套）
    public int method1(int param) {
        return something;
    }
    
    // 4. 可以有更多方法，都是平级的！
    public void method2() {
        // ...
    }
}
```

**关键记忆点：**
- 类 = 盒子
- 盒子里放：变量 + 构造函数 + 方法
- **方法不能嵌套在方法里！** 它们都是平级放在类里的！

---

### 4. String是对象，length是方法！（Q2, Q5反复错）

**你的错误：**
```java
moveSequence.length     // ❌ String的length是方法，不是属性
```

**必须记住的区别：**

| 类型 | 获取长度 | 示例 |
|------|---------|------|
| `String` | `.length()` | `"hello".length()` → 5 |
| 数组 `[]` | `.length` | `arr.length` |
| `ArrayList` | `.size()` | `list.size()` |

**对比：**
```java
String s = "hello";
int len1 = s.length();      // ✅ 方法，有括号

String[] arr = {"a", "b"};
int len2 = arr.length;      // ✅ 属性，无括号

ArrayList<String> list = new ArrayList<>();
int len3 = list.size();     // ✅ 方法，有括号
```

---

### 5. ArrayList访问元素：必须用.get(i)（Q4致命错误）

**你的错误：**
```java
playerList.[i]           // ❌ 语法错误！
target-playerList.[i]    // ❌ 且playerList[i]返回Player对象，不能直接减
```

**正确写法：**
```java
// 获取第i个元素
Player p = playerList.get(i);

// 获取该玩家的分数
int score = p.getScore();

// 计算差值
int diff = Math.abs(targetScore - score);

// 或者一行写：
int diff = Math.abs(targetScore - playerList.get(i).getScore());
```

**ArrayList操作速查：**
```java
ArrayList<Player> list = new ArrayList<>();

list.add(p);           // 添加
list.size();           // 大小（不是length！）
list.get(i);           // 获取第i个（不是[i]！）
list.set(i, p);        // 设置第i个
```

---

### 6. 方法调用的正确语法（Q4错误）

**你的错误：**
```java
(Math.abs)(target-playerList.[i])  // ❌ Math.abs不是对象，不能这样调用
playerList.[i]                     // ❌ 语法错误
```

**正确：**
```java
Math.abs(targetScore - playerList.get(i).getScore())  // ✅
```

**Math.abs的用法：**
```java
int diff = Math.abs(a - b);   // ✅ 直接传入一个表达式
```

---

### 7. 返回值类型必须匹配！（Q4, Q5）

**Q4你的错误：**
```java
public String playerWithClosestScore(...){
    // ...
    return playerList.[i];   // ❌ 返回Player对象，但方法声明返回String！
}
```

**正确：**
```java
public String playerWithClosestScore(...){
    // ...
    return playerList.get(i).getID();  // ✅ 返回String
}
```

**Q5你的错误：**
```java
public int countOrderedRows(){   // 应该返回int计数
    // ...
    return r;   // ❌ 返回行号！应该返回符合条件的行数！
}
```

**正确：**
```java
public int countOrderedRows(){
    int count = 0;   // ✅ 计数器
    for (...) {
        if (行是有序的) {
            count++;
        }
    }
    return count;    // ✅ 返回计数
}
```

---

### 8. 数组访问不能漏名字（Q5）

**你的错误：**
```java
if ([r][c] < [r][c+1]) {  // ❌ grid去哪了？
```

**正确：**
```java
if (grid[r][c].length() <= grid[r][c+1].length()) {  // ✅
```

---

### 9. 不要硬编码数字（Q5）

**你的错误：**
```java
for (int r = 0; r < 5; r++) {       // ❌ 硬编码5
    for (int c = 0; c < 4; c++) {   // ❌ 硬编码4
```

**正确：**
```java
for (int r = 0; r < grid.length; r++) {           // ✅ 用数组属性
    for (int c = 0; c < grid[r].length - 1; c++) { // ✅ 每行长度可能不同
```

---

### 10. 变量声明必须有类型（Q3）

**你的错误：**
```java
private times;  // ❌ 没有类型！
```

**正确：**
```java
private int times;        // ✅ 
private int count;
private String name;
```

---

## 📝 各题正确写法（对照学习）

### Q1: RobotMover 构造函数

```java
public RobotMover(int numMoves) {
    moveSequence = "";
    String[] dirs = {"up", "down", "left", "right"};
    
    for (int i = 0; i < numMoves; i++) {
        int rand = (int)(Math.random() * 4);
        moveSequence += dirs[rand] + "_";
    }
}
```

**你需理解的关键点：**
- 参数 `numMoves` 直接用，不用重新声明
- `Math.random()` 小写r
- `(int)(...)` 强制转换括号包裹整个表达式
- 随机数在**循环内**生成，每次循环都不同
- `moveSequence` 是实例变量，直接赋值

---

### Q2: countOccurrences

```java
public int countOccurrences(String str) {
    int count = 0;
    String temp = moveSequence;
    
    while (temp.indexOf(str) >= 0) {
        int loc = temp.indexOf(str);
        temp = temp.substring(loc + 1);
        count++;
    }
    return count;
}
```

**你需理解的关键点：**
- `indexOf` 和 `substring` 全小写
- 用临时变量 `temp` 避免修改原始 `moveSequence`
- `substring(loc + 1)` 从找到位置的下一个字符开始，允许重叠匹配

---

### Q3: LapTracker 完整类

```java
public class LapTracker {
    private int numLaps;
    private int numCalls;
    private int resetFrequency;
    
    public LapTracker(int resetFreq) {
        numLaps = 0;
        numCalls = 0;
        resetFrequency = resetFreq;
    }
    
    public int addLaps(int additionalLaps) {
        if (numCalls == resetFrequency) {
            numCalls = 0;
            numLaps = 0;
        }
        numCalls++;
        numLaps += additionalLaps;
        return numLaps;
    }
}
```

**你需理解的关键点：**
- 类里先放变量，再放构造函数，最后放方法
- **方法之间是平级的，不能嵌套！**
- 每个变量声明都要有类型
- `numCalls` 记录调用次数，到达 `resetFrequency` 时重置

---

### Q4: playerWithClosestScore

```java
public String playerWithClosestScore(int targetScore) {
    int minDiff = Math.abs(targetScore - playerList.get(0).getScore());
    String result = playerList.get(0).getID();
    
    for (int j = 1; j < playerList.size(); j++) {
        int diff = Math.abs(targetScore - playerList.get(j).getScore());
        if (diff < minDiff) {
            minDiff = diff;
            result = playerList.get(j).getID();
        }
    }
    return result;
}
```

**你需理解的关键点：**
- `playerList.get(j)` 获取Player对象
- `.getScore()` 获取分数
- `.getID()` 获取String ID
- 返回类型是String，所以return后面必须是String

---

### Q5: countOrderedRows

```java
public int countOrderedRows() {
    int count = 0;
    
    for (int r = 0; r < grid.length; r++) {
        boolean ordered = true;
        
        for (int c = 0; c < grid[r].length - 1; c++) {
            if (grid[r][c].length() > grid[r][c + 1].length()) {
                ordered = false;
            }
        }
        
        if (ordered) {
            count++;
        }
    }
    return count;
}
```

**你需理解的关键点：**
- `grid.length` 获取行数（属性，无括号）
- `grid[r][c].length()` 获取字符串长度（方法，有括号）
- 比较的是 `.length()`，不是字符串本身
- `ordered` 每行开始时重置为true
- 最后返回 `count`，不是行号

---

## ✅ 每日基础训练（必做，至少连续5天）

### 训练1：变量声明（5分钟）
写出以下变量的正确声明：
```
整数count初始为0 → _______________
字符串name → _______________
Player数组players → _______________
ArrayList<String>列表 → _______________
```

### 训练2：填空（5分钟）
```java
public class Dog {
    _____ String name;        // 声明实例变量
    
    public _____(String n) {  // 构造函数
        name = n;
    }
    
    public _____ getName() {  // 返回String的方法
        return _____;
    }
}
```

### 训练3：改错（10分钟）
找出以下代码中的所有错误：
```java
public class Test {
    private count;
    
    public void Test(int c) {
        int count = c;
        
        public int get() {
            return count;
        }
    }
}
```
（参考答案：缺类型、构造函数不应有void、方法嵌套、局部变量覆盖实例变量）

### 训练4：手写标准答案（15分钟）
不看参考，手写Q1-Q5的标准答案，然后对照检查。

---

## 🎯 考试策略（现阶段）

由于基础语法尚不牢固，建议：

1. **先保1-2道题全对**，而不是5道题都写一半
2. **写完后大声朗读代码**，检查：
   - 每个变量有没有类型？
   - 方法有没有嵌套？
   - return的类型对不对？
3. **如果一道题完全不会，先跳过**，把时间给有把握的题

---

## 📚 推荐学习顺序

不要直接刷题！按这个顺序重建基础：

1. **Day 1-2**: 类结构（变量、构造函数、方法的正确位置和语法）
2. **Day 3**: String方法（length(), indexOf(), substring(), equals()）
3. **Day 4**: 数组 vs ArrayList（访问方式的区别）
4. **Day 5**: Math.random() 和类型转换
5. **Day 6-7**: 重新做这套题，对照标准答案逐行理解

---

> **核心建议**：你目前最需要的是"**正确的代码模板**"而不是"解题思路"。把上面5道题的标准答案抄写并背诵，直到能独立默写为止。APCSA FRQ有很多固定套路，模板背熟了就能拿到基础分。
