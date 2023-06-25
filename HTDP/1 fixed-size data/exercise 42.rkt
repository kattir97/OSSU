;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname |exercise 42|) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp")) #f)))
(require 2htdp/universe)

; physical constants
(define WIDTH-OF-WORLD 200)
 
(define WHEEL-RADIUS 10) ; single point of control
(define WHEEL-DISTANCE (* WHEEL-RADIUS 2))
(define ROAD-LENGTH (* WHEEL-DISTANCE 20))
(define ROAD-HEIGHT (* WHEEL-DISTANCE 2))
(define Y-CAR (* WHEEL-RADIUS 2))
(define CAR-LENGTH (* WHEEL-DISTANCE 4))

;graphical constants
(define WHEEL
  (circle WHEEL-RADIUS "solid" "black"))

(define SPACE
  (rectangle WHEEL-DISTANCE WHEEL-RADIUS "solid" "white"))

(define CHASSIS (above 
  (rectangle (* WHEEL-DISTANCE 2) WHEEL-RADIUS  "solid" "red")
  (rectangle (* WHEEL-DISTANCE 4) ( * WHEEL-RADIUS 2) "solid" "red")
     )
  )

(define BOTH-WHEELS
  (beside WHEEL SPACE WHEEL))

(define CAR
  (overlay/align/offset "middle" "bottom"
   BOTH-WHEELS
   0 (- WHEEL-RADIUS)
   CHASSIS
   )
  )


(define TREE
  (underlay/xy (circle (* WHEEL-RADIUS 1) "solid" "green")
               (* WHEEL-RADIUS 0.9) (* WHEEL-RADIUS 1.3)
               (rectangle (/ WHEEL-RADIUS 4) (* WHEEL-RADIUS 2.3) "solid" "brown")))




(define BACKGROUND (empty-scene ROAD-LENGTH ROAD-HEIGHT ))
(define ROAD (place-image TREE (/ ROAD-LENGTH 1.5) Y-CAR BACKGROUND))



;FUNCTIONS

; WorldState -> Image
; places the image of the car x pixels from 
; the left margin of the BACKGROUND image 
(define (render x)
  (place-image/align CAR x Y-CAR "right" "center" ROAD )
  )


(check-expect (render 50) (place-image/align CAR 50 Y-CAR "right" "center" ROAD))
(check-expect (render 100) (place-image/align CAR 100 Y-CAR "right" "center" ROAD))
 
; WorldState -> WorldState
; adds 3 to x to move the car right 
(define (tock x)
  (+ x 3)
  )

(check-expect (tock 0) 3)
(check-expect (tock 3) 6)
(check-expect (tock 9) 12)

;WorldState -> Bool
; checks if cureent position of the car
; less then the length of the road
(define (end x)
  (>= (tock x) (+ ROAD-LENGTH (image-width CAR)))
  )
  

; WorldState -> WorldState
; launches the program from some initial state 
(define (main ws)
   (big-bang ws
     [on-tick tock]
     [to-draw render]
     [stop-when end]
     [close-on-stop #t]
     ))

;(main 0)
     
