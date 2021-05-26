insert into violation ( reader_id, book_id, reason, penalty_amount )
select'201700150168', '2', 'lost', '5' from dual where not EXISTS
(select book_id,reader_id from violation where book_id = '2' and reader_id = '201700150168');