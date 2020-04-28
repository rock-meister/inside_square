import matplotlib.pyplot as plt

# initial global value for b and c
b=15.0
c=5.0

def main():
    fig,ax=plt.subplots()
    axis_color = 'lightgoldenrodyellow'
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
        return
    draw_lines(b,c)

    plt.show()

if __name__ == '__main__':
  main() 