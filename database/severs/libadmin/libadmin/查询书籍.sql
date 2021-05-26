SELECT
	a.isbn,
	a.book_name,
	a.author,
	( SELECT count(*) FROM can_borrow_book WHERE can_borrow_book.isbn = a.isbn ) as left_book
FROM
	bookindex AS a;