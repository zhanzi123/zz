# from matplotlib import pyplot as plt
# input_values = [1,2,3,4,5]
# squares = [1,4,9,16,25]
# # 设置x、y坐标和折线宽度
# plt.plot(input_values,squares,linewidth=5)
# # 设置图表标题，并给坐标轴加上标签
# plt.title("Squares Numbers",fontsize=24)
# plt.xlabel("Value",fontsize=14)
# plt.ylabel("Suare of Value",fontsize=14)
# # 设置刻度标记的大小
# plt.tick_params(axis='both',labelsize=14)
# # 展示图表
# plt.show()

# import matplotlib.pyplot as plt
# # 绘制单个点
# # plt.scatter(2,4,s=200)
# # 绘制一系列点
# # x_values = [1,2,3,4,5]
# # y_values = [1,4,9,16,25]
# x_values = list(range(1,1001))
# y_values = [x**2 for x in x_values]
# # edgecolor='none'表示删除数据点轮廓
# plt.scatter(x_values,y_values,edgecolor='none',s=40)
# # 可以自定义数据点颜色，可使用英文也以使用RGB颜色模式
# # plt.scatter(x_values,y_values,c='yellow',edgecolor='none',s=40)
# # plt.scatter(x_values,y_values,c=(0.1,0.5,0.2),edgecolor='none',s=40)
# # 使用颜色映射,将参数c设置成一个y值列表，根据y值大小决定颜色深浅
# plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=40)
# # 设置图表标题并给坐标轴加上标签
# plt.title("Squares Numbers",fontsize=24)
# plt.xlabel("Value",fontsize=14)
# plt.ylabel("Square of Value",fontsize=14)
# # 设置刻度标记的大小
# plt.tick_params(axis='both',which='major',labelsize=14)
# # 如果要将图表保存到文件中，可将plt.show()替换成plt.savefig()
# # plt.show()
# plt.savefig('suqares_plot.png',bbox_inches='tight')

import matplotlib.pyplot as plt
# x_values = list(range(0,5))
# x_values = [1,2,3,4,5]
# y_values = [1,8,27,64,125]
x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=40)
plt.title("Squares Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)
plt.show()