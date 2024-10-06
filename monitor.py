import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_ylim(0, 100)
ax.set_xlim(0, 100)
ax.set_title("Uso de CPU e Memória")
ax.set_xlabel("Tempo")
ax.set_ylabel("Uso (%)")
cpu_line, = ax.plot([], [], label="CPU", color="#FF5733")
mem_line, = ax.plot([], [], label="Memória", color="#C70039")

ax.legend()

cpu_text = ax.text(0.77, 0.7, "", transform=ax.transAxes)
mem_text = ax.text(0.77, 0.6, "", transform=ax.transAxes)


def update_chart(frame):

    cpu_percent = psutil.cpu_percent()
    print(f"Uso da CPU: {cpu_percent}%")

    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    print(f"Uso da memória: {memory.percent}%")

    disk_usage = psutil.disk_usage("/")
    print(f"Uso do disco: {disk_usage.percent}%")

    cpu_line.set_data(list(range(frame)), [cpu_percent]*frame)
    mem_line.set_data(list(range(frame)), [memory_percent]*frame)

    cpu_text.set_text(f"CPU: {cpu_percent:.1f}%")
    mem_text.set_text(f"Memória: {memory_percent:.1f}%")


    return cpu_line, mem_line, cpu_text, mem_text


animation = FuncAnimation(
    fig, update_chart, frames=100, interval=1000, blit=True)

for line in [cpu_line, mem_line]:
    line.set_linewidth(2)
    line.set_marker("o")
    line.set_markersize(5)

ax.set_facecolor("#F5F5F5")

plt.show()
