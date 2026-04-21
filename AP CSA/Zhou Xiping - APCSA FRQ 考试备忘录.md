# Zhou Xiping - APCSA FRQ 考试备忘录

> 基于 Practice Exam 2 FRQ 的答卷分析

---

## 📊 总体表现概览

| 题目 | 满分 | 预估得分 | 核心问题 |
|------|------|----------|----------|
| Q1 RobotMover 构造函数 | 4 | 0 | 无构造函数声明、语法混乱 |
| Q2 countOccurrences | 3 | 0 | String方法、循环逻辑错误 |
| Q3 LapTracker 完整类 | 7 | 0 | 类结构完全崩溃 |
| Q4 playerWithClosestScore | 5 | 0 | 无方法声明、ArrayList语法 |
| Q5 countOrderedRows | 6 | 0 | 无方法声明、for语法错误 |
| **总计** | **25** | **0** | **Java语法框架需从零重建** |

---

## 🚨 紧急诊断：代码"散落"问题

你的代码最大的问题是：**代码不在应该待的地方**。

### 典型症状

```java
public class LapTracker{
    private int count;
    
    public getCount()           // ← 方法没括号、没类型
        return count;
    
    int count=LapTracker.getCount();  // ← 类里直接写执行代码！
    int sum=0;
    if(i<count){                // ← if在类里，不在方法里！
        public int addLaps(int num)   // ← 方法嵌套在if里！
            sum=sum+num;
    }
    i++                         // ← 游离代码！
```

**这就像把家具堆在房间中央，而不是放在该放的位置。**

---

## 🔧 第一优先级：建立"代码该放哪里"的概念

### 1. Java程序的四个层级（必须记住！）

```
第1层：类 (class)
    ↓
第2层：变量 和 方法/构造函数
    ↓
第3层：方法内部的语句（if/for/赋值/调用）
    ↓
第4层：表达式（计算、比较）
```

**你的错误：把第3层的东西放在了第2层！**

| 层级 | 可以放 | 不可以放 |
|------|--------|---------|
| 类里面 | 变量声明、方法、构造函数 | if语句、for循环、直接执行的代码 |
| 方法里面 | if、for、return、赋值、调用 | 其他方法、变量声明（不带private）|

---

### 2. 方法声明的完整语法（Q1, Q4, Q5 全部缺少！）

**你的错误：** 直接写代码，不写方法声明。

```java
// ❌ 你的写法：代码直接飘在外面
for(int k=0; k<playerList.length(), k++){
    // ...
}

// ✅ 正确写法：必须有方法头包裹
public String playerWithClosestScore(int targetScore) {
    for(int k=0; k<playerList.size(); k++){
        // ...
    }
    return result;
}
```

**方法声明模板（必须背诵）：**
```java
public 返回类型 方法名(参数类型 参数名) {
    // 方法体
    return 返回值;  // 如果返回类型不是void
}
```

**实例：**
```java
public int add(int a, int b) {   // public + 返回类型 + 名 + (参数)
    return a + b;                 // 方法体
}                                  // 结束括号
```

---

### 3. for循环的语法（Q1, Q5 错误）

**你的错误：**
```java
for(int i;i<numMoves;i++)        // ❌ i没初始化
for(int i=0,i<grid.length(),i++) // ❌ 用逗号分隔
```

**for循环固定格式（背下来）：**
```java
for (初始化; 条件; 更新) {
    // 循环体
}
//     ↑      ↑     ↑
//   分号   分号  没有逗号！
```

**正确示例：**
```java
for (int i = 0; i < numMoves; i++) {      // ✅
for (int j = 0; j < grid.length; j++) {   // ✅
for (int k = 0; k < list.size(); k++) {   // ✅
```

**常见错误对照：**
| 错误 | 正确 |
|------|------|
| `for(int i;i<n;i++)` | `for(int i=0;i<n;i++)` |
| `for(int i=0,i<n,i++)` | `for(int i=0;i<n;i++)` |
| `for(int i=0;i<n,i++)` | `for(int i=0;i<n;i++)` |

