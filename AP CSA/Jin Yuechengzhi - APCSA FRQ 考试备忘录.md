# Jin Yuechengzhi - APCSA FRQ 考试备忘录

> 基于 Practice Exam 2 FRQ 的答卷分析

---

## 📊 总体表现概览

| 题目 | 满分 | 预估得分 | 核心问题 |
|------|------|----------|----------|
| Q1 RobotMover 构造函数 | 4 | 0-1 | 循环变量未初始化、Random调用语法错 |
| Q2 countOccurrences | 3 | 0 | char比较用equals、循环条件混乱 |
| Q3 LapTracker 完整类 | 7 | 3-4 | reset逻辑错误、return变量名错 |
| Q4 playerWithClosestScore | 5 | 2-3 | 拼写错误、过度复杂化、变量未初始化 |
| Q5 countOrderedRows | 6 | 2-3 | 类型不匹配、方法名拼写 |
| **总计** | **25** | **7-11** | **细节错误多、喜欢复杂解法** |

---

## ✅ 优势（保持！）

相比其他同学，你的**基础框架是正确的**：
- 类结构清晰（Q3）
- 方法声明完整（Q4, Q5）
- 循环结构基本正确
- 能写出有一定逻辑的代码

**问题不是"不会"，而是"写不对"！**

---

## 🚨 第一优先级：消灭低级错误

### 1. 循环变量必须初始化（Q1 致命错误）

**你的错误：**
```java
for(int i; i < numMoves; i++) {   // ❌ i没有赋初值！
```

**正确：**
```java
for(int i = 0; i < numMoves; i++) {  // ✅ i = 0
```

**这个错误导致整道Q1几乎0分！** 在Java中，未初始化的局部变量不能直接使用，会编译错误。

**考试口诀：**
> 看到 `for(int i;` 立即警觉！必须是 `for(int i = 0;`

---

### 2. char是基本类型，用 == 比较（Q2 致命错误）

**你的错误：**
```java
moveSequence.charAt(i).equals(str.charAt(0))  // ❌ char没有equals方法！
moveSequence.charAt(k).equals(str.charAt(j))  // ❌
```

**正确：**
```java
moveSequence.charAt(i) == str.charAt(0)  // ✅ char用 ==
```

**Java比较规则：**
| 类型 | 比较方式 |
|------|---------|
| `char` | `==` |
| `int` | `==` |
| `String` | `.equals()` |
| 对象 | `.equals()` |

**记忆口诀：**
> 基本类型用 `==`，对象类型用 `.equals()`
> char, int, double 都是基本类型！

---

### 3. 拼写！拼写！拼写！（Q4 最可惜的错误）

**你的错误：**
```java
.gerScore()     // ❌ 漏了t
playList        // ❌ 少了ayer
targetSocre     // ❌ 少了e
.getSocre()     // ❌ e和o换位
```

**正确：**
```java
.getScore()     // ✅
playerList      // ✅
targetScore     // ✅
```

**Q4因为拼写错误至少丢了2分！** 这是最能避免的失分。

**防拼写策略：**
1. 写完后**逐字朗读**方法名
2. 记住常见词：**Score**（不是Socre）、**player**（不是play）
3. 不确定时**对照题目复制**（题目中写了 `getScore`）

---

### 4. 能用Math.abs就别手动判断（Q4 过度复杂化）

**你的代码（30+行，复杂且错）：**
```java
if(targetScore-playerList.get(0).gerScore>0){
    indicator=targetScore-playerList.get(0).getScore();
}else{
    indicator=playList.get(0).getScore()-targetScore;
}
// ... 后面还有一堆if-else判断正负
```

**标准答案（10行，简洁且对）：**
```java
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
```

**你的问题：** 手动判断正负来计算绝对值，代码量翻倍，错误翻倍。

**黄金法则：**
> 看到"求差值比较大小" → 立即用 `Math.abs()`

---

### 5. return的变量名必须存在（Q3 编译错误）

**你的错误：**
```java
return count;   // ❌ 类里没有count变量！只有lap_count！
```

**正确：**
```java
return lap_count;  // ✅
```

**另一个错误：**
```java
int place;   // 未初始化
// ... 如果if都不满足，place是什么？
return playList.get(place).getID();  // ❌ place未初始化
```

**正确：**
```java
int place = 0;   // ✅ 初始化！
```

**规则：**
- 局部变量使用前**必须赋值**
- return的变量名**必须和声明的一致**

---

### 6. Random类的正确使用（Q1）

**你的错误：**
```java
Random random = new Random();
// ...
if(a.random(4)==0)   // ❌ 变量名是random不是a，且方法不对
```

**Random的正确用法：**
```java
Random rand = new Random();
int n = rand.nextInt(4);   // ✅ 生成0,1,2,3
```

**但APCSA更推荐用Math.random()：**
```java
int n = (int)(Math.random() * 4);   // ✅ 不需要import
```

**建议：** 考试统一用 `Math.random()`，避免import和对象创建。

---

### 7. for循环三个部分必须正确（Q2）

**你的错误：**
```java
for(int j=1; str.length(); str++) {  // ❌ 条件和更新都错了！
```

**正确：**
```java
for(int j = 1; j < str.length(); j++) {  // ✅
// 初始化    条件         更新
```

**for循环模板：**
```java
for (int i = 0; i < n; i++) { }
//   ↑初始化  ↑条件   ↑更新
```

你的代码更新写的是 `str++`，str是String不会变，导致死循环。

---

### 8. String和int不能直接比较（Q5 类型错误）

