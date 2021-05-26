insert into borrow(reader_id,book_id,isbn)
select'201700150168','101',(select isbn from book where book_id = '101') from dual 
where	(select borrow_condition from bookindex where isbn = (select isbn from book where book_id = '101'))
and (select blacklist from reader where reader_id = '201700150168') is false;