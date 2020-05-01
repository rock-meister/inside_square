import matplotlib as matplotlib
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib import patches
class square_inside_square:   
    # declare variable b, c and area
    #TODO: Check if this is the right way to define and initilaize instance variables
    _b,_c,_area=[None, None, None]
  
    # init method or constructor
    def __init__(self, b, c):   
        self._b = b
        self._c = c
        self.calculate()
    def calculate(self):
        b=self._b
        c=self._c
        self._area = ((b*b)-((2*b*b*b*c)/(b*b+c*c)))

slider_b=None
slider_c=None
# Initial values for b and c
bnc = square_inside_square(15.0, 5.0)

def main():
    fig,ax=plt.subplots()
    fig.subplots_adjust(left=0.1, bottom=0.25)
    print(bnc._b)
    print(bnc._c)
    print(bnc._area)

    # draw the square x and y axes with the value of b
    def draw_axes(b):
        ax.set_xlim([0,b])
        ax.set_ylim([0,b])
        ax.axes.set_aspect('equal')
    draw_axes(bnc._b)

    # draw 4 lines and mark(tick) the x and y axis
    def draw_lines(b,c):
        ax.axes.get_xaxis().set_ticks([c,b])
        ax.axes.get_yaxis().set_ticks([b-c,b])
        plt.axis([0, b, 0, b])
        ax.plot([0,b], [0,c], color='black')
        ax.plot([0,c], [b,0], color='black')
        ax.plot([0,b], [b-c,b], color='black')
        ax.plot([b-c,b], [b,0], color='black')
    draw_lines(bnc._b,bnc._c)

    # draw slider b and c and set them to values b and c respectively
    def draw_sliders(b,c):
        global slider_b, slider_c
        axis_color='lightgoldenrodyellow'
        max_b=100.0
        slider_b_ax  = fig.add_axes([0.25, 0.15, 0.65, 0.03], facecolor=axis_color)
        slider_b = Slider(slider_b_ax, 'b value', 0, max_b, valinit=b, valfmt='%0.1f')
        slider_c_ax = fig.add_axes([0.25, 0.1, 0.65, 0.03], facecolor=axis_color)
        slider_c = Slider(slider_c_ax, 'c value', 0, b, valinit=c, valfmt='%0.1f')
    draw_sliders(bnc._b,bnc._c)

    # create a text for to show the current arre for a given b,c
    axLabel = plt.axes([0.25, 0.02, 0.4, 0.05])
    textbox = matplotlib.widgets.TextBox(axLabel, 'Area: ')
    textbox.set_val(format("{:.1f}".format(bnc._area)))

    # remove all the lines TODO: Is this the right way to remove lines?
    def remove_lines():
        num_of_lines=len(ax.lines)
        while(num_of_lines>0):
            ax.lines.pop(num_of_lines-1)
            num_of_lines-=1


    def sliders_b_changed(val):
        global bnc
        global slider_b, slider_c
        # round b to increments of .1
        bnc._b=round(val,1)
        bnc.calculate()
        remove_lines()
        # set max value of slider_c to the b value
        slider_c.valmax=bnc._b
        slider_c.ax.set_xlim(slider_c.valmin, slider_c.valmax)

        # TODO: handle scenario where the new b value is less then the current c value
        if (bnc._c>bnc._b):
            bnc._c=bnc._b/2
        slider_c.val=bnc._c
        draw_axes(bnc._b)
        draw_lines(bnc._b,bnc._c)
        textbox.set_val(format("{:.1f}".format(bnc._area)))
        fig.canvas.draw_idle()
    
    def sliders_c_changed(val):
        global bnc
        bnc._c=round(val,1)
        bnc.calculate()
        remove_lines()
        draw_lines(bnc._b,bnc._c)
        textbox.set_val(format("{:.1f}".format(bnc._area)))
        fig.canvas.draw_idle()
    
    slider_b.on_changed(sliders_b_changed)
    slider_c.on_changed(sliders_c_changed)

    # Create a Rectangle patch
    #rect = patches.Rectangle((0,0),b/2,b/2,linewidth=1,edgecolor='r',facecolor='blue')
    # Add the patch to the Axes
    #ax.add_patch(rect)
    plt.show()

if __name__ == '__main__':
  main() 