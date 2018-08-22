from matplotlib.patches import Circle
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredDrawingArea
import time
import random

print("LEFT        BACK-LEFT      BACK-RIGHT        RIGHT")


def radius(dbm):
    #return((random.randint(20,70)*5 ))
    return((-1 * int(dbm) - 25)*20)

def draw_circles():
    for ip in logfile:
      if ip[-1] == '2': 
        left_dbm = logfile[ip]['a8:96:75:c3:58:0d'][-1][1]
      elif ip[-1] == '5': 
        #print(dbm, " came from erick")
        right_dbm = logfile[ip]['a8:96:75:c3:58:0d'][-1][1]
      elif ip[-1] == '4': 
        #print(dbm, " came from justin")
        back_left_dbm = logfile[ip]['a8:96:75:c3:58:0d'][-1][1]
      elif ip[-1] == '3': 
        #print(dbm, " came from aaron")
        back_right_dbm = logfile[ip]['a8:96:75:c3:58:0d'][-1][1]
        #back_right_dbm =  logfile['172.24.1.90']['a8:96:75:c3:58:0d'][-1][1]
    print('{0}         {1}            {2}               {3}'.format(left_dbm, back_left_dbm, back_right_dbm, right_dbm), end='\r')
    
    fig, ax = plt.subplots(figsize=(10, 10))

    ada = AnchoredDrawingArea(10, 10, 0, 0,loc=1, pad=0., frameon=False)

    left_circle = Circle((-550,-540), radius(left_dbm), fc="none", ec='g')
    ada.drawing_area.add_artist(left_circle)
    
    back_left_circle = Circle((-550, 20), radius(back_left_dbm), fc="none", ec='r')
    ada.drawing_area.add_artist(back_left_circle)

    back_right_circle = Circle((20, 20), radius(back_right_dbm), fc="none", ec="b")
    ada.drawing_area.add_artist(back_right_circle)

    right_circle = Circle((20,-540), radius(right_dbm), fc="none", ec='k')
    ada.drawing_area.add_artist(right_circle)

    ax.add_artist(ada)
    plt.show()
    time.sleep(2)
    fig.clf()


draw_circles()
