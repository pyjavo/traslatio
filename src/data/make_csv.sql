SELECT Url, title, category, date as created_date, DATE('now') as current_date, view_count 
FROM news 
WHERE printf("%d", view_count) = view_count AND category != '';