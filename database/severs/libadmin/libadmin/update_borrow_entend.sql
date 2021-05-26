update borrow 
set borrow_extend = 1 , borrow_period = 40
where reader_id = '".$_POST[reader_id]."' and book_id = '".$_POST[book_id]."' and return_book = 0;