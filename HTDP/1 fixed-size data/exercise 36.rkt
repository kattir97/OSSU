;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname |exercise 36|) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp")) #f)))
; Image -> Number
; calculates an area of given image
; given: (rectangle 10 20 "solid" "black")
; expected: 200

(define (image-area img)
  (* (image-width img) (image-height img))
  )

(image-area (rectangle 10 20 "solid" "black"))