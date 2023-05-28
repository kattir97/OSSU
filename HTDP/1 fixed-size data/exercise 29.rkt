;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname |exercise 29|) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp")) #f)))
;constants

(define AVERAGE_TICKET_PRICE 5.00)
(define AVERAGE_ATTENDEES 120)
(define COST_PER_ATTENDEE 1.50)
(define TICKET_PRICE_CHANGE 0.10)
(define ATTENDEES_CHANGE 15)




(define (attendees ticket-price)
  (- AVERAGE_ATTENDEES (* (- ticket-price AVERAGE_TICKET_PRICE) (/ ATTENDEES_CHANGE TICKET_PRICE_CHANGE))))


(define (revenue ticket-price)
  (* ticket-price (attendees ticket-price)))


(define (cost ticket-price)
   (* COST_PER_ATTENDEE (attendees ticket-price)))


(define (profit ticket-price)
  (- (revenue ticket-price)
     (cost ticket-price)))

(profit 1)
(profit 2)
(profit 3)
(profit 4)
(profit 5)


(define (profit.v2 price)
  (- (* (+ 120
           (* (/ 15 0.1)
              (- 5.0 price)))
        price)
     
        (* 1.50
           (+ 120
              (* (/ 15 0.1)
                 (- 5.0 price))))))

(profit.v2 1)
(profit.v2 2)
(profit.v2 3)
(profit.v2 4)
(profit.v2 5)
