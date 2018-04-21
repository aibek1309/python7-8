import matplotlib.pyplot as plt
def put_syms(xs, ys, sym):
    to_draw_x = [x for x in xs]
    to_draw_y = [y for y in ys]
    ax.scatter(to_draw_x, to_draw_y, s=1500, marker=sym)

fig = plt.figure(figsize=(10, 10)) #делает график размера 10х10
ax = fig.add_subplot(1, 1, 1)

ax.set_facecolor("indigo")
coord_ticks = list(range(11))
grid_ticks = [t + 0.5 for t in coord_ticks]

ax.set_xticks(coord_ticks)
ax.set_xticks(grid_ticks, minor=True)
ax.set_yticks(coord_ticks)
ax.set_yticks(grid_ticks, minor=True)

ax.set_xlim([0.5, 10.5])
ax.set_ylim([0.5, 10.5])
ax.grid(which='minor', color="green")
put_syms([1, 3], [2, 4], 'x')
put_syms([1, 2], [1, 2], 'o')
plt.show()
