# Cai Lucy Cai - APCSA FRQ 考试备忘录

> 基于 Practice Exam 2 FRQ 的答卷分析

---

## 📊 总体表现概览

| 题目 | 满分 | 预估得分 | 核心问题 |
|------|------|----------|----------|
| Q1 RobotMover 构造函数 | 4 | 0 | 基础语法混乱，构造函数概念不清 |
| Q2 countOccurrences | 3 | 0 | String方法大小写、循环逻辑 |
| Q3 LapTracker 完整类 | 7 | 0 | 类结构完全错误 |
| Q4 playerWithClosestScore | 5 | 0-1 | ArrayList操作、比较运算符 |
| Q5 countOrderedRows | 6 | 0-1 | 数组属性、字符串长度比较 |
| **总计** | **25** | **0-2** | |

---

## 🚨 最高优先级：必须立即纠正的错误

### 1. 构造函数基础（Q1, Q3 全军覆没的根本原因）

**错误示例（你的代码）：**
```java
public void main LapTracker(int number){  // ❌ 完全错误
public addLaps(int num){                   // ❌ 缺少返回类型
```

**正确规则：**
- 构造函数 **没有返回类型**，连 `void` 都没有
- 构造函数名称 **必须和类名完全一致**
- 构造函数 **不能 return 值**

```java
public class LapTracker {
    private int count;  // 实例变量
    
    public LapTracker(int number) {  // ✅ 正确：无返回类型，名称=类名
        this.count = 0;
    }
    
    public int addLaps(int num) {    // ✅ 正确：普通方法需要返回类型
        return count;
    }
}
```

---

### 2. Java 区分大小写！（Q2 失分主因）

**错误示例（你的代码）：**
```java
int i = moveSequence.IndexOf(str);  // ❌ IndexOf 不存在
```

**正确：**
```java
int i = moveSequence.indexOf(str);  // ✅ indexOf i小写
```

**常见 String 方法（必须全小写）：**
| 错误写法 | 正确写法 |
|----------|----------|
| `IndexOf` | `indexOf` |
| `SubString` | `substring` |
| `Length` | `length` |
| `Equals` | `equals` |

---

### 3. ArrayList vs 数组的语法区别（Q4 核心错误）

**错误示例（你的代码）：**
```java
playerList.length()          // ❌ ArrayList 用 size()
playerList[i]                // ❌ ArrayList 用 get(i)
String ArrayList<String> x;  // ❌ 声明语法错误
```

**正确对照表：**

| 操作 | 数组 `String[]` | ArrayList `ArrayList<String>` |
|------|-----------------|-------------------------------|
| 获取长度 | `arr.length` | `list.size()` |
| 访问元素 | `arr[i]` | `list.get(i)` |
| 添加元素 | 不能动态添加 | `list.add(item)` |
| 声明 | `String[] arr;` | `ArrayList<String> list;` |

```java
// ✅ 正确访问 ArrayList
for (int i = 0; i < playerList.size(); i++) {
    Player p = playerList.get(i);
    int score = p.getScore();
}

// ✅ 或用增强for循环
for (Player p : playerList) {
    int score = p.getScore();
}
```

---

### 4. 比较运算符 `==` vs 赋值运算符 `=`（Q4 致命错误）

**错误示例（你的代码）：**
```java
if (Math.abs(...) = minScore) {  // ❌ 这是赋值！不是比较！
```

**正确：**
```java
if (Math.abs(...) == minScore) {  // ✅ 双等号才是比较
```

**记忆口诀：**
- `=` 赋值：把右边的值给左边
- `==` 比较：判断两边是否相等
- 条件判断中 **永远用 `==`**（除非故意赋值）

---

### 5. 数组的 `.length` 是属性，不是方法（Q5 错误）

**错误示例（你的代码）：**
```java
grid.length()      // ❌ 数组没有括号
grid[0].length()-1 // ❌ 这是String[]数组，grid[0]是String[]，用length属性
```

**正确：**
```java
grid.length              // ✅ 二维数组的行数（属性，无括号）
grid[i].length           // ✅ 第i行的列数（属性，无括号）
grid[i][j].length()      // ✅ String的长度（方法，有括号）
```

**关键区分：**
- `数组.length` — 属性，无括号
- `字符串.length()` — 方法，有括号
- `ArrayList.size()` — 方法，有括号

---

## ⚠️ 高优先级：常见语法陷阱

### 6. 类型转换必须显式写出（Q1 错误）

**错误示例（你的代码）：**
```java
int i = Math.random() * 4;  // ❌ random()返回double，需要强转
```

**正确：**
```java
int i = (int)(Math.random() * 4);  // ✅ 先乘后转，括号位置很重要
```

---

### 7. String 比较要调 `.length()`（Q5 核心错误）

**错误示例（你的代码）：**
```java
if (grid[i][j] > grid[i][j+1]) {  // ❌ 比较的是字符串引用，不是长度
```

**正确：**
```java
if (grid[i][j].length() > grid[i][j+1].length()) {  // ✅ 比较字符串长度
```

---

### 8. 变量初始化与重置（Q5 flag错误）

**错误示例（你的代码）：**
```java
boolean flag = true;  // 只初始化一次
for (...) {
    // flag=false后永远变不回true
}
```

**正确：**
```java
for (int i = 0; i < grid.length; i++) {
    boolean flag = true;  // ✅ 每行开始时重置
    for (...) {
        if (...) flag = false;
    }
    if (flag) count++;
}
```

