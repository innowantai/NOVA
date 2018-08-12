


def calc_similar(li, ri):
    return hist_similar(li.histogram(), ri.histogram())

        
m1 = PIL.Image.open(os.path.join(saveTestFigure,fileName + '_' + str(24) + '.jpg')) 
m2 = PIL.Image.open(os.path.join(saveTestFigure,fileName + '_' + str(25) + '.jpg')) 
    
    
# =============================================================================
# cooo2 = calc_similar(m1,m2)
#     
# m1 = np.array(m1).flatten()
# m2 = np.array(m2).flatten()     
# cooo = np.corrcoef(m1,m2)[0][1]    
#     
# =============================================================================
    

m3 = np.array(m2)
po = np.where(m3 >= (80,80,80))
m4 = m3[po]
m5 = np.array(m1)[po]

mm1 = np.array(m1).flatten()
mm2 = np.array(m2).flatten()

mm3 = np.array(m1.convert("L"))
image, con, hierarchy = cv2.findContours(mm3.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
x,y,w,h = cv2.boundingRect(con[1])

car_contour1 = cv2.drawContours(mm3, con, -1, (0,255,0), 3)

plt.imshow(mm3)



