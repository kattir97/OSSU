;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname |excercise 5|) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp")) #f)))
(define BOAT_SIZE 100)

(define left-t (triangle/saa (/ BOAT_SIZE 2) 90 40 "solid" "lightseagreen"))
(define right-t (triangle/asa 90 (/ BOAT_SIZE 2) 40 "solid" "lightseagreen"))
(define rect (rectangle BOAT_SIZE (/ BOAT_SIZE 2) "solid" "lightseagreen"))
(define mast (rectangle (/ BOAT_SIZE 20) (/ BOAT_SIZE 1.1) "solid" "gray"))
(define sail (triangle BOAT_SIZE "solid" "yellow"))

(define sail-on-mast (overlay/offset sail 0 (/ BOAT_SIZE 18)  mast))

(above sail-on-mast (beside left-t rect right-t))