;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname |exercise 17|) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp")) #f)))
(define (image-classify img )
  (if ( > (image-height img ) (image-width img))
      "tall"
      (if (> (image-width img) (image-height img))
          "wide"
          "square"
          )
      )
  )


(image-classify (rectangle 5 10 "solid" "gray"))