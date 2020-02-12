# Models/DB Fields

## Book
id: int
reader: int (foreign key)
rating_avg: int
title: str
author: str
genre: str
notes: text
has_read: bool [true]
add_date: date
cover_img: str

## Reader
id: int
name: str
profile_img: str
bio: test
is_top: bool [0]
join_date: date

## Rating
id: int
user_id: int (foreign key)
book: int
book_id: int
rating: int