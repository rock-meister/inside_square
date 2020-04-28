import matplotlib as matplotlib
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# initial global value for b and c
b=15.0
c=5.0
slider_b=0
slider_c=0

def main():
    fig,ax=plt.subplots()
    fig.subplots_adjust(left=0.1, bottom=0.25)

    # draw the square x and y axes with the value of b
    def draw_axes(b):
        ax.set_xlim([0,b])
        ax.set_ylim([0,b])
        ax.axes.set_aspect('equal')
    draw_axes(b)

    # draw 4 lines and mark(tick) the x and y axis
    def draw_lines(b,c):
        ax.axes.get_xaxis().set_ticks([c,b])
        ax.axes.get_yaxis().set_ticks([b-c,b])
        plt.axis([0, b, 0, b])
        ax.plot([0,b], [0,c], color='black')
        ax.plot([0,c], [b,0], color='black')
        ax.plot([0,b], [b-c,b], color='black')
        ax.plot([b-c,b], [b,0], color='black')
    draw_lines(b,c)

    # draw slider b and c and set them to values b and c respectively
    def draw_sliders(b,c):
        global slider_b, slider_c
        axis_color='lightgoldenrodyellow'
        max_b=100.0
        slider_b_ax  = fig.add_axes([0.25, 0.15, 0.65, 0.03], facecolor=axis_color)
        slider_b = Slider(slider_b_ax, 'b value', 0, max_b, valinit=b, valfmt='%0.1f')
        slider_c_ax = fig.add_axes([0.25, 0.1, 0.65, 0.03], facecolor=axis_color)
        slider_c = Slider(slider_c_ax, 'c value', 0, b, valinit=c, valfmt='%0.1f')
    draw_sliders(b,c)

    # create a text for to show the current arre for a given b,c
    axLabel = plt.axes([0.25, 0.02, 0.4, 0.05])
    textbox = matplotlib.widgets.TextBox(axLabel, 'Area: ')
    def area(b,c):
            return ((b*b)-((2*b*b*b*c)/(b*b+c*c)))
    textbox.set_val(format("{:.1f}".format(area(b,c))))

    def sliders_b_changed(val):
        global b,c
        global slider_b, slider_c
        b=val
        # round b to increments of .1
        b=round(b,1)
        #line.set_ydata(signal(amp_slider.val, freq_slider.val))
        #HACK remove the 4 lines that we just drew
        for i in [0,1,2,3]:
            ax.lines.pop(0)
        # set max value of slider_c to the b value
        slider_c.valmax=b
        slider_c.ax.set_xlim(slider_c.valmin, slider_c.valmax)

        # TODO: handle scenario where the new b value is less then the current c value
        if (c>b):
            c=b/2
        slider_c.val=c
        draw_axes(b)
        draw_lines(b,c)
        textbox.set_val(format("{:.1f}".format(area(b,c))))
        fig.canvas.draw_idle()
    
    def sliders_c_changed(val):
        global b,c
        c=val
        c=round(c,1)
        #HACK remove the 4 lines that we just drew
        for i in [0,1,2,3]:
            ax.lines.pop(0)
        draw_lines(b,c)
        textbox.set_val(format("{:.1f}".format(area(b,c))))
        fig.canvas.draw_idle()
    
    slider_b.on_changed(sliders_b_changed)
    slider_c.on_changed(sliders_c_changed)
    plt.show()

if __name__ == '__main__':
  main() 