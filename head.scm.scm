(define (q)
  (define (ask-gender)
    (display "�������㣬�����е�Ů�ģ�") (newline)
    (read-line))
  
  (define (ask-man)
    (display "�������������е��������㣬������˵�ҵ�ͷ�Ǽ�ģ��������������ǲ���ͺͷ�������ǲ��ǹ�ͷ���������ǹ�ͷ������ͷ���ģ�����") (newline)
    (read-line))
  
  (define (ask-woman)
    (display "�������Ů����˵�����Ļ��������������㣬��������Ů���ӣ��������㣬��������ͷ���ǲ��ǲ��Ǽ�ģ������������㣬��ͷ���Ǽ���أ�����ͺ���ģ��������ǣ�����Ⱦ��ɫȾ��ɫ�ģ��������㣬�������Ǵ��ٷ���?") (newline)
    (read-line))
  
  (define (response)
    (display "��ͷ��������ͷ����ô�ˣ��Ҿͼ���ô�ˣ������Ҿͼ���ô�ˣ��Ҿ�ͷ������ô�ˣ�������ͷ�������ѵ��㿴����ô����ͷ�����Ǽ����ô�ˣ��Ҿ��Ǽ⣬�Ҿ���Ҫ����ô�ˣ������㿴�����𣬰���") (newline))
  
  (define (loop-q)
    (let loop-gender ((a (ask-gender)))
      (cond
        ((or (string=? a "�е�") (string=? a "��"))
         (let loop-man ((c (ask-man)))
           (if (or (string=? c "��ͷ") (string=? c "ͺͷ") (string=? c "��ͷ����"))
               (response)
               (loop-man (ask-man)))))
        ((or (string=? a "Ů��") (string=? a "Ů"))
         (let loop-woman ((b (ask-woman)))
           (if (or (string=? b "���") (string=? b "ͺ��") (string=? b "Ⱦ��ɫ��") 
                   (string=? b "Ⱦ��ɫ��") (string=? b "���ٷ���"))
               (response)
               (loop-woman (ask-woman)))))
        (else (loop-gender (ask-gender))))))

  ;; �ⲿ��������
  (define (main-loop)
    (display "�����ʡ�") (newline)
    (let loop ((input (read-line)))
      (if (not (string-suffix? input "ͷ����ô����"))
          (begin
            (display "��������ʡ�") (newline)
            (loop (read-line)))
          (q))))
  
  ;; ��ʼִ��
  (main-loop))

(q)