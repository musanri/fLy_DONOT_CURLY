SELECT 
	a.isbn,
	a.book_name,
	a.author,
	( SELECT count(*) FROM can_borrow_book WHERE can_borrow_book.isbn = a.isbn ) as left_book,
	borrow_condition
FROM
	bookindex as a
WHERE
	book_type REGEXP '理工';