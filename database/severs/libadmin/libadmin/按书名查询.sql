SELECT a.book_name, a.isbn, author,( SELECT count(*) FROM can_borrow_book WHERE can_borrow_book.isbn = a.isbn ) AS left_book,
a.intro 
FROM
	bookindex AS a 
WHERE
	a.book_name REGEXP '物理';