---

### 4. 方法必须有返回类型（Q3 致命错误）

**你的错误：**
```java
public getCount()       // ❌ 缺少返回类型
    return count;
```

**正确：**
```java
public int getCount() {  // ✅ 返回int
    return count;
}
```

**规则：**
- 返回整数 → `public int`
- 返回字符串 → `public String`
- 返回布尔 → `public boolean`
- 不返回 → `public void`
- 构造函数 → **没有返回类型**（连void都没有）

---

### 5. 构造函数识别与写法（Q1, Q3）

**题目说"Complete the RobotMover constructor"** → 你必须写出：

```java
public RobotMover(int numMoves) {
    // 你的代码
}
```

**你的错误：** 只写了循环体，没写构造函数头。

**构造函数三要素：**
1. **没有返回类型**（没有int/String/void）
2. **名称=类名**
3. **有参数就写在括号里**

```java
public class LapTracker {
    // 构造函数：名=类名，无返回类型
    public LapTracker(int resetFreq) {
        // 初始化代码
    }
}
```

---

### 6. 数组声明与访问（Q1）

**你的错误：**
```java
arr[] direction=["up","down","left","right"]  // ❌ 类型位置错，应用花括号
```

**正确：**
```java
String[] direction = {"up", "down", "left", "right"};
// ↑类型    ↑变量名    ↑花括号！
```

**数组要点：**
```java
// 声明并初始化
String[] dirs = {"up", "down", "left", "right"};

// 访问元素
String first = dirs[0];     // "up"

// 获取长度
int len = dirs.length;      // 属性，无括号！
```

---

### 7. Math.random() 的正确写法（Q1）

**你的错误：**
```java
(MATH.random()*5)   // ❌ MATH大写，且*5范围错误
```

**正确：**
```java
(int)(Math.random() * 4)   // ✅ 生成0,1,2,3
//    ↑小写  ↑*4不是*5
```

**注意：**
- `Math` 不是 `MATH`
- `random()` 不是 `Random()`
- 4个方向用 `*4`，不是 `*5`

---

### 8. String方法大小写（Q2）

**你的错误：**
```java
list.subString(pos,pos+length)    // ❌ 大写S
moveSequence.subString(...)       // ❌ 大写S
```

**正确：**
```java
list.substring(start, end)        // ✅ 全小写
moveSequence.substring(start, end) // ✅ 全小写
```

**String常用方法（全小写）：**
| 方法 | 作用 |
|------|------|
| `length()` | 字符串长度 |
| `indexOf(str)` | 查找子串位置 |
| `substring(a, b)` | 截取子串 |
| `equals(other)` | 比较内容 |

---

### 9. ArrayList vs 数组（Q4 严重错误）

**你的错误：**
```java
playerList.length()          // ❌ ArrayList用size()
playerList[i][k]             // ❌ 双重数组语法
playerList.length(),k++      // ❌ 逗号分隔for语句
```

**正确：**
```java
playerList.size()                    // ✅ 获取元素个数
playerList.get(k)                    // ✅ 获取第k个元素
playerList.get(k).getScore()         // ✅ 获取分数
```

**ArrayList速查表：**
```java
ArrayList<Player> list = ...;

int n = list.size();              // 大小
Player p = list.get(i);           // 获取第i个
int score = p.getScore();         // 获取分数
String id = p.getID();            // 获取ID
```

---

### 10. 变量不能重复声明（Q2 错误）

**你的错误：**
```java
String list = new String moveSequence;   // 第一次声明
// ...
String list = moveSequence.subString(...); // ❌ 重复声明String list
```

**正确：**
```java
String list = moveSequence;    // 第一次声明
// ...
list = moveSequence.substring(...); // ✅ 第二次只写名字，不加类型
```

