import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
#matplotlib.widgets - 旨在为任何GUI后端工作的小工具。
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #GUI元件
window=tk.Tk()
fig=plt.Figure() #指定繪製元件(畫布)
# fig = plt.figure () 作用就是生成一个图框，但是这个图框还不能用来画图，画图需要在子图 (subplot)或者轴域 (Axes)中作图
canvas=FigureCanvasTkAgg(fig,window)#指定要畫在fig上，然後放到window 中
#FigureCanvasXAgg就是一个渲染器，渲染器的工作就是drawing，执行绘图的这个动作。渲染器是使物体显示在屏幕上
canvas.get_tk_widget().pack() #get_tk_widget()要加框框，不然是指物件
ax=fig.add_subplot(1,1,1) #在畫布上指定位置
fig.subplots_adjust(bottom=0.25) #加空白位置
x=[5,6,7,8]
ax.plot(x,x)
ax.axis([0,10,0,10])
ax_time=fig.add_axes([0.12,0.1,0.78,0.03])
#fig.add_axes ()在图表的任意位置添加子图，该方法接收一个包含4个数字的列表: $ [x, y, width, height]$
slider1=Slider(ax_time,'Time',0,30,valinit=0)
def update(val):
    pos=val #取得滑桿數值
    ax.axis([pos,pos+10,0,10])
    fig.canvas.draw_idle()#更新畫面
    #draw_idle ():延迟绘制，如果draw_idle ()在函数中，会等到函数执行完，程序进行到GUI主循环再进行绘制。
slider1.on_changed(update) #設定觸發事件
tk.mainloop()