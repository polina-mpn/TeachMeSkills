"""
📋 Чего должен добиться студент:
	1.	Подключиться к PostgreSQL через psycopg2.
	2.	Создать таблицу wishes, если её нет.
	3.	Реализовать вставку новых пожеланий через POST.
	4.	Реализовать выборку всех пожеланий и передать их в шаблон.
	5.	(По желанию) Добавить новую страницу или кнопки — например, очистка списка.

⸻

🧠 Можно добавить вопросы:
	•	Что произойдёт, если не делать conn.commit()?
	•	Как бы вы защитили форму от спама?
	•	Что можно было бы вынести в отдельные функции?
"""

from flask import Flask, render_template_string, request, redirect
import psycopg2


app = Flask(__name__)

# TODO: настрой подключение к PostgreSQL
conn = psycopg2.connect(
    dbname="notes",
    user="postgres",
    password="postgres",
    host="127.0.0.1",
    port="5432"
)

cur = conn.cursor()

# TODO: создай таблицу wishes (если не существует):
# Поля: id (serial), name (text), message (text)
create_table_query = """
CREATE TABLE IF NOT EXISTS wishes (
    id SERIAL PRIMARY KEY,
    name TEXT,
    message TEXT
);
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # TODO: Получи name и message из формы
        name = request.form.get("name", "").strip()
        message = request.form.get("message", "").strip()
        # TODO: Сохрани их в базу данных
        cur.execute(
            "INSERT INTO wishes (name, message) VALUES (%s, %s)",
            (name, message)
        )
        # TODO: Не забудь коммит
        conn.commit()
        return redirect("/")

    # TODO: Получи список пожеланий из базы (от новых к старым)
    cur.execute(
        "SELECT name, message FROM wishes ORDER BY id DESC"
    )
    wishes = cur.fetchall()

    # TODO: Верни шаблон с wishes
    return render_template_string(TEMPLATE, wishes=wishes)


# HTML-шаблон (можно доработать при желании)
TEMPLATE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Книга пожеланий</title>
</head>
<body>
    <h1>Книга пожеланий 💌</h1>

    <form method="post">
        <p><input type="text" name="name" placeholder="Ваше имя" required></p>
        <p><textarea name="message" placeholder="Ваше пожелание" required></textarea></p>
        <p><button type="submit">Оставить пожелание</button></p>
    </form>

    <h2>Все пожелания:</h2>
    {% for name, message in wishes %}
        <div style="border:1px solid #ccc; margin:10px; padding:10px;">
            <strong>{{ name }}</strong><br>
            <em>{{ message }}</em>
        </div>
    {% endfor %}
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)