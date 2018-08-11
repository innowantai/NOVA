(defun c:ss()
  
  
  (setq oriPoint (getpoint "Enter the point : "))
  (setq x (car oriPoint))
  (setq y (car (cdr oriPoint)))
  (setq ww (getreal "Input width : "))
  (setq hh (getreal "Input height : "))
  
  (command "line" (list x y) (list (+ x ww) y) (list (+ x ww) (+ y hh)) (list x (+ y hh)) (list x y)   "")  
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