

CREATE TABLE Movie(
	title char(20),
	year int,
	imdb float,
	director char(20),
	primary key(title, year),
	check(imdb >= 0 AND imdb<10));
CREATE TABLE Cinema(
	name char(20),
	address char(100),
	primary key(name));

CREATE TABLE Cast(
	title char(20),
	year int,
	actor char(20),
	role char(20),
	foreign key(title,year) references Movie(title,year));

CREATE TABLE Guide(
	theater char(20),
	film char(20),
	year int,
	start int,
	foreign key(film,year) references Movie(title,year));