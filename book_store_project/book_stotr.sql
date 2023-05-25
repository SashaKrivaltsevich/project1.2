PRAGMA foreign_keys = ON;
CREATE TABLE profiles(
    profile_id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    password TEXT NOT NULL,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    update_at NUMERIC DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE users(
    users_id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    username TEXT UNIQUE NOT NULL,
    age INTEGER CHECK (age > 0),
    profile_id INTEGER UNIQUE,
    FOREIGN KEY (profile_id) REFERENCES profiles (profile_id) ON DELETE CASCADE
);
CREATE TABLE roles (
    roles_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT  UNIQUE NOT NULL,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    update_at NUMERIC DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE users_roles (
    user_id INTEGER,
    role_id INTEGER,
    PRIMARY KEY (user_id, role_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (role_id) REFERENCES roles(role_id) ON DELETE CASCADE
);
CREATE TABLE permissions (
    permission_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    update_at NUMERIC DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE roles_permissions (
    role_id INTEGER,
    permission_id INTEGER,
    PRIMARY KEY (role_id, permission_id),
    FOREIGN KEY (role_id) REFERENCES roles(role_id) ON DELETE CASCADE,
    FOREIGN KEY (permission_id) REFERENCES permissions(permission_id) ON DELETE CASCADE
);
);
CREATE TABLE books (
    books_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    price REAL CHECK (price > 0),
    description TEXT,
    pages INTEGER,
    format TEXT,
    age_restriction INTEGER,
    quantity INTEGER,
    added_date NUMERIC DEFAULT CURRENT_TIMESTAMP,
    last_update NUMERIC DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE genres (
    genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    description TEXT,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    update_at NUMERIC DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE books_genres (
    book_id INTEGER,
    genre_id INTEGER,
    PRIMARY KEY (book_id, genre_id),
    FOREIGN KEY (book_id) REFERENCES books (book_id),
    FOREIGN KEY (genre_id) REFERENCES genres (genre_id)
);
CREATE TABLE authors (
    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT,
    lastname TEXT UNIQUE NOT NULL,
    date_of_birth NUMERIC ,
    date_of_death NUMERIC,
    info TEXT,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    update_at NUMERIC DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE books_authors (
    book_id INTEGER,
    author_id INTEGER,
    PRIMARY KEY (book_id, author_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE,
    FOREIGN KEY (author_id) REFERENCES authors(author_id) ON DELETE CASCADE
);
CREATE TABLE baskets (
    basket_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    update_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    basket_status TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
);
CREATE TABLE books_baskets (
    book_id INTEGER,
    basket_id INTEGER,
    PRIMARY KEY (book_id, basket_id),
    FOREIGN KEY (book_id) REFERENCES books (book_id),
    FOREIGN KEY (basket_id) REFERENCES baskets (basket_id)
);
CREATE TABLE bank_cards (
    card_id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    cvc INTEGER,
    expiration_month_year TEXT,
    user_id INTEGER,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    update_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
CREATE TABLE transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    basket_id INTEGER,
    card_id INTEGER,
    final_amount REAL,
    delivery_address TEXT,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    update_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (basket_id) REFERENCES baskets (baskets_id) ON DELETE CASCADE,
    FOREIGN KEY (bank_card_id) REFERENCES bank_cards (card_id)On DELETE CASCADE

);
CREATE TABLE countries (
    country_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
);
CREATE TABLE cities (
    city_idid INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    country_id INTEGER,
    FOREIGN KEY (country_id) REFERENCES countries (countries_id) ON DELETE CASCADE
);
CREATE TABLE addresses (
    address_id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_id INTEGER,
    city_id INTEGER,
    street TEXT,
    house_number TEXT,
    user_id INTEGER,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    update_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (country_id) REFERENCES countries (country_id),
    FOREIGN KEY (city_id) REFERENCES cities (city_id),
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);