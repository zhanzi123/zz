from random import randint
import pygal
class Die():
    """表示一个骰子的类"""
    def __init__(self,num_sides=6):
        """骰子默认为6面"""
        self.num_sides = num_sides

    def roll(self):
        """返沪一个位于1和骰子面数之间的随机值"""
        return randint(1,self.num_sides)

# die = Die()
# # 掷色子并将结果存在一个列表中
# results = []
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)
#
# # 分析结果
# frequencies = []
# for value in range(1,die.num_sides + 1):
#     frequency = results.count(value)
#     frequencies.append(frequency)
#
# # 对结果进行可视化
# hist = pygal.Bar()
#
# hist.title = "results of rolling one D6 1000 times"
# hist.x_labels = [1,2,3,4,5,6]
# hist.x_title = "result"
# hist.y_title = "frequency of result"
#
# hist.add('D6',frequencies)
# hist.render_to_file('die_visual.svg')
"""为创建条形图，我们创建了一个pygal.Bar() 实例，并将其存储在hist 中（见❶）。
接下来，我们设置hist 的属性title （用于标示直方图的字符串），将掷D6骰子的可 能结果用作 x 轴的标签（见❷），并给每个轴都添加了标题。
在❸处，我们使用add() 将一系列值添加到图表中（向它传递要给添加的值指定的标签，还有一个列表，其中包含 将出现在图表中的值）。
最后，我们将这个图表渲染为一个SVG文件，这种文件的扩展名必须为.svg。"""

"""同时投掷两个骰子"""
die_1 = Die()
die_2 = Die(10)
# 掷色子多次并将结果储存在一个列表中
results = []
for roll_num in range(5000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
# 分析结果
frenquencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2,max_result):
    frenquency = results.count(value)
    frenquencies.append(frenquency)
# 可视化结果
hist = pygal.Bar()
hist.title = "投掷2个6面骰子1000次"
hist.x_labels = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
hist.x_title = "点数"
hist.y_title = "次数"

hist.add("次",frenquencies)
hist.render_to_file("柱状图.svg")