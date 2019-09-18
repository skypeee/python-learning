# 排序算法

- 按时间复杂度划分
  - 时间复杂度为O(n²)的排序算法
    - 冒泡排序
    - 选择排序
    - 插入排序
    - 希尔排序（性能略优于O(n²)，但又比不上O(n log n)）
  - 时间复杂度为O(n log n)的排序算法
    - 快速排序
    - 归并排序
    - 堆排序
  - 时间复杂度为线性的排序算法
    - 计数排序
    - 桶排序
    - 基数排序
- 按稳定性划分
  - 稳定排序
    - 冒泡排序
  - 不稳定排序

## 冒泡排序

### 思路

- 把相邻的元素两两比较

  ![bubbleSort](https://raw.githubusercontent.com/skypeee/python-learning/master/排序算法/image/bubbleSort.png)

- 当一个元素大于右侧相邻元素时，交换他们的位置

- 当元素小于等于右侧相邻元素时，位置不变

  ![冒泡排序第一趟](https://raw.githubusercontent.com/skypeee/python-learning/master/排序算法/image/冒泡排序第一趟.png)

  ![冒泡排序第二趟](https://raw.githubusercontent.com/skypeee/python-learning/master/排序算法/image/冒泡排序第二趟.png)

### 时间复杂度为O(n²)

### 优化

- 第一版
  - 当进行过若干次排序后已经成为有序数列，但是还是会继续进行直到最后一次循环
  
  - 我们可以做一个标记，当数列已经有序列则后面循环不必执行
  
    ![冒泡排序第一次优化1](https://raw.githubusercontent.com/skypeee/python-learning/master/排序算法/image/冒泡排序第一次优化.png)
- 第二版
  - 如果列表后半部分已经是有序的，那么在每一轮还是会一次进行对比
  
  - 在每一轮排序后记录下最后一次元素交换的位置
  
  - 该位置即为无序列表的边界，再往后就是有序区
  
    ![冒泡排序第二次优化1](https://raw.githubusercontent.com/skypeee/python-learning/master/排序算法/image/冒泡排序第二次优化1.png)
  
    ![冒泡排序第一次优化2](https://raw.githubusercontent.com/skypeee/python-learning/master/排序算法/image/冒泡排序第二次优化2.png)
  
    ![冒泡排序第二次优化3](https://raw.githubusercontent.com/skypeee/python-learning/master/排序算法/image/冒泡排序第二次优化3.png)
- 鸡尾酒排序
  - 元素比较和交换是双向的
  - 第一躺从左到右、第二趟从右到左
  - 能在特定的条件下减少排序回合数
  - 代码量多
  - 大部分元素有序的情况下合适

![冒泡排序第二次优化3](https://raw.githubusercontent.com/skypeee/python-learning/master/排序算法/image/鸡尾酒排序.png)

## 快速排序

### 思路

- 分治法
- 每一轮挑选一个基准元素
- 比他大的元素移动到数列的一边
- 比他小的元素移动到数列的另一边

### 基准元素的选择

- 最简单的方法就是选择数列的第一个元素（效率可能会不高）
- 随机选择基准元素并且和数列的首元素交换位置

### 元素的交换

#### 双边循环法

- 选择基准元素pivot并设置两个指针left和right指向最左和最右两个元素
- 第一次循环从右开始，如果大于或等于pivot，则指针向左移动；如果小于pivot，则right指针停止移动，切换到left指针。
- left和right指针元素切换，指针left行动，如果指针所指向元素小于或等于基准元素，则指针向右移动；如果大于基准元素，left指针停止移动，此时让left与right指向的元素交换
- 当第二次循环重新切入right寻找
- 当left与right碰头时停止，将基准元素插入中间

![快速排序双边循环1](https://raw.githubusercontent.com/skypeee/python-learning/master/排序算法/image/quickSort3.png)

![快速排序双边循环2](https://raw.githubusercontent.com/skypeee/python-learning/master/排序算法/image/quickSort4.png)

#### 单边循环法

- 需要一个mark指针指向起始位置，代表小于基准元素的边界
- 如果找到大于基准元素的值，继续往后遍历
- 如果找到小于基准元素的值，则将mark指针后移一位，并将该元素与mark指向的值替换
- 循环结束后将基准元素插入到mark元素与基准元素交换

![快速排序单边循环1](https://raw.githubusercontent.com/skypeee/python-learning/master/排序算法/image/quickSort1.png)

![快速排序单边循环2](https://raw.githubusercontent.com/skypeee/python-learning/master/排序算法/image/quickSort2.png)

#### 非递归实现

- 可以将原本的递归实现转化成一个栈的实现

## 堆排序

- 空间复杂度是O(1)
- 二叉堆的节点“下沉”调整时堆排序算法的基础，时间复杂度时O(log n)

### 思路

- 把无序数组构建成二叉树（从小到大则构成最大堆，从大到小则构成最小堆）
- 循环删除堆顶元素，替换到二叉树的末尾，调整产生新的堆顶

### 堆排序和快速排序比较

- 堆排序和快速排序的平均时间复杂度都是O(n log n)
- 都是不稳定排序
- 快速排序最坏时间复杂度是O(n²)
- 堆排序的最坏时间复杂度稳定在O(n log n)
- 快速排序递归和非递归方法的平均空间复杂度是O(log n)
- 堆排序的空间复杂度是O(1)

## 计数排序

- 之前的冒泡排序、快速排序都是基于元素之间的比较来进行排序的

### 思路

- 取值范围为0~10之间的一组数据，进行快速地对数据排序![countSort1](https://raw.githubusercontent.com/skypeee/python-learning/master/排序算法/image/countSort.png)
- 创建一个长度为数据最大值加一（11）的数组，值全为0![countSort2](https://raw.githubusercontent.com/skypeee/python-learning/master/排序算法/image/countSort2.png)
- 将数据与数组下标对应，将值加一，统计出来的数组即为![countSort3](https://raw.githubusercontent.com/skypeee/python-learning/master/排序算法/image/countSort3.png)
- 遍历数组，值为几就等同于此下标对应的数据出现过几次![countSort4](https://raw.githubusercontent.com/skypeee/python-learning/master/排序算法/image/countSort4.png)

### 优化

- 如果数列的最大值为99，最小值为90，那么开辟一个长度为100的数组造成空间浪费![countSort1](https://raw.githubusercontent.com/skypeee/python-learning/master/排序算法/image/countSort5.png)

- 以数列最大值-数列最小值+1最为数组的长度![countSort1](https://raw.githubusercontent.com/skypeee/python-learning/master/排序算法/image/countSort6.png)

- 对应下标为数据-最小值

  ![countSort1](https://raw.githubusercontent.com/skypeee/python-learning/master/排序算法/image/countSort7.png)

  ![countSort1](https://raw.githubusercontent.com/skypeee/python-learning/master/排序算法/image/countSort8.png)

#### 数据不为数字

- 如果存储的数据是一个成绩表，张三：96分这样的数据的话，之前的需求就不满足要求
- 可以将开辟的数组进行变形，每个位置存储的都是每一个元素加上之前所有的元素之和
- 从后向前遍历数组，重新放进原数组
- 当前位置有数据就向前一位

### 缺点

- 当数列最大值与最小值差距过大时，不适合计数排序
- 当数列元素不是整数是，不适合计数排序

## 桶排序

- 桶排序的总体时间复杂度为O(n)
- 如果元素分布极端不均匀，时间复杂度退化为O(n log n)

### 思路

- 所谓的桶，就是每一个桶代表一个区间，里面可以放多个数据

- 区间跨度 = （最大值-最小值） / （桶的数量 - 1）  

- 桶的数量可以是数据的个数（可以自定义）

- 遍历数组，将数据对应放进桶中

- 对每个桶内进行排序

- 遍历所有的桶，依次输出元素

![桶排序](https://raw.githubusercontent.com/skypeee/python-learning/master/排序算法/image/桶排序.png)