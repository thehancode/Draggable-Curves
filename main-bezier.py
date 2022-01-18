import matplotlib as mpl
import matplotlib.animation as animation
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Button, Slider

from bezier import calcular_bezier


N = 4
xmin = 1 
xmax = 9 
xvals = np.array([1.0,4.0,6.0,8.0])
yvals = np.array([5.0,2.0,7.0,2.0])

puntos = np.array([xvals , yvals]).T


parametros_t = np.linspace(0.0 ,1.0 , 100)
curva = calcular_bezier(parametros_t , puntos)

fig,axe = plt.subplots(1,1,figsize=(9.0,9.0),sharex=True)



pind = None
epsilon = 7

def update():
    global yvals
    global xvals

    global parametros_t

    plot_puntos_control.set_data(xvals ,yvals)
    puntos = np.array([xvals , yvals]).T
    curva = calcular_bezier(parametros_t , puntos)
    plot_curva.set_data(curva[0],curva[1])

    fig.canvas.draw_idle()


def button_press_callback(event):
    'whenever a mouse button is pressed'
    global pind
    if event.inaxes is None:
        return
    if event.button != 1:
        return
    pind = get_ind_under_point(event)    

def button_release_callback(event):
    'whenever a mouse button is released'
    global pind
    if event.button != 1:
        return
    pind = None

def get_ind_under_point(event):
    'get the index of the vertex under point if within epsilon tolerance'
    print('display x is: {0}; display y is: {1}'.format(event.x,event.y))
    t = axe.transData.inverted()
    tinv = axe.transData 
    xy = t.transform([event.x,event.y])
    print('data x is: {0}; data y is: {1}'.format(xy[0],xy[1]))
    
    xr = np.reshape(xvals,(np.shape(xvals)[0],1))
    yr = np.reshape(yvals,(np.shape(yvals)[0],1))
    xy_vals = np.append(xr,yr,1)
    xyt = tinv.transform(xy_vals)
    xt, yt = xyt[:, 0], xyt[:, 1]
    d = np.hypot(xt - event.x, yt - event.y)
    indseq, = np.nonzero(d == d.min())
    ind = indseq[0]

    print(d[ind])
    if d[ind] >= epsilon:
        ind = None
    
    print(ind)
    return ind

def motion_notify_callback(event):
    'on mouse movement'
    global yvals
    global yvals
    if pind is None:
        return
    if event.inaxes is None:
        return
    if event.button != 1:
        return
      
    yvals[pind] = event.ydata 
    xvals[pind] = event.xdata 

    fig.canvas.draw_idle()
    update()




X = np.arange(0,xmax+1,0.1)

plot_puntos_control, = axe.plot (xvals,yvals,color='k',linestyle='-',marker='o',markersize=8)
plot_curva, = axe.plot (curva[0], curva[1], 'r-', label='bezie')



axe.set_yscale('linear')
axe.set_xlabel('x')
axe.set_ylabel('y')
axe.grid(True)
axe.yaxis.grid(True,which='minor',linestyle='--')


fig.canvas.mpl_connect('button_press_event', button_press_callback)
fig.canvas.mpl_connect('button_release_event', button_release_callback)
fig.canvas.mpl_connect('motion_notify_event', motion_notify_callback)

plt.show()
