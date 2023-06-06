;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname |exercise 38|) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp")) #f)))
; String -> String
; return given string without last charachter
; given: "chair"
; expected: "chai"

(define (string-remove-last str)
  (substring str 0 (- (string-length str) 1)
  ))

(string-remove-last "chair")