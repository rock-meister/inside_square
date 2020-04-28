import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# initial global value for b and c
b=15.0
c=5.0

def main():
    fig,ax=plt.subplots()
    fig.subplots_adjust(left=0.1, bottom=0.25)

    # draw the square x and y axes with the value of b
    def draw_axes(ax,b):
        ax.set_xlim([0,b])
        ax.set_ylim([0,b])
        ax.axes.set_aspect('equal')
    draw_axes(ax,b)

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
        axis_color='lightgoldenrodyellow'
        max_b=100.0
        slider_b_ax  = fig.add_axes([0.25, 0.15, 0.65, 0.03], facecolor=axis_color)
        slider_b = Slider(slider_b_ax, 'b value', 0, max_b, valinit=b, valfmt='%0.1f')
        slider_c_ax = fig.add_axes([0.25, 0.1, 0.65, 0.03], facecolor=axis_color)
        slider_c = Slider(slider_c_ax, 'c value', 0, b, valinit=c, valfmt='%0.1f')
    draw_sliders(b,c)

    plt.show()

if __name__ == '__main__':
  main() 