---

### 9. 局部变量 vs 实例变量（Q1, Q2 错误）

**错误示例（你的代码）：**
```java
String moveSequence = moveSequence + ...;  // ❌ 声明了局部变量，不是用实例变量
```

**正确：**
```java
this.moveSequence = this.moveSequence + ...;  // ✅ 明确使用实例变量
// 或
moveSequence = moveSequence + ...;            // ✅ 如果没有局部变量同名，自动用实例变量
```

---

### 10. 拼写检查（Q5）

| 错误拼写 | 正确拼写 |
|----------|----------|
| `ture` | `true` |
| `moveSequnce` | `moveSequence` |
| `ClosetList` | `ClosestList` |

---

## 📝 各题具体分析与正确写法

### Q1: RobotMover 构造函数

**题目要求：** 生成 numMoves 个随机方向，用 "_" 连接

**你的问题：**
- 语法错误：ArrayList声明错误
- 随机数只生成一次（在循环外）
- 局部变量覆盖实例变量
- 构造函数return值

**正确写法：**
```java
public RobotMover(int numMoves) {
    moveSequence = "";
    String[] dirs = {"up", "down", "left", "right"};
    for (int i = 0; i < numMoves; i++) {
        int rand = (int)(Math.random() * 4);  // 每次循环重新随机
        moveSequence += dirs[rand] + "_";
    }
}
```

---

### Q2: countOccurrences

**题目要求：** 统计 str 在 moveSequence 中出现次数

**你的问题：**
- `IndexOf` 大小写错误
- substring调用方式错误
- 无限循环（没有正确更新字符串）

**推荐写法（标准答案风格）：**
```java
public int countOccurrences(String str) {
    int count = 0;
    String temp = moveSequence;
    while (temp.indexOf(str) >= 0) {
        int loc = temp.indexOf(str);
        temp = temp.substring(loc + 1);  // 关键：从loc+1开始，允许重叠
        count++;
    }
    return count;
}
```

---

### Q3: LapTracker 完整类

**题目要求：** 每 resetFrequency 次调用 addLaps 后，lap计数重置为0

**你的问题：**
- 构造函数语法完全错误
- 没有实例变量
- 方法逻辑完全错误

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
        if (numCalls == resetFrequency) {  // 先检查是否到达重置点
            numCalls = 0;
            numLaps = 0;
        }
        numCalls++;
        numLaps += additionalLaps;
        return numLaps;
    }
}
```

**关键逻辑：**
- 第3次调用addLaps返回后，numCalls==3，下次调用时先重置
- 或者理解成：调用前先检查，如果numCalls已经等于resetFrequency就重置

---

### Q4: playerWithClosestScore

**题目要求：** 返回分数最接近 targetScore 的玩家ID

**你的问题：**
- ArrayList操作语法错误（length, [i]）
- 声明语法错误
- `=` 误用为 `==`
- 返回类型不匹配（返回ArrayList而非String）

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

**题目要求：** 统计二维数组中按字符串长度非递减排序的行数

**你的问题：**
- `ture` 拼写
- `grid.length()` 错误
- 字符串直接比较（未调.length()）
- flag未在每行重置

**正确写法（标准答案）：**
```java
public int countOrderedRows() {
    int count = 0;
    for (int r = 0; r < grid.length; r++) {  // grid.length无括号
        boolean rowInOrder = true;              // 每行重置
        for (int c = 0; c < grid[r].length - 1; c++) {
            if (grid[r][c].length() > grid[r][c + 1].length()) {  // .length()
                rowInOrder = false;
            }
        }
        if (rowInOrder) {
            count++;
        }
    }
    return count;
}
```

---

## ✅ 考试检查清单（写完后逐条核对）

### 语法检查
- [ ] 所有方法名大小写正确（indexOf, not IndexOf）
- [ ] 数组用 `.length`，String用 `.length()`，ArrayList用 `.size()`
- [ ] ArrayList元素用 `.get(i)` 访问，不是 `[i]`
- [ ] 比较用 `==`，赋值用 `=`，不要混用
- [ ] 类型转换加括号：`(int)(Math.random() * n)`
- [ ] 拼写检查：true, not ture

### 构造函数检查
- [ ] 没有返回类型（没有 void, int, String 等）
- [ ] 名称和类名完全一致
- [ ] 没有 return 语句

### 类结构检查
- [ ] 实例变量声明为 private
- [ ] 实例变量在类内部、方法外部
- [ ] 方法有正确的返回类型

### 逻辑检查
- [ ] 循环变量是否在正确位置重置
- [ ] 随机数是否在循环内重新生成
- [ ] String比较是否调用了 .length()
- [ ] 是否修改了不应修改的实例变量（如Q2要求moveSequence unchanged）

---

## 🎯 练习建议

1. **抄写标准答案**：把上面5道题的正确答案手抄3遍，建立肌肉记忆
2. **专项练习**：
   - 构造函数写法（每天至少写5个不同类的构造函数）
   - ArrayList操作（.size(), .get(), 增强for循环）
   - String方法（indexOf, substring, length, equals）
3. **限时模拟**：25分钟完成5道题，模拟真实考试压力
4. **互查代码**：和同学交换代码，互相找语法错误

---

> **核心问题诊断**：目前最大的问题不是算法思路，而是 **Java基础语法不熟练**。建议先暂停做新题，用2-3天专门复习类结构、构造函数、ArrayList、String方法的正确写法，然后再回来刷题。
