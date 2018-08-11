(defun c:dd()

  (setq oriP (getpoint "Enter the point : \n")) 


  (setq H1 473)
  (setq W1 437)
  (setq W2 21)
  (setq C1 26.6667)
  (setq S1 6.67)
  (setq S2 5)
  (setq sy (- y S2 )) 
  (setq H (- H1 (* 2 s2)))

  (setq p1 (polar oriP (- 0 (/ PI 2)) S2))
  (setq p2 (polar p1 (- 0 (/ PI 2)) H))
  (setq p3 (polar p2 0 S1))
  (setq p4 (polar p2 0 W2))
  
  (setq p5 (polar p1 0 W1))
  (setq p6 (polar p2 0 W1))
  (setq p7 (polar p3 0 W1))
  (setq p8 (polar p4 0 W1))
  
  (setq pc1 (polar oriP 0 (/ W2 2)))
  (setq pc2 (polar pc1 (- 0 (/ PI 2)) H1))
  (setq pc3 (polar pc1 0 W1))
  (setq pc4 (polar pc2 0 W1))
  
  (setq pc5 (polar oriP 0 C1))
  (setq pc6 (polar pc4 (- 0 PI) C1))

  (setq interP1 (inters pc5 pc6 p1 p5))
  (setq interP2 (inters pc5 pc6 p2 p7))
  (setq shp1R (polar interP1 0 (/ W2 2)))
  (setq shp1L (polar interP1 PI (/ W2 2)))
  (setq shp2R (polar interP2 0 (/ W2 2)))
  (setq shp2L (polar interP2 PI (/ W2 2)))
  
  
  (command "rectang" p1 p3 )
  (command "rectang" p1 p4 )
  (command "rectang" p5 p7 )
  (command "rectang" p5 p8 )

  (command "line" pc1 pc2 "")
  (command "line" pc3 pc4 "")
  (command "line" interP1 interP2 "")
  (command "line" shp1R shp2R "")
 
  
  ;(command "rectang" (list 0 0) (list 100 100)) 
  ;(command "-array" "L" "" "R" 3 5 100 100)


)



(defun c:ss()  
  
  (setq oriPoint (getpoint "Enter the point : "))
  (setq x (car oriPoint))
  (setq y (car (cdr oriPoint)))
  (setq ww (getreal "Input width : "))
  (setq hh (getreal "Input height : "))

  (setq p1 (list x y))
  (setq p2 (list (+ x ww) y))
  (setq p3 (list (+ x ww) (+ y hh)))
  (setq p4 (list x (+ y hh)))

  (command "line" p1 p2 p3 p4 p1 "")  
  
  ;(command "line" (list x y) (list (+ x ww) y) (list (+ x ww) (+ y hh)) (list x (+ y hh)) (list x y)   "")  
)







(defun c:re(/)
  (setq oriPoint (getpoint "Enter the point : "))
  (setq x (car oriPoint))
  (setq y (car (cdr oriPoint)))
  ;(setq w1 (getreal "w1")) 
  (setq H1 473)
  (setq W1 437)
  (setq W2 21)
  (setq C1 26.6667)
  (setq S1 6.67)
  (setq S2 5)
  (setq sy (- y S2 )) 
  (setq H (- H1 (* 2 s2)))


  ;(plotRec x y S1 H)  
  
  (command "rectang" (list x sy) (list (+ x S1) (- sy H)) "rectang" (list x sy) (list (+ x w2) (- sy H)))
  (command "rectang" (list x sy) (list (+ x w2) (- sy H)))  
  (command "rectang" (list (+ x W1) sy) (list (+ (+ x W1) s1) (- sy H)) "")  
  (command "rectang" (list (+ x W1) sy) (list (+ (+ x W1) w2) (- sy H)) "")
  
  ; (x + W2/2,y) (x + W2/2,y-H1)
  (command "line" (list (+ x (/ W2 2)) y) (list (+ x (/ W2 2)) (- y H1)) "")
  
  ; (x + W2/2 + W1 ,y) (x + W2/2 + W1,y-H1)
  (command "line" (list (+ x (+ (/ W2 2) W1)) y) (list (+ x (+ (/ W2 2) W1)) (- y H1)) "")


  
) 




(defun plotRec (xx yy ww hh) 
  
  (setq p1 (list xx yy))
  (setq p2 (list (+ xx ww) yy))
  (setq p3 (list (+ xx ww) (+ yy hh)))
  (setq p4 (list xx (+ yy hh)))
 
  (command "line" p1 p2  "" )  
  (command "line" p2 p3  "" )  
  (command "line" p3 p4  "" ) 
  (command "line" p4 p1  "" )  
)
 


(defun c:rr()

  ;(load "D:\\Users\\95074\\Desktop\\NOVA UseCode\\Code\\0_AutoLisp\\Lisp\\test.LSP")
  (load "C:\\Users\\Wantai\\Desktop\\NOVA UseCode\\Code\\0_AutoLisp\\Lisp\\test.LSP")
  (print "File Load Done !")

)