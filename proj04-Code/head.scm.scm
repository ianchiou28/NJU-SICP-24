(define (q)
  (define (ask-gender)
    (display "那我问你，你是男的女的？") (newline)
    (read-line))
  
  (define (ask-man)
    (display "如果是如果你是男的那我问你，啊，你说我的头是尖的，那我问你那你是不是秃头？那你是不是光头？啊？你是光头还是有头发的，啊？") (newline)
    (read-line))
  
  (define (ask-woman)
    (display "如果你是女的你说这样的话，啊，那我问你，你你你是女孩子，那我问你，那那你那头顶是不是不是尖的？那我那我问你，你头顶是尖的呢？还是秃顶的，啊，还是，啊，染黄色染红色的，那我问你，啊，还是戴假发的?") (newline)
    (read-line))
  
  (define (response)
    (display "我头顶，我我头尖怎么了？我就尖怎么了？哎，我就尖怎么了？我就头顶尖怎么了？哎，我头顶尖你难道你看不惯么？我头顶就是尖的怎么了？我就是尖，我就是要尖怎么了，啊，你看不惯吗，啊。") (newline))
  
  (define (loop-q)
    (let loop-gender ((a (ask-gender)))
      (cond
        ((or (string=? a "男的") (string=? a "男"))
         (let loop-man ((c (ask-man)))
           (if (or (string=? c "光头") (string=? c "秃头") (string=? c "有头发的"))
               (response)
               (loop-man (ask-man)))))
        ((or (string=? a "女的") (string=? a "女"))
         (let loop-woman ((b (ask-woman)))
           (if (or (string=? b "尖的") (string=? b "秃顶") (string=? b "染黄色的") 
                   (string=? b "染红色的") (string=? b "戴假发的"))
               (response)
               (loop-woman (ask-woman)))))
        (else (loop-gender (ask-gender))))))

  ;; 外部交互部分
  (define (main-loop)
    (display "请提问。") (newline)
    (let loop ((input (read-line)))
      (if (not (string-suffix? input "头顶怎么尖尖的"))
          (begin
            (display "请继续提问。") (newline)
            (loop (read-line)))
          (q))))
  
  ;; 开始执行
  (main-loop))

(q)