**你的错误：**
```java
grid[i][j+1].length() < grid[i][j]   // ❌ int < String？类型不匹配！
```

**正确：**
```java
grid[i][j+1].length() < grid[i][j].length()   // ✅ int < int
```

**分析：**
- 左边：`grid[i][j+1].length()` → `int`
- 右边：`grid[i][j]` → `String`
- `int < String` 在Java中是编译错误！

**必须两边都调.length()！**

---

### 9. 方法名必须和题目一致（Q5）

**你的错误：**
```java
public int counterOrderedRows() {  // ❌ 多了个r，应该是countOrderedRows
```

**APCSA严格规则：** 方法名写错 = 该方法不被调用 = 可能0分

**对策：** 直接复制题目中的方法名！

---

### 10. 不要假设所有行长度相同（Q5）

**你的错误：**
```java
for(int j=0; j<grid[0].length-1; j++) {  // ❌ 用第0行长度代表所有行
```

**正确：**
```java
for(int j=0; j<grid[i].length-1; j++) {  // ✅ 用当前行i的长度
```

---

## 📝 各题详细分析与正确写法

### Q1: RobotMover 构造函数

**你的问题：**
- `int i` 未初始化
- `a.random(4)` 变量名和方法都错

**正确写法：**
```java
public RobotMover(int numMoves) {
    moveSequence = "";
    String[] dirs = {"up", "down", "left", "right"};
    
    for (int i = 0; i < numMoves; i++) {          // ✅ i=0
        int rand = (int)(Math.random() * 4);      // ✅ Math.random
        moveSequence += dirs[rand] + "_";
    }
}
```

---

### Q2: countOccurrences

**你的代码过于复杂，完全重写。**

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

**关键点：** 用临时变量temp和indexOf/substring组合，比逐字符比较简洁得多。

---

### Q3: LapTracker

**你的问题：**
- add_time没有重置，导致reset频率越来越慢
- return count应该是return lap_count

**正确写法：**
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
        if (numCalls == resetFrequency) {  // 到达重置点
            numCalls = 0;                   // ✅ 重置计数
            numLaps = 0;                    // ✅ 重置圈数
        }
        numCalls++;
        numLaps += additionalLaps;
        return numLaps;                      // ✅ 返回lap_count
    }
}
```

**你的reset逻辑漏洞：**
```
你的逻辑：add_time=3时重置，但add_time不会归零，继续4,5,6...
        下次重置在add_time=6，然后是9...（频率变成3,6,9...不是每3次）
正确逻辑：重置时numCalls=0，下次1,2,3再重置（保持每3次）
```

---

### Q4: playerWithClosestScore

**你的问题：**
- 拼写错误（gerScore, playList, Socre等）
- 过度复杂化（手动判断正负）
- place未初始化

**正确写法：**
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

**对比：** 你的代码30+行充满if-else，标准答案10行。简洁=更少错误。

---

### Q5: countOrderedRows

**你的问题：**
- 方法名拼写
- `grid[i][j]` 缺少 `.length()`
- `grid[0].length` 应该用 `grid[i].length`

**正确写法：**
```java
public int countOrderedRows() {
    int count = 0;
    
    for (int r = 0; r < grid.length; r++) {
        boolean ordered = true;
        
        for (int c = 0; c < grid[r].length - 1; c++) {  // ✅ grid[r].length
            if (grid[r][c].length() > grid[r][c + 1].length()) {  // ✅ 两边都有.length()
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

## ✅ 考试检查清单（必须逐项打勾）

### 写完后必查（5分钟）

**变量初始化：**
- [ ] 所有for循环变量都初始化了？`int i = 0`
- [ ] 所有局部变量都赋值了？`int x = 0;`

**拼写（对照题目复制）：**
- [ ] 方法名和题目完全一致？
- [ ] `getScore` 不是 `getSocre`/`gerScore`
- [ ] `playerList` 不是 `playList`
- [ ] return的变量名和声明一致？

**类型检查：**
- [ ] char比较用 `==`，不是 `.equals()`
- [ ] String比较用 `.equals()`，不是 `==`
- [ ] 比较的两个变量类型相同？（int和int比，String和String比）

**简化检查：**
- [ ] 有没有手动写绝对值判断？换成 `Math.abs()`
- [ ] 代码超过20行？想想能不能简化

---

## 🎯 你的提升路径（预估可到18-22分）

| 阶段 | 时间 | 任务 | 预期提升 |
|------|------|------|---------|
| 第1周 | 2天 | 消灭拼写：把Q4抄10遍，记住getScore/playerList | +3分 |
| 第1周 | 2天 | 消灭初始化错误：练习写10个正确的for循环 | +2分 |
| 第2周 | 3天 | 简化算法：所有"求差值比较"都用Math.abs模板 | +2分 |
| 第2周 | 2天 | 类型意识：char==、String.equals、两边.length() | +2分 |

**你的基础比Cai/Abigail/Xiping好，只是输在细节上。把这些细节焊死，分数能翻倍！**

---

## 🏆 核心建议

1. **慢下来**：你写得快但错得多，慢5分钟检查，多拿5分
2. **用标准答案的写法**：不要发明复杂解法，上面的标准答案背下来
3. **出声朗读**：写完后把方法名、变量名读一遍，发现拼写错误

---

> **诊断总结**：你是"会但写不对"型选手。算法思路基本正确，但**初始化、拼写、类型匹配**三大细节杀手在偷走你的分数。这三项是最好提分的，集中精力1周就能见效！
