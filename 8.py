import matplotlib.pyplot as pyplot
import matplotlib.ticker as ticker
import numpy


with open('settings.txt') as file:
     settings = numpy.array([float(i) for i in file.read().split('\n')])

data=numpy.loadtxt('data.txt', dtype=int) * settings[1]
data_time=numpy.array([i*1/settings[0] for i in range(data.size)])

fig, ax=pyplot.subplots(figsize=(14, 7))

ax.axis([data.min(), data_time.max()+1, data.min(), data.max()+0.2])
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.set_title('Процесс заряда и разряда конденсатора в RC цепи')
ax.grid(which='major', color = 'k')
ax.minorticks_on()
ax.grid(which='minor', color = 'blue', linestyle = ':')
ax.set_ylabel("Напряжение, В")
ax.set_xlabel("Время, с")
ax.plot(data_time, data, c='black', linewidth=1, label = 'V(t)')
ax.scatter(data_time[0:data.size:100], data[0:data.size:100], marker = 's', c = 'green', s=10)
ax.legend(shadow = False, loc = 'right', fontsize = 30)


fig.savefig('graphic.png')
fig.savefig('graphic.svg')

pyplot.show()