import matplotlib.pyplot as plt

def visualize_array_with_indices_indicator_height(n):
    block_size = 50  # 각 블록의 크기
    border_color = 'black'
    inner_color = 'white'
    text_color = 'black'

    total_width = n * block_size
    total_height = block_size

    array_image = plt.figure(figsize=(10, 2))  # 그림의 크기를 조정합니다.
    ax = array_image.add_subplot(111)
    ax.set_xlim(0, total_width)
    ax.set_ylim(0, total_height)

    for i in range(n):
        # 블록의 좌표와 크기 계산
        x = i * block_size
        y = 0
        width = block_size
        height = block_size

        # 블록의 테두리 그리기
        ax.add_patch(plt.Rectangle((x, y), width, height, color=border_color))

        # 블록 내부 색칠
        inner_x = x + 1
        inner_y = y + 1
        inner_width = width - 2
        inner_height = height - 2
        ax.add_patch(plt.Rectangle((inner_x, inner_y), inner_width, inner_height, color=inner_color))

        # 블록 상단에 인덱스 표시
        index_text = str(i)
        ax.text(x + width / 2, y + height - 5, index_text, color=text_color,
                fontsize=10, ha='center', va='top')

    # "i" 지표 추가
    i_indicator_y = total_height - 10
    ax.text(-10, i_indicator_y, "i", color=text_color,
            fontsize=10, ha='center', va='center')

    ax.set_aspect('equal')
    ax.axis('off')  # 축 제거
    plt.show()

# 블록의 개수를 입력하세요
num_blocks = int(input("블록의 개수를 입력하세요: "))
visualize_array_with_indices_indicator_height(num_blocks)