**规则：**
- 第一次声明：`类型 名字 = 值;`
- 后续赋值：`名字 = 新值;`（不要加类型！）

---

## 📝 各题分析与正确写法

### Q1: RobotMover 构造函数

**你的问题：**
- 没写构造函数头
- 数组声明语法错误
- for循环i没初始化
- MATH大写
- 用了System.out.print而不是给moveSequence赋值

**正确写法：**
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

---

### Q2: countOccurrences

**你的问题：**
- substring大写
- indexOf没有推进
- 重复声明变量
- 逻辑混乱

**推荐写法（标准答案）：**
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

---

### Q3: LapTracker

**你的问题：**
- 类里直接写执行代码
- 方法嵌套在if里
- 没有构造函数
- 没有返回类型

**正确写法（标准答案）：**
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

**结构要点：**
```
class LapTracker {
    变量声明（private）
    
    构造函数（public LapTracker(...)）
    
    方法1（public int addLaps(...)）
    
    方法2（...）
}
```

---

### Q4: playerWithClosestScore

**你的问题：**
- 没写方法头
- playerList.length() → size()
- playerList[i][k] → get()
- 没有取绝对值
- return在循环里
- 拼写错误 platerList

**正确写法（标准答案）：**
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

---

### Q5: countOrderedRows

**你的问题：**
- 没写方法头
- for用逗号分隔
- grid.length() → grid.length
- i++写成内层循环的更新
- return在循环内
- 没有行级判断逻辑

**正确写法（标准答案）：**
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

---

## ✅ 代码位置自查表（写完后逐项核对）

### 类结构检查
```
□ 类名是否和文件名一致？
□ 变量是否都有private和类型？
□ 变量是否在类内部、方法外部？
□ 方法是否都在类里面、互相不嵌套？
□ 没有游离的if/for/赋值语句在类里？
```

### 方法声明检查
```
□ 每个方法都有 public 返回类型 方法名() { ？
□ 返回类型是否正确（int/String/void）？
□ 方法体是否被 {} 包裹？
```

### for循环检查
```
□ 格式：for (int i = 0; i < n; i++) ？
□ 三个部分用分号; 分隔，不是逗号, ？
□ 循环变量是否初始化了？
```

### 访问语法检查
```
□ 数组.length（无括号）？
□ String.length()（有括号）？
□ ArrayList.size()（有括号）？
□ ArrayList.get(i)（不是[i]）？
```

---

## 🎯 每日训练计划

### 第1天：方法声明（30分钟）
抄写并理解下面模板：
```java
public class Demo {
    private int x;
    
    public Demo(int val) {      // 构造函数
        x = val;
    }
    
    public int getX() {         // 返回int的方法
        return x;
    }
    
    public void setX(int val) { // 不返回的方法
        x = val;
    }
}
```

### 第2天：for循环（20分钟）
手写10个正确的for循环：
```java
for (int i = 0; i < 10; i++) { }
for (int j = 0; j < arr.length; j++) { }
for (int k = 0; k < list.size(); k++) { }
// ... 自己写7个
```

### 第3天：ArrayList操作（20分钟）
```java
ArrayList<String> list = new ArrayList<>();
// 写出获取大小、获取元素、遍历的代码
```

### 第4-5天：默写标准答案
不看参考，手写Q1-Q5的标准答案。

---

## 📋 考试应急策略

**如果时间有限，只做这些保分动作：**

1. **每道题先写方法头**
   ```java
   public int countOccurrences(String str) {
       // 即使后面不会写，也有结构分的可能
   }
   ```

2. **声明必要的变量**
   ```java
   int count = 0;
   String temp = ...;
   ```

3. **写一个空的return**
   ```java
   return count;  // 或 return "";
   ```

**这比写一堆散落的代码得分更高！**

---

> **核心建议**：你现在最需要的是"**代码组织纪律**"。Java是严格结构化的语言，每行代码都有它该在的位置。先把"什么东西该放在哪里"搞清楚，再谈算法逻辑。
