;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname |exercise 39|) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp")) #f)))
;physical constants 
(define WHEEL-RADIUS 10) ;single point of control
(define WHEEL-DISTANCE (* WHEEL-RADIUS 5))

;graphical constants
(define WHEEL
  (circle WHEEL-RADIUS "solid" "red"))

(define CAR-BODY (rectangle  (* WHEEL-RADIUS 8) (* WHEEL-RADIUS 3) "solid" "blue"))
(define SPACE (rectangle (* WHEEL-RADIUS 3) 0 "solid" "blue"))


(define WHEELS (beside WHEEL SPACE WHEEL))

(define CAR (overlay/align/offset "middle" "bottom"  WHEELS 0 (- WHEEL-RADIUS) CAR-BODY))


CAR