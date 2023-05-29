;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname |exercise 30|) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp")) #f)))
;constants

(define AVERAGE_TICKET_PRICE 5.00)
(define AVERAGE_ATTENDEES 120)
(define SHOW_COST 180)
(define COST_PER_ATTENDEE 0.04)
(define TICKET_PRICE_CHANGE 0.10)
(define ATTENDEES_CHANGE 15)
(define PRICE_SENSITIVITY (/ ATTENDEES_CHANGE TICKET_PRICE_CHANGE))




(define (attendees ticket-price)
  (- AVERAGE_ATTENDEES (* (- ticket-price AVERAGE_TICKET_PRICE) PRICE_SENSITIVITY)))


(define (revenue ticket-price)
  (* ticket-price (attendees ticket-price)))


(define (cost ticket-price)
  (+ SHOW_COST (* COST_PER_ATTENDEE (attendees ticket-price))))


(define (profit ticket-price)
  (- (revenue ticket-price)
     (cost ticket-price)))


(profit 5)