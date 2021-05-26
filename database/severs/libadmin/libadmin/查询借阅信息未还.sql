SELECT
	a.book_id,(
	SELECT
		book_name 
	FROM
		bookindex 
	WHERE
	isbn = ( SELECT isbn FROM book WHERE book_id = a.book_id )) AS book_name ,
	a.borrow_date,
	(DATE_ADD(now(),INTERVAL a.borrow_period DAY))as return_date,
	(a.borrow_period - DATEDIFF(now(),a.borrow_date)) as left_days,
	a.return_book,
	a.borrow_extend
FROM
	borrow AS a 
WHERE
	a.reader_id = '201700150168' and book_id not in (select book_id from violation) and return_book = 0 ;