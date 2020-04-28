import matplotlib.pyplot as plt

# initial global value for b and c
b=15.0
c=5.0

def main():
    fig,ax=plt.subplots()
    def draw_axes(ax,b):
        ax.set_xlim([0,b])
        ax.set_ylim([0,b])
        ax.axes.set_aspect('equal')
    draw_axes(ax,b)
    plt.show()

if __name__ == '__main__':
  main() 