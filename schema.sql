create table api_tokens (
    id integer primary key autoincrement,
    secret varchar(32) not null
);
insert into api_tokens (secret) values ('MeowmeowmeowMeowmeowmeowmeowmeow');

create table cat_pictures (
    slug varchar(32) primary key not null,
    url text not null,
    votes integer not null default 0
);

insert into cat_pictures (slug, url) values
('grumpy', 'https://storage.googleapis.com/imgur-for-cats/grumpy.jpg'),
('hover', 'https://storage.googleapis.com/imgur-for-cats/hover.jpg');

insert into cat_pictures (slug, url) values
('grumpy2', 'https://storage.googleapis.com/imgur-for-cats/grumpy.jpg'),
('hover2', 'https://storage.googleapis.com/imgur-for-cats/hover.jpg');
insert into cat_pictures (slug, url) values
('grumpy3', 'https://storage.googleapis.com/imgur-for-cats/grumpy.jpg'),
('hover3', 'https://storage.googleapis.com/imgur-for-cats/hover.jpg');