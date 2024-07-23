import matplotlib.pyplot as plt

# Function to perform C-LOOK on the request array starting from the given head
def CLOOK(arr, head):
    size = len(arr)
    seek_count = 0
    distance = 0
    cur_track = 0

    left = []
    right = []

    seek_sequence = []

    # Tracks on the left of the head will be serviced when
    # once the head comes back to the beginning (left end)
    for i in range(size):
        if arr[i] < head:
            left.append(arr[i])
        if arr[i] > head:
            right.append(arr[i])

    # Sorting left and right vectors
    left.sort()
    right.sort()

    # First service the requests on the right side of the head
    for i in range(len(right)):
        cur_track = right[i]

        # Appending current track to seek sequence
        seek_sequence.append(cur_track)

        # Calculate absolute distance
        distance = abs(cur_track - head)

        # Increase the total count
        seek_count += distance

        # Accessed track is now the new head
        head = cur_track

    # Once reached the right end jump to the last track that
    # is needed to be serviced in left direction
    if len(left) > 0:
        seek_count += abs(head - left[0])
        head = left[0]

        # Now service the requests again which are left
        for i in range(len(left)):
            cur_track = left[i]

            # Appending current track to seek sequence
            seek_sequence.append(cur_track)

            # Calculate absolute distance
            distance = abs(cur_track - head)

            # Increase the total count
            seek_count += distance

            # Accessed track is now the new head
            head = cur_track

    print("Total number of seek operations =", seek_count)
    print("Seek Sequence is")
    for track in seek_sequence:
        print(track)

    # Plotting the Gantt Chart
    plot_gantt_chart(seek_sequence, initial_head, seek_count)

def plot_gantt_chart(seek_sequence, initial_head, total_seek_operations):
    fig, ax = plt.subplots()
    y = list(range(len(seek_sequence) + 1))
    x = [initial_head] + seek_sequence
    distances = []

    for i in range(len(x) - 1):
        distance = abs(x[i + 1] - x[i])
        distances.append(distance)
        # Plot points
        ax.plot(x[i], y[i], marker='o', color='b')
        ax.plot(x[i + 1], y[i + 1], marker='o', color='b')
        # Add arrow to indicate direction
        ax.annotate('', xy=(x[i + 1], y[i + 1]), xytext=(x[i], y[i]),
                    arrowprops=dict(arrowstyle="->", color='r'))
        # Annotate distance in the middle
        mid_x = (x[i] + x[i + 1]) / 2
        mid_y = (y[i] + y[i + 1]) / 2
        ax.annotate(f'{distance}', (mid_x, mid_y), textcoords="offset points", xytext=(0, 10), ha='center')

    # Annotate track numbers
    for i, txt in enumerate(x):
        ax.annotate(txt, (x[i], y[i]), textcoords="offset points", xytext=(0, 10), ha='center')

    # Total seek operations annotation
    ax.annotate(f'Total seek operations: {total_seek_operations}', 
                xy=(0.5, 1.1), xycoords='axes fraction', ha='center', fontsize=12, color='black')

    plt.title("Disk Scheduling - C-LOOK Algorithm")
    plt.xlabel("Track Number")
    plt.ylabel("Sequence")
    plt.gca().invert_yaxis()  # Invert y-axis to show downward direction
    plt.grid(True)
    plt.show()

# Driver code
if __name__ == "__main__":
    # Input the variables manually
    disk_size = int(input("Enter the disk size: "))
    head = int(input("Enter the initial position of the head: "))
    arr = list(map(int, input("Enter the request array separated by space: ").split()))

    print("Initial position of head:", head)
    initial_head = head
    CLOOK(arr, head)
