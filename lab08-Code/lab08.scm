;;; Lab08: Scheme

(define (over-or-under a b)
  (cond ((> a b) 1) ((= a b) 0) ((< a b) -1))
)


(define (make-adder n)
  (lambda (x) (+ n x))
)


(define (composed f g)
  (lambda (x) (f (g x)))
)


(define (remainder a b)
  (- a (* b (quotient a b))))

(define (gcd a b)
  (if (= b 0) a (gcd b (remainder a b)))
)


(define lst
  '((1) 2 (3 4) 5)
)


(define (ordered s)
  (define carr (lambda (x) (car (cdr x))))
  (define (helper lst)
    (cond ((null? (cdr lst)) #t)
          ((<= (car lst) (carr lst)) (helper (cdr lst))) (else #f)))
  (helper s))
