import matplotlib.pyplot as plt

def draw_square(n):
    fig, ax = plt.subplots()
    
    for i in range(n):
        for j in range(n):
            ax.add_patch(plt.Rectangle((i, j), 1, 1, fill=None, edgecolor='black'))
    
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    ax.set_aspect('equal', adjustable='box')
    plt.xticks(range(n+1))
    plt.yticks(range(n+1))
    plt.grid(True)
    plt.show()

n = int(input("정사각형의 크기를 입력하세요: "))
draw_square(n)
