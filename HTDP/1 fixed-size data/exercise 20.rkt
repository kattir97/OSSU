;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname |exercise 20|) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp")) #f)))
(define (string-delete str idx)
  (if (and (>= idx 0)(<= idx (string-length str)))
      (string-append (substring str 0 idx) (substring str ( + idx 1) (string-length str)))
      "Error: index is out of range"
      )
  )

(string-delete "foobar" 5)