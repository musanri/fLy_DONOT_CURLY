SELECT
	a.reader_id,
	
		DATEDIFF(now(), (
		SELECT
			borrow_date 
		FROM
			borrow 
		WHERE
			reader_id = a.reader_id 
			AND book_id = a.book_id
		and borrow_date = a.borrow_date	
		)) as period,
	a.book_id,
	a.borrow_date
	
FROM
		borrow as a
WHERE
	a.return_book = 0 and a.book_id not in (select book_id from violation);